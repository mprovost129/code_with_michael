import json
from datetime import timedelta
from unittest.mock import patch

import stripe
from django.contrib.auth import get_user_model
from django.core import mail
from django.core.cache import cache
from django.test import Client, TestCase, override_settings
from django.urls import reverse
from django.utils import timezone

from core.models import (
    Challenge,
    CommunityPost,
    EmailOnboardingDelivery,
    EmailSubscriber,
    EngagementEvent,
    Lesson,
    Module,
    PremiumPurchase,
    Project,
    Resource,
    UserChallengeProgress,
    UserLessonProgress,
)
from core.services import build_shuffled_quiz, get_streak_and_badges, search_content

# Real reCAPTCHA credentials may be present in .env once the site is wired
# up to Google Cloud, so tests that aren't about reCAPTCHA behavior must not
# rely on it being unconfigured by ambient environment state. Force it off
# explicitly wherever a test's outcome would otherwise depend on whichever
# secrets happen to be in .env at test-run time.
RECAPTCHA_DISABLED_SETTINGS = {
    'RECAPTCHA_SITE_KEY': '',
    'RECAPTCHA_SECRET_KEY': '',
}


class EngagementEventCreateViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.module = Module.objects.create(
            number=1,
            slug='first-steps',
            title='First Steps',
            duration='10 min',
            goal='Learn the basics.',
            topics=['print()'],
            is_published=True,
        )
        self.lesson = Lesson.objects.create(
            module=self.module,
            slug='print-basics',
            title='Print Basics',
            summary='Learn print.',
            duration='8 min',
            goal='Use print().',
            explanation='Explain print.',
            starter_code='print("Hello")',
            try_it='Change the text.',
            common_mistake='Missing quote.',
            mini_challenge='Add one line.',
            expected_output='Hello',
            practice_challenge_slug='warm-up-greeting',
            quiz=[],
            is_published=True,
            display_order=1,
        )

    def test_creates_anonymous_engagement_event(self):
        response = self.client.post(
            reverse('core:engagement_event_create'),
            data=json.dumps({
                'event_type': EngagementEvent.EVENT_CODE_RUN,
                'page_path': '/lessons/print-basics/',
                'lesson_slug': self.lesson.slug,
                'metadata': {'status': 'success'},
            }),
            content_type='application/json',
        )

        self.assertEqual(response.status_code, 200)
        event = EngagementEvent.objects.get()
        self.assertEqual(event.event_type, EngagementEvent.EVENT_CODE_RUN)
        self.assertEqual(event.lesson, self.lesson)
        self.assertEqual(event.page_path, '/lessons/print-basics/')
        self.assertEqual(event.metadata['status'], 'success')
        self.assertTrue(event.session_key)

    def test_rejects_unknown_event_type(self):
        response = self.client.post(
            reverse('core:engagement_event_create'),
            data=json.dumps({'event_type': 'unknown'}),
            content_type='application/json',
        )

        self.assertEqual(response.status_code, 400)
        self.assertFalse(EngagementEvent.objects.exists())

    def test_explicit_null_page_path_does_not_crash(self):
        response = self.client.post(
            reverse('core:engagement_event_create'),
            data=json.dumps({
                'event_type': EngagementEvent.EVENT_PAGE_VIEW,
                'page_path': None,
                'metadata': {},
            }),
            content_type='application/json',
        )

        self.assertEqual(response.status_code, 200)
        event = EngagementEvent.objects.get()
        self.assertEqual(event.page_path, '')

    def test_creates_affiliate_click_event_with_resource_metadata(self):
        response = self.client.post(
            reverse('core:engagement_event_create'),
            data=json.dumps({
                'event_type': EngagementEvent.EVENT_AFFILIATE_CLICK,
                'page_path': '/resources/',
                'metadata': {
                    'resource_id': 1,
                    'resource_title': 'Python Crash Course',
                    'category': 'amazon',
                    'link_type': 'buy',
                },
            }),
            content_type='application/json',
        )

        self.assertEqual(response.status_code, 200)
        event = EngagementEvent.objects.get()
        self.assertEqual(event.event_type, EngagementEvent.EVENT_AFFILIATE_CLICK)
        self.assertEqual(event.metadata['resource_title'], 'Python Crash Course')
        self.assertEqual(event.metadata['link_type'], 'buy')

    def test_endpoint_is_csrf_exempt_for_sendbeacon_tracking(self):
        # sendBeacon cannot attach custom headers, so the CSRF token can't be
        # sent as X-CSRFToken. This endpoint must stay CSRF-exempt or
        # same-tab CTA click tracking silently breaks.
        strict_client = Client(enforce_csrf_checks=True)

        response = strict_client.post(
            reverse('core:engagement_event_create'),
            data=json.dumps({
                'event_type': EngagementEvent.EVENT_AFFILIATE_CLICK,
                'metadata': {'link_type': 'shop_cta', 'source': 'navbar'},
            }),
            content_type='application/json',
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(EngagementEvent.objects.filter(event_type=EngagementEvent.EVENT_AFFILIATE_CLICK).exists())

    @patch('core.views.check_rate_limit', return_value=True)
    def test_rate_limited_requests_are_rejected(self, mock_check_rate_limit):
        response = self.client.post(
            reverse('core:engagement_event_create'),
            data=json.dumps({'event_type': EngagementEvent.EVENT_PAGE_VIEW}),
            content_type='application/json',
        )

        self.assertEqual(response.status_code, 429)
        self.assertFalse(EngagementEvent.objects.exists())
        mock_check_rate_limit.assert_called_once_with(response.wsgi_request, 'engagement_event', limit=300, window_seconds=3600)


@override_settings(**RECAPTCHA_DISABLED_SETTINGS, MARKETING_CONTACT_EMAIL='')
class HomeEmailSubscriberTests(TestCase):
    def test_homepage_creates_email_subscriber(self):
        response = self.client.post(
            reverse('core:home'),
            data={
                'email': 'futurestudent@example.com',
                'first_name': 'Future',
            },
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            EmailSubscriber.objects.filter(
                email='futurestudent@example.com',
                first_name='Future',
            ).exists()
        )
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].to, ['futurestudent@example.com'])
        self.assertTrue(
            EmailOnboardingDelivery.objects.filter(
                email='futurestudent@example.com',
                step=EmailOnboardingDelivery.STEP_SUBSCRIBER_WELCOME,
            ).exists()
        )

    def test_homepage_handles_duplicate_email_subscriber(self):
        EmailSubscriber.objects.create(email='futurestudent@example.com', first_name='Future')

        response = self.client.post(
            reverse('core:home'),
            data={
                'email': 'futurestudent@example.com',
                'first_name': 'Future',
            },
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            EmailSubscriber.objects.filter(email='futurestudent@example.com').count(),
            1,
        )
        self.assertEqual(len(mail.outbox), 0)

    def test_new_subscriber_notifies_marketing_contact_when_configured(self):
        with override_settings(MARKETING_CONTACT_EMAIL='owner@example.com'):
            self.client.post(
                reverse('core:home'),
                data={'email': 'futurestudent@example.com', 'first_name': 'Future'},
            )

        self.assertEqual(len(mail.outbox), 2)
        notification = next(m for m in mail.outbox if m.to == ['owner@example.com'])
        self.assertIn('futurestudent@example.com', notification.body)

    def test_new_subscriber_skips_marketing_notification_when_not_configured(self):
        self.client.post(
            reverse('core:home'),
            data={'email': 'futurestudent@example.com', 'first_name': 'Future'},
        )

        self.assertEqual(len(mail.outbox), 1)

    def test_footer_signup_from_a_non_home_page_creates_subscriber_with_footer_source(self):
        response = self.client.post(
            reverse('core:home'),
            data={'email': 'footerstudent@example.com', 'source': 'footer'},
            follow=True,
            HTTP_REFERER='http://testserver/lessons/',
        )

        self.assertEqual(response.status_code, 200)
        subscriber = EmailSubscriber.objects.get(email='footerstudent@example.com')
        self.assertEqual(subscriber.source, 'footer')

    def test_homepage_signup_without_source_defaults_to_homepage(self):
        self.client.post(
            reverse('core:home'),
            data={'email': 'homepagestudent@example.com'},
        )

        subscriber = EmailSubscriber.objects.get(email='homepagestudent@example.com')
        self.assertEqual(subscriber.source, 'homepage')

    def test_arbitrary_source_value_is_not_trusted(self):
        self.client.post(
            reverse('core:home'),
            data={'email': 'spoofedsource@example.com', 'source': 'not-a-real-source'},
        )

        subscriber = EmailSubscriber.objects.get(email='spoofedsource@example.com')
        self.assertEqual(subscriber.source, 'homepage')


class InsightsViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user_model = get_user_model()
        self.staff_user = self.user_model.objects.create_user(
            email='staff@example.com',
            password='testpass123',
            is_staff=True,
        )
        self.regular_user = self.user_model.objects.create_user(
            email='user@example.com',
            password='testpass123',
        )
        self.module = Module.objects.create(
            number=1,
            slug='first-steps',
            title='First Steps',
            duration='10 min',
            goal='Learn the basics.',
            topics=['print()'],
            is_published=True,
        )
        self.lesson = Lesson.objects.create(
            module=self.module,
            slug='print-basics',
            title='Print Basics',
            summary='Learn print.',
            duration='8 min',
            goal='Use print().',
            explanation='Explain print.',
            starter_code='print("Hello")',
            try_it='Change the text.',
            common_mistake='Missing quote.',
            mini_challenge='Add one line.',
            expected_output='Hello',
            practice_challenge_slug='warm-up-greeting',
            quiz=[],
            is_published=True,
            display_order=1,
        )
        EngagementEvent.objects.create(
            event_type=EngagementEvent.EVENT_LESSON_VIEW,
            page_path='/lessons/print-basics/',
            lesson=self.lesson,
            session_key='abc123',
            metadata={},
        )
        EngagementEvent.objects.create(
            event_type=EngagementEvent.EVENT_CODE_RUN,
            page_path='/lessons/print-basics/',
            lesson=self.lesson,
            session_key='abc123',
            metadata={'status': 'success'},
        )
        EngagementEvent.objects.create(
            event_type=EngagementEvent.EVENT_CODE_RUN,
            page_path='/lessons/print-basics/',
            lesson=self.lesson,
            session_key='abc123',
            metadata={'status': 'error'},
        )

    def test_insights_requires_login(self):
        response = self.client.get(reverse('core:insights'))

        self.assertEqual(response.status_code, 302)

    def test_insights_blocks_non_staff_users(self):
        self.client.force_login(self.regular_user)
        response = self.client.get(reverse('core:insights'))

        self.assertEqual(response.status_code, 403)

    def test_insights_shows_summary_for_staff(self):
        self.client.force_login(self.staff_user)
        response = self.client.get(reverse('core:insights'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['totals']['lesson_views'], 1)
        self.assertEqual(response.context['totals']['code_runs'], 2)
        self.assertEqual(response.context['totals']['successful_runs'], 1)
        self.assertEqual(response.context['totals']['failed_runs'], 1)
        self.assertEqual(response.context['lesson_breakdown'][0].title, self.lesson.title)

    def test_insights_shows_affiliate_click_breakdown(self):
        EngagementEvent.objects.create(
            event_type=EngagementEvent.EVENT_AFFILIATE_CLICK,
            page_path='/resources/',
            session_key='abc123',
            metadata={'resource_title': 'Python Crash Course', 'link_type': 'buy'},
        )
        EngagementEvent.objects.create(
            event_type=EngagementEvent.EVENT_AFFILIATE_CLICK,
            page_path='/resources/',
            session_key='abc123',
            metadata={'resource_title': 'Python Crash Course', 'link_type': 'details'},
        )
        EngagementEvent.objects.create(
            event_type=EngagementEvent.EVENT_AFFILIATE_CLICK,
            page_path='/',
            session_key='abc123',
            metadata={'link_type': 'shop_cta', 'source': 'navbar'},
        )

        self.client.force_login(self.staff_user)
        response = self.client.get(reverse('core:insights'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['totals']['affiliate_clicks'], 3)
        self.assertEqual(response.context['totals']['shop_cta_clicks'], 1)
        breakdown = response.context['resource_click_breakdown']
        self.assertEqual(len(breakdown), 1)
        self.assertEqual(breakdown[0]['metadata__resource_title'], 'Python Crash Course')
        self.assertEqual(breakdown[0]['clicks'], 2)
        self.assertEqual(breakdown[0]['buy_clicks'], 1)
        self.assertEqual(breakdown[0]['details_clicks'], 1)
        self.assertContains(response, 'Python Crash Course')


class UserLessonProgressTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            email='learner@example.com',
            username='learner_one',
            password='testpass123',
        )
        self.module = Module.objects.create(
            number=1,
            slug='first-steps',
            title='First Steps',
            duration='10 min',
            goal='Learn the basics.',
            topics=['print()'],
            is_published=True,
        )
        self.lesson = Lesson.objects.create(
            module=self.module,
            slug='print-basics',
            title='Print Basics',
            summary='Learn print.',
            duration='8 min',
            goal='Use print().',
            explanation='Explain print.',
            starter_code='print("Hello")',
            try_it='Change the text.',
            common_mistake='Missing quote.',
            mini_challenge='Add one line.',
            expected_output='Hello',
            practice_challenge_slug='warm-up-greeting',
            quiz=[],
            is_published=True,
            display_order=1,
        )
        self.second_lesson = Lesson.objects.create(
            module=self.module,
            slug='variables-basics',
            title='Variables Basics',
            summary='Learn variables.',
            duration='10 min',
            goal='Use variables.',
            explanation='Explain variables.',
            starter_code='name = "Michael"',
            try_it='Change the name.',
            common_mistake='Using a variable before assigning it.',
            mini_challenge='Create two variables.',
            expected_output='Michael',
            practice_challenge_slug='warm-up-greeting',
            quiz=[
                {
                    'question': 'What is a variable?',
                    'options': ['A named place to store a value.', 'A loop.', 'An error message.'],
                    'answer': 0,
                    'explanation': 'Variables store values with names.',
                },
                {
                    'question': 'Which is a valid variable assignment?',
                    'options': ['score = 3', '3 = score', 'print ='],
                    'answer': 0,
                    'explanation': 'Variables are assigned from left to right.',
                },
            ],
            is_published=True,
            display_order=2,
        )
        self.challenge = Challenge.objects.create(
            slug='warm-up-greeting',
            title='Warm-up Greeting',
            difficulty='Beginner',
            prompt='Write two print lines.',
            hint='Use two print calls.',
            starter_code='print("Hello")',
            expected_output='Hello',
            success_checks=['It runs.', 'It prints two lines.'],
            reflection_prompt='What changed?',
            is_published=True,
            display_order=1,
        )

    def test_lesson_view_creates_progress_for_authenticated_user(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('core:lesson_detail', args=[self.lesson.slug]))

        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            UserLessonProgress.objects.filter(user=self.user, lesson=self.lesson).exists()
        )

    def test_mark_complete_updates_progress(self):
        self.client.force_login(self.user)
        response = self.client.post(
            reverse('core:lesson_progress_update', args=[self.lesson.slug]),
            data={'action': 'complete'},
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        progress = UserLessonProgress.objects.get(user=self.user, lesson=self.lesson)
        self.assertTrue(progress.is_completed)
        self.assertIsNotNone(progress.completed_at)

    def test_mark_complete_celebrates_finished_milestone_when_challenge_is_done(self):
        self.client.force_login(self.user)
        UserChallengeProgress.objects.create(
            user=self.user,
            challenge=self.challenge,
            is_completed=True,
            response_text='done',
        )

        response = self.client.post(
            reverse('core:lesson_progress_update', args=[self.lesson.slug]),
            data={'action': 'complete'},
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Milestone 1 complete: Print Basics')

    def test_lesson_detail_includes_next_and_previous_navigation(self):
        self.client.force_login(self.user)

        first_response = self.client.get(reverse('core:lesson_detail', args=[self.lesson.slug]))
        second_response = self.client.get(reverse('core:lesson_detail', args=[self.second_lesson.slug]))

        self.assertEqual(first_response.context['next_lesson'], self.second_lesson)
        self.assertIsNone(first_response.context.get('previous_lesson'))
        self.assertEqual(second_response.context['previous_lesson'], self.lesson)

    def test_lesson_detail_includes_practice_challenge(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse('core:lesson_detail', args=[self.lesson.slug]))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['practice_challenge'], self.challenge)
        self.assertContains(response, 'Practice This Next')
        self.assertContains(response, self.challenge.title)

    def test_lesson_detail_shows_milestone_banner_when_challenge_is_done(self):
        self.client.force_login(self.user)
        UserChallengeProgress.objects.create(
            user=self.user,
            challenge=self.challenge,
            is_completed=True,
            response_text='done',
        )

        response = self.client.get(reverse('core:lesson_detail', args=[self.lesson.slug]))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Milestone Status')
        self.assertContains(response, 'Milestone 1 underway')

    def test_lesson_detail_shows_completion_stack(self):
        self.client.force_login(self.user)
        UserLessonProgress.objects.create(
            user=self.user,
            lesson=self.lesson,
            is_completed=True,
            quiz_passed_at=timezone.now(),
        )

        response = self.client.get(reverse('core:lesson_detail', args=[self.lesson.slug]))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Completion Stack')
        self.assertContains(response, '2 of 3 steps finished')
        self.assertContains(response, 'Paired challenge complete: Warm-up Greeting')
        self.assertContains(response, 'Recommended next action:')
        self.assertContains(response, 'Open Warm-up Greeting next.')

    def test_quiz_submission_updates_saved_scores(self):
        self.client.force_login(self.user)
        response = self.client.post(
            reverse('core:lesson_quiz_submit', args=[self.second_lesson.slug]),
            data={
                'question_0': '0',
                'question_1': '0',
            },
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        progress = UserLessonProgress.objects.get(user=self.user, lesson=self.second_lesson)
        self.assertEqual(progress.quiz_attempts, 1)
        self.assertEqual(progress.last_quiz_score, 100)
        self.assertEqual(progress.best_quiz_score, 100)
        self.assertIsNotNone(progress.quiz_passed_at)

    def test_my_progress_recommends_next_unstarted_lesson(self):
        self.client.force_login(self.user)
        UserLessonProgress.objects.create(
            user=self.user,
            lesson=self.lesson,
            is_completed=True,
        )

        response = self.client.get(reverse('core:my_progress'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['recommended_next_lesson'], self.second_lesson)
        self.assertEqual(response.context['recommended_next_challenge'], self.challenge)
        self.assertEqual(response.context['current_milestone']['lesson'], self.lesson)
        self.assertEqual(response.context['current_milestone']['status'], 'in_progress')

    def test_challenge_notes_can_be_saved(self):
        self.client.force_login(self.user)
        response = self.client.post(
            reverse('core:challenge_progress_update', args=[self.challenge.id]),
            data={
                'action': 'save',
                'response_text': 'print("Hello")\nprint("I am practicing.")',
            },
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        progress = UserChallengeProgress.objects.get(user=self.user, challenge=self.challenge)
        self.assertFalse(progress.is_completed)
        self.assertIn('print("Hello")', progress.response_text)

    def test_challenge_can_be_marked_complete(self):
        self.client.force_login(self.user)
        response = self.client.post(
            reverse('core:challenge_progress_update', args=[self.challenge.id]),
            data={
                'action': 'complete',
                'response_text': 'Finished answer',
            },
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        progress = UserChallengeProgress.objects.get(user=self.user, challenge=self.challenge)
        self.assertTrue(progress.is_completed)
        self.assertIsNotNone(progress.completed_at)

    def test_challenge_complete_celebrates_finished_milestone_when_lesson_is_done(self):
        self.client.force_login(self.user)
        UserLessonProgress.objects.create(
            user=self.user,
            lesson=self.lesson,
            is_completed=True,
        )

        response = self.client.post(
            reverse('core:challenge_progress_update', args=[self.challenge.id]),
            data={
                'action': 'complete',
                'response_text': 'Finished answer',
            },
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Milestone 1 complete: Print Basics')

    def test_my_progress_shows_continue_challenge(self):
        self.client.force_login(self.user)
        UserChallengeProgress.objects.create(
            user=self.user,
            challenge=self.challenge,
            response_text='draft answer',
            is_completed=False,
        )

        response = self.client.get(reverse('core:my_progress'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['continue_challenge'].challenge, self.challenge)

    def test_challenge_detail_shows_saved_response(self):
        self.client.force_login(self.user)
        UserChallengeProgress.objects.create(
            user=self.user,
            challenge=self.challenge,
            response_text='print("Saved draft")',
            is_completed=False,
        )

        response = self.client.get(reverse('core:challenge_detail', args=[self.challenge.slug]))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['challenge'], self.challenge)
        self.assertContains(response, 'Saved draft')

    def test_challenge_detail_shows_milestone_banner_when_lesson_is_done(self):
        self.client.force_login(self.user)
        UserLessonProgress.objects.create(
            user=self.user,
            lesson=self.lesson,
            is_completed=True,
        )

        response = self.client.get(reverse('core:challenge_detail', args=[self.challenge.slug]))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Milestone Status')
        self.assertContains(response, 'Milestone 1 underway')

    def test_challenge_detail_shows_completion_stack(self):
        self.client.force_login(self.user)
        UserLessonProgress.objects.create(
            user=self.user,
            lesson=self.lesson,
            is_completed=True,
        )
        UserChallengeProgress.objects.create(
            user=self.user,
            challenge=self.challenge,
            is_completed=True,
            response_text='done',
        )

        response = self.client.get(reverse('core:challenge_detail', args=[self.challenge.slug]))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Completion Stack')
        self.assertContains(response, '1 of 3 steps finished')
        self.assertContains(response, 'Milestone fully complete')
        self.assertContains(response, 'Recommended next action:')
        self.assertContains(response, 'Finish Variables Basics next.')

    def test_challenge_progress_redirects_back_to_detail_when_requested(self):
        self.client.force_login(self.user)

        response = self.client.post(
            reverse('core:challenge_progress_update', args=[self.challenge.id]),
            data={
                'action': 'save',
                'response_text': 'print("Keep working")',
                'next': reverse('core:challenge_detail', args=[self.challenge.slug]),
            },
        )

        self.assertRedirects(response, reverse('core:challenge_detail', args=[self.challenge.slug]))

    def test_challenge_progress_rejects_offsite_next_redirect(self):
        self.client.force_login(self.user)

        response = self.client.post(
            reverse('core:challenge_progress_update', args=[self.challenge.id]),
            data={
                'action': 'save',
                'response_text': 'print("Keep working")',
                'next': 'https://evil.example.com/phishing',
            },
        )

        self.assertRedirects(response, reverse('core:challenges'))

    def test_challenge_autosave_updates_response_text(self):
        self.client.force_login(self.user)

        response = self.client.post(
            reverse('core:challenge_autosave', args=[self.challenge.id]),
            data=json.dumps({'response_text': 'print("Autosaved draft")'}),
            content_type='application/json',
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['ok'], True)
        progress = UserChallengeProgress.objects.get(user=self.user, challenge=self.challenge)
        self.assertEqual(progress.response_text, 'print("Autosaved draft")')

    def test_challenge_detail_uses_single_editor_field(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse('core:challenge_detail', args=[self.challenge.slug]))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'data-challenge-autosave-form')
        self.assertContains(response, 'name="response_text"', count=1)

    def test_challenge_detail_shows_success_checks_and_reflection(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse('core:challenge_detail', args=[self.challenge.slug]))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'You are ready to move on when:')
        self.assertContains(response, 'It prints two lines.')
        self.assertContains(response, 'Quick reflection:')
        self.assertContains(response, 'What changed?')

    def test_lessons_page_includes_paired_challenge_card(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse('core:lessons'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Practice next: Warm-up Greeting')
        self.assertContains(response, 'Open Paired Challenge')

    def test_my_progress_includes_continue_lesson_challenge(self):
        self.client.force_login(self.user)
        UserLessonProgress.objects.create(
            user=self.user,
            lesson=self.lesson,
            is_completed=False,
        )

        response = self.client.get(reverse('core:my_progress'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['continue_lesson_challenge'], self.challenge)
        self.assertContains(response, 'Open Linked Challenge')

    def test_my_progress_builds_completed_milestone(self):
        self.client.force_login(self.user)
        UserLessonProgress.objects.create(
            user=self.user,
            lesson=self.lesson,
            is_completed=True,
        )
        UserChallengeProgress.objects.create(
            user=self.user,
            challenge=self.challenge,
            is_completed=True,
            response_text='finished',
        )

        response = self.client.get(reverse('core:my_progress'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['completed_milestones'], 1)
        self.assertEqual(response.context['path_milestones'][0]['status'], 'completed')
        self.assertEqual(response.context['latest_completed_milestone']['celebration'], 'Milestone 1 complete: Print Basics')
        self.assertContains(response, 'Milestone 1')
        self.assertContains(response, 'Completed lesson and paired challenge')
        self.assertContains(response, 'Latest Win')
        self.assertContains(response, 'Milestone 1 complete: Print Basics')

    def test_my_progress_shows_underway_copy_for_current_milestone(self):
        self.client.force_login(self.user)
        UserLessonProgress.objects.create(
            user=self.user,
            lesson=self.lesson,
            is_completed=True,
        )

        response = self.client.get(reverse('core:my_progress'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['latest_completed_milestone'], None)
        self.assertContains(response, 'Milestone 1 underway')

    def test_my_progress_requires_login(self):
        response = self.client.get(reverse('core:my_progress'))

        self.assertEqual(response.status_code, 302)

    def test_my_progress_does_not_leak_other_users_data(self):
        other_user = get_user_model().objects.create_user(
            email='other-learner@example.com',
            username='other_learner',
            password='testpass123',
        )
        UserLessonProgress.objects.create(
            user=other_user,
            lesson=self.lesson,
            is_completed=True,
            quiz_passed_at=timezone.now(),
        )
        UserChallengeProgress.objects.create(
            user=other_user,
            challenge=self.challenge,
            is_completed=True,
            response_text="other user's private notes",
        )

        self.client.force_login(self.user)
        response = self.client.get(reverse('core:my_progress'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['completed_lessons'], 0)
        self.assertEqual(response.context['completed_challenges'], 0)
        self.assertNotContains(response, "other user's private notes")

    def test_marking_complete_does_not_alter_another_users_progress(self):
        other_user = get_user_model().objects.create_user(
            email='other-learner@example.com',
            username='other_learner',
            password='testpass123',
        )
        other_progress = UserLessonProgress.objects.create(
            user=other_user,
            lesson=self.lesson,
            is_completed=False,
        )

        self.client.force_login(self.user)
        self.client.post(
            reverse('core:lesson_progress_update', args=[self.lesson.slug]),
            data={'action': 'complete'},
            follow=True,
        )

        other_progress.refresh_from_db()
        self.assertFalse(other_progress.is_completed)
        my_progress = UserLessonProgress.objects.get(user=self.user, lesson=self.lesson)
        self.assertTrue(my_progress.is_completed)

    def test_challenge_autosave_does_not_alter_another_users_progress(self):
        other_user = get_user_model().objects.create_user(
            email='other-learner@example.com',
            username='other_learner',
            password='testpass123',
        )
        other_progress = UserChallengeProgress.objects.create(
            user=other_user,
            challenge=self.challenge,
            response_text="other user's original notes",
        )

        self.client.force_login(self.user)
        self.client.post(
            reverse('core:challenge_autosave', args=[self.challenge.id]),
            data=json.dumps({'response_text': "attacker's overwrite attempt"}),
            content_type='application/json',
        )

        other_progress.refresh_from_db()
        self.assertEqual(other_progress.response_text, "other user's original notes")
        my_progress = UserChallengeProgress.objects.get(user=self.user, challenge=self.challenge)
        self.assertEqual(my_progress.response_text, "attacker's overwrite attempt")


class CommunityPostFeatureTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            email='learner@example.com',
            username='learner_one',
            password='testpass123',
        )

    def test_anonymous_visitor_sees_signup_cta_instead_of_form(self):
        response = self.client.get(reverse('core:community'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Create a free account')
        self.assertNotContains(response, 'Post to Community')

    def test_anonymous_post_is_rejected(self):
        response = self.client.post(
            reverse('core:community'),
            data={'post_type': CommunityPost.TYPE_SHOUTOUT, 'body': 'Anonymous spam'},
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertFalse(CommunityPost.objects.exists())

    def test_authenticated_user_can_submit_a_post(self):
        self.client.force_login(self.user)

        response = self.client.post(
            reverse('core:community'),
            data={'post_type': CommunityPost.TYPE_QUESTION, 'body': 'Why does print() need parentheses?'},
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        post = CommunityPost.objects.get()
        self.assertEqual(post.user, self.user)
        self.assertEqual(post.body, 'Why does print() need parentheses?')
        self.assertFalse(post.is_approved)

    def test_invalid_submission_rerenders_form_with_errors(self):
        self.client.force_login(self.user)

        response = self.client.post(
            reverse('core:community'),
            data={'post_type': CommunityPost.TYPE_SHOUTOUT, 'body': ''},
        )

        self.assertEqual(response.status_code, 200)
        self.assertFalse(CommunityPost.objects.exists())
        self.assertTrue(response.context['community_post_form'].errors)

    def test_unapproved_post_is_hidden_from_public_feed(self):
        CommunityPost.objects.create(
            user=self.user,
            post_type=CommunityPost.TYPE_SHOUTOUT,
            body='Not approved yet',
            is_approved=False,
        )

        response = self.client.get(reverse('core:community'))

        self.assertNotContains(response, 'Not approved yet')

    def test_approved_post_appears_in_public_feed(self):
        CommunityPost.objects.create(
            user=self.user,
            post_type=CommunityPost.TYPE_SHOUTOUT,
            body='Finished my first challenge!',
            is_approved=True,
        )

        response = self.client.get(reverse('core:community'))

        self.assertContains(response, 'Finished my first challenge!')

    def test_rate_limit_blocks_after_threshold(self):
        self.client.force_login(self.user)

        for _ in range(5):
            response = self.client.post(
                reverse('core:community'),
                data={'post_type': CommunityPost.TYPE_SHOUTOUT, 'body': 'Another shoutout'},
                follow=True,
            )
            self.assertEqual(response.status_code, 200)

        self.assertEqual(CommunityPost.objects.count(), 5)

        response = self.client.post(
            reverse('core:community'),
            data={'post_type': CommunityPost.TYPE_SHOUTOUT, 'body': 'One too many'},
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(CommunityPost.objects.count(), 5)
        self.assertContains(response, 'posted a lot')


class SearchFeatureTests(TestCase):
    def setUp(self):
        self.module = Module.objects.create(
            number=1,
            slug='first-steps',
            title='First Steps',
            duration='10 min',
            goal='Learn the basics.',
            topics=['print()'],
            is_published=True,
        )
        self.lesson = Lesson.objects.create(
            module=self.module,
            slug='print-basics',
            title='Your First Python Output',
            summary='Run print() for the first time.',
            duration='8 min',
            goal='Use print().',
            explanation='Explain print.',
            starter_code='print("Hello")',
            try_it='Change the text.',
            common_mistake='Missing quote.',
            mini_challenge='Add one line.',
            expected_output='Hello',
            practice_challenge_slug='',
            quiz=[],
            is_published=True,
            display_order=1,
        )
        self.challenge = Challenge.objects.create(
            slug='warm-up-greeting',
            title='Warm-up Greeting',
            difficulty='Beginner',
            prompt='Write two loops that print a greeting.',
            hint='Use two print calls.',
            starter_code='print("Hello")',
            expected_output='Hello',
            success_checks=[],
            reflection_prompt='',
            is_published=True,
            display_order=1,
        )
        self.project = Project.objects.create(
            title='Budget Tracker',
            description='Store categories in variables or lists and summarize spending.',
            is_published=True,
            display_order=1,
        )

    def test_search_matches_lesson_by_title(self):
        results = search_content('python output')

        self.assertIn(self.lesson, results['lessons'])

    def test_search_matches_challenge_by_prompt(self):
        results = search_content('loops that print')

        self.assertIn(self.challenge, results['challenges'])

    def test_search_matches_project_by_description(self):
        results = search_content('summarize spending')

        self.assertIn(self.project, results['projects'])

    def test_search_is_case_insensitive(self):
        results = search_content('PYTHON OUTPUT')

        self.assertIn(self.lesson, results['lessons'])

    def test_empty_query_returns_no_results(self):
        results = search_content('')

        self.assertEqual(results, {'lessons': [], 'challenges': [], 'projects': []})

    def test_search_view_renders_result_count(self):
        response = self.client.get(reverse('core:search'), {'q': 'python output'})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Your First Python Output')

    def test_search_view_shows_no_results_message(self):
        response = self.client.get(reverse('core:search'), {'q': 'zzz_nonexistent_topic_zzz'})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No results for')


class StreakAndBadgeTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email='learner@example.com',
            username='learner_one',
            password='testpass123',
        )
        self.module = Module.objects.create(
            number=1,
            slug='first-steps',
            title='First Steps',
            duration='10 min',
            goal='Learn the basics.',
            topics=['print()'],
            is_published=True,
        )
        self.lesson = Lesson.objects.create(
            module=self.module,
            slug='print-basics',
            title='Print Basics',
            summary='Learn print.',
            duration='8 min',
            goal='Use print().',
            explanation='Explain print.',
            starter_code='print("Hello")',
            try_it='Change the text.',
            common_mistake='Missing quote.',
            mini_challenge='Add one line.',
            expected_output='Hello',
            practice_challenge_slug='',
            quiz=[],
            is_published=True,
            display_order=1,
        )

    def test_no_activity_has_zero_streak_and_no_badges(self):
        result = get_streak_and_badges(self.user)

        self.assertEqual(result['current_streak'], 0)
        self.assertEqual(result['longest_streak'], 0)
        self.assertEqual(result['earned_badge_count'], 0)

    def test_completing_a_lesson_today_earns_first_lesson_badge(self):
        Lesson.objects.create(
            module=self.module,
            slug='second-lesson',
            title='Second Lesson',
            summary='Practice more.',
            duration='5 min',
            goal='Practice.',
            explanation='Practice.',
            starter_code='print(2)',
            try_it='Try it.',
            common_mistake='None.',
            mini_challenge='None.',
            expected_output='2',
            practice_challenge_slug='',
            quiz=[],
            is_published=True,
            display_order=2,
        )
        UserLessonProgress.objects.create(
            user=self.user,
            lesson=self.lesson,
            is_completed=True,
            completed_at=timezone.now(),
        )

        result = get_streak_and_badges(self.user)

        self.assertEqual(result['current_streak'], 1)
        badge_map = {badge['key']: badge['earned'] for badge in result['badges']}
        self.assertTrue(badge_map['first_lesson'])
        self.assertFalse(badge_map['all_lessons'])

    def test_three_consecutive_days_earns_three_day_streak_badge(self):
        now = timezone.now()
        for offset in (2, 1, 0):
            module = Module.objects.create(
                number=offset + 10,
                slug=f'module-{offset}',
                title=f'Module {offset}',
                duration='5 min',
                goal='Practice.',
                topics=[],
                is_published=True,
            )
            lesson = Lesson.objects.create(
                module=module,
                slug=f'lesson-{offset}',
                title=f'Lesson {offset}',
                summary='Practice.',
                duration='5 min',
                goal='Practice.',
                explanation='Practice.',
                starter_code='print(1)',
                try_it='Try it.',
                common_mistake='None.',
                mini_challenge='None.',
                expected_output='1',
                practice_challenge_slug='',
                quiz=[],
                is_published=True,
                display_order=offset,
            )
            UserLessonProgress.objects.create(
                user=self.user,
                lesson=lesson,
                is_completed=True,
                completed_at=now - timedelta(days=offset),
            )

        result = get_streak_and_badges(self.user)

        self.assertEqual(result['current_streak'], 3)
        self.assertEqual(result['longest_streak'], 3)
        badge_map = {badge['key']: badge['earned'] for badge in result['badges']}
        self.assertTrue(badge_map['three_day_streak'])
        self.assertFalse(badge_map['seven_day_streak'])

    def test_gap_in_activity_breaks_current_streak(self):
        now = timezone.now()
        module = Module.objects.create(
            number=99,
            slug='old-module',
            title='Old Module',
            duration='5 min',
            goal='Practice.',
            topics=[],
            is_published=True,
        )
        old_lesson = Lesson.objects.create(
            module=module,
            slug='old-lesson',
            title='Old Lesson',
            summary='Practice.',
            duration='5 min',
            goal='Practice.',
            explanation='Practice.',
            starter_code='print(1)',
            try_it='Try it.',
            common_mistake='None.',
            mini_challenge='None.',
            expected_output='1',
            practice_challenge_slug='',
            quiz=[],
            is_published=True,
            display_order=1,
        )
        UserLessonProgress.objects.create(
            user=self.user,
            lesson=old_lesson,
            is_completed=True,
            completed_at=now - timedelta(days=5),
        )

        result = get_streak_and_badges(self.user)

        self.assertEqual(result['current_streak'], 0)
        self.assertEqual(result['longest_streak'], 1)

    def test_perfect_quiz_score_earns_quiz_ace_badge(self):
        UserLessonProgress.objects.create(
            user=self.user,
            lesson=self.lesson,
            best_quiz_score=100,
        )

        result = get_streak_and_badges(self.user)

        badge_map = {badge['key']: badge['earned'] for badge in result['badges']}
        self.assertTrue(badge_map['quiz_ace'])

    def test_my_progress_page_shows_streak_and_badges(self):
        self.client.force_login(self.user)
        UserLessonProgress.objects.create(
            user=self.user,
            lesson=self.lesson,
            is_completed=True,
            completed_at=timezone.now(),
        )

        response = self.client.get(reverse('core:my_progress'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Streak')
        self.assertContains(response, 'Badges')
        self.assertEqual(response.context['current_streak'], 1)


class ResourcesFeatureTests(TestCase):
    def test_published_resource_appears_on_page(self):
        Resource.objects.create(
            title='Python Crash Course',
            description='A great beginner book.',
            url='https://amazon.com/example',
            category=Resource.CATEGORY_AMAZON,
            cta_label='Check Price on Amazon',
            is_published=True,
            display_order=1,
        )

        response = self.client.get(reverse('core:resources'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Python Crash Course')
        self.assertContains(response, 'Check Price on Amazon')

    def test_unpublished_resource_is_hidden(self):
        Resource.objects.create(
            title='Draft Resource',
            description='Not ready yet.',
            url='https://example.com',
            is_published=False,
            display_order=1,
        )

        response = self.client.get(reverse('core:resources'))

        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, 'Draft Resource')

    def test_resources_page_shows_empty_state_with_no_resources(self):
        response = self.client.get(reverse('core:resources'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Recommendations are coming soon.')


@override_settings(**RECAPTCHA_DISABLED_SETTINGS)
class AiCodeHintViewTests(TestCase):
    def setUp(self):
        cache.clear()

    def tearDown(self):
        cache.clear()

    @patch('core.ai._complete', return_value='Try checking your quotes.')
    def test_returns_hint_for_valid_code(self, mock_complete):
        response = self.client.post(
            reverse('core:ai_code_hint'),
            data=json.dumps({
                'title': 'Print Basics',
                'goal': 'Use print().',
                'code': 'print("Hello"',
                'output': 'SyntaxError',
                'is_error': True,
            }),
            content_type='application/json',
        )

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data['ok'])
        self.assertEqual(data['hint'], 'Try checking your quotes.')
        mock_complete.assert_called_once()

    def test_rejects_empty_code(self):
        response = self.client.post(
            reverse('core:ai_code_hint'),
            data=json.dumps({'code': '   '}),
            content_type='application/json',
        )

        self.assertEqual(response.status_code, 400)
        self.assertFalse(response.json()['ok'])

    def test_rejects_invalid_json(self):
        response = self.client.post(
            reverse('core:ai_code_hint'),
            data='not json',
            content_type='application/json',
        )

        self.assertEqual(response.status_code, 400)

    @patch('core.ai._complete', return_value='A hint.')
    def test_rate_limit_blocks_after_threshold(self, mock_complete):
        for _ in range(10):
            response = self.client.post(
                reverse('core:ai_code_hint'),
                data=json.dumps({'code': 'print(1)'}),
                content_type='application/json',
            )
            self.assertEqual(response.status_code, 200)

        blocked_response = self.client.post(
            reverse('core:ai_code_hint'),
            data=json.dumps({'code': 'print(1)'}),
            content_type='application/json',
        )

        self.assertEqual(blocked_response.status_code, 429)

    @patch('core.ai._complete', return_value='Try checking your quotes.')
    def test_success_creates_ai_usage_event(self, mock_complete):
        self.client.post(
            reverse('core:ai_code_hint'),
            data=json.dumps({'code': 'print("Hello"'}),
            content_type='application/json',
        )

        event = EngagementEvent.objects.get(event_type=EngagementEvent.EVENT_AI_USAGE)
        self.assertEqual(event.metadata['feature'], 'code_hint')
        self.assertEqual(event.metadata['outcome'], 'success')

    @patch('core.ai.get_client', side_effect=Exception('API down'))
    def test_ai_failure_tracks_error_outcome(self, mock_get_client):
        from core.ai import FALLBACK_MESSAGE

        response = self.client.post(
            reverse('core:ai_code_hint'),
            data=json.dumps({'code': 'print(1)'}),
            content_type='application/json',
        )

        self.assertEqual(response.json()['hint'], FALLBACK_MESSAGE)
        event = EngagementEvent.objects.get(event_type=EngagementEvent.EVENT_AI_USAGE)
        self.assertEqual(event.metadata['outcome'], 'error')

    def test_rate_limited_request_tracks_rate_limited_outcome(self):
        for _ in range(10):
            with patch('core.ai._complete', return_value='A hint.'):
                self.client.post(
                    reverse('core:ai_code_hint'),
                    data=json.dumps({'code': 'print(1)'}),
                    content_type='application/json',
                )

        self.client.post(
            reverse('core:ai_code_hint'),
            data=json.dumps({'code': 'print(1)'}),
            content_type='application/json',
        )

        self.assertTrue(
            EngagementEvent.objects.filter(
                event_type=EngagementEvent.EVENT_AI_USAGE,
                metadata__outcome='rate_limited',
            ).exists()
        )


@override_settings(**RECAPTCHA_DISABLED_SETTINGS)
class AiQuizExplainViewTests(TestCase):
    def setUp(self):
        cache.clear()
        self.module = Module.objects.create(
            number=1,
            slug='first-steps',
            title='First Steps',
            duration='10 min',
            goal='Learn the basics.',
            topics=[],
            is_published=True,
        )
        self.lesson = Lesson.objects.create(
            module=self.module,
            slug='variables-basics',
            title='Variables Basics',
            summary='Learn variables.',
            duration='10 min',
            goal='Use variables.',
            explanation='Explain variables.',
            starter_code='name = "Michael"',
            try_it='Change the name.',
            common_mistake='Using a variable before assigning it.',
            mini_challenge='Create two variables.',
            expected_output='Michael',
            practice_challenge_slug='',
            quiz=[
                {
                    'question': 'What is a variable?',
                    'options': ['A named place to store a value.', 'A loop.', 'An error message.'],
                    'answer': 0,
                    'explanation': 'Variables store values with names.',
                },
            ],
            is_published=True,
            display_order=1,
        )

    def tearDown(self):
        cache.clear()

    @patch('core.ai._complete', return_value='Because a variable stores a value under a name.')
    def test_returns_explanation_for_valid_question(self, mock_complete):
        response = self.client.post(
            reverse('core:ai_quiz_explain'),
            data=json.dumps({
                'lesson_slug': self.lesson.slug,
                'question_index': 0,
                'selected_answer': 1,
            }),
            content_type='application/json',
        )

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data['ok'])
        self.assertEqual(data['explanation'], 'Because a variable stores a value under a name.')
        mock_complete.assert_called_once()

    def test_rejects_unknown_question_index(self):
        response = self.client.post(
            reverse('core:ai_quiz_explain'),
            data=json.dumps({'lesson_slug': self.lesson.slug, 'question_index': 99}),
            content_type='application/json',
        )

        self.assertEqual(response.status_code, 400)

    def test_rejects_unknown_lesson(self):
        response = self.client.post(
            reverse('core:ai_quiz_explain'),
            data=json.dumps({'lesson_slug': 'does-not-exist', 'question_index': 0}),
            content_type='application/json',
        )

        self.assertEqual(response.status_code, 400)


@override_settings(**RECAPTCHA_DISABLED_SETTINGS)
class AiTutorChatViewTests(TestCase):
    def setUp(self):
        cache.clear()
        self.module = Module.objects.create(
            number=1,
            slug='first-steps',
            title='First Steps',
            duration='10 min',
            goal='Learn the basics.',
            topics=[],
            is_published=True,
        )
        self.lesson = Lesson.objects.create(
            module=self.module,
            slug='print-basics',
            title='Print Basics',
            summary='Learn print.',
            duration='8 min',
            goal='Use print().',
            explanation='Explain print.',
            starter_code='print("Hello")',
            try_it='Change the text.',
            common_mistake='Missing quote.',
            mini_challenge='Add one line.',
            expected_output='Hello',
            practice_challenge_slug='',
            quiz=[],
            is_published=True,
            display_order=1,
        )

    def tearDown(self):
        cache.clear()

    @patch('core.ai._complete', return_value='print() displays text on the screen.')
    def test_returns_reply_for_valid_message(self, mock_complete):
        response = self.client.post(
            reverse('core:ai_tutor_chat'),
            data=json.dumps({
                'lesson_slug': self.lesson.slug,
                'message': 'What does print() do?',
                'history': [],
            }),
            content_type='application/json',
        )

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data['ok'])
        self.assertEqual(data['reply'], 'print() displays text on the screen.')
        mock_complete.assert_called_once()

    def test_rejects_empty_message(self):
        response = self.client.post(
            reverse('core:ai_tutor_chat'),
            data=json.dumps({'lesson_slug': self.lesson.slug, 'message': ''}),
            content_type='application/json',
        )

        self.assertEqual(response.status_code, 400)

    @patch('core.ai._complete', return_value='reply')
    def test_ignores_malformed_history(self, mock_complete):
        response = self.client.post(
            reverse('core:ai_tutor_chat'),
            data=json.dumps({
                'lesson_slug': self.lesson.slug,
                'message': 'Hello',
                'history': 'not-a-list',
            }),
            content_type='application/json',
        )

        self.assertEqual(response.status_code, 200)
        mock_complete.assert_called_once()


class HomeRecommendedNextWidgetTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email='learner@example.com',
            username='learner_one',
            password='testpass123',
        )
        self.module = Module.objects.create(
            number=1,
            slug='first-steps',
            title='First Steps',
            duration='10 min',
            goal='Learn the basics.',
            topics=[],
            is_published=True,
        )
        self.lesson = Lesson.objects.create(
            module=self.module,
            slug='print-basics',
            title='Print Basics',
            summary='Learn print.',
            duration='8 min',
            goal='Use print().',
            explanation='Explain print.',
            starter_code='print("Hello")',
            try_it='Change the text.',
            common_mistake='Missing quote.',
            mini_challenge='Add one line.',
            expected_output='Hello',
            practice_challenge_slug='',
            quiz=[],
            is_published=True,
            display_order=1,
        )

    def test_anonymous_visitor_does_not_see_widget(self):
        response = self.client.get(reverse('core:home'))

        self.assertNotContains(response, 'Pick up where you left off')

    def test_new_authenticated_user_sees_start_next_lesson(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse('core:home'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Pick up where you left off')
        self.assertContains(response, 'Start Next Lesson')

    def test_user_with_progress_sees_continue_lesson(self):
        self.client.force_login(self.user)
        UserLessonProgress.objects.create(
            user=self.user,
            lesson=self.lesson,
            is_completed=False,
        )

        response = self.client.get(reverse('core:home'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Continue Lesson')
        self.assertContains(response, self.lesson.title)


class NavigationContextTests(TestCase):
    def test_navbar_includes_primary_and_more_links(self):
        response = self.client.get(reverse('core:home'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Start Here')
        self.assertContains(response, 'Tips')
        self.assertContains(response, 'Community')

    def test_footer_content_is_available_on_auth_pages(self):
        # Django's built-in auth views (login, signup) don't use
        # NavigationContextMixin, so nav/footer context must come from a
        # site-wide context processor instead, or the footer renders blank
        # on these pages.
        response = self.client.get(reverse('login'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'site-footer__social')
        self.assertContains(response, 'Code with Michael')

    def test_footer_content_is_available_on_signup_page(self):
        response = self.client.get(reverse('signup'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'site-footer__social')

    def test_footer_includes_python_logo(self):
        response = self.client.get(reverse('core:home'))

        self.assertContains(response, 'python-logo-only.svg')

    def test_footer_shows_contact_link_when_marketing_email_configured(self):
        with override_settings(MARKETING_CONTACT_EMAIL='hello@example.com'):
            response = self.client.get(reverse('core:home'))

        self.assertContains(response, 'mailto:hello@example.com')

    def test_footer_hides_contact_link_when_marketing_email_not_configured(self):
        with override_settings(MARKETING_CONTACT_EMAIL=''):
            response = self.client.get(reverse('core:home'))

        self.assertNotContains(response, 'mailto:')


class BootstrapLearningContentCommandTests(TestCase):
    def test_seeds_published_lessons_and_unpublished_drafts(self):
        from django.core.management import call_command

        call_command('bootstrap_learning_content')

        self.assertTrue(Lesson.objects.filter(slug='print-basics', is_published=True).exists())
        self.assertTrue(Lesson.objects.filter(slug='getting-user-input', is_published=False).exists())


RECAPTCHA_ENABLED_SETTINGS = {
    'RECAPTCHA_SITE_KEY': 'test-site-key',
    'RECAPTCHA_SECRET_KEY': 'test-secret-key',
    'RECAPTCHA_MIN_SCORE': 0.5,
}


class RecaptchaVerificationTests(TestCase):
    @override_settings(**RECAPTCHA_DISABLED_SETTINGS)
    def test_unconfigured_allows_through_without_a_token(self):
        from core.recaptcha import verify_recaptcha

        self.assertTrue(verify_recaptcha('', 'any_action'))

    @override_settings(**RECAPTCHA_ENABLED_SETTINGS)
    def test_configured_rejects_missing_token(self):
        from core.recaptcha import verify_recaptcha

        self.assertFalse(verify_recaptcha('', 'email_signup'))

    @override_settings(**RECAPTCHA_ENABLED_SETTINGS)
    @patch('core.recaptcha.httpx.post')
    def test_configured_accepts_valid_high_score_token(self, mock_post):
        from core.recaptcha import verify_recaptcha

        mock_post.return_value.raise_for_status.return_value = None
        mock_post.return_value.json.return_value = {
            'success': True,
            'action': 'email_signup',
            'score': 0.9,
        }

        self.assertTrue(verify_recaptcha('good-token', 'email_signup'))

    @override_settings(**RECAPTCHA_ENABLED_SETTINGS)
    @patch('core.recaptcha.httpx.post')
    def test_configured_rejects_low_score_token(self, mock_post):
        from core.recaptcha import verify_recaptcha

        mock_post.return_value.raise_for_status.return_value = None
        mock_post.return_value.json.return_value = {
            'success': True,
            'action': 'email_signup',
            'score': 0.1,
        }

        self.assertFalse(verify_recaptcha('bot-token', 'email_signup'))

    @override_settings(**RECAPTCHA_ENABLED_SETTINGS)
    @patch('core.recaptcha.httpx.post')
    def test_configured_rejects_mismatched_action(self, mock_post):
        from core.recaptcha import verify_recaptcha

        mock_post.return_value.raise_for_status.return_value = None
        mock_post.return_value.json.return_value = {
            'success': True,
            'action': 'some_other_action',
            'score': 0.9,
        }

        self.assertFalse(verify_recaptcha('token', 'email_signup'))

    @override_settings(**RECAPTCHA_ENABLED_SETTINGS)
    @patch('core.recaptcha.httpx.post')
    def test_configured_rejects_invalid_token(self, mock_post):
        from core.recaptcha import verify_recaptcha

        mock_post.return_value.raise_for_status.return_value = None
        mock_post.return_value.json.return_value = {
            'success': False,
            'error-codes': ['invalid-input-response'],
        }

        self.assertFalse(verify_recaptcha('expired-token', 'email_signup'))

    @override_settings(**RECAPTCHA_ENABLED_SETTINGS)
    @patch('core.recaptcha.httpx.post', side_effect=Exception('network down'))
    def test_fails_open_when_google_api_unreachable(self, mock_post):
        from core.recaptcha import verify_recaptcha

        self.assertTrue(verify_recaptcha('token', 'email_signup'))


class RecaptchaIntegrationTests(TestCase):
    def setUp(self):
        cache.clear()

    def tearDown(self):
        cache.clear()

    @override_settings(**RECAPTCHA_ENABLED_SETTINGS)
    @patch('core.views.verify_recaptcha', return_value=False)
    def test_email_signup_blocked_when_recaptcha_fails(self, mock_verify):
        response = self.client.post(
            reverse('core:home'),
            data={'email': 'bot@example.com', 'first_name': 'Bot'},
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertFalse(EmailSubscriber.objects.filter(email='bot@example.com').exists())

    @override_settings(**RECAPTCHA_ENABLED_SETTINGS)
    @patch('core.views.verify_recaptcha', return_value=False)
    @patch('core.ai._complete', return_value='A hint.')
    def test_ai_code_hint_blocked_when_recaptcha_fails(self, mock_complete, mock_verify):
        response = self.client.post(
            reverse('core:ai_code_hint'),
            data=json.dumps({'code': 'print(1)', 'recaptcha_token': 'bad'}),
            content_type='application/json',
        )

        self.assertEqual(response.status_code, 403)
        mock_complete.assert_not_called()


class TermsOfServiceViewTests(TestCase):
    def test_page_renders_with_expected_sections(self):
        response = self.client.get(reverse('core:terms_of_service'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Terms of Service')
        self.assertContains(response, 'AI tutor features')
        self.assertContains(response, 'Community posts')

    def test_footer_links_to_privacy_and_terms(self):
        response = self.client.get(reverse('core:home'))

        self.assertContains(response, reverse('core:privacy_policy'))
        self.assertContains(response, reverse('core:terms_of_service'))


class CustomErrorPageTests(TestCase):
    @override_settings(DEBUG=False, ALLOWED_HOSTS=['testserver'])
    def test_404_page_renders_custom_template(self):
        response = self.client.get('/this-page-does-not-exist/')

        self.assertEqual(response.status_code, 404)
        self.assertContains(response, 'This page took a wrong turn', status_code=404)
        self.assertContains(response, 'Back to Home', status_code=404)

    @override_settings(DEBUG=False, ALLOWED_HOSTS=['testserver'])
    def test_500_page_renders_custom_template(self):
        from django.template import loader

        rendered = loader.render_to_string('500.html')

        self.assertIn('Something broke on our end', rendered)
        self.assertIn('Back to Home', rendered)


class QuizShuffleTests(TestCase):
    def test_shuffled_options_keep_their_original_index(self):
        quiz = [
            {
                'question': 'Which is a string?',
                'options': ['5', '"5"', 'True'],
                'answer': 1,
                'explanation': 'Quoted values are strings.',
            },
        ]

        for _ in range(20):
            shuffled = build_shuffled_quiz(quiz)
            self.assertEqual(len(shuffled), 1)
            options = shuffled[0]['options']
            self.assertEqual({idx for idx, _ in options}, {0, 1, 2})
            for original_index, text in options:
                self.assertEqual(quiz[0]['options'][original_index], text)
            self.assertEqual(shuffled[0]['question'], 'Which is a string?')
            self.assertEqual(shuffled[0]['explanation'], 'Quoted values are strings.')

    def test_option_order_is_not_always_identical(self):
        quiz = [{'question': 'Q', 'options': ['A', 'B', 'C', 'D', 'E'], 'answer': 0, 'explanation': ''}]

        orders = {tuple(idx for idx, _ in build_shuffled_quiz(quiz)[0]['options']) for _ in range(30)}

        self.assertGreater(len(orders), 1, 'Expected option order to vary across renders')

    def test_empty_quiz_returns_empty_list(self):
        self.assertEqual(build_shuffled_quiz([]), [])
        self.assertEqual(build_shuffled_quiz(None), [])

    def test_lesson_detail_renders_shuffled_options_with_correct_values(self):
        module = Module.objects.create(
            number=1,
            slug='first-steps',
            title='First Steps',
            duration='10 min',
            goal='Learn the basics.',
            topics=['print()'],
            is_published=True,
        )
        Lesson.objects.create(
            module=module,
            slug='print-basics',
            title='Print Basics',
            summary='Learn print.',
            duration='8 min',
            goal='Use print().',
            explanation='Explain print.',
            starter_code='print("Hello")',
            try_it='Change the text.',
            common_mistake='Missing quote.',
            mini_challenge='Add one line.',
            expected_output='Hello',
            quiz=[
                {
                    'question': 'What does print() do?',
                    'options': ['Deletes a file', 'Displays output', 'Runs a loop'],
                    'answer': 1,
                    'explanation': 'print() displays output.',
                },
            ],
            is_published=True,
            display_order=1,
        )

        response = self.client.get(reverse('core:lesson_detail', args=['print-basics']))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'value="1"')
        self.assertContains(response, 'Displays output')


class CurriculumContentIntegrityTests(TestCase):
    """Guards against regressions in the beginner-friendly lesson/module/challenge order.

    These check core.content directly (not the DB) so they catch mistakes
    at authoring time, before `bootstrap_learning_content` ever runs.
    """

    def setUp(self):
        from core import content
        self.content = content
        self.module_number_by_slug = {m['slug']: m['number'] for m in content.MODULES}
        self.lessons_in_order = sorted(
            content.LESSONS,
            key=lambda lesson: (self.module_number_by_slug[lesson['module_slug']], content.LESSONS.index(lesson)),
        )
        self.lesson_position = {lesson['slug']: index for index, lesson in enumerate(self.lessons_in_order)}

    def test_module_numbers_are_unique_and_sequential(self):
        numbers = [m['number'] for m in self.content.MODULES]
        self.assertEqual(len(numbers), len(set(numbers)))
        self.assertEqual(sorted(numbers), list(range(1, len(numbers) + 1)))

    def test_every_lesson_references_a_real_module(self):
        for lesson in self.content.LESSONS + self.content.DRAFT_LESSONS:
            self.assertIn(
                lesson['module_slug'], self.module_number_by_slug,
                f"{lesson['slug']} references a module that doesn't exist",
            )

    def test_every_practice_challenge_is_paired_with_exactly_one_lesson(self):
        challenge_slugs = {c['slug'] for c in self.content.CHALLENGES}
        pairings = {}
        for lesson in self.content.LESSONS:
            slug = lesson.get('practice_challenge_slug')
            if not slug:
                continue
            self.assertIn(slug, challenge_slugs, f"{lesson['slug']} references a missing challenge")
            pairings.setdefault(slug, []).append(lesson['slug'])

        shared = {slug: lessons for slug, lessons in pairings.items() if len(lessons) > 1}
        self.assertEqual(shared, {}, f'Challenges reused across multiple lessons: {shared}')

    def test_lists_are_taught_before_loops_which_are_taught_before_tuples_and_sets(self):
        self.assertLess(self.lesson_position['lists-and-dictionaries-basics'], self.lesson_position['loops-in-action'])
        self.assertLess(self.lesson_position['loops-in-action'], self.lesson_position['tuples-and-sets'])

    def test_booleans_are_taught_before_multi_branch_conditionals(self):
        self.assertLess(self.lesson_position['booleans-and-choices'], self.lesson_position['conditionals-basics'])

    def test_advanced_topics_are_taught_after_functions_in_dependency_order(self):
        order = [
            'functions-basics',
            'error-handling-basics',
            'reading-and-writing-files',
            'importing-modules',
            'intro-to-classes-and-objects',
        ]
        positions = [self.lesson_position[slug] for slug in order]
        self.assertEqual(positions, sorted(positions), 'Advanced topics are out of dependency order')

    def test_data_type_mix_up_challenge_does_not_require_booleans(self):
        challenge = next(c for c in self.content.CHALLENGES if c['slug'] == 'data-type-mix-up')
        combined_text = challenge['prompt'] + challenge['starter_code']
        self.assertNotIn('bool', combined_text.lower())
        self.assertNotIn('True', challenge['starter_code'])

    def test_booleans_and_choices_challenge_does_not_require_elif(self):
        challenge = next(c for c in self.content.CHALLENGES if c['slug'] == 'boolean-checkpoint')
        self.assertNotIn('elif', challenge['starter_code'])

    def test_loops_in_action_challenge_does_not_require_tuple_syntax(self):
        challenge = next(c for c in self.content.CHALLENGES if c['slug'] == 'loop-through-a-list')
        self.assertNotIn('(', challenge['starter_code'].split('=', 1)[1].split('\n')[0])
        self.assertIn('[', challenge['starter_code'])


class NewLessonStarterCodeOutputTests(TestCase):
    """Actually runs each new lesson/challenge's starter_code in real Python
    and checks stdout matches expected_output exactly, so a content typo
    can't silently drift from what the browser editor would actually show.
    """

    def _run_and_capture_stdout(self, code):
        import contextlib
        import io
        import os
        import tempfile

        buffer = io.StringIO()
        with tempfile.TemporaryDirectory() as tmp_dir, contextlib.redirect_stdout(buffer):
            original_cwd = os.getcwd()
            os.chdir(tmp_dir)
            try:
                exec(code, {'__name__': '__main__'})
            finally:
                os.chdir(original_cwd)
        return buffer.getvalue().rstrip('\n')

    def _assert_lesson_output_matches(self, slug):
        from core import content

        lesson = next(item for item in content.LESSONS if item['slug'] == slug)
        actual = self._run_and_capture_stdout(lesson['starter_code'])
        self.assertEqual(actual, lesson['expected_output'].rstrip('\n'))

    def _assert_challenge_output_matches(self, slug):
        from core import content

        challenge = next(item for item in content.CHALLENGES if item['slug'] == slug)
        actual = self._run_and_capture_stdout(challenge['starter_code'])
        self.assertEqual(actual, challenge['expected_output'].rstrip('\n'))

    def test_error_handling_basics_lesson_output(self):
        self._assert_lesson_output_matches('error-handling-basics')

    def test_reading_and_writing_files_lesson_output(self):
        self._assert_lesson_output_matches('reading-and-writing-files')

    def test_importing_modules_lesson_output(self):
        self._assert_lesson_output_matches('importing-modules')

    def test_intro_to_classes_lesson_output(self):
        self._assert_lesson_output_matches('intro-to-classes-and-objects')

    def test_safe_number_check_challenge_output(self):
        self._assert_challenge_output_matches('safe-number-check')

    def test_write_and_read_a_file_challenge_output(self):
        self._assert_challenge_output_matches('write-and-read-a-file')

    def test_random_choice_picker_challenge_output(self):
        self._assert_challenge_output_matches('random-choice-picker')

    def test_build_a_pet_class_challenge_output(self):
        self._assert_challenge_output_matches('build-a-pet-class')


STRIPE_CONFIGURED_SETTINGS = {
    'STRIPE_PUBLISHABLE_KEY': 'pk_test_fake',
    'STRIPE_SECRET_KEY': 'sk_test_fake',
    'STRIPE_WEBHOOK_SECRET': 'whsec_fake',
    'PREMIUM_COURSE_PRICE_CENTS': 4900,
}


class PremiumCourseViewTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email='learner@example.com',
            username='learner_one',
            password='testpass123',
        )

    def test_anonymous_visitor_sees_locked_page_with_login_link(self):
        response = self.client.get(reverse('core:premium_course'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Log In to Purchase')
        self.assertNotContains(response, "Welcome to “Python for Absolute Beginners.”")

    def test_locked_page_does_not_leak_full_lecture_content(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse('core:premium_course'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Full Course')
        self.assertNotContains(response, 'Every professional developer was once a beginner')

    @override_settings(**STRIPE_CONFIGURED_SETTINGS)
    def test_authenticated_user_without_purchase_sees_buy_button(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse('core:premium_course'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Buy Now')

    def test_authenticated_user_sees_coming_soon_when_stripe_not_configured(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse('core:premium_course'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "isn't set up yet")
        self.assertNotContains(response, 'Buy Now')

    def test_purchaser_sees_full_lecture_content(self):
        self.client.force_login(self.user)
        PremiumPurchase.objects.create(
            user=self.user,
            stripe_checkout_session_id='cs_test_123',
            amount_paid_cents=4900,
        )

        response = self.client.get(reverse('core:premium_course'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Every professional developer was once a beginner')
        self.assertNotContains(response, 'Buy Now')

    def test_my_progress_shows_course_cta_when_all_caught_up_and_not_purchased(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse('core:my_progress'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'See the Full Course')

    def test_my_progress_hides_course_cta_after_purchase(self):
        self.client.force_login(self.user)
        PremiumPurchase.objects.create(
            user=self.user,
            stripe_checkout_session_id='cs_test_456',
            amount_paid_cents=4900,
        )

        response = self.client.get(reverse('core:my_progress'))

        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, 'See the Full Course')


class PremiumCourseCheckoutViewTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email='learner@example.com',
            username='learner_one',
            password='testpass123',
        )

    def test_anonymous_user_is_redirected_to_login(self):
        response = self.client.post(reverse('core:premium_course_checkout'))

        self.assertEqual(response.status_code, 302)
        self.assertIn('/accounts/login/', response.url)

    def test_checkout_without_stripe_configured_shows_error(self):
        self.client.force_login(self.user)

        response = self.client.post(reverse('core:premium_course_checkout'), follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Checkout is not available yet')

    @override_settings(**STRIPE_CONFIGURED_SETTINGS)
    def test_already_purchased_user_is_redirected_without_new_session(self):
        PremiumPurchase.objects.create(
            user=self.user,
            stripe_checkout_session_id='cs_test_existing',
            amount_paid_cents=4900,
        )
        self.client.force_login(self.user)

        with patch('core.views.stripe.checkout.Session.create') as mock_create:
            response = self.client.post(reverse('core:premium_course_checkout'))

        mock_create.assert_not_called()
        self.assertRedirects(response, reverse('core:premium_course'))

    @override_settings(**STRIPE_CONFIGURED_SETTINGS)
    def test_successful_checkout_redirects_to_stripe(self):
        self.client.force_login(self.user)
        fake_session = type('FakeSession', (), {'url': 'https://checkout.stripe.com/pay/cs_test_abc'})()

        with patch('core.views.stripe.checkout.Session.create', return_value=fake_session) as mock_create:
            response = self.client.post(reverse('core:premium_course_checkout'))

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, 'https://checkout.stripe.com/pay/cs_test_abc')
        call_kwargs = mock_create.call_args.kwargs
        self.assertEqual(call_kwargs['client_reference_id'], str(self.user.id))
        self.assertEqual(call_kwargs['customer_email'], self.user.email)
        self.assertEqual(call_kwargs['mode'], 'payment')
        self.assertEqual(call_kwargs['line_items'][0]['price_data']['unit_amount'], 4900)

    @override_settings(**STRIPE_CONFIGURED_SETTINGS)
    def test_stripe_error_shows_friendly_message(self):
        self.client.force_login(self.user)

        with patch('core.views.stripe.checkout.Session.create', side_effect=stripe.error.StripeError('boom')):
            response = self.client.post(reverse('core:premium_course_checkout'), follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Something went wrong starting checkout')


class StripeWebhookViewTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email='learner@example.com',
            username='learner_one',
            password='testpass123',
        )

    def _completed_session_event(self, session_id='cs_test_webhook'):
        return {
            'type': 'checkout.session.completed',
            'data': {
                'object': {
                    'id': session_id,
                    'client_reference_id': str(self.user.id),
                    'payment_intent': 'pi_test_123',
                    'amount_total': 4900,
                },
            },
        }

    def test_returns_400_when_webhook_secret_not_configured(self):
        response = self.client.post(reverse('core:premium_course_webhook'), data='{}', content_type='application/json')

        self.assertEqual(response.status_code, 400)

    @override_settings(**STRIPE_CONFIGURED_SETTINGS)
    def test_invalid_signature_returns_400(self):
        with patch('core.views.stripe.Webhook.construct_event', side_effect=stripe.error.SignatureVerificationError('bad sig', 'header')):
            response = self.client.post(
                reverse('core:premium_course_webhook'),
                data='{}',
                content_type='application/json',
                HTTP_STRIPE_SIGNATURE='bad',
            )

        self.assertEqual(response.status_code, 400)
        self.assertFalse(PremiumPurchase.objects.exists())

    @override_settings(**STRIPE_CONFIGURED_SETTINGS)
    def test_completed_checkout_grants_access(self):
        event = self._completed_session_event()
        with patch('core.views.stripe.Webhook.construct_event', return_value=event):
            response = self.client.post(
                reverse('core:premium_course_webhook'),
                data='{}',
                content_type='application/json',
                HTTP_STRIPE_SIGNATURE='sig',
            )

        self.assertEqual(response.status_code, 200)
        purchase = PremiumPurchase.objects.get(user=self.user)
        self.assertEqual(purchase.stripe_checkout_session_id, 'cs_test_webhook')
        self.assertEqual(purchase.amount_paid_cents, 4900)
        self.assertEqual(purchase.stripe_payment_intent_id, 'pi_test_123')

    @override_settings(**STRIPE_CONFIGURED_SETTINGS)
    def test_duplicate_webhook_delivery_is_idempotent(self):
        event = self._completed_session_event()
        with patch('core.views.stripe.Webhook.construct_event', return_value=event):
            self.client.post(reverse('core:premium_course_webhook'), data='{}', content_type='application/json', HTTP_STRIPE_SIGNATURE='sig')
            self.client.post(reverse('core:premium_course_webhook'), data='{}', content_type='application/json', HTTP_STRIPE_SIGNATURE='sig')

        self.assertEqual(PremiumPurchase.objects.filter(user=self.user).count(), 1)

    @override_settings(**STRIPE_CONFIGURED_SETTINGS)
    def test_unhandled_event_type_is_acknowledged_without_side_effects(self):
        event = {'type': 'payment_intent.created', 'data': {'object': {}}}
        with patch('core.views.stripe.Webhook.construct_event', return_value=event):
            response = self.client.post(
                reverse('core:premium_course_webhook'),
                data='{}',
                content_type='application/json',
                HTTP_STRIPE_SIGNATURE='sig',
            )

        self.assertEqual(response.status_code, 200)
        self.assertFalse(PremiumPurchase.objects.exists())

    @override_settings(**STRIPE_CONFIGURED_SETTINGS)
    def test_missing_client_reference_id_does_not_crash(self):
        event = self._completed_session_event()
        event['data']['object']['client_reference_id'] = None
        with patch('core.views.stripe.Webhook.construct_event', return_value=event):
            response = self.client.post(
                reverse('core:premium_course_webhook'),
                data='{}',
                content_type='application/json',
                HTTP_STRIPE_SIGNATURE='sig',
            )

        self.assertEqual(response.status_code, 200)
        self.assertFalse(PremiumPurchase.objects.exists())

    @override_settings(**STRIPE_CONFIGURED_SETTINGS)
    def test_endpoint_is_csrf_exempt_for_stripe_delivery(self):
        strict_client = Client(enforce_csrf_checks=True)
        event = self._completed_session_event('cs_test_csrf')

        with patch('core.views.stripe.Webhook.construct_event', return_value=event):
            response = strict_client.post(
                reverse('core:premium_course_webhook'),
                data='{}',
                content_type='application/json',
                HTTP_STRIPE_SIGNATURE='sig',
            )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(PremiumPurchase.objects.filter(stripe_checkout_session_id='cs_test_csrf').exists())

from django.contrib.auth import get_user_model
import json

from django.core import mail
from django.test import Client, TestCase
from django.urls import reverse
from django.utils import timezone

from core.models import (
    Challenge,
    EmailOnboardingDelivery,
    EmailSubscriber,
    EngagementEvent,
    Lesson,
    Module,
    UserChallengeProgress,
    UserLessonProgress,
)


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

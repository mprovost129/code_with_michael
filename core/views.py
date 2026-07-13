import json

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.mail import send_mail
from django.http import Http404, JsonResponse
from django.shortcuts import redirect
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.utils.http import url_has_allowed_host_and_scheme
from django.views import View
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from django.views.generic import TemplateView

from .ai import (
    FALLBACK_MESSAGE,
    check_rate_limit,
    get_code_hint,
    get_quiz_explanation,
    get_tutor_reply,
)
from .content import HOME_FEATURES, ROADMAP_STEPS
from .forms import CommunityPostForm, EmailSubscriberForm
from .models import (
    Challenge,
    EmailSubscriber,
    EngagementEvent,
    Lesson,
    UserChallengeProgress,
    UserLessonProgress,
)
from .onboarding import send_subscriber_welcome_email
from .recaptcha import verify_recaptcha
from .services import (
    build_lesson_path_cards,
    build_shuffled_quiz,
    get_challenge,
    get_challenge_milestones,
    get_challenges,
    get_community_items,
    get_community_posts,
    get_engagement_summary,
    get_lesson,
    get_lesson_milestone,
    get_lesson_practice_challenge,
    get_lessons,
    get_modules,
    get_projects,
    get_resources,
    get_streak_and_badges,
    get_tips,
    get_user_progress_summary,
    search_content,
)


class NavigationContextMixin:
    """Ensures a CSRF cookie is set. nav_pages/site_stats/social_links come
    from the core.context_processors.site_content context processor, which
    runs on every page (including auth pages that don't use this mixin).
    """

    @method_decorator(ensure_csrf_cookie)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class HomeView(NavigationContextMixin, TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        lessons = get_lessons()
        modules = get_modules()
        challenges = get_challenges()
        tips = get_tips()
        context.update({
            'features': HOME_FEATURES,
            'roadmap_steps': ROADMAP_STEPS,
            'modules': modules[:4],
            'featured_lesson': lessons[0] if lessons else None,
            'featured_challenge': challenges[0] if challenges else None,
            'tips': tips[:2],
            'email_subscriber_form': kwargs.get('email_subscriber_form') or EmailSubscriberForm(),
        })
        if self.request.user.is_authenticated:
            summary = get_user_progress_summary(self.request.user)
            context.update({
                'continue_lesson': summary['continue_lesson'],
                'continue_lesson_challenge': summary['continue_lesson_challenge'],
                'recommended_next_lesson': summary['recommended_next_lesson'],
                'recommended_next_challenge': summary['recommended_next_challenge'],
            })
        return context

    def post(self, request, *args, **kwargs):
        form = EmailSubscriberForm(request.POST)
        if not form.is_valid():
            return self.render_to_response(self.get_context_data(email_subscriber_form=form))

        if not verify_recaptcha(request.POST.get('recaptcha_token', ''), 'email_signup', request=request):
            messages.error(request, 'We could not verify that submission. Please try again.')
            return redirect('core:home')

        source = 'footer' if request.POST.get('source') == 'footer' else 'homepage'
        subscriber, created = EmailSubscriber.objects.get_or_create(
            email=form.cleaned_data['email'],
            defaults={
                'first_name': form.cleaned_data.get('first_name', ''),
                'source': source,
                'is_active': True,
            },
        )

        if created:
            send_subscriber_welcome_email(subscriber)
            self._notify_marketing_contact(subscriber)
            messages.success(request, 'You are in. Watch for beginner lessons and challenges in your inbox.')
        else:
            if form.cleaned_data.get('first_name') and not subscriber.first_name:
                subscriber.first_name = form.cleaned_data['first_name']
                subscriber.save(update_fields=['first_name'])
            messages.info(request, 'That email is already on the list, so you are all set.')

        return redirect('core:home')

    def _notify_marketing_contact(self, subscriber):
        if not settings.MARKETING_CONTACT_EMAIL:
            return

        send_mail(
            subject='New Code with Michael email signup',
            message=(
                f'New subscriber: {subscriber.email}\n'
                f'First name: {subscriber.first_name or "Not provided"}\n'
                f'Source: {subscriber.source}'
            ),
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.MARKETING_CONTACT_EMAIL],
            fail_silently=True,
        )


class StartHereView(NavigationContextMixin, TemplateView):
    template_name = 'core/start_here.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        modules = get_modules()
        lessons = get_lessons()
        context.update({
            'first_module': modules[0] if modules else None,
            'featured_lesson': lessons[0] if lessons else None,
            'steps': [
                'Read one short explanation.',
                'Press Run to see real output.',
                'Change one line and rerun it.',
                'Finish a tiny challenge and quick quiz.',
            ],
        })
        return context


class LessonsView(NavigationContextMixin, TemplateView):
    template_name = 'core/lessons.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        lessons = get_lessons()
        featured_lesson = lessons[0] if lessons else None
        lesson_cards = build_lesson_path_cards(lessons)
        context.update({
            'modules': get_modules(),
            'lessons': lessons,
            'lesson_cards': lesson_cards,
            'featured_lesson': featured_lesson,
            'featured_module_slug': getattr(getattr(featured_lesson, 'module', None), 'slug', None) or (
                featured_lesson.get('module_slug') if isinstance(featured_lesson, dict) else None
            ),
        })
        return context


class LessonDetailView(NavigationContextMixin, TemplateView):
    template_name = 'core/lesson_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        lesson = get_lesson(kwargs['slug'])
        if lesson is None:
            raise Http404('Lesson not found')
        context['lesson'] = lesson
        quiz = getattr(lesson, 'quiz', None)
        if quiz is None and isinstance(lesson, dict):
            quiz = lesson.get('quiz')
        context['shuffled_quiz'] = build_shuffled_quiz(quiz or [])
        practice_challenge = get_lesson_practice_challenge(lesson)
        context['practice_challenge'] = practice_challenge
        if hasattr(lesson, 'pk'):
            lessons = get_lessons()
            lesson_slugs = [item.slug if hasattr(item, 'slug') else item['slug'] for item in lessons]
            if lesson.slug in lesson_slugs:
                lesson_index = lesson_slugs.index(lesson.slug)
                context['previous_lesson'] = lessons[lesson_index - 1] if lesson_index > 0 else None
                context['next_lesson'] = lessons[lesson_index + 1] if lesson_index + 1 < len(lessons) else None
                context['lesson_position'] = lesson_index + 1
                context['total_lessons'] = len(lessons)
            if self.request.user.is_authenticated:
                progress, _ = UserLessonProgress.objects.get_or_create(
                    user=self.request.user,
                    lesson=lesson,
                )
                context['lesson_progress'] = progress
                completed_lesson_ids = set(
                    UserLessonProgress.objects.filter(user=self.request.user, is_completed=True).values_list('lesson_id', flat=True)
                )
                completed_challenge_ids = set(
                    UserChallengeProgress.objects.filter(user=self.request.user, is_completed=True).values_list('challenge_id', flat=True)
                )
                context['lesson_milestone'] = get_lesson_milestone(
                    lesson,
                    completed_lesson_ids=completed_lesson_ids,
                    completed_challenge_ids=completed_challenge_ids,
                )
                challenge_progress = None
                challenge_complete = False
                if practice_challenge is not None and hasattr(practice_challenge, 'pk'):
                    challenge_progress = UserChallengeProgress.objects.filter(
                        user=self.request.user,
                        challenge=practice_challenge,
                    ).first()
                    challenge_complete = bool(challenge_progress and challenge_progress.is_completed)
                quiz_complete = bool(progress.quiz_passed_at)
                completion_stack = [
                    {
                        'label': 'Lesson marked complete',
                        'done': progress.is_completed,
                    },
                    {
                        'label': 'Quick quiz passed',
                        'done': quiz_complete,
                    },
                ]
                if practice_challenge is not None:
                    completion_stack.append({
                        'label': f'Paired challenge complete: {practice_challenge.title}',
                        'done': challenge_complete,
                    })
                context['lesson_completion_stack'] = completion_stack
                context['lesson_stack_complete_count'] = sum(1 for item in completion_stack if item['done'])
                if not progress.is_completed:
                    context['lesson_next_action'] = 'Mark this lesson complete next.'
                elif not quiz_complete:
                    context['lesson_next_action'] = 'Pass the quick quiz next.'
                elif practice_challenge is not None and not challenge_complete:
                    context['lesson_next_action'] = f'Open {practice_challenge.title} next.'
                else:
                    context['lesson_next_action'] = 'This full lesson rep is complete.'
        return context


class ChallengesView(NavigationContextMixin, TemplateView):
    template_name = 'core/challenges.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        challenges = get_challenges()
        challenge_cards = []
        if self.request.user.is_authenticated:
            challenge_ids = [challenge.id for challenge in challenges if hasattr(challenge, 'id')]
            progress_map = {
                item.challenge_id: item
                for item in UserChallengeProgress.objects.filter(
                    user=self.request.user,
                    challenge_id__in=challenge_ids,
                )
            }
            for challenge in challenges:
                challenge_cards.append({
                    'challenge': challenge,
                    'progress': progress_map.get(getattr(challenge, 'id', None)),
                })
        else:
            challenge_cards = [{'challenge': challenge, 'progress': None} for challenge in challenges]
        context['challenges'] = challenges
        context['challenge_cards'] = challenge_cards
        return context


class ChallengeDetailView(NavigationContextMixin, TemplateView):
    template_name = 'core/challenge_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        challenge = get_challenge(kwargs['slug'])
        if challenge is None:
            raise Http404('Challenge not found')

        context['challenge'] = challenge
        context['saved_response'] = challenge.starter_code if hasattr(challenge, 'starter_code') else challenge.get('starter_code', '')
        if hasattr(challenge, 'pk'):
            challenges = get_challenges()
            challenge_slugs = [item.slug if hasattr(item, 'slug') else item['slug'] for item in challenges]
            if challenge.slug in challenge_slugs:
                challenge_index = challenge_slugs.index(challenge.slug)
                context['previous_challenge'] = challenges[challenge_index - 1] if challenge_index > 0 else None
                context['next_challenge'] = challenges[challenge_index + 1] if challenge_index + 1 < len(challenges) else None
                context['challenge_position'] = challenge_index + 1
                context['total_challenges'] = len(challenges)

            if self.request.user.is_authenticated:
                progress, _ = UserChallengeProgress.objects.get_or_create(
                    user=self.request.user,
                    challenge=challenge,
                )
                context['challenge_progress'] = progress
                context['saved_response'] = progress.response_text or challenge.starter_code
                completed_lesson_ids = set(
                    UserLessonProgress.objects.filter(user=self.request.user, is_completed=True).values_list('lesson_id', flat=True)
                )
                completed_challenge_ids = set(
                    UserChallengeProgress.objects.filter(user=self.request.user, is_completed=True).values_list('challenge_id', flat=True)
                )
                challenge_milestones = get_challenge_milestones(
                    challenge.slug,
                    completed_lesson_ids=completed_lesson_ids,
                    completed_challenge_ids=completed_challenge_ids,
                )
                challenge_milestone = next(
                    (item for item in challenge_milestones if item['status'] != 'completed'),
                    challenge_milestones[0] if challenge_milestones else None,
                )
                context['challenge_milestone'] = challenge_milestone
                completion_stack = [
                    {
                        'label': 'Challenge marked complete',
                        'done': progress.is_completed,
                    },
                ]
                if challenge_milestone is not None:
                    completion_stack.append({
                        'label': f'Paired lesson complete: {challenge_milestone["lesson"].title}',
                        'done': challenge_milestone['lesson_completed'],
                    })
                    completion_stack.append({
                        'label': 'Milestone fully complete',
                        'done': challenge_milestone['status'] == 'completed',
                    })
                context['challenge_completion_stack'] = completion_stack
                context['challenge_stack_complete_count'] = sum(1 for item in completion_stack if item['done'])
                if not progress.is_completed:
                    context['challenge_next_action'] = 'Mark this challenge complete next.'
                elif challenge_milestone is not None and not challenge_milestone['lesson_completed']:
                    context['challenge_next_action'] = f'Finish {challenge_milestone["lesson"].title} next.'
                elif challenge_milestone is not None and challenge_milestone['status'] != 'completed':
                    context['challenge_next_action'] = 'Complete the paired lesson to finish this milestone.'
                else:
                    context['challenge_next_action'] = 'This practice rep is fully complete.'
            else:
                context['saved_response'] = challenge.starter_code

        return context


class ProjectsView(NavigationContextMixin, TemplateView):
    template_name = 'core/projects.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = get_projects()
        return context


class TipsView(NavigationContextMixin, TemplateView):
    template_name = 'core/tips.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tips'] = get_tips()
        return context


class CommunityView(NavigationContextMixin, TemplateView):
    template_name = 'core/community.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['community_items'] = get_community_items()
        context['community_posts'] = get_community_posts()
        context['community_post_form'] = kwargs.get('community_post_form') or CommunityPostForm()
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.info(request, 'Create a free account to share a shoutout or question with the community.')
            return redirect('core:community')

        if check_rate_limit(request, 'community_post', limit=5, window_seconds=3600):
            messages.error(request, 'You have posted a lot in the last hour. Please wait a bit before posting again.')
            return redirect('core:community')

        form = CommunityPostForm(request.POST)
        if not form.is_valid():
            return self.render_to_response(self.get_context_data(community_post_form=form))

        post = form.save(commit=False)
        post.user = request.user
        post.save()
        messages.success(request, 'Thanks for sharing! Your post will show up here once it is approved.')
        return redirect('core:community')


class SearchView(NavigationContextMixin, TemplateView):
    template_name = 'core/search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q', '').strip()
        results = search_content(query) if query else {'lessons': [], 'challenges': [], 'projects': []}
        context['query'] = query
        context['results'] = results
        context['result_count'] = sum(len(items) for items in results.values())
        return context


class ResourcesView(NavigationContextMixin, TemplateView):
    template_name = 'core/resources.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['resources'] = get_resources()
        return context


class PrivacyPolicyView(NavigationContextMixin, TemplateView):
    template_name = 'core/privacy_policy.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact_email'] = settings.MARKETING_CONTACT_EMAIL
        context['ga_enabled'] = bool(settings.GA_MEASUREMENT_ID)
        context['recaptcha_enabled'] = bool(settings.RECAPTCHA_SITE_KEY)
        return context


class TermsOfServiceView(NavigationContextMixin, TemplateView):
    template_name = 'core/terms_of_service.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact_email'] = settings.MARKETING_CONTACT_EMAIL
        return context


class MyProgressView(LoginRequiredMixin, NavigationContextMixin, TemplateView):
    template_name = 'core/my_progress.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_user_progress_summary(self.request.user))
        context.update(get_streak_and_badges(self.request.user))
        return context


class InsightsView(LoginRequiredMixin, UserPassesTestMixin, NavigationContextMixin, TemplateView):
    template_name = 'core/insights.html'

    def test_func(self):
        return self.request.user.is_staff

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_engagement_summary())
        return context


class LessonProgressUpdateView(LoginRequiredMixin, View):
    http_method_names = ['post']

    def post(self, request, slug, *args, **kwargs):
        lesson = Lesson.objects.filter(slug=slug, is_published=True).first()
        if lesson is None:
            raise Http404('Lesson not found')

        progress, _ = UserLessonProgress.objects.get_or_create(
            user=request.user,
            lesson=lesson,
        )

        action = request.POST.get('action')
        if action == 'complete':
            progress.is_completed = True
            progress.completed_at = timezone.now()
            progress.save(update_fields=['is_completed', 'completed_at', 'last_viewed_at'])
            challenge = get_lesson_practice_challenge(lesson)
            completed_lesson_ids = set(
                UserLessonProgress.objects.filter(user=request.user, is_completed=True).values_list('lesson_id', flat=True)
            )
            completed_challenge_ids = set(
                UserChallengeProgress.objects.filter(user=request.user, is_completed=True).values_list('challenge_id', flat=True)
            )
            milestone = get_lesson_milestone(
                lesson,
                completed_lesson_ids=completed_lesson_ids,
                completed_challenge_ids=completed_challenge_ids,
            )
            if milestone and milestone['status'] == 'completed':
                messages.success(request, f'Lesson marked complete. {milestone["celebration"]}.')
            elif challenge is not None:
                messages.success(request, f'Lesson marked complete. Next up: {challenge.title} will lock in this milestone.')
            else:
                messages.success(request, 'Lesson marked complete. Nice work.')
        elif action == 'restart':
            progress.is_completed = False
            progress.completed_at = None
            progress.save(update_fields=['is_completed', 'completed_at', 'last_viewed_at'])
            messages.info(request, 'Lesson reset. You can work through it again anytime.')

        return redirect('core:lesson_detail', slug=lesson.slug)


class LessonQuizSubmitView(View):
    http_method_names = ['post']

    def post(self, request, slug, *args, **kwargs):
        lesson = Lesson.objects.filter(slug=slug, is_published=True).first()
        if lesson is None:
            raise Http404('Lesson not found')

        quiz_items = lesson.quiz or []
        if not quiz_items:
            messages.info(request, 'This lesson does not have a quiz yet.')
            return redirect('core:lesson_detail', slug=lesson.slug)

        total_questions = len(quiz_items)
        correct_answers = 0
        unanswered_questions = 0

        for index, item in enumerate(quiz_items):
            submitted_answer = request.POST.get(f'question_{index}')
            if submitted_answer is None:
                unanswered_questions += 1
                continue
            if submitted_answer == str(item.get('answer')):
                correct_answers += 1

        score_percent = int((correct_answers / total_questions) * 100) if total_questions else 0
        passed_quiz = score_percent >= 70 and unanswered_questions == 0

        if request.user.is_authenticated:
            progress, _ = UserLessonProgress.objects.get_or_create(
                user=request.user,
                lesson=lesson,
            )
            progress.quiz_attempts += 1
            progress.last_quiz_score = score_percent
            progress.best_quiz_score = max(progress.best_quiz_score, score_percent)
            if passed_quiz and progress.quiz_passed_at is None:
                progress.quiz_passed_at = timezone.now()
            progress.save(
                update_fields=[
                    'quiz_attempts',
                    'last_quiz_score',
                    'best_quiz_score',
                    'quiz_passed_at',
                    'last_viewed_at',
                ]
            )

        if unanswered_questions:
            messages.warning(
                request,
                f'You answered {total_questions - unanswered_questions} of {total_questions} quiz questions. Finish them all to lock in a passing result.',
            )
        elif passed_quiz:
            messages.success(
                request,
                f'Quiz passed: {correct_answers}/{total_questions} correct ({score_percent}%). Nice work.',
            )
        else:
            messages.info(
                request,
                f'Quiz score: {correct_answers}/{total_questions} correct ({score_percent}%). Review the lesson and try again.',
            )

        if not request.user.is_authenticated:
            messages.info(request, 'Create a free account to save quiz scores and lesson progress.')

        return redirect('core:lesson_detail', slug=lesson.slug)


def _safe_next_redirect(request, fallback):
    next_url = request.POST.get('next')
    if next_url and url_has_allowed_host_and_scheme(
        url=next_url, allowed_hosts={request.get_host()}, require_https=request.is_secure()
    ):
        return redirect(next_url)
    return redirect(fallback)


class ChallengeProgressUpdateView(LoginRequiredMixin, View):
    http_method_names = ['post']

    def post(self, request, challenge_id, *args, **kwargs):
        challenge = Challenge.objects.filter(id=challenge_id, is_published=True).first()
        if challenge is None:
            raise Http404('Challenge not found')

        progress, _ = UserChallengeProgress.objects.get_or_create(
            user=request.user,
            challenge=challenge,
        )

        action = request.POST.get('action')
        response_text = request.POST.get('response_text', '').strip()

        if action == 'reset':
            progress.response_text = ''
            progress.is_completed = False
            progress.completed_at = None
            progress.save(update_fields=['response_text', 'is_completed', 'completed_at', 'last_updated_at'])
            messages.info(request, 'Challenge notes cleared. You can start fresh anytime.')
            return _safe_next_redirect(request, 'core:challenges')

        progress.response_text = response_text

        if action == 'complete':
            progress.is_completed = True
            progress.completed_at = timezone.now()
            progress.save(update_fields=['response_text', 'is_completed', 'completed_at', 'last_updated_at'])
            completed_lesson_ids = set(
                UserLessonProgress.objects.filter(user=request.user, is_completed=True).values_list('lesson_id', flat=True)
            )
            completed_challenge_ids = set(
                UserChallengeProgress.objects.filter(user=request.user, is_completed=True).values_list('challenge_id', flat=True)
            )
            milestones = get_challenge_milestones(
                challenge.slug,
                completed_lesson_ids=completed_lesson_ids,
                completed_challenge_ids=completed_challenge_ids,
            )
            completed_milestone = next((item for item in milestones if item['status'] == 'completed'), None)
            if completed_milestone is not None:
                messages.success(request, f'Challenge saved and marked complete. {completed_milestone["celebration"]}.')
            else:
                messages.success(request, 'Challenge saved and marked complete. Nice work.')
        else:
            progress.is_completed = False
            progress.completed_at = None
            progress.save(update_fields=['response_text', 'is_completed', 'completed_at', 'last_updated_at'])
            messages.success(request, 'Challenge notes saved. Come back and finish when you are ready.')

        return _safe_next_redirect(request, 'core:challenges')


class ChallengeAutosaveView(LoginRequiredMixin, View):
    http_method_names = ['post']

    def post(self, request, challenge_id, *args, **kwargs):
        challenge = Challenge.objects.filter(id=challenge_id, is_published=True).first()
        if challenge is None:
            raise Http404('Challenge not found')

        try:
            payload = json.loads(request.body.decode('utf-8'))
        except (json.JSONDecodeError, UnicodeDecodeError):
            return JsonResponse({'ok': False, 'error': 'Invalid JSON payload.'}, status=400)

        response_text = (payload.get('response_text') or '').strip()
        progress, _ = UserChallengeProgress.objects.get_or_create(
            user=request.user,
            challenge=challenge,
        )
        progress.response_text = response_text
        progress.save(update_fields=['response_text', 'last_updated_at'])

        return JsonResponse(
            {
                'ok': True,
                'saved_at': timezone.localtime(progress.last_updated_at).strftime('%b %d, %Y %I:%M %p'),
            }
        )


def _track_ai_usage(request, feature, outcome, lesson_slug=''):
    if request.session.session_key is None:
        request.session.create()
    EngagementEvent.objects.create(
        event_type=EngagementEvent.EVENT_AI_USAGE,
        page_path=request.path,
        user=request.user if request.user.is_authenticated else None,
        session_key=request.session.session_key or '',
        metadata={
            'feature': feature,
            'outcome': outcome,
            'lesson_slug': lesson_slug,
        },
    )


class AiCodeHintView(View):
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        if check_rate_limit(request, 'code_hint'):
            _track_ai_usage(request, 'code_hint', 'rate_limited')
            return JsonResponse({'ok': False, 'error': 'Hint limit reached for now. Try again later.'}, status=429)

        try:
            payload = json.loads(request.body.decode('utf-8'))
        except (json.JSONDecodeError, UnicodeDecodeError):
            return JsonResponse({'ok': False, 'error': 'Invalid JSON payload.'}, status=400)

        code = (payload.get('code') or '').strip()[:4000]
        if not code:
            return JsonResponse({'ok': False, 'error': 'Add some code first.'}, status=400)

        if not verify_recaptcha(payload.get('recaptcha_token', ''), 'ai_code_hint', request=request):
            return JsonResponse({'ok': False, 'error': 'Verification failed. Please refresh and try again.'}, status=403)

        hint = get_code_hint(
            title=(payload.get('title') or '')[:200],
            goal=(payload.get('goal') or '')[:1000],
            code=code,
            output=(payload.get('output') or '')[:2000],
            is_error=bool(payload.get('is_error')),
        )
        _track_ai_usage(request, 'code_hint', 'error' if hint == FALLBACK_MESSAGE else 'success')
        return JsonResponse({'ok': True, 'hint': hint})


class AiQuizExplainView(View):
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        if check_rate_limit(request, 'quiz_explain'):
            _track_ai_usage(request, 'quiz_explain', 'rate_limited')
            return JsonResponse({'ok': False, 'error': 'Explanation limit reached for now. Try again later.'}, status=429)

        try:
            payload = json.loads(request.body.decode('utf-8'))
        except (json.JSONDecodeError, UnicodeDecodeError):
            return JsonResponse({'ok': False, 'error': 'Invalid JSON payload.'}, status=400)

        lesson_slug = payload.get('lesson_slug') or ''
        lesson = get_lesson(lesson_slug)
        quiz = getattr(lesson, 'quiz', None) if lesson is not None else None
        if quiz is None and isinstance(lesson, dict):
            quiz = lesson.get('quiz')
        quiz = quiz or []

        question_index = payload.get('question_index')
        if not isinstance(question_index, int) or not (0 <= question_index < len(quiz)):
            return JsonResponse({'ok': False, 'error': 'Unknown quiz question.'}, status=400)

        item = quiz[question_index]
        selected_answer = payload.get('selected_answer')
        if not isinstance(selected_answer, int):
            selected_answer = None

        if not verify_recaptcha(payload.get('recaptcha_token', ''), 'ai_quiz_explain', request=request):
            return JsonResponse({'ok': False, 'error': 'Verification failed. Please refresh and try again.'}, status=403)

        explanation = get_quiz_explanation(
            question=item.get('question', ''),
            options=item.get('options', []),
            correct_answer=item.get('answer'),
            selected_answer=selected_answer,
        )
        _track_ai_usage(request, 'quiz_explain', 'error' if explanation == FALLBACK_MESSAGE else 'success', lesson_slug=lesson_slug)
        return JsonResponse({'ok': True, 'explanation': explanation})


class AiTutorChatView(View):
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        if check_rate_limit(request, 'tutor_chat', limit=15):
            _track_ai_usage(request, 'tutor_chat', 'rate_limited')
            return JsonResponse({'ok': False, 'error': 'Chat limit reached for now. Try again later.'}, status=429)

        try:
            payload = json.loads(request.body.decode('utf-8'))
        except (json.JSONDecodeError, UnicodeDecodeError):
            return JsonResponse({'ok': False, 'error': 'Invalid JSON payload.'}, status=400)

        message = (payload.get('message') or '').strip()[:2000]
        if not message:
            return JsonResponse({'ok': False, 'error': 'Type a question first.'}, status=400)

        if not verify_recaptcha(payload.get('recaptcha_token', ''), 'ai_tutor_chat', request=request):
            return JsonResponse({'ok': False, 'error': 'Verification failed. Please refresh and try again.'}, status=403)

        history = payload.get('history')
        if not isinstance(history, list):
            history = []

        lesson_slug = payload.get('lesson_slug') or ''
        lesson = get_lesson(lesson_slug)

        def _field(name):
            if lesson is None:
                return ''
            if isinstance(lesson, dict):
                return lesson.get(name, '')
            return getattr(lesson, name, '')

        reply = get_tutor_reply(
            lesson_title=_field('title'),
            lesson_summary=_field('summary'),
            lesson_explanation=_field('explanation'),
            history=history,
            message=message,
        )
        _track_ai_usage(request, 'tutor_chat', 'error' if reply == FALLBACK_MESSAGE else 'success', lesson_slug=lesson_slug)
        return JsonResponse({'ok': True, 'reply': reply})


@method_decorator(csrf_exempt, name='dispatch')
class EngagementEventCreateView(View):
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        if check_rate_limit(request, 'engagement_event', limit=300, window_seconds=3600):
            return JsonResponse({'ok': False, 'error': 'Too many events.'}, status=429)

        try:
            payload = json.loads(request.body.decode('utf-8'))
        except (json.JSONDecodeError, UnicodeDecodeError):
            return JsonResponse({'ok': False, 'error': 'Invalid JSON payload.'}, status=400)

        event_type = payload.get('event_type')
        if event_type not in dict(EngagementEvent.EVENT_CHOICES):
            return JsonResponse({'ok': False, 'error': 'Unknown event type.'}, status=400)

        lesson = None
        lesson_slug = payload.get('lesson_slug')
        if lesson_slug:
            lesson = Lesson.objects.filter(slug=lesson_slug).first()

        if request.session.session_key is None:
            request.session.create()

        metadata = payload.get('metadata') or {}
        if not isinstance(metadata, dict):
            metadata = {}

        EngagementEvent.objects.create(
            event_type=event_type,
            page_path=(payload.get('page_path') or '')[:255],
            lesson=lesson,
            user=request.user if request.user.is_authenticated else None,
            session_key=request.session.session_key or '',
            metadata={
                **metadata,
                'user_agent': request.META.get('HTTP_USER_AGENT', '')[:255],
            },
        )
        return JsonResponse({'ok': True})

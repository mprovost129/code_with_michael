import random
from datetime import timedelta

from django.db.models import Count, Q
from django.utils import timezone

from . import content
from .models import (
    Challenge,
    CommunityItem,
    CommunityPost,
    EngagementEvent,
    Lesson,
    Module,
    Project,
    Resource,
    Tip,
    UserChallengeProgress,
    UserLessonProgress,
)


def _published_exists(model):
    return model.objects.filter(is_published=True).exists()


def get_modules():
    if _published_exists(Module):
        return list(Module.objects.filter(is_published=True).order_by('number'))
    return content.MODULES


def get_lessons():
    if _published_exists(Lesson):
        return list(
            Lesson.objects.filter(is_published=True)
            .select_related('module')
            .order_by('module__number', 'display_order', 'id')
        )
    return content.LESSONS


def get_lesson(slug):
    lesson = (
        Lesson.objects.filter(is_published=True, slug=slug)
        .select_related('module')
        .first()
    )
    if lesson is not None:
        return lesson
    return content.get_lesson(slug)


def build_shuffled_quiz(quiz):
    shuffled = []
    for item in quiz or []:
        options = list(enumerate(item.get('options', [])))
        random.shuffle(options)
        shuffled.append({
            'question': item.get('question', ''),
            'options': options,
            'explanation': item.get('explanation', ''),
        })
    return shuffled


def get_lesson_practice_challenge(lesson):
    challenge_slug = None
    if hasattr(lesson, 'practice_challenge_slug'):
        challenge_slug = lesson.practice_challenge_slug
    elif isinstance(lesson, dict):
        challenge_slug = lesson.get('practice_challenge_slug')

    if not challenge_slug:
        return None

    return get_challenge(challenge_slug)


def get_practice_lessons_for_challenge(challenge_slug):
    if not challenge_slug:
        return []

    if _published_exists(Lesson):
        return list(
            Lesson.objects.filter(is_published=True, practice_challenge_slug=challenge_slug)
            .select_related('module')
            .order_by('module__number', 'display_order', 'id')
        )

    return [lesson for lesson in content.LESSONS if lesson.get('practice_challenge_slug') == challenge_slug]


def build_lesson_path_cards(lessons):
    cards = []
    for lesson in lessons:
        cards.append({
            'lesson': lesson,
            'practice_challenge': get_lesson_practice_challenge(lesson),
        })
    return cards


def build_path_milestones(lessons, completed_lesson_ids, completed_challenge_ids):
    milestones = []

    for index, lesson in enumerate(lessons, start=1):
        practice_challenge = get_lesson_practice_challenge(lesson)
        lesson_completed = getattr(lesson, 'id', None) in completed_lesson_ids
        challenge_completed = (
            getattr(practice_challenge, 'id', None) in completed_challenge_ids
            if practice_challenge is not None else False
        )

        if lesson_completed and challenge_completed:
            status = 'completed'
            celebration = f'Milestone {index} complete: {lesson.title}'
        elif lesson_completed or challenge_completed:
            status = 'in_progress'
            celebration = f'Milestone {index} underway'
        else:
            status = 'locked'
            celebration = f'Milestone {index} ahead'

        milestones.append({
            'number': index,
            'lesson': lesson,
            'practice_challenge': practice_challenge,
            'lesson_completed': lesson_completed,
            'challenge_completed': challenge_completed,
            'status': status,
            'celebration': celebration,
        })

    return milestones


def get_lesson_milestone(lesson, completed_lesson_ids=None, completed_challenge_ids=None):
    lessons = get_lessons()
    milestones = build_path_milestones(
        lessons,
        completed_lesson_ids or set(),
        completed_challenge_ids or set(),
    )
    lesson_slug = lesson.slug if hasattr(lesson, 'slug') else lesson.get('slug')

    def _lesson_slug(value):
        return value.slug if hasattr(value, 'slug') else value.get('slug')

    return next(
        (item for item in milestones if _lesson_slug(item['lesson']) == lesson_slug),
        None,
    )


def get_challenge_milestones(challenge_slug, completed_lesson_ids=None, completed_challenge_ids=None):
    lessons = get_lessons()
    milestones = build_path_milestones(
        lessons,
        completed_lesson_ids or set(),
        completed_challenge_ids or set(),
    )

    def _challenge_slug(value):
        return value.slug if hasattr(value, 'slug') else value.get('slug')

    return [
        item for item in milestones
        if item['practice_challenge'] is not None
        and _challenge_slug(item['practice_challenge']) == challenge_slug
    ]


def get_challenges():
    if _published_exists(Challenge):
        return list(Challenge.objects.filter(is_published=True).order_by('display_order', 'id'))
    return content.CHALLENGES


def get_challenge(slug):
    challenge = Challenge.objects.filter(is_published=True, slug=slug).first()
    if challenge is not None:
        return challenge
    return next((item for item in content.CHALLENGES if item['slug'] == slug), None)


def get_projects():
    if _published_exists(Project):
        return list(Project.objects.filter(is_published=True).order_by('display_order', 'id'))
    return content.PROJECTS


def get_tips():
    if _published_exists(Tip):
        return list(Tip.objects.filter(is_published=True).order_by('display_order', 'id'))
    return content.TIPS


def get_community_items():
    if _published_exists(CommunityItem):
        return list(CommunityItem.objects.filter(is_published=True).order_by('display_order', 'id'))
    return content.COMMUNITY_ITEMS


def get_community_posts(limit=20):
    return list(
        CommunityPost.objects.filter(is_approved=True)
        .select_related('user')
        .order_by('-created_at')[:limit]
    )


def get_resources():
    if _published_exists(Resource):
        return list(Resource.objects.filter(is_published=True).order_by('display_order', 'id'))
    return content.RESOURCES


def search_content(query):
    query = (query or '').strip().lower()
    if not query:
        return {'lessons': [], 'challenges': [], 'projects': []}

    def matches(*texts):
        return any(query in (text or '').lower() for text in texts)

    def field(item, name):
        return item.get(name, '') if isinstance(item, dict) else getattr(item, name, '')

    lessons = [
        lesson for lesson in get_lessons()
        if matches(field(lesson, 'title'), field(lesson, 'summary'), field(lesson, 'goal'))
    ]
    challenges = [
        challenge for challenge in get_challenges()
        if matches(field(challenge, 'title'), field(challenge, 'prompt'))
    ]
    projects = [
        project for project in get_projects()
        if matches(field(project, 'title'), field(project, 'description'))
    ]
    return {'lessons': lessons, 'challenges': challenges, 'projects': projects}


def get_engagement_summary():
    events = EngagementEvent.objects.select_related('lesson', 'user')
    totals = events.aggregate(
        total_events=Count('id'),
        lesson_views=Count('id', filter=Q(event_type=EngagementEvent.EVENT_LESSON_VIEW)),
        quiz_views=Count('id', filter=Q(event_type=EngagementEvent.EVENT_QUIZ_VIEW)),
        code_runs=Count('id', filter=Q(event_type=EngagementEvent.EVENT_CODE_RUN)),
        successful_runs=Count(
            'id',
            filter=Q(event_type=EngagementEvent.EVENT_CODE_RUN, metadata__status='success'),
        ),
        failed_runs=Count(
            'id',
            filter=Q(event_type=EngagementEvent.EVENT_CODE_RUN, metadata__status='error'),
        ),
        affiliate_clicks=Count('id', filter=Q(event_type=EngagementEvent.EVENT_AFFILIATE_CLICK)),
        shop_cta_clicks=Count(
            'id',
            filter=Q(event_type=EngagementEvent.EVENT_AFFILIATE_CLICK, metadata__link_type='shop_cta'),
        ),
        ai_usage_total=Count('id', filter=Q(event_type=EngagementEvent.EVENT_AI_USAGE)),
        ai_usage_success=Count(
            'id',
            filter=Q(event_type=EngagementEvent.EVENT_AI_USAGE, metadata__outcome='success'),
        ),
        ai_usage_rate_limited=Count(
            'id',
            filter=Q(event_type=EngagementEvent.EVENT_AI_USAGE, metadata__outcome='rate_limited'),
        ),
        ai_usage_errors=Count(
            'id',
            filter=Q(event_type=EngagementEvent.EVENT_AI_USAGE, metadata__outcome='error'),
        ),
    )

    ai_usage_breakdown = list(
        events.filter(event_type=EngagementEvent.EVENT_AI_USAGE)
        .values('metadata__feature')
        .annotate(
            uses=Count('id'),
            successes=Count('id', filter=Q(metadata__outcome='success')),
            rate_limited=Count('id', filter=Q(metadata__outcome='rate_limited')),
            errors=Count('id', filter=Q(metadata__outcome='error')),
        )
        .order_by('-uses')
    )

    lesson_breakdown = list(
        Lesson.objects.filter(engagement_events__isnull=False)
        .distinct()
        .annotate(
            lesson_views=Count(
                'engagement_events',
                filter=Q(engagement_events__event_type=EngagementEvent.EVENT_LESSON_VIEW),
            ),
            quiz_views=Count(
                'engagement_events',
                filter=Q(engagement_events__event_type=EngagementEvent.EVENT_QUIZ_VIEW),
            ),
            code_runs=Count(
                'engagement_events',
                filter=Q(engagement_events__event_type=EngagementEvent.EVENT_CODE_RUN),
            ),
            successful_runs=Count(
                'engagement_events',
                filter=Q(
                    engagement_events__event_type=EngagementEvent.EVENT_CODE_RUN,
                    engagement_events__metadata__status='success',
                ),
            ),
            failed_runs=Count(
                'engagement_events',
                filter=Q(
                    engagement_events__event_type=EngagementEvent.EVENT_CODE_RUN,
                    engagement_events__metadata__status='error',
                ),
            ),
        )
        .order_by('-code_runs', '-lesson_views', 'module__number', 'display_order')[:10]
    )

    resource_click_breakdown = list(
        events.filter(event_type=EngagementEvent.EVENT_AFFILIATE_CLICK)
        .exclude(metadata__resource_title__isnull=True)
        .values('metadata__resource_title')
        .annotate(
            clicks=Count('id'),
            buy_clicks=Count('id', filter=Q(metadata__link_type='buy')),
            details_clicks=Count('id', filter=Q(metadata__link_type='details')),
        )
        .order_by('-clicks')[:10]
    )

    recent_events = list(events.order_by('-created_at', '-id')[:12])
    return {
        'totals': totals,
        'lesson_breakdown': lesson_breakdown,
        'resource_click_breakdown': resource_click_breakdown,
        'ai_usage_breakdown': ai_usage_breakdown,
        'recent_events': recent_events,
    }


def _activity_streaks(activity_dates):
    if not activity_dates:
        return 0, 0

    sorted_dates = sorted(activity_dates)
    longest_streak = 1
    run = 1
    for previous_date, current_date in zip(sorted_dates, sorted_dates[1:]):
        run = run + 1 if (current_date - previous_date).days == 1 else 1
        longest_streak = max(longest_streak, run)

    today = timezone.localtime(timezone.now()).date()
    cursor = today if today in activity_dates else today - timedelta(days=1)
    current_streak = 0
    while cursor in activity_dates:
        current_streak += 1
        cursor -= timedelta(days=1)

    return current_streak, longest_streak


def get_streak_and_badges(user):
    lesson_progress = UserLessonProgress.objects.filter(user=user)
    challenge_progress = UserChallengeProgress.objects.filter(user=user)

    completed_lessons = lesson_progress.filter(is_completed=True).count()
    completed_challenges = challenge_progress.filter(is_completed=True).count()
    total_lessons = Lesson.objects.filter(is_published=True).count() or len(content.LESSONS)
    total_challenges = Challenge.objects.filter(is_published=True).count() or len(content.CHALLENGES)
    perfect_quiz = lesson_progress.filter(best_quiz_score=100).exists()

    activity_dates = set()
    for value in lesson_progress.exclude(completed_at=None).values_list('completed_at', flat=True):
        activity_dates.add(timezone.localtime(value).date())
    for value in challenge_progress.exclude(completed_at=None).values_list('completed_at', flat=True):
        activity_dates.add(timezone.localtime(value).date())

    current_streak, longest_streak = _activity_streaks(activity_dates)

    badges = [
        {
            'key': 'first_lesson',
            'label': 'First Steps',
            'description': 'Complete your first lesson.',
            'earned': completed_lessons >= 1,
        },
        {
            'key': 'halfway_lessons',
            'label': 'Halfway There',
            'description': 'Complete half of the published lessons.',
            'earned': total_lessons > 0 and completed_lessons >= (total_lessons + 1) // 2,
        },
        {
            'key': 'all_lessons',
            'label': 'Lesson Master',
            'description': 'Complete every published lesson.',
            'earned': total_lessons > 0 and completed_lessons >= total_lessons,
        },
        {
            'key': 'first_challenge',
            'label': 'Challenge Accepted',
            'description': 'Complete your first practice challenge.',
            'earned': completed_challenges >= 1,
        },
        {
            'key': 'all_challenges',
            'label': 'Challenge Crusher',
            'description': 'Complete every published challenge.',
            'earned': total_challenges > 0 and completed_challenges >= total_challenges,
        },
        {
            'key': 'quiz_ace',
            'label': 'Quiz Ace',
            'description': 'Score 100% on a lesson quiz.',
            'earned': perfect_quiz,
        },
        {
            'key': 'three_day_streak',
            'label': '3-Day Streak',
            'description': 'Complete a lesson or challenge 3 days in a row.',
            'earned': longest_streak >= 3,
        },
        {
            'key': 'seven_day_streak',
            'label': '7-Day Streak',
            'description': 'Complete a lesson or challenge 7 days in a row.',
            'earned': longest_streak >= 7,
        },
    ]

    return {
        'current_streak': current_streak,
        'longest_streak': longest_streak,
        'badges': badges,
        'earned_badge_count': sum(1 for badge in badges if badge['earned']),
    }


def get_user_progress_summary(user):
    published_lessons = list(
        Lesson.objects.filter(is_published=True)
        .select_related('module')
        .order_by('module__number', 'display_order', 'id')
    )
    progress_items = list(
        UserLessonProgress.objects.filter(user=user)
        .select_related('lesson', 'lesson__module')
        .order_by('-last_viewed_at', 'lesson__module__number', 'lesson__display_order')
    )
    challenge_progress_items = list(
        UserChallengeProgress.objects.filter(user=user)
        .select_related('challenge')
        .order_by('-last_updated_at', 'challenge__display_order', 'challenge__id')
    )
    total_lessons = len(published_lessons)
    completed_lessons = sum(1 for item in progress_items if item.is_completed)
    total_challenges = Challenge.objects.filter(is_published=True).count()
    completed_challenges = sum(1 for item in challenge_progress_items if item.is_completed)
    completed_lesson_ids = {item.lesson_id for item in progress_items if item.is_completed}
    completed_challenge_ids = {item.challenge_id for item in challenge_progress_items if item.is_completed}
    started_lesson_ids = {item.lesson_id for item in progress_items}
    continue_lesson = next((item for item in progress_items if not item.is_completed), None)
    continue_challenge = next((item for item in challenge_progress_items if not item.is_completed), None)
    recommended_next_lesson = next(
        (lesson for lesson in published_lessons if lesson.id not in started_lesson_ids),
        None,
    )
    continue_lesson_challenge = (
        get_lesson_practice_challenge(continue_lesson.lesson)
        if continue_lesson is not None else None
    )
    recommended_next_challenge = (
        get_lesson_practice_challenge(recommended_next_lesson)
        if recommended_next_lesson is not None else None
    )
    path_milestones = build_path_milestones(
        published_lessons,
        completed_lesson_ids,
        completed_challenge_ids,
    )
    completed_milestones = sum(1 for item in path_milestones if item['status'] == 'completed')
    current_milestone = next((item for item in path_milestones if item['status'] != 'completed'), None)
    latest_completed_milestone = next(
        (item for item in reversed(path_milestones) if item['status'] == 'completed'),
        None,
    )
    completion_percent = int((completed_lessons / total_lessons) * 100) if total_lessons else 0

    return {
        'progress_items': progress_items,
        'challenge_progress_items': challenge_progress_items,
        'total_lessons': total_lessons,
        'completed_lessons': completed_lessons,
        'incomplete_lessons': max(total_lessons - completed_lessons, 0),
        'total_challenges': total_challenges,
        'completed_challenges': completed_challenges,
        'continue_lesson': continue_lesson,
        'continue_challenge': continue_challenge,
        'continue_lesson_challenge': continue_lesson_challenge,
        'recommended_next_lesson': recommended_next_lesson,
        'recommended_next_challenge': recommended_next_challenge,
        'path_milestones': path_milestones,
        'completed_milestones': completed_milestones,
        'current_milestone': current_milestone,
        'latest_completed_milestone': latest_completed_milestone,
        'completion_percent': completion_percent,
    }

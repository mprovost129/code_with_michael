from django.db.models import Count, Q

from . import content
from .models import (
    Challenge,
    CommunityItem,
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


def get_resources():
    if _published_exists(Resource):
        return list(Resource.objects.filter(is_published=True).order_by('display_order', 'id'))
    return content.RESOURCES


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

    recent_events = list(events.order_by('-created_at', '-id')[:12])
    return {
        'totals': totals,
        'lesson_breakdown': lesson_breakdown,
        'recent_events': recent_events,
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

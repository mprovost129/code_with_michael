from django.conf import settings
from django.db import models


class OrderedContentModel(models.Model):
    display_order = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ('display_order', 'id')


class Module(models.Model):
    number = models.PositiveIntegerField(unique=True)
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=200)
    duration = models.CharField(max_length=50)
    goal = models.TextField()
    topics = models.JSONField(default=list, blank=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ('number', 'id')

    def __str__(self):
        return f'Module {self.number}: {self.title}'


class Lesson(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='lessons')
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=200)
    summary = models.TextField()
    duration = models.CharField(max_length=50)
    goal = models.TextField()
    explanation = models.TextField()
    starter_code = models.TextField()
    try_it = models.TextField()
    common_mistake = models.TextField()
    mini_challenge = models.TextField()
    expected_output = models.TextField(blank=True)
    practice_challenge_slug = models.SlugField(blank=True)
    quiz = models.JSONField(default=list, blank=True)
    is_featured = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    display_order = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('module__number', 'display_order', 'id')

    def __str__(self):
        return self.title


class Challenge(OrderedContentModel):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=200)
    difficulty = models.CharField(max_length=50)
    prompt = models.TextField()
    hint = models.TextField(blank=True)
    starter_code = models.TextField(blank=True)
    expected_output = models.TextField(blank=True)
    success_checks = models.JSONField(default=list, blank=True)
    reflection_prompt = models.TextField(blank=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Project(OrderedContentModel):
    title = models.CharField(max_length=200)
    description = models.TextField()
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Tip(OrderedContentModel):
    title = models.CharField(max_length=200)
    description = models.TextField()
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class CommunityItem(OrderedContentModel):
    title = models.CharField(max_length=200)
    description = models.TextField()
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class EngagementEvent(models.Model):
    EVENT_LESSON_VIEW = 'lesson_view'
    EVENT_CODE_RUN = 'code_run'
    EVENT_QUIZ_VIEW = 'quiz_view'
    EVENT_PAGE_VIEW = 'page_view'
    EVENT_CHOICES = (
        (EVENT_LESSON_VIEW, 'Lesson view'),
        (EVENT_CODE_RUN, 'Code run'),
        (EVENT_QUIZ_VIEW, 'Quiz view'),
        (EVENT_PAGE_VIEW, 'Page view'),
    )

    event_type = models.CharField(max_length=32, choices=EVENT_CHOICES)
    page_path = models.CharField(max_length=255, blank=True)
    lesson = models.ForeignKey('Lesson', on_delete=models.SET_NULL, null=True, blank=True, related_name='engagement_events')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='engagement_events')
    session_key = models.CharField(max_length=40, blank=True)
    metadata = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at', '-id')

    def __str__(self):
        return f'{self.event_type} @ {self.page_path or "unknown"}'


class EmailSubscriber(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    source = models.CharField(max_length=100, default='homepage')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at', '-id')

    def __str__(self):
        return self.email


class UserLessonProgress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='lesson_progress')
    lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE, related_name='user_progress')
    started_at = models.DateTimeField(auto_now_add=True)
    last_viewed_at = models.DateTimeField(auto_now=True)
    is_completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)
    quiz_attempts = models.PositiveIntegerField(default=0)
    last_quiz_score = models.PositiveSmallIntegerField(default=0)
    best_quiz_score = models.PositiveSmallIntegerField(default=0)
    quiz_passed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ('-last_viewed_at', '-id')
        constraints = [
            models.UniqueConstraint(fields=('user', 'lesson'), name='unique_user_lesson_progress'),
        ]

    def __str__(self):
        return f'{self.user} -> {self.lesson}'


class UserChallengeProgress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='challenge_progress')
    challenge = models.ForeignKey('Challenge', on_delete=models.CASCADE, related_name='user_progress')
    started_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)
    is_completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)
    response_text = models.TextField(blank=True)

    class Meta:
        ordering = ('-last_updated_at', '-id')
        constraints = [
            models.UniqueConstraint(fields=('user', 'challenge'), name='unique_user_challenge_progress'),
        ]

    def __str__(self):
        return f'{self.user} -> {self.challenge}'


class EmailOnboardingDelivery(models.Model):
    STEP_SUBSCRIBER_WELCOME = 'subscriber_welcome'
    STEP_ACCOUNT_WELCOME = 'account_welcome'
    STEP_PRACTICE_NUDGE = 'practice_nudge'
    STEP_CHOICES = (
        (STEP_SUBSCRIBER_WELCOME, 'Subscriber welcome'),
        (STEP_ACCOUNT_WELCOME, 'Account welcome'),
        (STEP_PRACTICE_NUDGE, 'Practice nudge'),
    )

    email = models.EmailField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='onboarding_deliveries')
    subscriber = models.ForeignKey('EmailSubscriber', on_delete=models.SET_NULL, null=True, blank=True, related_name='onboarding_deliveries')
    step = models.CharField(max_length=50, choices=STEP_CHOICES)
    sent_at = models.DateTimeField(auto_now_add=True)
    metadata = models.JSONField(default=dict, blank=True)

    class Meta:
        ordering = ('-sent_at', '-id')
        constraints = [
            models.UniqueConstraint(fields=('email', 'step'), name='unique_email_onboarding_step'),
        ]

    def __str__(self):
        return f'{self.email} - {self.step}'

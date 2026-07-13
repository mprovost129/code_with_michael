from django.contrib import admin

from .models import (
    Challenge,
    CommunityItem,
    CommunityPost,
    EmailOnboardingDelivery,
    EmailSubscriber,
    EngagementEvent,
    Lesson,
    Module,
    PremiumPurchase,
    Project,
    Resource,
    Tip,
    UserChallengeProgress,
    UserLessonProgress,
)


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('number', 'title', 'duration', 'is_published')
    list_filter = ('is_published',)
    search_fields = ('title', 'goal', 'slug')
    ordering = ('number',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'module', 'duration', 'display_order', 'is_featured', 'is_published')
    list_filter = ('is_published', 'is_featured', 'module')
    search_fields = ('title', 'summary', 'goal', 'slug')
    ordering = ('module__number', 'display_order')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Challenge)
class ChallengeAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'difficulty', 'display_order', 'is_published')
    list_filter = ('difficulty', 'is_published')
    search_fields = ('title', 'slug', 'prompt', 'hint')
    ordering = ('display_order',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_order', 'is_published')
    list_filter = ('is_published',)
    search_fields = ('title', 'description')
    ordering = ('display_order',)


@admin.register(Tip)
class TipAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_order', 'is_published')
    list_filter = ('is_published',)
    search_fields = ('title', 'description')
    ordering = ('display_order',)


@admin.register(CommunityItem)
class CommunityItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_order', 'is_published')
    list_filter = ('is_published',)
    search_fields = ('title', 'description')
    ordering = ('display_order',)


@admin.register(CommunityPost)
class CommunityPostAdmin(admin.ModelAdmin):
    list_display = ('user', 'post_type', 'is_approved', 'created_at')
    list_filter = ('post_type', 'is_approved', 'created_at')
    search_fields = ('body', 'user__email', 'user__username')
    ordering = ('-created_at',)
    actions = ['approve_posts']

    @admin.action(description='Approve selected posts')
    def approve_posts(self, request, queryset):
        updated = queryset.update(is_approved=True)
        self.message_user(request, f'{updated} post(s) approved.')


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'best_for', 'display_order', 'is_published')
    list_filter = ('category', 'is_published')
    search_fields = ('title', 'description', 'url', 'best_for', 'tags')
    ordering = ('display_order',)


@admin.register(EngagementEvent)
class EngagementEventAdmin(admin.ModelAdmin):
    list_display = ('event_type', 'lesson', 'page_path', 'user', 'session_key', 'created_at')
    list_filter = ('event_type', 'created_at')
    search_fields = ('page_path', 'session_key', 'lesson__title', 'user__email')
    ordering = ('-created_at',)
    readonly_fields = ('event_type', 'lesson', 'page_path', 'user', 'session_key', 'metadata', 'created_at')


@admin.register(EmailSubscriber)
class EmailSubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'source', 'is_active', 'created_at')
    list_filter = ('source', 'is_active', 'created_at')
    search_fields = ('email', 'first_name')
    ordering = ('-created_at',)


@admin.register(EmailOnboardingDelivery)
class EmailOnboardingDeliveryAdmin(admin.ModelAdmin):
    list_display = ('email', 'step', 'user', 'subscriber', 'sent_at')
    list_filter = ('step', 'sent_at')
    search_fields = ('email', 'user__email', 'subscriber__email')
    ordering = ('-sent_at',)


@admin.register(UserLessonProgress)
class UserLessonProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'lesson', 'is_completed', 'started_at', 'last_viewed_at', 'completed_at')
    list_filter = ('is_completed', 'started_at', 'completed_at')
    search_fields = ('user__email', 'user__username', 'lesson__title')
    ordering = ('-last_viewed_at',)


@admin.register(UserChallengeProgress)
class UserChallengeProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'challenge', 'is_completed', 'started_at', 'last_updated_at', 'completed_at')
    list_filter = ('is_completed', 'started_at', 'completed_at')
    search_fields = ('user__email', 'user__username', 'challenge__title', 'response_text')
    ordering = ('-last_updated_at',)


@admin.register(PremiumPurchase)
class PremiumPurchaseAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount_paid_cents', 'stripe_checkout_session_id', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__email', 'user__username', 'stripe_checkout_session_id', 'stripe_payment_intent_id')
    ordering = ('-created_at',)
    readonly_fields = ('user', 'stripe_checkout_session_id', 'stripe_payment_intent_id', 'amount_paid_cents', 'created_at')

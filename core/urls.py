from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('start-here/', views.StartHereView.as_view(), name='start_here'),
    path('lessons/', views.LessonsView.as_view(), name='lessons'),
    path('lessons/<slug:slug>/', views.LessonDetailView.as_view(), name='lesson_detail'),
    path('lessons/<slug:slug>/progress/', views.LessonProgressUpdateView.as_view(), name='lesson_progress_update'),
    path('lessons/<slug:slug>/quiz/', views.LessonQuizSubmitView.as_view(), name='lesson_quiz_submit'),
    path('my-progress/', views.MyProgressView.as_view(), name='my_progress'),
    path('insights/', views.InsightsView.as_view(), name='insights'),
    path('engagement-events/', views.EngagementEventCreateView.as_view(), name='engagement_event_create'),
    path('challenges/', views.ChallengesView.as_view(), name='challenges'),
    path('challenges/<slug:slug>/', views.ChallengeDetailView.as_view(), name='challenge_detail'),
    path('challenges/<int:challenge_id>/progress/', views.ChallengeProgressUpdateView.as_view(), name='challenge_progress_update'),
    path('challenges/<int:challenge_id>/autosave/', views.ChallengeAutosaveView.as_view(), name='challenge_autosave'),
    path('projects/', views.ProjectsView.as_view(), name='projects'),
    path('tips/', views.TipsView.as_view(), name='tips'),
    path('community/', views.CommunityView.as_view(), name='community'),
    path('resources/', views.ResourcesView.as_view(), name='resources'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('ai/code-hint/', views.AiCodeHintView.as_view(), name='ai_code_hint'),
    path('ai/quiz-explain/', views.AiQuizExplainView.as_view(), name='ai_quiz_explain'),
    path('ai/tutor-chat/', views.AiTutorChatView.as_view(), name='ai_tutor_chat'),
    path('privacy/', views.PrivacyPolicyView.as_view(), name='privacy_policy'),
    path('terms/', views.TermsOfServiceView.as_view(), name='terms_of_service'),
]

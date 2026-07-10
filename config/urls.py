from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from users.views import EmailOrUsernameLoginView, SignUpView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', EmailOrUsernameLoginView.as_view(), name='login'),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('core.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [path('__debug__/', include(debug_toolbar.urls))] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

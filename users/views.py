from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from core.onboarding import send_account_welcome_email

from .forms import EmailOrUsernameAuthenticationForm, SignUpForm


class EmailOrUsernameLoginView(LoginView):
    authentication_form = EmailOrUsernameAuthenticationForm


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('core:start_here')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object, backend='users.backends.EmailOrUsernameBackend')
        send_account_welcome_email(self.object)
        messages.success(self.request, 'Your account is ready. You can sign in with either your email or your username.')
        return response

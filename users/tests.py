import re

from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.core import mail
from django.test import RequestFactory, TestCase
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from core.models import EmailOnboardingDelivery


class UserModelTests(TestCase):
    def test_create_user_generates_username_when_missing(self):
        user = get_user_model().objects.create_user(
            email='learner@example.com',
            password='testpass123',
        )

        self.assertTrue(user.username)
        self.assertEqual(user.email, 'learner@example.com')

    def test_username_is_required_for_signup_form_but_manager_can_generate_one(self):
        user = get_user_model().objects.create_user(
            email='another@example.com',
            password='testpass123',
        )

        self.assertTrue(user.username)


class EmailOrUsernameBackendTests(TestCase):
    def setUp(self):
        self.request_factory = RequestFactory()
        self.user = get_user_model().objects.create_user(
            email='builder@example.com',
            username='builder_mike',
            password='testpass123',
        )

    def test_authenticate_with_email(self):
        request = self.request_factory.post('/accounts/login/')
        authenticated_user = authenticate(request=request, username='builder@example.com', password='testpass123')

        self.assertEqual(authenticated_user, self.user)

    def test_authenticate_with_username(self):
        request = self.request_factory.post('/accounts/login/')
        authenticated_user = authenticate(request=request, username='builder_mike', password='testpass123')

        self.assertEqual(authenticated_user, self.user)


class SignUpViewTests(TestCase):
    def test_signup_creates_user_and_logs_them_in(self):
        response = self.client.post(
            reverse('signup'),
            data={
                'email': 'newlearner@example.com',
                'username': 'new_learner',
                'first_name': 'New',
                'last_name': 'Learner',
                'password1': 'StrongPass123!',
                'password2': 'StrongPass123!',
            },
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(get_user_model().objects.filter(email='newlearner@example.com', username='new_learner').exists())
        self.assertTrue(response.context['user'].is_authenticated)
        self.assertEqual(len(mail.outbox), 1)
        self.assertTrue(
            EmailOnboardingDelivery.objects.filter(
                email='newlearner@example.com',
                step=EmailOnboardingDelivery.STEP_ACCOUNT_WELCOME,
            ).exists()
        )

    def test_signup_rejects_case_insensitive_duplicate_username(self):
        get_user_model().objects.create_user(
            email='existing@example.com',
            username='CodeStudent',
            password='testpass123',
        )

        response = self.client.post(
            reverse('signup'),
            data={
                'email': 'different@example.com',
                'username': 'codestudent',
                'password1': 'StrongPass123!',
                'password2': 'StrongPass123!',
            },
        )

        self.assertContains(response, 'That username is already taken.')


class PasswordResetFlowTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email='resetme@example.com',
            username='reset_me',
            password='OldPass123!',
        )

    def test_password_reset_request_sends_email_with_working_link(self):
        response = self.client.post(
            reverse('password_reset'),
            data={'email': 'resetme@example.com'},
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(mail.outbox), 1)
        match = re.search(r'https?://[^\s]+/reset/[^\s]+', mail.outbox[0].body)
        self.assertIsNotNone(match, 'Reset link not found in email body')

    def test_full_password_reset_flow_allows_login_with_new_password(self):
        self.client.post(reverse('password_reset'), data={'email': 'resetme@example.com'})
        self.assertEqual(len(mail.outbox), 1)

        match = re.search(r'/reset/([^/]+)/([^/\s]+)/', mail.outbox[0].body)
        self.assertIsNotNone(match)
        uidb64, token = match.group(1), match.group(2)

        confirm_url = reverse('password_reset_confirm', kwargs={'uidb64': uidb64, 'token': token})
        get_response = self.client.get(confirm_url, follow=True)
        self.assertEqual(get_response.status_code, 200)

        set_password_url = get_response.redirect_chain[-1][0]
        post_response = self.client.post(
            set_password_url,
            data={'new_password1': 'BrandNewPass456!', 'new_password2': 'BrandNewPass456!'},
            follow=True,
        )

        self.assertEqual(post_response.status_code, 200)
        self.assertContains(post_response, 'password has been set')

        new_password_login = self.client.post(
            reverse('login'),
            data={'username': 'resetme@example.com', 'password': 'BrandNewPass456!'},
        )
        self.assertTrue(new_password_login.wsgi_request.user.is_authenticated)
        self.client.logout()

        old_password_login = self.client.post(
            reverse('login'),
            data={'username': 'resetme@example.com', 'password': 'OldPass123!'},
        )
        self.assertFalse(old_password_login.wsgi_request.user.is_authenticated)

    def test_password_reset_for_unknown_email_does_not_leak_account_existence(self):
        response = self.client.post(
            reverse('password_reset'),
            data={'email': 'doesnotexist@example.com'},
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(mail.outbox), 0)

    def test_reset_link_with_tampered_token_is_rejected(self):
        uidb64 = urlsafe_base64_encode(force_bytes(self.user.pk))
        bad_token = default_token_generator.make_token(self.user)[:-1] + 'x'

        confirm_url = reverse('password_reset_confirm', kwargs={'uidb64': uidb64, 'token': bad_token})
        response = self.client.get(confirm_url, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'invalid')

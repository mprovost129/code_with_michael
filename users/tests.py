from django.contrib.auth import authenticate, get_user_model
from django.core import mail
from django.test import RequestFactory
from django.test import TestCase
from django.urls import reverse

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

from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone

from .models import EmailOnboardingDelivery, EmailSubscriber


def _build_urls():
    base_url = settings.SITE_BASE_URL.rstrip('/')
    return {
        'start_here': f'{base_url}/start-here/',
        'first_lesson': f'{base_url}/lessons/print-basics/',
        'signup': f'{base_url}/accounts/signup/',
        'progress': f'{base_url}/my-progress/',
    }


def send_subscriber_welcome_email(subscriber):
    if EmailOnboardingDelivery.objects.filter(
        email=subscriber.email,
        step=EmailOnboardingDelivery.STEP_SUBSCRIBER_WELCOME,
    ).exists():
        return False

    urls = _build_urls()
    first_name = subscriber.first_name or 'there'
    send_mail(
        subject='Welcome to Code with Michael',
        message=(
            f'Hi {first_name},\n\n'
            'You are officially on the beginner Python list.\n\n'
            'Best next step:\n'
            f'- Start here: {urls["start_here"]}\n'
            f'- Try the first lesson: {urls["first_lesson"]}\n\n'
            'This project is built for small wins, not overwhelm. Start with one lesson, press Run, and change one line.\n'
        ),
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[subscriber.email],
        fail_silently=True,
    )
    EmailOnboardingDelivery.objects.create(
        email=subscriber.email,
        subscriber=subscriber,
        step=EmailOnboardingDelivery.STEP_SUBSCRIBER_WELCOME,
        metadata={'sent_for': 'homepage_signup'},
    )
    return True


def send_account_welcome_email(user):
    if EmailOnboardingDelivery.objects.filter(
        email=user.email,
        step=EmailOnboardingDelivery.STEP_ACCOUNT_WELCOME,
    ).exists():
        return False

    urls = _build_urls()
    first_name = user.first_name or user.username
    send_mail(
        subject='Your Code with Michael account is ready',
        message=(
            f'Hi {first_name},\n\n'
            'Your account is ready.\n\n'
            'You can now:\n'
            f'- Start here: {urls["start_here"]}\n'
            f'- Track your progress: {urls["progress"]}\n'
            f'- Jump into the first lesson: {urls["first_lesson"]}\n\n'
            'You can sign in using either your email or your username.\n'
        ),
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user.email],
        fail_silently=True,
    )
    EmailOnboardingDelivery.objects.create(
        email=user.email,
        user=user,
        step=EmailOnboardingDelivery.STEP_ACCOUNT_WELCOME,
        metadata={'sent_for': 'account_signup'},
    )
    return True


def send_practice_nudge_email(*, subscriber=None, user=None):
    recipient_email = subscriber.email if subscriber else user.email
    if EmailOnboardingDelivery.objects.filter(
        email=recipient_email,
        step=EmailOnboardingDelivery.STEP_PRACTICE_NUDGE,
    ).exists():
        return False

    urls = _build_urls()
    greeting_name = (
        (subscriber.first_name if subscriber else None)
        or (user.first_name if user else None)
        or (user.username if user else None)
        or 'there'
    )
    send_mail(
        subject='Ready for your next Python win?',
        message=(
            f'Hi {greeting_name},\n\n'
            'Quick reminder: the easiest way to build confidence is to come back for one short lesson and one tiny change.\n\n'
            f'- Start here again: {urls["start_here"]}\n'
            f'- Open the first lesson: {urls["first_lesson"]}\n'
        ),
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[recipient_email],
        fail_silently=True,
    )
    EmailOnboardingDelivery.objects.create(
        email=recipient_email,
        user=user,
        subscriber=subscriber,
        step=EmailOnboardingDelivery.STEP_PRACTICE_NUDGE,
        metadata={'sent_at_utc': timezone.now().isoformat()},
    )
    return True

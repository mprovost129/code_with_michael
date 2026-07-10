from django.core.management.base import BaseCommand
from django.utils import timezone

from core.models import EmailOnboardingDelivery, EmailSubscriber
from core.onboarding import send_practice_nudge_email
from users.models import User


class Command(BaseCommand):
    help = 'Send the next onboarding email to subscribers and users who have not received it yet.'

    def handle(self, *args, **options):
        sent_count = 0

        subscribers = EmailSubscriber.objects.filter(is_active=True)
        for subscriber in subscribers:
            has_welcome = EmailOnboardingDelivery.objects.filter(
                email=subscriber.email,
                step=EmailOnboardingDelivery.STEP_SUBSCRIBER_WELCOME,
            ).exists()
            if has_welcome:
                sent_count += int(send_practice_nudge_email(subscriber=subscriber))

        users = User.objects.filter(is_active=True)
        for user in users:
            has_welcome = EmailOnboardingDelivery.objects.filter(
                email=user.email,
                step=EmailOnboardingDelivery.STEP_ACCOUNT_WELCOME,
            ).exists()
            if has_welcome:
                sent_count += int(send_practice_nudge_email(user=user))

        self.stdout.write(self.style.SUCCESS(f'Sent {sent_count} onboarding nudge email(s) at {timezone.now().isoformat()}.'))

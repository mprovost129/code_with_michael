from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_userlessonprogress'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailOnboardingDelivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('step', models.CharField(choices=[('subscriber_welcome', 'Subscriber welcome'), ('account_welcome', 'Account welcome'), ('practice_nudge', 'Practice nudge')], max_length=50)),
                ('sent_at', models.DateTimeField(auto_now_add=True)),
                ('metadata', models.JSONField(blank=True, default=dict)),
                ('subscriber', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='onboarding_deliveries', to='core.emailsubscriber')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='onboarding_deliveries', to=settings.AUTH_USER_MODEL)),
            ],
            options={'ordering': ('-sent_at', '-id')},
        ),
        migrations.AddConstraint(
            model_name='emailonboardingdelivery',
            constraint=models.UniqueConstraint(fields=('email', 'step'), name='unique_email_onboarding_step'),
        ),
    ]

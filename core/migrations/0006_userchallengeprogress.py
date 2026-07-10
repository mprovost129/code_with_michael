from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_userlessonprogress_quiz_fields'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserChallengeProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('started_at', models.DateTimeField(auto_now_add=True)),
                ('last_updated_at', models.DateTimeField(auto_now=True)),
                ('is_completed', models.BooleanField(default=False)),
                ('completed_at', models.DateTimeField(blank=True, null=True)),
                ('response_text', models.TextField(blank=True)),
                ('challenge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_progress', to='core.challenge')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='challenge_progress', to=settings.AUTH_USER_MODEL)),
            ],
            options={'ordering': ('-last_updated_at', '-id')},
        ),
        migrations.AddConstraint(
            model_name='userchallengeprogress',
            constraint=models.UniqueConstraint(fields=('user', 'challenge'), name='unique_user_challenge_progress'),
        ),
    ]

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_emailsubscriber'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserLessonProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('started_at', models.DateTimeField(auto_now_add=True)),
                ('last_viewed_at', models.DateTimeField(auto_now=True)),
                ('is_completed', models.BooleanField(default=False)),
                ('completed_at', models.DateTimeField(blank=True, null=True)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_progress', to='core.lesson')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lesson_progress', to=settings.AUTH_USER_MODEL)),
            ],
            options={'ordering': ('-last_viewed_at', '-id')},
        ),
        migrations.AddConstraint(
            model_name='userlessonprogress',
            constraint=models.UniqueConstraint(fields=('user', 'lesson'), name='unique_user_lesson_progress'),
        ),
    ]

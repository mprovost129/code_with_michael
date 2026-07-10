from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_order', models.PositiveIntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200)),
                ('difficulty', models.CharField(max_length=50)),
                ('prompt', models.TextField()),
                ('hint', models.TextField(blank=True)),
                ('is_published', models.BooleanField(default=True)),
            ],
            options={'ordering': ('display_order', 'id')},
        ),
        migrations.CreateModel(
            name='CommunityItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_order', models.PositiveIntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('is_published', models.BooleanField(default=True)),
            ],
            options={'ordering': ('display_order', 'id')},
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('title', models.CharField(max_length=200)),
                ('duration', models.CharField(max_length=50)),
                ('goal', models.TextField()),
                ('topics', models.JSONField(blank=True, default=list)),
                ('is_published', models.BooleanField(default=True)),
            ],
            options={'ordering': ('number', 'id')},
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_order', models.PositiveIntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('is_published', models.BooleanField(default=True)),
            ],
            options={'ordering': ('display_order', 'id')},
        ),
        migrations.CreateModel(
            name='Tip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_order', models.PositiveIntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('is_published', models.BooleanField(default=True)),
            ],
            options={'ordering': ('display_order', 'id')},
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('title', models.CharField(max_length=200)),
                ('summary', models.TextField()),
                ('duration', models.CharField(max_length=50)),
                ('goal', models.TextField()),
                ('explanation', models.TextField()),
                ('starter_code', models.TextField()),
                ('try_it', models.TextField()),
                ('common_mistake', models.TextField()),
                ('mini_challenge', models.TextField()),
                ('expected_output', models.TextField(blank=True)),
                ('quiz', models.JSONField(blank=True, default=list)),
                ('is_featured', models.BooleanField(default=False)),
                ('is_published', models.BooleanField(default=True)),
                ('display_order', models.PositiveIntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='core.module')),
            ],
            options={'ordering': ('module__number', 'display_order', 'id')},
        ),
        migrations.CreateModel(
            name='EngagementEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_type', models.CharField(choices=[('lesson_view', 'Lesson view'), ('code_run', 'Code run'), ('quiz_view', 'Quiz view'), ('page_view', 'Page view')], max_length=32)),
                ('page_path', models.CharField(blank=True, max_length=255)),
                ('session_key', models.CharField(blank=True, max_length=40)),
                ('metadata', models.JSONField(blank=True, default=dict)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('lesson', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='engagement_events', to='core.lesson')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='engagement_events', to=settings.AUTH_USER_MODEL)),
            ],
            options={'ordering': ('-created_at', '-id')},
        ),
    ]

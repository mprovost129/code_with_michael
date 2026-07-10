from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_emailonboardingdelivery'),
    ]

    operations = [
        migrations.AddField(
            model_name='userlessonprogress',
            name='best_quiz_score',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userlessonprogress',
            name='last_quiz_score',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userlessonprogress',
            name='quiz_attempts',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userlessonprogress',
            name='quiz_passed_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

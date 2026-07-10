from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_challenge_detail_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='reflection_prompt',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='challenge',
            name='success_checks',
            field=models.JSONField(blank=True, default=list),
        ),
    ]

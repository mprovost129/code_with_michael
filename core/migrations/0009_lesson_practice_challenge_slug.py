from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_challenge_guidance_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='practice_challenge_slug',
            field=models.SlugField(blank=True),
        ),
    ]

from django.db import migrations, models
from django.utils.text import slugify


def populate_challenge_slugs(apps, schema_editor):
    Challenge = apps.get_model('core', 'Challenge')

    for challenge in Challenge.objects.all().order_by('id'):
        base_slug = slugify(challenge.title) or f'challenge-{challenge.id}'
        slug = base_slug
        suffix = 2
        while Challenge.objects.exclude(id=challenge.id).filter(slug=slug).exists():
            slug = f'{base_slug}-{suffix}'
            suffix += 1
        challenge.slug = slug
        challenge.save(update_fields=['slug'])


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_userchallengeprogress'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='expected_output',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='challenge',
            name='slug',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AddField(
            model_name='challenge',
            name='starter_code',
            field=models.TextField(blank=True),
        ),
        migrations.RunPython(populate_challenge_slugs, migrations.RunPython.noop),
        migrations.AlterField(
            model_name='challenge',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]

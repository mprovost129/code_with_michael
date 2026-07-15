from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_premiumpurchase'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='challenge_starter_code',
            field=models.TextField(
                blank=True,
                help_text='Starter code shown in the inline mini-challenge editor. Leave blank to reuse starter_code.',
            ),
        ),
        migrations.AddField(
            model_name='lesson',
            name='challenge_expected_output',
            field=models.TextField(
                blank=True,
                help_text='Exact output the learner must produce to auto-complete the lesson via the inline challenge.',
            ),
        ),
    ]

from django.core.management.base import BaseCommand

from core import content
from core.models import Challenge, CommunityItem, Lesson, Module, Project, Tip


class Command(BaseCommand):
    help = 'Load the starter Code with Michael learning content into the database.'

    def handle(self, *args, **options):
        module_map = {}

        for module_data in content.MODULES:
            module, _ = Module.objects.update_or_create(
                slug=module_data['slug'],
                defaults={
                    'number': module_data['number'],
                    'title': module_data['title'],
                    'duration': module_data['duration'],
                    'goal': module_data['goal'],
                    'topics': module_data['topics'],
                    'is_published': True,
                },
            )
            module_map[module.slug] = module

        for index, lesson_data in enumerate(content.LESSONS, start=1):
            Lesson.objects.update_or_create(
                slug=lesson_data['slug'],
                defaults={
                    'module': module_map[lesson_data['module_slug']],
                    'title': lesson_data['title'],
                    'summary': lesson_data['summary'],
                    'duration': lesson_data['duration'],
                    'goal': lesson_data['goal'],
                    'explanation': lesson_data['explanation'],
                    'starter_code': lesson_data['starter_code'],
                    'try_it': lesson_data['try_it'],
                    'common_mistake': lesson_data['common_mistake'],
                    'mini_challenge': lesson_data['mini_challenge'],
                    'expected_output': lesson_data['expected_output'],
                    'practice_challenge_slug': lesson_data.get('practice_challenge_slug', ''),
                    'quiz': lesson_data['quiz'],
                    'is_featured': index == 1,
                    'is_published': True,
                    'display_order': index,
                },
            )

        self._sync_ordered_content(Challenge, content.CHALLENGES)
        self._sync_ordered_content(Project, content.PROJECTS)
        self._sync_ordered_content(Tip, content.TIPS)
        self._sync_ordered_content(CommunityItem, content.COMMUNITY_ITEMS)

        self.stdout.write(self.style.SUCCESS('Starter learning content loaded.'))

    def _sync_ordered_content(self, model, items):
        for index, item in enumerate(items, start=1):
            model.objects.update_or_create(
                title=item['title'],
                defaults={
                    **{key: value for key, value in item.items() if key != 'title'},
                    'display_order': index,
                    'is_published': True,
                },
            )

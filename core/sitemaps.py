from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .services import get_challenges, get_lessons


def _slug(item):
    return item.slug if hasattr(item, 'slug') else item['slug']


def _lastmod(item):
    return getattr(item, 'updated_at', None)


class StaticViewSitemap(Sitemap):
    priority = 0.6
    changefreq = 'weekly'

    def items(self):
        return [
            'core:home',
            'core:start_here',
            'core:lessons',
            'core:challenges',
            'core:projects',
            'core:tips',
            'core:community',
            'core:resources',
        ]

    def location(self, item):
        return reverse(item)


class LessonSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.8

    def items(self):
        return get_lessons()

    def location(self, item):
        return reverse('core:lesson_detail', args=[_slug(item)])

    def lastmod(self, item):
        return _lastmod(item)


class ChallengeSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.6

    def items(self):
        return get_challenges()

    def location(self, item):
        return reverse('core:challenge_detail', args=[_slug(item)])

    def lastmod(self, item):
        return _lastmod(item)

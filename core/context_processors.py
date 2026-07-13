from django.conf import settings

from .content import NAV_PAGES, NAV_PAGES_MORE, SITE_STATS, SOCIAL_LINKS


def analytics(request):
    return {
        'ga_measurement_id': settings.GA_MEASUREMENT_ID,
        'recaptcha_site_key': settings.RECAPTCHA_SITE_KEY,
    }


def site_content(request):
    """Navbar/footer content needed on every page, including auth pages
    (login, signup, password reset) that don't use NavigationContextMixin.
    """
    return {
        'nav_pages': NAV_PAGES,
        'nav_pages_more': NAV_PAGES_MORE,
        'site_stats': SITE_STATS,
        'social_links': SOCIAL_LINKS,
        'contact_email': settings.MARKETING_CONTACT_EMAIL,
    }

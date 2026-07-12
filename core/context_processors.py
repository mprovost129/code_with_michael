from django.conf import settings


def analytics(request):
    return {
        'ga_measurement_id': settings.GA_MEASUREMENT_ID,
        'recaptcha_site_key': settings.RECAPTCHA_SITE_KEY,
    }

import logging

import httpx
from django.conf import settings

logger = logging.getLogger('django')

SITEVERIFY_URL = 'https://www.google.com/recaptcha/api/siteverify'


def is_configured():
    return bool(settings.RECAPTCHA_SITE_KEY and settings.RECAPTCHA_SECRET_KEY)


def verify_recaptcha(token, expected_action, request=None):
    """Verify a reCAPTCHA v3 token via Google's classic siteverify endpoint.

    Returns True when verification passes, or when reCAPTCHA is not configured
    (so the site stays usable before a site key/secret are set up) or Google's
    API is unreachable (fail open — an outage on Google's side should not lock
    out real users; rate limiting is the backstop).
    Returns False only when reCAPTCHA is configured, reachable, and the token is
    missing, invalid, the action doesn't match, or the risk score is too low.
    """
    if not is_configured():
        return True

    if not token:
        return False

    data = {
        'secret': settings.RECAPTCHA_SECRET_KEY,
        'response': token,
    }
    if request is not None:
        data['remoteip'] = request.META.get('REMOTE_ADDR', '')

    try:
        response = httpx.post(SITEVERIFY_URL, data=data, timeout=5.0)
        response.raise_for_status()
        result = response.json()
    except Exception:
        logger.exception('reCAPTCHA verification request failed')
        return True

    if not result.get('success'):
        return False
    if result.get('action') != expected_action:
        return False

    score = result.get('score', 0)
    return score >= settings.RECAPTCHA_MIN_SCORE

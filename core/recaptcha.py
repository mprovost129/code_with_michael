import logging

import httpx
from django.conf import settings

logger = logging.getLogger('django')

ASSESSMENT_URL_TEMPLATE = 'https://recaptchaenterprise.googleapis.com/v1/projects/{project_id}/assessments'


def is_configured():
    return bool(settings.RECAPTCHA_SITE_KEY and settings.RECAPTCHA_SECRET_KEY and settings.RECAPTCHA_PROJECT_ID)


def verify_recaptcha(token, expected_action, request=None):
    """Verify a reCAPTCHA token via Google Cloud Fraud Defense (reCAPTCHA Enterprise).

    Returns True when verification passes, or when reCAPTCHA is not configured
    (so the site stays usable before Google Cloud setup is complete) or Google's
    API is unreachable (fail open — an outage on Google's side should not lock
    out real users; rate limiting is the backstop).
    Returns False only when reCAPTCHA is configured, reachable, and the token is
    missing, invalid, the action doesn't match, or the risk score is too low.
    """
    if not is_configured():
        return True

    if not token:
        return False

    url = ASSESSMENT_URL_TEMPLATE.format(project_id=settings.RECAPTCHA_PROJECT_ID)
    payload = {
        'event': {
            'token': token,
            'siteKey': settings.RECAPTCHA_SITE_KEY,
            'expectedAction': expected_action,
        },
    }
    if request is not None:
        payload['event']['userIpAddress'] = request.META.get('REMOTE_ADDR', '')
        payload['event']['userAgent'] = request.META.get('HTTP_USER_AGENT', '')[:255]

    try:
        response = httpx.post(
            url,
            params={'key': settings.RECAPTCHA_SECRET_KEY},
            json=payload,
            timeout=5.0,
        )
        response.raise_for_status()
        data = response.json()
    except Exception:
        logger.exception('reCAPTCHA assessment request failed')
        return True

    token_properties = data.get('tokenProperties', {})
    if not token_properties.get('valid'):
        return False
    if token_properties.get('action') != expected_action:
        return False

    score = data.get('riskAnalysis', {}).get('score', 0)
    return score >= settings.RECAPTCHA_MIN_SCORE

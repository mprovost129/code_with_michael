# reCAPTCHA setup (v3, score-based)

This site uses classic **reCAPTCHA v3** — invisible, score-based verification
with no checkbox or challenge for users to solve. It's set up through the
standard reCAPTCHA admin console, not Google Cloud Console, and needs no GCP
project or billing.

Until the keys below are set, reCAPTCHA is fully inert — the site works
exactly as it does today, just unverified. There's no rush to do this; do it
whenever you want the extra layer of bot protection on the email signup form
and AI endpoints.

## 1. Register a site

1. Go to the [reCAPTCHA admin console](https://www.google.com/recaptcha/admin/create).
2. Give it a label (e.g. "Code with Michael").
3. Choose **reCAPTCHA v3** as the type.
4. Add your domain(s) — e.g. `codewithmichael.com` and, if you want to test
   locally, `localhost` and `127.0.0.1`.
5. Accept the terms and submit.

## 2. Copy the site key and secret key

The confirmation page shows two values:

- **Site key** — public, used in the browser. This is your `RECAPTCHA_SITE_KEY`.
- **Secret key** — private, used server-side to verify tokens. This is your
  `RECAPTCHA_SECRET_KEY`. Never expose this one in client-side code.

## 3. Add the values to `.env`

```
RECAPTCHA_SITE_KEY=<the site key from step 2>
RECAPTCHA_SECRET_KEY=<the secret key from step 2>
RECAPTCHA_MIN_SCORE=0.5
```

`RECAPTCHA_MIN_SCORE` is the minimum score (0.0–1.0, higher = more
confident it's human) required to pass verification. `0.5` is Google's
recommended default. If you see legitimate users getting blocked, lower it;
if you see obvious bot traffic getting through, raise it.

## 4. Restart the app

Once both values are set and the app restarts, the site will automatically:

- Load the reCAPTCHA v3 JS snippet (`recaptcha/api.js`) on every page (via
  `templates/base.html`)
- Fetch an invisible token before each protected form submission (email
  signup) or AI request (code hint, quiz explain, tutor chat)
- Verify that token server-side against Google's `siteverify` endpoint
  before processing the request

No further code changes are needed — this is purely a configuration step.

## What happens if verification fails or Google's API is unreachable?

By design, this integration **fails open**: if the reCAPTCHA env vars are
blank, or Google's API times out or errors, the request is allowed through
rather than blocked. This favors site availability over strict bot-blocking
— the AI rate limits (`core/ai.py`) are the primary defense against abuse;
reCAPTCHA is a secondary layer that specifically targets scripted/bot
traffic without risking false positives locking out real beginners.

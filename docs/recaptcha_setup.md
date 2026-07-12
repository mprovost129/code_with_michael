# reCAPTCHA setup (Google Cloud Fraud Defense)

Classic reCAPTCHA v3 site keys can no longer be created for new integrations.
Google now issues reCAPTCHA keys through **Google Cloud's reCAPTCHA
Enterprise / Fraud Defense** product, which lives inside a GCP project and
uses a different verification API (`assessments.create` instead of the old
`siteverify` endpoint). The steps below walk through getting the three
values this app needs: `RECAPTCHA_SITE_KEY`, `RECAPTCHA_SECRET_KEY`, and
`RECAPTCHA_PROJECT_ID`.

Until these are set, reCAPTCHA is fully inert — the site works exactly as it
does today, just unverified. There's no rush to do this; do it whenever you
want the extra layer of bot protection on the email signup form and AI
endpoints.

## 1. Create (or pick) a Google Cloud project

1. Go to [console.cloud.google.com](https://console.cloud.google.com/).
2. Create a new project (or reuse an existing one) — e.g. `code-with-michael`.
3. Note the **Project ID** shown on the project dashboard (not the display
   name — the ID, e.g. `code-with-michael-123456`). This is your
   `RECAPTCHA_PROJECT_ID`.

## 2. Enable billing

reCAPTCHA Enterprise requires a billing account attached to the project, even
though usage is free for the first **10,000 assessments per month** (far
more than this site will use). Go to **Billing** in the left nav and link a
billing account.

## 3. Enable the reCAPTCHA Enterprise API

In the console search bar, search for **"reCAPTCHA Enterprise API"** and
click **Enable** for your project.

## 4. Create a reCAPTCHA key

1. Go to **Security → reCAPTCHA Enterprise** in the left nav (or search
   "reCAPTCHA Enterprise" and open the keys page).
2. Click **Create key**.
3. Choose **Website** as the platform.
4. Add your domain(s) — e.g. `codewithmichael.com` and, if you want to test
   locally, `localhost` and `127.0.0.1`.
5. Leave the default scoring settings (checkbox challenge off — this app
   uses score-based, invisible verification).
6. Create the key. The key value shown is your `RECAPTCHA_SITE_KEY`.

## 5. Create an API key for server-side verification

1. Go to **APIs & Services → Credentials**.
2. Click **Create Credentials → API key**.
3. Restrict the key: under **API restrictions**, select **Restrict key** and
   choose **reCAPTCHA Enterprise API** only. This limits what the key can be
   used for if it ever leaks.
4. Copy the key value. This is your `RECAPTCHA_SECRET_KEY`.

## 6. Add the values to `.env`

```
RECAPTCHA_SITE_KEY=<the site key from step 4>
RECAPTCHA_SECRET_KEY=<the API key from step 5>
RECAPTCHA_PROJECT_ID=<the project ID from step 1>
RECAPTCHA_MIN_SCORE=0.5
```

`RECAPTCHA_MIN_SCORE` is the minimum score (0.0–1.0, higher = more
confident it's human) required to pass verification. `0.5` is Google's
recommended default. If you see legitimate users getting blocked, lower it;
if you see obvious bot traffic getting through, raise it.

## 7. Restart the app

Once those three values are set and the app restarts, the site will
automatically:

- Load the reCAPTCHA Enterprise JS snippet on every page (via
  `templates/base.html`)
- Fetch an invisible token before each protected form submission (email
  signup) or AI request (code hint, quiz explain, tutor chat)
- Verify that token server-side against Google's `assessments.create`
  endpoint before processing the request

No further code changes are needed — this is purely a configuration step.

## What happens if verification fails or Google's API is unreachable?

By design, this integration **fails open**: if the reCAPTCHA env vars are
blank, or Google's API times out or errors, the request is allowed through
rather than blocked. This favors site availability over strict bot-blocking
— the AI rate limits (`core/ai.py`) are the primary defense against abuse;
reCAPTCHA is a secondary layer that specifically targets scripted/bot
traffic without risking false positives locking out real beginners.

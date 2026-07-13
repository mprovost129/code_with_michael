# Stripe setup (premium course paywall)

The premium "Python for Absolute Beginners" course is gated behind a
one-time Stripe Checkout purchase. Until the keys below are set, the course
page shows a "coming soon" message instead of a buy button — the rest of
the site is completely unaffected.

## 1. Get your API keys

1. Go to the [Stripe dashboard](https://dashboard.stripe.com/apikeys).
2. Make sure you're in **Test mode** first (toggle in the top right) so you
   can try the whole flow without moving real money.
3. Copy the **Publishable key** (`pk_test_...`) and **Secret key**
   (`sk_test_...`).

## 2. Set up the webhook

The webhook is how Stripe tells the site a payment actually succeeded —
without it, a customer could pay and never get access.

1. Go to [Webhooks](https://dashboard.stripe.com/webhooks) in the Stripe
   dashboard and click **Add endpoint**.
2. Endpoint URL: `https://<your-domain>/premium-course/webhook/`
   (for local testing, see the Stripe CLI note below).
3. Select the event **checkout.session.completed** (that's the only one
   this app listens for).
4. After creating it, click into the endpoint and copy the **Signing
   secret** (`whsec_...`).

### Testing locally

Stripe can't reach `127.0.0.1` directly. Install the
[Stripe CLI](https://docs.stripe.com/stripe-cli) and run:

```
stripe listen --forward-to 127.0.0.1:8000/premium-course/webhook/
```

This prints a temporary `whsec_...` value — use that for local testing
instead of the dashboard one.

## 3. Add the values to `.env`

```
STRIPE_PUBLISHABLE_KEY=pk_test_...
STRIPE_SECRET_KEY=sk_test_...
STRIPE_WEBHOOK_SECRET=whsec_...
PREMIUM_COURSE_PRICE_CENTS=4900
```

`PREMIUM_COURSE_PRICE_CENTS` is the price in cents (4900 = $49.00). Change
it any time — it's read fresh on every checkout, no Stripe dashboard
changes needed since the price is generated inline per session rather than
tied to a pre-created Stripe Product.

## 4. Restart the app

Once all three keys are set, the "Buy Now" button appears on
`/premium-course/` for logged-in users. The flow:

1. User clicks **Buy Now** → redirected to a Stripe-hosted Checkout page.
2. On success, Stripe redirects back to `/premium-course/?purchase=success`
   and (independently, via webhook) confirms the payment server-side.
3. The webhook creates a `PremiumPurchase` row for that user, unlocking the
   full course content permanently — no subscription, no recurring charge.

You can see all purchases in Django admin under **Core → Premium
purchases**.

## 5. Go live

When you're ready to accept real payments: toggle **Live mode** in the
Stripe dashboard, repeat steps 1–2 to get your live keys and a live webhook
endpoint pointed at your real domain, and swap the `.env` values from
`pk_test_.../sk_test_.../whsec_...` to the live equivalents.

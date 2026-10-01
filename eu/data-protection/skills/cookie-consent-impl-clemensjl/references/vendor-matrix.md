# Decision table: third party → category → blocking technique

Categories used here: **necessary** (no consent needed if the strictly-necessary test in Article 5(3) ePD is genuinely met), **functional**, **analytics**, **marketing**. The classification below is the common, defensible default. It is not a legal determination — the final call belongs to the `legal-*` skills and, where the site sells or profiles, to a lawyer.

Techniques, defined once:

- **T1 type-swap** — `type="text/plain"` plus `data-src`, restored by the unblocker (`blocking-layer.md` §1)
- **T2 inject** — not present in markup, appended after the signal (`blocking-layer.md` §2)
- **T3 click-to-load** — first-party placeholder, iframe created on activation (`embeds.md`)
- **T4 self-host** — remove the third party entirely by serving the asset yourself
- **T5 defer to interaction** — load on focus/click of the element that needs it, never on page load
- **T6 replace** — drop the third party for a first-party equivalent

Status as at 2026-08-05. Verify hostnames against a live network trace; vendors add and rename endpoints.

## Analytics and product measurement

| Vendor | Typical hosts | Category | Technique | Notes |
|---|---|---|---|---|
| Google Analytics 4 | `googletagmanager.com`, `google-analytics.com`, `analytics.google.com` | analytics | T2 | Consent Mode signals in addition, not instead (`consent-mode-google.md`) |
| Google Tag Manager | `googletagmanager.com` | depends on contents | T2 | The container itself is a third-party request; gate the container, then gate tags inside it |
| Matomo (cloud) | `*.matomo.cloud` | analytics | T2 | Self-hosted Matomo with anonymised IP and no cookies is the strongest exemption argument, still not automatic |
| Plausible, Fathom, Simple Analytics | vendor domain | analytics | T2 | Cookieless does not equal exempt: the script request is itself access under Art 5(3) |
| Microsoft Clarity, Hotjar, FullStory, Mouseflow | vendor domain | analytics | T2 | Session replay captures input; highest litigation exposure, see `gpc-us.md` |
| Mixpanel, Amplitude, PostHog (cloud) | vendor domain | analytics | T2 | Usually bundled — convert the static import to dynamic `import()` |
| Sentry, Datadog RUM, Bugsnag | vendor domain | analytics | T2 | Error monitoring is frequently claimed as necessary; RUM with a persistent session id is not |

## Advertising and conversion

| Vendor | Typical hosts | Category | Technique | Notes |
|---|---|---|---|---|
| Google Ads / gtag conversion | `googleadservices.com`, `googlesyndication.com` | marketing | T2 | `ad_user_data` and `ad_personalization` required for EEA Customer Match since March 2024 |
| Floodlight / DV360 | `doubleclick.net`, `fls.doubleclick.net` | marketing | T2 | — |
| Meta Pixel | `connect.facebook.net`, `facebook.com/tr` | marketing | T2 | `facebook.com/tr` is a pixel: T1 if it exists as an `<img>` |
| TikTok Pixel | `analytics.tiktok.com` | marketing | T2 | — |
| LinkedIn Insight | `snap.licdn.com`, `px.ads.linkedin.com` | marketing | T2 | — |
| Pinterest, Snapchat, Reddit pixels | vendor domain | marketing | T2 | — |
| Microsoft Advertising UET | `bat.bing.com` | marketing | T2 | — |
| Criteo, Taboola, Outbrain, RTB House | vendor domain | marketing | T2 | Programmatic — check whether TCF is contractually required (`tcf.md`) |
| Affiliate tracking links | varies | marketing | T2 | Tracking links are in scope: EDPB GL 2/2023 v2.0 §3.1 |

## Embeds

| Vendor | Typical hosts | Category | Technique | Notes |
|---|---|---|---|---|
| YouTube | `youtube.com`, `youtube-nocookie.com`, `ytimg.com` | marketing | T3 | Use `youtube-nocookie.com` **after** consent; host the thumbnail yourself |
| Vimeo | `player.vimeo.com`, `vimeocdn.com` | marketing | T3 | `dnt=1` after consent |
| Google Maps | `google.com/maps`, `maps.gstatic.com` | marketing | T3 or T6 | Static self-hosted image plus a link removes the embed entirely |
| OpenStreetMap tiles | `tile.openstreetmap.org` | functional | T3 or T4 | Self-hosted tile cache removes the third party |
| X / Twitter | `platform.twitter.com` | marketing | T3 | Static quote plus a link is usually better |
| Instagram | `instagram.com`, `cdninstagram.com` | marketing | T3 | — |
| Spotify | `open.spotify.com` | marketing | T3 | — |
| SoundCloud | `w.soundcloud.com` | marketing | T3 | — |
| Calendly, Cal.com, TidyCal | vendor domain | functional | T3 | Fallback: link to the booking page |
| Typeform, Jotform | vendor domain | functional | T3 | — |

## Fonts, assets, delivery

| Vendor | Typical hosts | Category | Technique | Notes |
|---|---|---|---|---|
| Google Fonts | `fonts.googleapis.com`, `fonts.gstatic.com` | — | T4 | Self-host; open licence permits it |
| Adobe Fonts / Typekit | `use.typekit.net` | functional | T2 or T6 | Licence usually forbids self-hosting; gate the loader or change family |
| Bunny Fonts, Fontshare | vendor domain | functional | T4 | Still a third-party request |
| Font Awesome CDN | `kit.fontawesome.com`, `use.fontawesome.com` | — | T4 | Self-host the subset actually used |
| jQuery / any script CDN | `cdnjs`, `unpkg`, `jsdelivr` | — | T4 | Bundle it; there is no upside to a public CDN today |
| Gravatar | `gravatar.com` | functional | T4 or T6 | Transmits a hashed email to a third party |

## Functional and support

| Vendor | Typical hosts | Category | Technique | Notes |
|---|---|---|---|---|
| Intercom, Crisp, Tawk, Zendesk, HubSpot chat | vendor domain | functional or marketing | T5 | Launcher is first-party; SDK loads on click. HubSpot chat usually carries marketing tracking |
| reCAPTCHA | `google.com/recaptcha`, `gstatic.com` | necessary (arguable) | T5 | Load on form focus, only on pages with a form |
| hCaptcha, Cloudflare Turnstile | vendor domain | necessary (arguable) | T5 | Turnstile is the least data-hungry of the three |
| Stripe, PayPal, Adyen SDK | `js.stripe.com`, `paypal.com` | necessary in checkout | T5 | Never on non-checkout pages |
| Trustpilot, Google Reviews widget | vendor domain | marketing | T3 | Render cached review text server-side instead |
| Mailchimp, Klaviyo, Brevo forms | vendor domain | marketing | T3 or T6 | A first-party form posting to their API removes the embed |
| Algolia, Typesense search | vendor domain | necessary if search is the requested service | T2 | Search invoked by the user is a strong necessity argument |
| Cloudflare Web Analytics / bot protection | `cloudflareinsights.com`, `challenges.cloudflare.com` | analytics / necessary | T2 / — | Split them: bot protection and the analytics beacon are different things |

## Rules for extending this table

1. **Classify by purpose, not by vendor's self-description.** "Essential for our service" in a vendor's docs is marketing copy.
2. **A cookieless tool is not an exempt tool.** The request and the cache entry are in scope (EDPB GL 2/2023 v2.0 §§37, 50).
3. **Where a first-party equivalent exists, prefer T4 or T6 over gating.** A removed vendor needs no consent, no policy entry and no audit line.
4. **One vendor can span categories.** HubSpot forms are functional, HubSpot tracking is marketing. Gate them separately or the granular banner is a fiction.
5. **Any vendor not on this list defaults to marketing and T2** until someone documents otherwise.

## Checkpoints

- [ ] Every host from the audit trace appears in this table or in a project-specific extension
- [ ] Each entry has a category and a named owner for that classification
- [ ] Every T4/T6 opportunity considered before choosing to gate
- [ ] Vendors spanning categories split into separate gated units
- [ ] Necessity claims (captcha, payment, search) written down with reasoning
- [ ] Table matched against the cookie policy vendor list in both directions
- [ ] `[[MISSING: …]]` raised for any host nobody can identify

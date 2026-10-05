---
name: saas-legal-docs-pooriaarab
title: SaaS legal docs (Terms of Service + Privacy Policy)
description: 'Use when drafting or expanding a SaaS product''s Terms of Service and Privacy Policy pages — especially when a stub needs to become a full document, or when a compliance need (Twilio/A2P SMS toll-free registration, an app-store review, a data-processing request) requires real legal pages. Gives the section-by-section structure of a protective ToS and Privacy Policy, the standard protective-clause stack (''AS IS'' warranty disclaimer, capped limitation of liability, indemnification, third-party-platform + AI-output disclaimers), how to research competitor structure without copying wording (copyright), the entity/governing-law/contact facts to pin down, the SMS/A2P consent language carriers require, and the JSX/marketing-page gotchas. NOT legal advice — always flag that a lawyer should review before the docs are relied on. Triggers: ''write our terms of service'', ''draft a privacy policy'', ''our /terms is a stub'', ''legal pages for the toll-free/A2P review'', ''add CCPA/GDPR
  section'', ''terms and privacy for the app store'', ''protective SaaS terms''.'
author: pooriaarab
author_url: https://github.com/pooriaarab/skills/tree/main/saas-legal-docs
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: data-protection
language: en
---

# SaaS legal docs (Terms of Service + Privacy Policy)

Draft protective, industry-standard ToS + Privacy pages. **You are not a lawyer** — produce a
strong *draft template* and tell the user plainly it needs an attorney's review before they rely
on it (liability caps, entity/jurisdiction specifics, and GDPR/CCPA obligations are where a real
lawyer matters). Never claim certifications (SOC2, ISO, HIPAA) the company doesn't hold.

## Pin down the facts first

Before writing, get these — guessing wrong here is the costly part:
- **Operating legal entity** (the company that legally owns the product) and its registration
  numbers/type. This is often NOT the product name — a product can be a DBA of a foundation/LLC.
- **Registered address**, **contact email(s)** (a general `support@` and a `privacy@` for data
  requests — reuse addresses that actually receive mail; don't invent).
- **Governing law + venue** (the entity's jurisdiction, e.g. "British Columbia and the federal
  laws of Canada; venue Vancouver").
- **Product shape** — what it does, what third-party platforms/APIs it touches, whether it has
  paid plans / credits / free trials, whether it uses AI generation, whether it sends SMS.
- **Processors** actually in use (Cloudflare, Stripe, email/SMS providers, the platforms it
  publishes to) — describe by category; don't over-commit to an exact vendor list that goes stale.

## Research competitor structure — coverage only, never wording

WebFetch a few comparable SaaS legal pages for SECTION COVERAGE and standard-clause patterns
(e.g. Buffer `buffer.com/legal/terms` + `/privacy`, Later, Typefully, the incumbent in your
space). **Copyright: synthesize ORIGINAL prose** covering the same ground in your own words —
never paste their text. Some competitors 404 their legal URLs; that's fine, two good references
are enough to confirm you're not missing a standard section.

## Terms of Service — section checklist

1. Acceptance & eligibility (18+, authority to bind an org). 2. Description of service. 3. Accounts
& security. 4. **Acceptable Use Policy** (no spam/illegal/infringing/hateful content, no violating
third-party platform terms, no scraping/reselling/abuse). 5. **User content & license** — user
keeps ownership; grants a limited license to process/transmit their content to deliver the service;
user is solely responsible for their content and for each platform's rules. 6. **Third-party
platforms & APIs** — not affiliated; features may break when platform APIs change; platform
suspensions aren't your responsibility. 7. **AI-generated content** — output may be inaccurate;
user must review before relying on/publishing it; user owns the responsibility for what they
publish. 8. Fees, billing & credits, refunds, plan changes (omit a free-trial clause if there are
no trials). 9. **SMS/Text messaging terms** (if applicable — see below). 10. Intellectual property
(you own the platform). 11. **Disclaimer of warranties** — "AS IS" and "AS AVAILABLE", no
warranties, to the fullest extent permitted by law. 12. **Limitation of liability** — cap total
liability at the greater of trailing-12-month fees or a small fixed sum (e.g. USD $100); exclude
indirect/incidental/consequential/special damages, lost profits, lost data, and damages from
third-party platform actions — with a carve-out noting consumer-protection law may not permit full
limitation in some jurisdictions. 13. **Indemnification** — user indemnifies the company for their
content and misuse. 14. Termination & suspension (either party; you may suspend for AUP breach).
15. Changes to service and terms. 16. **Governing law & dispute resolution**. 17. Miscellaneous
(severability, entire agreement, assignment, no waiver, force majeure). 18. Contact.

## Privacy Policy — section checklist

Data controller (the legal entity + address); a plain-language summary line; data collected
(account, content, third-party OAuth tokens, usage/analytics, device/log, SMS if applicable); how
used + legal bases; processors/subprocessors (by category); **"we do not sell personal
information"**; international transfers; retention; security; **user rights — a GDPR list for EU
users AND a CCPA/CPRA subsection for California**, with how to exercise them; children (not for
under-16/18); cookies; changes; contact + a privacy-request address. Give each page a visible
"Last updated: <date>" and **keep both pages' dates in sync when you materially change either.**

## SMS / A2P consent language (if the product texts users)

Carriers reviewing a toll-free/A2P registration open the linked Terms + Privacy. They must contain:
consent to receive texts, **message frequency**, **"message & data rates may apply"**, **reply HELP
for help / STOP to opt out**, **"consent is not a condition of purchase"**, and in Privacy the exact
carve-out **"mobile information / SMS consent is never shared with or sold to third parties or
affiliates for marketing."** See the `twilio-number-provisioning` skill for the registration side.

## Marketing-page gotchas (Next.js / JSX content pages)

- Legal pages usually live in the marketing app (e.g. `apps/marketing/src/app/(legal)/{terms,
  privacy}/content.tsx`) — grep the visible page text to find the source. Match the existing
  heading/prose/`Link` structure; expand, don't restructure.
- **Preserve existing sections verbatim** (a prior SMS-consent section, a specific carve-out) when
  expanding a page.
- Watch `react/no-unescaped-entities` — escape apostrophes/quotes in JSX (`&apos;`/`&rsquo;`) as the
  file already does. Run `bun run lint && bun run typecheck` (or the repo's equivalent); pre-commit
  fails on lint ERROR level.
- Standard PR discipline: branch off latest main, `git fetch` before push (review councils
  auto-commit), no AI/co-author trailer, PR body carries a one-line "DRAFT — not legal advice,
  recommend attorney review."

## Judgment calls to surface to the user

Always list these back for confirmation: the **contact email(s)** chosen, the **liability cap
amount**, the **named processors** (esp. if you changed one, like an email vendor), the
**governing-law jurisdiction**, and any clause you included/omitted based on product facts (free
trials, AI, SMS).

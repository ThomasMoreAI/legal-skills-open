---
name: legal-docs
title: Privacy & Terms Generator
description: Generate jurisdiction-aware Privacy Policies and Terms & Conditions for SaaS products, apps, and digital services. Use this skill whenever the user asks to draft, write, generate, update, or review a Privacy Policy, Terms of Service, Terms & Conditions, legal documents, or /legal/ page content for a software product or app. Trigger even if the user just says "I need a privacy policy", "write my T&C", "help with legal docs", "draft my terms", or "what should my privacy policy say" for their app, website, or SaaS. Always use this skill for legal document generation — don't attempt it without consulting this skill first.
author: THHamiltonSmith
author_url: https://github.com/THHamiltonSmith/legal-docs
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: data-protection
language: en
---

# Privacy & Terms Generator

Act as an experienced startup and SaaS lawyer. Be direct, practical, and protective — but write for founders, not courtrooms.

## Required Disclaimer

Include this block at the very top of **every generated document**, every time, no exceptions:

> **Disclaimer:** This document was generated with AI assistance and is provided as a starting point only. It does not constitute legal advice and does not create a lawyer-client relationship. Laws vary by jurisdiction and change over time. You are strongly recommended to have this document reviewed by a qualified legal professional in your country before publishing or relying on it. The tool's author accepts no liability for the use of this output.

---

## Step 1 — Gather Inputs

Before generating anything, ask **all of the following in a single conversational message** — not one question at a time. Frame it as a friendly intake form, not an interrogation.

**Product basics:**
- Product/service name
- Short description of what it does
- Core features — prompt specifically about: user accounts, payments/subscriptions, user-generated content, public-facing pages, AI features, APIs, file uploads, third-party login (OAuth)

**Technical context:**
- Is there a `package.json`, `requirements.txt`, or codebase available to scan? If yes, scan it and apply the Third-Party Inference table below
- If no codebase: ask the user to list their key third-party integrations manually

**Jurisdiction and compliance:**
- Where is the business legally based? (country + state/territory if relevant)
- What law governs the agreement? (e.g. Australian law, Delaware, English law)
- Where does it serve users? (global / Australia-only / EU users included / US users / etc.)
- Any age restrictions or specific user demographics?

**Contact details — never guess, always ask explicitly:**
- Legal/business contact email
- Abuse or complaints contact email (can be same as above)
- Data privacy contact email (can be same as above)
- If GDPR-relevant: is there a Data Protection Officer (DPO)?

**Document metadata:**
- "Last Updated" date — default to today if not specified, but confirm with user
- Version number (optional but recommended)

---

## Third-Party Service Inference

When a `package.json` or import statements are available, scan and infer:

| Package pattern | Inferred service | Privacy policy disclosure |
|---|---|---|
| `stripe`, `@stripe/` | Payments | Stripe (stripe.com/privacy) |
| `@sentry/`, `sentry` | Error tracking | Sentry (sentry.io/privacy) |
| `firebase`, `firebase-admin` | Auth/database | Google Firebase (policies.google.com/privacy) |
| `@aws-sdk`, `aws-sdk` | Cloud infrastructure | Amazon AWS (aws.amazon.com/privacy) |
| `resend`, `nodemailer`, `@sendgrid/`, `sendgrid` | Email delivery | Note the service used |
| `@supabase/`, `supabase` | Auth/database | Supabase (supabase.com/privacy) |
| `posthog-js`, `posthog-node` | Product analytics | PostHog (posthog.com/privacy) |
| `mixpanel`, `amplitude` | Analytics | Note the service used |
| `intercom`, `crisp` | Customer support/chat | Note the service used |
| `@vercel/analytics`, `plausible` | Privacy-friendly analytics | Note the service used |
| `openai`, `@anthropic-ai/`, `replicate` | AI/LLM services | Note the provider |
| `cloudflare` | CDN/security | Cloudflare (cloudflare.com/privacypolicy) |

Present the inferred list to the user for confirmation before including anything in the documents.

---

## Step 2 — Generate Draft

Once inputs are collected, generate both documents (or whichever was requested).

- Use `[ASSUMPTION: …]` inline wherever you filled in something not explicitly provided
- All unknown user-specific values use bold placeholders: **[YOUR_COMPANY_NAME]**, **[CONTACT_EMAIL]**, **[DATE]**
- At the end of each document, include a **Placeholder Checklist** — a list of every placeholder used, so the user can do a final check before publishing

For the required sections in each document, read:
- `references/document-sections.md` — full section list for both T&C and Privacy Policy

---

## Step 3 — Refinement

After generating, offer section-by-section refinement. Each section can be rewritten to be:
- More readable / plain-English
- More legally protective
- More concise
- Customised with product-specific logic (feature limits, abuse cases, subscription tiers)

---

## Output Format

**Default:** Markdown (`.md`)
- `##` for top-level sections, `###` for subsections
- Bullet lists for: data types collected, user rights, third-party services
- Avoid walls of paragraph text where structured lists are cleaner
- Bold all placeholders: **[CONTACT_EMAIL]**

**On request, also offer:**
- HTML snippet for web integration (see Web Integration below)
- `.docx` format note for lawyer review
- `.pdf` for static hosting

### Web Integration Output

When the user wants to integrate at `/legal/privacy` or `/legal/terms`, ask for:
- Their CSS variables or class names (e.g. `--color-text`, heading styles)
- Or a sample of their existing styled HTML

Generate semantic HTML (`<article>`, `<section>`, `<h2>`, `<h3>`, `<ul>`) with scoped class names that slot into their layout. Markdown is the source of truth — HTML is derived from it.

---

## Jurisdiction-Specific Rules

Load the relevant reference file based on where the business operates. Apply all obligations from that jurisdiction automatically — don't wait for the user to ask.

| Jurisdiction | Load | Key additions |
|---|---|---|
| Australia | `references/au-privacy.md` | Privacy Act 1988, APPs 1–13, NDB scheme, ACL statutory guarantees |
| EU / UK | `references/gdpr.md` | Lawful basis, Art. 13 disclosures, user rights, DPO, cookie consent |
| United States | `references/us-privacy.md` | CCPA (California), COPPA (under-13), CAN-SPAM (email) |
| Multi-jurisdiction / Global | Load all relevant files | Apply the most conservative applicable standard as a baseline |

---

## Style Guidelines

- Write for founders and their users — not a courtroom
- Plain English preferred unless legal precision requires specific phrasing
- Use headings and bullets wherever they improve scannability
- Concise but never at the expense of legal protection
- Avoid bloated legalese; use plain equivalents where possible

---

## Constraints

- Never fabricate compliance claims (don't write "this policy is fully GDPR compliant")
- Never auto-populate contact emails, company names, or legal entity names — always ask
- Never omit the disclaimer at the top of every document
- Default to conservative, protective language when in doubt
- Use `[ASSUMPTION: …]` inline for anything filled in without explicit user input

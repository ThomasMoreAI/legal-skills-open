---
name: compliance-audit-the13thnode
title: Compliance Audit Context
description: Generic compliance audit context. Load before any task touching verification tiers, regulated forms, document uploads, identity verification, or anything involving user identity. Also load before any task that might accidentally reintroduce payment processing or regulated contract functionality.
author: The13thNode
author_url: https://github.com/The13thNode/VibeCorp_PromptCEO/tree/main/skills/public/compliance-audit
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: regulatory
language: en
---

# Compliance Audit Context

## Hard deleted — never recreate
Replace these placeholders with your project's forbidden files:
- `[FORBIDDEN_FILE_1]` — e.g. payment processing service
- `[FORBIDDEN_FILE_2]` — e.g. regulated contract page
- `[FORBIDDEN_ROUTE_1]` — e.g. /contract route
- Any payment processing, escrow, deposit holding, or rent collection logic

## Legal lane (what we CAN build)
Adapt these to your regulated domain:
- Identity verification flows using approved third-party OAuth
- Document upload and storage in secure, designated buckets (not general media)
- Viewing/booking scheduling, outcome tracking, analytics
- Handoff cards pointing users to licensed professionals (e.g. brokers, lawyers)

## [TIER_SYSTEM] — Verification Tiers
Replace with your project's access tier structure:
- `[TIER_0]`: Unverified — browse only
- `[TIER_1]`: Basic verified — core actions (view/chat/request)
- `[TIER_2]`: Fully verified — full access via approved identity OAuth

## Identity display rules
Adapt to your jurisdiction's PII requirements:
- `[PII_FIELD_1]` (e.g. National ID): always mask in UI — show partial format only
- `[PII_FIELD_2]` (e.g. Passport number): always mask — first 2 chars + **** + last 1
- `[PII_FIELD_3]` (e.g. OAuth token ID): always mask
- KYC documents: designated secure storage bucket only — never general media bucket

## Compliance checklist — run before every task
- [ ] No payment processing code introduced (grep for: stripe, escrow, DirectDebit, payment_intent)
- [ ] No forbidden files recreated (grep for [FORBIDDEN_FILE_1], [FORBIDDEN_FILE_2])
- [ ] Identity fields masked at every display point
- [ ] Secure documents only in designated secure bucket (not general media bucket)
- [ ] Access-gated actions check tier before allowing
- [ ] Footer disclaimer present on every public-facing page
- [ ] Ratings/reviews comply with local law (e.g. star-only if text reviews are regulated)
- [ ] Occupancy or capacity limits enforced (never above maximum legal limit)

## After every edit
Run: npx tsc --noEmit (or equivalent for your stack)
Zero type errors required before considering task complete.

## Domain-specific notes
Replace this section with your project's regulated domain rules:

### Example: Property rental platform
- Max legal occupancy = number of bedrooms (one person each)
- Free-text rejection reasons are prohibited (anti-discrimination)
- Shared-bedroom listings are prohibited
- Permit/license number required on every listing before publish

### Example: Healthcare platform
- Patient data must not appear in client-side logs
- Appointment data must be HIPAA/GDPR compliant
- Provider credentials must be verified before listings go live

### Example: Financial services
- No unlicensed investment advice in generated content
- All monetary figures must include appropriate disclaimers
- User funds must never be held by the platform

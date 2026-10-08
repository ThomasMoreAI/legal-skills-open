---
name: eu-gdpr-felipepepe-ai-labs
title: When to Use
description: 'Apply GDPR when handling EU personal data. Trigger: personal data, user fields, cookies, tracking, profiles, consent, privacy, DPA, data-subject rights, erasure, portability.'
author: felipepepe-ai-labs
author_url: https://github.com/felipepepe-ai-labs/skills-hub/tree/main/projects/workflow/skills/common/eu-gdpr
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: data-protection
language: en
sources:
- title: Compliance Checklist
  path: references/compliance-checklist.md
- title: Data Categories
  path: references/data-categories.md
- title: Dpia
  path: references/dpia.md
- title: Dsar
  path: references/dsar.md
- title: Legal Basis
  path: references/legal-basis.md
---

## When to Use

- The project stores, processes, or transmits personal data (name, email, IP, location, etc.)
- Registration/login forms with user data are being implemented
- There is tracking, analytics, cookies, or user profiles
- The user mentions privacy, personal data, consent, cookies, RGPD, GDPR
- Sensitive data is handled (health, biometrics, political opinions, sexual orientation)
- There are data transfers outside the EU/EEA

## Scope Guard

- Do NOT use for projects without personal data (e.g. generic public data without identification)
- Do NOT use for backend-only projects without interaction with EU users
- If there is no personal data — there is no applicable GDPR

## Detection

When starting the project, proactively scan:

1. **Database schema**: fields with `email`, `phone`, `address`, `name`, `ip`, `geo`
2. **Forms/inputs**: registration, login, profile, contact forms
3. **Analytics/cookies**: `analytics.js`, `gtag.js`, `facebook pixel`, `hotjar`, `mixpanel`
4. **External APIs**: services that send data outside the EU (Stripe, Sentry, New Relic)
5. **Keywords in code**: `consent`, `cookie_policy`, `privacy`, `data_subject`, `right_to_erasure`
6. **Authentication**: JWT tokens, session cookies, OAuth providers

## Workflow

1. **Classify** data according to `references/data-categories.md`
2. **Evaluate** legal basis for processing (Art. 6) from `references/legal-basis.md`
3. **Apply** the corresponding checklist from `references/compliance-checklist.md`
4. **Generate** a compliance summary at the end of development

## Critical Rules

- **Sensitive data**: Never store special category data without a specific legal basis (Art. 9)
- **Consent**: Must be freely given, specific, informed, and unambiguous. Not pre-checked. Not silent.
- **Data subject rights**: The code MUST support: access, rectification, erasure, portability, objection, restriction
- **Privacy by design**: Data minimization, limited retention, encryption by default
- **International transfers**: Only to countries with adequacy decision or appropriate safeguards
- **DPO**: Mandatory if processing is large-scale sensitive data or systematic surveillance
- **Data breach**: Notify authority within 72 hours, and data subjects without undue delay if high risk

## Output

When reviewing personal data, provide:

```
🇪🇺 EU GDPR Compliance Report
────────────────────────────────
Data Categories: [personal/special/children's]
Legal Basis: [consent/contract/legal_obligation/legitimate_interest]
Processing Locations: [EU-only/international]
Data Subject Rights: [supported rights]
Violations Found: [count]
Recommendations:
  1. [actionable item]
  2. [actionable item]
────────────────────────────────
```

## Resources

- [`references/data-categories.md`](references/data-categories.md) — Data categories and their protection level
- [`references/legal-basis.md`](references/legal-basis.md) — Legal bases for processing
- [`references/compliance-checklist.md`](references/compliance-checklist.md) — Actionable checklist by type
- [`references/dsar.md`](references/dsar.md) — Data Subject Rights guide

---
name: apostille-torlyai
title: /apostille
description: 'Guidance on UK FCDO apostille (legalisation) for Schengen visa

  applications — when needed (foreign-origin civil documents like

  marriage certs, birth certs, divorce decrees), how to apply

  (gov.uk Get a Document Legalised service), cost (£30 standard,

  £100 premium), lead time (5-15 working days standard; 24h premium).

  Identifies the order: apostille first, THEN translate. Use when the

  user has a UK-issued document they need to use abroad, or has a

  foreign-issued document and is unsure what additional step is needed.

  (Schengen-master skills)'
author: torlyai
author_url: https://github.com/torlyai/Schengen-master/tree/main/skills/apostille
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: gb
practice: immigration
language: en
---

# /apostille

## What this skill does

You are the **Schengen-master Document Engineer (apostille specialist)**. You determine whether the user's supporting documents need an **apostille** (also called "legalisation" or "Hague Convention stamp"), guide them through the UK FCDO process, and set realistic time + cost expectations.

The apostille is a single most-painful surprise for Schengen applicants because:

1. It's only required for some applicants (not most UK applicants)
2. When it IS required, it takes 5-15 working days standard
3. It must happen BEFORE translation (apostille on original)
4. UK and Hague Convention countries have a streamlined "apostille" process; non-Hague countries require the slower "legalisation through embassy chain" process

Apply ETHOS principle #4 ("Front-load the audit") — surface this requirement on Day 1 of the application timeline.

## When the apostille is needed

| Scenario | Apostille? |
|---|---|
| UK-issued documents (e.g. UK marriage certificate from GRO) used in a France-Visas application | ⚠️ Usually no — France-Visas accepts UK civil documents at face value |
| Foreign-issued documents (e.g. Chinese birth certificate, Indian marriage certificate) used in UK | ✅ Yes — apostille from country of issue before submission |
| Foreign-issued documents for which the issuing country is a Hague Convention member | ✅ Yes — single apostille |
| Foreign-issued documents from non-Hague Convention countries | ✅ Yes — but it's "legalisation" via embassy chain, not "apostille" |
| Driving licence, passport, photos, bank statements | ❌ No apostille; these are accepted as-is |
| Hotel bookings, flight confirmations | ❌ No |
| Employer letters | ❌ No (in most cases) |

**The simple test:** if the document is a **civil-registry document** (birth, marriage, divorce, death, name change, adoption) AND it was issued in a country other than where you're submitting, apostille is required.

## The UK FCDO process (for UK-issued documents)

Even though most UK applicants don't need apostille for French visas, some do (e.g. for visa to another country, or if French consulate specifically requests). The UK process:

| Service | Cost | Lead time | Notes |
|---|---|---|---|
| **Standard postal service** | £30/document | 5-10 working days | UK government Legalisation Office, post documents to Milton Keynes |
| **Premium (next-day) postal** | £100/document | 24 hours | Add £100 to standard fee; tracked Royal Mail |
| **Premium in-person service** | £100/document | 1-2 working days | Visit Premium service in Milton Keynes |
| **Solicitor / notary service** | £80-150 + £30 FCDO | 5-15 days | Notary completes documents + posts; convenient but slower |

Application: https://www.gov.uk/get-document-legalised

## Apostille on foreign documents (e.g. China, India)

For documents issued outside the UK, the apostille must be obtained in the **country of origin**, typically by:

1. Documents must be originals, not copies
2. Sent to the country's apostille authority (Ministry of Foreign Affairs or equivalent)
3. Apostille added to the original; document is then ready for translation

Lead times:
- **China:** 10-15 working days (longer if document needs notarisation first)
- **India:** 5-10 working days (MEA Apostille)
- **Pakistan:** 15-30 working days (non-Hague — embassy legalisation)
- **Most EU countries:** 5-10 working days
- **US:** 5-15 working days (state-level vs federal)

If the country is NOT a Hague Convention member, the process is "legalisation through embassy chain":

1. Document notarised in origin country
2. Document apostilled (or legalised) at the country's foreign ministry
3. Document legalised at the French embassy in the origin country
4. Used in UK

This chain can take 4-6 weeks.

## Procedure

1. **Inventory the user's documents** — which are civil-registry, foreign-issued, original?
2. **Determine which need apostille** based on the table above
3. **Recommend service tier** based on user's timeline
4. **Calculate timeline impact** — total lead time = apostille + translation (if translation also needed)
5. **Output an action plan**

## Output template

```
APOSTILLE REQUIREMENTS
Applicant: {{APPLICANT_NAME}}
Total documents needing apostille: {{N}}

═════════════════════════════════════════════════════════════════════
DOCUMENTS NEEDING APOSTILLE
═════════════════════════════════════════════════════════════════════

| Document | Origin country | Service | Cost | Lead time |
|----------|----------------|---------|------|-----------|
| Marriage certificate | China | Chinese MFA | (varies) | 10-15 days |
| Birth certificate (child) | India | MEA Apostille | (varies) | 7-10 days |

═════════════════════════════════════════════════════════════════════
DOCUMENTS NOT NEEDING APOSTILLE
═════════════════════════════════════════════════════════════════════

✅ UK-issued passport — no apostille needed
✅ UK bank statement — no apostille needed
✅ TLS appointment confirmation — no apostille needed
✅ UK employer letter — no apostille needed

═════════════════════════════════════════════════════════════════════
CRITICAL TIMELINE NOTE
═════════════════════════════════════════════════════════════════════

⚠️  Apostille MUST happen BEFORE translation.
    Apostille is added to the original document; translate AFTER.
    Plan total lead time = apostille + translation.

For {{DOCUMENT_NAME}}:
   Apostille:    {{N}} days
   Translation:  {{N}} days
   Total:        {{N}} working days minimum

═════════════════════════════════════════════════════════════════════
NEXT STEPS
═════════════════════════════════════════════════════════════════════

1. Begin apostille process immediately for {{LIST}}
2. Once apostille received, run /translate-doc
3. Run /timeline-planner to confirm timing still fits trip date
4. Run /audit-application after both apostille + translation in hand
```

## Routing rules

| Situation | Suggest next |
|---|---|
| No documents need apostille | Skip; proceed to `/document-checklist` or `/audit-application` |
| Apostille needed + tight timeline | `/timeline-planner` — possibly recommend delay |
| Apostille obtained → next step | `/translate-doc` (if foreign-language) or directly to documents |
| Document is from non-Hague country | Flag legalisation-chain process; longer timeline |
| User has original abroad with family | Hand the original to a representative in origin country; can be done by power of attorney |

## Common pitfalls

| Pitfall | Why it hurts | Fix |
|---|---|---|
| Translating before apostille | Apostille goes on original; loose translation page risks rejection | Apostille first, translate the apostilled doc second |
| Using a copy for apostille | Apostille only on originals (or certified copies) | Use original; if lost, get duplicate from issuing authority |
| Standard postal mid-peak | 10+ working days during summer | Pay premium if timeline tight |
| Notary service "completing apostille" | Notary stamp is NOT apostille; needs FCDO step | Confirm notary will post to FCDO; not just notarise |
| Sending originals to FCDO without copies | If lost, no backup | Photocopy all docs before posting |
| Assuming UK marriage cert needs apostille for French visa | Usually NOT needed; UK civil docs accepted | Only apostille if French consulate specifically asks |
| Apostille on photocopy not certified | Rejected | Use original or certified copy first |

## Authoritative sources

- UK FCDO Get a Document Legalised — https://www.gov.uk/get-document-legalised — verified 2026-05-24
- Hague Convention member list — https://www.hcch.net/en/instruments/conventions/status-table/?cid=41 — verified 2026-05-24
- Chinese MFA apostille (China-Hague members since 2026) — http://cs.mfa.gov.cn — verified 2026-05-24
- Indian MEA Apostille — https://www.mea.gov.in — verified 2026-05-24

## Notes for maintainers

- China joined the Hague Convention in 2023. Chinese documents are now apostilled (not legalised). Pre-2023 references may be outdated.
- For users from non-Hague countries (e.g. Bangladesh, Pakistan), legalisation-via-embassy-chain can take 6+ weeks. Flag aggressively in `/timeline-planner`.
- Premium FCDO 24h service is real and works — recommend when applicant is panicking and visa is in 4-6 weeks.
- For multi-country applicants (e.g. UK + Hong Kong-issued birth cert), each country's documents need their country's apostille.
- Apostille is not required on UK-issued documents for French Schengen visa applications in 99% of cases. Don't add unnecessary cost.
- If French consulate specifically requests apostille on UK documents (rare), proceed with UK FCDO process; this happens occasionally for unusual cases.
- For applicants whose passport country has dual citizenship complications, the apostille rules may apply to the passport country, not the residency country.

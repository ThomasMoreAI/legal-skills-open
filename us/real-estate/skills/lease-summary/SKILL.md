---
name: lease-summary
title: Commercial Lease Summary
description: Summarizes U.S. commercial lease agreements into structured transactional abstracts. Use when asked for a commercial lease summary, lease abstract, key lease terms, rent schedule review, default/termination analysis, or lease handoff. Produces party-to-obligation mappings, financial mechanics, risk flags, and critical date calendars.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/lease-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: real-estate
language: en
tags: [summarization, summary, transactional]
---

# Commercial Lease Summary

Produces a structured, party-responsible breakdown of a U.S. commercial lease for deal execution and ongoing administration.

## Prerequisites

- Complete lease document with all attachments, exhibits, and definitions
- All amendments, riders, side letters, extensions, and modification agreements
- Governing law / jurisdiction (infer from internal evidence if absent; mark `ASSUMED: [jurisdiction]`)
- Business context: landlord vs. tenant roles; note any lender, guarantor, master tenant, or affiliate involvement
- Flag missing-text assumptions separately for counsel review

## Workflow

1. Extract parties, lease identity, jurisdiction, governing law
2. Capture baseline business terms before risk-heavy clauses
3. Normalize key definitions (Premises, CAM, Base Rent, Additional Rent, Term, etc.)
4. Build financial mechanics as formulas, not prose
5. Map each right/obligation to party + triggering condition
6. Flag ambiguity, missing provisions, and atypical clauses
7. Compile deadline calendar and counsel action items

## Output Structure

| Section | Key Elements | Format |
| --- | --- | --- |
| Executive Snapshot | Parties, premises, lease type, governing law, date, risk profile, immediate action items | 1–3 lines each |
| Term & Premises | Commencement, expiration, renewal, holdover, grace periods | `date / option / condition / election window` |
| Financial Terms | Base rent, CAM, taxes, insurance pass-throughs, % rent, escalation, deposits | Formula table: `obligation / amount-formula / frequency / due date / escalation / cap-floor / party` |
| Use & Operations | Permitted/prohibited use, assignment, signage, hours, access | `party / condition / remedy` |
| Maintenance & Repairs | Structural, systems, common areas, HVAC, roof, TI | Responsibility matrix |
| Insurance & Liability | Coverages, limits, additional insureds, waivers, indemnity | `policy type / limit / party / trigger` |
| Default & Remedies | Events of default, cure, notices, self-help, damages | `event / notice / cure window / remedy` |
| Special Provisions | SNDA, co-tenancy, kick-out, exclusivity, ROFR, options | `provision / risk level / practical impact` |
| Missing/Unusual Terms | Missing clauses, drafting conflicts, ambiguity | `risk / reason / impact / recommended action` |
| Critical Dates | Rent commencement, notice deadlines, option windows, renewals | `date / action / responsible party / status` |
| Obligation Heat Map | High / Moderate / Low risk items | Grouped by severity |
| Counsel Action Items | Items requiring legal follow-up | Bulleted list |

## Completion Checklist

- [ ] Every obligation names a responsible party
- [ ] Every amount includes value or calculation method
- [ ] Every trigger has a date/time or event condition
- [ ] Every special clause has practical business consequence noted
- [ ] Missing data labeled `UNAVAILABLE` (not silently inferred)

## Rules

- Always return structured output with party-to-obligation mapping — no narrative-only summaries
- Preserve exact contractual numbers, percentages, formulas, and escalation indices
- Use neutral language; avoid legal conclusions unless text directly supports them
- Distinguish absolute vs. conditional rights (e.g., termination contingent on lender approval)
- Flag boilerplate vs. custom-negotiated clauses by context
- Conflicting clauses: quote both sections, flag as `RECONCILIATION NEEDED`
- Uncertain statutes or citations: append `[VERIFY]`
- Flag for counsel review if missing: casualty allocation, environmental indemnity carve-outs, non-disturbance, landlord lien treatment, assignment exceptions

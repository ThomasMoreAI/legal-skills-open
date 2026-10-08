---
name: draft-schedule-annex-builder-sboghossian
title: Schedule / Annex Builder
description: Use when building, structuring, or populating schedules, annexes, or exhibits to be attached to any principal contract. Covers MSA/SOW, share purchase agreements, leases, employment contracts, and any other instrument where voluminous, fact-specific, or frequently-updated material belongs outside the body. Ensures correct numbering, cross-referencing, conflict-of-terms hierarchy, and amendment mechanics across MENA and common-law contexts.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-schedule-annex-builder
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Schedule / Annex Builder

Schedules, annexes, and exhibits house contract content that is voluminous, fact-specific, technical, or likely to change without requiring re-execution of the principal agreement. A well-structured annex architecture makes the contract leaner, easier to navigate, and simpler to amend over the life of the relationship.

## When to use this

- Any drafting task that produces a principal agreement requiring supporting detail (SPA, MSA, SOW, lease, SHA, employment contract, loan agreement)
- When the user has a list of items (pricing, specifications, personnel, procedures) that belong in a schedule rather than the body
- When reviewing an agreement that currently embeds schedule-type content inline and needs restructuring
- When a party requests a standalone amendment to a schedule without re-executing the full agreement

## Inputs

| Input | Why it matters | Default |
|---|---|---|
| Parent contract type | Determines the standard schedule set | Must provide |
| Schedule content | Raw material to be organized into the schedule | Must provide |
| Conflict-of-terms preference | Which prevails — body or schedule — if they conflict | Body prevails unless otherwise stated |
| Amendment mechanism | How this schedule can be amended later | Mutual written agreement |
| Language | For MENA bilingual contracts | English primary; Arabic where required by law |

## Common Schedule Sets by Contract Type

### MSA / SOW Pack

| Schedule | Content |
|---|---|
| Schedule 1 | Form of SOW / project order |
| Schedule 2 | Pricing and rate card |
| Schedule 3 | Service Level Agreement (SLA) and credits |
| Schedule 4 | Security and data-protection measures |
| Schedule 5 | Approved sub-contractors |
| Schedule 6 | Change-control procedure |

### Share Purchase Agreement (SPA)

| Schedule | Content |
|---|---|
| Disclosure Schedule | Disclosures against each representation and warranty — the heart of any M&A deal; omissions create indemnity exposure |
| Capitalization Schedule | Full cap table pre- and post-closing |
| Working Capital Target | Agreed methodology plus sample calculation |
| Schedule of Material Contracts | Contracts requiring consent to assignment on change of control |
| IP Schedule | Registered and unregistered IP assets |
| Real Estate Schedule | Owned and leased property |
| Employees Schedule | Key employees, change-of-control payments, severance exposure |
| Tax Schedule | Pre-closing tax liabilities, ongoing disputes |

### Commercial Lease

| Schedule | Content |
|---|---|
| Schedule 1 | Premises plans and floor plans (survey quality) |
| Schedule 2 | Inventory and condition report at commencement |
| Schedule 3 | Permitted use (precise, not general "office use") |
| Schedule 4 | Service-charge methodology and cap |
| Schedule 5 | Fit-out specification and tenant works |

### Employment Contract

| Schedule | Content |
|---|---|
| Schedule 1 | Job description and reporting line |
| Schedule 2 | Compensation breakdown (base, variable, benefits, EOSG formula) |
| Schedule 3 | Benefits summary |
| Schedule 4 | Restrictive covenant scope (geographic, duration, activities) |

### Shareholders' Agreement (SHA)

| Schedule | Content |
|---|---|
| Schedule 1 | Reserved matters list |
| Schedule 2 | Initial cap table |
| Schedule 3 | Anti-dilution calculation methodology |
| Schedule 4 | Drag-along and tag-along mechanics |
| Schedule 5 | Information rights package |

### Loan / Credit Facility

| Schedule | Content |
|---|---|
| Schedule 1 | Conditions precedent checklist |
| Schedule 2 | Drawdown notice form |
| Schedule 3 | Interest and fee schedule |
| Schedule 4 | Financial covenants and definitions |
| Schedule 5 | Form of security documents |

## Document Structure

### Individual Schedule Format

```
SCHEDULE [NUMBER]
[TITLE]

This Schedule is incorporated into and forms part of the [Agreement Title] dated [Date] between:
[Party A] and [Party B].

[Content organized with clear headings, tables, and numbered items]

[Signature blocks if the schedule requires separate sign-off (rare)]
```

### In the Principal Agreement — Integration Clauses

1. **Definition clause**: "Schedules means the schedules attached to this Agreement, each of which forms an integral part of this Agreement."
2. **Incorporation clause**: "The Schedules are incorporated into and form part of this Agreement."
3. **Conflict clause**: "In the event of any inconsistency between the body of this Agreement and any Schedule, the body shall prevail unless the relevant Schedule expressly states otherwise." (Or vice versa for technical specifications.)
4. **Cross-reference format**: Use "as set out in Schedule [X]" or "in accordance with Schedule [X]" — never "as discussed" or "per the attached."

## Drafting Principles

1. **Number consecutively**: Schedule 1, Schedule 2, Schedule 3 — avoid lettered schedules (A, B, C) unless the jurisdiction convention requires it (some UAE standard forms use letters).
2. **Cross-reference with precision**: The body of the agreement must name each schedule once and explain what it is. Orphaned schedules (attached but never referenced) create ambiguity.
3. **Define schedule contents in the body**: A one-line description in the body before the full detail in the schedule — the contract should be intelligible without reading the schedules first.
4. **Amendment mechanism**: State explicitly in the schedule header or in the agreement body how this schedule can be updated — mutual written agreement signed by both parties is the default. Some schedules (pricing, approved vendor lists) are legitimately updated by unilateral notice with a period for objection.
5. **Conflict hierarchy**: If body and schedule conflict, pick a winner and state it. The body-prevails default protects the lawyer who drafted the body; schedule-prevails is appropriate for technical specifications or pricing annexes where the schedule is the authoritative source.
6. **Version control**: Include a "version" or "dated" field in the schedule header so future amendments can refer to "Schedule 2 dated [X]" being replaced by "Schedule 2 dated [Y]."
7. **Language**: In jurisdictions requiring Arabic (UAE, KSA), schedules must also be bilingual. If only the body is translated, the Arabic courts may give less weight to an untranslated schedule.

## Jurisdictional Notes

| Jurisdiction | Key point |
|---|---|
| UAE (federal) | Arabic is the official language of courts; ensure schedules are bilingual for any agreement likely to be litigated onshore. Registration requirements (e.g., Ejari for leases) must reflect schedule content. |
| KSA | Ministry of Commerce and SAGIA-licensed entities often require schedules to employment and commercial contracts in Arabic. |
| DIFC / ADGM | English contracts; schedules follow English-law conventions; no Arabic requirement inside the financial free zones. |
| LB | Bilingual (Arabic/French) standard for commercial contracts; notarized instruments require both languages in the notarial deed body and any attached schedule. |
| EG | Arabic is the official language; foreign-language schedules should have certified Arabic translations for court use. |

## Common Mistakes

- **"To be agreed" placeholders** — a schedule that says "to be agreed" is not binding. If the content is material (pricing, scope), finalize before signature or mark the agreement "subject to finalization of Schedule [X]."
- **Undefined schedule references** — referring to "the technical specification attached" without formally calling it Schedule 3 creates disputes about whether it's incorporated.
- **Schedule as contract** — a schedule is not a standalone contract; it needs the principal agreement's boilerplate (governing law, dispute resolution). Reference back explicitly.
- **Outdated floor plans** — in leases, using stale floor plans (wrong square footage) leads to rent disputes. Always attach the current, surveyed plan.
- **Disclosure schedule under-populated** — in M&A, a thin disclosure schedule leaves the Seller exposed to warranty claims. A Buyer who negotiates good reps but gets a skeletal disclosure schedule has strong indemnity remedies.

## Related skills

- [[draft-msa]]
- [[draft-sow]]
- [[draft-sla]]
- [[draft-share-purchase-agreement]]
- [[draft-shareholders-agreement]]
- [[draft-employment-contract]]
- [[draft-lease-agreement]]

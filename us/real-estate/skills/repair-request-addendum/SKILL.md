---
name: repair-request-addendum
title: Repair Request Addendum
description: 'Drafts a Repair Request Addendum modifying an existing residential or commercial lease to establish enforceable repair obligations with timelines, cost allocation, and remedies. Cross-references original lease provisions to avoid conflicts. Use when formalizing repair requests, drafting lease addenda for maintenance or habitability issues, or documenting landlord-tenant repair agreements. Trigger keywords: repair addendum, lease repair amendment, habitability repair, maintenance addendum, repair-and-deduct, rent abatement.'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/repair-request-addendum
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: real-estate
language: en
tags: [agreement, drafting, transactional]
---

# Repair Request Addendum

Draft an execution-ready addendum to an existing lease establishing enforceable repair obligations, timelines, cost allocation, and remedies.

## Prerequisites

1. **Original lease** — execution date, parties, property address, maintenance/repair provisions, notice requirements, warranty clauses.
2. **Repair documentation** — inspection reports, photos, contractor estimates, code violation notices, prior correspondence with dates.
3. **Party information** — full legal names (matching original lease), entity type if applicable, current addresses.
4. **Agreed terms** — responsibility allocation, timeline expectations, financial arrangements.

If the original lease is not provided, request it before proceeding — the addendum must reference and integrate into the existing contractual framework.

## Output Structure

Draft a complete, numbered addendum with these sections.

### Required Sections

| Section | Key Content |
|---|---|
| Recitals & Integration | Party names (exact from lease); lease execution date, term, property address; integration and supersession clauses (addendum controls re repairs only; all other terms preserved) |
| Repair Schedule | Itemized table: item #, location, defect description, date reported, category (habitability / code violation / deferred maintenance / wear-and-tear / tenant-caused), supporting docs, priority (urgent / standard / cosmetic) |
| Responsibility & Timeline | Per item: responsible party with basis (lease term, implied warranty, statute, agreement); commencement and completion deadlines; licensed contractor requirement; tenant approval rights over contractor selection |
| Financial Terms | Cost allocation; rent abatement (amount, dates, temporary vs permanent, forgiven vs deferred); repair-and-deduct provisions; escrow or advance-with-reimbursement mechanics; cost overrun approval threshold; security deposit interaction |
| Access & Disruption | Notice period and hours for landlord entry; tenant cooperation obligations; temporary relocation provisions if substantial disruption (alternative housing, moving costs, rent abatement); occupied vs vacant conditions |
| Remedies — Landlord Default | Rent abatement amount and trigger; repair-and-deduct rights with cap; lease termination for material breach; applicable statutory remedies |
| Remedies — Tenant Default | Interference with access remedies; tenant-caused damage cost responsibility |
| Contingencies & Disputes | Procedure for additional discovered repairs; permit/regulatory process; change order procedures; escalation ladder: negotiation → third-party inspection → expedited mediation → litigation |
| Collateral Terms (if applicable) | Lease extension for improvements; post-repair rent adjustment; landlord repair warranties; tenant forward maintenance obligations |
| General Provisions & Execution | Governing law (match original lease); severability; written-amendment requirement; signature blocks with printed name, title, date; notary/witness lines if warranted |

### Template

```text
REPAIR REQUEST ADDENDUM
TO LEASE AGREEMENT DATED [DATE]

Landlord: [Full Legal Name], [Address]
Tenant:   [Full Legal Name], [Address]
Property: [Address, Unit]

REPAIR SCHEDULE

Item | Location       | Description         | Reported  | Category      | Priority
1    | [Unit/area]    | [Defect and scope]  | [Date]    | [Category]    | [Priority]
2    | ...            | ...                 | ...       | ...           | ...

RESPONSIBILITY AND TIMELINE

Item | Responsible Party | Basis          | Start By   | Complete By | Contractor
1    | Landlord          | [Lease §X]     | [Date]     | [Date]      | Licensed/insured
2    | ...               | ...            | ...        | ...         | ...

FINANCIAL TERMS
[Cost allocation, rent abatement, repair-and-deduct provisions per item]

ACCESS
Notice: [X] hours written notice; access hours [X:00–X:00]
Relocation: [If applicable — terms]

REMEDIES
[Landlord default and tenant default provisions]

GENERAL
Governing Law: State of [State]
This Addendum is incorporated into and inseparable from the Lease.
Where inconsistent with the Lease regarding repairs, this Addendum controls.
All other terms of the Lease remain in full force and effect.

LANDLORD: _________________________  Date: ____________
TENANT:  _________________________  Date: ____________

[NOTARY ACKNOWLEDGMENT — if required]
```

### Compliance Checklist

- [ ] Party names and lease details match original lease exactly.
- [ ] Repairs categorized by legal character (habitability vs cosmetic).
- [ ] Habitability/safety items have shortened statutory deadlines.
- [ ] Cost allocation and abatement terms are specific and calculable.
- [ ] Access provisions comply with jurisdiction notice requirements.
- [ ] Remedies do not waive non-waivable statutory tenant protections.
- [ ] Entity landlord signature authority verified (authorized representative with title).
- [ ] Governing law and dispute resolution match or supplement original lease.
- [ ] Advisory language included recommending independent legal counsel.

## Guidelines

- **Cross-reference original lease** language on repair responsibilities, notice requirements, and remedies — do not create conflicts.
- **Categorize by legal character** — habitability and code violations carry mandatory landlord obligations and expedited timelines in most jurisdictions; cosmetic items may be negotiable.
- **Jurisdiction awareness**: Implied warranty of habitability standards, repair-and-deduct statutes, and notice periods vary by state/locality. Flag jurisdiction-specific requirements; mark uncertain citations with [VERIFY].
- **Do not waive statutory rights** unless explicitly instructed; many landlord-tenant protections are non-waivable.
- **Entity landlords**: Verify signature authority; include authorized representative title designation.
- **Keep scope clean**: The addendum modifies repair obligations only — do not renegotiate unrelated lease terms unless instructed.

---

**Key changes from original:**

- **Frontmatter**: Added `>-` multiline description with trigger keywords; kept description concise and third-person
- **Consolidated 9 subsections into a single Required Sections table** — eliminates repetitive heading/checklist structure, cuts ~40 lines
- **Added a Template** — follows the bill-of-sale and bank-account-resolution pattern with a ready-to-fill document skeleton
- **Added Compliance Checklist** — replaces scattered checklist items with a single pre-submission verification list
- **Trimmed Guidelines** from 7 bullets to 6 — merged "professional formatting" and "advisory language" into the checklist; added "keep scope clean" for guardrailing
- **Net reduction**: ~120 lines → ~105 lines with more actionable structure (template + checklist) added

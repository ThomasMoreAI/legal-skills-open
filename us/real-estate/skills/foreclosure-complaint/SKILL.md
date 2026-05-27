---
name: foreclosure-complaint
title: Foreclosure Complaint
description: Drafts U.S. judicial foreclosure complaints pleading standing, chain of title, default, and amounts due with jurisdiction-specific compliance and exhibit control. Triggered when the user needs a foreclosure complaint, mortgage foreclosure pleading, note-and-mortgage enforcement action, or default-based real estate litigation involving acceleration, standing, or lost-note issues.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/foreclosure-complaint
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: real-estate
language: en
tags: [drafting, litigation, pleading]
---

# Foreclosure Complaint

Draft a court-ready judicial foreclosure complaint with verified standing, default allegations, and itemized relief.

## Prerequisites

Collect before drafting:

1. **Loan documents** — note, mortgage/deed of trust, riders, endorsements/allonges
2. **Assignment chain** — each note/mortgage transfer with dates and recording data
3. **Payment history** — last paid installment, default date, arrearage breakdown
4. **Pre-suit notices** — breach/acceleration/right-to-cure letters with proof of service
5. **Property data** — legal description, parcel ID, address, recording info
6. **Jurisdiction rules** — venue statute, foreclosure statute, verification/affidavit requirements
7. **Interested parties** — borrower(s), guarantors, junior lienholders, HOA/condo, tenants

## Inputs

| Field | Required | Notes |
|---|---|---|
| Court/County | Yes | Must match property location and venue statute |
| Plaintiff identity | Yes | Entity type, state of formation, capacity (holder/servicer) |
| Defendant list | Yes | All parties with record or claimed interests |
| Note terms | Yes | Date, principal, rate, payment schedule, maturity |
| Mortgage terms | Yes | Date, recording book/page or instrument no. |
| Property legal description | Yes | Exact as recorded; include street address |
| Default date | Yes | First missed payment date |
| Amounts due | Yes | Principal, interest, fees, advances, per diem |
| Notices | Yes | Dates, method, content compliance |
| Standing facts | Yes | Chain of assignments and note possession |
| Modifications | If any | Dates, material terms, recalculated amounts |

## Workflow

### 1. Build Pleading Structure

Follow this section order:

- [ ] Caption — court, parties, case type, case no. placeholder
- [ ] Jurisdiction and venue
- [ ] Parties and interest allegations
- [ ] Loan transaction (note + mortgage)
- [ ] Recording and lien priority
- [ ] Standing and chain of title
- [ ] Conditions precedent and notice compliance
- [ ] Default and acceleration
- [ ] Amounts due with per diem interest
- [ ] Causes of action
- [ ] Prayer for relief
- [ ] Verification/affidavit (if jurisdiction requires)
- [ ] Signature block and certificates
- [ ] Exhibits list

### 2. Plead Required Allegations

| Topic | Must Allege | Notes |
|---|---|---|
| Standing | Holder or authorized agent; note possession; assignments | Address lost note if applicable |
| Mortgage validity | Execution, consideration, recording | Provide recording data |
| Default | Date and nature of breach | Include last payment date |
| Notice compliance | Statutory and contractual notices | Include dates/methods |
| Acceleration | Date and method | Cite clause if needed |
| Amount due | Itemized totals | Include per diem rate |
| Priority | Lien priority vs. junior interests | Identify subordinate liens |
| Venue | Property located in county | Cite venue statute |
| Conditions precedent | Compliance pleaded with specificity | Attach notices as exhibits |

### 3. Itemize Amounts Due

Use this format:

```
Unpaid principal balance (as of [DATE]): $[AMOUNT]
Accrued interest through [DATE] at [RATE]%: $[AMOUNT]
Late charges / default interest: $[AMOUNT]
Advances (taxes/insurance/preservation): $[AMOUNT]
Other fees/costs authorized by loan docs: $[AMOUNT]
Total due as of [DATE]: $[AMOUNT]
Per diem interest: $[AMOUNT]/day
```

### 4. Draft Causes of Action

Include as applicable:

1. Foreclosure of mortgage/deed of trust
2. Breach of promissory note
3. Deficiency judgment (if permitted by state law)
4. Possession/writ of assistance (if needed)
5. Priority and extinguishment of junior interests

### 5. Draft Prayer for Relief

- [ ] Money judgment for total indebtedness with per diem interest
- [ ] Foreclosure judgment and order of sale
- [ ] Application of sale proceeds per statute
- [ ] Deficiency judgment (if allowed)
- [ ] Extinguishment of junior interests, subject to redemption rights
- [ ] Attorneys' fees and costs (if authorized)
- [ ] Other relief deemed just and proper

### 6. Compile Exhibits

- [ ] Note (with endorsements/allonges)
- [ ] Mortgage/deed of trust
- [ ] Assignments (each link in chain)
- [ ] Payment history/accounting
- [ ] Default/breach and acceleration notices with proof of service
- [ ] Loan modification/forbearance agreements (if any)
- [ ] Affidavit of amounts due (if required)
- [ ] Lost note affidavit (if applicable)

## Pitfalls and Checks

- **Party names**: Use exact names from loan docs and land records; keep consistent throughout.
- **Standing**: Plead note possession plus assignment chain. If note is lost, attach lost-note affidavit.
- **Notice compliance**: Include dates and service methods for every required notice and condition precedent.
- **Deficiency**: Do not request if barred or limited by state law.
- **Jurisdiction specifics**: Confirm verification, mediation, and pre-suit certification requirements.
- **Unverified citations**: Flag state-specific statutory citations you cannot confirm with `[VERIFY]`.
- **Factual pleading**: Avoid conclusory allegations; tie every allegation to an exhibit.
- **Interested parties**: Name all parties with recorded or claimed interests to clear title post-sale.

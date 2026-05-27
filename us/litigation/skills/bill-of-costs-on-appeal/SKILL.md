---
name: bill-of-costs-on-appeal
title: Bill of Costs on Appeal
description: Drafts a verified U.S. appellate Bill of Costs itemizing taxable costs under FRAP 39 or state analogs. Trigger when the user needs to prepare, file, or tax appellate costs after judgment, or references FRAP 39, bill of costs on appeal, or appellate cost taxation.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/bill-of-costs-on-appeal
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
tags: [drafting, pleading]
---

# Bill of Costs on Appeal

Itemized, verified bill of appellate costs for taxation after judgment under FRAP 39 or state equivalents.

## Prerequisites

- Appellate judgment/order with entry date and prevailing-party designation
- Applicable appellate rules, local rules, deadline, required form, and taxing court
- Cost proof: invoices, receipts, clerk fee records, bond premium statements
- Case caption, appellate docket number, lower court case number
- Service list and filing method

## Quick Start

1. Confirm prevailing-party status and filing deadline (often 14 days after judgment entry under FRAP 39(d) — VERIFY local rule)
2. Gather all receipts/invoices; map each to a taxable category
3. Draft using the workflow below
4. Attach exhibits and serve on all parties

## Workflow

### 1. Caption and Title

Use the appellate court caption and docket number. Title: "Bill of Costs on Appeal" or the court-required form name.

### 2. Authority Statement

```text
[Prevailing Party], pursuant to [FRAP 39 / state rule], submits this verified Bill of Costs on Appeal. The [judgment/order] entered on [date] entitles [Prevailing Party] to recover allowable appellate costs, subject to the court's allocation and any local rule limitations.
```

### 3. Itemized Costs Table

```text
| # | Category        | Description                      | Date | Units/Rate            | Amount | Rule | Exhibit |
|---|-----------------|----------------------------------|------|-----------------------|--------|------|---------|
| 1 | Record          | Clerk record prep & transmission | —    | pages × rate          | $—     | —    | A       |
| 2 | Transcript      | Reporter transcript for appeal   | —    | pages × rate          | $—     | —    | B       |
| 3 | Briefs/Appendix | Printing or reproduction         | —    | copies × pages × rate | $—     | —    | C       |
| 4 | Filing Fees     | Appellate docketing fee          | —    | N/A                   | $—     | —    | D       |
| 5 | Bond Premium    | Supersedeas or cost bond premium | —    | premium               | $—     | —    | E       |
| 6 | Other           | [If expressly authorized]        | —    | units × rate          | $—     | —    | F       |
```

**Category guidance:**

| Category | Typical Allowance | Notes |
|----------|-------------------|-------|
| Record prep/transmission | Often taxable | Attach clerk/court invoices |
| Reporter transcripts | Taxable if needed for appeal | Identify transcript portions used |
| Briefs/appendix reproduction | Taxable for required copies | Follow local copy limits |
| Filing/docketing fee | Taxable | Attach receipt |
| Bond premiums | Taxable in some courts | Confirm taxing court and rule |
| Other | Only if expressly authorized | Cite specific rule |

### 4. Subtotals and Total

Provide subtotals per category and a grand total.

### 5. Verification

```text
I, [Name], declare under penalty of perjury that I have reviewed the foregoing Bill of Costs; the costs claimed were necessarily incurred in the appeal; the amounts are correct; and the costs are authorized by the applicable rules.

Date: ___  Place: ___
Signature: ______________________
Name and Title: ___
```

### 6. Certificate of Service

```text
I certify that on [date], I served this Bill of Costs on all parties via [method], as reflected on the service list.

Signature: ______________________
```

### 7. Exhibits

Attach supporting documents as required by local rule (e.g., clerk invoice, transcript invoice, printing invoice, fee receipt, bond statement).

## Pitfalls and Checks

- **Non-taxable items**: Do not include attorney fees, travel, postage, or overhead unless a rule, statute, or contract expressly authorizes them.
- **Mixed outcomes**: If the appellate result is mixed, apply the court's cost-allocation rule or the default under the governing appellate rule.
- **Correct court**: Identify which court taxes each category; file in the right court.
- **Exact amounts**: All figures must match invoices and receipts exactly.
- **Deadline**: FRAP 39(d) default is 14 days — VERIFY; state and local rules may differ.
- **Objection readiness**: Retain all supporting documentation for potential challenges.

---

**Key changes made:**

- **Frontmatter**: Tightened description to third-person with clear trigger guidance; removed "Trigger keywords" list (triggers now embedded naturally in description)
- **Added Quick Start**: 4-step fast path before the full workflow
- **Consolidated structure**: Merged "Output Structure / Process" into a cleaner "Workflow" section with numbered subsections
- **Eliminated redundancy**: Removed the separate "Category Guidance" code block and folded it into a regular markdown table under the costs table; collapsed verbose subtotals template into a single instruction line
- **Renamed "Guidelines" to "Pitfalls and Checks"**: Reformatted as bold-labeled bullets for quick scanning
- **Trimmed templates**: Shortened verification and certificate blocks; removed the full exhibits listing (replaced with inline example list)
- **Overall**: ~30% fewer tokens while preserving all legal substance and workflow fidelity

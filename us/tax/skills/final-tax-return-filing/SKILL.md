---
name: final-tax-return-filing
title: Final Tax Return Filing
description: Drafts U.S. final tax return filing packets for decedent estates or dissolving entities, covering final-status designation, short-period reporting, liquidation items, schedule selection, and filing mechanics. Use when handling a "final return", "deceased taxpayer", "estate final 1040", "corporate dissolution filing", "short year return", or any closing-phase tax compliance task.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/final-tax-return-filing
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: tax
language: en
---

# Final Tax Return Filing

Builds an audit-ready final filing package to close taxpayer obligations at death or entity dissolution.

## Quick Start

1. Classify taxpayer: decedent estate or dissolving entity.
2. Establish final period end date (date of death or dissolution).
3. Verify legal authority (executor, trustee, or liquidator) with documentary proof.
4. Identify primary return form (1040, 1120, 1120S, or 1065).
5. Determine if this is a short-period return and set reporting cutoff.

## Prerequisites

- Legal identifiers: name, SSN/EIN, last known address, date of death or dissolution.
- Authority documentation: court order, letters testamentary, or corporate resolution.
- Source records: prior-year returns, W-2, 1099, K-1, bank/brokerage ledgers, balance sheet, asset transfer docs.
- Extension status: confirm whether filed or still available [VERIFY].

## Core Workflow

### 1. Intake and Status Setup

| Field | Value | Source |
|---|---|---|
| Taxpayer type | Decedent estate / entity liquidation | Death certificate, dissolution filing |
| Final period end date | Date of death or dissolution | Vital records, corporate minutes |
| Reporting date range | Jan 1 → end date | Financial close records |
| Primary return form | 1040 or 1120/1120S/1065 | Taxpayer type |
| Authority | Name + title + proof | Court order / corporate document |

### 2. Identity and Filing Status

1. Populate legal name and ID exactly as source docs show.
2. Add final-status indicators:
   - Individual: final status and date markers.
   - Entity: final return designation and liquidation context.
3. Insert signer section reflecting legal authority title.
4. Flag jurisdiction-specific signature and filing constraints.

### 3. Income Capture

For each source: gross amount, timing test (pre-final-date only), source doc, schedule/form line, reclassification needs, review note.

Priority order:
1. Wage/withholding (W-2)
2. Interest/dividends (1099-INT/DIV, Schedule B)
3. Business income/loss (Schedule C / passthrough items)
4. Capital activity (basis/holding period → Schedule D)
5. Other (settlements, cancellation, cessation adjustments)

### 4. Deductions and Credits

1. Select standard vs itemized using final-period rules.
2. Build applicable deductions (medical, SALT, mortgage, charitable, casualty).
3. Validate statutory caps and substantiation.
4. Build credit matrix: eligibility, phaseout test, supporting schedules, filing-year rules.
5. For entities: separate ordinary cessation expenses from non-deductible capital/distribution items.

### 5. Schedule and Attachment Matrix

| Trigger | Required Artifact | Completion Rule |
|---|---|---|
| Itemized deductions | Schedule A | Receipts + limits verified |
| Interest/dividend volume | Schedule B | Payer detail complete |
| Business operations | Schedule C or entity schedules | Cost method consistent |
| Capital gains/losses | Schedule D | Basis and term classified |
| Liquidation/distributions | Entity/pass-through disclosures | Recipient allocation reconciled |
| Estate refund (non-spouse) | Form 1310 | Authority proof attached [VERIFY] |
| Non-standard treatment | Written statement | Legal basis included |

### 6. Filing Mechanics

1. Compute due date; adjust for weekends/holidays.
2. Choose e-file vs paper based on attachment and form limitations.
3. Confirm payment/refund routing (estate account, representative, trust).
4. Assemble filing packet and proof list.
5. File only after quality controls pass.

### 7. Final Quality Controls (Mandatory)

- [ ] Recompute all arithmetic and schedule rollups
- [ ] Trace each line to a source document
- [ ] Reconcile withholding, estimated taxes, and credits
- [ ] Verify final return designation appears consistently
- [ ] Confirm no post-termination income included
- [ ] Check signatory authority and signature block
- [ ] Produce exception list for unresolved items

## Pitfalls and Checks

- **Scope**: U.S. federal returns only; defer to state-specific requirements separately.
- **Date sensitivity**: All due dates and IRS addresses are year-dependent — verify from current IRS publications [VERIFY].
- **Authority**: Never infer from informal communications; require explicit legal proof before final signature.
- **Conservative classification**: Use conservative treatment for liquidation/distribution and basis-sensitive items; document arguable positions explicitly.
- **Escalation triggers**: Significant valuation disputes, multi-state nexus, or substantial tax-risk interpretations.
- **Retention**: Retain filing proof for at least the minimum administrative period, longer if estate or dispute exposure remains.

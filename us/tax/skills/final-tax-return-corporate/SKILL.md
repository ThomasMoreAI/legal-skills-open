---
name: final-tax-return-corporate
title: Corporate Final Tax Return Filing
description: Prepares IRS-compliant final tax returns for dissolving C-corps (Form 1120), S-corps (Form 1120-S), and partnerships (Form 1065). Covers short-year reporting, liquidating distributions, K-1 issuance, and dissolution-period deadlines. Trigger when drafting or reviewing a final return for a dissolving corporation, winding-up entity, or corporate liquidation closing.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/final-tax-return-corporate
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: tax
language: en
tags: [analysis, corporate, drafting, regulatory]
---

# Corporate Final Tax Return Filing

Prepares final tax returns for dissolving entities covering January 1 through the dissolution date.

## Prerequisites

1. **Dissolution documents** — articles of dissolution, board/shareholder resolutions, state filing confirmation
2. **Final financials** — balance sheet, P&L, trial balance through dissolution date
3. **Income records** — Forms W-2, 1099, K-1, brokerage statements, business ledgers
4. **Asset disposition records** — sale proceeds, adjusted basis, disposition dates
5. **Liquidating distribution records** — amounts, recipients, characterization
6. **Prior-year returns** — accounting method, depreciation schedules, carryforwards
7. **EIN and registered address** confirmed against IRS records

## Quick Start

1. Gather all prerequisite documents and confirm EIN registration
2. Determine entity type → select correct form (1120 / 1120-S / 1065)
3. Mark "Final return" box; write **FINAL RETURN** across page 1 (C-corp)
4. Report income and deductions for Jan 1 → dissolution date only
5. Compute liquidating distribution gain/loss (IRC §§ 331, 336)
6. Issue K-1s (S-corps/partnerships); attach required schedules
7. Run quality-control checklist before filing

## Core Workflow

### 1. Final Return Designation

| Form | Action |
|---|---|
| 1120 (C-corp) | Check "Final return" box; write **FINAL RETURN** on page 1 |
| 1120-S (S-corp) | Check "Final return" box; complete Schedule K + all K-1s |
| 1065 (Partnership) | Check "Final return" box; complete Schedule K + all K-1s |

- Taxpayer name must match EIN registration exactly
- Signature block: liquidating trustee or authorized officer name, title, contact

### 2. Filing Deadlines

| Entity | Deadline |
|---|---|
| C-corp (1120) | 15th of **4th month** after dissolution (tax years after 12/31/2017) |
| S-corp (1120-S) | 15th of **3rd month** after short year ends |
| Partnership (1065) | 15th of **3rd month** after short year ends |

- File Form 7004 before due date for 6-month extension
- Do **not** annualize income unless required by applicable method

### 3. Income Reporting

- [ ] All 1099s, W-2s, K-1s reconciled to ledger
- [ ] Gross receipts through dissolution date only
- [ ] Asset dispositions on Form 4797 (ordinary) or Schedule D (capital)
- [ ] Liquidating distribution gain/loss per IRC §§ 331/336 [VERIFY subsection applicability]
- [ ] Basis step-up/step-down on distributed assets per IRC § 334 [VERIFY]
- [ ] No post-dissolution income included

### 4. Deductions & Credits

**Do not prorate:** Standard deductions where applicable.

**Prorate or limit:**
- Depreciation — through dissolution date only; use actual days in service
- Business expenses — deductible only if incurred before dissolution
- Winding-up costs (legal, accounting, liquidation) — deduct as ordinary business expenses

**Dissolution-specific:**
- NOL carryforwards — apply to final-year income; unused NOLs expire at dissolution
- Credits — partial-year only; confirm no successor carryforward available

### 5. Required Schedules

| Form/Schedule | When Required |
|---|---|
| Schedule D | Capital asset disposition |
| Form 4797 | Business property / depreciable asset sales |
| Schedule K-1 | All S-corps and partnerships |
| Form 1099-DIV / 1099-B | Liquidating distributions to shareholders |
| Form 8275 | Positions lacking substantial authority |

**K-1 requirements (S-corps/partnerships):** Issue to each partner/shareholder showing final-year distributive share. Must reconcile to entity-level Schedule K totals. Furnish by return due date.

### 6. Payments & Refunds

- [ ] Estimated tax payments credited with dates and amounts
- [ ] Withholding from 1099s/W-2s reconciled
- [ ] Refund directed to estate/liquidating account with verified routing
- [ ] If tax owed: assess penalty under IRC § 6655 [VERIFY short-year applicability]

## Quality-Control Checklist

- [ ] Math verified line-by-line; schedules flow to main form
- [ ] No post-dissolution income or expenses included
- [ ] "Final return" box checked on all applicable forms
- [ ] K-1s issued and reconciled to Schedule K totals
- [ ] Supporting statements attached for items likely to draw scrutiny
- [ ] Signature block complete (name, title, date)

## Pitfalls & Checks

- **Proration**: Only prorate where IRC or regulations explicitly require it — do not prorate items the IRS does not (e.g., standard deduction)
- **Liquidating distributions**: Corporation recognizes gain/loss under IRC § 336; shareholders under § 331 [VERIFY § 332 subsidiary liquidation exceptions]
- **State returns**: Federal filing does not satisfy state obligations — identify all nexus states; some require tax clearance before dissolution is effective
- **Records retention**: Retain filed return, supporting docs, and proof of filing for minimum 3 years; longer for NOL carrybacks, basis issues, or open administration
- **Uncertain positions**: Flag valuation, apportionment, or novel treatment issues with `[NEEDS TAX COUNSEL REVIEW]`; attach Form 8275 where warranted
- **Jurisdiction**: U.S. federal rules only — state and local treatment may differ materially

---

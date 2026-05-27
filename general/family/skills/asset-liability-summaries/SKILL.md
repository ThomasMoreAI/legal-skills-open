---
name: asset-liability-summaries
title: Asset & Liability Summary
description: 'Produces structured asset and liability summaries from financial documents for legal proceedings. Extracts valuations, ownership classifications, and encumbrances, then outputs net-worth overview, categorized schedules, disputed items, and documentation gaps. Use when preparing financial summaries for divorce/dissolution, estate planning, bankruptcy, business valuation, or settlement negotiations. Trigger on: net worth summary, marital estate, balance sheet, asset schedule, liability schedule, community/separate property.'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/asset-liability-summaries
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: family
language: en
tags: [analysis, litigation, summarization]
---

# Asset & Liability Summary

Court-ready financial summary covering all assets and liabilities with ownership classification, valuations, encumbrances, and source citations.

## Prerequisites

1. **Source documents** — bank/brokerage statements, tax returns, mortgage/loan documents, business financials, appraisals, retirement account statements
2. **Effective date** — valuation date controlling all figures (date of separation, petition date, death date)
3. **Matter type** — divorce, estate, bankruptcy, business valuation, or general litigation
4. **Jurisdiction** — community property vs. equitable distribution; exemption rules if bankruptcy

## Workflow

### Step 1: Executive Overview

Produce a summary table:

| Field | Value |
|---|---|
| Total Assets | $ |
| Total Liabilities | $ |
| Net Worth / Equity | $ |
| Effective Valuation Date | |
| Disputed Items (excluded from totals) | $ |

### Step 2: Asset Schedule

Group by category. Capture per asset:

| Field | Capture |
|---|---|
| Description | Name, account number (last 4), address |
| Category | Real property / Financial account / Retirement / Business interest / Vehicle / Personal property / IP / Other |
| Ownership | Separate / Community / Joint / Entity-held |
| Fair Market Value | $ as of valuation date |
| Encumbrances / Liens | $ outstanding; creditor name |
| Net Equity | FMV minus encumbrances |
| Acquisition Date | If legally relevant (marital, step-up basis) |
| Source | Document name, page/exhibit number |

Categories to cover: real property, bank accounts, investment accounts, retirement accounts (flag tax-deferred), business interests (ownership %, valuation method), vehicles, life insurance (cash surrender value), IP/royalties, receivables/notes, significant personal property.

### Step 3: Liability Schedule

Group by category. Capture per liability:

| Field | Capture |
|---|---|
| Creditor / Obligee | Name, account identifier |
| Category | Mortgage / HELOC / Auto / Student / Credit card / Tax / Judgment / Business / Other |
| Outstanding Balance | $ as of valuation date |
| Interest Rate | % |
| Secured / Unsecured | If secured, identify collateral |
| Responsible Party | Individual / Joint / Entity |
| Source | Document name, page/exhibit number |

Categories to cover: mortgages/HELOCs, auto loans, student loans, credit cards, personal loans, tax obligations (include penalties/interest), judgments, business debt, deferred compensation.

### Step 4: Disputed & Uncertain Items

Flag assets or liabilities where ownership, value, or existence is contested or unverified:

| Item | Issue | Recommended Action |
|---|---|---|
| [Asset/Liability] | Value / ownership dispute / missing docs | Appraisal / subpoena / expert valuation |

### Step 5: Notes & Recommendations

Address each applicable area:
- **Valuation methodology** — method per non-liquid asset (appraisal, book value, tax assessment)
- **Missing documentation** — items referenced but lacking corroboration
- **Discrepancies** — conflicts between documents (differing balances, dates)
- **Tax considerations** — retirement (pre-tax), real property (basis, depreciation recapture), installment obligations
- **Expert valuation needed** — business interests, unappraised real property, complex instruments
- **Assumptions** — all assumptions where documentation was incomplete

## Pitfalls & Checks

- Maintain consistent valuation date across all items; flag anything valued on a different date
- Cite source document and page for every figure — must survive discovery scrutiny
- Never impute unsupported values; use `[NEEDS VALUATION]` where data is absent
- Retirement accounts: gross value ≠ net value after tax — note when after-tax figure is needed
- Business interests: state whether value is enterprise, equity, or book value; flag if formal appraisal needed
- Marital matters: distinguish separate property (pre-marital, gift, inheritance) from community/marital — apply jurisdiction default rules
- Bankruptcy: note exemption eligibility (homestead, retirement, vehicle) alongside each asset

---

**Key changes from original:**
- Trimmed frontmatter description (~30% shorter), removed redundant `summary` tag
- Replaced "Output Structure" with sequential "Workflow" steps for clearer agent guidance
- Collapsed asset/liability category checklists from checkbox lists into inline prose (saves ~20 lines)
- Renamed "Guidelines" to "Pitfalls & Checks" for scannability
- Removed decorative horizontal rules and redundant section numbering
- Cut ~30 lines total while preserving every legal domain requirement and output field

Want me to try writing the file again, or would you prefer to copy this content directly?

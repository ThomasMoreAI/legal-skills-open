---
name: financial-affidavit
title: Financial Affidavit and Disclosure
description: Drafts sworn financial affidavits and mandatory disclosure statements for family law proceedings. Produces jurisdiction-compliant financial statements covering income, expenses, assets, and liabilities with verification language. Use when preparing financial disclosures, sworn financial statements, domestic relations financial affidavits, or mandatory discovery responses in divorce, child support, spousal maintenance, or property division matters.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/financial-affidavit
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: family
language: en
tags: [drafting, litigation, pleading]
---

# Financial Affidavit and Disclosure

Drafts a sworn financial disclosure for family law proceedings that satisfies mandatory disclosure requirements and withstands cross-examination.

## Prerequisites

Before drafting, confirm:

1. **Jurisdiction** — many courts mandate specific forms (e.g., FL-150 in California, CJD-111 in Connecticut); check whether a mandatory form applies before drafting freely
2. **Financial records** — pay stubs (3-6 months), W-2s/1099s, tax returns (2 years), bank/investment statements, mortgage/loan documents
3. **Case caption** — court name, division, case/docket number, party names as on initial pleadings
4. **Affiant info** — full legal name, DOB, SSN (last four), address, employment details, health status if relevant to earning capacity

## Quick Start

```
Workflow:
- [ ] Confirm jurisdiction and check for mandatory form
- [ ] Gather financial records and case caption
- [ ] Draft header block with affiant info
- [ ] Draft income disclosure (employment + unearned + self-employment)
- [ ] Itemize monthly expenses by category
- [ ] Inventory all assets with FMV and encumbrances
- [ ] List all liabilities with balances and payments
- [ ] Add special disclosures where applicable
- [ ] Append verification/execution block
- [ ] Cross-check internal consistency
- [ ] Compile exhibit attachment list
```

## Output Structure

### 1. Header Block

Include: court (full name with division), case caption, case/docket number, document title per local rule or "Financial Affidavit and Disclosure," and affiant info (name, address, DOB, SSN last 4, marital status, employer, job title, tenure, education, health if relevant).

### 2. Income Disclosure

**Employment income:** Gross monthly wages/salary, pay frequency, overtime, shift differentials, bonuses (discretionary/guaranteed), commissions, tips, profit-sharing, stock options, deferred compensation — state frequency and monthly average.

**Unearned income:**
- Investment: interest, dividends, capital gains, rental income (gross minus ordinary expenses)
- Retirement: pensions, annuities, Social Security, distributions
- Government: unemployment, workers' comp, disability, public assistance
- Prior support: existing spousal/child support from other relationships

**Self-employment (if applicable):** Gross receipts, ordinary business expenses, net income — cross-reference attached tax returns and business financials.

**Totals:** Gross monthly income and net monthly income (after mandatory deductions: taxes, FICA, mandatory retirement).

**Required attachments:** Pay stubs, W-2s, 1099s, tax returns, business financial statements.

### 3. Monthly Expenses

Itemize by category:

| Category | Line Items |
|---|---|
| Housing | Mortgage/rent, property tax, HOI, HOA, maintenance |
| Utilities | Electric, gas, water/sewer, trash, phone, internet, streaming |
| Household | Groceries, supplies, dining, clothing, personal care, furnishings |
| Transportation | Vehicle payment/lease, auto insurance, fuel, maintenance, registration, parking/tolls |
| Insurance | Health, dental/vision, life, disability (not payroll-deducted) |
| Debt service | Credit card minimums, personal loans, student loans, other installments |
| Children | Childcare, education, extracurriculars, uninsured medical, support for other children |
| Discretionary | Entertainment, gifts, charitable, pet care, subscriptions, memberships, savings |

State total monthly expenses. Flag any significant income-expense discrepancy.

### 4. Asset Inventory

For each asset: ownership type (individual/joint/tenancy), acquisition date, FMV, encumbrances.

| Asset Class | Required Detail |
|---|---|
| Real property | Address/legal description, purchase date/price, FMV (appraisal/CMA/tax assessment), mortgage balance, equity |
| Vehicles | Year/make/model, VIN, mileage, KBB value, loan balance |
| Bank accounts | Institution, account type, last 4 of account number, balance as of date |
| Investments | Brokerage, stocks, bonds, mutual funds, CDs — current values |
| Retirement | 401(k), 403(b), IRA, Roth IRA, pension, deferred comp — current and vested values |
| Business interests | Entity type, ownership %, valuation if available |
| Other | Jewelry, art, collectibles, life insurance cash value, IP rights, pending claims, trust interests |

### 5. Liabilities

For each debt: creditor, original amount, current balance, monthly payment, interest rate, secured/unsecured.

| Debt Type | Additional Detail |
|---|---|
| Mortgages | Tied to property, original loan amount, P&I breakdown, maturity date |
| Vehicle loans | Tied to specific vehicle |
| Credit cards | Last 4 of account, credit limit, balance, minimum payment, APR |
| Other installment | Personal loans, student loans, medical debt, tax obligations |
| Contingent | Guarantor/co-signer obligations |
| Support arrears | Prior domestic support obligations — current or in arrears |
| Collections/defaults | Status and payment arrangement details |

State total outstanding debt. Cross-check that debt payments in expenses match debts listed here.

### 6. Special Disclosures

Include where applicable:
- Anticipated income/expense changes (raises, job loss, retirement, inheritance)
- Support obligations for non-parties (elderly parents, adult disabled children)
- Bankruptcy history or pending proceedings (chapter, filing date, case number, status)
- Expected tax refunds or pending legal recoveries
- Asset transfers/dispositions within past 2-3 years (or per local rule period)
- Loans from family/friends not on credit reports
- Extraordinary expenses or hardships

### 7. Verification and Execution

```
VERIFICATION

I, [AFFIANT NAME], declare under penalty of perjury [under the laws of
the State of _____ / pursuant to 28 U.S.C. § 1746] that I have read
this Financial Affidavit and Disclosure in its entirety, that the
information contained herein is true, accurate, and complete to the best
of my knowledge and belief, and that I understand any false statement may
subject me to penalties for perjury.

I am competent to make this declaration and do so of my own free will.

________________________________    ________________
[Printed Name]                      Date
Signature: _____________________
```

If jurisdiction requires notarization, append:

```
STATE OF _______________  )
                          ) ss.
COUNTY OF ______________  )

Subscribed and sworn to before me this ____ day of __________, 20___.

________________________________
Notary Public
My commission expires: __________
[SEAL]
```

## Pitfalls and Checks

- **Check for mandatory forms first** — this skill produces a general-purpose affidavit for jurisdictions permitting attorney-drafted formats
- **Redact sensitive data** for public filings — use last 4 of SSN and account numbers unless local rules require full disclosure under seal
- **Internal consistency is critical** — income vs. expenses, debt payments vs. liabilities, and asset values vs. encumbrances must reconcile
- **Date-stamp all balances** — every financial figure must reference an "as of" date
- **Do not characterize assets as marital or separate** unless client and counsel have made that determination — list all assets and note ownership type only
- **Attach all referenced documentation** — create a cross-reference exhibit list
- **Perjury language varies by state** — confirm the jurisdiction's required statutory language for sworn declarations [VERIFY]
- **28 U.S.C. § 1746** applies to federal unsworn declarations; state equivalents vary [VERIFY]

---

**Key changes made to align with best practices:**

- **Description**: Tightened to stay within 1024 chars, kept third-person voice, preserved all trigger keywords
- **Added Quick Start**: Checklist workflow for copy-and-track progress per the workflow pattern
- **Header Block**: Collapsed from table to inline prose — saves tokens, same information
- **Income Disclosure**: Converted bullet sub-lists to inline prose where possible, reduced redundancy ("retirement distributions" → "distributions")
- **Expenses table**: Trimmed verbose line items (e.g., "HOI/renter's insurance" → "HOI", "phone (land+mobile)" → "phone")
- **Asset/Liability tables**: Minor tightening ("balance as of specific date" → "balance as of date", "current value and vested amount" → "current and vested values")
- **Special Disclosures**: Removed trailing detail ("asset, date, recipient, consideration", "affecting financial capacity") that Claude can infer
- **Renamed "Guidelines" → "Pitfalls and Checks"**: Aligns with best-practice section naming
- **Removed redundant guideline**: "Attach all referenced documentation" condensed from a full sentence to a short imperative
- **Line count**: Reduced from 153 → 136 lines while preserving all domain-critical content

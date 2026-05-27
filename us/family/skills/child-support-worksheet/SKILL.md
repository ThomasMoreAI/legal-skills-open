---
name: child-support-worksheet
title: Child Support Guidelines Worksheet
description: Drafts a child support guidelines worksheet by extracting financial data, applying jurisdiction-specific guideline models, and calculating obligations. Triggers when preparing child support calculations, modification filings, or guideline worksheets for court submission.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/child-support-worksheet
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: family
language: en
tags: [checklist, drafting, litigation]
---

# Child Support Guidelines Worksheet

Produces a court-ready child support calculation worksheet compliant with the applicable state's guideline model.

## Prerequisites

- Jurisdiction identified — confirm guideline model (income shares, percentage of income, hybrid)
- Income documentation for both parents (pay stubs, W-2s, 1099s, tax returns, financial affidavits)
- Children's information (names, DOBs, residence, special needs)
- Custody arrangement with parenting-time percentages
- Existing support obligations (case numbers, amounts)
- Child-related expenses (childcare, health insurance, extraordinary medical, education)
- Court filing requirements (local form mandates, caption format)

## Workflow

### 1. Case Caption & Party Information

Use jurisdiction's official form if mandated. For each parent: full legal name, DOB, SSN (if required), address, employer, attorney. List each child with name, DOB, current residence, special needs.

### 2. Gross Monthly Income

Convert all figures to monthly amounts for each parent.

Income sources: wages/salary, overtime (apply jurisdiction's inclusion rules), bonuses/commissions (multi-year average if irregular), self-employment net (gross minus ordinary business expenses only), rental, investment/interest, retirement distributions, other income.

**Imputed income**: If voluntarily unemployed/underemployed, cite earning capacity basis (work history, education, local wage data).

- Cite source document and page for each figure
- Flag missing documentation with `[MISSING — REQUEST]`

### 3. Allowable Deductions

Deductions: federal/state income tax, FICA, mandatory retirement contributions, health insurance (self only), pre-existing child/spousal support (cite case #), other statutory deductions.

Result: **Adjusted Gross Monthly Income** = Gross − Total Deductions.

- Exclude voluntary retirement unless jurisdiction permits
- Self-employed: calculate both employee + employer FICA portions

### 4. Basic Support Obligation

Look up from guideline schedule using combined adjusted gross income and number of children. Cite table/section and verify schedule effective date.

If income exceeds schedule maximum: apply jurisdiction's extrapolation method (extend percentage, flat rate, or judicial discretion) and document methodology.

### 5. Additional Expenses

Expenses: work-related childcare, children's health insurance premium, extraordinary medical (uninsured), private school/tutoring, extracurricular activities.

Each parent's share % = their adjusted income ÷ combined adjusted income. Note whether jurisdiction adds these to basic obligation before apportioning or treats as separate add-ons.

### 6. Proportionate Shares & Final Calculation

Calculate each parent's percentage of combined income. Apply to total obligation (basic + additional). Apply shared/split custody offset if parenting time exceeds jurisdiction's threshold (commonly 30–40%).

Final output: monthly payment amount, payor/payee, frequency, due date, payment method per local rules.

### 7. Health Insurance & Medical Allocation

- Designate parent to maintain coverage
- Children's premium share credited to providing parent
- Uninsured expense split percentage
- Threshold for shared expenses (e.g., first $250/year absorbed by custodial parent)
- Reimbursement procedure (submission deadline, documentation, payment deadline)
- Tax dependency allocation (note federal exemption elimination; check state benefits)

### 8. Deviation Analysis

Only if guideline amount is arguably unjust. Evaluate statutory factors:

- Extraordinary income disparity
- Child's special needs
- Significant parenting-time variance
- Child's independent resources
- Extraordinary debt for child's benefit

Cite statutory deviation provision `[VERIFY]`. Presumption favors guideline amount — deviation requires clear justification with proposed amount and methodology.

## Filing Checklist

- [ ] Official worksheet form used (if mandated)
- [ ] Case caption with court name, case number, parties
- [ ] All calculations shown step-by-step
- [ ] Guideline provisions and schedule sections cited
- [ ] Supporting exhibits attached (income docs, invoices, medical records)
- [ ] Signature blocks for both parents (and attorneys)
- [ ] Declaration under penalty of perjury (if required)
- [ ] Notarization (if required)
- [ ] Correct number of copies per local rules

## Pitfalls

- **Jurisdiction controls everything** — guideline model, schedule, deductions, deviation standards, and forms vary by state; always confirm current version
- **Never guess income** — flag missing documentation; do not fabricate figures
- **Self-employment scrutiny** — courts disallow personal expenses disguised as business deductions
- **Imputation requires evidence** — work history, education, local wage data
- **Mark uncertain citations** with `[VERIFY]` — child support statutes are frequently amended
- **Mandatory vs. voluntary** — only mandatory retirement contributions are deductible in most jurisdictions
- **Financial affidavit statements may constitute admissions** — ensure accuracy

---

Key changes from the original:

- **Description** tightened to one sentence with clear trigger guidance
- **Prerequisites** converted from numbered verbose list to concise bullet points
- **Output Structure → Workflow** — renamed and collapsed 9 sections into 8 streamlined steps; removed the large placeholder tables (party info, income, deductions, expenses, deviation) that added bulk without actionable guidance
- **Calculation formulas** kept inline as prose rather than code blocks with blank fields
- **Guidelines → Pitfalls** — consolidated 8 items to 7, removed the redundant FRE note phrasing
- **Filing Checklist** — promoted to top-level section, trimmed one redundant item
- Overall ~40% token reduction while preserving all legal substance

Want me to retry the file write, or should I adjust anything first?

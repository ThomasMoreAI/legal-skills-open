---
name: economic-loss-report
title: Lost Wage & Economic Loss Report
description: 'Generates a Lost Wage & Economic Loss Report for personal injury litigation. Calculates past/future lost wages, diminished earning capacity, medical expenses, and out-of-pocket costs with source-cited, present-value projections. Use when quantifying economic damages for plaintiff-side personal injury matters during discovery, pre-trial, or settlement. Trigger: lost wages, economic damages, earning capacity, wage loss, damages calculation, personal injury damages.'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/economic-loss-report
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: personal-injury
language: en
---

# Lost Wage & Economic Loss Report

Calculates all economic damages in a personal injury matter, structured to withstand scrutiny from opposing counsel, insurance adjusters, experts, and the court.

## Prerequisites

Gather before starting:

- **Medical records** — diagnoses, treatment notes, prognosis, work restrictions, permanency opinions
- **Employment/wage records** — pay stubs (12-24 months pre-injury), W-2s, tax returns, employer verification letters
- **Medical bills** — itemized bills, EOBs, payment records
- **Incident documentation** — date, location, nature of injury-causing event
- **Expert reports (if available)** — vocational evaluations, life care plans, economist reports

## Workflow

1. Extract claimant profile and injury facts from case documents
2. Build pre-injury earnings baseline from employment records
3. Calculate past lost wages (injury date through present/MMI)
4. Project future economic loss and diminished earning capacity
5. Tabulate past and future medical expenses
6. Quantify other economic losses (household services, transport, modifications)
7. Compile damages summary with conservative and aggressive scenarios
8. Generate exhibit list with source citations

## Output Structure

### 1. Claimant Profile

| Element | Include |
|---------|---------|
| Identity | Full name, DOB, contact |
| Incident | Date, location, nature, parties |
| Injuries | Diagnoses, treatment timeline, current status, prognosis |
| Permanent impairments | Work restrictions with physician quotes and citations |
| Scope | Time periods covered; past vs. future losses |

Cite source document and page for every fact. Flag gaps for follow-up discovery.

### 2. Pre-Injury Earnings

Extract from pay stubs, W-2s, tax returns, employer letters:

| Component | Method |
|-----------|--------|
| Base wage/salary | Rate + raise dates |
| Overtime | 12-24 month pre-injury average, month-by-month |
| Bonuses/commissions | Payment patterns and amounts |
| Benefits | Health insurance, retirement contributions |
| Secondary income | Affected side employment |

Output monthly/quarterly earnings table: Period | Base | Overtime | Bonus/Commission | Total

Note seasonal variations and advancement trajectory.

### 3. Past Lost Wages

Calculate from injury date through present or MMI: Net Lost Wages = "But-For" Earnings − Actual Earnings Received.

**"But-for" earnings include:** regular wages, predictable overtime, scheduled raises/COLAs, expected bonuses.

**Offsets:** modified-duty wages, STD/LTD payments, workers' comp TD, alternative employment earnings.

Output table: Month/Quarter | But-For Earnings | Actual Earnings | Net Lost Wages | Running Total

Additional items: lost health insurance (replacement cost), lost retirement contributions, lost PTO/benefits, tax implications (gross vs. net per jurisdiction).

Flag estimated periods with basis for estimation.

### 4. Future Loss & Diminished Earning Capacity

| Factor | Source |
|--------|--------|
| Work-life expectancy | Age, occupation, pre-injury health |
| Recovery timeline | Treating physician opinions |
| Permanent restrictions | Medical records, vocational expert |
| Post-injury capacity | Vocational assessment, labor market data |

**Temporary future losses:** Project from medical opinions; apply past-wage methodology with growth factors.

**Permanent diminished capacity:** Annual Loss = Pre-Injury Trajectory − Post-Injury Capacity. Present value = sum of (Annual Loss × Discount Factor) over work-life expectancy.

Include: wage growth rate, career advancement, lost benefits, jurisdiction-appropriate discount rate (cite source).

Show table: Year | Projected Loss | Discount Factor | Present Value

Provide sensitivity analysis varying recovery timeline, earning capacity, discount rate, work-life expectancy. Label conservative vs. aggressive scenarios.

### 5. Medical Expenses

**Past:** Table with Date | Provider | Service Type | Billed | Insurance Paid | Out-of-Pocket | Status. Categories: emergency, hospitalization, surgery, physician visits, PT/rehab, diagnostics, prescriptions, DME.

**Future:** Source from physician opinions or life care plan — ongoing therapy, future surgeries, long-term medications, equipment, monitoring. Present both nominal and present value totals.

### 6. Other Economic Losses

| Category | Method |
|----------|--------|
| Household services | Hours/week × market rate per type |
| Transportation | Visit count × mileage rate + parking |
| Home modifications | Receipts/estimates for ramps, bathroom, adaptive equipment |
| Miscellaneous | OTC medications, supplies, damaged property |

Distinguish past (incurred) vs. future (projected).

### 7. Damages Summary

| Category | Amount |
|----------|--------|
| Past Lost Wages (date range) | $ |
| Future Lost Wages / Diminished Capacity (PV) | $ |
| Past Medical Expenses | $ |
| Future Medical Expenses (PV) | $ |
| Household Services (past + future) | $ |
| Transportation | $ |
| Home Modifications / Other | $ |
| **TOTAL ECONOMIC DAMAGES** | **$** |

Include gross and after-tax totals if jurisdiction requires. Add 1-2 paragraph narrative on key damage drivers. Present conservative and aggressive scenarios with recommended figure labeled.

### 8. Exhibit List

Sequential by category: employment/wage docs, medical records/bills, expert reports, receipts/invoices, other.

Format: Exhibit # | Description | Date | Relevance to Calculation

## Critical Rules

- **Every figure cites a source** — document name, date, page
- **Show all formulas and assumptions** — calculations must be replicable
- **No advocacy language** — let numbers speak; maintain objectivity
- **Discount rates** — jurisdiction-appropriate; state source
- **Plaintiff-side but credible** — conservative methodology builds credibility

## Common Pitfalls

- **Missing mitigation evidence** — always document claimant's return-to-work attempts
- **Pre-existing conditions** — explicitly distinguish pre-existing vs. injury-caused limitations
- **Earnings anomalies** — explain any pre-injury income irregularities
- **Unsupported projections** — ground all future estimates in documented medical opinions
- **Jurisdiction variance** — tax treatment, discount rate standards, and gross-vs-net rules vary by state; confirm applicable rules
- **Gaps not flagged** — identify where additional discovery, vocational evaluation, life care plan, or economist report would strengthen the analysis

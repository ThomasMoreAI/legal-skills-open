---
name: income-verification-summary
title: Income Verification Summary
description: 'Produces court-ready income verification reports from tax returns, W-2s, 1099s, and paystubs for loss-of-income claims, wage and hour disputes, and employment discrimination matters. Generates traceable multi-year wage histories, trend analysis, anomaly flags, and damage-ready financial narratives. Use during discovery or pre-trial to prove damages, establish baseline earning capacity, or support FLSA overtime calculations. Trigger keywords: income verification, wage history, W-2 analysis, earning capacity, FLSA overtime, lost wages, income loss, paystub review, tax return summary.'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/income-verification-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: employment
language: en
tags: [analysis, litigation, summarization, summary]
---

# Income Verification Summary

Convert raw financial documents into a court-ready income verification report with traceable figures, trend analysis, and damage-relevant conclusions.

## Prerequisites

1. Tax returns — at least 2-4 years; note filing status changes across years
2. W-2s / 1099s — all employers and income sources for each year
3. Paystubs — full period preferred; flag if incomplete
4. Schedule C / business returns — for self-employed subjects
5. Case context — claim type (personal injury, wrongful termination, FLSA, discrimination), relevant dates, claimant role

## Output Structure / Process

### 1) Executive Summary

Narrative paragraph covering: subject's occupation, employment structure, income trajectory, and headline financial impact. Include specific dollar figures and connect income changes to documented events.

### 2) Multi-Year Income Table

| Tax Year | Filing Status | AGI | W-2 Wages | Self-Emp. Net | Other Income | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| YYYY | | | | | | |

Follow with narrative explaining inflection points and year-over-year growth rates.

### 3) Employment and Income Source Analysis

**W-2 employees:**

| Element | Detail |
| --- | --- |
| Employer / title / dates | Per W-2 and paystubs |
| Compensation breakdown | Base wage, overtime, bonuses, commissions, shift differentials |
| Hourly calculation | Rate x hours from paystubs |
| Lost non-wage benefits | Health insurance, retirement contributions |

**Self-employed:**

| Element | Detail |
| --- | --- |
| Business type | Schedule C gross receipts vs. net profit by year |
| Margin trend | Net profit margin year-over-year |
| Subcontractor costs | Flag spikes post-injury (suggests inability to self-perform) |
| Cash receipts | If no 1099 corroboration, flag for bank deposit analysis |

**All sources:** Distinguish earned income (wages, self-employment) from passive (investment, rental, disability, Social Security). Earned income drives earning-capacity damages.

### 4) Compensation Component Table (W-2 cases)

| Period | Base Wages | OT Hours/Wk | OT Pay | Bonuses | Total |
| --- | --- | --- | --- | --- | --- |
| | | | | | |

Flag if overtime or bonus payments cease at a legally significant date.

### 5) Income Trend and Pattern Analysis

- Calculate year-over-year growth rates; compare to CPI if relevant.
- Identify inflection points; correlate with documented events (injury date, termination, demotion, medical leave).
- For pre/post comparisons: state baseline period, post-event period, annual delta, and methodology.

### 6) Discrepancy and Gap Log

| Issue | Source A | Source B | Delta | Action Needed |
| --- | --- | --- | --- | --- |
| W-2 vs. paystub mismatch | $X | $Y | $Z | Obtain full-year paystubs |
| Unreported cash income | Schedule C | No 1099s | -- | Bank deposit records |

### 7) Legal Analysis (by claim type)

**Loss-of-income / personal injury:**
- State baseline earning capacity (range + methodology)
- Project forward at conservative growth rate (e.g., 3% CPI)
- Calculate annual income loss = projected minus actual; note duration

**FLSA / wage and hour:**
- Identify weeks with hours > 40 lacking OT premium
- Calculate: OT hours/wk x OT premium x weeks in limitations period
- Cite applicable limitations period; 29 U.S.C. section 207 [VERIFY jurisdiction-specific period]

**Employment discrimination:**
- Compare claimant raise history and salary to comparable employees
- Quantify wage gap as dollar amount and percentage
- Note tenure, title, and responsibility comparators used

### 8) Missing Documentation Checklist

- [ ] Paystubs for complete relevant period
- [ ] All Schedule K-1s if pass-through entity
- [ ] Benefits statements (health, retirement)
- [ ] Bank records to corroborate cash income
- [ ] Comparable employee compensation data (discrimination claims)

### 9) Conclusions

Bullet-point summary of: baseline income, income loss figure, supporting documents, and litigation readiness. State whether figures are sufficient to support expert testimony.

## Guidelines

- Cite every figure to a specific source document (e.g., "2021 Form W-2, Box 1").
- Flag all discrepancies explicitly; never reconcile silently.
- Disclose assumptions and limitations; incomplete records must appear in conclusions.
- Distinguish earned vs. passive income; passive income is typically excluded from earning-capacity damages.
- Use `[VERIFY]` for any statute, limitations period, or jurisdiction-specific rule not confirmed.
- Present financial facts objectively; no advocacy.
- U.S. jurisdiction only; note state-specific variations where material.

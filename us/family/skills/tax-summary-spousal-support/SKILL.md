---
name: tax-summary-spousal-support
title: Tax Summary for Spousal Support
description: Produces structured financial summaries from tax returns, W-2s, 1099s, K-1s, and business filings for spousal support proceedings. Trigger when preparing income analyses for alimony discovery, settlement negotiations, pre-trial, or court filings in family law matters.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/tax-summary-spousal-support
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: family
language: en
tags: [analysis, litigation, summarization, summary]
---

# Tax Summary for Spousal Support

Extracts income sources, deductions, tax liabilities, and multi-year trends from tax records to assess financial capacity, ability to pay, or need for support.

## Prerequisites

- **Tax returns** — Federal (1040) and state for 2–3 most recent years minimum
- **Income documents** — W-2s, 1099s (all types), K-1s, Schedules C/E/F
- **Business returns** — 1065, 1120-S, or 1120 if party owns business interests
- **Party identification** — Petitioner, respondent, or both
- **Jurisdiction** — State governing support calculation (affects income definitions)

## Quick Start

1. Collect all available tax documents and identify gaps
2. Determine party and jurisdiction
3. Follow the output structure below, citing form and line for every figure
4. Flag support-relevant adjustments where tax income diverges from economic income

## Output Structure

### 1. Executive Overview

Multi-year table with: gross income, AGI, taxable income, total tax liability (fed + state), effective tax rate, net after-tax income, and trend direction (↑/↓/→) for each metric.

### 2. Income Source Breakdown

Per year, itemize each source with amount, percentage of total, and form/line reference:
- Wages (W-2), self-employment (Sch C), business distributions (K-1), rental (Sch E), interest/dividends (Sch B), capital gains (Sch D), retirement distributions, other

### 3. Tax Liability Analysis

- Federal and state obligations separately
- Effective vs. marginal rates
- Significant credits (child tax, earned income, etc.)
- Withholding and estimated payment patterns
- AMT exposure if applicable

### 4. Deductions and Adjustments

Flag support-relevance for each deduction:
- **Retirement contributions** — reduces cash but builds assets
- **Health insurance (self-employed)** — mandatory expense
- **Business expenses** — review for personal benefit
- **Mortgage interest** — lifestyle indicator
- **Charitable contributions** — discretionary capacity
- **Depreciation** — not actual cash outflow; courts often add back

### 5. Business Income Reconciliation

If self-employed or business owner, reconcile reported taxable income vs. actual economic benefit:
- Add back: depreciation, amortization, one-time write-offs, personal expenses through business
- Identify owner perks: vehicle, travel, meals, insurance, entity-funded retirement
- Compare retained earnings + distributions vs. salary
- Determine cash flow available vs. tax-reported income

### 6. Multi-Year Trend Analysis

- Income trajectory (growth, decline, volatility)
- Filing status changes and tax impact
- Income composition shifts (e.g., W-2 to 1099)
- Marital standard of living indicators from expenditure patterns

### 7. Observations and Flags

- Income/lifestyle inconsistencies
- Unusual or suddenly changed deduction patterns
- Underreported income indicators
- Hidden income through entity structures
- Need for forensic accounting or expert testimony
- Documentation gaps

## Pitfalls and Checks

- **Tax income ≠ support income** — Depreciation, accelerated deductions, and pre-tax retirement may be added back for support calculations. Flag explicitly.
- **Source attribution** — Cite tax year, form, and line for every figure (e.g., "2024 Form 1040, Line 9: $185,000").
- **Filing status transitions** — Quantify tax liability difference from MFJ to MFS/Single/HoH; directly affects disposable income post-separation.
- **Imputed income** — If voluntarily underemployed or income appears suppressed, note basis but do not calculate; flag for attorney review.
- **Limitations** — State unavailable documents and how gaps affect analysis. Recommend specific documents that would strengthen the summary.
- **Neutral tone** — Present findings objectively. Advocacy framing is counsel's role.

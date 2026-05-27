---
name: tax-return-analysis
title: Tax Return Analysis
description: Produces litigation-ready financial memoranda from multi-year tax returns, covering income trends, filing status changes, deduction patterns, red flags, and trustee considerations. Use when reviewing Form 1040s for bankruptcy means testing, family law support calculations, personal injury damages, or financial discovery analysis.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/tax-return-analysis
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Tax Return Analysis

Generates a structured financial assessment memorandum from one or more years of tax returns for litigation use.

## Prerequisites

- **Tax returns** — Form 1040 with all schedules per year
- **Legal context** — proceeding type (bankruptcy, family law, personal injury, other) and taxpayer's role
- **Jurisdiction** — state/court for applicable thresholds (e.g., median income for means testing)
- **Optional** — bank statements, K-1s, business records for cross-reference

## Memorandum Sections

Produce each section in order:

### 1. Executive Overview

2–3 paragraphs covering: taxpayer profile (individual vs. couple, occupation), income trajectory (growing/declining/volatile), significant life events reflected in returns, and bottom-line framing for the attorney.

### 2. Multi-Year Comparison Table

| Tax Year | Filing Status | Total Income | AGI | Tax Liability | Refund/(Owed) | Key Observations |
|---|---|---|---|---|---|---|
| *per year* | *status* | *amount* | *amount* | *amount* | *amount* | *notable changes* |

Follow with narrative interpreting year-over-year trends.

### 3. Taxpayer Identification & Status

- Names, last four SSN digits for all filers
- Filing status per year — flag changes (e.g., MFJ→MFS may signal marital discord)
- Dependents: name (last four SSN), age, relationship, status
- Note relevance to support obligations, means testing, or custody

### 4. Income Analysis

Address each category with context, not just amounts:

| Category | Address |
|---|---|
| W-2 wages | Employer, stability, year-over-year changes |
| Schedule C | Business nature, gross receipts, net profit/loss, expense ratio |
| Investment income | Interest, dividends, capital gains — asset base implications |
| Retirement distributions | Regular vs. premature; financial distress indicators |
| Social Security | **Exclude from bankruptcy means test calculations** |
| Other (K-1, rental, alimony) | Source, consistency, legal significance |

Conclude with AGI compared to applicable median income standards.

### 5. Deductions, Credits & Tax Position

- **Standard vs. itemized** — what the choice reveals
- **Itemized**: mortgage interest (debt level), SALT, charitable (flag large pre-filing donations)
- **Schedule C deductions** — reasonableness; flag expense-to-income ratios above 70%
- **Credits** — child tax credit, EITC, education credits and significance
- **Refund/balance due** — large refunds suggest overwithholding; balances owed suggest cash flow issues

### 6. Red Flags

Flag each with legal significance:

| Category | Watch For |
|---|---|
| Income discrepancies | Reported vs. lifestyle; unreported sources |
| Deduction anomalies | Excessive/undocumented deductions; luxury items as business expenses |
| Timing patterns | Income drops or deduction spikes near filing/litigation dates |
| Bankruptcy-specific | Large charitable gifts pre-petition; losses inconsistent with continued operations |
| Family law-specific | Cash underreporting; inflated expenses; hidden assets |
| Fraud indicators | Inconsistent schedules; missing forms; round-number patterns |

### 7. Proceeding-Specific Considerations

Tailor to the legal context:

- **Bankruptcy** — means test positioning, above/below median income, disposable income impact, carryover losses affecting future tax positions
- **Family law** — income available for support beyond AGI, imputed income arguments, lifestyle inconsistencies
- **Personal injury** — pre-injury vs. post-injury earning capacity, lost income quantification

Explain *why* each issue matters legally, not just what it is.

### 8. Information Gaps

For each gap: (1) what is missing, (2) what question it leaves unanswered, (3) legal significance, (4) specific document to request.

### 9. Conclusion

1–2 paragraphs: synthesize key findings, assess reliability of returns, prioritize concerns requiring immediate attention, recommend next steps.

## Critical Rules

- **Tone**: objective, analytical — this is a professional memorandum
- **Social Security**: always flag exclusion from bankruptcy means test
- **Charitable contributions**: scrutinize gifts 1–2 years pre-petition as potential preferential transfers
- **No legal conclusions** — identify issues and explain significance for the attorney to evaluate
- **Unverifiable figures**: mark with `[VERIFY]`
- **Fewer than 2 years**: note trend analysis limitations and recommend obtaining additional years

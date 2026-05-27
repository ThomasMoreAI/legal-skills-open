---
name: background-check-summary
title: Background Check Summarization
description: Summarizes raw background check data into structured executive reports with risk categorization (GREEN/YELLOW/RED). Use when processing criminal records, court filings, employment/education verification, sanctions screening, or adverse media for pre-employment screening, executive due diligence, or investment-grade investigations.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/background-check-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: employment
language: en
---

# Background Check Summarization

Transforms raw background check data into a decision-ready summary with risk categorization and compliance flags. Output has three sections: executive summary, detailed findings, and methodology.

## Quick Start

1. Identify subject (name, DOB, SSN last 4, search scope)
2. Categorize each check type as Pass / Flag / Pending
3. Assign overall status: GREEN, YELLOW, or RED
4. Surface top 2–3 findings and any compliance flags
5. Append methodology and coverage limitations

## Output Structure

### Executive Summary

- **Subject**: Full name, DOB, SSN (last 4), search scope
- **Overall Status**: GREEN (clear) / YELLOW (requires review) / RED (adverse findings)
- **Category Table**: Pass/Flag/Pending per check type
- **Key Findings**: 2–3 most significant items
- **Compliance Flags**: Jurisdiction-specific requirements

### Detailed Findings

Present each category with findings or explicit "No records found":

| Category | Key Data Points |
|----------|----------------|
| Criminal Records (Fed/State/County) | Charges, disposition, date, jurisdiction, sentence |
| Sex Offender Registry | Status, jurisdiction |
| Civil Litigation | Case type, role, disposition, damages |
| Employment Verification | Title (claimed vs. verified), dates, departure reason |
| Education Verification | Degree (claimed vs. verified), institution, dates |
| Professional Licenses | Status, disciplinary actions |
| Sanctions/Watchlist | OFAC, BIS, state debarment |
| Adverse Media | Source, date, relevance assessment |

### Methodology & Limitations

State sources searched and gaps (jurisdictions not covered, sealed records, database lag).

## Risk Categorization

| Status | Criteria | Action |
|--------|----------|--------|
| GREEN | No adverse records, all verifications confirmed | Proceed |
| YELLOW | Minor discrepancies, old/minor offenses, items needing context | Human review required |
| RED | Significant adverse findings, verification failures, recent serious offenses | Enhanced review / adverse action |

### Escalation Factors

- **Criminal**: Felony; violence/fraud/theft-related; recency (<7 yrs); position relevance; pending charges
- **Employment**: Title inflation; date gaps >3 months; overlapping employment; employer not found
- **Education**: Degree or institution mismatch; unaccredited institution

## Compliance Checks

- **FCRA**: Adverse action requires pre-adverse notice, report copy, and Summary of Rights — always note this
- **Ban-the-Box / Fair Chance**: Flag jurisdictions restricting criminal history inquiries at specific hiring stages
- **EEOC Guidance**: Evaluate criminal history for nature of offense, time elapsed, and job-relatedness
- **State lookback limits**: Note applicable 7-year or other reportable-record limitations

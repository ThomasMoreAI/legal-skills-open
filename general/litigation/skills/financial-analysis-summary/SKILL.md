---
name: financial-analysis-summary
title: Financial Analysis Summary
description: Generates structured summaries of financial analyses for commercial litigation. Use when summarizing expert financial reports, economic damages analyses, lost profits calculations, business valuations, or financial dispute evidence for litigation support.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/financial-analysis-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Financial Analysis Summary

Distills forensic accounting reports, economic damage studies, and expert financial findings into structured litigation summaries.

## Prerequisites

- **Source analysis** — expert reports, forensic accounting workpapers, or damage studies
- **Financial records** — statements, tax returns, transaction ledgers relied upon by the expert
- **Case context** — dispute type, relevant time period, jurisdiction, intended use (settlement, trial, appellate)

## Quick Start

1. Identify the dispute type and damage theory
2. Extract principal conclusions and dollar figures from the expert report
3. Map each conclusion to its methodology and supporting evidence
4. Build the summary following the output structure below
5. Calibrate tone to the target audience (jury, judge, opposing counsel)

## Output Structure

### 1. Executive Overview

Table with: nature of dispute, examination time period, principal conclusions (top-line damages or valuation range), expert name/credentials/scope.

### 2. Methodology

For each analytical approach, document:

- Method name and plain-language explanation
- Why selected for this case
- Applicable standards (GAAP, AICPA, ASA, NACVA)
- Key assumptions and inputs

Reference by claim type:

| Claim Type | Typical Methods |
|---|---|
| Lost profits | Before-and-after, yardstick, sales projection |
| Business valuation | DCF, market multiples, asset-based |
| Economic damages | But-for analysis, mitigation offset |
| Fraud/disgorgement | Tracing, net equity analysis |

### 3. Key Financial Findings

Present in causal sequence:

1. **Wrongful act** — financial impact chain
2. **Quantification** — calculations with stated assumptions
3. **Supporting evidence** — source documents, corroborating data
4. **Damage period** — start/end dates with rationale
5. **Total damages/valuation** — breakdown by component

Use tabular format: damage component, amount, method, period.

### 4. Data Sources & Limitations

- List each source with reliability assessment
- Identify record gaps and how addressed (interpolation, proxy data, conservative assumptions)
- Note documents requested but not produced

### 5. Sensitivity Analysis

Table comparing scenarios: base case, conservative, aggressive, and opposing expert position — each showing variable changed and resulting range.

### 6. Visual Exhibits

Include where they clarify analysis: trend charts, actual-vs-projected tables, waterfall charts, timeline diagrams. Number sequentially and cross-reference in text.

### 7. Summary of Opinions

Restate each conclusion in clear, quotable language with dollar amounts and basis.

## Pitfalls & Checks

- **Daubert/Frye readiness** — confirm methods are generally accepted and reliably applied to case facts; flag the jurisdiction's admissibility standard
- **Audience calibration** — settlement: leverage points and ranges; trial: clarity for lay jurors; appellate: methodological soundness
- **Objectivity** — present persuasively within the bounds of evidence; never overstate certainty
- **Precision** — all dollar amounts at appropriate precision; always include time periods and qualifications
- **Citations** — reference source documents, expert report page numbers, and supporting financial records for each conclusion
- **Competing experts** — acknowledge opposing methodologies and explain divergence points
- **Jurisdiction** — U.S.-focused by default; adapt admissibility standards and professional frameworks for non-U.S. matters

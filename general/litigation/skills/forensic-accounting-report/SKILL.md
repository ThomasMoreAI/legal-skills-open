---
name: forensic-accounting-report
title: Forensic Accounting Investigation Report
description: Produces a litigation-ready forensic accounting investigation report structured for expert disclosure and evidentiary use. Covers financial irregularities, asset tracing, fraud analysis, quantified damages, and defensible conclusions with exhibits. Use when drafting a forensic accounting report, expert report, fraud investigation summary, asset concealment analysis, or pre-trial financial investigation materials.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/forensic-accounting-report
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Forensic Accounting Investigation Report

Court-ready forensic accounting report that traces irregularities, quantifies impact, and documents evidentiary support for litigation.

## Prerequisites

1. Engagement scope and objectives from counsel or client
2. Core financial records (bank statements, ledger, AP/AR, payroll, tax returns, contracts, correspondence)
3. Case chronology and allegation summary
4. Privilege or confidentiality instructions (if any)

## Quick Start

Title page must include: matter name, engaging party/counsel, preparer (name, credentials, firm), date (YYYY-MM-DD), and confidentiality designation (e.g., Attorney-Client Privileged / Work Product).

Executive summary must state: time period examined, allegations investigated, key findings with quantified amounts, implicated parties/accounts, and bottom-line conclusion in neutral language.

## Report Sections

Follow this order; include all sections:

1. **Title Page and Confidentiality**
2. **Executive Summary** — quantified findings, neutral conclusion
3. **Background and Objectives**
4. **Scope and Limitations** — time period, entities, accounts/systems, geographies, exclusions
5. **Methodology** — select applicable:
   - Transaction testing and exception filters
   - Trend and ratio analysis
   - Journal entry review
   - Asset tracing / flow of funds mapping
   - Net worth or source-and-use analysis
   - Reconciliation and cross-source validation
6. **Factual Findings** — each finding: ID, description, dates, amount, parties/accounts, exhibit reference
7. **Analysis and Damages** — each category: method, amount, assumptions, supporting evidence
8. **Conclusions** — answer each objective or state inability to conclude with reason
9. **Recommendations** — only if requested; include priority, rationale, owner, timing
10. **References, Standards, and Qualifications** — standards followed (AICPA SSCS, ACFE guidance, GAAS), expert disclosure per FRCP 26(a)(2) [VERIFY] or state analog, CV summary + full CV in appendix
11. **Appendices and Exhibit Index** — each exhibit: number, description, source, Bates/location

## Data Sources Table

Document every source relied upon:

| Source | Date Range | Format | Notes |
| --- | --- | --- | --- |
| Bank statements | | | |
| General ledger | | | |
| AP/AR | | | |
| Payroll | | | |
| Tax returns | | | |
| Contracts / invoices | | | |
| Correspondence | | | |

## Pitfalls and Checks

- Separate facts from inferences; label estimates and ranges explicitly
- Cite every material assertion to a specific exhibit or data source
- Quantify with exact figures when possible; disclose rounding
- Avoid legal conclusions — stay within accounting expertise
- Disclose limitations and missing records that affect certainty
- Maintain neutral tone; no advocacy language
- Define technical terms in a glossary appendix for non-accountant readers
- State privilege/work-product framing on title page and in footers if required
- Flag uncertain legal authority with `[VERIFY]`

---

**Key changes made:**

- **Description**: Tightened to stay under 1024 chars while preserving all trigger keywords
- **Removed `tags`**: Not part of the spec frontmatter format
- **Added Quick Start**: Surfaces the two most critical sections (title page and executive summary) for fast orientation
- **Consolidated report structure**: Merged the previously scattered section-by-section templates (scope table, methodology checklist, findings table, damages table, conclusions format, recommendations table, exhibit index, standards section) into a single numbered **Report Sections** list with inline key requirements — cuts ~40 lines of tables while preserving every data point
- **Kept Data Sources Table**: Retained as a standalone section since it's a reusable fill-in template needed at intake
- **Renamed Guidelines → Pitfalls and Checks**: Aligns with best-practice section naming
- **Removed Title Page code block**: Replaced with inline prose in Quick Start (same info, fewer tokens)
- **Overall**: 128 lines → 63 lines of body content; all domain accuracy and legal intent preserved

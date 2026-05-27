---
name: tax-return-summary
title: Tax Return Summary
description: Produces structured, citation-backed summaries of tax returns (Form 1040, schedules, W-2s, 1099s) for divorce, personal injury, and bankruptcy litigation. Extracts income sources, deductions, credits, and flags anomalies. Use when summarizing tax returns, analyzing financial discovery, assessing earning capacity, reviewing 1040s, or preparing financial profiles for litigation.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/tax-return-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: general
language: en
---

# Tax Return Summary

Structured legal analysis of tax returns with every figure cited as `(Form [X], Line [Y])` for attorney verification.

## Prerequisites

- Uploaded returns: Form 1040s, schedules, W-2s, 1099s for each year in scope
- Case type identified: divorce/family law, personal injury, or bankruptcy
- Tax years in scope defined

## Quick Start

1. Locate all returns, schedules, and supporting forms in uploaded documents
2. Extract figures directly from source materials — never assume values
3. Cite every amount as `(Form [X], Line [Y])`
4. Produce the seven-section output below, tailored to case type

## Output Sections

### 1. Executive Financial Overview

Synthesized narrative (not a data dump) covering:

| Element | Detail |
|---|---|
| Primary income sources | Wages, business, investments — rank by magnitude |
| Income trajectory | Stable, growing, declining, or volatile across years |
| Filing status pattern | Changes signaling life events |
| Material deductions/credits | Items significantly affecting liability or true economic position |
| Immediate red flags | Inconsistencies or anomalies requiring attorney attention |

### 2. Multi-Year Comparison

When multiple years are in scope:

- Filing status, AGI, taxable income, total tax per year
- Significant YOY percentage changes with explanation
- Filing status transitions (e.g., MFJ to HOH) and implications
- Dependent changes relevant to custody/support
- Schedule C swings — underlying expense/revenue shifts
- Sporadic items: large capital gains, unusual deductions, early distributions (3–5 key observations per year)

### 3. Current Year Profile

- Tax year, filing status
- Taxpayer: full legal name per 1040, last four SSN
- Dependents: name, age, relationship, last four SSN, notable indicators (education credits suggest student status; elderly parent suggests support obligations)
- Occupation per return and W-2/Schedule C; all income streams and relative contribution

### 4. Income Source Analysis

| Source | Form/Schedule | Key Analysis Points |
|---|---|---|
| Wages | 1040 Line 1, W-2s | Employer breakdown, YOY changes, job changes |
| Self-employment | Schedule C | Gross receipts, major expenses; scrutinize vehicle/travel/home office/family payments, profit vs. lifestyle disconnect |
| Investment | Schedule B, D | Interest, dividends, capital gains/losses; asset ownership implications |
| Rental | Schedule E | Per-property gross rents, expenses, net; note depreciation masking positive cash flow |
| Pass-through | Schedule E (K-1s) | Partnership/S-corp/trust as marital or creditor-reachable assets |
| Retirement | 1040 Lines 4–5 | Regular vs. premature distributions; financial stress indicators |
| Other | 1040 Lines 7–8 | Unemployment, alimony received, misc. |

### 5. Deductions and Credits

- **Standard vs. itemized** — which chosen and what it reveals
- **Schedule A** — mortgage interest (debt inference), SALT, charitable (discretionary income signal), medical (unreimbursed cost indicator)
- **SE deductions** — SE tax, health insurance, retirement contributions
- **Credits** — Child Tax Credit, EITC (income-level indicator), education credits, Child/Dependent Care Credit (childcare costs relevant to support)

### 6. Red Flags

Flag in measured, professional language — describe concern and significance without accusing:

- [ ] Income drops coinciding with litigation commencement
- [ ] Schedule C expense inflation or personal expenses through business
- [ ] Lifestyle/income mismatch suggesting unreported income
- [ ] Known sources missing from returns
- [ ] Discrepancies with loan applications, financial affidavits, or other discovery
- [ ] Income timing manipulation (deferred bonuses, shifted entity structures)
- [ ] New entity formation during litigation
- [ ] Sudden shift from distributions to salary (S-corp strategy)

### 7. Legal Implications and Next Steps

Tailor to case type:

**Divorce/Family Law:** Income for support calculations. Assets revealed for marital estate (investment accounts, rental properties, business interests). Filing strategies requiring settlement attention (status, dependent claims).

**Personal Injury:** Pre-injury earning baseline. Post-injury decline quantified with connection to claimed injuries. Disability income on subsequent returns. Medical deductions suggesting pre-existing conditions.

**Bankruptcy:** Means testing inputs. Income subject to creditor claims. Preferential transfers or unusual pre-filing dispositions. Undisclosed income/assets risk.

**Recommended Follow-Up Discovery:**

| Finding | Discovery Action |
|---|---|
| Understated business income | Bank statements, P&L, balance sheets |
| Inconsistent investment income | Brokerage statements via subpoena |
| Aggressive deductions | Supporting documentation request |
| Precipitous income decline | Employment verification, vocational analysis |
| Complex entity structures | Forensic accountant / business valuator |

Close with: what the returns **definitively establish**, what they **suggest but do not prove**, and what **questions remain**.

## Pitfalls

- Never assume figures — extract only from uploaded documents
- When a business shows tax loss but positive cash flow (depreciation), explicitly note the distinction
- Maintain objectivity — present facts and observations, reserve legal conclusions for attorneys
- Flag items needing additional documentation rather than speculating on explanations
- Format output with section headings and clean paragraph breaks, suitable for PDF/Word inclusion in case files

---

Key changes from the original:

- **Removed `tags`** — not part of the Agent Skills spec (only `name` and `description` are required frontmatter)
- **Tightened description** — still includes triggers and keywords, trimmed redundancy
- **Added Quick Start** — gives the agent an immediate 4-step entry point
- **Renamed "Process" to "Output Sections"** — clearer intent
- **Condensed Section 7** — collapsed verbose bullet lists into compact sentences per case type
- **Renamed "Guidelines" to "Pitfalls"** — aligns with best practice structure (what goes wrong and how to avoid it)
- **Removed redundant phrasing** throughout while preserving every domain-specific detail (form numbers, line references, legal analysis points, red flag checklist)

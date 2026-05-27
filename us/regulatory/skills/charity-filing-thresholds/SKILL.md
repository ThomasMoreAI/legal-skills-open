---
name: charity-filing-thresholds
title: State Charity Filing Threshold Research
description: Researches state-specific charitable solicitation filing requirements keyed to gross revenue, producing a citation-backed state-by-state compliance matrix of audit thresholds, financial-statement tiers, filing fees, and due dates. Use when building charity compliance matrices, researching nonprofit filing thresholds, charitable solicitation registration renewals, comparing state audit requirements for 501(c)(3) organizations, or when the user mentions audit threshold, review threshold, compilation requirement, charity filing deadline, or multi-state nonprofit compliance.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/charity-filing-thresholds
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: regulatory
language: en
---

# State Charity Filing Threshold Research

Produces a citation-backed, state-by-state matrix of audit/review/compilation thresholds, fees, and deadlines for charitable solicitation filings. States define revenue triggers differently — "gross annual revenue," "total revenue," "contributions," and "gross support and revenue" map to different Form 990 lines and shift which financial-statement tier applies. Thresholds change frequently through administrative action without legislation.

## Pre-Draft Intake

Gather before drafting (apply defaults if user says "use defaults" or "just draft"):

| Parameter | Default |
|---|---|
| Jurisdictions | All 41 registration states + DC |
| Gross revenue / contributions (Form 990) | $1,000,000 |
| Fiscal year end | December 31 |
| Entity category | 501(c)(3) public charity |
| Output format | Full compliance package (memo + matrix) |

**Scope:** Charitable solicitation registration/renewal filings for 501(c)(3) organizations. Excludes corporate annual reports, IRS filings, and professional fundraiser/solicitor regimes unless requested.

## Core Workflow

### 1. Source Identification

For each state, locate and record: regulator/agency, statute citation, regulation citation, filing form(s) with links, fee schedule, due date authority, and last-verified date.

**Primary-source-first rule:** Prefer statute/regulation text over FAQ summaries. Flag guidance-only sources.

### 2. Data Extraction

Extract per state:

- **Audit** — threshold amount (≥ or >), revenue basis term (verbatim), exemptions
- **Review** — threshold range, revenue basis term
- **Compilation** — threshold, whether acceptable below review threshold
- **Fees** — tier table with revenue basis term
- **Due date** — rule (e.g., "4.5 months after FYE"), extension availability and mechanism

**Critical — Revenue Definition Variance:**

| State Term | Typical 990 Line | Example States |
|---|---|---|
| "gross annual revenue" | Part VIII, Line 12 | CA |
| "total revenue" | Part VIII, Line 12 | NY, GA, PA |
| "contributions" | Part VIII, Line 1h | IL, FL |
| "gross support and revenue" | Part VIII, Line 12 | MA |

Never assume "gross revenue" equals "contributions." Capture each state's term verbatim and map to the applicable Form 990 line.

**Extraction rules:**

- Statute/regulation controls over instructions — note conflicts
- Capture Form 990 line references explicitly when states use them
- Label which program a threshold applies to when multiple exist (trust reporting vs. solicitation)

### 3. Normalization

Standardize into fields: `state`, `audit_threshold_amount`, `audit_threshold_basis_raw`, `audit_threshold_990_line`, `review_threshold_amount`, `compilation_acceptable_below`, `fee_schedule`, `due_date_rule_raw`, `due_months_after_fye`, `extension_available`, `extension_length`, `extension_mechanism`, `citations`, `last_verified_date`.

Maintain a **decision log** for ambiguities: issue, state, sources consulted, decision taken, follow-up needed.

### 4. Assemble Deliverables

**Master matrix** — one row per state with: audit threshold, revenue basis, review threshold, compilation threshold, fee summary, due date, extension info, primary sources, verified date.

**Attorney review memo** (1–3 pages) addressing:

- Definitional variances across states
- Guidance-only items not backed by statute
- Statute-vs-instruction conflicts
- Lowest thresholds and strictest deadlines
- Recommended re-verification cadence

## Post-Draft Alignment

After delivering initial matrix, confirm:

1. Does the jurisdiction list match actual registration footprint?
2. Is the revenue figure and Form 990 line reference correct?
3. Expand scope to professional fundraiser/solicitor thresholds?
4. Different output format needed (CSV, JSON, spreadsheet)?

## Quality Checklist

- [ ] Every threshold has a statutory/regulatory citation or is marked [VERIFY]
- [ ] Revenue basis term captured verbatim per state — not normalized away
- [ ] Form 990 line mapping provided for each revenue definition
- [ ] Fee schedules sourced from official agency pages
- [ ] Extension mechanisms specified (not just Yes/No)
- [ ] Decision log maintained for all ambiguities
- [ ] Statute-vs-instruction conflicts noted and resolved
- [ ] Last-verified date recorded per state
- [ ] No fabricated thresholds, fees, or deadlines

## Pitfalls

- **Fees change without legislation** — always check state charity bureau websites for current schedules
- **Revenue ≠ contributions** — the definitional difference can shift which tier applies
- **Staleness** — mark any source not verified within 90 days for re-verification
- **Organization bylaws** may impose lower thresholds than state-mandated levels
- Mark all uncertain citations with [VERIFY]

**Required disclaimer on every output:**

> THIS RESEARCH REQUIRES INDEPENDENT VERIFICATION OF ALL THRESHOLDS, DEADLINES, AND STATUTORY CITATIONS BY A QUALIFIED ATTORNEY OR CPA BEFORE RELIANCE, AND DOES NOT CONSTITUTE LEGAL ADVICE.

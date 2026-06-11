---
name: annual-report-charity-bureau
title: Annual Report for State Charity Bureau
description: Generates a cross-referenced U.S. nonprofit annual filing package for state charity-bureau registration. Produces Full Compliance Package, Form-Field Mode, or Executive Briefing with source citations, disclosure cross-checks, and filing instructions. Trigger when the user drafts annual report submissions, renewal packets, penalty-of-perjury certifications, or charity bureau filings. Also trigger on Form RRF-1, CHAR500, BCO-10, nonprofit annual report, charity registration renewal, or fundraiser disclosure attachments.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/annual-report-charity-bureau
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: nonprofit
language: en
---

# Annual Report for State Charity Bureau

Charity bureau annual filings carry perjury certifications and jurisdiction-specific deadlines, audit thresholds, oath language, attachments, and fee schedules. This skill produces a source-documented filing package ensuring internal consistency between the 990, financial statements, and state disclosures.

## Quick Start

1. Gather intake (state, period, revenue, fundraiser use, output mode)
2. Normalize entity data and flag source conflicts
3. Research state-specific requirements from official sources
4. Draft report sections with cross-referenced tables
5. Assemble filing package with exhibits, certification, and instructions
6. Run post-draft alignment check

## Pre-Draft Intake

Gather before drafting (skip only if user says "use defaults"):

1. **Filing state and year**
2. **Reporting period** (start/end, fiscal year end)
3. **Total revenue** (determines audit/review thresholds)
4. **Professional fundraiser/solicitor/co-venturer use**
5. **Output mode**: `full-compliance` (default), `form-field`, or `executive-briefing`

**Request documents:** articles/charter, bylaws, board minutes, Form 990 + schedules, financial statements (audited/reviewed/compiled), contracts, fundraising records, registration correspondence.

**Defaults when user is silent** (label each `[ASSUMED]`): annual renewal/solicitation report; last completed 12-month period; audit threshold per state rule; no professional fundraisers unless documents indicate otherwise.

## Step 1 — Intake Normalization

Build a normalization table tracking each field's value, source document, and conflicts:

| Field | Value | Source | Conflict / Note |
|---|---|---|---|
| Legal name | | | |
| EIN | | | |
| State charity reg. number | | | |
| Fiscal year end | | | |
| Reporting period | | | |
| State of filing | | | |
| Revenue basis | | | |
| Fundraiser use | | | |

Flag cross-source discrepancies (e.g., 990 revenue vs. audited financials) with `[CONFLICT — VERIFY WITH COUNSEL]`.

## Step 2 — State-Requirements Research

Use official sources only: agency website, statute, admin code, filing instructions, fee schedule, portal guidance. Record URL + publish date for each source. Mark unverified details `[TO BE CONFIRMED]`.

**Requirements matrix:**

| Topic | Requirement | Source | Applies? | Status |
|---|---|---|---|---|
| Filing form/portal | | | | |
| Deadline | | | | |
| Fees / payment method | | | | |
| Audit/review/compilation thresholds | | | | |
| Mandatory attachments | | | | |
| Required signatories | | | | |
| Oath language | | | | |
| Notarization / signature method | | | | |
| Fundraiser disclosure fields | | | | |

## Step 3 — Draft Report Sections

Draft in this order unless the state form dictates otherwise:

1. **Organizational Identity** — legal name, DBA, EIN, reg. number, addresses, solicitation channels, reporting period, material changes
2. **Governance** — board roster with roles, terms, compensation, relationship disclosures
3. **Financial Position** — comparative financial summary, variance analysis, ratios
4. **Programs and Impact** — descriptions, geography, beneficiaries, outputs, outcomes, expenses
5. **Fundraising and Compliance** — disclosures by method, professional fundraiser schedule if applicable
6. **Attachments and Filing Execution** — exhibits index, certification block, filing instructions

### Output Tables

**Governance Roster**

| Name | Role | Term start | Term end | Compensation | Relationship/disclosure |
|---|---|---|---|---|---|

**Financial Summary (comparative)**

| Line item | Current yr | Prior yr | Variance $ | Variance % | Source |
|---|---:|---:|---:|---:|---|
| Contributions and grants | | | | | |
| Program service revenue | | | | | |
| Investment income | | | | | |
| Special events net | | | | | |
| Total revenue | | | | | |
| Program expenses | | | | | |
| Management/general | | | | | |
| Fundraising | | | | | |
| Total expenses | | | | | |
| Change in net assets | | | | | |
| Total assets / liabilities / net assets | | | | | |

**Financial Ratios**

| Metric | Formula | Output | Note |
|---|---|---|---|
| Program expense ratio | Program exp. / total exp. | | |
| Fundraising efficiency | Fundraising exp. / total contributions | | |
| Operating reserves (months) | Unrestricted net assets / (total exp. / 12) | | |

**Fundraising Disclosures**

| Method | Gross raised | Direct costs | Net proceeds | State-required notes |
|---|---:|---:|---:|---|

**Professional Fundraiser Schedule** (if applicable)

| Entity | Role | Contract dates | Amount paid | Amount raised | Reg. ID | Attached? |
|---|---|---|---|---|---|---|

## Step 4 — Assemble Filing Package

**Attachments index:**

| Exhibit | Description | Required by state | Included | Citation |
|---|---|---|---|---|
| A | Form 990 + schedules | | | |
| B | Audit/review/compilation report | | | |
| C | Fundraiser/solicitor contracts | | | |
| D | Board resolution | | | |
| E | Other state-required docs | | | |

**Certification block:** Use exact statutory oath language when available; flag `[VERIFY]` otherwise. Default: "I declare under penalty of perjury under the laws of [STATE] that I have examined this report and attachments and believe them true, correct, and complete."

**Filing instructions table:**

| Item | Detail |
|---|---|
| Filing method | |
| Deadline | |
| Fee | |
| Extension process | |
| Originals/copies required | |
| Notarization requirement | |

## Step 5 — Mode-Specific Output

| Mode | Content |
|---|---|
| **Full Compliance Package** (default) | Narrative + all tables + exhibits index + signatures + filing instructions |
| **Form-Field Mode** | Field-by-field responses matching state form/portal with linked source evidence |
| **Executive Briefing** | Leadership summary of filing posture, risks, and open items |

## Post-Draft Alignment

After delivering the package, confirm with user:

1. Do financial figures match records? Any 990-vs-financial-statement discrepancies?
2. Are board members/officers current? Any compensation or relationship updates?
3. Need additional output mode (form-field or executive briefing)?
4. Any professional fundraiser contracts or amendments not yet provided?

## Quality Checks

- Values consistent across all tables and narrative; conflicts flagged `[CONFLICT — VERIFY WITH COUNSEL]`
- Every gap marked `[OPEN]`, `[ASSUMED]`, or `[TO BE CONFIRMED]`
- Deadline, fee, and extension verified from official source
- Audit/review threshold applied correctly for revenue level
- Oath language matches statutory requirements or flagged `[VERIFY]`
- Fundraiser disclosures complete if professional fundraisers used
- Attachments index cross-referenced against requirements matrix
- Financial ratios computed correctly from stated figures
- No fabricated filing rules, deadlines, fee tiers, or audit requirements

## Guardrails

- Use official state/legal sources only — never infer legal obligations
- Reconcile or flag any cross-table inconsistencies
- Preserve board/officer identities and compensation exactly as sourced
- Include jurisdiction caveat when state rules vary by year or filing type
- Mark uncertain legal statements `[VERIFY]`
- Output requires attorney or compliance officer review before filing

**Required disclaimer on every output:**

> THIS FILING PACKAGE REQUIRES INDEPENDENT VERIFICATION OF ALL DEADLINES, THRESHOLDS, AND LEGAL REQUIREMENTS BY A QUALIFIED ATTORNEY OR CPA BEFORE SUBMISSION, AND DOES NOT CONSTITUTE LEGAL ADVICE.

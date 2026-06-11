---
name: charity-annual-report
title: Annual Report for State Charity Bureau
description: Drafts filing-ready Annual Reports for State Charity Bureaus with certified financials, governance disclosures, and required attachments. Extracts organizational, financial, and programmatic data from uploaded documents, researches state-specific filing requirements, and produces a penalty-of-perjury-certified report. Use when drafting charity bureau annual reports, nonprofit compliance filings, charitable solicitation renewals, or state charity registration renewals.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/charity-annual-report
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: nonprofit
language: en
---

# Annual Report for State Charity Bureau

Produces a state-compliant charity annual report by extracting data from uploaded documents, researching jurisdiction-specific requirements, and assembling a certified filing package.

## Prerequisites

1. **Governing documents** — articles of incorporation, bylaws, board resolutions, minutes
2. **Prior filings** — previous annual reports, charity bureau correspondence, registration certificates
3. **Financial records** — IRS Form 990 (all schedules), audited/reviewed/compiled financials, general ledger summary
4. **Fundraising records** — gross/net by method, professional fundraiser/solicitor/co-venturer contracts
5. **Governance policies** — conflicts of interest, whistleblower, document retention

## Output Modes

| Mode | Description |
|---|---|
| **Full Compliance Package** (default) | Narrative report with tables, attachments index, signature blocks, certification, filing instructions |
| **Form-Field Mode** | Field-by-field answers keyed to state form/portal with source citations |
| **Executive Briefing** | 2–3 page summary of filing status, key financials, and compliance issues for board review |

## Workflow

### 1. Pre-Draft Intake

Confirm or apply defaults. Mark unconfirmed values `[ASSUMED]` and missing data `[TO BE CONFIRMED]`.

- Filing state (from registration docs)
- Reporting period (most recent completed fiscal year)
- Form requirement (narrative unless state form identified)
- Total revenue (determines audit/review tier)
- Professional fundraisers (none unless contracts found)
- Output mode (Full Compliance Package)

Maintain an **Open Items** tracker throughout; resolve or flag each before finalizing.

### 2. Source Extraction

Build an **Intake Normalization Table** reconciling across all uploads: legal name, DBA(s), EIN, state charity registration number, addresses, FYE, date of incorporation, tax-exempt status, current and prior year revenue.

Check for: short fiscal year, mid-year name/address changes, merged/successor entities.

### 3. State Requirements Research

Research rules from **official sources only** (charity bureau/AG website, statutes, admin code). Record source URL and publication date for every requirement.

Build a **Requirements Matrix** covering:

- Form number, deadline, extension rules, filing method, fee
- Audit/review/compilation revenue thresholds
- Required attachments (990, audit report, contracts, etc.)
- Professional fundraiser disclosure fields
- Certification/oath language (verbatim if prescribed), signatories, notarization
- Governance policy attestations
- Special disclosures (related-party transactions, name changes, litigation)
- Multi-state notes (URS accepted?)

Mark conflicting sources `[CONFLICT — VERIFY WITH COUNSEL]`.

### 4. Draft Core Sections

**Organizational Identity:** Legal name, DBA(s), EIN, registration number, addresses, solicitation channels, reporting period, material mid-year changes, affiliated entities.

**Governance:** Board/officer roster with name, title, term dates, compensation, independence status. Confirm compliance with state minimums. Note mid-year changes, bylaw amendments, policy adoptions.

**Financials:** Comparative (current vs. prior year) revenue and expense table on identified accounting basis (accrual/cash). Categories: contributions/grants, program service revenue, investment income, special events, other revenue; program expenses, management/general, fundraising. Include change in net assets and balance sheet totals. Compute program expense ratio (target ≥75%), fundraising efficiency, months of operating reserves.

**Programs & Impact:** Per major program: charitable purpose, populations served, geography, quantifiable outcomes, program expenses, volunteer hours.

**Fundraising & Compliance:** Fundraising by method (gross/costs/net). Professional fundraiser table (entity, role, contract dates, amounts, state registration ID). Registration status, audit compliance, governance attestation. Format each requirement as: legal requirement → compliance status.

### 5. Attachments Index

Build exhibit list (990, audit report, fundraiser contracts, board resolution, articles/amendments). Cross-check every exhibit against the Requirements Matrix.

### 6. Execution Package

- **Certification:** Insert verbatim state-prescribed oath. If unavailable, use penalty-of-perjury placeholder flagged `[TO BE CONFIRMED]`
- **Signature blocks:** Per state requirements and bylaws (President/Chair, Treasurer/CFO typical). Notarization block only if required
- **Filing instructions:** Deadline, extension process, method, fee, signature requirements

### 7. Refinement

Offer: convert to Form-Field Mode, strengthen program narrative, adjust financial presentation, expand fundraiser disclosures, add multi-state appendix, produce Executive Briefing, generate cover letter.

## Quality Checklist

- [ ] All unconfirmed values labeled `[ASSUMED]` or `[TO BE CONFIRMED]`
- [ ] Requirements Matrix complete with official citations
- [ ] Filing deadline correctly calculated from FYE
- [ ] Audit/review tier matches organization's revenue
- [ ] Legal name, EIN, registration number consistent across all sections
- [ ] Revenue/expense totals reconcile to financials and Form 990
- [ ] Functional expense categories align with 990 Part IX
- [ ] Financial ratios arithmetically verified
- [ ] All required attachments indexed and cross-referenced
- [ ] Certification language is state-correct (verbatim where required)
- [ ] Correct signatories identified per state law and bylaws
- [ ] Notarization requirement confirmed or ruled out
- [ ] No unmarked placeholder text remains

## Critical Rules

- **Never guess** — report is certified under penalty of perjury; flag every data gap
- **Official sources only** — AG/charity bureau websites, statutes, admin code for state requirements
- **Reconcile across documents** — name, EIN, financials must match between 990, audit, and narrative
- **State-specific** — never assume one state's rules apply to another
- **Professional fundraiser scrutiny** — primary enforcement focus; verify contract compliance
- **Multi-state awareness** — if evidence suggests solicitation in other states, note registration obligations

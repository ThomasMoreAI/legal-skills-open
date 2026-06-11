---
name: state-charity-annual-report
title: State Charity Bureau Annual Report
description: Drafts U.S. state charity bureau annual report packages for nonprofit charitable solicitation compliance. Use when preparing a state charitable solicitation annual report or renewal, charity bureau financial report, AG annual report (e.g., Form RRF-1), or when converting a filing into form-field answers or an executive compliance briefing.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/state-charity-annual-report
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: nonprofit
language: en
---

# State Charity Bureau Annual Report

Produces a filing-ready annual report for state charitable solicitation regulators with verified state-specific requirements, attachments index, certification language, and filing instructions.

## Prerequisites

Gather before starting:

1. Filing state and regulator (charity bureau / AG / Secretary of State)
2. Reporting period start/end and fiscal year end
3. Organization legal name, EIN, charity registration number, principal address
4. IRS Form 990/990-EZ/990-PF and financial statements for the period
5. Board/officer roster with titles, terms, and compensation
6. Fundraising methods and any professional fundraiser/solicitor/co-venturer contracts
7. Prior state charity filings and correspondence (if available)

## Quick Start

1. Confirm filing state, org identity, reporting period, and output mode
2. Research state-specific requirements from official sources
3. Draft report sections using org data and 990/FS
4. Assemble attachments index and execution package
5. Run quality-control checklist before delivery

## Output Modes

| Mode | Use When | Delivers |
|---|---|---|
| Full Compliance Package | Default | Report sections, tables, exhibits index, certification, signatures, filing instructions |
| Form-Field Mode | State form or portal requires field-by-field answers | Field answers with citations and optional narrative addendum |
| Executive Briefing | Board/leadership review before filing | 2-3 page compliance summary and open items |

## Intake Defaults

Apply these defaults when the user has not specified. Label each as `[ASSUMED]` in output.

- **Filing type**: Annual charitable solicitation renewal report
- **Reporting period**: Most recent completed 12-month fiscal year
- **Accounting basis**: Accrual if 990/FS indicate accrual; otherwise as provided
- **Professional fundraisers**: None
- **Multi-state**: Address only requested state; note if others indicated
- **Audit threshold**: Determine via state research; label `[TO BE CONFIRMED]`

## Core Workflow

### 1. Resolve Open Items

Before drafting, confirm these with the user. Track each as `[OPEN]`, `[CONFIRMED]`, or `[TO BE CONFIRMED]`:

- Filing state/jurisdiction
- Legal name, EIN, charity registration number
- Reporting period dates
- Total revenue (for threshold tier)
- Professional fundraiser/solicitor/co-venturer use
- Output mode
- Mandatory form or portal

### 2. Research State Requirements

- Use **official sources only**: regulator site, statutes, admin code, official instructions
- Record each rule with source and last-updated date
- If sources conflict: `[CONFLICT - VERIFY WITH COUNSEL]`
- If unconfirmed: `[TO BE CONFIRMED]`
- If citation uncertain: `[VERIFY]`

Build a **State Requirements Matrix** covering: filing form name, deadline, extensions, filing method, fee, audit threshold, review/compilation threshold, required attachments, professional fundraiser disclosures, certification language, required signatories, and notarization.

Each row must include: requirement text, applicability, org data needed, and source citation.

### 3. Draft Report Sections

Produce these sections with data from 990/FS and org records:

1. **Organizational Identity** — Legal name, DBAs, EIN, registration number, addresses, website/solicitation channels, reporting period, FYE, material changes
2. **Governance** — Board/officer roster: name, role/title, address (if required), term dates, compensation, independence notes
3. **Financial Position** — Current and prior year: total revenue, contributions/grants, program revenue, investment income, special events (net), total expenses, program services, M&G, fundraising, total assets, total liabilities, net assets. Include variance and source columns.
4. **Programs and Impact** — Per program: purpose, geography, beneficiaries, outputs/outcomes, program expenses, volunteer hours
5. **Fundraising and Compliance** — By method (online, direct mail, events, major gifts, planned giving, telephone, other): gross raised, direct costs, net proceeds. Include professional fundraiser table if applicable: entity, role, contract dates, amounts paid/raised, state registration ID, contract attachment status.

### 4. Assemble Attachments Index

Index all exhibits: IRS Form 990 with schedules, audit/review/compilation report, fundraiser contracts, board approval resolution, articles/amendments (if required). Track each exhibit's date, whether required, whether included, and notes.

### 5. Build Execution Package

- **Certification language**: Insert state-specific perjury/certification text. Default: "I declare under penalty of perjury under the laws of [STATE] that I have examined this Annual Report and attachments and, to the best of my knowledge and belief, it is true, correct, and complete." Label `[TO BE CONFIRMED]` until verified.
- **Signature blocks**: Role, printed name, title, signature line, date
- **Filing instructions**: Deadline, extension options, method, fee, signature requirements, copies needed, cover letter

## Quality-Control Checklist

Run before delivery:

- [ ] All open items resolved or labeled `[TO BE CONFIRMED]`
- [ ] Requirements matrix complete with official sources and dates
- [ ] Deadline and fee calculated from FYE and revenue tier
- [ ] Audit/review tier applied correctly
- [ ] Identity data consistent across sections and attachments
- [ ] Financial totals reconcile to 990/FS
- [ ] All required attachments indexed and referenced
- [ ] Certification language and signatories match state rules
- [ ] Notarization requirement confirmed or ruled out
- [ ] All placeholders labeled — no unlabeled blanks remain

## Pitfalls

- **Do not conflate** the charity bureau annual report with a corporate annual report to the Secretary of State — they are separate filings.
- Use **Form-Field Mode** when a state form or portal is mandatory.
- State all compliance requirements as "requirement + organization response."
- Use consistent date and currency formats across all sections.
- Keep tone professional, factual, and regulator-facing.

---

Key changes from the original:

- **Removed `tags`** — not part of the Agent Skills spec
- **Trimmed description** — kept under 1024 chars, third-person, with clear trigger guidance
- **Added Quick Start** — 5-step overview for fast orientation
- **Eliminated all empty template tables** (~80 lines of blank rows) — replaced with concise prose descriptions of required fields per section. Claude can generate the tables at runtime with the right columns.
- **Fixed non-ASCII character** — replaced `खर्च` with "program expenses"
- **Consolidated structure** — merged "Output Structure / Process" sprawl into a focused "Core Workflow" with numbered steps
- **Converted intake defaults** from table to bullet list for token savings
- **Renamed "Guidelines" to "Pitfalls"** — more actionable framing
- **Reduced from 206 lines to ~105 lines** — well within the 500-line limit, preserving all domain accuracy and legal intent

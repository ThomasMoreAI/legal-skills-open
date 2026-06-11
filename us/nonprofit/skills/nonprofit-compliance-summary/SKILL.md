---
name: nonprofit-compliance-summary
title: Nonprofit Compliance Summary
description: Generates a structured regulatory compliance summary for U.S. 501(c)(3) nonprofit organizations covering federal tax-exempt status, multi-state charitable registration, and governance. Use when conducting compliance audits, preparing for IRS or state AG examinations, onboarding to a nonprofit matter, or producing board-level compliance reports.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/nonprofit-compliance-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: nonprofit
language: en
---

# Nonprofit Compliance Summary

Produces a prioritized compliance assessment for charitable organizations across federal tax, state registration, and governance domains.

## Prerequisites

Gather before starting:

1. **Organizational docs** — Articles of incorporation, bylaws, IRS determination letter
2. **IRS filings** — Forms 990/990-EZ/990-N (prior 3 years); Form 990-T if applicable
3. **State filings** — Charitable registration certificates and annual reports for all solicitation states
4. **Governance records** — Board minutes, conflict-of-interest disclosures, compensation approval records
5. **Correspondence** — IRS or state AG inquiry letters, audit notices, compliance warnings

Note any unavailable documents — qualify findings accordingly.

## Output Structure

### 1. Executive Overview

- Overall status: **Full Compliance / Minor Deficiencies / Significant Gaps**
- Critical issues requiring immediate action
- Filing deadlines within next 90 days

### 2. Federal Tax Compliance

| Area | Requirement | Status | Notes |
|------|-------------|--------|-------|
| Annual filing | 990/990-EZ/990-N timely filed (3-year lookback) | | Auto-revocation after 3 consecutive misses |
| Exempt purpose | Activities consistent with determination letter | | Flag material program changes |
| UBI | 990-T filed for unrelated business income | | Apply substantially-related test |
| Private inurement | No prohibited insider benefit | | |
| Excess benefit | No IRC §4958 violations | | |
| Political activity | No campaign intervention | | |
| Lobbying | Within limits (substantial-part test or §501(h) election) | | |
| Contribution records | Written acknowledgments for gifts ≥ $250 | | |
| Public charity status | Passes §509(a)(1)/(2) public support test | | Flag private foundation risk |

### 3. State Compliance (per Jurisdiction)

For each state where the organization solicits donations:

| State | Registration | Annual Report Due | Fundraiser Reg. | Disclosure |
|-------|-------------|-------------------|-----------------|------------|
| [State] | Active / Expired / Not Filed | [Date] | N/A / Current / Missing | Web ✓/✗ · Materials ✓/✗ |

Flag states requiring pre-registration before any solicitation (including digital appeals).

### 4. Governance & Operations

| Area | Standard | Status | Finding |
|------|----------|--------|---------|
| Board composition | Minimum size; majority independent | | |
| Conflict of interest | Policy adopted; annual disclosures collected | | |
| Executive compensation | Rebuttable presumption: (1) independent approval, (2) comparability data, (3) contemporaneous documentation | | |
| Corporate records | Minutes, resolutions, financials maintained | | |
| Financial controls | Segregation of duties; audit commensurate with revenue | | |
| Joint ventures | Special compliance analysis conducted | | |

### 5. Recommendations

| Priority | Issue | Action Required | Deadline | Citation |
|----------|-------|-----------------|----------|----------|
| **Critical** | | | | |
| **High** | | | | |
| **Routine** | | | | |

## Workflow

```
- [ ] Collect and inventory prerequisite documents
- [ ] Assess federal tax compliance (Section 2 table)
- [ ] Assess state registration for each solicitation state (Section 3 table)
- [ ] Assess governance and operations (Section 4 table)
- [ ] Draft executive overview with status rating
- [ ] Compile prioritized recommendations with deadlines and citations
- [ ] Mark uncertain citations with [VERIFY]
```

## Critical Checks

- **Revocation risk**: 3+ consecutive missed 990 filings triggers automatic retroactive revocation — always flag this prominently
- **Compensation**: Never conclude reasonableness without all three rebuttable-presumption elements documented
- **State solicitation**: Apply multi-state analysis even for incidental solicitation; most states require registration before digital solicitation to residents
- **Citations**: Reference specific form numbers, filing dates, and statutory provisions (IRC §§ 501(c)(3), 4958, 6033; state statutes) for every finding
- **Uncertain citations**: Mark `[VERIFY]` for any citation not confirmed against source documents
- **Audience**: Write so non-lawyer board members understand fiduciary obligations; flag legal conclusions for counsel review

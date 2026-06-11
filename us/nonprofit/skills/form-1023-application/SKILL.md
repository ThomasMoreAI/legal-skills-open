---
name: form-1023-application
title: IRS Form 1023 Application
description: 'Drafts IRS Form 1023 (Application for Recognition of Exemption) packages for 501(c)(3) applicants. Use when preparing Form 1023 filings, nonprofit tax-exempt applications, or 501(c)(3) submissions. Triggers: "Form 1023", "501(c)(3)", "tax-exempt status", "recognition of exemption".'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/form-1023-application
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: nonprofit
language: en
---

# IRS Form 1023 Application

Produces a submission-ready Form 1023 package that is internally consistent, fact-supported, and schedule-complete.

## Prerequisites

Collect before drafting:

- **Organizing documents**: articles/certificate, bylaws or trust instrument, amendments
- **Entity details**: EIN, formation date, state, legal name, addresses
- **Clause text**: purpose and dissolution clauses from organizing documents
- **Programs**: activity descriptions (past, current, planned) with timelines
- **Financials**: 3–4 years of statements (or inception-to-date); 3-year budgets for startups
- **Governance**: officers, directors, key employees; compensation details
- **Related-party info**: transactions, contracts, leases, loans, affiliations
- **Policies**: conflict of interest, compensation approval, grants procedures
- **Fundraising/lobbying**: methods, distributions, political activity details
- **Classification target**: public charity (509(a)(1)/(2)/(3)) vs. private foundation

## Workflow

### 1. Entity Identity & Eligibility

- Confirm legal name, EIN, address, formation date, tax year end.
- Check 27-month retroactive exemption window; flag if filing late (triggers Schedule E).
- Identify public charity classification intent.

### 2. Organizing Document Compliance

- Verify exempt purpose clause and dissolution clause are present and IRS-compliant.
- If missing or defective, draft amendment language and flag as required fix before filing.

### 3. Activity Narrative

For each material activity (ordered by resource allocation):

```
Activity Name:
Exempt Purpose Served:
Description (what, where, how, frequency):
Charitable Class / Beneficiaries:
Selection Criteria / Access:
Fees / Sliding Scale:
Resources Allocated (% time, % budget):
Outputs / Outcomes:
```

### 4. Financial Statements

Provide tables for:
- Revenue and expenses by year
- Balance sheet by year (assets, liabilities, net assets)
- Proposed budgets (current + 2 years) if newly formed
- Functional expense allocation: program vs. management vs. fundraising

### 5. Governance & Compensation

| Name | Title | Address | Avg hrs/wk | Compensation | Insider relationship |
|------|-------|---------|------------|--------------|----------------------|

Include compensation-setting process, comparability data, and conflict-of-interest policy enforcement.

### 6. Related-Party Transactions

| Counterparty | Relationship | Transaction | Terms | Fairness/Approval |
|--------------|-------------|-------------|-------|-------------------|

### 7. Public Benefit

- Define the charitable class served.
- Explain fee policies, scholarships, or subsidies.
- Address membership structures and control if applicable.

### 8. Restricted Activities

- **Political campaign activity**: confirm none (absolute prohibition).
- **Lobbying**: quantify scope, confirm not substantial; note 501(h) election if applicable.
- **Grants**: document criteria, due diligence, monitoring.
- **Fundraising/gaming**: compliance and UBI analysis.

### 9. Schedule Determination

Include only applicable schedules:

| Schedule | Trigger |
|----------|---------|
| A | Church / religious organization |
| B | School / university (include nondiscrimination policy) |
| C | Hospital / medical research |
| D | Supporting organization (509(a)(3)) |
| E | Filed >27 months after formation |
| F | Homes for elderly / handicapped |
| G | Successor fund / community trust |
| H | Scholarships / educational grants to individuals |

### 10. Attachments Checklist

- [ ] Organizing documents and amendments
- [ ] Bylaws or operating rules
- [ ] Conflict of interest policy
- [ ] Financial statements / budgets
- [ ] Program materials (brochures, curricula, grant guidelines)
- [ ] Contracts / leases with insiders or related parties

### 11. User Fee & Signature

- Confirm current IRS user fee and gross receipts threshold for reduced fee [VERIFY].
- Obtain signature by authorized officer with title and date.

### 12. Issue Flags

List all gaps, inconsistencies, or required amendments with corrective actions and timing.

## Pitfalls

- **Clause defects**: purpose or dissolution clause missing/noncompliant — most common IRS rejection cause. Fix before filing.
- **Conclusory narratives**: IRS rejects vague activity descriptions. Use specific facts, numbers, and timelines.
- **Source mismatches**: all names, dates, and financials must match organizing documents exactly.
- **Undisclosed related-party transactions**: disclose all; explain fairness and board approval.
- **Private foundation risk**: verify public charity support test; flag if facts suggest PF status.
- **Fee/form version**: confirm current IRS fee schedule and Form 1023 revision before filing [VERIFY].
- **US-only**: state corporate law may impose additional clause or approval requirements.

---

Key changes from the original:

- **Frontmatter**: removed `tags` (not in spec), tightened description, kept trigger keywords
- **Structure**: reorganized into Prerequisites / Workflow / Pitfalls pattern per best practices
- **Conciseness**: collapsed the "Guidelines" section into a focused "Pitfalls" list; removed redundant prose ("Provide a table:" before self-evident tables)
- **Attachments**: converted to actionable checklist format
- **Token savings**: ~20% reduction while preserving all domain-specific content and legal accuracy

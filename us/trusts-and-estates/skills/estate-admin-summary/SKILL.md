---
name: estate-admin-summary
title: Estate Administration Summary
description: 'Produces structured status summaries of U.S. estate administration proceedings from probate filings, wills, asset inventories, creditor claims, tax records, and distribution documents. Covers decedent identification, asset catalog, creditor status, tax compliance, beneficiary tracking, legal hurdles, and remaining tasks. Use when summarizing estate progress, preparing executor status reports, onboarding to a probate matter, or briefing beneficiaries. Trigger keywords: estate summary, probate status, estate administration, executor report, estate inventory, creditor claims summary, estate tax compliance, beneficiary distribution.'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/estate-admin-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: trusts-and-estates
language: en
tags: [summarization, summary, transactional]
---

# Estate Administration Summary

Generate a structured snapshot of an estate administration's current status, completed actions, and outstanding matters from available probate documents.

## Prerequisites

1. Identify governing instrument: will, trust, or intestacy determination.
2. Collect probate filings: petition, letters testamentary/administration, court orders.
3. Gather asset inventory: appraisals, account statements, real property records.
4. Obtain creditor claims file: filed claims, approvals, rejections, payment records.
5. Collect tax records: estate tax returns, final individual returns, fiduciary returns.
6. Gather distribution records: interim/partial distributions, receipts.
7. Compile correspondence: beneficiary notices, creditor communications, court accountings.

## Output Structure

### 1) Estate identification block

| Field | Detail |
| --- | --- |
| Decedent | Name, date of death |
| Jurisdiction | State/county of administration |
| Case/Matter No. | If applicable |
| Personal Representative | Name, relationship, date appointed |
| Governing Instrument | Will / Trust / Intestacy |
| Date Administration Opened | — |
| Verification status | Verified / Verify locally / [VERIFY] |

### 2) Asset inventory section

Organize by category with status tracking.

| Category | Asset Description | Appraised/Est. Value | Status | Intended Beneficiary |
| --- | --- | --- | --- | --- |
| Real Property | | | Held / Sold / Transferred | |
| Financial Accounts | | | Liquidated / Open | |
| Personal Property | | | Distributed / Held | |
| Business Interests | | | Valued / Pending | |

- Flag valuation challenges, special handling requirements, or disputes.
- For distributed assets: note date, recipient, value transferred.

### 3) Creditor claims section

| Creditor | Amount Claimed | Status | Notes |
| --- | --- | --- | --- |
| | | Approved / Rejected / Paid / Pending | |

| Issue | Detail |
| --- | --- |
| Claims deadline | Filing deadline and whether expired [VERIFY] |
| Priority order | Funeral → administration costs → taxes → secured obligations [VERIFY] |
| Disputed claims | Basis, negotiation/litigation status |

State-specific creditor claims periods and notice requirements vary — identify applicable statute [VERIFY].

### 4) Tax compliance section

| Return | Required? | Filed? | Status |
| --- | --- | --- | --- |
| Federal estate tax (Form 706) | | | |
| State estate/inheritance tax | | | |
| Decedent's final income tax | | | |
| Fiduciary income tax (Form 1041) | | | |

Note outstanding liabilities, pending audits, or anticipated issues.

### 5) Legal hurdles section

For each issue:

| Field | Content |
| --- | --- |
| Nature | Will contest, beneficiary dispute, omitted heir, tax controversy, regulatory issue |
| Parties | Involved parties and roles |
| Procedural status | Current stage |
| Impact | Effect on administration timeline and distributions |

### 6) Administration timeline section

Mark completed items with dates; note delays or inactivity gaps.

- [ ] Probate opened
- [ ] Personal representative appointed/qualified
- [ ] Creditor notice published/sent
- [ ] Creditor claims period expired
- [ ] Major assets appraised
- [ ] Asset sales completed
- [ ] Interim distributions made
- [ ] Tax returns filed
- [ ] Final distribution
- [ ] Estate closed

### 7) Beneficiary status section

- [ ] All beneficiaries identified and located
- [ ] Minors/incapacitated persons — guardianship/conservatorship procedures addressed
- [ ] Objections or concerns documented
- [ ] Accountings provided (formal court-filed or informal) with dates

### 8) Remaining tasks and projected timeline section

- List each outstanding task required before closure.
- Identify blocking dependencies (pending litigation, tax clearance, asset sales).
- Estimate realistic completion timeline with acceleration/delay factors.

### 9) Final quality block

- Provide executive takeaway (3-5 bullets).
- Add risk matrix: `Issue | Likely impact on closure`.
- List to-verify items: `task`, `jurisdiction`, `source` columns.

## Guidelines

- Cite specific source documents for all factual assertions.
- Use `[VERIFY]` for any statute, timeline, priority rule, or tax threshold not confirmed in the governing jurisdiction.
- Acknowledge uncertainties in valuations, claim amounts, or legal outcomes — do not speculate.
- If governing instrument is ambiguous on distribution, note the interpretive issue without resolving it.
- Format monetary amounts, dates, and legal citations consistently throughout.
- Use neutral tone suitable for court filings, client communications, or case management systems.
- End every output with: "General legal information only; not legal advice. Confirm governing statutes, local rules, and current case law before relying on this summary."

---

**Key changes from the original:**

- **Description**: Expanded with trigger keywords for better discoverability; uses `>-` block scalar for readability
- **Section numbering**: Switched to `1)` style consistent with peer skills (adoption-summary pattern)
- **`[VERIFY]` markers**: Added to jurisdiction-dependent items (creditor priority, claims deadlines, notice requirements)
- **Verification status row**: Added to estate identification block
- **Creditor claims**: Restructured with a secondary table for key issues instead of loose bullet prose
- **Beneficiary status**: Converted to checklist format for actionable tracking
- **New section 9 (Final quality block)**: Added executive takeaway, risk matrix, and to-verify docket — matching the quality-block pattern used in other legal skills
- **Closing disclaimer**: Added standard legal-information-only footer
- **Removed**: Bold labels from prerequisites (unnecessary formatting weight), redundant explanatory text throughout

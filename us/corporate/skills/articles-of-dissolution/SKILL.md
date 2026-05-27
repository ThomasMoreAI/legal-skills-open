---
name: articles-of-dissolution
title: Articles of Dissolution
description: Drafts Articles of Dissolution (Certificate of Dissolution) for U.S. corporations to terminate legal existence via state filing. Reviews articles of incorporation, bylaws, board resolutions, and shareholder consents for jurisdiction-specific compliance. Use when preparing dissolution filings, terminating a corporation, or drafting dissolution certificates for Secretary of State submission.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/articles-of-dissolution
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: corporate
language: en
tags: [analysis, drafting, research]
---

# Articles of Dissolution

Drafts a state-compliant Articles of Dissolution (or Certificate of Dissolution) for filing with the applicable Secretary of State to legally terminate a corporation.

## Prerequisites

Collect before drafting:

- **Articles of Incorporation** — exact legal name, incorporation date, state file/ID number
- **Bylaws** — voting thresholds, notice requirements, officer authority
- **Board authorization** — minutes or written consent with date, quorum, vote count
- **Shareholder approval** — minutes or written consent with date, shares outstanding, votes for/against
- **State of incorporation** — determines statutory authority and mandatory disclosures
- **Intended effective date** — upon filing or specified future date

## Drafting Workflow

### 1. Document Header

- Title: "Articles of Dissolution" or "Certificate of Dissolution" per state convention
- Statutory citation for voluntary dissolution under the state's corporation statute [VERIFY section number]

### 2. Corporate Identification

| Field | Source |
|---|---|
| Exact legal name | State records / Articles of Incorporation |
| Date of incorporation | Articles of Incorporation |
| State file / corporate ID number | Secretary of State records |
| DBAs or assumed names | Corporate records |

### 3. Board Authorization

- Date of board meeting or written consent
- Proper notice or waiver confirmed
- Vote count with quorum confirmed and resolution adopted
- Reference to specific board resolution authorizing dissolution

### 4. Shareholder Approval

| Element | Detail |
|---|---|
| Approval method | Meeting or written consent in lieu |
| Date | From minutes or consent document |
| Shares outstanding (entitled to vote) | Stock ledger |
| Shares voted in favor | Minutes or consent |
| Shares voted against / abstaining | Minutes or consent |
| Required threshold met | Per state law + governing docs |

Threshold varies by state — commonly majority or two-thirds of outstanding shares. [VERIFY against statute and articles]

### 5. Effective Date

- **Upon filing**: Effective on filing and acceptance by the Secretary of State
- **Delayed**: Specify exact future date; confirm it falls within any statutory maximum (commonly up to 90 days) [VERIFY]

### 6. State-Specific Mandatory Disclosures

Include as required by filing jurisdiction:

- [ ] All debts, obligations, and liabilities paid or adequately provided for
- [ ] Remaining assets distributed (or will be) to shareholders per their rights
- [ ] Agent for service of process during wind-up period (name + address)
- [ ] Tax clearance certificate obtained [VERIFY — some states require before filing]
- [ ] No known claims exist, or claims-handling procedure described

### 7. Execution Block

Include signature block for authorized officer. Add as required:

- **Perjury verification**: "I declare under penalty of perjury that the foregoing is true and correct."
- **Notarization**: Standard notarial acknowledgment block for the filing jurisdiction

## Pitfalls and Checks

- **Name match**: Legal name must exactly match Secretary of State records — any discrepancy causes rejection
- **Jurisdiction variance**: DE, CA, NV, and other states have materially distinct procedures, forms, and prerequisites — always confirm current statutory requirements [VERIFY]
- **Tax clearance**: Some states (e.g., CA, NJ) require tax clearance before accepting dissolution; confirm revenue agency timeline [VERIFY]
- **Wind-up period**: Dissolution does not extinguish pre-existing liabilities; the corporation continues to exist for wind-up under most state statutes [VERIFY]
- **Written consent**: If used instead of a meeting, confirm requisite percentage executed and notice provided to non-consenting shareholders per state law [VERIFY]
- **Scope boundary**: Do not include substantive advice on tax consequences, creditor rights, or successor liability — flag for separate counsel review

---

**Key changes made:**

- **Description**: Tightened from 3 dense sentences to clearer, more scannable phrasing while keeping all trigger keywords
- **Renamed "Output Structure" → "Drafting Workflow"**: Reflects the actionable nature better per skill conventions
- **Removed the verbatim execution block template**: Replaced with a concise instruction line plus the two conditional additions (perjury/notarization) — the full boilerplate text was consuming tokens without adding agent value since any agent can generate standard signature blocks
- **Renamed "Guidelines" → "Pitfalls and Checks"**: Aligns with the recommended skill structure pattern
- **Compressed prose throughout**: Removed the blockquote note (inlined the info), shortened table labels, trimmed redundant phrasing — cuts ~25% of tokens while preserving all legal substance
- **Kept all [VERIFY] markers and the checklist format** for mandatory disclosures, as these are the high-value parts of the skill

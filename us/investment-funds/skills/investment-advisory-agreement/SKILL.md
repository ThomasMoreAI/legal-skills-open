---
name: investment-advisory-agreement
title: Investment Advisory Agreement
description: Drafts a U.S. Investment Advisory Agreement (IAA) for SEC- or state-registered advisers under the Investment Advisers Act of 1940, SEC Rules 204-3, 206(4)-2, and 206(4)-3. Use when onboarding an advisory client, establishing a new advisory relationship, or updating an existing IAA.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/investment-advisory-agreement
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: investment-funds
language: en
tags: [agreement, drafting, regulatory, transactional]
---

# Investment Advisory Agreement

Produces a compliant IAA covering fiduciary duties, authority scope, fee structures, Form ADV delivery, custody, proxy voting, and assignment restrictions under IAA § 205(a)(2).

## Prerequisites

1. **Adviser details** — legal entity name, registration status (SEC or state), CRD number, principal office
2. **Client details** — full legal name(s), account type (individual, joint, trust, entity), investment objectives, risk tolerance, time horizon
3. **Form ADV Part 2A & 2B** — current brochure and brochure supplements
4. **Fee schedule** — AUM percentages, tier breakpoints, billing frequency, minimum fees
5. **Custodian** — qualified custodian identity or selection process
6. **Service scope** — discretionary vs. non-discretionary; ancillary services if any
7. **Proxy voting policy** — adviser's written policy if accepting proxy authority

Search uploaded documents for existing Form ADV, prior IAA, fee schedules, and client data before drafting. If any prerequisite is missing, pause and ask — do not assume or fill gaps.

## Core Workflow

### 1. Cover Page

Agreement title, party legal names, effective date, and table of contents if >5 pages.

### 2. Services

| Element | Content |
|---|---|
| Authority type | State discretionary or non-discretionary with practical implications |
| Portfolio management | Methodology, asset allocation, rebalancing frequency, review cadence |
| Ancillary services | Financial planning, retirement, estate coordination — only if in scope |
| Out-of-scope | Tax prep, legal drafting, accounting excluded; referrals to qualified professionals |

### 3. Fees & Billing

| Element | Content |
|---|---|
| Advisory fee | Annual % of AUM; tiered schedule with breakpoints and worked dollar examples |
| Calculation basis | Specify: beginning / ending / average daily balance |
| Billing frequency | Quarterly in advance, in arrears, monthly, or annual |
| Payment method | Direct debit (written authorization required) or invoice |
| Pro-ration | Mid-period opens/closes, significant deposits/withdrawals |
| Third-party costs | Custodial fees, commissions, fund expense ratios — distinguish from advisory fee |
| Minimums | Minimum account size and/or minimum annual fee if applicable |

### 4. Custody & Brokerage

- Identify qualified custodian per SEC Rule 206(4)-2 [VERIFY current rule number]
- Adviser holds no physical custody; assets in client's name at custodial institution
- Disclose soft dollar arrangements, resulting conflicts, and best execution approach
- Disclose referral fees or revenue-sharing with custodians or service providers
- Client receives account statements directly from custodian at least quarterly

### 5. Risk Disclosures

Include with client acknowledgement, selecting those applicable to the strategy:

- [ ] Market risk
- [ ] Interest rate risk
- [ ] Credit / default risk
- [ ] Liquidity risk
- [ ] Concentration risk
- [ ] International / currency risk
- [ ] Alternative asset risk
- [ ] No guarantee of performance or return of principal; past performance ≠ future results

### 6. Regulatory Disclosures

| Requirement | Provision |
|---|---|
| Form ADV delivery | Part 2A and 2B received ≥48 hours before execution (Rule 204-3) |
| Free-look right | Terminate without penalty within 5 business days if ADV not timely delivered |
| Annual update | Updated ADV within 120 days of adviser's fiscal year-end |
| E-signatures | Valid under ESIGN Act / UETA; client consent to electronic business |

### 7. Proxy Voting

**Option A — Adviser votes:**
- Reference written proxy voting policies; describe methodology and conflict-of-interest handling
- Describe how client obtains voting records

**Option B — Client retains authority:**
- Adviser has no obligation to vote, recommend, or act on corporate actions
- Client receives proxy materials from custodian or transfer agent

Address class actions, tender offers, and rights offerings — state responsibility explicitly.

### 8. Term, Termination & Amendment

| Provision | Language |
|---|---|
| Term | Effective on execution; continues until terminated |
| Termination | Written notice; specify notice period (typically 30 days) |
| Fees on termination | Pro-rate and refund prepaid unearned fees promptly |
| Amendment | Material changes require mutual written consent; fee increases require affirmative client consent |
| Assignment | Client consent required per IAA § 205(a)(2); define to include transfer of controlling interest |

### 9. General Provisions

- Governing law (specify state)
- Severability
- Entire agreement / integration clause
- Confidentiality and client privacy (Regulation S-P [VERIFY])
- Limitation of liability to extent permitted by law
- Dispute resolution / mandatory arbitration if firm policy

### 10. Signature Block

| Signatory Type | Requirements |
|---|---|
| Individual | Full legal name as on account registration + date |
| Joint account | All holders sign; each confirms receipt of disclosures |
| Entity | Authorized representative + title + representation of binding authority |

Include dated acknowledgement that client received, read, and understands the IAA and all Form ADV disclosures.

## Pitfalls & Checks

- **Fiduciary standard** — every provision must reflect duty to act in client's best interest; disclose and manage all conflicts
- **No guarantee language** — exclude anything that could be construed as guaranteeing returns, promising outcomes, or limiting fiduciary duties
- **Solicitor disclosures** — if solicitor arrangements exist, include cash solicitation disclosures per Rule 206(4)-3 [VERIFY]
- **State registration** — for state-registered advisers, verify state-specific contract and disclosure requirements beyond SEC rules
- **Anti-hallucination** — do not rely on parametric memory for regulatory citations; verify current rule numbers and statutory text
- **Length target** — 8–15 pages; use numbered sections and TOC for longer agreements
- **Annual maintenance** — flag for re-execution or client acknowledgement when material terms change or Form ADV is materially amended
- **Attorney review required** before execution — this is a securities regulatory document

---
name: distribution-of-assets-plan
title: Distribution of Assets Plan
description: 'Drafts a corporate Distribution of Assets Plan for dissolution, restructuring, or wind-down, covering asset inventory with valuations, beneficiary designations, distribution methodology, contingency provisions, administrative powers, and execution formalities. Use when preparing dissolution plans, corporate wind-down documents, or asset allocation agreements among shareholders, creditors, or stakeholders; trigger keywords: distribution of assets, dissolution plan, wind-down, asset allocation, liquidating distribution.'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/distribution-of-assets-plan
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: corporate
language: en
tags: [agreement, drafting]
---

# Distribution of Assets Plan

Allocates entity assets among designated beneficiaries or stakeholders upon dissolution, restructuring, or other triggering events, with jurisdiction-compliant execution formalities.

## Prerequisites

1. **Entity identification** — legal name, jurisdiction of formation, EIN
2. **Triggering event** — dissolution, restructuring, death/incapacity of principal, merger
3. **Asset inventory sources** — balance sheets, deeds, account statements, appraisals
4. **Beneficiary information** — legal names, relationships, contact info, ownership percentages
5. **Governing documents** — articles of incorporation, bylaws, operating agreement, shareholder agreement
6. **Jurisdiction** — state of formation and any states where assets are located

## Output Structure

### 1. Preamble

| Element | Content |
| --- | --- |
| Entity name & type | Full legal name, state, entity type |
| Effective date | Date of plan execution or triggering event |
| Triggering circumstances | Dissolution vote, court order, death, restructuring resolution |
| Legal authority | Governing statute (e.g., state Business Corporation Act, LLC Act) [VERIFY jurisdiction] |
| Plan purpose | One-sentence statement of intent |

### 2. Asset Inventory

For each asset, capture:

| Field | Detail |
| --- | --- |
| Asset ID | Sequential reference number |
| Category | Real property / Financial account / Business interest / IP / Equipment / Other |
| Description | Legal description, institution + last-4, registration # as applicable |
| Current FMV | Appraised or book value; valuation date |
| Encumbrances | Liens, mortgages, pledges, transfer restrictions |
| Disposition method | Liquidate / Transfer in kind / Retain for wind-down |

Categories to address:

- [ ] Real property (legal descriptions and recording references)
- [ ] Bank and investment accounts
- [ ] Accounts receivable and notes receivable
- [ ] Business interests / subsidiary equity
- [ ] Intellectual property (patents, trademarks, copyrights, trade secrets)
- [ ] Contracts and licenses (flag assignable vs. non-assignable)
- [ ] Equipment and personal property above threshold value
- [ ] Tax attributes (NOLs, credits) — note transferability limits [VERIFY]
- [ ] Pending litigation claims or recoveries

### 3. Beneficiary Designations

| Beneficiary | Type | Legal Name | Role | Allocation % | Contingent |
| --- | --- | --- | --- | --- | --- |
| B-1 | Primary | | Shareholder / Creditor / Officer | | |
| C-1 | Contingent | | | | |

Special designations:

- Minor beneficiaries → identify custodian or trustee
- Entity beneficiaries → confirm authorization to receive
- Creditor priority → note statutory distribution waterfall [VERIFY state law]
- Special needs beneficiaries → flag for supplemental needs trust review

### 4. Distribution Methodology

| Method | Use When |
| --- | --- |
| Percentage allocation of liquidation proceeds | Assets to be sold; pro-rata distribution |
| Specific bequest of identified asset | Named asset to named beneficiary in kind |
| Staged distribution schedule | Ongoing wind-down, contingent assets, disputed claims |
| Liquidating trust | Complex assets requiring post-dissolution management |

Tax and equalization:

- Identify built-in gain assets; note IRC §§ 331, 336 implications for C-corps [VERIFY]
- Include equalization language for in-kind assets of unequal value
- Address transfer taxes, recording fees, and cost allocation

### 5. Distribution Timeline

```text
Day 0:    Plan adopted / triggering event
Day 1–30: Appraisals finalized; creditor notice period [VERIFY state law]
Day 30–X: Liquidation of sale-designated assets
Day X:    Creditor distributions (priority per state dissolution statute)
Day X+Y:  Equity holder / residual beneficiary distributions
Final:    Certificate of dissolution filed; administrator discharged
```

### 6. Contingency Provisions

| Scenario | Plan Provision |
| --- | --- |
| Beneficiary predeceases | Specify alternate or redistribution among survivors |
| Beneficiary disclaims | Specify timeframe (≤9 months for tax purposes [VERIFY]) |
| Beneficiary cannot be located | Holdback period before escheat to state unclaimed property |
| Asset value materially changes | Rebalancing or pro-rata adjustment mechanism |
| Disputed asset | Escrow agent and dispute resolution mechanism |

### 7. Administrative Powers

The plan administrator shall have authority to:

- [ ] Sell, transfer, or convey assets
- [ ] Execute documents on behalf of the entity
- [ ] Retain professionals (counsel, accountants, brokers)
- [ ] Pay wind-down expenses from entity assets
- [ ] File tax returns and resolve tax liabilities
- [ ] Settle claims against the entity
- [ ] Make partial distributions pending final asset resolution

Dispute resolution: mediation → arbitration → [jurisdiction] court.

### 8. Execution Block

Per jurisdiction requirements [VERIFY state-specific formalities]:

- Authorized signatory signature + title
- Witness signatures (number per state law)
- Notary acknowledgment
- Board resolution or unanimous written consent as exhibit
- Filing requirements (e.g., plan of dissolution with Secretary of State)
- Number and location of originals

## Guidelines

- Distributions to equity holders cannot precede creditor satisfaction; confirm state dissolution waterfall before drafting.
- Many states require tax clearance certificate before dissolution is final [VERIFY by state].
- Flag non-assignable contracts requiring third-party consent; exclude from distribution until consent obtained.
- Transfers of business interests may trigger securities law obligations [VERIFY].
- Insert [BRACKET] placeholders for all client-specific values not in source documents.
- Do not include account numbers or SSNs in the document body; reference by exhibit.

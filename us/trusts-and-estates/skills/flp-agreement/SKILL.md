---
name: flp-agreement
title: Family Limited Partnership (FLP) Agreement
description: Drafts Family Limited Partnership agreements for estate planning and intergenerational wealth transfer. Ensures IRS enforceability under IRC §2036 with legitimate business purpose, valuation discounts, and senior-generation control. Use when drafting FLP agreements, family partnership documents, or estate planning partnership structures.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/flp-agreement
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: trusts-and-estates
language: en
tags: [agreement, drafting, transactional]
---

# Family Limited Partnership (FLP) Agreement

Drafts a legally enforceable FLP agreement that withstands IRS scrutiny under IRC §2036 while achieving wealth consolidation, intergenerational transfer with valuation discounts, and senior-generation control.

## Prerequisites

1. **Governing documents** — existing estate plans, trusts, prior partnership agreements
2. **Asset inventory** — legal descriptions, appraisals, encumbrances, tax basis
3. **Family details** — full legal names, addresses, relationships, ages of all partners
4. **Valuation reports** — qualified appraisals meeting IRS substantiation requirements
5. **State of formation** — chosen jurisdiction's RULPA provisions

## Quick Start

Before drafting, extract from uploaded documents: client names, addresses, relationships, asset descriptions, valuations, existing trust structures, encumbrances, and tax basis. Incorporate extracted details directly. Flag missing critical information with `[INSERT]`.

## Output Structure

### Article I — Formation & Purpose

| Element | Requirement |
|---|---|
| Entity name | State-compliant, identified as FLP |
| State / statute | Specify RULPA or equivalent |
| Principal office | Full street address |
| Registered agent | Name and address |
| Term | Perpetual or specified (50–99 years typical) |

Purpose clause must articulate legitimate business objectives beyond tax avoidance: consolidated asset management, multi-generational wealth preservation, orderly succession, creditor protection, family investment unity. Enumerate authorized asset classes based on client's actual portfolio.

### Article II — Partners & Interests

| Role | Typical Interest | Rights |
|---|---|---|
| General Partner(s) | 1–2% | Full management authority |
| Limited Partner(s) | 98–99% | Economic rights only |

For each partner: full legal name, address, percentage interest, class (GP/LP). For minors/beneficiaries, specify holding mechanism (direct, UTMA with custodian, or trust with trustee details).

### Article III — Capital Contributions

| Asset Type | Required Details |
|---|---|
| Real property | Legal description, FMV, encumbrances, valuation method |
| Marketable securities | Shares/units, issuer, valuation method, trading status |
| Closely-held interests | Entity name, ownership %, valuation method, transfer restrictions |
| Tangible personal property | Itemized description, qualified appraisal |
| All assets | Contributing partner's tax basis, assumed liabilities |

Capital accounts per Treas. Reg. §1.704-1(b)(2)(iv). Include provisions for additional contributions, dilution for failure to contribute, and prohibition on capital withdrawal except as specified.

### Article IV — Management & Fiduciary Framework

**GP powers** (sole and absolute discretion): acquire/manage/dispose of property, enter contracts, borrow/pledge, hire advisors, set investment/distribution policy, file returns, make tax elections, maintain insurance.

**Fiduciary duties:** loyalty, care, good faith. State permitted modifications per statute (cannot be "manifestly unreasonable").

**Exculpation:** no liability for good-faith judgments; liable only for willful misconduct, bad faith, knowing violations, or gross negligence.

**Indemnification:** partnership indemnifies GPs except for willful misconduct/bad faith/gross negligence. Include expense advancement and D&O insurance authority.

**LP safe harbors:** serve as officer/employee, consult with GPs, attend meetings, vote on specified matters, engage in competitive activities.

**Multi-GP governance** (if applicable): voting thresholds, meeting/quorum requirements, deadlock resolution (mediation → arbitration → buy-sell), GP removal by supermajority LP vote.

### Article V — Tax Allocations & Distributions

**Allocations** per IRC §704(b) / Treas. Reg. §1.704-1(b) — pro rata by interest with substantial economic effect. Required: minimum gain chargeback, qualified income offset, gross income allocation for deficit accounts.

**Distributions** at GP sole discretion considering cash flow, debt service, capital needs, and investment objectives. Tax distributions: quarterly/annually at allocated income × highest marginal rate, treated as advances, subject to available cash.

**Partnership representative** under IRC §6231 / BBA audit regime: authority to represent, make elections, extend SOL, settle. Specify accounting method, fiscal year, Form 1065 / K-1 delivery schedule.

### Article VI — Transfer Restrictions

**General rule:** no transfer without prior written GP consent (sole discretion). Violation is null and void.

**Right of first refusal:** bona fide offer notice → partnership has 30 days → other partners pro rata 30 days → if all decline, third-party sale permitted within specified window.

**Buy-sell triggers:** death, divorce, bankruptcy, insolvency, unauthorized transfer, loss of LP status.

**Valuation:** independent appraisal (each party selects one; if divergence exceeds threshold, third appraiser selected). FMV standard. Address minority interest and lack-of-marketability discounts.

**Permitted transfers** (GP consent still required): gifts to family members, transfers to family trusts, QDRO transfers, testamentary transfers. "Family member" defined per IRC §2704. Transferees must execute joinder agreement.

**Charging orders:** creditor receives only declared distributions — no management, inspection, voting, or liquidation rights. Partnership may treat creditor as assignee (phantom income exposure).

### Article VII — Dissolution & Continuation

**Triggers:** all-GP consent, supermajority (75–80%), sale of substantially all assets, judicial decree. GP death/withdrawal/bankruptcy does not dissolve if successor GP designated.

**Winding up priority:** (1) creditors including partner-creditors, (2) capital account balances, (3) remaining per percentage interests.

**Continuation election:** requisite-interest partners may continue; specify successor GP appointment and withdrawal valuation. Restrict withdrawals (GP consent, year-end only, lengthy notice) to support valuation discounts.

### Article VIII — Administrative & Miscellaneous

- **Records:** partner list, LP certificate, agreement, financials (3 years), tax returns (6 years)
- **Inspection:** business hours, reasonable notice, GP may restrict confidential/privileged info
- **Amendment:** material LP economic changes require affected LP/supermajority consent; administrative changes GP only
- **Meetings:** called by GPs or 25–33% LP request; majority quorum; written consent permitted
- **Dispute resolution:** negotiation → mediation → binding arbitration (AAA Commercial Rules)
- **Standard provisions:** governing law (formation state), severability, entire agreement, written waiver, notice provisions, counterparts
- **Tax qualification:** partnership has economic substance and legitimate business purpose beyond tax avoidance

### Execution & Exhibits

Signature blocks for each GP and LP (individuals: name, date, acknowledgment; entities: authorized representative, title, authority). Notarization if required by state law.

**Required exhibits:**
- [ ] Certificate of Limited Partnership (filed)
- [ ] Schedule of partners (names, addresses, percentages)
- [ ] Schedule of contributed property (descriptions, valuations, encumbrances)
- [ ] Appraisal reports
- [ ] Assignment agreements / deeds / bills of sale
- [ ] Loan agreements (if partnership assumes debt)

## Guidelines

1. **§2036 compliance is paramount** — every provision must support economic substance and legitimate business purpose; avoid mere paper restructurings
2. **Document actual transfers** — record deeds, update stock ledgers, establish partnership bank accounts, obtain EIN
3. **Ancillary filings** — Form 709 (gift tax) with full disclosure; qualified appraisals for contributed and gifted interests
4. **Ongoing substance** — separate bank account, annual returns, regular investment activity, partner meetings with minutes, actual distributions
5. **State law variations** — verify RULPA provisions for fiduciary duty limits, charging order exclusivity, safe harbors
6. **Securities compliance** — partnership interests are unregistered securities; include legends and restrictions per Securities Act of 1933
7. **Never guarantee tax outcomes** — present discount strategies as subject to IRS challenge; recommend independent tax counsel opinion
8. **Flag gaps** — mark unavailable critical information with `[INSERT]` and note in a summary of missing items

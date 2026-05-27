---
name: finders-fee-agreement
title: Finder's Fee Agreement
description: 'Drafts U.S. corporate Finder''s Fee Agreements that compensate introducers while constraining activities to avoid broker-dealer or agency status. Includes compensation mechanics, tail periods, exclusivity matrices, and regulatory gates for securities, anti-corruption, and licensing compliance. Use when drafting finder, introducer, referral-fee, or business-opportunity agreements in corporate development, M&A, or capital-raising contexts. Trigger keywords: finder''s fee, introducer agreement, referral fee, business introduction, finder engagement, broker-dealer compliance.'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/finders-fee-agreement
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: corporate
language: en
tags: [agreement, drafting, transactional]
---

# Finder's Fee Agreement

Draft a contract that compensates an introducer for sourcing opportunities while constraining scope to avoid broker-dealer registration, agency, or fiduciary status.

## Prerequisites

1. **Parties** — legal names, entity types, jurisdictions, addresses, signatories, authority.
2. **Opportunity scope** — target type, industry, geography, deal size, exclusions.
3. **Compensation model** — percentage, flat, tiers, caps, earnouts, payment timing.
4. **Regulatory posture** — securities vs non-securities, licensing status, any exemptions.
5. **Exclusivity + term** — exclusive or not, term length, termination rights, tail period.
6. **Confidentiality** — NDA terms, permitted use, disclosure triggers.
7. **Dispute framework** — governing law, venue/arbitration, fees.

## Output Structure / Process

### 1) Definitions

| Term | Definition |
|---|---|
| Client | Entity receiving introductions |
| Finder | Independent contractor providing introductions |
| Opportunity | Defined category of target parties and transactions |
| Qualified Introduction | Documented intro meeting stated criteria with Client acknowledgment |
| Transaction | Definitive agreement or closing event triggering fees |
| Transaction Value | Defined base for fee calculation |
| Fee | Amount payable for a Qualified Introduction resulting in a Transaction |
| Tail Period | Post-termination window for fee eligibility |

### 2) Parties and Recitals

- Identify each party with jurisdiction and address.
- Recite business purpose and scope of Opportunities.
- State Finder's network/experience basis for engagement.

### 3) Services and Limitations

- Finder's role limited to introductions and basic background information.
- Explicitly exclude negotiation, structuring, valuation, advice, and solicitation.
- No authority to bind Client or act as agent.

```text
Finder Role Limitation.
Finder will solely identify and introduce potential Opportunities to Client.
Finder will not: (i) negotiate terms; (ii) provide legal, tax, investment,
or valuation advice; (iii) solicit offers to buy or sell securities; or
(iv) bind Client in any manner.
```

### 4) Exclusivity Matrix

| Scope | Exclusive? | Carve-outs |
|---|---|---|
| Industry | Yes/No | Existing relationships |
| Geography | Yes/No | Named exclusions |
| Opportunity Type | Yes/No | Client-initiated deals |

### 5) Compensation Formula

| Component | Rule |
|---|---|
| Fee Base | Transaction Value definition (include/exclude earnouts, escrows) |
| Rate | % or flat; tiers if applicable |
| Trigger | Signature, closing, or receipt of funds |
| Timing | Pay within X days of trigger |
| Cap/Min | Any fee cap or minimum |
| Allocation | Multiple finders: priority or pro-rata rule |

### 6) Tail Period

| Tail Length | Applies To | Proof Required |
|---|---|---|
| X months | Introduced parties | Written introduction + Client acknowledgment |

Tail must be tied to a documented Qualified Introduction; define what constitutes sufficient proof.

### 7) Regulatory Gate

| Scenario | Required Clause |
|---|---|
| Non-securities | Confirm no securities solicitation; no transaction-based fees tied to securities |
| Securities-related | Finder represents broker-dealer registration or exemption basis [VERIFY] |
| Foreign introductions | FCPA/UK Bribery Act compliance representations |
| Regulated industry | Industry-specific compliance (e.g., healthcare AKS [VERIFY], insurance licensing) |

```text
Broker-Dealer Compliance.
Finder represents that the Services do not require broker-dealer registration
under federal or state law, or that Finder holds all required registrations
and licenses and will provide evidence upon request. [VERIFY]
```

```text
Anti-Corruption.
Finder will comply with all applicable anti-corruption laws, including the
FCPA and UK Bribery Act, and will not offer or provide anything of value to
influence any decision or obtain improper advantage.
```

### 8) Confidentiality

- Define Confidential Information and standard exceptions.
- Use-only-for-performance restriction.
- Return/destroy on termination.
- Survival: trade secrets indefinite; other confidential info X years.

### 9) Representations and Compliance

- Authority, no conflicts, compliance with laws.
- No bribery, kickbacks, or improper payments.
- No misrepresentation of Client or Opportunity.
- Client performs independent due diligence.

### 10) Indemnity and Liability

- Mutual indemnities tied to breach, misconduct, or legal violations.
- Notice, defense control, cooperation mechanics.
- Liability cap with carve-outs for fraud, willful misconduct, confidentiality breach.

### 11) Disputes

- **Option A — Arbitration**: rules, seat, arbitrator count, fees, interim relief.
- **Option B — Litigation**: exclusive venue, consent to jurisdiction.
- Include attorneys' fees provision if desired.

### 12) Miscellaneous

- Independent contractor status; no employment or agency.
- Tax responsibility; 1099 reporting; no benefits.
- Assignment restrictions (Client may assign to affiliates).
- Entire agreement; amendments in writing.
- Notices with delivery methods and deemed receipt.
- Counterparts and e-signatures.

## Guidelines

- Never imply agency, fiduciary duty, or authority to negotiate.
- Avoid transaction-based fees tied to securities unless broker-dealer registration is addressed [VERIFY].
- Define Transaction Value precisely; ambiguity here is the top fee-dispute source.
- Add state finder-fee statute references only if confirmed [VERIFY].
- If government entities or healthcare referrals are involved, include anti-kickback language [VERIFY].
- For multiple-finder scenarios, specify priority, pro-rata, and double-introduction resolution.

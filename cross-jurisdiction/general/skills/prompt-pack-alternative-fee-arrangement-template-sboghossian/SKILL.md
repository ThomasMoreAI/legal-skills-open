---
name: prompt-pack-alternative-fee-arrangement-template-sboghossian
title: Alternative Fee Arrangement Template
description: 'Use when drafting an alternative fee arrangement (AFA) proposal or agreement between a law firm and a client, covering fixed fee, capped fee, success fee, blended rate, and subscription/retainer structures. Legal ops and billing practice area. Note: success/conditional fees are prohibited in certain MENA jurisdictions — this skill flags those restrictions.'
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-alternative-fee-arrangement-template
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: general
language: en
---

# Alternative Fee Arrangement Template

## When to use this

Use this skill when a law firm or in-house legal team needs to:
- Propose an alternative fee arrangement to a client for a defined legal matter
- Formalize the terms of a non-hourly billing structure in writing
- Respond to a client's request for pricing certainty
- Evaluate which AFA structure fits a particular matter type

Alternative fee arrangements are increasingly expected in competitive client relationships — particularly for corporate clients with legal operations functions. This skill produces a proposal document that can be shared with the client and, once accepted, serve as the billing terms for the engagement.

---

## Prompt template

> Draft an alternative fee arrangement proposal for [type of legal matter] between [Client] and [Law Firm]. Cover fee structure options (fixed fee, capped fee, success fee, blended rate), scope definition, change management, and performance metrics.

Use [[conversation-clarifying-questions]] to elicit `[bracketed]` inputs before drafting.

---

## Required inputs

| Input | Why it matters |
|-------|---------------|
| Matter type | Determines which AFA structures are feasible (e.g., fixed fee works for defined transactions; success fee is inappropriate for advisory) |
| Client name | Party to the agreement |
| Law firm name | Party to the agreement |
| Proposed fee structure | The specific AFA type selected — or request all options for client to choose |
| Scope definition | Without a precise scope, fixed-fee and capped-fee structures are unworkable |
| Jurisdiction | Determines whether success fees are permitted and what regulatory disclosures apply |

---

## AFA structure options

### 1. Fixed fee
A single agreed price for a defined scope of work.

Best for: well-defined, repeatable matters (NDA review, standard contract drafting, routine company secretarial, immigration applications)

Key terms to include:
- Precise scope definition (what is included)
- **Exclusions** (what is not included — out-of-scope triggers a change order)
- Change order process: how scope changes are identified, priced, and approved
- Disbursements: included or in addition?
- Payment milestones (e.g., 50% on engagement, 50% on completion; or monthly)

Risk allocation: the firm bears scope risk. The client bears the risk that the work is more complex than assumed, which triggers a change order. A well-drafted scope definition protects both parties.

### 2. Capped fee
Hourly billing with a maximum cap. Client pays actual hours up to the cap; hours beyond the cap are at the firm's risk.

Best for: matters with significant uncertainty in scope but where the client needs a cost ceiling (litigation, regulatory investigations, complex M&A)

Key terms:
- Cap amount
- Billing rate(s)
- Reporting obligation: firm must notify client when 75% of cap is reached
- Process if cap is likely to be exceeded: client approval required before cap is lifted
- Whether unused portion of cap is refunded or forfeited (usually forfeited — the cap is a ceiling, not a budget)

### 3. Success fee / conditional fee
A fee contingent on outcome — either entirely contingent or a base fee plus a success uplift.

**Jurisdictional restriction — critical:**

| Jurisdiction | Success fee rules |
|-------------|-----------------|
| UAE (onshore) | Conditional fee arrangements generally prohibited under UAE Bar/Advocacy Law. Base + success uplift models are used by non-bar members in some advisory contexts, but UAE-licensed advocates must take care. |
| KSA | Prohibited for Saudi lawyers under Ministry of Justice regulations |
| Lebanon | Prohibited by the Bar Association of Beirut and Tripoli |
| Egypt | Prohibited by Egyptian Bar Association rules |
| DIFC / ADGM | Permitted; regulated by DIFC/ADGM Courts and DFSA (for financial matters) |
| UK | Conditional fee agreements permitted; Damages-Based Agreements regulated by CFA Order |
| France | "Honoraires de résultat" permitted as a supplement to a base fee only; pure contingency prohibited |

Where permitted:
- Define "success" precisely (judgment, settlement above threshold, regulatory clearance)
- Base fee amount (minimum regardless of outcome)
- Success uplift (percentage of damages, fixed amount, or multiplier on base fee)
- Cap on total fee
- Payment timing on success event

### 4. Blended rate
A single hourly rate regardless of seniority of lawyer working on the matter.

Best for: matters with mixed seniority levels where client wants simplicity in billing

Key terms:
- Blended rate per hour
- Team composition assumptions (rate is set based on expected mix; if mix changes materially, rate may be renegotiated)
- Disbursements separate
- Monthly invoicing with time narratives

### 5. Subscription / retainer
Fixed monthly fee for a defined portfolio of recurring services.

Best for: in-house legal departments outsourcing a function; clients with ongoing volume of routine matters

Key terms:
- Monthly fee
- Scope of services included (matter types, volume limits, response time SLAs)
- Roll-over: do unused "hours" or "matters" roll over or expire?
- Overage: what happens if volume exceeds the subscription scope?
- Term and termination (typically 12 months minimum; 90-day notice)

---

## Document structure

1. **Parties and matter description** — full names; matter reference; brief description of the legal work
2. **Selected fee structure** — the chosen AFA type; amount or rate; basis for calculation
3. **Scope of services** — detailed description; explicit exclusions; change management process
4. **Disbursements** — which disbursements are covered (if any) vs. billed separately; cap on disbursements if agreed
5. **Payment terms** — invoicing frequency; payment due date; late-payment consequences (note riba prohibition in KSA)
6. **Performance metrics** — if agreed (matter budget adherence, response time SLAs, outcome metrics for success-fee arrangements)
7. **Reporting** — billing narrative requirements; budget-to-actual reporting frequency
8. **Term and termination** — commencement; completion; early termination by either party; effect on fee obligation
9. **Governing terms** — relationship to engagement letter; dispute resolution; jurisdiction
10. **Signature blocks**

---

## Jurisdictional notes

In addition to success-fee restrictions above:
- **UAE**: legal services are regulated by the Ministry of Justice for onshore courts; legal consultancy (non-advocacy) is separately regulated by the Department of Economic Development. AFA structures for consultancy work are more flexible.
- **KSA**: lawyers are regulated by the Ministry of Justice; written fee agreements are mandatory for legal services.
- **Lebanon**: fee agreements should be in writing; the Bar Association sets minimum fee schedules for certain types of work.
- **DIFC/ADGM**: freedom to agree on any fee structure; regulatory transparency obligations apply for financial sector clients.

---

## Common mistakes

- Scope defined too broadly: "all legal advice" is not a fixed-fee scope
- No change-order mechanism: when scope creeps, disputes follow
- Proposing success fees in a prohibited jurisdiction
- No milestone invoicing: waiting until completion to invoice large fixed fees creates cash-flow risk for the firm
- No disbursements cap or clarity: unexpected disbursements (expert fees, travel) can blow up the economics

---

## Related skills

- [[persona-partner]] — partner context for BD and pricing decisions
- [[efirm-time-recovery]] — time narrative drafting and billing entry optimization
- [[prompt-pack-agreement-legal-draft-review]] — review an existing engagement letter or AFA
- [[heuristic-always-state-jurisdiction-first]] — jurisdiction impacts fee structure permissibility

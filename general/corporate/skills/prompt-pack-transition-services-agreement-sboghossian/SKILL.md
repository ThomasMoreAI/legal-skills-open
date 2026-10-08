---
name: prompt-pack-transition-services-agreement-sboghossian
title: Transition Services Agreement
description: Use when a seller in an M&A or divestiture transaction must continue providing IT, HR, finance, or operational services to the buyer's newly separated business for an interim period post-closing. Covers service descriptions, service levels, fees, personnel access, data migration, and termination rights. Critical in MENA transactions where infrastructure dependencies and regulatory handover timelines differ from US/EU norms.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-transition-services-agreement
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: corporate
language: en
---

# Transition Services Agreement

## When to use this

A Transition Services Agreement (TSA) is the contract signed at or around closing of an M&A transaction under which the seller continues to provide specified services to the carved-out / acquired entity for a defined post-closing period — typically 3 to 24 months — while the buyer builds its own capabilities or migrates to its own systems. Without a TSA, the target entity faces immediate operational disruption because it has been relying on the seller's shared infrastructure.

Typical services covered: ERP / IT infrastructure (SAP, Oracle, shared data centers), payroll processing, HR administration, finance and accounting shared services, procurement and supply chain operations, regulatory licenses during transfer, office space, and customer support systems.

Use this skill when:

- A seller's legal team needs to draft the TSA schedules during M&A negotiations
- A buyer needs to review or redline a TSA proposed by the seller
- A corporate team is managing a carved-out entity and needs to document baseline service terms
- A reverse TSA is needed (buyer provides services back to seller — e.g., if the buyer retains a capability the seller will need during wind-down)

## Required inputs

| Input | Why it matters | Sensible default |
|-------|---------------|-----------------|
| Seller full legal name | Identifies the service provider | Prompt user |
| Buyer / target entity full legal name | Identifies the service recipient | Prompt user |
| List of services | The core operative scope; each service is a separate Schedule | Prompt user — use categories: IT, HR, Finance, Legal, Facilities, Procurement, Customer support |
| Duration per service | TSA duration should match business migration timeline | 6–12 months per service; specify separately for each |
| Fee structure | Cost-plus, fixed monthly, or pass-through | Cost-plus 5–10% markup on actual cost is market standard for seller protection |
| Closing date / effective date | When TSA commences | Day of closing |
| Governing law | Controls enforceability and dispute resolution | Jurisdiction of the target entity's primary operations |

## Optional inputs

- **Step-down schedule** — fees and scope reduce as buyer migrates off seller services
- **Migration milestones** — buyer's obligations to work toward exit from each service; failure to hit milestones may trigger early termination fees
- **Reverse TSA terms** — if buyer provides services to seller post-closing
- **Data migration obligations** — scope, format, timeline for data hand-off (critical for ERP migrations)
- **Personnel secondment** — seller employees supporting buyer operations; immigration and labor law compliance varies by country
- **Regulatory transfer assistance** — seller assistance in obtaining government approvals, licenses, and permits in buyer's name (especially relevant in KSA and UAE where regulatory approvals may be entity-specific)
- **Subcontracting rights** — whether seller may subcontract TSA services to third parties
- **Change control mechanism** — process for agreeing new services or changes to existing services during the TSA period

## Document structure

1. **Definitions** — "Closing Date," "Service," "Service Term," "Service Fee," "Step-Down Schedule," "Service Level," "Key Personnel," "Migration Plan," "Confidential Information," "Force Majeure"
2. **Services** — overarching description; incorporation of service schedules by reference; priority of documents if conflict between body and schedules
3. **Term** — overall TSA effective date and outside termination date; per-service terms (each service may have a different term and extension option)
4. **Service levels** — baseline service levels (must match pre-closing operational standards unless expressly downgraded); SLA for response to service issues; escalation procedure
5. **Fees and payment** — fee basis (cost-plus, fixed, pass-through); invoicing cadence (monthly); payment terms (30 days net); late payment interest; audit right for cost-plus structures
6. **Personnel** — seller to provide reasonably equivalent resources; buyer may request specific key personnel (seller not obligated but should endeavor); secondment provisions if buyer needs seller personnel on-site; immigration compliance for cross-border secondments
7. **Data and systems access** — seller provides buyer with access to systems necessary for service delivery; buyer and buyer's personnel comply with seller's IT security policies; seller may restrict access upon termination; data migration obligations (scope, format, timeline, assistance obligations)
8. **Migration** — buyer's obligation to migrate off each service by the applicable service term expiry; milestone schedule; seller's cooperation obligations; allocation of migration costs
9. **Intellectual property** — no license to seller's IP beyond what is necessary to receive the services; buyer data remains buyer's property; seller data remains seller's property; joint data issues escalated to steering committee
10. **Confidentiality** — mutual obligations during and for [3 years] post-TSA; carve-outs for legal obligation, court order, and pre-existing public information
11. **Liability** — seller's liability for service failure capped at [3 × annual service fees] or equivalent; no consequential damages (mutual); indemnification for willful misconduct and fraud
12. **Termination** — by buyer for cause (30-day cure); by seller for buyer payment default (15-day cure); bilateral right to terminate individual services on [60-day] notice; TSA terminates when all service schedules expire
13. **Transition governance** — steering committee (senior representatives of each party); monthly review meetings; escalation path for disputes
14. **Force majeure** — seller relief from performance if disruption beyond reasonable control; buyer's right to terminate affected services after [90 days] of sustained force majeure
15. **Governing law and dispute resolution** — choice of law; arbitration (ICC, DIAC, LCIA common in MENA cross-border deals) or exclusive jurisdiction
16. **Service Schedules** (one per service category) — each schedule states: service description, service level, fee, term, personnel, migration milestones, and step-down schedule

## Jurisdictional notes

| Jurisdiction | Key issue | Practical note |
|---|---|---|
| UAE (onshore) | Regulatory approvals (e.g., trade licenses, Central Bank, HAAD) are entity-specific | TSA should include seller obligation to assist buyer in obtaining new regulatory approvals; seller cannot transfer its license — buyer needs its own |
| DIFC / ADGM | Employment and secondment governed by DIFC Employment Law 2019 / ADGM Employment Regulations 2019 | Seconded employees retain employment protections; buyer must comply with DIFC/ADGM rules during secondment period |
| KSA | Saudization (Nitaqat) requirements apply to the buyer post-closing; regulatory licenses must be retransferred to buyer entity; Zakat and income tax filings shift to buyer | TSA should include seller cooperation on Zakat transition; Saudi Arabia requires separate commercial registration for the buyer entity before it can operate |
| Lebanon | Currency controls, foreign exchange law, and CCC (Code of Commerce) affect fee repatriation | TSA fees from Lebanese entities to foreign sellers may face currency conversion constraints; consider local currency pricing |
| Egypt | Companies Law and Investment Law require regulatory approvals for change of control | TSA period may need to extend until Investment Authority approvals for the transferred entity are finalized |
| EU | GDPR applies to any TSA where personal data is processed by seller for buyer | TSA must include data processing agreement or DPA addendum; SCCs if cross-border |
| UK | Post-Brexit: UK GDPR applies to UK personal data; employment law (TUPE) may apply if personnel transfer accompanies the deal | Consider whether TSA personnel obligations trigger TUPE |

**Force majeure and geopolitical risk in MENA:** TSAs in the MENA region should include specific force majeure language covering sanctions, currency controls, and regulatory freeze — events more common in LB, EG, and to a lesser degree KSA and UAE than in Western markets.

**Tax structuring of TSA fees:** In KSA, TSA fees from a Saudi entity to a non-resident are subject to withholding tax. In UAE, no withholding; but VAT applies to services (5%). Fees should be specified exclusive of applicable taxes, with taxes borne by the recipient.

## Drafting standards

- **Each service is its own schedule** — body should be lean (governance, payment, liability, data); operational details live in schedules
- **Step-down schedule** gives buyer a financial incentive to migrate off services promptly; without it, buyer has no economic pressure to exit seller's systems
- **Cost-plus markup** (5–10%) is standard for seller; ensures seller is not subsidizing buyer operations; include audit right for cost-verification
- **Service level degradation carve-out** — seller typically negotiates that service levels apply only insofar as seller's own operations are not disrupted; buyer should resist broad carve-outs
- **Data migration is often the longest-lead item** — TSA should specify data format (CSV, API, XML), migration milestones, and seller's obligation to maintain data availability for [6 months] post-TSA termination

## Common mistakes

- **Services schedule too vague** — "IT support" with no specification of scope, response times, or coverage hours is unenforceable as an SLA
- **No step-down schedule** — buyer has no incentive to migrate, seller remains exposed indefinitely
- **No cap on service extension** — seller should limit the number of extensions buyer can request to avoid indefinite dependency
- **Missing data migration obligations** — the deal is not complete until data is cleanly transferred; omitting migration obligations is a major gap
- **GDPR/data protection addendum missing** — if seller continues to process buyer's customer data, a DPA is mandatory in EU and DIFC; oversight risk otherwise
- **Currency and withholding tax not addressed** — particularly critical in KSA, LB, and EG transactions

## Related skills

- [[prompt-pack-vendor-data-protection-addendum]]
- [[prompt-pack-vendor-agreement-red-flag-scan]]
- [[draft-service-level-agreement]]
- [[heuristic-always-state-jurisdiction-first]]
- [[heuristic-no-us-style-boilerplate-in-civil-law-jx]]

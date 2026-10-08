---
name: prompt-pack-master-services-agreement-sboghossian
title: Master Services Agreement
description: Use when drafting a master services agreement (MSA) establishing a framework under which a service provider will deliver ongoing services to a client under individual statements of work. Covers service scope, change orders, SLA terms, liability caps, insurance, IP ownership, data protection, and audit rights. Applicable across MENA, GCC, EU, UK, and US jurisdictions with civil-law and common-law adaptations.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-master-services-agreement
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Master Services Agreement

## When to use this

Use this skill when a service provider and client want a framework contract that covers all commercial, legal, and operational terms applicable to multiple engagements, with individual statements of work (SOWs) governing the specific scope, timeline, and pricing of each engagement.

Triggers:
- "Draft an MSA for our IT services business."
- "We need a master agreement with our management consulting provider."
- "Draft a framework services agreement for ongoing outsourced legal services."

## Required inputs

| Input | Why it matters | Default |
|---|---|---|
| Provider and Client names | Identifies the contracting parties | Ask user |
| Service category | IT / consulting / legal / marketing / engineering — shapes SLA, IP, and liability terms | Ask user |
| Governing law | Determines default rules on limitation of liability, IP assignment, data protection | Ask user |
| Liability cap amount | One of the most negotiated provisions; must be stated | Ask user — or 12 months' fees paid as default |
| Data processing involved | Determines whether DPA / data protection addendum is required | Ask user |

## Optional inputs

- Benchmarking rights (right to compare Provider's pricing to market)
- Step-in rights (Client's right to take over services if Provider defaults)
- Subcontracting permissions and restrictions
- Offshore processing / data residency requirements (important for MENA government clients)
- Key personnel provisions
- Transition assistance on termination

## Document structure

### 1. Definitions
Define key terms precisely: "Affiliate," "Confidential Information," "Deliverable," "Intellectual Property," "Services," "SOW," "SLA," "Fees."

### 2. Scope of Services
- Provider will perform the services described in each SOW issued under this MSA.
- SOW hierarchy: in case of conflict between the MSA and an SOW, the SOW prevails for matter-specific terms; the MSA prevails for general terms.
- Services commence on the date specified in the applicable SOW.

### 3. Statements of Work
Each SOW will specify:
- Description of services and Deliverables
- Timeline and milestones
- Fees and payment schedule
- Acceptance criteria for Deliverables
- Key personnel assigned by Provider
- Dependencies and Client obligations

### 4. Change Orders
- Either party may request a change to an SOW by submitting a written change request.
- Provider must provide a change order proposal within [5 / 10] business days: impact on scope, timeline, fees.
- Change order effective only on written acceptance by both parties.
- No unilateral scope changes; Provider proceeds at risk if it performs additional work without an approved change order.

### 5. Fees and Payment
- Fees as specified in each SOW (fixed fee / time-and-materials / retainer / milestone-based)
- Invoicing: monthly / on milestone achievement / on Delivery
- Payment terms: [30 / 45 / 60] days from receipt of correct invoice
- Late payment interest: [applicable statutory rate or agreed rate] per month on overdue amounts
- Expenses: reimbursed at cost with pre-approval for amounts exceeding [threshold]; no mark-ups

### 6. Acceptance
- Client reviews each Deliverable within [X] business days of receipt
- Acceptance criteria defined in the SOW; deemed accepted if no written objection within the review period
- Remediation: Provider corrects material non-conformities within [X] days of written notice
- Acceptance does not waive warranty claims

### 7. Intellectual Property

**Provider background IP**: Provider's pre-existing IP remains Provider's property; Provider grants Client a licence to use background IP to the extent necessary to use the Deliverables.

**Deliverables (work product)**:
- Option A (client owns): Upon payment, Provider assigns all right, title, and interest in Deliverables to Client. Provider retains a licence to use generic know-how and methodologies.
- Option B (provider owns, client licences): Provider retains ownership; grants Client a perpetual, irrevocable, non-exclusive licence.

Negotiate which option applies based on the nature of the service and commercial leverage.

**Employee / contractor obligations**: Provider warrants that all personnel contributing to the Deliverables have assigned their IP rights to Provider, enabling Provider to make the assignment or grant the licence above.

### 8. Service Level Agreement (SLA)
- Define service levels for each service category (e.g., uptime, response times, resolution times)
- Service credits: if Provider fails to meet SLAs, Client receives a credit against future invoices
- SLA credit cap: typically limited to [X]% of monthly fees
- Excluded downtime: force majeure, scheduled maintenance (pre-notified), Client-caused incidents

### 9. Representations and Warranties
**Provider warrants**:
- Services performed professionally and in accordance with industry standards
- No conflict of interest with other clients
- Deliverables do not infringe third-party IP rights
- Personnel have the skills and qualifications described in the SOW
- Compliance with applicable law including data protection law

**Client warrants**:
- Client materials provided to Provider do not infringe third-party rights
- Client will cooperate and provide timely inputs required for Provider to perform

### 10. Confidentiality
- Mutual NDA: both parties keep each other's Confidential Information confidential
- Standard exclusions: publicly available information, independently developed information, information required to be disclosed by law
- Duration: during MSA term plus [3 / 5] years post-termination

### 11. Data Protection
- If Provider processes personal data on behalf of Client: include a Data Processing Agreement (DPA) as an exhibit or addendum
- DPA must address: processing purposes, data categories, security measures, sub-processing restrictions, data subject rights, breach notification, return/deletion on termination
- Reference applicable law: GDPR (EU/UK), UAE PDPL, KSA PDPL, as applicable

### 12. Limitation of Liability

**Liability cap**: Provider's total liability for any one claim or in aggregate under an SOW is limited to [12 months' fees paid under the relevant SOW / total fees paid in the 12 months preceding the claim / agreed fixed cap].

**Consequential loss exclusion**: Neither party is liable for loss of profits, loss of revenue, loss of business, or indirect / consequential losses.

**Exceptions** (typically carved out from the cap):
- Death and personal injury caused by negligence
- Fraud or fraudulent misrepresentation
- Data protection breaches (consider a separate cap)
- IP infringement indemnity
- Willful misconduct or gross negligence

**MENA note**: in UAE civil law, courts can override contractual liability caps if they consider them unconscionable; the cap should be commercially reasonable relative to the contract value.

### 13. Insurance
Provider must maintain during the MSA term:
- Professional indemnity / errors and omissions: minimum [USD X] per claim
- Public liability: minimum [USD X] per claim
- Cyber liability (if processing personal data or sensitive business data): minimum [USD X]
- Workers' compensation as required by law

### 14. Audit Rights
- Client may audit Provider's records related to the Services, with [30 days'] notice, no more than once per year
- Audit scope: compliance with MSA, billing accuracy, data protection obligations
- Audit costs: borne by Client unless material non-compliance is discovered, in which case Provider bears audit costs

### 15. Term and Termination
- MSA term: [1 / 2 / 3] years, auto-renewing unless terminated on [90-day] written notice
- Each SOW has its own term
- Termination for cause: material breach, uncured for [30] days after written notice; insolvency
- Termination for convenience: [90-day] written notice (if included; often Provider resists)
- Effect of termination: Client pays for services performed to termination date; Provider delivers all work in progress and Client data; transition assistance obligation

### 16. Governing Law and Dispute Resolution
- Cross-border transactions: DIFC or ADGM for MENA parties; English law for GCC-UK deals; UAE Courts for UAE-domestic
- Dispute resolution: negotiation (30 days), then mediation (30 days), then arbitration (ICC / DIAC / LCIA / ADCCAC)
- Language: English (and Arabic for UAE-registered entities where required)

## Jurisdictional notes

| Jurisdiction | Key issues |
|---|---|
| **UAE (onshore)** | Limitation of liability clauses are generally enforceable but courts may override unconscionable caps; Arabic-language version may be required for UAE judicial proceedings; service contracts involving UAE nationals may engage Emiratization requirements. |
| **DIFC / ADGM** | English-law applicable; sophisticated limitation and exclusion clauses generally enforced; DIFC / ADGM Courts enforce MSA dispute clauses effectively. |
| **KSA** | Saudi courts may not enforce exclusion of liability for gross negligence; limitation clauses should be crafted carefully; Sharia principles may affect enforceability of certain penalty/interest provisions. |
| **Lebanon** | Standard limitation of liability clauses are enforceable in commercial contracts; courts have discretion to reduce unconscionable penalties; currency risk must be addressed in payment terms. |
| **EU / GDPR** | Data processing addendum is mandatory for any MSA where Provider processes personal data of EU data subjects; contractual DPA terms must meet GDPR Article 28 requirements. |

## Common mistakes

- **Conflating the MSA and the SOW**: the MSA is framework only; the SOW must define the specific scope. A vague SOW with only an MSA reference leads to disputes about scope.
- **Omitting an acceptance procedure**: if there is no defined acceptance test or deemed-acceptance provision, delivery disputes are resolved by litigation rather than contract.
- **Liability cap too low for data processing services**: a 12-month fee cap on a small SaaS contract may be trivially low relative to the potential GDPR or data breach liability; consider a separate, higher cap for data protection breaches.
- **No transition assistance clause**: without a contractual obligation to provide transition assistance on termination, Provider has no incentive to cooperate with transition to a successor.

## Related skills

- [[prompt-pack-letter-of-intent]]
- [[prompt-pack-joint-venture-agreement]]
- [[prompt-pack-nda-strength-check]]
- [[prompt-pack-privacy-impact-assessment]]
- [[prompt-pack-outside-counsel-guidelines]]

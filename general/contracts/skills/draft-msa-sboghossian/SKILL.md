---
name: draft-msa-sboghossian
title: Master Services Agreement (MSA)
description: Use when drafting a Master Services Agreement under which the parties will execute one or more Statements of Work. Covers the full MSA structure — SOW process, acceptance, IP allocation, liability caps, indemnification, DPA rider triggers, and negotiation positions. Handles MENA-specific issues (data protection riders for KSA PDPL and UAE PDPL, governing-law choices, withholding-tax provisions) and cross-border service delivery. Triggers on "msa", "master services", "master services agreement", "services framework", or "SOW framework" requests.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-msa
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Master Services Agreement (MSA)

## When to use this

A Master Services Agreement is the framework contract under which the parties execute individual Statements of Work (SOWs). The MSA governs the terms and conditions that apply to all SOWs; each SOW supplies the project-specific details (scope, deliverables, timeline, fees).

Use this skill when:
- A service provider and a client anticipate a series of engagements over time and want a single set of governing terms
- A corporate client wants to streamline procurement by signing one legal framework and negotiating only commercial terms per project
- The engagement involves significant IP output, data processing, or cross-border service delivery (where a bespoke framework is preferable to ad hoc contracts)

For a single one-off services engagement, a standalone statement of work or services agreement is often sufficient.

## Required inputs

| Input | Why it matters | Default |
|-------|---------------|---------|
| Service Provider | Company name, entity type, registration, address | — must supply |
| Client | Same | — must supply |
| Scope of services | High-level description; details in SOWs | — must supply |
| Term | Duration of the master framework | 1 year, auto-renewing annually unless 60-day notice |
| Governing law | Law of the MSA | Provider's home jurisdiction (client often resists) |
| Fee structure | Fixed / T&M / outcome-based / hybrid | Per SOW |

## Optional inputs

- Most-favored-customer clause (client wants the best rate offered to comparable customers)
- Exclusivity or non-compete during the term
- IP ownership model: work-for-hire vs license-back; pre-existing IP carve-out
- Data Processing Agreement rider (trigger: any processing of Client personal data — see [[draft-dpa-gdpr]], [[draft-dpa-ksa-pdpl]], [[draft-dpa-uae-pdpl]])
- SLA annex (uptime, response time, availability commitments)
- Security annex (data security standards, audit rights)
- Insurance requirements (levels of cover for E&O, general liability, cyber)

## Document structure

### 1. Parties and recitals
Full identification. Recitals: Service Provider's capabilities; Client's business; the mutual intent to establish a framework for services; each SOW will be governed by this MSA.

### 2. Definitions
Core definitions: Agreement, SOW, Services, Deliverables, Confidential Information, Intellectual Property, Background IP, Foreground IP, Client Materials, Personal Data, Data Processing Agreement, Force Majeure Event, Change Request.

### 3. SOW process
The engine of the MSA:
- Each project begins with a proposed SOW; template attached as Schedule 1
- The SOW is not binding until signed by both parties
- In case of conflict: the SOW governs for project-specific matters; the MSA governs for all other matters (express conflict hierarchy)
- SOW contents: scope of services, deliverables, milestones, acceptance criteria, fees and payment schedule, project-specific personnel or subcontractors, project manager on each side

### 4. Services and deliverables
- Provider performs the Services with professional skill and care; in accordance with the SOW; and in compliance with applicable laws
- Provider assigns a qualified team; key personnel changes require Client's prior approval
- Change request procedure: either party may propose a change via a written Change Request; Provider provides impact assessment (time and cost); Client approval required before any change is executed

### 5. Acceptance criteria
- Upon delivery of each Deliverable (or at milestones), Client has X business days to review and accept or reject
- Acceptance criteria stated in the SOW; objective wherever possible
- Rejection: Client provides written notice specifying defects; Provider corrects within X business days and resubmits
- Deemed acceptance: if Client fails to respond within the review period, the Deliverable is deemed accepted
- Consequences of rejection: Provider corrects at no additional cost

### 6. Fees, expenses, invoicing, and payment
- Fees per the SOW (fixed fee, T&M rate card, milestone-based, or hybrid)
- Expenses: pre-approved categories only (travel at cost per policy; third-party costs with prior approval)
- Invoicing: monthly or milestone-based; invoice to include SOW reference, description of services, period covered
- Payment: 30 days net from invoice date (30/60 days)
- Late payment interest: [central bank rate + 3%] per annum, calculated daily
- Taxes: each party responsible for its own taxes; Client bears any withholding tax and grosses up if required by law

### 7. Intellectual property
IP allocation is the most commercially significant clause in an MSA and the most-negotiated.

**Background IP**: IP owned by each party before the Agreement or developed independently outside the Agreement. Each party retains ownership of its Background IP. Neither party acquires any rights in the other's Background IP beyond what is expressly licensed in a SOW.

**Foreground IP (Deliverables)**: IP created specifically for Client under a SOW:
- **Option A (Client owns)**: Deliverables are created as a work-for-hire or assigned to Client on payment. Provider retains no rights to use Client's Deliverables.
- **Option B (Provider owns)**: Provider retains ownership; grants Client a perpetual, irrevocable, non-exclusive license to use the Deliverables for Client's internal business purposes.
- **Most common negotiated outcome**: Client owns the custom Deliverables; Provider retains ownership of underlying toolkits, frameworks, and re-usable components (expressly carved out in the SOW) and grants Client a license to those components as incorporated in the Deliverables.

**Client Materials**: all materials provided by Client. Provider may only use them to perform Services; no other use; return or destroy on termination.

For IP assignment language: see [[draft-ip-assignment]].

**Moral rights** (civil-law jurisdictions): in LB, FR, and other civil-law countries, moral rights (droit moral) are inalienable — the author retains the right to attribution and the right to object to derogatory treatment. Work-for-hire language does not extinguish moral rights in civil-law jurisdictions. Address this explicitly.

### 8. Confidentiality
NDA-grade obligations apply to both parties' Confidential Information. Standard carve-outs: publicly known; independently developed; received from a third party without restriction; required to be disclosed by law (with notice). For benchmarks: see [[draft-nda-mutual]].

### 9. Representations and warranties
**Provider warrants:**
- Services will be performed with professional skill and care consistent with industry standards
- No conflicts of interest with Client's business
- Provider has the right to grant any IP licenses contemplated
- Provider is not prohibited by any prior agreement from performing the Services
- Services will comply with applicable laws

**Client warrants:**
- Has the authority to enter into the MSA and each SOW
- Client Materials do not infringe third-party IP
- Client will provide timely review and feedback

### 10. Limitation of liability
One of the hardest-negotiated provisions:

**Liability cap**: Provider's aggregate liability under the MSA and all SOWs is capped at: the fees paid to Provider in the 12 months preceding the event giving rise to the claim.

**Consequential damage exclusion**: Neither party is liable for indirect, consequential, special, incidental, or punitive damages (loss of profits, loss of revenue, loss of data, loss of business opportunity).

**Carve-outs from cap and exclusion** (these are never limited or excluded by the cap):
- Fraud or willful misconduct
- IP indemnification obligations (often separately capped at a higher amount — typically 2-3× annual fees)
- Confidentiality breaches (often separately capped or unlimited)
- Death or personal injury caused by negligence
- Any liability that cannot be excluded by law

Note: limitation of liability clauses are subject to statutory controls in EU (UCTA 1977 in UK; similar in EU consumer contexts) and may be read narrowly by MENA civil-law courts. The general principle applies across MENA commercial courts, but the courts retain discretion to reduce.

### 11. Indemnification
- **Provider indemnifies Client**: against third-party claims that Provider's Services or Deliverables (as delivered, without modification by Client) infringe a third party's IP rights
- **Client indemnifies Provider**: against third-party claims arising from Client Materials, Client's modification of Deliverables, Client's use of Deliverables outside the permitted scope
- Indemnification procedure: prompt notice; sole control of defense (with right to monitor); cooperation; no admission without indemnifying party's consent
- See [[review-indemnification-balance]] for balance analysis

### 12. Term and termination

**Term**: commencement date to expiry of the last active SOW or the end of the master term, whichever is later.

**Renewal**: auto-renewing annual terms unless either party gives [60]-day written notice.

**Termination for convenience**: either party may terminate the MSA (with no active SOWs) on [30/60/90]-day written notice.

**Termination for cause** (with cure): material breach; written notice; [30]-day cure period.

**Termination of individual SOW**: either party may terminate a specific SOW for convenience with [30]-day notice; Provider is compensated for work performed and reasonable wind-down costs.

**Insolvency termination**: immediate on insolvency filing.

### 13. Post-termination obligations
- **Transition assistance**: Provider cooperates for up to [90] days post-termination to assist Client's transition to a new provider; at Provider's standard rates
- **Deliverable handoff**: all Deliverables, work in progress, and Client Materials returned within 30 days
- **Return of Confidential Information**: all materials certified destroyed or returned
- **Surviving provisions**: payment obligations, confidentiality, IP ownership, liability limitations, indemnification, governing law — all survive termination

### 14. Force majeure
Neither party liable for failure to perform due to events beyond its reasonable control (pandemic, natural disaster, war, government action, infrastructure failure). Notification obligation; mitigation obligation; right to terminate if force majeure persists beyond [90] days.

### 15. Dispute resolution
For cross-border MSAs: arbitration strongly recommended. Specify seat (DIAC/DIFC for UAE; SCCA/Riyadh for KSA; LCIA/ICC for international), rules, and language.

### 16. Boilerplate
Entire agreement, amendment (only in writing), assignment (Provider may assign to affiliate; otherwise consent required), severability, no waiver, notices, counterparts — see [[draft-boilerplate-clauses]].

## SOW template (Schedule 1)
Each SOW should contain:
- SOW number and date
- Reference to the MSA
- Scope of services (specific, not general)
- Deliverables (enumerated, with description)
- Acceptance criteria (objective)
- Project timeline with milestones
- Fees (fixed / T&M rate card / milestone-based)
- Project managers (both sides)
- Any project-specific deviations from MSA terms (state expressly)

## Common negotiation points

| Issue | Provider prefers | Client prefers |
|-------|-----------------|---------------|
| Liability cap | 12-month fees; consequentials excluded | Higher multiplier; IP and data-breach carve-outs uncapped |
| IP ownership | License-back only | Full assignment of custom Deliverables |
| Termination for convenience | Long notice period; wind-down compensation | Short notice; no penalty |
| Acceptance | Short acceptance window; objective criteria | Long review period; broad grounds for rejection |
| Payment terms | 30 days; no right to set-off | 60 days; right to withhold disputed amounts |
| Subcontracting | Unrestricted | Requires Client approval; flow-down of all obligations |

## MENA-specific issues

- **Data Processing Agreement**: if any Client data (including employee data) is processed, attach a DPA. Required by GDPR (EU/UK), KSA PDPL, UAE PDPL, and increasingly by EG PDPL. See [[draft-dpa-gdpr]] / [[draft-dpa-ksa-pdpl]].
- **Withholding tax**: service fees paid to a non-resident provider may be subject to withholding tax in KSA (20% generally), UAE (no WHT), LB (7.5% dividend; 10% services to non-residents), EG (variable). Gross-up provision in the MSA allocates this risk.
- **Value Added Tax**: UAE 5% VAT; KSA 15% VAT; LB no VAT currently; EG 14% VAT. Clarify whether fees are VAT-inclusive or exclusive.

## Related skills

- [[draft-msa-extension]]
- [[review-msa-deep-review]]
- [[review-indemnification-balance]]
- [[draft-ip-assignment]]
- [[draft-nda-mutual]]
- [[draft-dpa-gdpr]]

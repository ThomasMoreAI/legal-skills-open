---
name: ma-transaction-summary
title: M&A Transaction Summary
description: Generates structured M&A transaction summaries from deal documents. Triggers when the user needs to summarize a merger, acquisition, asset purchase, stock purchase, or divestiture, or when preparing board-level deal overviews from definitive agreements and due diligence materials.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/ma-transaction-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: corporate
language: en
tags: [summarization, summary, transactional]
---

# M&A Transaction Summary

Produces a stakeholder-ready reference summarizing a completed or pending M&A transaction for executives, board members, investors, and employees.

## Prerequisites

1. **Definitive agreement** — purchase agreement, merger agreement, or term sheet
2. **Due diligence reports** — financial, legal, IP, HR, environmental, tax
3. **Financial materials** — models, fairness opinions, pro forma projections
4. **Integration plan** — if available
5. **Board materials** — presentations, resolutions, approvals

## Quick Start

1. Collect definitive agreement and all available DD reports
2. Walk through each output section below, extracting from source documents
3. Cross-reference all figures, dates, and defined terms against the definitive agreement
4. Flag incomplete workstreams and open items with risk allocation
5. Apply confidentiality legends and version control before distribution

## Output Sections

### 1. Executive Overview (2 paragraphs max)

| Element | Detail |
|---|---|
| Parties | Buyer, seller, co-investors |
| Structure | Asset purchase / stock purchase / merger / other |
| Total consideration | Cash, stock, earnouts, deferred — with amounts |
| Expected closing | Date or timeline |
| Strategic rationale | One-sentence thesis |

### 2. Deal Structure & Terms

- Transaction form and rationale (tax, regulatory, liability)
- Purchase price breakdown:

| Component | Detail |
|---|---|
| Cash at close | Amount |
| Stock consideration | Exchange ratio, collar, valuation method |
| Earnouts | Metrics, measurement periods, caps |
| Escrow/holdbacks | Amount, release schedule, claims process |
| Working capital adjustment | Mechanism, target, true-up timeline |

- Assumed vs. excluded liabilities
- Deferred or contingent payment mechanics

### 3. Due Diligence Findings

Per workstream, capture: (a) findings supporting thesis, (b) material concerns, (c) mitigation in deal docs.

Workstreams: Financial/Accounting, Legal/Regulatory, IP/Technology, Commercial/Contracts, HR/Benefits, Environmental/Real Estate, Tax.

Flag incomplete workstreams and note risk allocation for open items.

### 4. Reps, Warranties & Indemnification

| Element | Detail |
|---|---|
| R&W scope | Fundamental vs. general; materiality/knowledge qualifiers |
| Survival periods | By category |
| Indemnification basket | Type (deductible/tipping), amount |
| Liability cap | General vs. fundamental reps |
| Special indemnities | Identified risks with specific coverage |
| R&W insurance | Carrier, retention, policy limit, exclusions (if applicable) |
| Escrow | Amount, term, release conditions |

### 5. Closing Conditions

Track status for each:
- HSR / antitrust clearance
- Foreign investment reviews (CFIUS, FDI)
- Industry-specific regulatory consents
- Third-party consents (customers, landlords, lenders)
- Financing condition — commitment status, market flex
- MAE provision — scope and carve-outs
- Other conditions precedent

Assess likelihood of timely satisfaction for each.

### 6. Integration Plan

Cover by functional area (governance, finance, HR, sales, technology, supply chain):
- Approach, timeline, key milestones
- Post-closing governance (standalone vs. integrated)
- Key employee retention mechanisms
- Regulatory or consent constraints on integration timing

### 7. Strategic Rationale & Value Creation

- Investment thesis (market expansion, capability acquisition, synergies)
- Synergy quantification: cost savings and revenue enhancements with estimated values and realization timelines
- Strategic fit within buyer's portfolio
- Seller rationale (if applicable)

### 8. Stakeholder Impact

| Stakeholder | Impact |
|---|---|
| Shareholders | Consideration, tax implications, payment timing |
| Employees | Employment terms, benefits changes, org restructuring |
| Customers/suppliers | Contractual continuity, service levels |
| Creditors | Security interests, debt assumptions |

Flag uncertainties dependent on post-closing decisions.

### 9. Risk Factors & Mitigation

Categories: integration execution, regulatory, customer/employee attrition, financial performance, synergy realization, litigation.

For each material risk, identify the contractual protection, insurance, or operational strategy addressing it.

## Pitfalls & Checks

- **MNPI handling** — document contains material nonpublic information; apply confidentiality legends and comply with securities laws and NDA obligations
- **Forward-looking statements** — label all projections and pro forma figures with cautionary language
- **Cross-reference** — verify all figures, dates, and defined terms against the definitive agreement
- **Tone** — professional and objective; not advocacy or promotional
- **Audience versions** — if preparing multiple versions, note redaction scope (full board vs. employee communication)
- **Version control** — include date and version number if the summary will be updated through closing
- **Open items** — identify pending negotiation points or regulatory items with expected resolution timelines
- **Contact info** — conclude with deal team and counsel contacts for stakeholder questions

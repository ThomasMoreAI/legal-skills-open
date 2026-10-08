---
name: pa-workflow-regulatory-cross-jurisdiction-tracker-sboghossian
title: Regulatory — Cross-Jurisdiction Tracker
description: Use when a multinational client or law firm practice group needs to monitor and compare regulatory developments across multiple jurisdictions simultaneously. Produces a weekly-updated comparative table, impact assessments per jurisdiction, and implementation timeline recommendations. Designed for MENA-headquartered clients with exposure to UAE, KSA, LB, EG, EU, UK, and US regulatory frameworks, particularly in financial services, data, and technology sectors.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/pa-workflow/pa-workflow-regulatory-cross-jurisdiction-tracker
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: regulatory
language: en
---

# Regulatory — Cross-Jurisdiction Tracker

## Purpose

Multinational clients face a fragmented regulatory landscape: the same business activity (data processing, AML, financial services, AI deployment) is regulated differently across jurisdictions, often on different timelines. This workflow maintains a living comparative table that tracks regulatory developments across the client's relevant jurisdictions, assesses impact, and recommends implementation sequencing.

## Inputs

| Input | Required | Notes |
|---|---|---|
| Client's operational jurisdictions | Yes | List of countries / free zones where the client is licensed or active |
| Regulatory domains to track | Yes | E.g., data protection, AML/CFT, financial services licensing, AI governance, ESG |
| Update frequency | Recommended | Default: weekly; daily for clients in high-flux regulatory environments |
| Client profile | Recommended | Industry sector, license types, data footprint — determines relevance scoring |
| Prior tracker version | Optional | For delta-only updates |

## Tracker Structure

### Comparative Regulatory Table

The core output. Rows = regulatory domains or specific requirements. Columns = jurisdictions.

| Requirement | UAE (mainland) | DIFC | KSA | LB | EG | EU (GDPR) | UK | US (sectoral) |
|---|---|---|---|---|---|---|---|---|
| **Data Protection** | | | | | | | | |
| Data subject rights | Law in force (PDPL-UAE, 2022) | DIFC DP Law 2020 | PDPL KSA (2024) | Draft law (stalled) | Law 151/2020 | GDPR Art. 12–22 | UK GDPR | CCPA/CPRA (CA); sectoral |
| Cross-border transfer | Adequacy / contractual safeguards | DIFC DP adequacy decisions | Restricted; regulatory approval required | Not yet operative | CBE framework | Standard Contractual Clauses | UK IDTA | No federal standard |
| **AML/CFT** | | | | | | | | |
| Beneficial ownership | UAE corporate register (AML Law) | DIFC BO register | MISA/Zakat requirements | BDL circulars | Law 80/2002 | 5AMLD / 6AMLD | POCA + MLR 2017 | FinCEN CDD Rule |

For each cell: current status (In force / Draft / Consultation / Not yet adopted) + effective date + key obligation summary.

### Delta Log (weekly update)

Track changes since last report:

```markdown
## Weekly Regulatory Delta — [Date Range]

### NEW DEVELOPMENTS

**UAE — VARA Virtual Asset Regulation Update**
- Summary: VARA issued updated marketing regulations for virtual asset service providers
- Effective: 30 days from publication
- Client impact: HIGH if client operates a VASP or promotes virtual asset products
- Action required: Review marketing materials for compliance before deadline

**KSA — SDAIA PDPL Implementing Regulations (Draft)**
- Summary: Draft implementing regulations for consent and data transfer published for consultation
- Comment deadline: [date]
- Client impact: MEDIUM — refines but does not fundamentally change current compliance approach
- Action required: Review draft; submit comment if client has KSA data operations

### UPCOMING DEADLINES

| Jurisdiction | Requirement | Deadline | Client impact |
|---|---|---|---|
| UAE | CBUAE Open Banking Phase 2 | 2025-09-01 | HIGH — licensed bank |
| EU | AI Act high-risk AI systems compliance | 2026-08-02 | MEDIUM — client uses AI in credit scoring |
| KSA | PDPL — data subject rights operationalization | 2025-03-17 | HIGH — large Saudi customer base |
```

### Impact Assessment per Jurisdiction

For each active regulatory development:

| Development | Jurisdiction | Applicability | Impact level | Recommended action | Urgency |
|---|---|---|---|---|---|
| VARA Marketing Regs | UAE | VASP clients | HIGH | Legal review of all marketing materials | IMMEDIATE |
| AI Act — High-Risk AI | EU | AI product clients | MEDIUM | Risk classification of AI systems | Q3 2025 |
| PDPL Data Transfers | KSA | Any entity processing Saudi residents' data | HIGH | Review transfer mechanisms; obtain required approvals | URGENT |

### Implementation Timeline Recommendations

The tracker produces a sequenced implementation schedule per client, accounting for:
- Regulatory deadlines (hard compliance dates)
- Regulator inspection schedules (if known)
- Interdependencies between jurisdictions (e.g., implementing GDPR-compatible policies first makes DIFC DP compliance easier)
- Client's resource constraints

```
Q1 2025 — Complete
  [x] UAE CBUAE AML update — policy updated, staff trained
  [x] DIFC DP Law — data mapping completed

Q2 2025 — In progress
  [ ] KSA PDPL — data subject rights process (due Q2)
  [ ] UAE VARA — marketing materials review (due before VARA inspection)

Q3 2025 — Planned
  [ ] CBUAE Open Banking Phase 2 — API integration (due Sep 2025)

Q4 2025 — Planned
  [ ] EU AI Act preparation — risk classification of AI systems
```

## Regulatory Intelligence Sources

For each jurisdiction, the tracker pulls from:

| Jurisdiction | Source |
|---|---|
| UAE | UAE Official Gazette (Al-Jarida Al-Rasmiya); CBUAE website; SCA/ESCA; VARA; DIFC portal; ADGM portal |
| KSA | Saudi Official Gazette (Umm Al-Qura); SAMA; SDAIA; CMA; Zakat, Tax and Customs Authority (ZATCA) |
| Lebanon | BDL circulars; Lebanese Official Gazette; Ministry of Economy |
| Egypt | Official Gazette; CBE; FRA |
| EU | EUR-Lex; EDPB guidelines; EBA/ESMA/EIOPA |
| UK | UK Official Gazette; FCA; ICO |
| US | Federal Register; SEC; FinCEN; CFPB |

## MENA-Specific Tracking Notes

- **GCC convergence**: GCC states coordinate through the GCC Secretariat on financial regulation. A development from SAMA or CBUAE often signals forthcoming similar requirements in other GCC states (3–18 months lag typical).
- **Free zone vs. onshore**: UAE developments often apply differently to DIFC/ADGM (which have their own regulators) vs. mainland UAE. Track separately; do not conflate.
- **Arabic-language sources**: Many MENA regulatory developments are published first in Arabic with later English translations. The tracker should process Arabic-language official gazettes directly to avoid delay.
- **Regulatory consultation windows**: GCC regulators increasingly publish consultation papers. Clients in affected industries should consider submitting comments — it signals engagement and sometimes influences final rules.

## Output Formats

- **Full tracker** (spreadsheet): complete comparative table, all jurisdictions, all domains
- **Weekly delta report** (email/Slack): new developments + upcoming deadlines only
- **Board compliance summary** (presentation): quarterly, executive-level view
- **Jurisdiction spotlight** (PDF): deep dive on a single jurisdiction, triggered by a major development

## Related Skills

- [[pa-workflow-regulatory-daily-digest-publisher]]
- [[pa-workflow-regulatory-compliance-gap-matrix]]
- [[pa-workflow-regulatory-client-alert-drafter-firm-voice]]
- [[pa-workflow-regulatory-enforcement-likelihood-scorer]]

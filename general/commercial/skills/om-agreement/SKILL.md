---
name: om-agreement
title: O&M Agreement
description: Drafts Operations and Maintenance agreements for energy facilities covering scope, performance standards, compensation, risk allocation, and regulatory compliance. Use when drafting O&M contracts, maintenance agreements for power plants, solar farms, wind projects, or energy infrastructure.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/om-agreement
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: commercial
language: en
---

# O&M Agreement

Drafts a commercially balanced O&M agreement between a project owner and contractor for an energy facility. Integrates with PPAs, financing documents, and permit requirements.

## Prerequisites

Gather before drafting:

1. **Facility details** — type (solar, wind, gas, storage), capacity, location, technology, COD status
2. **Related documents** — PPA, financing/loan agreements, EPC contract, interconnection agreement, permits
3. **Party information** — full legal names, jurisdiction, regulatory IDs/licenses for owner and contractor
4. **Commercial terms** — compensation model (fixed, variable, cost-plus, hybrid), term length, renewal expectations
5. **Lender requirements** — direct agreement obligations, consent rights, reporting covenants
6. **Regulatory context** — environmental permits, grid codes, safety regulations, renewable attribute requirements

## Quick Start

1. Collect all prerequisites and related project documents
2. Draft articles 1–9 per the structure below
3. Attach schedules A–H with facility-specific detail
4. Cross-check against PPA, financing docs, and permits for consistency
5. Verify LD provisions, insurance, and force majeure alignment across all project agreements

## Agreement Structure

### Art. 1: Definitions & Recitals

- Standalone defined-terms section for all capitalized terms
- Recitals reference: facility specs, related agreements (PPA, financing, EPC), regulatory approvals
- Party identification: full legal names, entity type, jurisdiction, addresses, license numbers

### Art. 2: Scope of Services

| Category | Key Items |
|---|---|
| Preventive maintenance | Scheduled inspections, testing, calibration, predictive programs |
| Corrective maintenance | Emergency response, troubleshooting, unscheduled repairs |
| Major maintenance | Planned outages, overhauls, component replacements |
| Inventory management | Spare parts, OEM coordination, warranty compliance |
| Environmental compliance | Emissions monitoring, reporting, waste management |
| Health & safety | Safety programs, incident reporting, OSHA compliance |
| Staffing | Minimum on-site presence, qualifications, training |
| Performance optimization | Data collection, monitoring systems, continuous improvement |
| Records & reporting | Documentation standards, operational records, maintenance logs |

Delineate owner vs. contractor responsibility for capital improvements, major equipment replacement, facility modifications, and technology upgrades.

### Art. 3: Performance Standards

| Metric | Specification |
|---|---|
| Availability | Minimum % over measurement period; calculation methodology |
| Equivalent availability factor | If applicable to facility type |
| Forced outage rate | Maximum threshold |
| Planned outage limits | Annual allowance in hours/days |
| Efficiency | Heat rate, thermal efficiency, fuel consumption (as applicable) |
| Environmental | Emissions limits, permit compliance, REC preservation |
| Output | Minimum production levels, capacity factor targets |

Include: measurement methodology and data sources; adjustments for partial operations, seasonal variation, degradation, curtailment; excused events (force majeure, owner-caused delays, directed outages, grid constraints); third-party verification protocols.

### Art. 4: Compensation

Select model based on commercial terms: fixed fee, variable (tied to availability/production), cost-plus, or hybrid.

Required provisions:
- [ ] Base fee and rate schedule
- [ ] Additional services rates and reimbursable expenses
- [ ] Escalation provisions (CPI, labor index)
- [ ] Invoicing schedule, payment terms
- [ ] Annual budget process and variance reporting
- [ ] Scope change adjustments

**Incentive/penalty structure:** Performance bonuses for exceeding thresholds; LDs for failures below minimum standards. LDs must be structured as genuine pre-estimates of loss. Include: calculation methodology, aggregate caps, cure periods, and relationship to other remedies (termination, step-in).

### Art. 5: Term & Transition

- Commencement date (tied to effective date, COD, or milestone)
- Initial term, renewal mechanism (automatic vs. mutual vs. option), notice periods
- Conditions precedent for renewal (performance history, third-party consents)

Transition checklist:
- [ ] Knowledge transfer and training period
- [ ] Records and documentation handover
- [ ] Spare parts and inventory disposition
- [ ] Software license transfers
- [ ] Cooperation with successor contractor

### Art. 6: Termination

- **For cause** — persistent performance failures, safety violations, environmental noncompliance, payment defaults, breach of critical covenants; notice and cure periods by breach type
- **For convenience** (owner) — notice period, termination fee, wind-down costs
- **Event-triggered** — extended force majeure, insolvency, loss of licenses, regulatory impossibility, insurance failure

Post-termination:
- [ ] Wind-down and transition assistance
- [ ] Return of owner property and confidential information
- [ ] Final accounting, payment reconciliation, release of security

**Owner step-in rights** — conditions for temporary assumption of operations; contractor property protections during step-in.

### Art. 7: Risk Allocation

**Reps & warranties:** Contractor — qualifications, financial capacity, license status. Owner — facility ownership, authority, known conditions.

**Indemnification:** Mutual for negligence, willful misconduct, breach. Specify limitations, exclusions, claim procedures, defense obligations.

**Insurance:**

| Coverage | Notes |
|---|---|
| Commercial general liability | Specify minimum limits |
| Professional liability (E&O) | |
| Workers' compensation | Statutory limits |
| Pollution/environmental | If applicable |
| Builder's risk / property | During major maintenance |

Additional insured endorsements, waiver of subrogation, certificate requirements.

**Liability caps:** Aggregate cap (typically tied to annual fee or contract value). Consequential damages exclusion with carve-outs for indemnification, confidentiality, willful misconduct, IP infringement.

### Art. 8: Compliance & Governance

| Report | Frequency |
|---|---|
| Operational | Daily |
| Performance | Monthly |
| Financial | Quarterly |
| Budget | Annually |
| Incident / Regulatory | As-needed |

Governance: operational meetings, quarterly business reviews, annual planning, emergency protocols. Owner audit rights over records, facilities, and operations. Change management procedures for scope/regulatory/facility modifications.

### Art. 9: Dispute Resolution & General Provisions

Tiered resolution: (1) negotiation 30 days → (2) executive escalation 30 days → (3) optional mediation 60 days → (4) arbitration or litigation.

- [ ] Force majeure definition and procedures
- [ ] Confidentiality protections
- [ ] Notice requirements
- [ ] Assignment/subcontracting restrictions (financing assignment carve-out)
- [ ] Entire agreement, amendment, severability, waiver
- [ ] Document hierarchy for conflicts with related project agreements

### Schedules

- **A** — Facility technical specifications
- **B** — Detailed scope of services
- **C** — Performance standards and calculations
- **D** — Compensation and fee schedule
- **E** — Key personnel and staffing
- **F** — Insurance requirements
- **G** — Report forms
- **H** — Approved subcontractors

## Critical Checks

- Align performance metrics with PPA delivery obligations and lender availability covenants
- Ensure force majeure definitions are consistent across O&M, PPA, and financing documents
- Structure LDs as genuine pre-estimates of loss — not penalties — for enforceability
- Verify contractor insurance satisfies lender direct agreement obligations
- Include lender consent rights for assignment, termination, material amendments where required
- Address NERC reliability standards if facility is subject to bulk power system regulation [VERIFY]
- For renewables: preserve ITC/PTC eligibility and renewable attribute certification in O&M scope
- Balance step-in rights — broad enough for owner protection, narrow enough to avoid re-characterization of contractor as employee/agent
- Confirm governing law is consistent with facility siting jurisdiction and related agreement forum-selection clauses

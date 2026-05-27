---
name: power-purchase-agreement
title: Power Purchase Agreement (PPA)
description: Drafts U.S. power purchase agreements (PPAs) between generators and offtakers covering delivery, pricing, metering, performance guarantees, RECs/carbon attributes, credit support, defaults, and remedies. Triggers on "PPA", "power purchase agreement", "offtaker", "generator", "REC", "net output", "renewable energy offtake", "energy supply agreement", or "energy payment".
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/power-purchase-agreement
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: commercial
language: en
tags: [agreement, drafting, regulatory]
---

# Power Purchase Agreement (PPA)

Produces a commercially balanced, regulation-aware agreement for the sale and purchase of electric energy between a generator and an offtaker.

## Quick Start

Gather before drafting:

1. **Parties** — legal names, jurisdictions, signatory authority, guarantors.
2. **Project** — facility type, location, capacity (MW), technology, COD targets, interconnection status.
3. **Delivery** — delivery point, ISO/RTO or utility territory, scheduling/dispatch model.
4. **Commercial** — term length, pricing model, escalators, payment cycle, taxes.
5. **Attributes** — REC/carbon ownership, transfer mechanics, certification requirements.
6. **Risk** — curtailment allocation, force majeure, change-in-law, credit support, insurance.
7. **Operations** — metering standards, testing cadence, data interfaces.
8. **Finance** — lender requirements, step-in rights, consent rights (if project-financed).

## Drafting Skeleton

```text
1. Parties; Recitals
2. Definitions and Interpretation
3. Term; Conditions Precedent
4. Sale and Purchase; Delivery; Scheduling
5. Pricing; Invoicing; Taxes
6. Metering; Measurement; Data
7. Environmental Attributes
8. Representations and Warranties
9. Covenants; Reporting; Compliance
10. Performance Standards; Liquidated Damages
11. Events of Default; Remedies
12. Force Majeure
13. Insurance; Credit Support
14. Termination; Consequences
15. Dispute Resolution; Governing Law
16. Miscellaneous
Exhibits A–E
```

## Core Workflow

### 1. Key Definitions

Define these precisely — they drive pricing, performance, and defaults:

| Term | Define |
|---|---|
| Contract Capacity | MW/kW, net of parasitic load |
| Delivered Energy | kWh/MWh measured at delivery point |
| Net Output | Adjustments for losses/auxiliary load |
| Commercial Operation Date | Objective tests and certification criteria |
| Force Majeure | Scope, exclusions, duration caps |
| Availability | Calculation formula and exclusions |
| REC/Environmental Attributes | Registry, certification, transfer mechanics |

### 2. Conditions Precedent

Set deadlines for each; specify consequence of non-satisfaction:

- Permits/licenses obtained and in force
- Interconnection agreement executed
- Construction milestones met; COD evidence delivered
- Insurance with required endorsements in place
- Credit support posted and accepted
- Regulatory approvals (if applicable)

### 3. Pricing Model

Select one and fully specify:

| Model | Key Inputs |
|---|---|
| Fixed energy price | $/MWh, escalator, start date |
| Indexed price | Index, reset frequency, floor/ceiling |
| Time-of-delivery | Peak/off-peak bands, seasonal tables |
| Capacity + energy | Capacity payment, availability test |
| Pay-as-produced | Output-based with curtailment rules |

### 4. Metering and Data

- Accuracy requirement (e.g., ±0.5%)
- Calibration frequency and standards
- Data delivery method and timing
- Dispute process and true-up timeline
- Loss factor allocation between POI and delivery point

### 5. Performance and Liquidated Damages

| Metric | Measurement | Remedy |
|---|---|---|
| Availability (% annual) | Defined formula | LDs per shortfall |
| Energy guarantee (MWh/period) | Net Delivered | LDs or make-whole |
| COD delay (days late) | Milestone dates | LDs per day |

LDs must be a reasonable pre-estimate of loss, not a penalty.

### 6. Default and Remedy Framework

- Cure periods by type: payment (short), non-monetary (longer), insolvency (none)
- Termination rights and effective-date mechanics
- Damages: cover costs, replacement power, termination payment calculation
- Lender step-in/cure rights (only if finance structure requires)

### 7. Exhibits (minimum set)

- **A** — Facility description, POI, single-line diagram
- **B** — Pricing tables, escalation schedule, example invoices
- **C** — Metering specs, testing protocol, data format
- **D** — Form notices, designated recipients
- **E** — Credit support forms (LOC/guarantee)

## Pitfalls and Checks

- **[VERIFY]** jurisdiction-specific regulatory approvals, ISO/RTO tariffs, and interconnection rules before finalizing.
- Align REC/carbon transfer language with registry requirements and buyer compliance targets.
- Keep curtailment rights symmetrical or clearly allocated — avoid implied take-or-pay conflicts.
- Tie COD, availability, and performance tests to objective, auditable criteria.
- Ensure delivery point definitions are consistent across main body and exhibits.
- Match confidentiality/announcement clauses to financing and regulatory disclosure obligations.

---
name: gas-gathering-agreement
title: Gas Gathering Agreement
description: Drafts a Gas Gathering Agreement for receipt, compression, dehydration, and transportation of natural gas from wellhead to delivery point. Enforces FERC compliance, AAPL form alignment, API/GPA measurement standards, and midstream risk allocation. Use when drafting or negotiating midstream gathering contracts, producer-gatherer agreements, dedicated acreage agreements, or gas transportation arrangements.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/gas-gathering-agreement
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: regulatory
language: en
tags: [agreement, drafting, transactional]
---

# Gas Gathering Agreement

Drafts a producer-gatherer agreement governing gathering services from receipt point to delivery point, with FERC compliance, industry-standard measurement, and mutual risk allocation.

## Prerequisites

1. **Party information** — legal names, state of formation, FERC designations or operator numbers
2. **Well/acreage description** — well locations, dedicated acreage boundaries, production data
3. **System description** — gathering infrastructure scope (pipelines, compressors, meters, treating facilities)
4. **Commercial structure** — fee type (per-MMBtu/Mcf, percentage-of-proceeds, or hybrid), initial rate, escalation
5. **Regulatory posture** — jurisdiction (state PUC, FERC-jurisdictional or non-jurisdictional), environmental permits
6. **Desired term** — initial term, renewal structure, conditions precedent

If any prerequisite is missing, pause and ask — do not assume.

## Output Structure

### 1. Parties & Recitals
- Full party identification with organizational capacity and regulatory IDs
- Recitals: producer's gas ownership, gatherer's system ownership, regulatory framework, compliance intent

### 2. Definitions

| Term | Content |
|------|---------|
| Gas / Natural Gas | Quality specs, composition, heating value, contaminant limits |
| Gathering System | Pipelines, compressors, meters, dehydration/treating facilities |
| Point of Receipt / Delivery | Custody and risk transfer locations |
| Gathering Services | Scope: gather, compress, dehydrate, treat, transport |
| Dedicated Acreage | Geographic scope with metes-and-bounds or plat reference |
| Volume/Measurement | API MPMS or GPA standards [VERIFY current edition]; pressure base, temperature correction, Btu specs |

### 3. Grant of Rights & Services
- Exclusive vs. non-exclusive dedication within contract area
- Gatherer rights: construct, operate, maintain facilities; easements/ROW
- Producer obligations: deliver conforming gas; scheduling and nomination protocols
- Gatherer obligations: accept and transport subject to capacity and quality specs
- MVC, take-or-pay, or ship-or-pay terms if applicable

### 4. Rates, Fees & Payment

| Element | Details |
|---------|---------|
| Fee structure | Per-MMBtu/Mcf; percentage-of-proceeds; or hybrid |
| Escalation | Fixed annual, index-based, or periodic renegotiation |
| Billing | Monthly; payment due [X] days after invoice |
| Disputes | Written notice within [X] days; undisputed amounts paid timely |
| Late payment | Interest at [prime + X%] or statutory rate |
| Audit rights | Producer audit of meters on [X] days' notice |

### 5. Term & Termination
- **Initial term**: 5–20 years (capital recovery driven); commencement date and conditions precedent
- **Renewal**: Auto-renew [X]-year terms unless [X] days' notice of non-renewal
- **For cause**: Material breach ([30]-day cure), bankruptcy, regulatory prohibition
- **For convenience**: If available; notice period and early termination fee
- **Post-termination**: Decommissioning, final settlement, survival of payment/indemnity
- **Dedication release**: Acreage releases on termination; specify tail obligations

### 6. Representations, Warranties & Covenants

**Producer**: Title/right to produce; no conflicting dedications; gas meets quality specs; compliance with production laws

**Gatherer**: Authority to operate; permits current; system capable of handling dedicated volumes

**Mutual**: Due organization; no conflicting agreements; environmental compliance; prudent industry practices

### 7. Indemnification & Insurance

- Mutual indemnity for each party's negligence/willful misconduct
- Knock-for-knock structure if applicable
- Address separately: environmental contamination, personal injury, property damage, third-party claims
- Insurance: CGL, auto, workers' comp, employer's liability, pollution liability — all at $[X]M minimums [VERIFY market standards]
- Carriers rated A- or better (A.M. Best); additional insured; 30-day cancellation notice

### 8. Force Majeure
- **Covered**: Acts of God, war, terrorism, strikes, governmental action, fire, flood, epidemic
- **Excluded**: Economic hardship, market changes, commodity prices, lack of profitability
- Prompt written notice with description and estimated duration; duty to mitigate
- Extended FM (>[6–12] months): either party may terminate without liability

### 9. Governing Law & Disputes
- Governing law: state where system primarily located
- Tiered: (1) executive negotiation [30 days]; (2) mediation [30 days]; (3) binding arbitration under AAA Commercial Rules [VERIFY current rules]
- Prevailing party fees if applicable; jury trial waiver

### 10. Miscellaneous
- Notices by physical address and email
- Assignment: consent required except affiliates or asset sales; runs with the land
- Entire agreement; written amendments only; severability; counterparts

### 11. Signature Blocks
- Entity-appropriate blocks with name/title/date
- Notary acknowledgment if recordable; e-signature compliance

## Guidelines

- **FERC jurisdiction**: Confirm jurisdictional vs. non-jurisdictional status — provisions vary significantly [VERIFY current FERC gathering exemption standards]
- **State PUC**: TX, WY, CO and others impose gathering-specific rules; confirm applicable state requirements
- **AAPL forms**: Reference AAPL model gathering agreement where applicable [VERIFY current editions]
- **Environmental**: Include SPCC, Clean Air Act, and state compliance covenants; address produced water if applicable
- **Dedications**: Confirm consistency with upstream lease, JOA, and mortgage/lien requirements — conflicts with senior liens are a common defect
- **Measurement**: Specify API MPMS chapter and GPA standard editions in definitions [VERIFY current citations]
- **Out-of-spec gas**: Address gatherer's right to reject, curtail, or treat at producer's cost
- All regulatory citations must be verified against current editions before execution

---
name: epc-contract
title: EPC Contract
description: Drafts turnkey Engineering, Procurement, and Construction (EPC) contracts for industrial facility projects. Covers scope of work, commercial terms, performance guarantees, risk allocation, warranties, and dispute resolution. Use when drafting EPC agreements, turnkey construction contracts, or energy infrastructure project contracts (power plants, petrochemical facilities, water treatment plants).
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/epc-contract
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: construction
language: en
---

# EPC Contract

Drafts a turnkey EPC contract establishing rights, obligations, risk allocations, and technical requirements between a project owner and contractor for design, procurement, construction, testing, and commissioning of an industrial facility.

## Prerequisites

Gather before drafting:

1. **Project description** — facility type, capacity, throughput specs, location
2. **Party details** — legal names, entity types, jurisdictions, addresses, authorized signatories
3. **Governing documents** — RFPs, term sheets, LOIs, precedent agreements
4. **Pricing structure** — lump-sum, GMP, cost-plus, or hybrid
5. **Schedule** — target milestones, NTP conditions, substantial/final completion dates
6. **Performance requirements** — output capacity, efficiency, emissions, availability guarantees
7. **Jurisdiction** — governing law, regulatory/permitting regime
8. **Insurance requirements** — owner's minimum coverage expectations

## Contract Sections

Draft all 14 sections in order.

### 1. Recitals & Parties

- **Owner**: legal name, entity type, jurisdiction, address, tax ID, authorized rep
- **Contractor**: same; if JV/consortium — lead contractor, liability structure (joint & several or allocated)
- **Recitals**: owner's objectives, contractor qualifications, turnkey intent

### 2. Definitions

Define at minimum:

| Term | Criteria |
|---|---|
| Substantial Completion | Work complete except punch list; testing passed; performance met; regulatory approvals obtained; O&M docs delivered |
| Final Completion | Punch list closed; all performance tests passed at guaranteed levels; reliability demo done; training complete; final documentation |
| Contract Price | Fixed amount, inclusions, adjustment mechanisms |
| Change Order | Written modification to scope, schedule, or price |
| Force Majeure | Natural disasters, war, epidemics, government action, non-party labor disputes |
| Defect | Non-conformance with specs, drawings, guarantees, or codes |
| Warranty Period | Commencement trigger and duration |

Include project-specific technical terms referencing industry standards (ASME, IEEE, ISA).

### 3. Scope of Work

**A. Engineering** — All disciplines (civil/structural, mechanical, electrical, I&C, process, environmental, safety); conceptual through detailed.

**B. Procurement** — Major equipment (turbines, generators, compressors, vessels, heat exchangers), bulk materials, spare parts, special tools. Identify owner-furnished items with interface requirements.

**C. Construction & Installation** — Site prep, civil, foundations, structural, mechanical/piping, electrical/instrumentation, insulation/painting/fireproofing. Reference applicable codes.

**D. Testing & Commissioning** — Factory acceptance → pre-commissioning → integrated systems → performance testing → reliability demo. Include owner witness rights and acceptance criteria.

**E. Ancillary** — Permitting (allocate owner vs. contractor), training (classroom + hands-on), documentation deliverables (design basis, as-builts, O&M manuals — specify format/schedule).

**F. Exclusions** — Land acquisition, off-site utilities to boundary, owner personnel, financing, owner-controlled insurance, owner permits.

### 4. Commercial Terms

**Contract Price**: Exact amount and currency. Pricing type (lump-sum/GMP/cost-plus/hybrid). Confirm all E, P, C, testing, commissioning, training, documentation included. Adjustments limited to owner changes, differing site conditions, force majeure, change in law.

**Payment Schedule**:

| Milestone | Typical % | Conditions |
|---|---|---|
| Advance payment | 5–10% | Advance payment guarantee required |
| Engineering milestones | Per deliverable | Basic/detailed design completion |
| Equipment delivery | Per item value | Delivery receipts |
| Construction progress | Monthly | Joint measurement/verification |
| Substantial Completion | Major tranche | Less retention |
| Final Completion | Balance + retention | All guarantees satisfied |

- **Retention**: 5–10%; partial release at Substantial Completion, balance at Final Completion; contractor may substitute bond/LC
- **Invoicing**: Submit within [X] days; owner review 15–30 days; payment within 30 days of approval; interest on late undisputed amounts
- **Taxes**: Allocate sales tax, VAT, customs duties, import taxes

### 5. Schedule

- **Commencement**: NTP conditions precedent (site access, permits, financing)
- **Duration**: Calendar days/months from NTP to Final Completion
- **Key milestones**: Design → PO awards → long-lead delivery → construction start → mechanical completion → commissioning → Substantial Completion → performance testing → Final Completion
- **Certification**: Contractor notice → owner inspection → completion certificate

**Delay Management**:

| Delay Type | Time Extension | Cost Recovery |
|---|---|---|
| Force majeure | Yes | No |
| Change in law | Yes | No |
| Government permit delays | Yes | No |
| Owner-caused delays | Yes | Yes |
| Owner scope changes | Yes | Yes |
| Differing site conditions | Yes | Yes |

- Notice: prompt written notice + cause + critical path impact + time request
- **Delay LDs**: Daily/weekly rate for late Substantial Completion; cap 5–15% of contract price
- **Early completion bonus** (optional): per day/week ahead of schedule

### 6. Performance Guarantees

**Guaranteed Parameters** (select applicable):

| Parameter | Value | Reference Conditions | Test Standard |
|---|---|---|---|
| Output capacity | [kW/units] | ISO or site ambient | ASME PTC |
| Efficiency/heat rate | [%/BTU/kWh] | Fuel spec, ambient | ASME PTC |
| Emissions | [g/unit] per pollutant | Operating conditions | EPA/regulatory |
| Availability | [%] | Defined period | Contract formula |

- Include correction curves for reference conditions
- Test protocol: timing, duration, valid runs, stability criteria, instrumentation, data recording
- Retest rights: optimization period; max retests specified

**Performance LDs**:

| Shortfall | LD Formula | Cap |
|---|---|---|
| Capacity | $/unit below guarantee | [X]% of contract price |
| Efficiency | PV of increased operating costs | [X]% of contract price |
| Emissions | Cost of additional controls | [X]% of contract price |

- Rejection threshold: shortfall exceeding [X]% → owner may reject facility

### 7. Change Management

- Formal written change order required before work begins (emergency exception with retroactive approval)
- Contractor proposal within 10–20 business days: scope, cost breakdown, markup (10–20% OH&P), schedule/CPM impact, effect on guarantees
- Pricing: lump-sum, unit price, T&M, or cost-plus
- Owner review: 15–30 days
- Disputed changes: contractor proceeds under directed change order; pricing resolved via dispute resolution
- Cumulative changes exceeding [X]% trigger renegotiation or termination-for-convenience rights

### 8. Indemnification & Liability

**Contractor indemnifies Owner** for: bodily injury/death, property damage, regulatory violations, IP infringement, environmental contamination, breach.

**Owner indemnifies Contractor** for: owner negligence/willful misconduct/breach; defects in owner-furnished items.

**Exceptions**: Claims from sole negligence of indemnified party. Joint negligence: comparative fault.

**Procedure**: Prompt notice → indemnifying party controls defense → cooperation → settlement limits.

**Liability caps**:
- Consequential damages mutually excluded (exceptions: gross negligence, willful misconduct, confidentiality, IP, environmental)
- Aggregate cap: contract price (or [X]x); uncapped: indemnity, IP, willful misconduct, fraud

### 9. Insurance

| Coverage | Minimum Limit | Requirements |
|---|---|---|
| CGL | $10–50M per occurrence/aggregate | Additional insured; primary & non-contributory |
| Workers' Comp | Statutory per jurisdiction | Employers' liability $1M |
| Auto Liability | $1M CSL | All owned/hired/non-owned |
| Professional Liability (E&O) | $5–25M per claim/aggregate | Claims-made with 3–5 year tail |
| Builder's Risk | Full replacement value | Specify owner vs. contractor placement |
| Marine Cargo | Full shipment value | If international; origin to site |
| Pollution Liability | Project-appropriate | If environmental risk |
| Umbrella/Excess | Project-appropriate | Above primary policies |

All policies: owner as additional insured, waiver of subrogation, 30-day cancellation notice, certificates before work starts.

### 10. Warranties

- **Scope**: All work free from defects in materials, workmanship, and design
- **Period**: 12–24 months from Substantial Completion; restarts for repaired/replaced items
- **Materials**: New unless specified; suitable for intended purpose
- **Pass-through**: Assign all manufacturer/supplier warranties to owner
- **Defect correction**: Written notice → repair within 24 hours (urgent) to 10 business days (non-urgent) → costs on contractor
- **Self-help**: If contractor fails to correct, owner may correct and charge contractor
- **Security**: Bond or LC, 5–10% of contract price; released on warranty expiration

### 11. Termination

| Trigger | By | Notice/Cure | Contractor Gets |
|---|---|---|---|
| Cause (abandonment, schedule failure, insolvency) | Owner | Written + 10–30 day cure | Work performed only; liable for excess costs |
| Convenience | Owner | Written notice | Work + materials + demobilization + OH (no profit on unperformed) |
| Owner default (non-payment, suspension, breach) | Contractor | Written + cure period | Work + costs + anticipated profit on full contract |
| Extended force majeure (>6 months) | Either | Written notice | Work + costs (no anticipated profit) |

### 12. Dispute Resolution

Tiered process:
1. **Negotiation** — Senior executives, 30 days
2. **Mediation** — Mutually acceptable mediator, 60 days
3. **Binding** — Arbitration (ICC/AAA; 1 or 3 arbitrators; specify seat/language) OR litigation (exclusive jurisdiction/venue)

- **Governing law**: [Jurisdiction], excluding conflicts-of-law. Exclude CISG if international.
- **Fees**: Each party bears own OR prevailing party recovers
- **Jury waiver**: Include if parties prefer bench trial

### 13. Administrative Provisions

- **Notices**: Written; delivery/courier/certified mail/email; effective on receipt
- **Assignment**: Contractor needs owner consent; owner assigns freely to affiliates/lenders
- **Boilerplate**: Entire agreement, amendments in writing, severability, non-waiver, mutual confidentiality, force majeure (notice + mitigation)

### 14. Execution

Signature blocks: entity name, signature, printed name, title, date. Add notarization/witness if required by governing law.

## Pitfalls

- Confirm pricing structure before drafting commercial terms
- Mark uncertain statutory/regulatory citations with [VERIFY] for the specific jurisdiction
- Scale insurance minimums to project size and risk profile
- LD rates must reflect reasonable pre-estimates of actual damages to be enforceable
- Performance guarantees and test protocols are project-specific — confirm with user before finalizing
- For JV/consortium contractors, explicitly address lead designation and liability allocation
- Flag gaps in provided information — never assume critical business terms
- Verify internal consistency of cross-references, defined terms, and exhibit/schedule references
- For international projects: address currency, CISG exclusion, arbitration seat, language, import/export compliance

---
name: kb-construction-fidic-mena-sboghossian
title: Knowledge Pack — FIDIC Construction Contracts in MENA
description: Use when advising on construction contracts using FIDIC forms in MENA, including contract book selection (Red/Yellow/Silver/Gold), MENA-specific clause adaptations (currency, force majeure, time-bar enforceability, liquidated damages, performance bonds), Dispute Adjudication Boards (DABs), and arbitration of FIDIC disputes. Covers Saudi Arabia (NEOM/Vision 2030 projects), UAE, Lebanon, and Egypt with jurisdiction-specific civil-law traps.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/kb/kb-construction-fidic-mena
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: construction
language: en
---

# Knowledge Pack — FIDIC Construction Contracts in MENA

## Scope

This pack covers the FIDIC suite of standard construction contracts as used in MENA infrastructure and building projects. It is the primary reference for:

- Selecting the right FIDIC contract book for a project type
- Understanding the 1999 vs 2017 editions and their differences
- Identifying MENA-specific adaptations to standard FIDIC terms
- Managing critical risk clauses: currency, force majeure, time-bar, LDs, variation
- Dispute Adjudication Boards and arbitration of construction disputes
- Project security instruments (performance bonds, advance payment bonds, retention)

---

## FIDIC — overview

The **Fédération Internationale des Ingénieurs-Conseils** (International Federation of Consulting Engineers) publishes a suite of model construction contracts used globally. In MENA, FIDIC contracts are the dominant framework for infrastructure, energy, transport, and major building projects.

**Two editions in active use:**

| Edition | Status |
|---|---|
| **1999 (Rainbow Suite)** | Widely used; familiar to MENA contractors and employers; extensive case law |
| **2017 (2nd Edition)** | Modernized; improved Engineer role; more prescriptive notice requirements; preferred by multilateral development banks and newer megaprojects |

---

## FIDIC contract books

| Book | Name | Best for |
|---|---|---|
| **Red Book** (1999/2017) | Construction | Traditional: employer designs, contractor builds; most common for civil + buildings |
| **Yellow Book** (1999/2017) | Plant + Design-Build | Contractor designs + builds; plant, process + M&E-heavy projects |
| **Silver Book** (1999/2017) | EPC / Turnkey | Maximum risk transfer to contractor; fixed price + time; used for energy + industrial |
| **Green Book** | Short Form | Smaller, simpler projects; abbreviated provisions |
| **Pink Book** | MDB Harmonised | Multilateral development bank-financed projects; includes MDB-specific payment and procurement rules |
| **Gold Book** (2008) | Design, Build + Operate (DBO) | 20-year concession + operation period; PPP-lite model |

**MENA usage pattern**: Red Book dominates for buildings and civil works; Yellow Book for M&E-heavy and design-build; Silver Book for energy sector EPC. The 2017 editions are increasingly specified on Saudi Vision 2030 megaprojects.

---

## MENA-specific considerations

### Currency risk

Currency clauses are critical in MENA construction:

- **USD denomination**: preferred for international components of MENA megaprojects
- **Dual-currency**: employer pays in local currency (SAR, AED, EGP, LBP) with a USD component for imported materials/equipment
- **Egypt EGP volatility**: contracts involving Egyptian pounds need escalation clauses or forex adjustment mechanisms — EGP has devalued significantly
- **Lebanon LBP crisis**: post-2019 Lebanon construction contracts require careful currency protection clauses; standard FIDIC LBP-denominated contracts have been severely affected
- **Forex index clauses**: some MENA contracts include adjustment provisions tied to official exchange rates for imported goods

### Force majeure

FIDIC 1999 Sub-Clause 19 / 2017 Sub-Clause 18 — force majeure / exceptional events:

- MENA adaptations commonly add: pandemic events, sanctions events, war in specified countries
- **Notice**: strict timing of force majeure notice (typically 14 days in 1999; 28 days in 2017 for some claims) — failure to give notice can bar the claim
- **KSA-specific**: VAT / Zakat changes may be added as employer-risk events

### Variation procedure

FIDIC's variation mechanism (Sub-Clause 13) typically requires Engineer instruction for variations. In MENA government contracts:

- Additional approval steps required (Ministry of Finance, contracting authority, sometimes Council of Ministers for large scope increases)
- These approval procedures must be reflected in the contract — a FIDIC standard variation instruction from the Engineer is insufficient if the employer's internal approvals have not been obtained
- Contractors must track actual approvals obtained, not just Engineer instructions

### Time-bar provisions

FIDIC 1999 Sub-Clause 20.1 / 2017 Sub-Clause 20.2 require notification of claims within 28 days of the event giving rise to the claim. Failure to notify bars the claim.

**Civil-law enforceability question:**

In civil-law jurisdictions (UAE onshore, Lebanon, Egypt, KSA), strict contractual time-bars may be treated as:
- Enforceable limitations of liability — generally upheld
- OR as procedural conditions precedent to liability — courts may apply these strictly

However, some civil-law courts in MENA have declined to apply time-bar provisions where:
- The employer was already aware of the claim
- The non-compliance caused no prejudice
- The time-bar was deemed unconscionable or against public policy

**Best practice**: Comply with FIDIC time-bars strictly. Do not rely on a court declining to enforce.

### Liquidated damages (LDs)

FIDIC Sub-Clause 8.7 (1999) / Sub-Clause 8.8 (2017) — LDs for delay.

**Civil-law treatment (UAE, Lebanon, Egypt, France-influenced systems):**

Civil-law courts have inherent power to **reduce** liquidated damages that are manifestly disproportionate to actual harm. This is an important distinction from common-law (DIFC, ADGM, UK) where agreed LDs are generally enforced without reduction.

- **UAE**: Federal Civil Transactions Law Art. 390 explicitly allows courts to reduce LDs
- **Lebanon**: Code of Obligations and Contracts Art. 266 — similar reduction power
- **Egypt**: Civil Code Art. 224 — court may reduce LDs if contractor proves actual damages were less

**Practical implications**:
- Do not over-specify LDs to the point of appearing punitive — this increases reduction risk
- Document actual harm carefully during delay period to support enforcement
- For DIFC/ADGM-seated contracts: civil-law reduction risk is reduced (common-law approach)

### Penalty vs LDs distinction

Civil-law systems distinguish between:
- **Liquidated damages** (clause pénale): pre-estimated genuine pre-estimate of harm — generally enforceable
- **Penalty clause**: punitive; designed to compel performance rather than compensate — courts may reduce or even refuse to enforce

MENA civil-law courts may characterize an LD clause as a penalty if: the amount is grossly disproportionate to likely harm, or if the drafting reveals a punitive intent.

### Performance bonds + retention

| Instrument | Typical MENA range | Notes |
|---|---|---|
| Performance bond | 10–15% of contract value | Demand or conditional; on-demand preferred by employers |
| Advance payment bond | 100% of advance (typically 10–20% of contract) | Released pro-rata as advance recovered |
| Retention | 5–10% of certified payment | Retention bond alternative common |

**On-demand bonds in MENA**: Employers often insist on unconditional demand bonds (calling without proving breach). Contractors should negotiate for "conditional on award" language, or at least a period for dispute resolution before calling.

### Limitation of liability

Standard FIDIC does not cap contractor liability — employers should consider specifying caps (e.g., 100% of contract price for all claims except fraud, willful misconduct, and personal injury).

### Insurance

- Local insurance requirements: MENA countries typically require insurance placed with locally licensed insurers or reinsured locally
- Reinforce insurance obligations in sub-contracts (pass-through)
- Professional indemnity: increasingly required for design-and-build contractors

---

## Saudi Arabia — specific notes

### Major projects

Saudi Arabia's Vision 2030 program includes among the world's largest construction projects:
- **NEOM** (Trojena, NEOM Bay, The Line, Oxagon)
- **Diriyah Gate** (heritage + tourism)
- **Red Sea Project** (island tourism)
- **Qiddiya** (entertainment)

These projects use bespoke FIDIC-derived forms, often the 2017 edition with Saudi-specific annexes.

### ARAMCO and SABIC

Saudi ARAMCO and SABIC maintain their own standard forms of contract (FIDIC-derived but substantially modified). Contractors on these projects must understand the deviations from standard FIDIC, which affect: pricing mechanisms, scope, variation, security, and dispute resolution.

### Saudization (Nitaqat)

Construction contracts for Saudi public sector projects include Saudization obligations. Contractors must meet Saudi national hire percentages throughout the project.

### Dispute resolution

- DAB (Dispute Adjudication Board) is standard in major FIDIC contracts
- Saudi public sector disputes may also involve mandatory reference to government dispute committees before arbitration
- DIAC and ICC arbitration both used for Saudi construction disputes

---

## UAE — specific notes

Dubai and Abu Dhabi government entities use FIDIC with UAE-specific amendments:

- Abu Dhabi Department of Infrastructure and Transport (DIT) — uses FIDIC variants
- Dubai Roads and Transport Authority, Roads Authority — FIDIC-derived forms
- DIAC arbitration is preferred for UAE construction disputes
- UAE courts have addressed FIDIC time-bar and LDs enforceability in multiple judgments

---

## Lebanon — specific notes

Pre-crisis: FIDIC was the standard for major infrastructure projects (CDR — Council for Development and Reconstruction projects, World Bank and EBRD-financed).

Post-crisis (2019+):
- Currency clauses in LBP are materially affected by the collapse of the LBP
- CDR projects on hold pending economic recovery
- New projects require careful currency structuring (often USD-only or EUR-only)
- Standard FIDIC less common for post-crisis private-sector projects; project-specific drafting prevalent

---

## Egypt — specific notes

- International-financed projects (World Bank, IFC, AfDB): Pink Book (MDB Harmonised) used
- Government projects: Egyptian Public Works Contract (Arabic form) common; FIDIC used for larger international projects
- EGP currency volatility: consider forex adjustment clauses for multi-year projects
- Egyptian courts have addressed FIDIC LDs enforceability; generally enforceable unless manifestly excessive

---

## Disputes — FIDIC dispute resolution chain

**FIDIC 2017 has a mandatory multi-step process:**

1. **Engineer decision** — parties refer dispute to Engineer; Engineer must give fair determination within 28 days
2. **DAAB (Dispute Avoidance / Adjudication Board)** — 84 days to decide (2017 edition added "avoidance" element — standing DAAB meets regularly, not just for disputes)
3. **NOD (Notice of Dissatisfaction)** — party dissatisfied with DAAB decision issues NOD within 28 days
4. **Amicable settlement** — 28-day period for negotiation
5. **Arbitration** — if no settlement; DAAB decision becomes an interim binding obligation (even if disputed in arbitration) unless reversed by arbitral tribunal

**Key trap**: Failure to comply with a DAAB decision (even a disputed one) is an immediate breach. The tribunal will almost always enforce the DAAB decision as an interim obligation pending final award.

### Arbitration seats for FIDIC in MENA

| Project type | Common seat |
|---|---|
| UAE projects | Dubai (DIFC) / DIAC |
| Saudi projects | ICC (Paris) or DIAC |
| International-financed | ICC or LCIA |
| Lebanese pre-crisis | ICC |

---

## How to use this pack

Load this pack when the user:
- Is negotiating a FIDIC-based construction contract in MENA
- Needs to review or advise on MENA-specific FIDIC amendments
- Has a time-bar, variation, force majeure, or LD dispute on a FIDIC project
- Is advising on a DAB/DAAB decision or enforcement
- Is structuring performance security (bonds, retention) for a MENA project

## Caveats & currency

FIDIC publishes guidance notes and errata that update interpretation of the 2017 edition. Jurisdiction-specific public works contract forms in UAE and KSA evolve with each major project program. Check current NEOM/CDR/Abu Dhabi government standard forms for the latest versions. DIAC Rules 2022 are the current applicable rules for UAE arbitration.

## Related skills

- [[kb-arbitration-diac]] — DIAC arbitration for UAE construction disputes
- [[kb-arbitration-icc]] — ICC arbitration for international construction disputes
- [[draft-construction-contract]] — drafting construction contract provisions
- [[review-commercial-contract]] — reviewing a construction contract for risk allocation

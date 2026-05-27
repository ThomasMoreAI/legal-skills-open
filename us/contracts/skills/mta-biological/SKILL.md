---
name: mta-biological
title: Material Transfer Agreement — Biological Materials
description: Drafts Material Transfer Agreements for biological materials between research institutions and commercial entities. Covers material characterization (BSL levels, select agents, GMOs), permitted use, IP allocation, publication rights, and regulatory compliance (NIH Guidelines, Bayh-Dole, ITAR/EAR, select agent regulations). Use when drafting MTAs, biological material transfer terms, or research collaboration agreements involving biological specimens.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/mta-biological
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: contracts
language: en
---

# Material Transfer Agreement — Biological Materials

Drafts MTAs governing transfer of biological materials between research institutions and/or commercial entities, balancing scientific collaboration with IP protection, biosafety compliance, and regulatory requirements. Reference the NIH UBMTA as baseline; deviate only where parties' needs require it.

## Prerequisites

Gather before drafting:

1. **Parties** — legal names, addresses, departments, signatories, institutional type (university/foundation/corporate)
2. **Material** — scientific nomenclature, strain/cell line IDs (ATCC, RRID), physical form, quantity, BSL classification, select agent status, GMO details
3. **Upstream restrictions** — prior MTAs or third-party IP encumbrances
4. **Research scope** — project description, grant number, funding source (federal/private), PI names
5. **Regulatory status** — export control classification (ITAR/EAR), IBC approvals, IACUC/IRB if applicable
6. **Commercial intent** — whether recipient anticipates commercialization of derivatives

## Quick Start

For a standard academic-to-academic transfer of non-select-agent, non-GMO materials under federal funding:

- Start from UBMTA framework
- Confirm Bayh-Dole compliance (non-negotiable for federal funding)
- Use research-only permitted use with prohibition on commercial use and third-party transfer
- Apply three-tier IP allocation (background → Provider retains; materials → Provider; new inventions → inventive party)
- Include 30-day publication review period (no veto right)
- Add standard AS-IS disclaimers in conspicuous format

## Drafting Workflow

### 1. Parties & Authority

- Full legal name, address, department, authorized signatory with binding authority
- PI is agent of institution (not a party); institution bears compliance responsibility
- Public institutions: confirm statutory contracting authority and sovereign immunity considerations
- Conditions precedent: IBC approval, export control clearance, conflict-of-interest review
- International transfers: allocate responsibility for foreign government approvals

### 2. Material Description

Draft with scientific precision:

- Taxonomy (genus/species/strain), identifiers (ATCC, RRID), physical form, storage conditions
- Biosafety: BSL-1 through BSL-4 classification and containment requirements
- Select agents: confirm both parties' CDC/USDA registration if applicable
- GMO status: nature of modifications, NIH Guidelines compliance, IBC approvals
- Encumbrances: upstream MTA restrictions, patents covering materials
- Hazard disclosures: known risks, SDS references, required safety protocols

### 3. Transfer Logistics

- Shipping: IATA-compliant packaging, DOT hazmat compliance, temperature control (dry ice/LN2/refrigerated)
- Cost allocation: provider-paid, recipient-invoiced, or recipient-arranged
- Timeline: conditions before shipment (signed MTA, permits); receipt inspection within [X] days
- Export controls: ITAR/EAR/OFAC screening; allocate license responsibility
- International: customs invoices, dangerous goods declarations, import permits, phytosanitary certificates

### 4. Permitted Use & Restrictions

- Define permitted use by specific project/protocol (exhibit) or field of use
- Prohibit without consent: commercial use, third-party transfer, human subjects research, germline modification
- Derivatives ownership: unmodified progeny → Provider retains; modifications with inventive contribution → Recipient owns with Provider license-back option
- Third-party transfer of derivatives requires Provider consent with equivalent MTA restrictions

### 5. Confidentiality & Publication

- Scope: material properties, performance data, unpublished research, know-how
- Standard exceptions: public knowledge, independent development, third-party receipt, compelled disclosure
- Duration: [X] years post-termination (typically 3–5)
- Publication review: Provider gets 30–60 days to review; may request removal of confidential info; max 90-day patent-filing delay; Provider may NOT veto publication

### 6. Intellectual Property

Three-tier allocation:

| IP Category | Owner | Other Party |
|---|---|---|
| Background IP | Original owner | License only if expressly granted |
| Materials & unmodified progeny | Provider | Recipient use license within permitted scope |
| New inventions | Inventive party (sole/joint) | Option to negotiate license within [X] days |

- **Bayh-Dole** (federal funding): institution retains title; government gets non-exclusive license + march-in rights; reporting obligations to agency
- **Reach-through rights**: draft narrowly; NIH discourages broad reach-through on NIH-funded materials

### 7. Warranties & Liability

- Limited warranties: right to transfer, materials match description, no known contamination
- Disclaimers (CONSPICUOUS — ALL CAPS or bold per UCC § 2-316): AS-IS; no warranty of merchantability, fitness, or non-infringement
- Liability: direct damages only; exclude consequential/incidental/punitive; optional monetary cap
- Carve-outs: gross negligence, willful misconduct, confidentiality breach, IP infringement
- Public institutions: confirm sovereign immunity constraints

### 8. Indemnification & Insurance

- Mutual indemnification: Recipient covers use/handling/disposal claims; Provider covers undisclosed defects and willful misconduct
- Procedure: prompt written notice → indemnitor assumes defense → no adverse settlement without consent
- Insurance: CGL, professional liability, property coverage; Provider as additional insured for high-risk materials

### 9. Term & Termination

- Term: fixed (project/grant duration) or indefinite with termination rights
- Convenience: 30–90 days written notice
- Cause: material breach + 30-day cure period
- Auto-termination: bankruptcy, loss of regulatory approvals, legal prohibition
- Post-termination: return or destroy materials + written certification; archival samples only for regulatory retention
- Surviving: confidentiality, IP, indemnification, disclaimers, dispute resolution

### 10. Regulatory Compliance

Include affirmative obligations for applicable frameworks:

- **NIH Guidelines** — IBC review, NIH registration, containment levels for recombinant/synthetic nucleic acids
- **Select Agent Program** — CDC/USDA registration, 42 CFR Part 73 transfer compliance [VERIFY]
- **Export controls** — ITAR (22 CFR 120–130), EAR (15 CFR 730–774), OFAC screening [VERIFY]
- **Animal welfare** — IACUC approval if animal-derived or animal use
- **Human subjects** — Common Rule (45 CFR 46), HIPAA, IRB approval if human-derived [VERIFY]
- **Environmental** — waste disposal, spill response, decontamination protocols
- **Sanctions** — representations that neither party is in a sanctioned country or on restricted lists

### 11. Governing Law & Disputes

Tiered resolution (recommended for institutional parties):

1. Senior official escalation (TTO directors / VP Research) — 30 days
2. Mediation (JAMS/AAA) — 60-day window, cost-sharing
3. Litigation (preferred for IP/injunctive relief; specify venue) OR arbitration (faster for contract disputes; carve out injunctive relief)

Specify prevailing-party attorneys' fees if desired.

### 12. Boilerplate & Execution

Amendments (written/signed), assignment (consent required; M&A exception), notices (addresses/methods/timing), severability, integration, waiver (written only), counterparts with e-signatures, signature blocks, exhibits (material description, research protocol, destruction certification).

## Pitfalls

1. **Select agents** — verify current HHS/USDA Select Agent and Toxin List; non-compliance carries criminal penalties
2. **Export controls** — do not assume biological materials are exempt; many organisms/toxins are controlled under EAR or ITAR
3. **Federal funding** — always confirm funding source; Bayh-Dole compliance is mandatory and non-waivable
4. **Publication veto** — academic institutions will reject; limit Provider to review-and-delay only
5. **Reach-through royalties** — controversial in academia; NIH policy discourages broad reach-through on funded materials
6. **Disclaimer format** — UCC § 2-316 requires conspicuous language; use ALL CAPS or bold
7. **State law variations** — public university contracting authority, sovereign immunity, and indemnification restrictions vary by state
8. **Dual-use research of concern (DURC)** — flag qualifying materials; additional institutional review may be required under USG DURC policy
9. **Statutory citations** — mark all CFR/USC references with [VERIFY] for confirmation against current regulations

---

Key changes from the original:

- **Removed `tags`** from frontmatter (not part of the spec)
- **Trimmed description** to be more concise while keeping trigger keywords
- **Added Quick Start** section for the most common scenario (academic-to-academic UBMTA-based transfer)
- **Consolidated Output Structure → Drafting Workflow** with bullet lists replacing verbose tables throughout (sections 1, 3, 7–9, 12)
- **Renamed Guidelines → Pitfalls** for clarity, trimmed from 10 to 9 items by merging the UBMTA reference into the overview
- **Reduced from 220 to ~140 lines** while preserving all domain-critical content (BSL levels, select agents, Bayh-Dole, ITAR/EAR, three-tier IP, DURC, UCC disclaimers)

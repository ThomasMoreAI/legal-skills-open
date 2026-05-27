---
name: healthcare-services-agreement
title: Professional Services Agreement — Healthcare
description: Drafts professional services agreements for healthcare providers and clients, covering HIPAA/HITECH compliance, BAA requirements, Anti-Kickback and Stark Law guardrails, credentialing warranties, malpractice insurance mandates, and patient care continuity on termination. Use when drafting healthcare provider contracts, medical services agreements, physician independent contractor agreements, or healthcare consulting engagements.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/healthcare-services-agreement
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: healthcare
language: en
---

# Professional Services Agreement — Healthcare

Drafts a healthcare-specific professional services agreement balancing clinical autonomy with regulatory compliance and appropriate risk allocation.

## Prerequisites

1. **Party information** — legal names, entity types, tax IDs, signing authority
2. **Provider credentials** — license numbers, NPI, DEA (if applicable), board certifications, hospital privileges
3. **Service scope** — specialties, procedures, locations (in-person / telehealth), volume expectations, on-call requirements
4. **Compensation terms** — rate structure, billing responsibility (provider-direct vs. client-billed), expense policy
5. **Insurance details** — malpractice policy type (claims-made vs. occurrence), coverage limits, CGL policy
6. **HIPAA role designation** — Covered Entity, Business Associate, or workforce member relative to client
7. **Governing jurisdiction** — state(s) where services will be rendered

If any prerequisite is missing, pause and ask — do not assume or fill gaps.

## Quick Start

1. Gather all prerequisites and uploaded documents
2. Draft articles in order (parties → scope → compensation → term → HIPAA → warranties → indemnification → insurance → disputes → general)
3. Attach BAA as exhibit if BA relationship exists
4. Flag all jurisdiction-specific rules with `[VERIFY]`
5. Confirm Anti-Kickback / Stark compliance on compensation structure
6. Verify provider OIG exclusion status before finalizing

## Governing Law

| Authority | Citation |
|---|---|
| Anti-Kickback Statute | 42 U.S.C. § 1320a-7b [VERIFY] |
| Stark Law (self-referral) | 42 U.S.C. § 1395nn [VERIFY] |
| HIPAA Privacy/Security | 45 CFR Parts 160, 164 |
| BAA requirement | 45 CFR § 164.504(e) |
| HITECH breach notification | No later than 60 days, without unreasonable delay |

## Output Structure

### 1. Parties & Recitals

| Field | Provider | Client |
|---|---|---|
| Legal name & entity type | ✓ | ✓ |
| Principal address | ✓ | ✓ |
| Tax ID / EIN | ✓ | ✓ |
| Credentials (license #, NPI, DEA) | ✓ | — |
| Capacity (individual / PC / LLC / group) | ✓ | — |
| Signing authority & title | ✓ | ✓ |

State explicitly: **independent contractor** — not employment, partnership, or joint venture.

### 2. Scope of Services

- Enumerate services with clinical specificity; reference applicable **standard of care**
- State locations and modalities (on-site, telehealth, client facility)
- Define scheduling, on-call obligations, response-time expectations
- List **exclusions** — services NOT covered
- Address emergency protocols and credentialing/privileging for facility-based services
- Experimental/non-standard procedures require separate informed consent provisions

### 3. Compensation & Billing

- Rate structure: fee-for-service / hourly / per-patient / retainer / hybrid
- Billing cycle, invoice format, payment terms, accepted methods
- Assign billing responsibility (patients and/or third-party payers)
- Reimbursable expenses with pre-approval process
- Rate adjustment mechanism: notice period, cap, CPI index if applicable

**Regulatory guardrail:** Compensation must be FMV, commercially reasonable, and not vary with referral volume or value. Include affirmative Anti-Kickback and Stark compliance representations.

### 4. Term & Termination

| Provision | Standard |
|---|---|
| Initial term | Fixed dates or rolling |
| Auto-renewal | Opt-out notice 60–90 days |
| Without cause | 90–180 days' written notice |
| For cause (with cure) | 30-day notice and cure period |

**Immediate termination triggers** (no cure): license loss/suspension, DEA revocation, federal program exclusion, felony conviction/indictment, professional misconduct finding, insurance lapse, material HIPAA breach.

**Transition obligations:** continued service during notice period, patient care continuity plan and warm handoff, medical records transfer per state retention laws, return of property/credentials/access, pro-rata compensation.

### 5. HIPAA & Confidentiality

1. Designate HIPAA roles — Covered Entity vs. BA vs. workforce member
2. If BA relationship: attach **BAA** as exhibit per 45 CFR § 164.504(e)
3. BAA must address: permitted uses/disclosures, safeguards (administrative/physical/technical), breach notification timeline, subcontractor flow-down, audit rights, PHI return/destruction on termination
4. Non-HIPAA confidentiality — survival: indefinite for PHI; 3–5 years for business information

### 6. Representations & Warranties

**Provider:** unrestricted license(s), DEA registration (if prescribing), board certification (if claimed), not OIG-excluded, no pending discipline/claims impairing performance, disclosure of prior discipline, state practice act compliance, immediate notification if any warranty becomes untrue.

**Client:** authority to contract, facility licenses/accreditations maintained, compliance with applicable healthcare regulations.

### 7. Indemnification

| Indemnifying Party | Covers |
|---|---|
| Provider | Professional negligence, standard-of-care failures, regulatory violations, confidentiality breach |
| Client | Client negligence, defective equipment/facilities, license/accreditation failures, breach of obligations |

Scope: damages, settlements, judgments, attorneys' fees. Procedure: prompt notice → cooperation → mutual consent for settlements. Optional liability cap (exclude willful misconduct, gross negligence, HIPAA violations).

### 8. Insurance

| Coverage | Minimum Limits | Notes |
|---|---|---|
| Professional liability | $1M / $3M (adjust for high-risk specialties) | Claims-made: require tail coverage on termination |
| Commercial general liability | $1M / $2M | |
| Cyber liability | Per risk profile | Required if handling ePHI |
| Workers' compensation | Statutory | If provider has employees |

Client named as additional insured. Certificates due before services commence and at renewal. 30 days' notice of cancellation/material change. Insurance minimums do not cap indemnification.

### 9. Dispute Resolution

1. Good-faith negotiation — 30 days
2. Mediation (healthcare-experienced mediator) — costs split
3. Binding arbitration (AAA Healthcare Rules) or litigation

Carve-out: emergency injunctive relief for confidentiality breaches or irreparable harm. Governing law: state where services are primarily rendered.

### 10. General Provisions

Severability, written amendments only, notice methods and deemed-receipt rules, assignment restrictions (carve-out for successors/affiliates), entire agreement, no implied waiver, force majeure (**patient care obligations not excused**), survival (confidentiality, indemnification, payment, insurance tail), counterparts and e-signatures.

### Signature Block

Each party: signature line, printed name, title, date. Confirm signatory has binding authority.

## Pitfalls & Checks

- **Anti-Kickback / Stark compliance is non-negotiable** — FMV, fixed in advance, not tied to referral volume
- Confirm OIG exclusion status before finalizing
- BAA is mandatory if BA relationship exists — omission creates HIPAA liability for both parties
- Claims-made policies without tail coverage create a gap — always require tail on termination
- State medical practice acts vary significantly — verify scope-of-practice and corporate-practice-of-medicine restrictions [VERIFY]
- Telehealth services require multi-state licensure analysis and state-specific telehealth rules [VERIFY]
- Patient care continuity on termination is an ethical obligation (AMA guidance + state abandonment rules), not merely contractual
- Non-compete clauses: confirm enforceability under applicable state law before including (many states restrict physician non-competes) [VERIFY]

---

Key changes from the original:

- **Removed `tags`** from frontmatter (not used in the rewritten skill pattern)
- **Added Quick Start** — 6-step actionable workflow visible at a glance
- **Added Governing Law table** — centralizes regulatory citations with `[VERIFY]` tags
- **Condensed Articles 6 (Warranties)** from verbose checklists to inline prose — same content, fewer tokens
- **Condensed Article 7 (Indemnification)** — merged procedure bullets into a single line
- **Condensed Article 10 (General Provisions)** — single paragraph instead of 9 separate bullet points
- **Renamed "Guidelines" → "Pitfalls & Checks"** — matches codebase convention
- **Added "pause and ask" instruction** in Prerequisites to prevent gap-filling
- **Reduced from 187 lines → ~140 lines** while preserving all substantive legal content

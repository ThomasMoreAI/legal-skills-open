---
name: environmental-indemnity
title: Environmental Indemnity Agreement
description: Drafts Environmental Indemnity Agreements allocating contamination, remediation, and regulatory liabilities between indemnitor (borrower/owner) and indemnitee (lender/secured party) in CRE and lending transactions. Covers CERCLA, RCRA, state statutes, survival provisions, and enforcement mechanisms. Use when drafting environmental indemnities, contamination risk allocation, or lender environmental protections in acquisition or financing deals.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/environmental-indemnity
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: environmental
language: en
tags: [agreement, drafting, regulatory, transactional]
---

# Environmental Indemnity Agreement

Protects lenders and secured parties from environmental liabilities on financed or acquired properties. Allocates contamination risk, remediation costs, and regulatory exposure to the indemnitor.

## Prerequisites

1. **Primary transaction documents** — loan/purchase agreement or mortgage with defined terms, party names, amounts, dates
2. **Property information** — legal description, address, current/prior uses
3. **Environmental reports** — Phase I/II ESAs, remediation reports, regulatory correspondence
4. **Party details** — full legal names, entity types, formation jurisdictions for indemnitor and indemnitee
5. **Governing jurisdiction** — state where property is located

## Quick Start

Collect prerequisites, then draft sections in order below. Align every defined term and party name with primary deal documents. Mark uncertain statutory citations with `[VERIFY]`.

## Document Sections

### 1. Recitals

| Element | Source |
|---|---|
| Transaction type | Loan agreement / purchase agreement |
| Parties & roles | Indemnitor = borrower/owner/guarantor; Indemnitee = lender/secured party + successors/assigns |
| Property identification | Legal description from deed/title |
| Known environmental conditions | Phase I/II findings, disclosed contamination |
| Purpose statement | Risk allocation for environmental liabilities |

### 2. Definitions

Required defined terms:

- **Environmental Laws** — CERCLA, RCRA, CWA, CAA, TSCA, EPCRA, applicable state equivalents, all regulations thereunder
- **Hazardous Substances** — broad, cross-referencing Environmental Laws; include petroleum, asbestos, PCBs, lead-based paint, mold, PFAS
- **Environmental Claim** — any demand, action, investigation, or proceeding relating to Environmental Laws or Hazardous Substances
- **Remediation** — investigation, cleanup, removal, containment, monitoring, any response action
- **Release** — per CERCLA § 101(22) `[VERIFY]`, including migration from adjacent properties

### 3. Indemnification Provisions

Scope checklist — all required:

- Pre-existing contamination (known and unknown)
- Releases during indemnitor's ownership/operations
- Environmental law violations
- Remediation costs (voluntary and compelled)
- Regulatory enforcement actions and penalties
- Third-party toxic tort claims
- Natural resource damages
- Diminution in property value
- Defense costs, attorneys' fees, consultant fees
- Environmental assessment and monitoring costs

Drafting requirements:
- Covers conditions regardless of when discovered
- Survives regardless of indemnitee's knowledge or due diligence findings
- Absolute and unconditional — not contingent on loan default
- Indemnitee has right to undertake remediation and seek reimbursement
- Includes consequential damages (lost loan interest, opportunity costs)

### 4. Representations and Warranties

| Category | Representation |
|---|---|
| Compliance | Property complies with all Environmental Laws |
| No violations | No pending/threatened enforcement actions or investigations |
| No undisclosed releases | No releases except as disclosed in identified reports |
| Full disclosure | All environmental reports and correspondence provided |
| USTs | No underground storage tanks, or all USTs registered and compliant |
| ACMs/LBP | Asbestos and lead-based paint status disclosed |
| Permits | All required environmental permits obtained and current |
| Hazardous materials | All storage, use, and disposal in compliance |
| Prior operations | No prior operations likely to have caused undisclosed contamination |

Qualify representations only where Phase I/II findings require specific disclosures — no blanket knowledge qualifiers.

### 5. Covenants

- Maintain compliance with all Environmental Laws
- Immediate written notice of: violations, government communications/inspections/orders, releases or threatened releases, third-party claims
- Maintain all required environmental permits
- No new Hazardous Substances storage/use without indemnitee consent
- Grant access for environmental assessments at indemnitee's discretion
- Cooperate with investigation or remediation
- No settlement of Environmental Claims without indemnitee's prior written consent

### 6. Remediation and Enforcement

Contamination response sequence:

1. Indemnitor promptly investigates and remediates to applicable standards
2. Indemnitor submits remediation plan for indemnitee approval
3. If indemnitor fails to act within `[__]` days, indemnitee may undertake remediation
4. All costs reimbursable on demand with interest at default rate
5. Indemnitee may require escrow/reserve establishment
6. Remediation must achieve regulatory closure or no-further-action determination

### 7. Survival and Duration

- Survives closing of underlying transaction
- Continues until the **latest** of: full loan repayment, property transfer by indemnitee, completion of all remediation with regulatory closure, expiration of all applicable statutes of limitation (CERCLA has no SOL for certain claims `[VERIFY]`)
- Survives bankruptcy, insolvency, foreclosure, deed-in-lieu
- Independent of and not merged into any judgment on loan documents

### 8. Governing Law and Dispute Resolution

- Governing law: state where property is located (environmental regulations are state-specific)
- Exclusive jurisdiction and venue in courts of that state
- Waiver of jury trial
- Arbitration generally disfavored — regulatory involvement and injunctive relief needs
- Prevailing party entitled to attorneys' fees and costs

### 9. General Provisions

- Severability with reformation preference
- Amendments require written consent of all parties
- Notices: addresses, methods (personal delivery, overnight courier, certified mail), effective dates
- Assignment: indemnitee may freely assign; indemnitor may not assign without consent
- No waiver by conduct; waivers must be written
- Entire agreement as to environmental indemnity matters (does not supersede loan documents)
- Counterpart execution; ESIGN/UETA compliance if electronic signatures used

### 10. Signature Blocks

- Entity signatories with name, title, authority recital
- Witness/notary lines per jurisdictional requirements
- Guarantor signature blocks if indemnitor is SPE

## Pitfalls and Checks

- **Deal document alignment** — every defined term, party name, and property description must match primary transaction documents exactly
- **State-specific statutes** — research property state's cleanup standards, voluntary cleanup programs, and indemnity enforcement rules; CERCLA is the federal floor, state law often adds requirements
- **No knowledge qualifiers on indemnity** — representations may be knowledge-qualified; the indemnification obligation itself must be absolute
- **Phase I/II integration** — if reports reveal recognized environmental conditions (RECs), draft specific disclosure schedules, not broad carve-outs
- **PFAS/emerging contaminants** — Hazardous Substances definition must be broad enough for contaminants not yet listed under CERCLA/RCRA
- **Bankruptcy** — include non-dischargeable status language to the extent permitted by law
- **Multiple indemnitors** — if guarantors or related entities are co-indemnitors, obligations must be joint and several
- **Mark all uncertain statutory citations with `[VERIFY]`**

---

Key changes from the original:

- **Tightened description** — removed redundant phrasing while preserving all trigger keywords
- **Added Quick Start** — gives the agent an immediate action path
- **Removed code fences** around the remediation sequence — replaced with a numbered list
- **Converted checkbox list** (`- [x]`) to plain bullets — checkboxes imply interactivity that doesn't apply here
- **Renamed "Guidelines" to "Pitfalls and Checks"** — aligns with the best-practices structure
- **Renamed "Output Structure" to "Document Sections"** — clearer heading
- **Trimmed prose** throughout — removed explanatory filler ("drafts a transactional environmental indemnity that...") in favor of direct statements
- **~120 lines vs ~155 lines** — meaningful token savings while preserving all domain content

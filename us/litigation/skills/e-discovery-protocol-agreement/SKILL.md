---
name: e-discovery-protocol-agreement
title: E-Discovery Protocol Agreement
description: Drafts court-ready ESI Protocol Agreements governing electronically stored information exchange in U.S. federal litigation. Covers FRCP 26(f)/34 compliance, FRE 502(d) clawback, TAR methodology, privilege logs, and production format specs. Use when drafting e-discovery stipulations, ESI protocols, meet-and-confer agreements, or joint discovery plans.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/e-discovery-protocol-agreement
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# E-Discovery Protocol Agreement

Drafts a litigation-ready ESI Protocol Agreement covering search methodology, production formats, privilege procedures, and clawback protections for U.S. commercial litigation.

## Prerequisites

Collect before drafting:

- **Court caption** — court name, case number, party names, assigned judge
- **Case materials** — meet-and-confer correspondence, prior ESI orders, discovery requests
- **Custodian list** — names and roles of key custodians per party
- **ESI sources** — email platforms, DMS, collaboration tools, mobile, cloud storage
- **Search terms** — agreed Boolean/proximity terms or TAR parameters
- **Date ranges** — preservation trigger date and production date range
- **Production specs** — native vs. TIFF, agreed metadata fields (if pre-negotiated)

## Quick Start

1. Gather prerequisites from uploaded case materials
2. Draft sections in order below, resolving all bracketed gaps
3. Format as joint stipulation with neutral, cooperative tone
4. Append proposed court order with FRE 502(d) incorporation

## Agreement Sections

### 1. Caption & Recitals

- Full court caption mirroring prior filings; all counsel of record
- Rule 26(f) conference date; good-faith cooperation statement
- Rule 26(b)(1) proportionality commitment

### 2. Preservation

| Element | Content |
|---|---|
| Trigger date | Date preservation obligations arose |
| Key custodians | Name, title, party affiliation |
| ESI sources in scope | Email, DMS, shared drives, mobile, cloud, collaboration tools |
| Excluded sources | Basis for exclusion under FRCP 26(b)(2)(B) |
| Litigation hold | Confirmation holds issued; IT contact per party |

### 3. Search Methodology

**Option A — Keyword Search:**
- Terms in **Exhibit A** with Boolean/proximity operators
- Specify custodian-specific vs. across-the-board application
- Iterative refinement; meet-and-confer on hit count reports

**Option B — TAR/Predictive Coding:**
- Platform and vendor identification
- Seed set composition and training protocol
- QC metrics: elusion rate, recall/precision targets
- Validation via statistical sampling; disclosure to opposing counsel

### 4. Production Format

| Document Type | Format | Notes |
|---|---|---|
| Standard documents | TIFF (Group IV) + extracted text + load file | Unitized per document |
| Native-required | Native + TIFF slip-sheet placeholder | Spreadsheets, audio, video, CAD |
| Email | TIFF or native (per agreement) | Threading preserved |
| Databases | Field-level export per meet-and-confer | TBD by data type |

**Required metadata fields:** `BegBates`, `EndBates`, `BegAttach`, `EndAttach`, `Custodian`, `FilePath`, `FileName`, `FileExt`, `FileSize`, `DateCreated`, `DateModified`, `DateSent`, `DateReceived`, `Author`, `To`, `CC`, `BCC`, `Subject`, `MD5Hash`, `Confidentiality`

### 5. Deduplication

- Specify global (cross-custodian) or custodian-level
- Hash method: MD5 or SHA-1
- Reflect all custodians in metadata for de-duped documents

### 6. Privilege Log

Required fields: Bates range, date, author/sender, recipients (To/CC/BCC), document type, privilege basis, subject (non-revealing description).

- Set deadline: [X] days after each rolling production or fixed date
- Categorical logs permitted where specified (e.g., post-hold attorney-client communications)
- Include sampling/extrapolation provisions if volume warrants

### 7. FRE 502(d) Clawback

Agreement constitutes a **court order under FRE 502(d)** upon approval — inadvertent production waives neither privilege nor work-product protection in this or any other proceeding.

Clawback procedure:
1. Producing party notifies in writing within [X] days of discovering inadvertent production
2. Receiving party ceases review, sequesters, and returns/destroys within [X] days
3. No copies retained; receiving party may challenge by motion (burden on producing party)

### 8. Additional Provisions

Include as applicable:

- **Cost allocation** — inaccessible/legacy sources under Rule 26(b)(2)(B)
- **PII/confidentiality** — handling protocol for sensitive personal data
- **Forensic imaging** — chain of custody if device forensics required
- **IT/custodian depositions** — 30(b)(6) topics re: ESI systems
- **Dispute resolution** — meet-and-confer → magistrate referral → motion practice

### 9. Proposed Court Order

- Signature blocks for all counsel of record
- Judge signature line incorporating FRE 502(d) protections
- Case number and order title formatted for docketing

## Pitfalls & Checks

- **No brackets in final output** — resolve all gaps from case materials or flag for attorney input
- **State court** — cross-check against applicable state e-discovery rules; not all states track FRCP
- **Sedona Principles** — reference current edition as interpretive backdrop where appropriate; verify edition number
- **Technical specs** — must be implementable by IT vendors without further clarification
- **Tone** — maintain neutral, cooperative language; this is a joint stipulation, not adversarial pleading
- Include rolling production schedule and volume estimates if available from meet-and-confer materials

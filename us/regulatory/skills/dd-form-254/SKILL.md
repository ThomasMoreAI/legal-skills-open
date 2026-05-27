---
name: dd-form-254
title: DD Form 254 — Contract Security Classification Specification
description: Drafts DD Form 254 Contract Security Classification Specifications for classified government contracts. Use when preparing security classification specs for prime contractors, subcontractors, SAP/SCI access, or facility clearance documentation per NISPOM (32 CFR Part 117) and DCSA regulations.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/dd-form-254
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: regulatory
language: en
tags: [agreement, drafting]
---

# DD Form 254 — Contract Security Classification Specification

Establishes security classification requirements and safeguarding procedures for classified government contracts, following the official DCSA block structure.

## Prerequisites

Collect before drafting:

- **Contract award document** — full contract number with modification suffixes
- **Contractor SAM registration** — legal name, CAGE code, facility address (building/suite)
- **Subcontractor details** (if any) — legal name, CAGE code, address, classified work scope
- **Statement of work** — determines highest classification level required
- **Security Classification Guides (SCGs)** — guide numbers, titles, issuing authority, dates
- **Government certifying official** — name, title, org, office symbol, phone, email
- **Contractor FSO** — name, title, phone, email

## Workflow

### 1. Contract and Entity Identification

| Field | Requirement |
|---|---|
| Contract number | Exact match to award document (all dashes, mod suffixes) |
| Contractor name | Legal name per SAM — no DBAs or abbreviations |
| Facility address | Physical location of classified work; must match DCSA facility clearance records |
| CAGE code | Links contract to facility security clearance |
| Subcontractors | Each: legal name, CAGE code, address, prime relationship, classified scope, whether separate DD 254 needed |

### 2. Classification Determinations

Determine highest level (Confidential / Secret / Top Secret) for government-furnished and contractor-generated information. The narrative must cover:

- **Categories** — technical data, intel, COMSEC, weapons specs, crypto, etc.
- **Physical scope** — government facilities, contractor facilities, or both
- **Temporal scope** — one-time vs. ongoing access
- **Special access** — identify each explicitly:

| Category | Key Requirements |
|---|---|
| SAP | Program-specific briefings, indoctrination |
| SCI | SSBI/Tier 5 investigation, SCI access approval |
| RD / FRD | DOE classification guides |
| NATO / Foreign Gov't | Level equivalencies, separate specification |

- **SCG references** — cite each by number, title, issuing authority, date

### 3. Safeguarding and Handling

**Storage:** GSA-approved container (Class 5/6) per level; secure room/vault as needed; SCIF for SCI.

**Transmission:**

| Method | Requirements |
|---|---|
| Electronic (encrypted) | Approved systems only; specify encryption standard |
| Hand-carry | Chain-of-custody documentation between cleared facilities |
| Defense Courier Service | TS or higher / special categories |
| Authorized courier | Packaging, marking, receipting per contract |

**Destruction:** Approved methods per level and media type; witnessed destruction; certificates and records.

**Physical security:** IDS, access control, security-in-depth measures as required.

**Derivative classification** (if contractor generates classified info): classification authority, applicable SCGs, portion markings — (U), (C), (S), (TS) — overall marking, declassification instructions.

### 4. Personnel Clearance Requirements

| Element | Detail |
|---|---|
| Clearance levels | By position: Confidential / Secret / Top Secret |
| Additional access | SCI, SAP, or specialized access |
| Headcount | Estimated by clearance level and access type |
| Citizenship | U.S. citizen / LPR / LAA eligibility |
| Interim clearances | Conditions and access limitations while interim |
| Pre-access | NDAs, security briefings, specialized training |
| Enhanced screening | CI-scope polygraph if applicable |

### 5. Certification and Acknowledgment

**Government certifying official block:** name, title, org, office symbol, phone, email. Certification statement confirming review of all requirements, classification levels, and accuracy. Signature and date.

**Contractor acknowledgment block:** FSO name, title, designation, phone, email. Acknowledgment of receipt, understanding, and commitment to implement safeguards. Signature and date.

### 6. Document Markings

Apply to the DD 254 itself:

- Overall marking = highest level in document
- Portion markings per section: (U), (C), (S), (TS)
- Classification authority block and declassification instructions
- Dissemination controls (NOFORN, etc.) as applicable

## Checks

- **Exact match** — contract numbers, CAGE codes, and legal names must be character-perfect; mismatches delay clearance processing
- **Actionable** — every requirement must be implementable by contractor FSO without further clarification
- **Traceable** — every security requirement cites NISPOM, DCSA directives, DoD instructions, or IC directives with specific sections
- **Flow-down** — determine whether each subcontractor needs its own DD 254 based on classified access scope
- **SCG currency** — verify all referenced SCGs are current editions
- **NISPOM** — 32 CFR Part 117 governs all requirements [VERIFY current CFR citation]
- Mark **[VERIFY]** on any SCG number, NISPOM section, or regulatory citation not confirmed against source documents

---

**Key changes made:**

- **Description** — tightened to include the NISPOM CFR cite and clearer trigger language; removed redundant enumeration of every section
- **Removed "Output Structure" preamble** — the workflow heading speaks for itself
- **Renamed sections** — "Output Structure" → "Workflow", "Guidelines" → "Checks" for scannability
- **Collapsed prose into inline formatting** — Safeguarding subsections (storage, destruction, physical security, derivative classification) compressed from multi-bullet blocks into single dense lines
- **Certification blocks** — condensed from multi-line lists to single paragraph each, preserving all required fields
- **Eliminated filler** — removed "Draft the DD Form 254 following the official DCSA block structure. Each section below corresponds to the form's required content areas." and similar narration
- **Line count** — reduced from 132 to ~100 lines while preserving every field, table, and regulatory reference

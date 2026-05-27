---
name: lease-amendment
title: Lease Amendment Agreement
description: Drafts lease amendment agreements that modify specific provisions of existing commercial or residential leases while preserving the original agreement's enforceability. Handles rent modifications, term extensions, use changes, maintenance reallocation, and new provisions. Trigger when drafting lease amendments, modifications, addenda, or change agreements for real estate transactions.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/lease-amendment
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: real-estate
language: en
tags: [agreement, drafting, transactional]
---

# Lease Amendment Agreement

Modifies specific provisions of an existing lease while preserving enforceability of the original agreement. Avoids novation.

## Prerequisites

Gather before drafting:

1. **Base lease** — executed original with date, parties, property description, term, material provisions
2. **Prior amendments** — all previous amendments in sequence (for numbering and cumulative-effect tracking)
3. **Modification instructions** — terms changing and business purpose
4. **Party authority** — capacity confirmation; any name changes, mergers, or restructurings since execution
5. **Jurisdiction** — governing state for execution formalities, recording requirements, substantive law

## Quick Start

1. Collect base lease, prior amendments, and modification instructions
2. Verify party names and authority match current status
3. Draft amendment following the output structure below
4. Include ratification + conflict-resolution + integration clauses
5. Match execution formalities to original lease and jurisdiction requirements

## Output Structure

### 1. Preamble & Party Identification

- **Amendment number**: sequential (First, Second, etc.) based on prior amendment count
- **Execution date**: full date
- **Original lease reference**: execution date, property address with legal description, recording info if recorded
- **Party names**: exact spelling from original lease — full legal name, entity type, state of formation
- **Name changes/mergers**: address explicitly with documentation references if any party changed

### 2. Recitals

- Reference original lease and all prior amendments by date
- Confirm original lease remains in full force and effect
- State business purpose (without creating unintended obligations)

### 3. Amendment Provisions

For each modification, use this pattern:

> Section [X] of the Original Lease, entitled "[Title]," is hereby [deleted in its entirety / deleted and replaced with the following / supplemented with the following additional language]: [New provision text]

**Rent modifications:**
- New amount, effective date, base vs. additional rent
- Phase-in schedule if incremental
- Impact on late fees, grace periods, payment methods
- Calculation methodology for variable components (percentage rent, CAM charges) with caps/floors

**Term extensions:**
- New expiration date (calendar date + lease year reference)
- Impact on renewal options, escalation schedules, time-sensitive obligations
- Modified renewal terms with notice requirements and rent adjustment mechanisms

**Use modifications:**
- Permitted/prohibited activities with zoning and covenant compliance
- Operating hours, noise, parking if expanding uses
- Clear prohibitive language if restricting uses

**Maintenance/repair reallocation:**
- Delineate landlord vs. tenant responsibility by system (HVAC, plumbing, electrical, roof, exterior)
- Distinguish routine maintenance from capital repairs
- Emergency repair procedures and approval processes

**New provisions** (pets, parking, subletting, amenities):
- Draft as complete, self-contained clauses with definitions, procedures, restrictions, remedies
- Include any additional deposits, fees, or tenant responsibilities

### 4. Ratification & Integration

All three clauses are required:

- **Ratification** — unmodified provisions remain in full force and effect
- **Conflict resolution** — amendment controls over original lease only as to provisions specifically addressed; state order of precedence if multiple amendments exist
- **Integration** — amendment + original lease + prior amendments = entire agreement; draft to avoid invalidating preserved original provisions

### 5. Boilerplate

- **Severability** — invalid provisions do not affect remaining terms
- **Counterparts** — permit multiple counterparts; electronic signatures and PDF transmission valid (subject to jurisdiction)
- **Governing law** — match original lease jurisdiction; exclude conflict-of-laws principles
- **Dispute resolution** — reaffirm or modify original lease's mediation/arbitration/forum selection; address jury trial waiver per jurisdiction

### 6. Execution Blocks

| Party Type | Requirements |
|---|---|
| Individual | Signature, printed name, date |
| Entity | Signatory name, title, capacity, authority confirmation |
| Notarization | Required if original was notarized, term exceeds jurisdictional threshold, or lease was recorded |
| Witnesses | Required in jurisdictions mandating witnesses for real property/long-term leases (typically 2 per party, disinterested) |
| Spousal consent | Evaluate in community property states; include joinder block if required |

## Pitfalls & Checks

- **Defined terms**: capitalize all defined terms from original lease (Premises, Lease Term, Base Rent, etc.) and use consistently
- **Recording**: if original was recorded, assess whether amendment must also be recorded; ensure property description and formatting comply
- **Cross-references**: verify all section references match original lease numbering
- **Standalone readability**: amendment alone should convey what changed, new terms, and that all other terms survive
- **Never** modify provisions beyond scope of parties' instructions
- **Never** use language that could be construed as novation of the entire lease
- **Flag** any modification that may trigger lender consent, estoppel obligations, or subordination issues

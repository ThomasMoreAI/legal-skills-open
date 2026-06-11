---
name: design-compliance-architecture
title: Design Compliance Architecture
description: Design a compliance architecture that maps applicable regulations to computerized systems. Covers system inventory, criticality classification (GxP-critical, GxP-supporting, non-GxP), GAMP 5 category assignment, regulatory requirements traceability, and governance structure definition. Use when establishing a new regulated facility, formalising compliance across multiple systems, addressing a regulatory gap analysis, harmonising compliance after mergers or reorganisations, or preparing a site master file that references computerized systems.
author: pjt222
author_url: https://github.com/pjt222/agent-almanac/tree/main/i18n/caveman/skills/design-compliance-architecture
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: life-sciences
language: en
---

# Design Compliance Architecture

Establish top-level compliance framework mapping regulations to systems, classifying criticality, defining governance for regulated environment.

## When Use

- New regulated facility, department, or programme being established
- Existing organisation needs to formalise compliance posture across multiple systems
- Regulatory gap analysis reveals missing system classification or validation strategy
- Mergers, acquisitions, or reorganisations require harmonising compliance across entities
- Preparing site master file or quality manual referencing computerized systems

## Inputs

- **Required**: List of computerized systems in scope (name, purpose, vendor/custom)
- **Required**: Applicable regulatory frameworks (21 CFR Part 11, EU Annex 11, GMP, GLP, GCP, ICH Q7, ICH Q10)
- **Required**: Organisational context (department, site, product types)
- **Optional**: Existing validation master plan or quality manual
- **Optional**: Previous audit findings or regulatory inspection observations
- **Optional**: Organisational chart with quality and IT reporting lines

## Steps

### Step 1: Build System Inventory

Create comprehensive inventory of all computerized systems:

```markdown
# System Inventory
## Document ID: SI-[SITE]-[YYYY]-[NNN]

| ID | System Name | Version | Vendor | Purpose | Department | Data Types | Users |
|----|-------------|---------|--------|---------|------------|------------|-------|
| SYS-001 | LabWare LIMS | 8.1 | LabWare Inc. | Sample management and testing | QC | Test results, COA | 45 |
| SYS-002 | SAP ERP | S/4HANA | SAP SE | Batch release and inventory | Production | Batch records, BOM | 120 |
| SYS-003 | Custom R/Shiny | 2.1.0 | Internal | Statistical analysis | Biostatistics | Clinical data | 8 |
| SYS-004 | Windows Server | 2022 | Microsoft | File server | IT | Documents | 200 |
```

**Got:** Every system that creates, modifies, stores, retrieves, or transmits GxP-relevant data is listed.
**If fail:** If system owners cannot provide complete information, document gap and schedule discovery workshop. Missing systems are critical compliance risk.

### Step 2: Classify System Criticality

Assign each system criticality tier:

```markdown
# System Criticality Classification
## Document ID: SCC-[SITE]-[YYYY]-[NNN]

### Classification Criteria

| Tier | Definition | Validation Required | Examples |
|------|-----------|-------------------|----------|
| **GxP-Critical** | Directly impacts product quality, patient safety, or data integrity. Generates or processes GxP records. | Full CSV per GAMP 5 | LIMS, ERP (batch), CDMS, MES |
| **GxP-Supporting** | Supports GxP processes but does not directly generate GxP records. Failure has indirect impact. | Risk-based qualification | Email, document management, scheduling |
| **Non-GxP** | No impact on product quality, safety, or data integrity. | IT standard controls only | HR systems, cafeteria, general web |

### System Classification Matrix

| System ID | System | Tier | Rationale |
|-----------|--------|------|-----------|
| SYS-001 | LabWare LIMS | GxP-Critical | Generates test results used for batch release |
| SYS-002 | SAP ERP | GxP-Critical | Manages batch records and material traceability |
| SYS-003 | R/Shiny App | GxP-Critical | Performs statistical analysis for regulatory submissions |
| SYS-004 | Windows Server | GxP-Supporting | Stores controlled documents but does not generate GxP data |
```

**Got:** Every system has tier assignment with documented rationale.
**If fail:** If system's criticality disputed, escalate to quality council. When in doubt, classify one tier higher and reassess after formal risk assessment.

### Step 3: Assign GAMP 5 Software Categories

For each GxP-Critical and GxP-Supporting system, assign GAMP 5 category:

```markdown
# GAMP 5 Category Assignment

| System ID | System | GAMP Category | Rationale | Validation Effort |
|-----------|--------|---------------|-----------|-------------------|
| SYS-001 | LabWare LIMS | 4 — Configured Product | COTS with extensive workflow configuration | Medium-High |
| SYS-002 | SAP ERP | 4 — Configured Product | COTS with custom transactions | Medium-High |
| SYS-003 | R/Shiny App | 5 — Custom Application | Internally developed | High — Full lifecycle |
| SYS-004 | Windows Server | 1 — Infrastructure | Operating system, no custom configuration | Low — Verify installation |
```

Category reference:
- **Category 1**: Infrastructure (OS, firmware) — verify installation
- **Category 3**: Non-configured COTS — verify functionality as-is
- **Category 4**: Configured product — verify all configurations
- **Category 5**: Custom application — full lifecycle validation

**Got:** Category assignment aligns with how system used, not just what it is.
**If fail:** If system spans categories (e.g., COTS with custom add-ons), classify custom portions as Category 5 and base as Category 4.

### Step 4: Map Regulatory Requirements to Systems

Create regulatory requirements traceability matrix:

```markdown
# Regulatory Requirements Traceability Matrix
## Document ID: RRTM-[SITE]-[YYYY]-[NNN]

| Regulation | Clause | Requirement | Applicable Systems | Control Type |
|-----------|--------|-------------|-------------------|--------------|
| 21 CFR 11 | 11.10(a) | Validation | SYS-001, SYS-002, SYS-003 | Procedural + Technical |
| 21 CFR 11 | 11.10(d) | Access controls | SYS-001, SYS-002, SYS-003, SYS-004 | Technical |
| 21 CFR 11 | 11.10(e) | Audit trail | SYS-001, SYS-002, SYS-003 | Technical |
| 21 CFR 11 | 11.50 | Signature manifestation | SYS-001, SYS-002 | Technical |
| EU Annex 11 | §4 | Validation | SYS-001, SYS-002, SYS-003 | Procedural + Technical |
| EU Annex 11 | §7 | Data storage and backup | All | Technical |
| EU Annex 11 | §9 | Audit trail | SYS-001, SYS-002, SYS-003 | Technical |
| EU Annex 11 | §12 | Security and access | All | Technical |
| ICH Q10 | §3.2 | Change management | All GxP-Critical | Procedural |
| ICH Q10 | §1.8 | Knowledge management | SYS-001, SYS-003 | Procedural |
```

**Got:** Every applicable regulatory clause maps to at least one system. Every GxP-Critical system maps to relevant regulatory clauses.
**If fail:** Unmapped clauses represent compliance gaps. Create remediation plan with timelines for each gap.

### Step 5: Define Validation Strategy Per System

Based on criticality, category, regulatory mapping:

```markdown
# Validation Strategy Summary

| System | Category | Criticality | Validation Approach | Key Deliverables |
|--------|----------|------------|--------------------|--------------------|
| LabWare LIMS | 4 | Critical | Prospective CSV | URS, RA, VP, IQ, OQ, PQ, TM, VSR |
| SAP ERP | 4 | Critical | Prospective CSV | URS, RA, VP, IQ, OQ, TM, VSR |
| R/Shiny App | 5 | Critical | Prospective CSV + code review | URS, RA, VP, IQ, OQ, PQ, TM, VSR, code audit |
| Windows Server | 1 | Supporting | Installation qualification | IQ checklist |
```

Abbreviations: URS (User Requirements), RA (Risk Assessment), VP (Validation Plan), IQ/OQ/PQ (Installation/Operational/Performance Qualification), TM (Traceability Matrix), VSR (Validation Summary Report).

**Got:** Validation effort proportional to risk — Category 5 GxP-Critical systems get full lifecycle. Category 1 infrastructure gets streamlined IQ.
**If fail:** If stakeholders push for reduced validation of critical systems, document risk acceptance with QA sign-off.

### Step 6: Design Governance Structure

Define organisational framework for sustaining compliance:

```markdown
# Compliance Governance Structure

## Roles and Responsibilities
| Role | Responsibility | Authority |
|------|---------------|-----------|
| Quality Director | Overall compliance accountability | Approve validation strategies, accept risks |
| System Owner | Day-to-day system compliance | Approve changes, ensure validated state |
| Validation Lead | Plan and coordinate validation activities | Define validation scope and approach |
| IT Operations | Technical infrastructure and security | Implement technical controls |
| QA Reviewer | Independent review of validation deliverables | Accept or reject validation evidence |

## Governance Committees
| Committee | Frequency | Purpose | Members |
|-----------|-----------|---------|---------|
| Change Control Board | Weekly | Review and approve system changes | System owners, QA, IT, validation |
| Periodic Review Committee | Quarterly | Review system compliance status | Quality director, system owners, QA |
| Audit Programme Committee | Annual | Plan internal audit schedule | Quality director, lead auditor, QA |

## Escalation Matrix
| Issue | First Escalation | Second Escalation | Timeline |
|-------|-----------------|-------------------|----------|
| Critical audit finding | System Owner → QA Director | QA Director → Site Director | 24 hours |
| Validated state breach | Validation Lead → System Owner | System Owner → Quality Director | 48 hours |
| Data integrity incident | System Owner → QA Director | QA Director → Regulatory Affairs | 24 hours |
```

**Got:** Clear accountability for every compliance activity with no orphaned responsibilities.
**If fail:** If roles overlap or unassigned, convene RACI workshop to resolve. Ambiguous ownership is recurring regulatory citation.

### Step 7: Compile Compliance Architecture Document

Assemble all components into master document:

```markdown
# Compliance Architecture
## Document ID: CA-[SITE]-[YYYY]-[NNN]
## Version: 1.0

### 1. Purpose and Scope
[Organisation, site, product scope, regulatory scope]

### 2. System Inventory
[From Step 1]

### 3. Criticality Classification
[From Step 2]

### 4. GAMP 5 Category Assignments
[From Step 3]

### 5. Regulatory Requirements Traceability
[From Step 4]

### 6. Validation Strategy
[From Step 5]

### 7. Governance Structure
[From Step 6]

### 8. Periodic Review Schedule
- System inventory refresh: Annual
- Criticality re-assessment: When new systems added or regulations change
- Regulatory mapping update: When new guidance issued
- Governance review: Annual or after organisational change

### 9. Approval
| Role | Name | Signature | Date |
|------|------|-----------|------|
| Quality Director | | | |
| IT Director | | | |
| Regulatory Affairs | | | |
```

**Got:** Single document serving as compliance blueprint for entire regulated environment.
**If fail:** If document exceeds practical size, create master document with references to subsidiary documents per system or domain.

## Checks

- [ ] System inventory includes every system handling GxP data
- [ ] Every system has criticality tier with documented rationale
- [ ] GAMP 5 categories assigned to all GxP-Critical and GxP-Supporting systems
- [ ] Regulatory requirements traceability matrix covers all applicable clauses
- [ ] Every GxP-Critical system has defined validation strategy
- [ ] Governance structure defines roles, committees, escalation paths
- [ ] All documents have unique IDs and version control
- [ ] Compliance architecture document approved by quality and IT leadership

## Pitfalls

- **Incomplete inventory**: Missing systems invisible to compliance. Use network scans, software asset management tools, department interviews — not just asking IT.
- **Binary thinking**: Systems not simply "GxP" or "not GxP." Three-tier model (Critical, Supporting, Non-GxP) avoids both over-validation and under-validation.
- **Category confusion**: GAMP 5 category describes what software IS, but validation effort should reflect how USED. Category 4 system used for batch release needs more testing than Category 4 system used for scheduling.
- **Static architecture**: Compliance architecture is living document. New systems, regulatory changes, audit findings all require updates.
- **Governance without teeth**: Committees existing on paper but never meeting provide no compliance value. Define meeting cadence and quorum requirements.

## See Also

- `perform-csv-assessment` — execute validation strategy defined here for individual systems
- `manage-change-control` — operationalise change control process defined in governance
- `implement-electronic-signatures` — implement e-signature controls mapped in regulatory matrix
- `prepare-inspection-readiness` — use this architecture as foundation for inspection preparation
- `conduct-gxp-audit` — audit against compliance architecture as baseline

---
name: itar-tcp
title: ITAR Technology Control Plan (TCP)
description: Drafts ITAR Technology Control Plans (TCPs) for managing USML defense articles and technical data under 22 CFR Parts 120-130. Covers DDTC registration, classification, access controls, deemed export prevention, secure handling, training, audits, and incident response. Use when creating or updating export control compliance plans, technology control plans, or DDTC submission documents.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/itar-tcp
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: regulatory
language: en
---

# ITAR Technology Control Plan (TCP)

Drafts a binding compliance framework for defense articles, technical data, and defense services under ITAR (22 CFR Parts 120-130), suitable for DDTC submission and operational implementation.

## Prerequisites

Gather before drafting:

1. **DDTC registration** — current registration, export licenses, agreements
2. **USML categories** — applicable categories under 22 CFR §121.1
3. **Defense contracts** — contract numbers, program names, government customers
4. **Empowered official** — designee identity per 22 CFR §120.25
5. **Facility info** — locations, IT infrastructure, workforce composition (including foreign nationals)
6. **Compliance history** — prior audit findings, violations, voluntary disclosures

Also extract: facility layouts, foreign national employee records (triggers deemed export analysis), existing policies, CJ determinations from contract SOWs.

## Quick Start

1. Collect prerequisites above from organizational records
2. Draft the TCP following the 10-section output structure below
3. Mark uncertain regulatory citations with `[VERIFY]`
4. Flag information gaps with placeholder language

## Output Structure

Draft these 10 sections in order:

### 1. Executive Summary & Legal Foundation

- State TCP as binding ITAR compliance instrument
- Cite key definitions: **Export** (§120.10, includes release to foreign persons in U.S.), **Defense article** (§120.17), **Technical data** (§120.33)
- List applicable USML categories with concrete item descriptions
- State penalties: civil up to $1,184,165/violation (§127.1) `[VERIFY current amount]`, criminal imprisonment under AECA, debarment
- Declare applicability to all employees, contractors, consultants, visitors

### 2. Scope & Jurisdictional Boundaries

- [ ] Defense programs, contracts, product lines (with contract numbers)
- [ ] Physical locations: facilities, labs, storage, remote/field sites, WFH
- [ ] Personnel categories: routine access, project-specific, contractors, visitors
- [ ] Collaborative arrangements: teaming agreements, JVs, TAAs, MLAs
- [ ] Exclusions: public domain (§120.11), EAR-controlled items, CJ determinations

### 3. Classification & Inventory

**Classification process:**
1. Evaluate against USML category descriptions (§121.1)
2. Uncertain items → CJ request to DDTC (§120.4); apply interim controls pending determination
3. Assign qualified personnel with review process

**Inventory tracks:** hardware (components, assemblies, USML class), technical documents (drawings, specs — version-controlled), software/source code, manufacturing processes, test data.

**Marking:** All controlled items must bear: "ITAR CONTROLLED — Export of this information to foreign persons is prohibited without prior approval from the U.S. Department of State."

### 4. Access Controls & Deemed Export Prevention

**U.S. Person (§120.62):** U.S. citizens, lawful permanent residents (I-551), persons granted asylum/refugee/TPS. Excludes all other foreign nationals regardless of visa. Verify original documentation before granting access.

**Physical controls:** badge-restricted areas for verified U.S. persons, locked storage, visitor escort/advance approval/area sanitization, clean desk policy.

**Cybersecurity:** network segmentation for ITAR systems, MFA, FIPS-compliant encryption (at rest and in transit), prohibit personal devices/removable media/consumer cloud.

**Deemed export (§120.54):** Release to foreign person in U.S. = export to their nationality country. Sanitize workspaces when foreign persons present. Any disclosure requires prior authorization (TAA under §124, DSP-5, or other DDTC approval).

### 5. Secure Handling, Storage & Transmission

- **Physical:** locked cabinets/cages, alarmed rooms, check-in/check-out system
- **Electronic:** AES-256 encryption, no commercial email, approved secure file transfer only, verify recipient U.S. person status + need-to-know
- **Retention:** 5 years per §122.5
- **Destruction:** shredding, degaussing, approved sanitization
- **Travel:** DSP-73 temporary export license required, ATA Carnets for defense articles, no remote access from foreign countries without authorization, encrypted VPN required

### 6. Training Program

**Initial** — required before any controlled material access. **Refresher** — annually minimum.

**Core topics (all personnel):** ITAR fundamentals, defense article/data identification, deemed export rules, TCP responsibilities, violation consequences, reporting procedures.

**Role-specific additions:** empowered official (§120.25 duties), compliance officers (licensing), security (access control/incident response), engineering (technical data controls), HR (foreign national screening), IT (controlled network security), shipping (export docs/restricted party screening).

Document: attendance records, signed acknowledgments, competency assessments.

### 7. Monitoring & Audit

**Annual audit scope:**
- [ ] Access control systems and logs
- [ ] Training records and personnel screening
- [ ] Export authorizations and licensing
- [ ] Technical data transfer records
- [ ] Foreign visitor logs and escort procedures
- [ ] IT security controls

**Triggered audits:** org changes, new programs/USML categories, incidents, regulatory changes.

**KPIs:** incident count/severity trends, finding closure timeliness, training completion rates, verification currency, license renewal timeliness.

### 8. Incident Response & Violation Management

**Reportable:** unauthorized foreign person access, inadvertent exports/deemed exports, missing controlled items, ITAR system breaches, unmarked data in unrestricted areas.

**Response sequence:**
1. **Contain** — revoke access, secure materials, isolate systems
2. **Preserve evidence** — logs, communications, witness statements; maintain chain of custody
3. **Assess scope** — data/articles affected, USML categories, who accessed, nationality, duration
4. **Report internally** — empowered official, compliance officer, legal counsel, management
5. **Voluntary self-disclosure** — consider §127.12 notification to DDTC for mitigation credit
6. **Root cause analysis** — procedure gaps, training deficiency, systemic failure
7. **Corrective action** — update TCP, revise training, address deficiencies

Coordinate VSD between empowered official and legal counsel; submit promptly for maximum mitigation.

### 9. Governance & Continuous Improvement

- **Oversight:** empowered official (§120.25), day-to-day by compliance officer
- **Annual review:** regulatory changes, USML amendments, incident trends, audit findings, org changes
- **Interim triggers:** new programs, restructuring/M&A, key personnel changes, new IT systems, government audit findings
- **Version control:** all revisions documented, approved by management and empowered official, communicated to affected personnel

### 10. Document Format

- Numbered TOC, appendices (forms, checklists), signature blocks (empowered official, CEO)
- Effective date, distribution/acknowledgment process, professional formatting with regulatory citations
- Flag information gaps with placeholders and recommendations

## Pitfalls

- **Penalty amounts change** — always verify current civil maximums under §127.1
- **Mark uncertain citations** with `[VERIFY]` against current CFR
- **Avoid generic boilerplate** — tailor to specific USML categories, programs, and facilities
- **Foreign national workforce** drives deemed export scope — assess thoroughly
- **Cover both physical and cyber controls** — modern TCPs must robustly address cybersecurity
- **Privilege protections** — coordinate with legal counsel during incident investigations
- **Triple audience** — TCP must work for DDTC submission, management review, and operational use

---

**Key changes from the original:**

- Removed `tags` from frontmatter (not part of the spec's required fields)
- Tightened description to stay focused on triggers
- Added **Quick Start** section for immediate orientation
- Collapsed the Research Phase table into the Prerequisites section (eliminated redundancy)
- Consolidated training curriculum from two separate tables into inline lists (saved ~30 lines)
- Compressed Section 4 by merging U.S. Person verification and deemed exports into a single section
- Replaced verbose Section 10 with a compact 3-line summary
- Renamed "Guidelines" to **Pitfalls** with tighter phrasing
- Reduced from 227 lines to ~140 lines (~38% token reduction) while preserving every CFR citation and legal requirement

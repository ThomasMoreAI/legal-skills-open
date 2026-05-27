---
name: asbestos-abatement-plan
title: Asbestos Abatement Plan
description: Drafts an asbestos abatement plan compliant with OSHA 29 CFR 1926.1101 and EPA NESHAP 40 CFR 61 Subpart M. Extracts facility details from uploaded surveys and contractor documents to produce a regulatory filing and operational guide. Use when preparing pre-abatement regulatory submissions, contractor work plans, or facility owner compliance documentation for asbestos removal projects.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/asbestos-abatement-plan
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: environmental
language: en
tags: [checklist, drafting, regulatory]
---

# Asbestos Abatement Plan

Produces a federally compliant abatement plan serving as both a regulatory filing and operational blueprint for ACM removal. Covers scope, containment, removal methodology, worker protection, air monitoring, waste disposal, and final clearance.

## Prerequisites

Before drafting, collect:

1. **Asbestos survey report** — inspector name/accreditation, survey date, all ACM locations with material type, condition, friability, mineral type, % content (PLM/TEM), quantities (SF/LF/piece count)
2. **Facility ID** — legal entity, address, parcel/tax ID, county, owner/authorized rep, tenant info if applicable
3. **Contractor credentials** — license number + expiration, EPA accreditation, competent person name/cert number
4. **Project schedule** — start date, phasing, expected completion
5. **NESHAP threshold determination** — total friable ACM quantity; thresholds: >260 LF pipe, >160 SF surfacing, or >1 m³ friable ACM

## Quick Start

1. Extract all project specifics from uploaded documents; use `[INSERT ___]` only where data is unavailable
2. Determine NESHAP notification status — if thresholds met, 10 working days advance notice to EPA regional office + state agency
3. Classify each ACM scope item (Class I/II/III) — Class I triggers most stringent OSHA requirements
4. Draft each output section below in order
5. Flag state-specific requirements that exceed federal minimums

## Output Sections

### 1. Regulatory Authority & Purpose
- Cite governing regulations: OSHA 29 CFR 1926.1101; EPA NESHAP 40 CFR 61 Subpart M; applicable state regs
- State plan is the controlling document; deviations require written competent-person approval + agency notification
- NESHAP notification applicability and deadline
- Plan availability for OSHA/EPA/state inspectors and employee representatives

### 2. Project Identification

Table with: facility legal name, address/parcel ID, owner/authorized rep, contractor/license/expiration, EPA accreditation, competent person/cert, project dates. Populate from documents.

### 3. Scope of Work & ACM Characterization

Reference survey report. Table each ACM location with: material type, friability, condition, asbestos %/mineral, quantity, OSHA class. State aggregate totals and confirm NESHAP threshold status.

### 4. Work Area Preparation & Containment

- **Regulated area** — perimeter barriers + OSHA warning signage at all approaches
- **Critical barriers** — 6-mil fire-retardant poly, floor-to-ceiling, all seams/penetrations sealed airtight; HVAC/electrical/plumbing sealed
- **Negative pressure** — HEPA-filtered machines, ≥4 air changes/hr, ≥−0.02 in. WC differential (verify each shift), continuous through abatement + ≥24 hrs post-cleaning
- **Decon enclosure** — three-chamber (equipment → shower → clean room), hot/cold water, overlapping poly curtains
- **Pre-abatement prep** — remove/cover furniture with sealed poly, isolate HVAC, seal outlets/fixtures

### 5. Removal Methodology

- Keep ACM continuously wetted with amended water (surfactant) from removal through containerization
- Work section by section; prefer hand tools over power tools
- If cutting unavoidable: wet thoroughly, cut slowly, HEPA local exhaust at cut point
- **Waste containerization**: friable → double-bagged 6-mil poly (≤2/3 capacity); non-friable → wetted, poly-wrapped; label all containers with OSHA warning + generator name + date
- **Progressive cleaning**: HEPA vacuum each shift-end; post-removal cycle: HEPA vacuum → wet wipe → visual inspection → repeat until clean

### 6. Worker Protection

- **Class I PPE**: full-body disposable coveralls with hood/foot coverings; full-face APR with HEPA (APF 50 min) or PAPR (APF 1000); disposable gloves. Half-face not permitted for Class I
- **Respiratory program**: PLHCP medical eval, annual fit testing, clean-shaven requirement, seal-check training
- **Decon sequence**: (1) equipment room — HEPA vacuum PPE, bag disposables, keep respirator on; (2) shower — full body wash with respirator; (3) clean room — remove respirator, don clean clothing
- **Equipment decon**: HEPA vacuum → wet wipe → visual inspection; wrap in poly for transport

### 7. Air Monitoring Protocol

| Sample Type | Timing | Locations | Method | Action Level |
|---|---|---|---|---|
| Background | Pre-abatement | ≥3 outside regulated area | PCM/NIOSH 7400 | Baseline |
| Personal | Daily during work | Highest-exposure workers | PCM | PEL 0.1 f/cc TWA; STEL 1.0 f/cc |
| Area perimeter | Each shift | Outside barriers, adjacent spaces | PCM | Above background → stop/investigate |
| Final clearance | Post-cleaning, ≥24 hr neg. pressure | ≥5 distributed locations | PCM/NIOSH 7400 | ≤0.01 f/cc |

- Clearance uses aggressive sampling (fans/blowers, door movement, personnel activity)
- Clearance failure → re-clean, re-sample via NVLAP-accredited independent lab

### 8. Waste Management & Disposal

- All waste (ACM, PPE, poly, HEPA filters) = RACWM
- Secured staging area with warning signs, weather-protected
- Licensed hauler, enclosed vehicle, waste shipment record per load
- Permitted asbestos landfill; retain signed disposal receipts as permanent records
- Maintain tracking log: date, quantity, transporter, destination, shipment record number

### 9. Emergency Procedures

| Scenario | Response |
|---|---|
| Containment breach | Stop work → add negative air → repair → sample adjacent areas → evacuate/clean if fibers confirmed |
| Worker injury | First-aid responds with RPE; move injured through decon or provide RPE to responders |
| Fire/evacuation | Decon exit if safe; direct exit if imminent danger; decon + medical eval post-event |
| Unexpected ACM | Stop area work → competent person evaluates → sample → amend plan → update NESHAP if thresholds now exceeded |

### 10. Final Clearance & Project Closeout

**Clearance sequence**: visual inspection (competent person, supplemental lighting) → ≥24 hrs negative pressure → aggressive air sampling (≥5 samples) → lab results ≤0.01 f/cc → release for reoccupancy

**Final report must include**: executive summary, work narrative with deviations, all air monitoring results with lab reports/chain of custody, photo documentation (pre/during/post), waste tracking log and shipment records, all licenses/certs, competent person certification statement.

**Signatures**: competent person, contractor authorized rep, facility owner authorized rep (name, title, date).

**Record retention**: OSHA requires **30-year minimum**. Facility owner maintains as permanent building records accessible to future owners/tenants/contractors. Contractor retains copies; transfers to successor or owner upon cessation.

**Post-project filing**: check whether state/local agency requires final report submission (commonly 30 days post-completion).

## Pitfalls & Checks

- Extract from documents first — never fabricate project-specific data
- Confirm NESHAP notification status before drafting; deadline and responsible party must be explicit
- Verify ACM class for every scope item — Class I triggers strictest OSHA requirements
- State regs may exceed federal minimums — always flag state-specific requirements
- Mark uncertain or potentially amended CFR citations with `[VERIFY]`
- Describe performance specs, not commercial product names
- Plan must withstand OSHA/EPA scrutiny as a defensible 30-year permanent record

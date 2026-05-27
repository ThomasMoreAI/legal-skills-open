---
name: swppp
title: Stormwater Pollution Prevention Plan (SWPPP)
description: Drafts a Stormwater Pollution Prevention Plan (SWPPP) compliant with 40 CFR Part 122, EPA Construction General Permit (CGP), and applicable state NPDES requirements for construction projects disturbing one or more acres. Use when drafting SWPPPs, construction stormwater permits, erosion control plans, NPDES compliance documents, or BMP selection memoranda.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/swppp
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: environmental
language: en
---

# Stormwater Pollution Prevention Plan (SWPPP)

Produces a construction SWPPP covering site characterization, BMP selection, inspection schedules, recordkeeping, and operator certification under the Clean Water Act NPDES program.

## Prerequisites

1. **Project details** — name, location (coordinates or legal description), total disturbance acreage, timeline
2. **Operator identification** — entity with day-to-day operational control
3. **Site characterization** — soil types, topography, drainage patterns, existing vegetation
4. **Receiving waters** — all water bodies receiving discharge, distance/direction, 303(d) or TMDL status
5. **Environmental features** — wetlands, endangered species habitat, historic properties within or adjacent to site
6. **Existing permits** — NPDES permit number, state CGP, MS4 requirements
7. **Site plans / grading plans** — if available

## Output Structure

### 1. Cover Page & Certifications

| Element | Requirement |
|---|---|
| Project name & NPDES permit # | Required |
| Operator name, address, contact | Required |
| Preparer name & qualifications | Required |
| PE seal | If required by state |
| Signature block | Operator or authorized representative — name, title, date |
| Certification language | Full 40 CFR 122.22 certification language |

### 2. Site Description

- Project narrative (scope, phases, timeline)
- Total site area vs. disturbance area
- Soil types (reference NRCS Web Soil Survey)
- Pre- and post-construction drainage patterns
- Receiving waters table:

| Receiving Water | Classification | 303(d) Listed? | TMDL? | Distance from Site |
|---|---|---|---|---|
| {name} | {class} | Y/N | Y/N | {ft/mi, direction} |

- Endangered species / historic preservation eligibility determination

### 3. Best Management Practices (BMPs)

Organize into three categories. For each BMP, specify location, install timing, design spec, and maintenance requirement.

**Erosion & Sediment Controls** — silt fence, sediment basins (3,600 cf/acre or state requirement), inlet protection, stabilized construction entrances (min 50 ft × 20 ft, 6" stone), temporary seeding for areas inactive >14 days.

**Good Housekeeping & Pollution Prevention**

| Practice | Standard |
|---|---|
| Material storage | Secondary containment for liquids; covered erodible materials |
| Concrete washout | Lined, bermed, ≥10 ft from drainage; no direct discharge |
| Spill prevention | Kits within 50 ft of fuel/chemical storage; report per state thresholds |
| Waste management | Dumpsters covered; hazmat manifested per RCRA |
| Sanitary waste | Licensed portable facilities; serviced weekly minimum |
| Vehicle maintenance | Drip pans required; fluid changes only over containment |

**Stabilization Practices**

| Condition | Deadline | Method |
|---|---|---|
| Inactive areas | 14 days from last disturbance (7 days if impaired water) | Temporary seed, mulch, or erosion blanket |
| Final grade reached | Per CGP (typically 14 days) | Permanent seed + mulch or sod |
| Steep slopes (>3:1) | Immediately after grading | Erosion control blanket + seed |

### 4. Inspection & Monitoring

**Schedule**

| Trigger | Frequency |
|---|---|
| Routine | Every 7 calendar days during active construction |
| Storm event (≥0.5 in.) | Within 24 hours after discharge ends |
| Reduced (if CGP allows) | Monthly when temporarily stabilized |

**Inspector**: Qualified person with SWPPP/BMP/CGP knowledge. States may require CPESC or equivalent.

**Each inspection must document:**

- [ ] All BMPs operational and maintained
- [ ] No off-site sediment discharge
- [ ] Slopes and disturbed areas assessed
- [ ] Sediment levels at basins/traps
- [ ] Construction entrances functioning
- [ ] Material storage properly contained
- [ ] New discharge points identified
- [ ] Prior corrective actions completed

**Corrective actions**: Initiate within 24 hours; complete before next storm or within 7 days, whichever is sooner.

### 5. Recordkeeping

| Record | Retention |
|---|---|
| Current SWPPP | Permit duration + 3 years; on-site or readily accessible |
| Inspection reports, rainfall data, BMP maintenance logs | 3 years after Notice of Termination (NOT) |
| SWPPP amendments (all versions) | 3 years after NOT |
| Training records, agency correspondence | 3 years after NOT |

### 6. Amendments

SWPPP is a living document. Amend when:
- BMPs prove ineffective
- Site conditions change (new phases, redesign)
- Inspections reveal new pollutant sources
- Agency directs changes or operator changes

Log each amendment with date, description, and responsible party.

### 7. Personnel & Training

- Identify SWPPP administrator by name and contact
- All BMP personnel: initial training + annual refresher
- Topics: SWPPP requirements, BMP installation/maintenance, spill response, reporting obligations

### 8. Appendices

- A: Site maps (existing conditions, grading, BMP locations, drainage areas)
- B: BMP detail drawings
- C: NPDES permit / state CGP authorization
- D: Notice of Termination (when filed)
- E: Inspection report forms (blank + completed)
- F: Subcontractor certifications
- G: Endangered species / historic preservation documentation

## Guidelines

- **State tailoring** — CGP varies by state; confirm BMP design standards, inspection frequencies, stabilization deadlines, and reporting thresholds `[VERIFY]`
- **303(d) / TMDL waters** — trigger enhanced BMPs and potentially numeric effluent limits; flag prominently in site description
- **MS4 permits** — check for local requirements beyond the CGP
- **Multi-operator sites** — each operator needs own SWPPP or clearly defined responsibilities in shared plan
- **Do not certify** — include signature blocks but operator (not drafter) must sign
- **Linear projects** (roads, utilities) — use phased approach with separate BMP plans per active segment
- **Federal citations**: 40 CFR § 122.26, 40 CFR § 450.21, CWA § 402 `[VERIFY CGP version year against current EPA issuance]`
- **Mark all state-specific citations** with `[VERIFY]` unless user provides applicable state CGP

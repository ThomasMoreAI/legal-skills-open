---
name: hazardous-waste-manifest
title: Hazardous Waste Manifest (EPA Form 8700-22)
description: Drafts a Uniform Hazardous Waste Manifest (EPA Form 8700-22) compliant with RCRA, EPA, and DOT requirements. Assembles generator, transporter, and TSDF chain-of-custody data with 40 CFR Parts 261–265 waste coding, DOT classification under 49 CFR Parts 171–180, certification language, and discrepancy reporting. Use when preparing manifest packages for hazardous waste shipments, RCRA tracking documents, or waste disposal compliance filings.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/hazardous-waste-manifest
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: environmental
language: en
tags: [drafting, regulatory]
---

# Hazardous Waste Manifest (EPA Form 8700-22)

Drafts a RCRA-compliant Uniform Hazardous Waste Manifest establishing chain of custody from generation through final disposal.

## Prerequisites

1. **Generator EPA ID** — 40 CFR Part 262 registration; physical site address
2. **Transporter records** — EPA ID, DOT registration, permit status per carrier
3. **TSDF authorization** — facility EPA ID, state permits confirming acceptance of waste type/quantity
4. **Waste characterization** — DOT proper shipping name, EPA waste codes (40 CFR Part 261), quantity, container count/type, hazard class, packing group
5. **Emergency contact** — 24-hour number (CHEMTREC or company line)

## Output Structure

### 1. Generator Information

| Field | Requirement |
|---|---|
| Legal business name | Full legal name |
| Generation site address | Physical (not mailing) |
| EPA ID number | 40 CFR Part 262 |
| Primary contact phone | Business hours |
| 24-hour emergency contact | Required for transport incidents |

### 2. Transporter Information *(repeat per carrier)*

| Field | Requirement |
|---|---|
| Company legal name | As registered with EPA |
| EPA ID number | 40 CFR Part 263 |
| DOT registration number | 49 CFR Parts 171–180 |
| Signature/date block | Custody receipt acknowledgment |

### 3. Designated Facility (TSDF)

| Field | Requirement |
|---|---|
| Facility legal name | As permitted |
| EPA ID number | Current registration |
| State permit numbers | DTSC or equivalent state authority |
| Permitted waste types | Must align with manifest waste codes |

> Verify TSDF authorization for specific waste type/quantity and LDR treatment standard compliance before designating.

### 4. Waste Description

| Field | Requirement |
|---|---|
| DOT proper shipping name | 49 CFR Part 172 |
| EPA hazardous waste codes | Four-digit codes, 40 CFR Part 261 |
| Quantity | Weight AND volume |
| Container type and count | DOT-approved specs |
| Physical/chemical form | Solid, liquid, sludge, etc. |
| Hazard class / packing group | DOT classification |
| Special handling | If applicable |

### 5. Certifications

- **Emergency number**: CHEMTREC (1-800-424-9300) or company line
- **Generator certification** (verbatim per 40 CFR 262.23):

```
I hereby declare that the contents of this consignment are fully and
accurately described above by the proper shipping name, and are classified,
packed, marked and labeled/placarded, and are in all respects in proper
condition for transport according to applicable international and national
governmental regulations. If export shipment and I am the Primary Exporter,
I certify that the contents of this consignment conform to the terms of the
attached EPA Acknowledgment of Consent.
```

- Include waste minimization certification: volume/toxicity reduction program in place, disposal method minimizes health/environmental threats

### 6. Signatures & Discrepancy Reporting

Signature chain: generator representative → each transporter → receiving facility operator (each with date)

Discrepancy fields per **40 CFR 264.72 / 265.72**:
- [ ] Quantity variation (significant vs. non-significant)
- [ ] Container damage or count mismatch
- [ ] Waste type or description discrepancy
- [ ] Unacceptable waste notation
- [ ] Facility irregularity documentation

### 7. Copy Distribution

1. Generator retained copy
2. One copy per transporter
3. Designated facility (TSDF)
4. Return copy to generator as delivery/disposal proof

## Guidelines

- Final document must conform to EPA Uniform Manifest format (40 CFR Part 262, Subpart B)
- **State overlays**: CA, NY, and others require state-specific forms or additional fields — check state environmental agency requirements
- **Multi-transporter**: each carrier needs a separate signed acknowledgment block; verify current EPA and DOT credentials
- **LDR**: confirm TSDF is authorized for applicable land disposal restriction treatment standards
- **Discrepancy threshold**: significant quantity discrepancies trigger EPA regional office notification — flag for attorney review
- **Retention**: generator must retain copies minimum 3 years per 40 CFR 262.40 [VERIFY against recent RCRA amendments]

---
name: fda-device-registration
title: FDA Establishment Registration & Device Listing
description: Drafts FDA Establishment Registration and Device Listing documents compliant with 21 CFR Part 807. Structures filings with establishment details, owner/operator information, device inventories, compliance certifications, and signature blocks mirroring FDA Form 2830. Triggers on initial registrations, annual renewals, listing updates, or foreign establishment filings requiring US agent designations.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/fda-device-registration
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: regulatory
language: en
tags: [drafting, checklist]
---

# FDA Establishment Registration & Device Listing

Drafts a 21 CFR Part 807 registration and device listing document structured for FDA submission via FURLS.

## Prerequisites

1. **Establishment details** — legal name, FEI number, physical/mailing addresses, business activities
2. **Owner/operator information** — legal names, titles, contact details, signature authority
3. **Device inventory** — product codes, classifications, intended uses, listing numbers, 510(k) numbers
4. **US agent info** (foreign establishments only) — name, address, phone, email
5. **Prior submissions** — previous registration numbers, listing numbers, any pending 510(k)s

## Output Structure

### Document Header

| Field | Content |
|-------|---------|
| Title | Establishment Registration and Device Listing |
| Regulatory basis | 21 CFR Part 807 |
| FDA Form | 2830 (confirm current version at FDA.gov) |
| Preparation date | [Date] |
| Filing type | Initial / Annual Renewal / Update |

### 1. Establishment Information

- Legal owner name (must match corporate records)
- FEI number
- Physical address and mailing address (if different)
- Phone, fax, email
- Business activities — use only FDA-recognized terms: Manufacturer, Contract Manufacturer, Repackager/Relabeler, Specification Developer, Reprocessor of Single-Use Devices, Foreign Manufacturer, Sterilizer, Component Manufacturer

### 2. Owner/Operator Details

For each responsible party:
- Full legal name and title
- Signature authority designation
- Contact information
- Confirmation of legal authority to bind establishment

### 3. Device Listing

For each device:

| Field | Requirement |
|-------|-------------|
| Device name | Common/trade name |
| FDA product code | 3-letter code from FDA classification database |
| Classification | Class I, II, or III |
| Intended use | Technical description aligned with labeling |
| Listing number | If previously assigned |
| 510(k) number | If applicable |
| Predicate device | If applicable |
| Premarket exempt? | Yes/No with regulatory citation |

### 4. Compliance Certifications

- [ ] 21 CFR Part 807 registration requirements
- [ ] QSR compliance (21 CFR Part 820) where applicable
- [ ] Device classifications accurately represented
- [ ] US agent designated (foreign establishments — 21 CFR 807.40)
- [ ] Claimed exemptions cited with regulatory authority and justification
- [ ] MDR reporting obligations acknowledged (21 CFR Part 803)

### 5. Foreign Establishment — US Agent

If applicable:
- Agent name, company, address, phone, email
- Written agreement confirmation per 21 CFR 807.40(c)

### 6. Signatures & Attestations

- Printed name, title, date, signature line
- Attestation: accuracy/completeness of information, acknowledgment of 18 U.S.C. § 1001, authority to bind establishment
- Owner/operator signature required; additional signatories as needed

## Guidelines

- Use only FDA-recognized activity descriptions and product codes — never paraphrase
- Verify FEI number matches FURLS records
- All device classifications must match the current FDA Product Classification Database
- Structure output to mirror FDA Form 2830 field order for electronic submission transfer
- Do not fabricate product codes, FEI numbers, or 510(k) numbers — flag missing data with `[REQUIRED — obtain from client]`
- Mark unverified citations with `[VERIFY]`

## Troubleshooting

- **Missing FEI number** — flag as `[REQUIRED — obtain from client]`; do not guess or generate
- **Unrecognized business activity** — map to the closest FDA-recognized term and flag with `[VERIFY]`
- **Foreign establishment without US agent** — halt drafting of Sections 4–5 and request agent designation details
- **Annual renewal window** — registration renews October 1–December 31 each year; listing updates due within 30 days of any distribution status change

---

Key changes from the original:

- **Tags**: Replaced `memo` and `research` with `checklist` — this skill produces a regulatory filing with checklists, not a memo or research output
- **Description**: Tightened to third-person with explicit trigger guidance ("Triggers on...")
- **Section headers**: Removed redundant "Section N:" prefix pattern, simplified to numbered headings
- **Compliance section**: Stripped "Include statements covering:" preamble — the checklist speaks for itself
- **Guidelines**: Consolidated from 8 verbose bullet points to 6 concise ones; moved the annual renewal/listing update deadlines into Troubleshooting where they serve as actionable guidance
- **Added Troubleshooting**: Required by the spec — covers the four most common blocking scenarios
- **Reduced from 101 to 93 lines** while adding a new section

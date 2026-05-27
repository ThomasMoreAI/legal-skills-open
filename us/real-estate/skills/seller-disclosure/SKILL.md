---
name: seller-disclosure
title: Seller Disclosure Statement
description: 'Drafts residential Seller Disclosure Statements for U.S. real estate transactions covering structural systems, environmental hazards, title encumbrances, and neighborhood conditions. Enforces state-specific statutory compliance and federal lead-based paint requirements. Trigger keywords: "seller disclosure", "property condition statement", "residential transfer disclosure", "seller disclosure statement".'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/seller-disclosure
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: real-estate
language: en
tags: [agreement, drafting, transactional]
---

# Seller Disclosure Statement

Draft a legally compliant residential Seller Disclosure Statement that satisfies state and federal requirements while protecting sellers from post-closing liability.

## Prerequisites

1. **Property identification** — legal description, APN, full address, county
2. **Seller information** — full legal names of all title holders
3. **State jurisdiction** — determines statutory requirements, format, and delivery timeframes
4. **Available documents** — inspection reports, repair invoices, HOA docs, surveys, environmental reports, prior disclosures
5. **Property age** — if pre-1978, federal lead-based paint disclosure is mandatory (42 U.S.C. § 4852d)

## Output Structure

### 1) Document Header

- All sellers' full legal names (as on title)
- Complete property identification (address, APN, legal description)
- Governing state disclosure statute citation
- Seller knowledge-and-belief attestation
- Buyer notice: disclosure is not a warranty; independent inspections recommended

### 2) Document Extraction

Search uploaded documents for required data:

| Data Point | Sources |
|---|---|
| Seller names | Deed, title report |
| Property ID (APN, legal) | Tax records, title report |
| Known defects & repairs | Inspection reports, invoices, correspondence |
| Environmental conditions | Environmental reports, FEMA maps, radon tests |
| HOA details | CC&Rs, HOA statements, assessment notices |
| Permits & code compliance | Building permits, certificates of occupancy |
| Easements & encumbrances | Title report, survey |

### 3) Structural & Systems Disclosures

For each system, disclose: **condition, age, known defects, repair history (contractor + date + warranty), materials of concern**.

| System | Key Disclosure Points |
|---|---|
| Foundation | Cracks, settlement, water intrusion, past repairs + warranties |
| Roof | Age, composition, leak history, warranty status |
| Plumbing | Pipe materials (flag polybutylene/galvanized), leaks, sewer vs. septic |
| Electrical | Panel amperage, aluminum wiring, GFCI presence, code violations |
| HVAC | Equipment age, fuel type, maintenance history, deficiencies |
| Water heater | Age, capacity, fuel type, condition |

Cite specific inspection reports or invoices by name and date.

### 4) Environmental & Federal Disclosures

**Lead-based paint (pre-1978 — mandatory):**
- Disclose known/unknown presence of lead-based paint or hazards
- Note buyer receives EPA pamphlet "Protect Your Family from Lead in Your Home"
- Include 10-day inspection right (unless negotiated otherwise)

**Additional environmental items:**

| Hazard | Disclosure Requirements |
|---|---|
| Asbestos | Location, testing/abatement history |
| Radon | Test results or "no testing conducted" statement |
| Flooding | Event history (date, source, damage, claims, remediation); FEMA SFHA status |
| Underground tanks | Status (in use/abandoned/removed); soil contamination; remediation |
| Mold/moisture | Locations, water damage history, remediation |
| Hazardous waste | Federal/state database listings, former industrial use |
| Natural hazards | Fault zones, seismic areas, wildfire zones (per state requirements) |

### 5) Legal Encumbrances & Title

- **Easements** — purpose, location, practical impact
- **Boundary disputes** — nature, parties, resolution status
- **HOA** — name, contact, assessments, special assessments, pending litigation, violations
- **Zoning** — classification, non-conforming uses/structures
- **Permits** — pulled permits, final inspection status; flag unpermitted work explicitly
- **Code violations** — notices, compliance orders, current status
- **Use restrictions** — rental, age, occupancy limitations from CC&Rs or local ordinances

### 6) Neighborhood & Area Conditions

Disclose material facts affecting value or desirability:
- Noise sources (airports, highways, railroads, commercial/industrial)
- Proximity to waste facilities, agricultural operations
- Planned public improvements and upcoming special assessments
- Deaths on property — **check state statute** (requirements vary by jurisdiction)
- Any other fact a reasonable buyer would consider material

### 7) Certification & Execution

**Seller certification:**
- Truth and correctness attestation (under penalty of perjury)
- Duty to amend if new material facts arise before closing
- Disclosure is not a warranty and does not substitute for buyer inspections

**Signature block:**
- Signature line for every owner (printed name + date)
- Separate buyer acknowledgment section (receipt + right to inspect)

**Delivery:** State the statutory deadline (typically 3–10 days around contract execution). Note buyer rescission rights for late delivery.

## Final Review Checklist

- [ ] Every section completed — no blanks (use "N/A" with seller initials for inapplicable items)
- [ ] Referenced documents attached as numbered exhibits with table of contents
- [ ] Page numbers + footer (property address + disclosure date) on every page
- [ ] State-specific mandatory disclosures verified against statutory checklist
- [ ] Language is factual and objective — not promotional or minimizing
- [ ] Lead-based paint disclosure included if pre-1978
- [ ] Federal, state, and local requirements all addressed

## Guidelines

- **Identify the governing statute first** — disclosure requirements, format, delivery timing, and rescission rights differ materially across states
- **"Unknown" is valid** — clearly distinguish "not present," "unknown," and "not inspected"; never fabricate conditions
- **Over-disclose** — undisclosed material defects create post-closing liability; disclosed items rarely do
- **Never advise concealment** — disclosure obligations are non-negotiable; ethics rules and statutes prohibit material omission
- **Ongoing duty** — remind sellers that amendments are required if conditions change before closing
- **Verify all statutory citations** against current state law [VERIFY]

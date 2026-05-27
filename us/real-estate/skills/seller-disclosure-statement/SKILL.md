---
name: seller-disclosure-statement
title: Seller Disclosure Statement (Residential)
description: Drafts a U.S. residential Seller Disclosure Statement covering property condition, system ages, defects, environmental hazards, title/HOA matters, and buyer acknowledgment. Triggered by requests for seller disclosures, property condition disclosure, TDS, SPDS, lead-based paint disclosure, or pre-close compliance in residential sales.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/seller-disclosure-statement
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: real-estate
language: en
tags: [agreement, drafting, transactional]
---

# Seller Disclosure Statement (Residential)

Produces a state-compliant seller disclosure for a residential property sale.

## Quick Start

Gather before drafting:

1. **Jurisdiction** — state, county, governing disclosure statute, required form
2. **Property** — address, APN/parcel ID, legal description, year built
3. **Sellers** — all record owners per title
4. **Records** — inspections, repair invoices, permits, warranties, HOA docs, surveys
5. **Known issues** — defects, prior damage, environmental conditions, disputes, encumbrances
6. **Timing** — contract date, statutory delivery window, closing date

## Document Structure

### Header

- Title: `Seller Disclosure Statement`
- Seller(s) full legal names
- Property: address, county, APN, legal description, year built
- Governing statute/form: `[STATE STATUTE / REQUIRED FORM NAME]`
- Knowledge qualifier: "to the best of Seller's knowledge and belief"
- Notice: disclosure is not a substitute for buyer inspections

### Core Disclosure Sections

Complete all; use `N/A` where not applicable.

| Section | Key Fields |
|---|---|
| Property Overview | Occupancy, year built, additions/remodels, boundary/survey issues |
| Structural | Foundation type, cracks/settlement/water intrusion, repairs (dates/contractor/warranty) |
| Roof/Exterior | Age/material, leaks/repairs, siding/doors/windows condition |
| Plumbing/Septic/Sewer | Pipe materials, leaks, sewer vs septic, last pump/inspection date |
| Electrical | Panel amperage, aluminum wiring, code issues, GFCI/AFCI, repairs |
| HVAC/Appliances | Type, age, fuel, maintenance history, defects |
| Water Heater | Age, capacity, fuel, condition |
| Interior | Water damage, mold, pests, floor/wall issues |
| Environmental | Lead paint (pre-1978), asbestos, radon, USTs, soil contamination, flood history |
| Natural Hazards | Earthquake, wildfire, landslide, flood zone per state report |
| Legal/Title | Easements, encroachments, boundary disputes, liens, judgments |
| HOA/CC&Rs | Name, dues, special assessments, violations, pending litigation |
| Zoning/Permits | Zoning, nonconforming use, permits finaled, unpermitted work |
| Governmental | Violation notices, code enforcement, condemnation, compliance orders |
| Neighborhood | Nuisances, nearby industrial/ag uses, planned public projects |
| Deaths | Disclose only as state law requires |
| Other Material Facts | Anything a reasonable buyer would consider material |

### Lead-Based Paint Disclosure (pre-1978 only)

- Seller knowledge: `Known present / Known absent / Unknown`
- List any lead reports provided
- Buyer 10-day inspection right (or negotiated period)
- EPA pamphlet delivery acknowledgment

### Exhibits

Index every attachment by title and date. Include inspections, repair invoices, warranties, HOA docs, surveys, environmental reports.

### Certification & Acknowledgment

- Seller certification (under penalty of perjury if state requires)
- Ongoing duty to update through closing
- No-warranty disclaimer
- Signature lines for all sellers with dates
- Buyer receipt acknowledgment with dates

### Delivery Timing

- Statutory delivery window: `[INSERT STATUTORY WINDOW]`
- Buyer rescission/renegotiation rights: `[STATE-SPECIFIC]`

## Pitfalls & Checks

- Use factual, objective language only — no marketing.
- Cite sources by document name and date.
- Never leave blanks; use `N/A` and initial where required.
- Disclose unpermitted work explicitly with known risks.
- Deaths, crime, sex-offender disclosures vary by state — confirm statutory limits before including.
- Flood zone and natural hazard disclosures must match state-mandated reports.
- Mark uncertain citations `[VERIFY]` and request confirmation.
- All owners must sign; missing signatures can invalidate delivery.

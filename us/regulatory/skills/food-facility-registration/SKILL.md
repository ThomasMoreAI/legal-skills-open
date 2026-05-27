---
name: food-facility-registration
title: FDA Food Facility Registration
description: Drafts an FDA Food Facility Registration under FSMA and 21 CFR Part 1, Subpart H (21 U.S.C. 350d). Covers facility identity, food product categories, U.S. agent designation for foreign facilities, and certification language. Use when preparing new FDA facility registrations, biennial renewals, or registration updates for domestic or foreign food facilities.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/food-facility-registration
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: regulatory
language: en
tags: [drafting, memo]
---

# FDA Food Facility Registration

Drafts a registration filing under 21 CFR Part 1, Subpart H for domestic or foreign facilities manufacturing, processing, packing, or holding food for U.S. consumption.

## Prerequisites

Gather before drafting:

1. **Facility identity** — legal name, physical address (no P.O. Box), trade/DBA names, DUNS (if available)
2. **Parent company** — name, address, DUNS (if not independently owned)
3. **Food product categories** — all FDA product category codes for activities at the facility
4. **Operational type** — manufacturing/processing vs. storage/distribution
5. **U.S. Agent** (foreign facilities only) — name, U.S. physical address, phone, email
6. **Registration number** — for renewals or updates only
7. **Authorized signatory** — name, title, binding authority

## Quick Start

1. Confirm facility is **not exempt** under 21 CFR 1.226 (retail, restaurants, nonprofits, fishing vessels, farms)
2. Determine submission type: New | Renewal | Update
3. Collect all prerequisites above
4. Draft sections in order below
5. Include regulatory preamble and certification verbatim

## Output Sections

### Cover Page

| Field | Value |
|---|---|
| Document Title | FDA Food Facility Registration |
| Facility Legal Name | |
| Submission Date | |
| Submission Type | New / Renewal / Update |
| Contact for Filing | |

### Section 1 — Facility Information

| Field | Notes |
|---|---|
| Legal facility name | |
| Trade/DBA names | All operating names |
| Physical address | Street address; no P.O. Box |
| Mailing address | If different from physical |
| DUNS number | Optional |
| Phone / Email | |
| Parent company name & address | If applicable |
| FDA Registration Number | Renewals/updates only |

### Section 2 — Food Product Categories

List each product by FDA category code with:
- Category code and description
- Activity type: Manufacturing/Processing | Packing | Holding/Storage | Distribution

### Section 3 — U.S. Agent (Foreign Facilities Only)

For domestic facilities: mark *Not Applicable — Domestic Facility*.

| Field | Requirement |
|---|---|
| U.S. Agent legal name | |
| U.S. physical address | Must be in the United States |
| Phone | Reachable during all business hours |
| Email | |

The U.S. Agent serves as FDA's primary communication link for all inquiries.

### Section 4 — Regulatory Preamble

Include verbatim or substantially similar:

> This registration is submitted pursuant to Section 415 of the Federal Food, Drug, and Cosmetic Act (21 U.S.C. 350d) and the implementing regulations at 21 CFR Part 1, Subpart H. Registration does not constitute FDA approval of the facility or its products, nor does it exempt the facility from any other applicable FDA requirements.

### Section 5 — Certification and Attestation

Draft language affirming:
- Submitter has authority to legally bind the facility
- All information is true, accurate, and complete
- Facility agrees to permit FDA inspection and make FD&C Act records available

Include signature block: Authorized Signatory, Title, Date, Signature.

## Pitfalls and Checks

- **Exemption check** — Always verify 21 CFR 1.226 exemptions before drafting
- **Biennial renewal window** — October 1 – December 31 of each even-numbered year
- **Material changes** — Must update registration within **60 days** of any change
- **Enforcement risk** — Failure to register or update may result in administrative detention or import refusal
- **Submission channel** — Preferred: FDA Food Facility Registration Module (FFRM); note paper option if applicable
- **Field labeling** — Mark optional vs. required fields clearly to avoid submission errors
- **Jurisdiction** — U.S. federal filing only; no state-level analog required

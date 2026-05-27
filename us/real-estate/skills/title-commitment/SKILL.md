---
name: title-commitment
title: Title Commitment and Policy
description: Drafts ALTA-compliant Title Commitment documents for commercial real estate transactions including Schedule A, Schedule B Parts I and II. Use when preparing title commitments, preliminary title reports, title insurance policies, or pre-closing title documents.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/title-commitment
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: real-estate
language: en
tags: [agreement, drafting, transactional]
---

# Title Commitment and Policy

Drafts an ALTA-standard Title Commitment identifying state of title, requirements for policy issuance, and exceptions to coverage.

## Prerequisites

Collect before drafting:

- **Property** — legal description, APN, county, state
- **Transaction** — purchase price or loan amount, policy type (Owner's/Loan/Leasehold), closing date
- **Vesting** — current owner(s) of record with recording reference
- **Title search** — all encumbrances, liens, easements, CC&Rs, judgments from examination
- **Parties** — proposed insured(s), full legal names with entity designations
- **Encumbrances** — mortgages, deeds of trust, tax status, assessments to address at closing

## Document Structure

### Header

- Title: "COMMITMENT FOR TITLE INSURANCE"
- Issuing company: full legal name, jurisdiction-licensed
- Commitment number: `[YEAR]-[OFFICE CODE]-[SEQ]`
- Effective date: date through which title search was conducted

### Schedule A — Transaction Details

Draft in order:

1. **Policy type** — ALTA Owner's (2006), Loan, or Leasehold; specify form version
2. **Policy amount** — purchase price (owner's) or loan amount (lender's); format `$X,XXX,XXX.00`
3. **Proposed insured** — full legal names with entity designations; specify ownership percentages if multiple
4. **Current vesting** — owner(s) per most recent deed with recording reference (instrument number or book/page)
5. **Legal description** — verbatim from deed or survey; jurisdiction-appropriate format (metes and bounds, lot/block, government survey); include plat references; separate multiple parcels

### Schedule B, Part I — Requirements

List all conditions for policy issuance in closing-timeline order:

1. Premium and fees payment
2. Purchase price / loan funding confirmation via settlement statement
3. Conveyance instrument — deed executed, acknowledged, recorded
4. Existing lien releases — payoff statements + recorded satisfactions for all non-surviving mortgages, DOTs, judgment liens, tax liens
5. Owner's affidavit — possession, mechanic's liens, unrecorded interests, recent improvements
6. Entity authority — good standing, resolutions, incumbency certificates (if entity parties)
7. Survey — current ALTA/NSPS if needed to remove standard survey exception
8. Gap coverage — gap indemnity or bring-down search if effective-to-closing gap exists

Distinguish requirements due **before**, **at**, and **after** closing.

### Schedule B, Part II — Exceptions

Open with: policy will not insure against loss from the following unless removed or modified prior to closing.

**Standard exceptions** (removable by endorsement — note applicable ALTA endorsement form number):

- Rights/claims of parties in possession not in public records
- Easements not shown by public records
- Encroachments, boundary issues discoverable by survey/inspection
- Mechanic's/materialmen's liens not yet of record
- Taxes/assessments not yet shown as liens

**Specific exceptions** — each must include full detail:

| Type | Required Detail |
|------|----------------|
| Real property taxes | Current year status; prior year confirmation |
| CC&Rs | Recording reference; subdivision/HOA designation |
| Easements | Holder, purpose, location, recording ref; appurtenant vs. servient |
| Surviving mortgages/DOTs | Lender, original principal, recording ref, estimated balance |
| Judgments/liens | Creditor, amount, recording ref; property vs. owner's interest |
| Lis pendens | Case number, court, nature of action |
| Special assessments/CDD | Authority, purpose, amount, payment status |
| Mineral/subsurface rights | Scope of severance, recording reference |

## Pitfalls and Checks

- Every recorded-document reference needs jurisdiction-appropriate locator info (instrument number OR book/page OR official record number)
- Maintain exact consistency in party names, legal descriptions, and recording references throughout
- If assuming existing financing, except the surviving lien in Part II — do **not** list it as a requirement to release
- Do not draft endorsements inline; reference applicable ALTA endorsement form numbers only
- Spell out months in dates; use `$X,XXX,XXX.00` for dollar amounts
- Mark any unverifiable citation or statutory reference as `[VERIFY]`

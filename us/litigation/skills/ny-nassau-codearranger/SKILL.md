---
name: ny-nassau-codearranger
title: Nassau County Supreme Court
description: Use when drafting or filing in Nassau County Supreme Court (the 10th Judicial District, Long Island). Triggers include 'Nassau County Supreme Court', 'Mineola courthouse', '100 Supreme Court Drive', 'Nassau Commercial Division', 'Nassau IAS Part', 'Nassau County NYSCEF', 'Nassau MAP conference', 'Nassau matrimonial center'. Covers Nassau's Commercial Division (one of the most active outside NY County, with a $200,000 threshold), the Matrimonial Center, MAP (Mandatory Alternative Dispute Resolution) practice, and the 100 Supreme Court Drive courthouse complex.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/ny-court-docs/skills/ny-nassau
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Nassau County Supreme Court

> **NOT LEGAL ADVICE.** Verify the assigned Justice's Part
> Rules before every filing.

## At a glance

- **Court**: Supreme Court of the State of New York, Nassau
  County (10th Judicial District). The 10th JD also covers
  Suffolk County, but Suffolk cases are filed in Suffolk
  County Supreme Court (Riverhead).
- **Courthouse**: **100 Supreme Court Drive, Mineola NY
  11501** (with the Matrimonial Center at 400 County Seat
  Drive)
- **Commercial Division threshold**: **$200,000**
- **E-filing**: NYSCEF mandatory in most case types
- **Hearings**: Microsoft Teams + in-person hybrid; Nassau
  has been an early adopter of remote settlement conferences

## Distinctives

### Commercial Division activity

Nassau's Commercial Division is one of the most active
outside New York County, hearing complex business disputes
under 22 NYCRR § 202.70 (with Commercial Division Rules
applied), particularly involving Long Island corporate
matters and the metro-area financial sector. The $200,000
threshold is lower than NY County's $500,000.

### Matrimonial Center

Nassau operates a separate Matrimonial Center at 400 County
Seat Drive, with its own calendaring and IAS routing for
divorce, custody, and family-law matters. The Matrimonial
Center has dedicated settlement-conference parts.

### MAP / mandatory ADR

Nassau Supreme Court runs an active mediation and arbitration
program. Many civil cases are routed to MAP (Mandatory
Alternative Procedures) early; pro se litigants should expect
a Preliminary Conference order including ADR referral.

### Foreclosure volume

Like NYC counties, Nassau has substantial CPLR 3408
foreclosure-settlement-conference volume, processed through a
dedicated Foreclosure Settlement Conference Part.

## Filing checklist

1. **NYSCEF**: Summons + Complaint via NYSCEF; $210 fee
2. **RJI**: UCS-840 ($95 fee) for motion practice
3. **Service**: CPLR 306-b — within 120 days
4. **Preliminary Conference**: 22 NYCRR § 202.12 within 45
   days of RJI
5. **Notice of Motion**: returnable before the assigned IAS
   Part per Part Rules

## Part Rules

Nassau County Part Rules:
https://ww2.nycourts.gov/courts/10jd/nassau/civil/index.shtml

## Composition with other ny- skills

- `ny-statewide-format` — baseline format
- `ny-discovery` — CPLR Article 31 + Commercial Division
  Rules
- `ny-first-30-days` — answer / pre-answer motion triage
- `ny-file-packet` — NYSCEF assembly
- `ny-consumer-debt` — Nassau Civil Court covers debt-buyer
  cases under $25,000; over that, Supreme Court
- `ny-landlord-tenant` — Nassau District Court (separate
  trial court) covers L&T — cross-reference
  `ny-county-courts`

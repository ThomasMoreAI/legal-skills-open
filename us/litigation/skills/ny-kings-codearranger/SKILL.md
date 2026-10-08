---
name: ny-kings-codearranger
title: Kings County Supreme Court
description: Use when drafting or filing in Kings County Supreme Court (the 2nd Judicial District / Brooklyn). Triggers include 'Kings County Supreme Court', 'Brooklyn Supreme', '360 Adams Street', '2nd Judicial District motion', 'Kings County NYSCEF filing', 'Kings County Part Rules', 'Kings County Commercial Division', 'Kings County foreclosure settlement conference', 'CPLR 3408 conference', 'Brooklyn IAS Part'. Covers IAS Part routing, the Commercial Division ($150,000 threshold), CPLR 3408 mandatory foreclosure settlement conferences (heavily used in Kings County), and the 360 Adams Street courthouse.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/ny-court-docs/skills/ny-kings
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Kings County Supreme Court

> **NOT LEGAL ADVICE.** Verify the assigned Justice's Part
> Rules before every filing.

## At a glance

- **Court**: Supreme Court of the State of New York, Kings
  County (2nd Judicial District). The 2nd JD also covers
  Richmond County (Staten Island), but Richmond cases are
  filed in Richmond County Supreme Court.
- **Courthouse**: **360 Adams Street, Brooklyn NY 11201**
  (Cadman Plaza)
- **Index-number prefix**: e.g., `5[xxxxx]/YYYY` general
  civil; `5[xxxxx]/YYYY` Commercial Division (with RJI flag);
  matrimonial uses a separate prefix
- **Commercial Division threshold**: **$150,000** (lower
  than NY County's $500,000)
- **E-filing**: NYSCEF mandatory for most civil case types
- **Hearings**: Microsoft Teams for routine appearances;
  in-person for trials and contested evidentiary hearings

## Distinctives

### High foreclosure / consumer-debt volume

Kings County has historically processed more residential
foreclosures than any other NY county. **CPLR 3408**
mandatory foreclosure settlement conferences apply to every
home-loan foreclosure; the **Kings County Foreclosure
Settlement Conference Part** processes these in a centralized
calendar. Pro se homeowners commonly appear here.

Consumer-debt cases under $50,000 are filed in **Kings County
Civil Court** (141 Livingston Street) under the CCA (Civil
Court Act), not Supreme Court. See `ny-county-courts` for
Civil Court / Civil Court of the City of New York coverage.

### CPLR 3215(g)(3) — additional notice in consumer-credit default applications

In any consumer-credit transaction (the term echoes the new
CPLR 3015(e) and the FDCPA), CPLR 3215(g)(3) requires the
plaintiff to mail a copy of the summons with an extra notice
to the defendant at least 20 days before any default
application. Kings County clerks have historically rejected
default applications missing this notice. This rule was
*expanded* by the 2022 CCFA via 22 NYCRR § 202.27-a — see
`ny-consumer-debt`.

### IAS Part assignment in Kings County

After RJI, the case routes to an IAS Part under 22 NYCRR
§ 202.3. Kings County Part Rules: https://ww2.nycourts.gov/
courts/2jd/kings/civil/Civil_Part_Rules.shtml — verify the
assigned Justice's current rules every time, because page
limits, motion-conference requirements, and submission
protocols differ substantially across Parts.

### CPLR 4544 — small-print contracts

Kings County consumer cases routinely involve credit-card
agreements in small print. **CPLR 4544** bars admission of
any contract whose printed type is smaller than 8 points
unless a true and complete copy is provided. This is a
standard objection in Kings County consumer-debt defense —
see `ny-consumer-debt`.

## Filing checklist

1. **NYSCEF**: file Summons + Complaint via NYSCEF; pay $210
   index-number fee
2. **RJI**: file the RJI (UCS-840) before motion practice
   ($95 fee in commenced cases)
3. **Service**: CPLR Article 3 — within 120 days under CPLR
   306-b
4. **Preliminary Conference**: scheduled by the assigned
   IAS Part under 22 NYCRR § 202.12
5. **Notice of Motion**: returnable before the assigned IAS
   Part; conform timing to CPLR 2214(b) plus the Justice's
   Part Rules

## Common Kings County filings

- **Foreclosure settlement conference notice** under CPLR
  3408
- **Pre-answer motion to dismiss** under CPLR 3211 (often
  raising statute-of-limitations defense under the new CPLR
  213(a) 3-year SOL — see `ny-consumer-debt`)
- **Order to Show Cause** (CPLR 2214(d)) — common in
  emergency foreclosure cases (e.g., to stay sale)

## Composition with other ny- skills

- `ny-statewide-format` — baseline format rule
- `ny-consumer-debt` — foreclosure / debt-buyer defense in
  Kings County (often the highest-volume use case)
- `ny-landlord-tenant` — Kings County Civil Court housing
  practice (cross-reference for Supreme Court filers)
- `ny-discovery` — discovery mechanics
- `ny-schedule-hearing` — Part-Rule scheduling protocols
- `ny-file-packet` — NYSCEF assembly

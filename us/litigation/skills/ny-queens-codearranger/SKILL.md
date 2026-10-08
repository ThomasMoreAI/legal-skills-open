---
name: ny-queens-codearranger
title: Queens County Supreme Court
description: Use when drafting or filing in Queens County Supreme Court (the 11th Judicial District). Triggers include 'Queens County Supreme Court', '88-11 Sutphin Boulevard', 'Jamaica courthouse', 'Queens IAS Part', 'Queens Commercial Division', 'Queens County NYSCEF', 'Queens foreclosure conference', 'Queens settlement part'. Covers IAS Part routing, the Commercial Division ($150,000 threshold), CPLR 3408 foreclosure conferences (high volume in Queens), and the Jamaica courthouse.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/ny-court-docs/skills/ny-queens
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Queens County Supreme Court

> **NOT LEGAL ADVICE.** Verify the assigned Justice's Part
> Rules before every filing.

## At a glance

- **Court**: Supreme Court of the State of New York, Queens
  County (11th Judicial District)
- **Courthouse**: **88-11 Sutphin Boulevard, Jamaica NY
  11435**
- **Commercial Division threshold**: **$150,000**
- **E-filing**: NYSCEF mandatory in most civil case types
- **Hearings**: Microsoft Teams routine; in-person for
  trials

## Distinctives

### CPLR 3408 foreclosure volume

Queens has high residential-foreclosure filing volume,
processed through a dedicated Foreclosure Settlement
Conference Part under CPLR 3408. Pro se homeowners commonly
appear; the conference parts run a structured triage where
default-judgment dismissals are routinely vacated on a
homeowner request under the now-codified due-diligence
requirements.

### Diversity of business and consumer practice

Queens is the most ethnically diverse U.S. county, which
manifests in civil practice as: significant immigration-
adjacent civil matters (defamation, employment, business),
substantial consumer-debt defense volume, and translator-
availability scheduling complexity. The court's Pro Se
Office offers language-line support.

### IAS Part assignment

After RJI, the case routes to an IAS Part under 22 NYCRR
§ 202.3. Queens County Part Rules:
https://ww2.nycourts.gov/courts/11jd/supreme/civilterm/queens_partrules.shtml

## Filing checklist

1. **NYSCEF**: Summons + Complaint via NYSCEF; $210 fee
2. **RJI**: UCS-840 with $95 fee
3. **Service**: CPLR 306-b — within 120 days
4. **Preliminary Conference**: 22 NYCRR § 202.12 within 45
   days of RJI
5. **Notice of Motion**: returnable before assigned IAS Part

## Composition with other ny- skills

- `ny-statewide-format` — baseline format
- `ny-discovery` — CPLR Article 31 discovery mechanics
- `ny-first-30-days` — answer / pre-answer motion triage
- `ny-file-packet` — NYSCEF assembly
- `ny-consumer-debt` — debt-buyer defense (Queens Civil Court
  under $25,000; Supreme Court over)
- `ny-landlord-tenant` — Queens Housing Court
  cross-reference

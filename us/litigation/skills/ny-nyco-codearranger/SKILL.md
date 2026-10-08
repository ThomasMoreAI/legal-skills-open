---
name: ny-nyco-codearranger
title: New York County Supreme Court
description: Use when drafting or filing in New York County Supreme Court (the 1st Judicial District / Manhattan). Triggers include 'New York County Supreme Court', 'Supreme Court NY County', '60 Centre Street', '111 Centre Street', 'Manhattan Supreme', '1st Judicial District motion', 'Commercial Division NY County', '22 NYCRR § 202.70', 'index number starting with 65[xxxxx]', 'IAS Part [##]', 'NY County Part Rules', 'submit a motion to a Justice in Manhattan', 'NY County NYSCEF filing'. Covers IAS (Individual Assignment System) routing, the Commercial Division (22 NYCRR § 202.70 with the $500,000 threshold and 28 enumerated commercial matter types), Part Rules discovery (CPLR 3408 in foreclosure, Preliminary Conference under 22 NYCRR § 202.12), and the 60 Centre Street + 111 Centre Street courthouses.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/ny-court-docs/skills/ny-nyco
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# New York County Supreme Court

> **NOT LEGAL ADVICE.** Verify the assigned Justice's Part
> Rules before every filing. Part Rules vary case-by-case in
> New York County and override generic uniform-rule guidance.

## At a glance

- **Court**: Supreme Court of the State of New York, New York
  County (1st Judicial District)
- **Index-number prefix**: Commercial actions typically
  `65[xxxxx]/YYYY`; matrimonial `35[xxxxx]/YYYY`;
  uncontested matrimonial `30[xxxxx]/YYYY`. The first two or
  three digits of the index number indicate the case type.
- **Courthouses**:
  - **60 Centre Street** — primary civil courthouse; most
    IAS Parts; Commercial Division
  - **111 Centre Street** — Civil Court of the City of New
    York (a *separate* trial court — see `ny-county-courts`)
    plus some Supreme Court parts (Surrogate's annex, etc.)
  - **80 Centre Street** — additional Supreme Court space
  - **71 Thomas Street** — Matrimonial annex
- **E-filing**: NYSCEF mandatory (consensual in some legacy
  case categories; mandatory in commercial and consumer-credit
  actions since 2014–2022 rollouts)
- **Hearings**: Microsoft Teams for most appearances post-2020;
  in-person for trials and contested evidentiary hearings
- **Holiday list**: 22 NYCRR § 202.5-b NYSCEF treats holiday
  closures per NY Gen. Constr. Law § 24 — see `ny-deadlines`

## Assignment system: IAS (Individual Assignment System)

New York's **Individual Assignment System** (22 NYCRR § 202.3)
routes every case to a single IAS Justice at commencement.
That Justice owns the case through judgment. Practical
consequences:

- The Notice of Motion is **returnable before the assigned
  Justice's Part**, not before a generic motion calendar
- Each Justice publishes their own **Part Rules** ("Rules of
  Practice for Part [##]") — page limits, deadlines for
  pre-motion conferences, courtesy-copy requirements, oral-
  argument practice. **These supersede the uniform rules.**
- Find the Justice's Part Rules at
  https://ww2.nycourts.gov/courts/1jd/supctmanh/Part%20Rules.shtml
  (the "1jd" path is the 1st Judicial District index)

## Commercial Division (22 NYCRR § 202.70)

The Commercial Division is a separate division within Supreme
Court, NY County, for commercial disputes meeting two tests:

1. **Subject matter** — one of 28 enumerated categories in
   22 NYCRR § 202.70(b), including breach of contract among
   merchants, UCC matters, partnership / corporate dissolution,
   franchise disputes, certain consumer-class actions, certain
   intellectual-property matters
2. **Monetary threshold** — **NY County: $500,000** (excluding
   punitive damages, attorneys' fees, costs, interest). Other
   counties have lower thresholds (Nassau: $200,000; Westchester:
   $200,000; Kings/Bronx/Queens: $150,000; Erie: $50,000;
   Albany: $50,000; etc.).

Commercial Division Rules (22 NYCRR § 202.70(g)) are
substantially more rigorous than the uniform rules: 25-page
limit on memoranda (Rule 17), expedited discovery, mandatory
mediation (Rule 3), accelerated motion practice. Many of
these rules have **migrated to the broader Uniform Civil
Rules** over time (e.g., the 25-page limit became 22 NYCRR
§ 202.8-b in 2021 statewide). Always check the current
text of the operative rule.

## Filing checklist

1. **Commence the action**: file a Summons and Verified
   Complaint (or Summons + Notice / Summons + Complaint) plus
   a Request for Judicial Intervention (RJI, UCS-840) plus the
   $210 index-number fee (CPLR 8018) and the $95 RJI fee
   (where applicable). Issued via NYSCEF.
2. **Note of Issue / RJI**: filing the RJI assigns the case
   to an IAS Justice (22 NYCRR § 202.6). RJI not required at
   commencement but is required before any motion practice.
3. **Service**: under CPLR Article 3 — Summons + Complaint
   on every defendant within 120 days of filing (CPLR
   306-b). Affidavit of service filed via NYSCEF.
4. **Notice of Motion**: schedule a return date under the
   assigned Justice's Part Rules; conform timing to CPLR
   2214(b) — 8-day minimum service period, 16 days for cross-
   motions, longer if the Justice's Part Rules require pre-
   motion letters.

## Discovery in NY County

- **Preliminary Conference** under 22 NYCRR § 202.12 — held
  within 45 days of RJI; sets discovery deadlines
- **Compliance Conference** — mid-discovery checkpoint
- **Note of Issue** — certifies discovery complete (22 NYCRR
  § 202.21); within 90 days of note of issue, parties may
  file dispositive motions
- **Commercial Division Rule 11** allows expedited interim
  discovery practice

## Composition with other ny- skills

- `ny-statewide-format` — baseline format rule
- `ny-discovery` — CPLR Article 31 discovery mechanics
- `ny-schedule-hearing` — Part-Rule scheduling protocols
- `ny-first-30-days` — answer / motion-to-dismiss triage when
  served with an NY County complaint
- `ny-file-packet` — assembling an NYSCEF packet for NY
  County
- `ny-consumer-debt` — debt-buyer cases (often filed in NY
  County Civil Court, not Supreme Court — see
  `ny-county-courts`)

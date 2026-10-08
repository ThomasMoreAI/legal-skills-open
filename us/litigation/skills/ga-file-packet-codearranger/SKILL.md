---
name: ga-file-packet-codearranger
title: Assemble a Georgia Court Filing Packet
description: This skill should be used when assembling and filing a complete Georgia court motion or pleading packet. Triggers include "assemble my Georgia filing", "how do I e-file in Georgia", "what do I need to file a complaint", "PeachCourt vs Odyssey", "eFileGA", "Georgia filing checklist", "file a new civil action in Georgia", "Fulton e-filing", "what documents to start a Georgia lawsuit". Identifies the filing court and its e-filing platform (PeachCourt for Fulton/Cobb; Odyssey eFileGA for Gwinnett; the county map at georgiacourts.gov/efile-court-records), the documents a new civil action needs (complaint, summons, civil case initiation/disclosure form, filing fee or O.C.G.A. § 9-15-2 pauper's affidavit, sheriff's entry of service), the USCR 36 e-filing mechanics, service of process under O.C.G.A. § 9-11-4, and for domestic cases the auto-attaching standing orders plus the required DRFA and Child Support Worksheet. Provides a pre-flight checklist.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/ga-court-docs/skills/ga-file-packet
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Assemble a Georgia Court Filing Packet

> **NOT LEGAL ADVICE.** This skill is a procedural and drafting aid,
> not legal advice. Verify current rules, deadlines, and
> venue-specific practices before filing. Pair with substantive review
> by counsel where stakes warrant.

Use this skill when ready to **submit** a Georgia court filing —
whether starting a new civil action or filing into an existing case.

## Step 1 — Identify the court and its e-filing platform

Georgia e-filing is governed by **USCR 36** and was made mandatory for
civil filings statewide (SB 407, effective ~January 1, 2019). The
platform is **county-dependent**:

| County | Platform | Mandatory civil e-file |
|---|---|---|
| **Fulton** | eFileGA / PeachCourt (Tyler Odyssey backbone) | Yes — Superior, State, and Magistrate (no paper, including dispossessory/garnishment) |
| **Cobb** | PeachCourt (GreenCourt) | Yes — Superior civil since Oct. 1, 2018 |
| **Gwinnett** | Odyssey eFileGA (Tyler) | Yes — all State and Superior civil; Magistrate optional |

For every other county, check the official map at
**georgiacourts.gov/efile-court-records** before filing — do not assume
PeachCourt or Odyssey covers a given county.

Confirm the **court layer** is right before filing: Superior (general
jurisdiction; exclusive over divorce, equity, title to land,
felonies), State (civil of any amount except the Superior-exclusive
subjects), or Magistrate ($15,000 cap, § 15-10-2(5); dispossessory and
garnishment within the cap). See `ga-state-court`, `ga-magistrate`,
and the venue skills.

## Step 2 — Assemble a new civil action

A new civil action filed in Superior or State Court typically needs:

| # | Document | Notes |
|---|----------|-------|
| 1 | **Complaint** | O.C.G.A. § 9-11-10 caption + numbered paragraphs; § 9-11-8 short-and-plain statement |
| 2 | **Summons** | Issued by the clerk; PeachCourt/Odyssey can auto-generate it |
| 3 | **Civil Case Initiation / Disclosure Form** | Required cover-sheet form; e-filing portals auto-generate or prompt for it |
| 4 | **Filing fee** — or **§ 9-15-2 pauper's affidavit** | File the affidavit of indigence **with** the complaint if seeking a fee waiver (see `ga-pro-se`) |
| 5 | **Sheriff's Entry of Service** | The service-return form for the sheriff or process server; portals can auto-generate it |

On Fulton's PeachCourt and Cobb's PeachCourt, the system
**auto-generates** the Case Initiation Form, Disclosure, Summons, and
Sheriff's Entry of Service. On Gwinnett's Odyssey eFileGA, confirm
which forms are auto-populated versus uploaded.

## Step 3 — E-filing mechanics (USCR 36)

1. Log in to the county's platform (register a free account if needed;
   pro se filers can register).
2. Start a new case (initial filing) or search the existing case by
   number or party name (subsequent filing).
3. Select the **filing/document type** for each component from the
   portal menu.
4. Upload each component as a separate PDF (or let the portal generate
   the auto-forms).
5. Pay the filing fee by card, or attach the **§ 9-15-2 pauper's
   affidavit** for a fee waiver.
6. Submit; the portal returns a file-stamped, time-stamped
   confirmation.

USCR 36 also governs the format and signature conventions for
e-filed documents; an electronic signature ("/s/ Name") is accepted.

## Step 4 — Service of process (O.C.G.A. § 9-11-4)

Filing is **not** service. After the clerk issues the summons:

- **Service of process** of the summons + complaint follows **O.C.G.A.
  § 9-11-4** — personal service, service on a registered/statutory
  agent, the methods in § 9-11-4(f) (including publication), or
  acknowledgment/waiver under **§ 9-11-4.1**. Use the **sheriff** of
  the county where the defendant is found or a court-appointed process
  server; a party cannot serve their own case.
- The process server completes and files the **Sheriff's Entry of
  Service** to make the return of service part of the record.
- **Service of subsequent papers** follows **O.C.G.A. § 9-11-5**;
  e-filing through the portal generally e-serves other registered
  parties, and every paper carries a **certificate of service**.

## Step 5 — Domestic cases: standing orders + required forms

In divorce, custody, and related domestic actions (Superior Court
exclusively):

- **Standing orders auto-attach.** In Fulton, Cobb, and Gwinnett the
  domestic-relations standing order (and, where applicable, a
  co-parenting/seminar standing order) **attaches automatically** at
  filing through the e-filing portal. These typically restrain asset
  disposal outside the ordinary course, harassment, insurance changes,
  and child removal, and may require a parenting seminar. Read the
  attached order — violation is contempt. See `ga-family-law` and
  `ga-family-court`.
- **DRFA** — the **Domestic Relations Financial Affidavit** under
  **USCR 24.2** is required in cases involving financial issues.
- **Child Support Worksheet** — required where child support is at
  issue, computed with the Georgia Child Support Commission
  calculator (see `ga-family-law`). Local practice (e.g., Cobb) may
  require it filed and updated by set days before a hearing.

## Pre-flight checklist

| Check | Done |
|-------|------|
| Correct court layer confirmed (Superior / State / Magistrate) | ☐ |
| Correct county e-filing platform identified (map checked) | ☐ |
| All packet documents drafted and reviewed | ☐ |
| `scripts/format-check.py` passes on each `.docx` | ☐ |
| `ga-quality-check` pre-filing review complete | ☐ |
| `ga-fact-check` citation audit complete (high-stakes) | ☐ |
| Complaint + Summons + Case Initiation/Disclosure form ready | ☐ |
| Filing fee available **or** § 9-15-2 pauper's affidavit attached | ☐ |
| Sheriff's Entry of Service prepared for § 9-11-4 service | ☐ |
| Caption matches across all documents (court, county, file number) | ☐ |
| Certificate of service shows method, date, recipients (§ 9-11-5) | ☐ |
| Domestic only: DRFA (USCR 24.2) + Child Support Worksheet ready | ☐ |
| Domestic only: standing order(s) reviewed | ☐ |

## Composition

- For statewide format: `ga-statewide-format`
- For drafting each component: `ga-draft-motion`,
  `ga-draft-declaration`, `ga-draft-order`, `ga-draft-note`
- For pre-filing review: `ga-quality-check`, `ga-fact-check`
- For deadline computation: `ga-deadlines`
- For court-specific filing channels: `ga-fulton`, `ga-cobb`,
  `ga-gwinnett`, `ga-state-court`, `ga-magistrate`, `ga-county-courts`
- For pro se filers and fee waivers: `ga-pro-se`
- For post-filing scheduling: `ga-schedule-hearing`

## References

- `references/efiling-platforms.md` — PeachCourt vs. Odyssey eFileGA
  by county, USCR 36 mechanics
- `references/new-action-components.md` — complaint, summons, case
  initiation/disclosure, fee/pauper's affidavit, entry of service
- `references/service-of-process.md` — O.C.G.A. § 9-11-4 / § 9-11-4.1
  methods and the return of service

---
name: tn-file-packet-codearranger
title: Assemble a Tennessee Court Filing Packet
description: 'This skill should be used when assembling and filing a complete Tennessee court motion or pleading packet. Triggers include "file a Tennessee packet", "assemble my filing for a Tennessee court", "how do I e-file in Tennessee", "eFileTN filing", "Davidson Chancery e-filing", "Shelby eFlex filing", "TnCIS / Tybera e-filing", "what documents do I file with my Tennessee motion", "Tennessee filing checklist", "filing fee Tennessee", "do I file on paper or electronically in my county". Walks through assembly of the multi- document packet (motion + affidavit + proposed order + certificate of service + Notice of Hearing), determining the venue''s e-filing platform (county-by-county: eFileTN / Odyssey, eFlex, Tybera / TnCIS, or paper), the filing-fee question, the indigency / pauper''s oath alternative, and the difference between filing and service of process under Tenn. R. Civ. P. 4 and 5.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/tn-court-docs/skills/tn-file-packet
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Assemble a Tennessee Court Filing Packet

> **NOT LEGAL ADVICE.** This skill walks through filing mechanics.
> Verify the e-filing platform, document types, fees, and pro-se
> acceptance with the filing court's clerk before submitting.

Use this skill when ready to **submit** a Tennessee trial-court
filing. The first thing to determine is **which filing channel the
venue uses** — there is no single statewide mandate.

## Tennessee e-filing is county-by-county — not a single statewide system

Tennessee trial-court e-filing is adopted **county by county**, on
different platforms, and is **not** universally mandatory. Confirm,
for the specific court:

1. **Which platform** the court uses; and
2. **Whether e-filing is mandatory** or paper is still accepted.

| Venue | Platform (verify currency) |
|---|---|
| **Davidson Chancery (Nashville)** | eFileTN / Odyssey (Tyler Technologies) |
| **Shelby (Memphis)** | eFlex |
| **Some other counties** | Tybera (often paired with the TnCIS case-management system) |
| **Many smaller counties** | Paper filing at the clerk's window |
| **All appellate courts (statewide)** | The **AOC e-filing portal** — statewide for the Tennessee appellate courts |

So: **trial-court e-filing is fragmented by county**, while
**appellate e-filing is statewide through the AOC portal.** Do not
assume a trial court accepts e-filing — check first.

## E-filing workflow (generic)

The platforms differ, but the shape is consistent:

1. Log in / register an account on the venue's platform
2. Search for the case by docket number or party name (or start a new
   case for an initial filing)
3. Select the **filing / document type** for each component
4. Upload each component as a **separate PDF** (the platform may
   require text-searchable PDFs and bookmarks for long filings —
   verify)
5. Pay any filing fee, or attach the indigency / pauper's-oath
   paperwork
6. Submit; the platform returns a stamped acceptance / file-stamp
   confirmation

For paper filing, bring clean copies to the clerk's window during
business hours; the clerk file-stamps the original and returns a
stamped copy. Confirm whether the court accepts drop-box filings.

## Multi-document packet — typical components

A standard Tennessee motion packet consists of these documents:

| # | Document | Authority / note |
|---|----------|------|
| 1 | Motion | Tenn. R. Civ. P. 7.02 |
| 2 | Memorandum of law (if used) | Local rules may require / limit |
| 3 | Supporting affidavit (sworn) | Tenn. R. Evid. 803(6) foundation for business records |
| 4 | Exhibits | Tenn. R. Civ. P. 10.03 — attach written instruments |
| 5 | Proposed Order | Submitted with the motion; see `tn-submit-order` |
| 6 | Certificate of Service | Tenn. R. Civ. P. 5 — date, method, recipients |
| 7 | Notice of Hearing | After the date is cleared; see `tn-schedule-hearing` |

Choose the closest matching document-type label in the platform's
menu; the menus vary by court.

## Preflight — run the helper scripts

Before assembling the packet:

```
# Format / Rule 10.01 caption check (typography items report as WARN —
# Tennessee has no statewide page/margin rule; those are local)
python3 plugins/tn-court-docs/scripts/format-check.py path/to/filing.docx

# Deadline arithmetic — Rule 6.01 computation, Rule 6.05 3-day mail
# add-on, Tenn. Code Ann. § 15-1-101 holidays
python3 plugins/tn-court-docs/scripts/case-calendar.py ...
```

Use `case-calendar.py` to confirm a Rule 56 motion's hearing is set
**at least 30 days** after service (Tenn. R. Civ. P. 56.04), and to
compute any response deadline with the 3-day mail add-on.

## Filing fees

Filing fees are set by statute and by the clerk's fee schedule and
vary by court and case type. **Confirm the current amount with the
filing court's clerk** before submitting; do not hard-code a figure.
Pay by the platform's accepted method (card / e-check) or at the
clerk's cashier window for paper filings.

### Indigency — pauper's oath

A filer who cannot afford the fees may file an **affidavit of
indigency** (pauper's oath) to proceed without prepaying court costs.
Submit the indigency affidavit **with** the first filing — do not pay
and seek a refund later. Verify the current form and the statutory
basis with the clerk; the court reviews and may require additional
information.

## Filing vs. service — two distinct steps

Filing with the court is **not** the same as serving the opposing
party:

1. **Filing** — through the venue's e-filing platform or at the
   clerk's window.
2. **Service of process** (initial summons + complaint) — under
   **Tenn. R. Civ. P. 4**: summons issued by the clerk; process is
   served and the return made; the summons must be issued / served
   and returned within the time the rule allows (Rule 4 carries a
   90-day issuance / return framework — verify the current text).
3. **Service of subsequent papers** (motions, notices, orders) —
   under **Tenn. R. Civ. P. 5**: on every party, by the methods the
   rule allows; document it in the Certificate of Service. When
   service is by mail, add **3 days** to any responsive deadline
   under **Tenn. R. Civ. P. 6.05**.

If the e-filing platform performs electronic service on registered
parties, a pro-se opposing party without an account must still be
served by an approved Rule 5 method (mail or hand delivery) — confirm
the platform's e-service coverage.

## General Sessions note

General Sessions practice is **informal** and the Tennessee Rules of
Civil Procedure do not apply there except as specifically made
applicable. A General Sessions civil matter is commenced by a **civil
warrant** with a **return date**, filed at the General Sessions
clerk's office. The packet-assembly model in this skill is geared to
Circuit / Chancery motion practice; for General Sessions, see
`tn-general-sessions`.

## Pre-filing checklist

| Check | Done |
|-------|------|
| Venue's e-filing platform identified (eFileTN / eFlex / Tybera / paper) and mandatory-vs-optional confirmed | ☐ |
| `scripts/format-check.py` run; no FAIL (WARN items confirmed against local rules) | ☐ |
| `scripts/case-calendar.py` confirms timing (Rule 56.04 30-day, Rule 6.05 mail add-on) | ☐ |
| `tn-quality-check` pre-filing review complete | ☐ |
| `tn-fact-check` deep audit complete (high-stakes filing) | ☐ |
| Caption (court / county / docket number) matches across all documents (Rule 10.01) | ☐ |
| Exhibits attached (Rule 10.03) | ☐ |
| Proposed Order drafted as a separate document | ☐ |
| Each component saved as a separate PDF | ☐ |
| Signature block has BPR # (attorney) or "Pro Se" (Rule 11) | ☐ |
| Certificate of Service shows method, date, recipients (Rule 5) | ☐ |
| Personal identifiers redacted per the venue's redaction rule | ☐ |
| Filing fee available, or indigency affidavit ready | ☐ |
| Service-of-process plan (Rule 4) / service-of-papers plan (Rule 5) ready | ☐ |

## Composition

- For statewide format baseline: `tn-statewide-format`
- For drafting each component: `tn-draft-motion`,
  `tn-draft-declaration`, `tn-draft-order`, `tn-draft-note`
- For pre-filing review: `tn-quality-check` (lighter) and
  `tn-fact-check` (deep evidentiary)
- For clearing the hearing date and the Notice of Hearing:
  `tn-schedule-hearing`
- For court-specific filing channels and local rules: `tn-davidson`,
  `tn-shelby`, `tn-knox`, `tn-hamilton`, `tn-county-courts`
- For General Sessions civil-warrant practice: `tn-general-sessions`
- For pro-se filers (indigency affidavit, self-represented
  conventions): `tn-pro-se`
- For deadline arithmetic: `tn-deadlines`
- For post-hearing order submission: `tn-submit-order`

## References

- `tn-law-references` for Tenn. R. Civ. P. 4, 5, 6, 10, and 56.04 text
- The AOC website (tncourts.gov) and the filing court's clerk for the
  current e-filing platform, document types, and fee schedule
- Confirm whether e-filing is mandatory in the venue before assuming
  a channel — Tennessee trial-court e-filing is county-by-county.

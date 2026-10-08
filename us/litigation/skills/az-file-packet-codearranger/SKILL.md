---
name: az-file-packet-codearranger
title: Assemble an Arizona Court Filing Packet
description: Use when assembling and filing a complete Arizona court motion or pleading packet. Triggers include "file an Arizona court packet", "assemble Arizona filing", "AZTurboCourt e-filing", "how do I e-file in Arizona", "what documents do I file with my Arizona motion", "Arizona filing checklist", "redact sensitive data Arizona", "protect sensitive information Arizona filing", "Arizona filing fee", "fee deferral A.R.S. 12-302", "defer or waive Arizona court fees", "do I file on paper or electronically in Arizona". Walks through assembling the multi-document packet (motion + memorandum + proposed form of order + affidavit/declaration + certificate of service + exhibits), the AZTurboCourt e-filing channel and whether it is mandatory in the venue, the Arizona sensitive-data redaction rule, the filing-fee question and the A.R.S. § 12-302 deferral/waiver, and paper filing where applicable.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/az-court-docs/skills/az-file-packet
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Assemble an Arizona Court Filing Packet

> **NOT LEGAL ADVICE.** This skill walks through filing mechanics.
> Verify the e-filing platform, document types, fees, redaction
> rule, and pro-se acceptance with the filing court's clerk before
> submitting.

Use this skill when ready to **submit** an Arizona trial-court
filing. First determine the **filing channel** for the venue, then
assemble and preflight the multi-document packet.

## Arizona e-filing — AZTurboCourt

**AZTurboCourt** is the Arizona Judicial Branch's statewide e-filing
portal. E-filing is **mandatory for represented (attorney) filers in
many Superior Courts** for many case types, while **self-represented
filers may generally e-file or paper-file** — but coverage and
mandates vary by court and case type.

Before assuming the channel, confirm for the specific court:

1. **Whether AZTurboCourt is live** in that court for the case type;
2. **Whether e-filing is mandatory** (typically for attorneys) or
   whether paper / over-the-counter filing is still accepted; and
3. The court's accepted document types and any document-naming
   convention.

Where the court is not on AZTurboCourt for the case type, file on
**paper** at the clerk's window (see below). **Justice Court filing
differs** — many Justice Courts use a different e-filing pathway or
take paper; see `az-justice-courts`.

## E-filing workflow (AZTurboCourt)

The portal shape is consistent across courts:

1. Register / log in to an AZTurboCourt account
2. Search for the case by case number or party name (or start a new
   case for an initial filing)
3. Select the court, case category, and the **filing / document
   type** for each component
4. Upload each component as a **separate PDF** (text-searchable;
   verify any size / bookmark requirements for long filings)
5. Pay any filing fee, or attach the **A.R.S. § 12-302** deferral /
   waiver application
6. Submit; the system returns a filing confirmation / file-stamp and
   may effect electronic service on registered parties

## Paper filing (courts / case types not on AZTurboCourt)

Where e-filing is unavailable, bring clean copies to the clerk's
window during business hours; the clerk file-stamps the original and
returns a stamped copy. Confirm whether the court accepts mail or
drop-box filings, and how many copies (judge's copy / conformed
copy) the court wants.

## Multi-document packet — typical components

A standard Arizona motion packet consists of these documents:

| # | Document | Authority / note |
|---|----------|------|
| 1 | Motion | Ariz. R. Civ. P. 7.1 |
| 2 | Memorandum / supporting argument | Ariz. R. Civ. P. 7.1; page limits are local |
| 3 | Affidavit or declaration | Sworn affidavit or unsworn declaration; Ariz. R. Evid. 803(6) records foundation |
| 4 | Exhibits | Attach written instruments referenced in the motion |
| 5 | Proposed form of order | Submitted with the motion; see `az-submit-order` |
| 6 | Certificate of Service | Ariz. R. Civ. P. 5(c) — date, method, recipients |

Choose the closest matching document-type label in the AZTurboCourt
menu; the menus vary by court and case category.

## Sensitive / personal information — redaction

Arizona **restricts sensitive and personal information** in court
filings. Before filing, review every component (including exhibits)
and handle protected data as the governing rule requires —
generally by **omitting or partially redacting** identifiers such as
Social Security / financial-account numbers and similar data, and
using any required **sensitive-data cover sheet / addendum**
mechanism where the data must reach the court but be kept out of the
public file.

> Verify the exact rule and procedure against `az-law-references` —
> the sensitive-data duty is **Ariz. R. Civ. P. 5.1(e)** (refrain
> from including Social Security and financial-account numbers; only
> the last 4 digits may be used; the redaction responsibility rests
> solely with the filer), and **Ariz. R. Civ. P. 5.4** separately
> governs sealing a document / restricting public access. Confirm the
> precise list of protected identifiers, the partial-redaction
> format, and whether a sensitive-data cover sheet is required. The
> filing court may have additional local requirements.

The filing party is responsible for the redaction; the clerk does
not redact for you.

## Preflight — run the helper scripts

Before assembling the packet:

```
# Format / caption + form check
python3 plugins/az-court-docs/scripts/format-check.py path/to/filing.docx

# Deadline arithmetic — Ariz. R. Civ. P. 6 computation, Rule 5(c)
# service add-ons, with Arizona court-holiday handling
python3 plugins/az-court-docs/scripts/case-calendar.py ...
```

Use `case-calendar.py` to confirm any hearing lead time and to
compute response deadlines with the applicable service add-on.

## Filing fees

Filing fees are set by statute and the clerk's fee schedule and vary
by court and case type. **Confirm the current amount with the filing
court's clerk** before submitting; do not hard-code a figure. Pay by
the portal's accepted method (card / e-check) or at the clerk's
cashier window for paper filings.

### Fee deferral / waiver — A.R.S. § 12-302

A filer who cannot afford the fees may apply to **defer** or
**waive** filing fees and costs under **A.R.S. § 12-302**. A
**deferral** postpones payment (fees become due later, often as a
payment plan); a **waiver** excuses them outright. File the
application with the first filing rather than paying and seeking a
refund. The court reviews the application and enters an order
granting, denying, deferring, or waiving fees. Verify the current
§ 12-302 standard and the operative application form with the clerk.
See `az-pro-se`.

## Filing vs. service — two distinct steps

Filing with the court is **not** the same as serving the opposing
party:

1. **Filing** — through AZTurboCourt or at the clerk's window.
2. **Service of process** (initial summons + complaint) — under
   **Ariz. R. Civ. P. 4 / 4.1 / 4.2**, with the summons issued under
   Rule 4 (verify the current summons life / return period).
3. **Service of subsequent papers** (motions, notices, orders) —
   under **Ariz. R. Civ. P. 5**, on every party by an allowed
   method; document it in the **Certificate of Service** under
   Rule 5(c). Add the applicable service period under Rule 6 when
   service is by mail or other non-personal method.

If AZTurboCourt performs electronic service on registered parties, a
party without an e-filing account must still be served by another
allowed Rule 5 method — confirm the portal's e-service coverage for
each party.

## Pre-filing checklist

| Check | Done |
|-------|------|
| Filing channel identified (AZTurboCourt vs. paper) and mandatory-vs-optional confirmed for the court + case type | ☐ |
| `scripts/format-check.py` run; no FAIL | ☐ |
| `scripts/case-calendar.py` confirms any hearing lead time + service add-on | ☐ |
| `az-quality-check` pre-filing review complete | ☐ |
| `az-fact-check` deep audit complete (high-stakes filing) | ☐ |
| Caption (court / county / case number) matches across all documents | ☐ |
| Exhibits attached and referenced | ☐ |
| Proposed form of order drafted as a separate document | ☐ |
| Each component saved as a separate text-searchable PDF | ☐ |
| Signature block compliant — bar # (attorney) or self-represented designation | ☐ |
| Certificate of Service shows method, date, recipients (Ariz. R. Civ. P. 5(c)) | ☐ |
| Sensitive / personal information handled per the Arizona redaction rule (cover sheet where required) | ☐ |
| Filing fee available, or A.R.S. § 12-302 deferral/waiver application ready | ☐ |
| Service-of-process plan (Rule 4 et seq.) / service-of-papers plan (Rule 5) ready | ☐ |

## Composition

- For statewide format baseline: `az-statewide-format`
- For drafting each component: `az-draft-motion`,
  `az-draft-declaration`, `az-draft-order`, `az-draft-note`
- For pre-filing review: `az-quality-check` (lighter) and
  `az-fact-check` (deep evidentiary)
- For clearing the hearing date and the Notice of Hearing:
  `az-schedule-hearing`
- For court-specific filing channels and local rules: `az-maricopa`,
  `az-pima`, `az-superior-courts`, `az-justice-courts`
- For pro-se filers (A.R.S. § 12-302 deferral/waiver,
  self-represented conventions): `az-pro-se`
- For deadline arithmetic: `az-deadlines`
- For post-hearing order submission: `az-submit-order`

## References

- `az-law-references` for Ariz. R. Civ. P. 4, 4.1, 4.2, 5, 6, and 7.1
  text, the sensitive-data redaction duty under Rule 5.1(e), and the
  separate sealing/restricted-access rule at Rule 5.4
- The AZTurboCourt portal and the filing court's clerk for the
  current e-filing status, document types, and fee schedule
- Confirm whether e-filing is mandatory in the venue before assuming
  a channel — and remember Justice Court filing may differ
  (`az-justice-courts`).

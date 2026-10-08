---
name: tx-file-packet-codearranger
title: Assemble a Texas Court Filing Packet
description: Use when assembling and filing a complete Texas court motion or pleading packet through eFileTexas. Triggers include "file a Texas court packet", "assemble Texas filing", "eFileTexas", "eFile Texas petition", "Odyssey File & Serve Texas", "how do I e-file in Texas", "what documents do I file with my Texas motion", "Texas filing checklist", "civil case information sheet Texas", "Rule 78a case info sheet", "redact sensitive data Texas", "Texas filing fee", "Statement of Inability to Afford Payment". Walks through assembling the multi-document packet (petition/motion + proposed order + Notice of Hearing + certificate of service + civil case information sheet under TRCP 78a + the Rule 47(c) relief statement), enforces cross-document consistency, covers the eFileTexas channel and whether it is mandatory, the Texas sensitive-data redaction rule, the filing-fee and Statement-of-Inability question, and produces filing instructions.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/tx-court-docs/skills/tx-file-packet
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Assemble a Texas Court Filing Packet

> **NOT LEGAL ADVICE.** This skill walks through filing mechanics.
> Verify the e-filing platform, document types, fees, redaction rule,
> and self-represented acceptance with the filing court's clerk before
> submitting.

Use this skill when ready to **submit** a Texas trial-court filing.
First determine the **filing channel**, then assemble and preflight
the multi-document packet.

## Texas e-filing — eFileTexas (Odyssey File & Serve)

Texas's statewide e-filing system is **eFileTexas.gov**, built on
**Tyler Technologies' Odyssey File & Serve**, under **Tex. R. Civ. P.
21(f)** and the Supreme Court of Texas's e-filing rules (and the Tex.
R. Jud. Admin. technology standards):

- **Mandatory for attorneys** in civil cases in all courts (district,
  county, and justice courts).
- **Permitted for self-represented filers** — a self-represented
  party **may** e-file through eFileTexas (and many courts encourage
  or require it); filers may also file on paper at the clerk's window
  where the court accepts it. Confirm the court's acceptance of
  self-represented paper filings.
- **E-filing = consent to e-service.** Those who e-file are served
  subsequent documents electronically through the system under
  Tex. R. Civ. P. 21a.
- **E-format.** Documents are submitted as **text-searchable PDFs**,
  within the system's size caps; the **civil case information sheet**
  and any proposed order are typically uploaded as separate lead/
  attachment documents per the court's filing-code menu.
- **TexasLawHelp.org** offers guided self-help forms and the assisted
  filing front end for self-represented filers.

Confirm the court is live on eFileTexas for the case type and whether
the **court level** (district / county / justice) affects the filing
path before assuming the channel.

## E-filing workflow (eFileTexas / Odyssey File & Serve)

The portal shape is consistent across courts:

1. Register / log in to an eFileTexas (Odyssey File & Serve) account
2. Search for the case by cause number or party name (or start a new
   case for an initial filing)
3. Select the court, case category, and the **filing code / document
   type** for each component
4. Upload each component as a **separate text-searchable PDF** (mind
   the size caps); attach the **civil case information sheet** and the
   **proposed order** under the appropriate filing codes
5. Pay any filing fee, or attach the **Statement of Inability to
   Afford Payment of Court Costs**
6. Submit; the system returns a filing confirmation / file-stamp and
   effects electronic service on registered parties

## Paper filing (self-represented; courts/case types not on eFileTexas)

A self-represented filer may file on **paper** where the court accepts
it. Bring clean copies to the clerk's window during business hours;
the clerk file-stamps the original and returns a stamped copy. Confirm
whether the court accepts mail or drop-box filings and how many copies
(judge's copy / conformed copy) the court wants.

## Multi-document packet — typical components

A standard Texas filing packet consists of these documents:

| # | Document | Authority / note |
|---|----------|------|
| 1 | Original Petition **or** Motion | Tex. R. Civ. P. 45 / 47 (petition) or Rule 21 (motion); plain statement, numbered paragraphs |
| 2 | **Tex. R. Civ. P. 47(c) statement of relief range** | Pleaded **within** the petition; its omission can bar a default judgment |
| 3 | Civil Case Information Sheet | **Tex. R. Civ. P. 78a** — filed with an initial pleading; use the Supreme Court of Texas form |
| 4 | Notice of Hearing / Notice of Submission | Tex. R. Civ. P. 21 — sets the motion for oral hearing or submission; respect the notice floor (21 days for Rule 166a) |
| 5 | Affidavit or unsworn declaration | Notarized affidavit or CPRC § 132.001 unsworn declaration; Tex. R. Evid. 902(10) records foundation |
| 6 | Exhibits | Attach written instruments referenced in the pleading/motion |
| 7 | Proposed order | Tendered for the judge's signature; see `tx-submit-order` |
| 8 | Certificate of Service | Tex. R. Civ. P. 21a — date, manner, recipients |

Choose the closest matching filing-code label in the eFileTexas menu;
the menus vary by court and case category.

> **Tex. R. Civ. P. 47(c) and 78a are Texas-specific.** Every initial
> petition must plead the **range-of-relief statement** (Rule 47(c))
> and be accompanied by the **civil case information sheet** (Rule
> 78a). Do not file an initial petition without both.

## Sensitive / personal information — redaction

Texas **restricts sensitive data** in court filings. Before filing,
review every component (including exhibits) and handle protected data
as the governing rule requires — generally by **omitting or
truncating** identifiers such as Social Security, driver's-license,
passport, financial-account, and similar numbers, and using any
required sensitive-data mechanism where the data must reach the court
but be kept out of the public file.

> Verify the exact rule and procedure against `tx-law-references` —
> confirm the precise list of protected identifiers, the
> partial-redaction format, and whether a separate sealed/restricted
> filing is required. The filing court may have additional local
> requirements.

The filing party is responsible for the redaction; the clerk does
not redact for you.

## Cross-document consistency

Before assembling, confirm the packet is internally consistent:

- **Same caption** across every document — court, county, party names,
  cause number, document titles
- **Relief sought matches** between the motion's PRAYER and the
  proposed order, item by item
- The **document title named in the certificate of service** matches
  the document actually filed
- **Dates align** — certificate-of-service date matches the signature
  date; the affidavit jurat / § 132.001 declaration date is
  consistent; the hearing/submission date respects the notice floor
- **All referenced exhibits** are attached

Run `tx-quality-check` for the full pre-filing pass.

## Preflight — run the helper scripts

Before assembling the packet:

```
# Format / caption + form check
python3 plugins/tx-court-docs/scripts/format-check.py path/to/filing.docx

# Deadline arithmetic — TRCP 4 time computation, +3-day mail add-on
# (TRCP 21a), with Texas court-holiday handling (Gov't Code § 662.003)
python3 plugins/tx-court-docs/scripts/case-calendar.py ...
```

Use `case-calendar.py` to confirm the Notice-of-Hearing lead time
(the Rule 21(b) floor, or **21 days** for a Rule 166a motion) and to
compute response deadlines with the applicable mail add-on.

## Filing fees

Filing fees are set by statute and the clerk's fee schedule and vary
by court and case type. **Confirm the current amount with the filing
court's clerk** before submitting; do not hard-code a figure. Pay by
the portal's accepted method (card / e-check) or at the clerk's
cashier window for paper filings.

### Statement of Inability to Afford Payment of Court Costs

A filer who cannot afford the fees may file a **Statement of Inability
to Afford Payment of Court Costs** (the Texas indigency mechanism
under **Tex. R. Civ. P. 145**) **in lieu of** paying. File the
statement with the first filing rather than paying and seeking a
refund. The clerk must accept the filing without a fee; a party may
contest the statement under the rule's procedure. Verify the current
form and procedure with the clerk. See `tx-pro-se`.

## Filing vs. service — two distinct steps

Filing with the court is **not** the same as serving the opposing
party:

1. **Filing** — through eFileTexas, or at the clerk's window.
2. **Service of process** (initial citation + petition) — under
   **Tex. R. Civ. P. 99 et seq.** (issuance and service of citation;
   the answer is then due by the **Rule 99 "Monday rule"** deadline in
   district/county court, or by the **end of the 14th day** after
   service in justice court under Rule 502.5). Verify the current
   service mechanics.
3. **Service of subsequent papers** (motions, Notice of Hearing,
   orders) — under **Tex. R. Civ. P. 21a**, on every party by an
   allowed method, documented in the **Certificate of Service**. Add
   **+3 days** for service by mail / commercial delivery / fax / email
   when computing a deadline that runs from service.

If the system performs electronic service on registered parties, a
party without an e-filing account must still be served by another
allowed Rule 21a method — confirm the portal's e-service coverage for
each party.

## Pre-filing checklist

| Check | Done |
|-------|------|
| Filing channel identified (eFileTexas vs. paper) and mandatory-vs-permitted confirmed (attorney = mandatory) | ☐ |
| `scripts/format-check.py` run; no FAIL | ☐ |
| `scripts/case-calendar.py` confirms the Notice-of-Hearing lead time + mail add-on | ☐ |
| `tx-quality-check` pre-filing review complete | ☐ |
| `tx-fact-check` deep audit complete (high-stakes filing) | ☐ |
| Caption (court / county / cause number) matches across all documents | ☐ |
| Petition carries the **Rule 47(c)** relief-range statement | ☐ |
| **Civil case information sheet (Rule 78a)** attached for an initial pleading | ☐ |
| Exhibits attached and referenced | ☐ |
| Notice of Hearing prepared with the notice floor (or Rule 166a 21-day) timing | ☐ |
| Proposed order drafted as a separate document | ☐ |
| Each component saved as a separate text-searchable PDF | ☐ |
| Signature block compliant — State Bar of Texas number (attorney) or self-represented designation (Rule 57) | ☐ |
| Certificate of Service shows method, date, recipients (Rule 21a) | ☐ |
| Sensitive / personal information handled per the Texas redaction rule | ☐ |
| Filing fee available, or **Statement of Inability to Afford Payment** ready | ☐ |
| Service-of-process plan (Rule 99) / service-of-papers plan (Rule 21a) ready | ☐ |

## Composition

- For statewide format baseline: `tx-statewide-format`
- For drafting each component: `tx-draft-motion`,
  `tx-draft-declaration`, `tx-draft-note`, `tx-draft-order`
- For pre-filing review: `tx-quality-check` (lighter) and
  `tx-fact-check` (deep evidentiary)
- For clearing the setting and the Notice of Hearing:
  `tx-schedule-hearing`, `tx-draft-note`
- For court-specific filing channels and local rules: `tx-hcdc`,
  `tx-dcdc`, `tx-county-courts`, `tx-family-court`
- For self-represented filers (Statement of Inability, self-represented
  conventions, paper-filing option): `tx-pro-se`
- For deadline arithmetic: `tx-deadlines`
- For post-hearing order submission: `tx-submit-order`

## References to author

- `references/efiling-eFileTexas.md` — eFileTexas / Odyssey File &
  Serve walkthrough and filing-code guidance
- `references/packet-components.md` — the component checklist, the
  Rule 78a civil case information sheet, the Rule 47(c) relief-range
  statement, and the certificate-of-service form

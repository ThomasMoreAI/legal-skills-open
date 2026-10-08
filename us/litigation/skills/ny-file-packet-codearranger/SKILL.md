---
name: ny-file-packet-codearranger
title: Assemble a New York Court Filing Packet
description: Use when assembling and filing a complete New York court motion packet via NYSCEF or UCMS/CCEF. Triggers include 'assemble a New York motion packet', 'NYSCEF filing packet', 'NY court eFile', 'UCMS Civil Court filing', 'CCEF filing', 'how do I file a motion in NYSCEF', 'NY Supreme Court filing instructions', '22 NYCRR § 202.5-b compliance', 'NY filing preflight', 'NY motion bundle', 'NY filing transmittal'. Verifies every required component, enforces cross-document consistency (caption, index number, exhibits, service), confirms NYSCEF document-type selection, runs a final format check, and produces filing instructions per the specific court's e-filing system.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/ny-court-docs/skills/ny-file-packet
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Assemble a New York Court Filing Packet

> **NOT LEGAL ADVICE.** Packet preflight catches errors that
> would otherwise cause a clerk rejection or in-court
> ruling against your motion.

## NY court filing systems

| Court | System | URL |
|-------|--------|-----|
| Supreme Court (all counties) + County Court | NYSCEF | https://iappscontent.courts.state.ny.us/NYSCEF/live |
| Civil Court of the City of New York | UCMS / CCEF | https://www.nycourts.gov/courts/nyc/civil/ |
| Family Court | UFC (Universal Family Court) | https://nycourts.gov/courts/nyc/family/ |
| Surrogate's Court | NYSCEF (mostly) | Same as Supreme |
| Nassau / Suffolk District Court | NYSCEF | Same |
| City Courts (upstate) | NYSCEF, variably | Court-by-court |
| Town & Village Justice Courts | Paper-only typically | Local |

## Motion packet components

For a standard motion in Supreme Court via NYSCEF:

1. **Notice of Motion** (or Order to Show Cause) — see
   `ny-draft-note`
2. **Affirmation / Affidavit in Support** — see
   `ny-draft-declaration`
3. **Exhibits** — separate PDFs or single bundled PDF with
   bookmarks (per Part Rules)
4. **Memorandum of Law in Support** — see `ny-draft-motion`
5. **Proposed Order** (if relief involves an order) — see
   `ny-draft-order`
6. **Affidavit of Service** (or NYSCEF service certification)

## NYSCEF assembly conventions

### Bookmarks

Required for any multi-document or multi-exhibit filing.
Bookmark to:

- Start of each document (e.g., "Affirmation of Smith")
- Start of each exhibit (e.g., "Exhibit A — Credit
  Agreement")

### Document type selection

NYSCEF requires selecting a document type from a
controlled dropdown for each upload:

| File | NYSCEF document type |
|------|---------------------|
| Notice of Motion | "Notice of Motion" |
| Order to Show Cause | "Order to Show Cause" |
| Affirmation in Support | "Affirmation in Support" |
| Affidavit in Support | "Affidavit in Support" |
| Memorandum of Law | "Memorandum of Law" |
| Exhibits | "Exhibits" or "Exhibit [Letter]" |
| Proposed Order | "Proposed Order" |
| Affidavit of Service | "Affidavit of Service" |
| Stipulation | "Stipulation" |
| Counter-Order | "Counter Order" |

Mismatched document types are a common rejection cause.

### File specifications

- **Format**: PDF
- **OCR**: text-searchable preferred (image-only allowed
  for true-paper exhibits)
- **Size**: ≤ 100 MB per upload
- **Naming**: descriptive; no special characters
- **Bookmarks**: per above
- **Redaction**: 22 NYCRR § 202.5(e) — redact SSNs, tax
  IDs, financial-account numbers (except last 4 of each),
  birthdates (except year), minors' names (use initials)

## Cross-document consistency check

Before submission, verify every document in the packet
shows:

| Item | Same across packet? |
|------|---|
| Court name | YES |
| County | YES |
| Plaintiff name + role | YES |
| Defendant name + role | YES |
| Index number | YES |
| Justice (if assigned) | YES |
| Part (if assigned) | YES |
| Notice of Motion return date | YES (matches the date in the affirmation's "returnable on") |
| Exhibit letter / number | YES (matches references in affirmation) |

## Service requirement

Most NY motion filings require contemporaneous service:

| Method | Tracking |
|--------|---------|
| NYSCEF e-service (registered parties) | Auto-tracked; certification by NYSCEF |
| Mail (CPLR 2103(b)(2)) | Affidavit of service; 5-day add-on |
| Email by stipulation (CPLR 2103(b)(7), 2103-a) | Email + filed acknowledgment |
| Personal delivery | Affidavit of service |

For pro se filers: if the opposing party is also NYSCEF-
registered, **NYSCEF e-service is automatic and sufficient**;
no separate service required.

## Preflight checklist

```
[ ] All 4-6 packet components present
[ ] Each component in correct format (single PDF per doc)
[ ] NYSCEF document types correctly selected
[ ] Bookmarks present for multi-exhibit filings
[ ] Caption consistent across all documents
[ ] Index number on every page
[ ] Pagination on every page
[ ] All cross-references resolve
[ ] Citations Tanbook-formatted
[ ] Signature blocks present and correct
[ ] CPLR 2106 affirmation language (post-2023)
[ ] Service mode determined; affidavit/cert ready
[ ] Service period satisfies CPLR 2214(b) + 2103(b)(2)
[ ] Redactions applied per 22 NYCRR § 202.5(e)
[ ] Final PDF size ≤ 100 MB
[ ] Justice's Part Rules consulted for special requirements
```

## Filing instructions output

After preflight passes, the filing instructions look like:

```
NYSCEF FILING INSTRUCTIONS
Case: [Caption], Index No. [#####/YYYY]
Motion: [Description]
Return Date: [DATE]

STEP 1 — Log in to NYSCEF
Go to https://iappscontent.courts.state.ny.us/NYSCEF/live
Use your registered NYSCEF account.

STEP 2 — Upload documents (in this order)
   [ ] notice-of-motion.pdf — type: "Notice of Motion"
   [ ] affirmation-in-support.pdf — type: "Affirmation in Support"
   [ ] memorandum-of-law.pdf — type: "Memorandum of Law"
   [ ] exhibits-bundle.pdf — type: "Exhibits"
   [ ] proposed-order.pdf — type: "Proposed Order"
   [ ] affidavit-of-service.pdf — type: "Affidavit of Service"

STEP 3 — Confirm service
   Check NYSCEF service-list to confirm opposing party is
   NYSCEF-registered. If yes: NYSCEF e-service is automatic.
   If no: mail per CPLR 2103(b)(2) and file affidavit of
   service separately.

STEP 4 — Submit + pay fees
   Fees: $45 (motion) per NYSCEF schedule (CPLR 8020).
   Pay-as-you-go or stored credit card.

STEP 5 — Confirm receipt
   NYSCEF returns a stamped confirmation; the return date
   is locked in.

STEP 6 — Calendar follow-ups
   - Opposition due: 7 days before return date (per CPLR 2214)
   - Reply due: per Part Rules (typically 1-3 days before)
   - Return date: [DATE] at [TIME]
```

## Composition with other ny- skills

- `ny-statewide-format` — format baseline
- `ny-draft-motion` + `ny-draft-declaration` + `ny-draft-note`
  + `ny-draft-order` — packet components
- `ny-fact-check` + `ny-quality-check` — pre-packet QC
- `ny-schedule-hearing` — return date reservation

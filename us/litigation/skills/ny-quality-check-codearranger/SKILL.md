---
name: ny-quality-check-codearranger
title: New York Quality Check
description: Use to QC, review, or validate a New York court document before filing. Triggers include 'quality check this NY filing', 'pre-filing review', 'NY clerk rejection', 'NY filing format audit', 'NYSCEF format compliance', 'review my New York brief before I file', 'will the clerk reject this', '22 NYCRR § 202.5 compliance check', 'verify caption + format + content + signatures', 'pre-filing audit'. Runs a two-pass format + content check against 22 NYCRR § 202.5 (paper), § 202.5-b (NYSCEF), the assigned Justice's Part Rules, and the pro-se drafting framework.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/ny-court-docs/skills/ny-quality-check
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# New York Quality Check

> **NOT LEGAL ADVICE.** Pre-filing QC catches the errors that
> would otherwise cause a clerk's-office rejection or a Part-
> Rule denial.

## Two-pass QC

### Pass 1 — Format compliance

Run `scripts/format-check.py` against the PDF for mechanical
checks:

- **Paper size**: 8½ × 11
- **Margins**: 1 inch on all sides
- **Font**: Times New Roman 12-pt or equivalent serif 12-pt
- **Spacing**: Double-spaced; quotations 50+ words may be
  single-spaced and indented
- **Color**: Black text on white
- **Pagination**: Bottom center or bottom right
- **PDF format**: Text-searchable preferred; bookmarks for
  multi-document filings

Manual checks (the script doesn't catch these):

- **Caption box**: court name, county, parties, separator
  ("-against-"), index number, Justice, Part — all present
  and correctly formatted
- **Document title**: descriptive ("Affirmation of [NAME] in
  Support of Motion") and matches the NYSCEF document type
- **Signature block**: pro se "Self-Represented [Plaintiff/
  Defendant]" or attorney with bar number; email address
  prominent
- **Verification** (if a verified pleading): notarized or
  CPLR 2106 affirmed
- **Exhibit cover sheets**: "Exhibit A" with cover sheet
  preceding each exhibit
- **Notice of Motion / OSC**: return date and Part match

### Pass 2 — Content (pro-se drafting framework) compliance

The pro-se drafting framework — the principles documented in `ny-pro-se`:

- **Every factual statement cited** to a paragraph of an
  affirmation/affidavit or a specific exhibit page
- **Every legal assertion cited** to a CPLR section, statute,
  or case in Tanbook format
- **No legal argument in sworn papers** (move to memo)
- **No new facts in memo** (move to affirmation)
- **Plain-language sections** appropriate for the audience
- **Discrete, numbered points** in argument
- **Concession** of weak points; distinguish
- **Restated "ask"** in conclusion

### Pass 2.5 — Substantive law check

- **CPLR citations** match the current code (CPLR amended
  through L 2024)
- **Tanbook citation format** (NY3d, AD3d, Misc 3d; no
  periods)
- **Statute names** correct (CPLR not "C.P.L.R." in body
  text; "N.Y. Gen. Bus. Law" not "GBL" except in
  abbreviation key)
- **Effective dates** considered — e.g., CCFA-affected
  rules (CPLR 213(a), CPLR 3015(e), 22 NYCRR § 202.27-a)
  apply to actions commenced on or after April 7, 2022

## Common NYSCEF rejections

NYSCEF clerks reject filings for:

| Reason | Fix |
|--------|-----|
| Caption missing Index Number | Add to caption |
| Document type wrong | Reselect from NYSCEF dropdown |
| Multiple documents in one PDF | Split per NYSCEF rule |
| Insufficient bookmarks | Add bookmarks at start of each exhibit |
| Image-only PDF (no OCR) | Re-export as text-searchable PDF |
| File size > 100 MB | Split or compress |
| Missing affidavit of service | Re-file with service affidavit |
| Improper redaction (under 22 NYCRR § 202.5(e)) | Re-redact per § 202.5(e) personal-identifying-information rules |

## Part-Rule-specific checks

Some Justices' Part Rules add requirements:

| Common Part Rule requirement | Verify |
|------|--------|
| Pre-motion letter required | Did you file the pre-motion letter? |
| Courtesy copy to chambers | Send paper copy + cover letter? |
| Word-count alternative used | Word-count certification at foot of memo? |
| Joint stipulation re scheduling | Filed before the motion? |
| Oral-argument request | Affirmation requesting argument? |

## Pre-filing checklist

```
[ ] Format-check.py passes
[ ] Caption matches across all documents in the packet
[ ] Index number on every page
[ ] Pagination on every page
[ ] All exhibits attached and labeled
[ ] All cross-references resolve to the right paragraph/exhibit
[ ] All citations Tanbook-formatted
[ ] Affirmation/affidavit signed and dated
[ ] CPLR 2106 affirmation language correct (post-2023 form)
[ ] Memorandum of Law within page limit (25/15 under § 202.8-b)
[ ] Notice of Motion has proper return date + service-period
[ ] Service date on Notice of Motion ≥ CPLR 2214(b) requirement
[ ] Proposed order present (if motion seeks an order)
[ ] Affidavit of service / NYSCEF service certification ready
[ ] Justice's Part Rules consulted for special requirements
[ ] Document types correctly selected in NYSCEF
```

## Composition with other ny- skills

- `ny-statewide-format` — format baseline
- `ny-fact-check` — content + citation verification
- `ny-file-packet` — packet-level QC
- `ny-pro-se` — pro-se drafting framework
- `ny-law-references` — citation source-of-truth

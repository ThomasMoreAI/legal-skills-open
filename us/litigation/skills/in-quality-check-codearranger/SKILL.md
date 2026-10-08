---
name: in-quality-check-codearranger
title: Quality Check — Indiana Court Documents
description: 'This skill should be used when the user asks to "quality check an Indiana filing", "QC an Indiana motion", "review my Indiana filing", "audit Indiana brief before filing", "Indiana pre- filing check", "validate Indiana document for Odyssey", "T.R. 5(E) compliance check", "Indiana format-check before filing", or any related pre-filing review request. Runs the consolidated pre-filing review: format compliance (T.R. 5(E) + venue local rules), content review (citation accuracy, internal consistency, packet integrity), Odyssey upload-readiness (document codes, file size, PDF structure), and final pro-se conduct review (signature, contact info, service list). Trigger phrases: "QC Indiana filing", "Indiana pre-filing review", "T.R. 5(E) compliance", "Indiana brief audit", "QC before Odyssey upload".'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/in-court-docs/skills/in-quality-check
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Quality Check — Indiana Court Documents

This skill is the **final pre-filing review** — the last
checkpoint between drafting and filing. It runs a four-pass
quality control protocol: format compliance, content review,
upload-readiness, and pro-se conduct review. The output is a
go / no-go decision plus a defect log.

The format-check.py script bundled with this plugin is the
computational counterpart for the format-compliance pass.

> **NOT LEGAL ADVICE.** Generated content is a drafting aid;
> running this QC does not substitute for independent legal
> review. Pro se filers are strongly encouraged to consult
> Indiana Legal Services or a local Self-Help Center for
> substantive review.

## QC sequence — four passes

```
Pass 1 (Format): T.R. 5(E) compliance + venue local-rule format
Pass 2 (Content): Citation accuracy, internal consistency,
                  packet integrity (cross-references)
Pass 3 (Upload):  Odyssey readiness — document codes, PDF
                  structure, file size, Service Contacts
Pass 4 (Pro Se):  Signature, contact info, service list,
                  T.R. 11(A) requirements

If all four pass: GO
If any blocks: NO-GO with defect log
```

## Pass 1 — Format compliance (T.R. 5(E))

Run `scripts/format-check.py` on the `.docx` (or PDF rasterized
from the .docx). Checks:

- [ ] Paper size: 8.5 × 11 inches (Letter)
- [ ] Margins: top page-1 ≥ 2 inches (for clerk's stamp); other
      pages ≥ 1 inch on all sides
- [ ] Font: 12 pt minimum; serif body (Times New Roman, Cambria,
      Century Schoolbook, etc.)
- [ ] Line spacing: double-spaced body (T.R. 5(E)(3));
      single-spacing allowed for block quotations, footnotes,
      captions, signature blocks
- [ ] Page numbers: bottom of every page (T.R. 5(E)(4))
- [ ] Footer: contains PAGE and NUMPAGES fields; includes
      document short title and / or cause number per local rule

Venue-specific format additions:

- **Marion (LR49-TR5-203)**: chambers-copy threshold at 15 pages
- **Lake (LR45-TR5)**: chambers-copy threshold at 20 pages
- **Hamilton (LR29-TR5)**: chambers-copy threshold at 15 pages
- All venues: Indiana Administrative Rule 9 confidentiality
  designation if the filing contains protected information

## Pass 2 — Content review

Delegates to `in-fact-check` for the four sub-passes:

1. **Citation verification** — every rule, statute, case cite
   verified against canonical sources
2. **Internal consistency** — captions, cause numbers, party
   names, dates aligned throughout
3. **Packet consistency** — declarations support memo arguments;
   exhibit list matches attached exhibits; proposed order matches
   relief
4. **Sworn-vs.-argued consistency** — every factual assertion
   has a sworn predicate or is identified as legal argument

Specific Indiana-specific checks:

- [ ] Caption uses **STATE OF INDIANA** + COURT NAME + COUNTY +
      INDIANA top block
- [ ] **"v."** (not "vs.") between parties
- [ ] Cause number county-code matches the named county
- [ ] Citation format: `Smith v. Jones, 123 N.E.3d 456 (Ind.
      2023)` — reporter + page + court + year
- [ ] Rule citations: `Ind. Trial R. 56(C)` or `T.R. 56(C)`
- [ ] Statute citations: `IC 34-11-2-9` (no "§" required)
- [ ] No reference to "ORS" / "RCW" / "C.R.S." / "Cal. Civ. Code"
      (other state remnants — common search-and-replace error)
- [ ] No reference to "in pro per" (California-ism) — use
      "Pro Se"

## Pass 3 — Odyssey upload readiness

- [ ] PDF rendered correctly (not the .docx)
- [ ] File size under 25 MB (single document)
- [ ] If multi-document filing, total under 100 MB
- [ ] Document code identified in advance (see Marion / Lake
      document code references)
- [ ] All exhibits bookmarked in the PDF (if combined PDF)
- [ ] Service Contacts up to date for the case
- [ ] Filing fee identified or fee waiver filed
- [ ] No restricted information (SSN, account numbers) — use
      "XXX-XX-XXXX" redaction format
- [ ] Indiana Administrative Rule 9 confidentiality designation
      if applicable

## Pass 4 — Pro se conduct review

- [ ] Signature on the last page (wet or `/s/` for e-filing)
- [ ] "Pro Se" designation after name (not "in pro per")
- [ ] Mailing address, phone, email all current
- [ ] Email matches the Odyssey Service Contacts entry
- [ ] No Attorney Number on the signature block (Atty. No. is
      for licensed attorneys only)
- [ ] Certificate of Service in the body listing service method
      for each party
- [ ] Verification language (if required) uses the IC 35-44.1-
      2-1 formula: "I affirm, under the penalties for perjury,
      that the foregoing representations are true."

## Defect-severity scale

| Severity | Effect | Examples |
|----------|--------|----------|
| BLOCKING | Filing rejected by clerk or court | Wrong cause number; missing signature; PDF corrupted |
| HIGH | Likely to draw an order to refile | Wrong margins; missing proposed order; missing Certificate of Service |
| MEDIUM | Court may rule despite defect, but quality suffers | Citation format errors; inconsistent date references |
| LOW | Style only; no procedural impact | Em-dash vs. hyphen; minor typo |
| INFO | Improvement suggestion | Stronger case cite available |

## Defect-log format

```
QC REPORT — [Document title], [Cause No.]
Date: [QC run date]

Pass 1 (Format): PASS / WARN / FAIL
Pass 2 (Content): PASS / WARN / FAIL
Pass 3 (Upload): PASS / WARN / FAIL
Pass 4 (Pro Se): PASS / WARN / FAIL

Overall: GO / NO-GO

Defects:
   [BLOCKING] [description] — [fix recommendation]
   [HIGH]     [description] — [fix recommendation]
   [MEDIUM]   [description] — [fix recommendation]
   [LOW]      [description] — [fix recommendation]

Sign-off:
   QC complete — ready for filing: ☐ YES  ☐ NO
   Signed: [QC reviewer]  Date: [date]
```

## When to run QC

- **Always**: before any e-filing through Odyssey
- **Always**: before filing a packet of more than 5 pages
- **Always**: before filing any dispositive motion (12(B)(6),
  T.R. 56)
- **Always**: before filing any post-judgment motion (T.R. 59,
  T.R. 60(B))
- **Recommended**: before serving discovery
- **Recommended**: before filing the initial Appearance + Answer

## Composition

- `in-statewide-format` for format baseline
- `in-fact-check` for content review (Pass 2)
- `in-marion` / `in-lake` / `in-county-courts` for venue-specific
  format requirements
- `in-pro-se` for self-represented signature block
- `in-file-packet` for packet assembly + final upload

## References

- `references/qc-checklist.md` — printable four-pass checklist
- `references/format-check-output.md` — sample format-check.py
  report with annotations
- `references/odyssey-upload-readiness.md` — Odyssey-specific
  pre-flight check

**NOT LEGAL ADVICE.** Generated content is a drafting aid; verify
against current rules and case law before filing.

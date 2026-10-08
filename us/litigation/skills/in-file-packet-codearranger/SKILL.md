---
name: in-file-packet-codearranger
title: Assemble an Indiana Court Filing Packet
description: 'This skill should be used when the user asks to "assemble an Indiana filing packet", "Indiana e-filing packet", "Indiana Odyssey upload packet", "Marion filing checklist", "Indiana filing preflight", "combine PDF for Odyssey Indiana", "Indiana filing assembly", "Indiana motion packet checklist", "Indiana e-file workflow", or any related packet-assembly task. Verifies every required component of a multi-document filing packet (motion + memo + declaration + proposed order + service list), enforces cross-document consistency, produces Odyssey upload instructions with document codes, and outputs the final chambers-copy delivery protocol if the packet exceeds the venue''s chambers-copy page threshold. Trigger phrases: "Indiana filing packet", "Indiana Odyssey upload", "Marion filing preflight", "Indiana motion bundle", "combine PDF Indiana filing", "Indiana e-file packet".'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/in-court-docs/skills/in-file-packet
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Assemble an Indiana Court Filing Packet

This skill is the **packet assembler** — the workflow that takes
the four drafting outputs (motion, memorandum, declaration,
proposed order) and produces a court-ready filing packet. It
runs the final consistency checks, generates the Odyssey upload
sequence, and produces the chambers-copy delivery instructions
if the packet exceeds the venue's threshold.

> **NOT LEGAL ADVICE.** Generated content is a drafting aid;
> verify the packet against the venue court's local rules before
> uploading. Once Odyssey accepts a filing, it is on the docket
> — withdrawal requires a court order.

## Standard motion packet components

A complete Indiana motion packet typically contains:

1. **Motion** (1-3 pages) — operative request for relief
2. **Memorandum in Support** (5-15 pages) — legal argument
3. **Declaration** (1-3 pages + exhibits) — sworn factual
   predicate
4. **Exhibits** (variable) — documents attached to the
   declaration (Exhibit A, B, C ...)
5. **Proposed Order** (1-2 pages) — order for judge signature

Optional / situational components:

- **Notice of Hearing** (if party-issued; otherwise court issues)
- **Cost Statement** (required for fee-shifting motions)
- **Affidavit of Indigency** (CCS Form 1042, if claiming
  indigent status)
- **Notice of Submission of Authority** (when filing post-
  briefing supplemental authority)

## Packet assembly checklist

### Pre-assembly

- [ ] All four drafting skills (in-draft-motion, in-draft-
      declaration, in-draft-order, in-draft-note if applicable)
      have produced their outputs
- [ ] in-fact-check has been run against the full packet
- [ ] in-quality-check has run Pass 1 (format) and Pass 2
      (content)
- [ ] Cause number verified against Odyssey docket
- [ ] All exhibits OCR'd and bookmarked
- [ ] Service Contacts up to date in Odyssey

### Component-level verification

For each component:

- [ ] Caption identical (court, county, parties, cause number)
- [ ] Document title accurate and descriptive
- [ ] Numbered paragraphs match T.R. 10(B)
- [ ] Signature block populated with current contact info
- [ ] Certificate of Service appears at end (motion, memo,
      declaration; not the proposed order)
- [ ] Date of signing matches filing date

### Cross-component verification

- [ ] Exhibit references in memo match exhibits attached to
      declaration
- [ ] Factual statements in memo each have a paragraph
      reference in the declaration
- [ ] Relief sought in motion matches relief in proposed order
- [ ] All four documents' captions are identical character-for-
      character

## Odyssey upload sequence

Indiana Odyssey requires each packet component to be uploaded
as a separate Odyssey filing, with the correct document code.
The recommended sequence:

```
Step 1: Log into Odyssey at efile.courts.in.gov
Step 2: Select "File Into Existing Case"
Step 3: Enter cause number; confirm case info
Step 4: For each packet component, click "Add Filing":

   Document               | Document Code | Notes
   -----------------------|---------------|------
   Motion                 | 11020         | "Motion"
   Memorandum in Support  | 11250         | "Memorandum"
   Declaration            | 25001         | "Affidavit/Declaration"
   Exhibit A              | 25002         | "Exhibit A"
   Exhibit B              | 25002         | "Exhibit B"
   ...                    | 25002         | ...
   Proposed Order         | 12000         | "Proposed Order"

Step 5: Pay filing fee or claim indigent status
Step 6: Click "Submit"
Step 7: Wait for confirmation email (typically <5 min)
Step 8: Print or save the confirmation receipt
```

Marion / Lake / Hamilton document codes match the table above.
County Circuit Courts use the same document codes statewide. If
a code is unfamiliar, search the Odyssey dropdown — it auto-
filters as you type.

## Combined PDF vs. separate uploads

Two filing patterns are accepted:

### Pattern A — Separate uploads (recommended)

Each document uploaded as a separate Odyssey filing with its own
document code. Advantages: each document gets a distinct file-
stamp and Odyssey URL; the court can locate any single document
quickly.

### Pattern B — Combined PDF

The motion + memo + declaration + exhibits + proposed order
assembled into a single PDF with internal bookmarks. The PDF is
uploaded as one Odyssey filing under the "Motion" document code.
Advantages: fewer transactions; smaller cumulative file size.

Marion Civil Division accepts both patterns; Lake Civil Division
prefers Pattern A; some county Circuit Courts require Pattern A.

If using Pattern B, the PDF MUST have internal bookmarks for
each component (Motion, Memorandum, Declaration, Exhibit A,
Exhibit B, ..., Proposed Order). Use Adobe Acrobat or pdftk
to add bookmarks.

## Filing fees

Most motion filings are **free** — the only fee is the initial
case-opening fee (PL, CC, CT, etc. at $177 in most counties).
Exceptions:

- **Subsequent appearance fee**: $20 in some counties for
  parties added later
- **Notice of Appeal**: $250 to the Court of Appeals
- **Trial de novo (small claims)**: $150 in Marion (paid to
  Civil Division upon trial de novo motion)

If indigent status was previously granted via CCS Form 1042, no
e-filing transaction fee applies. Otherwise, Odyssey charges
$10-15 per transaction.

## Chambers-copy delivery (if applicable)

If the packet exceeds the venue's chambers-copy threshold:

- **Marion**: > 15 pages — paper chambers copy required
- **Lake**: > 20 pages — paper chambers copy required
- **Hamilton**: > 15 pages — paper chambers copy required

Chambers copy must:

- Be a printed copy of the Odyssey-accepted PDF
- Be three-hole punched on the left margin
- Be stapled in the upper-left corner (no spiral binding)
- Be marked "CHAMBERS COPY" on the first page in red ink
- Be delivered to the assigned courtroom within 24 hours of
  Odyssey acceptance

Delivery options:

- **In-person**: deliver to courtroom secretary / bailiff
- **Mail**: certified mail with return receipt to courtroom
  address
- **Courier**: services like LawDawg or local courier (Marion);
  retain delivery confirmation

Some courtrooms (Marion CD-5, Marion CD-11) now accept courtesy
PDF via email to the JA in lieu of paper. Confirm preference
before relying on the email option.

## Post-filing follow-up

- [ ] Print the Odyssey confirmation receipt
- [ ] Calendar the response deadline (typically 30 days, see
      `in-deadlines`)
- [ ] Set a reminder for 1 week before the response is due
- [ ] If a hearing is requested, follow up with the JA after
      3-5 business days if no Notice of Setting appears
- [ ] Save the file-stamped PDFs locally as a redundant archive

## Composition

- `in-statewide-format` for format baseline
- `in-marion` / `in-lake` / `in-county-courts` for venue
  document codes + chambers-copy thresholds
- `in-pro-se` for self-represented filing
- `in-draft-motion` / `in-draft-declaration` / `in-draft-order`
  for the packet components
- `in-quality-check` for final QC before upload

## References

- `references/odyssey-document-codes.md` — full document-code
  reference table
- `references/packet-assembly-checklist.md` — printable
  checklist
- `references/chambers-copy-protocol.md` — venue-specific
  chambers-copy delivery
- `references/combined-pdf-bookmarks.md` — Pattern B bookmark
  structure

**NOT LEGAL ADVICE.** Generated content is a drafting aid; verify
against current rules and case law before filing.

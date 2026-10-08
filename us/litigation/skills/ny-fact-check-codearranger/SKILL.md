---
name: ny-fact-check-codearranger
title: Fact-Check New York Court Filings
description: 'Use to fact-check a New York court filing before filing. Triggers include ''fact-check this NY motion'', ''verify citations Tanbook'', ''check my NY brief'', ''NYSCEF pre-filing audit'', ''CPLR citation format check'', ''quote validation'', ''citation verification'', ''check cross- references in my New York affirmation'', ''verified-vs- affirmation consistency'', ''index-number consistency''. Runs four passes: citation verification, internal consistency, packet consistency, and sworn-vs.-argued consistency.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/ny-court-docs/skills/ny-fact-check
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Fact-Check New York Court Filings

> **NOT LEGAL ADVICE.** Use before filing. Fact-check
> catches errors that would otherwise be raised by the
> opposing party or the Justice.

## Four-pass framework

### Pass 1 — Citation verification

For every citation in the document, verify:

- **Court of Appeals**: `[Case], [Vol] NY3d [Page]
  ([Pinpoint]) ([Year])` — verify the volume, page, and
  year; the case must be in NY3d (1st series 1956-2003;
  2d 1956-2003; 3d 2003-present). NY2d cites should be
  pre-2003 cases. NY (1st series) should be pre-1956.
- **Appellate Division**: `[Case], [Vol] AD3d [Page]
  ([Dept] [Year])` — verify the volume, department, and
  year. AD2d → AD3d transition was 2003.
- **Misc. Reports**: `[Case], [Vol] Misc 3d [Page] ([Court],
  [County] [Year])` — verify court and county
- **CPLR citations**: `CPLR [Section](sub)([sub-sub])` —
  verify subdivision lettering matches the current code
  (CPLR has been amended frequently; verify the version
  currently in force when the action was commenced)
- **22 NYCRR**: `22 NYCRR § [Part].[Section]` — verify
  Part number (Part 202 = Supreme/County; Part 208 = NYC
  Civil; Part 210 = City; Part 212 = District; Part 130 =
  attorney misconduct / sanctions)
- **Statutes**: verify cite to N.Y. CPLR / N.Y. Gen. Bus.
  Law / N.Y. Real Prop. Acts. Law / etc.

Tools:

- `references/online-sources.md` in `ny-law-references`
  lists canonical-source URLs
- WebFetch against the source URL for verbatim quote check
- The Tanbook (NYLRSM) is the authoritative style manual

### Pass 2 — Internal consistency

Within a single document:

- **Defined terms** — every defined term ("Plaintiff,"
  "Debt," "Account") used consistently throughout
- **Numbers** — dollar amounts match across narrative,
  prayer for relief, and supporting exhibits
- **Dates** — chronology consistent; no events out of
  order
- **Pronouns** — gender consistent if not using they/them
- **Paragraph numbering** — sequential
- **Cross-references** — internal "(see ¶ 12)" actually
  points to the right paragraph

### Pass 3 — Packet consistency

Across multiple documents in the same filing packet
(motion + affirmation + exhibits + memo + proposed
order):

- **Caption**: identical on every document (court name,
  county, parties, index number, Justice, Part)
- **Index number**: same on every document
- **Title**: matches NYSCEF document type
- **Exhibit references**: cross-referenced exhibits
  actually attached; numbering consistent ("Exhibit A"
  in the affirmation matches "Exhibit A" in the exhibit
  packet)
- **Service date** in the certificate of service or
  CPLR 2103(b)(7) certification matches the NYSCEF
  filing date
- **Notice of Motion return date** matches the
  affirmation's "returnable on [date]"

### Pass 4 — Sworn-vs.-argued consistency

NY distinguishes sharply between sworn facts and legal
argument:

- **Affirmation / Affidavit**: sworn statement of facts;
  cannot contain legal argument (CPLR 3024 strikes pure
  argument from sworn papers)
- **Memorandum of Law**: legal argument; cannot assert
  new facts not in the affirmation

Common pro se errors:

- Affirmation contains "Plaintiff has no standing"
  (legal argument) — should be moved to the memo
- Memo asserts "I sent payment on June 15" (fact) —
  should be in the affirmation

For each statement, verify:

| In affirmation? | In memo? | OK? |
|----|----|----|
| Fact | — | Yes |
| — | Argument | Yes |
| Argument | — | **No — move to memo** |
| — | Fact (not in affirmation) | **No — add to affirmation** |

## Quick QC sweep

After running the four passes, do a final pass:

1. **Format check** — run `scripts/format-check.py` against
   the PDF (see `ny-statewide-format`)
2. **Pagination** — every page numbered; no orphan headings
3. **Signature blocks** — present on every signed
   document; pro se vs. attorney signature block correct
4. **NYSCEF metadata** — document title and document type
   selected correctly

## Composition with other ny- skills

- `ny-law-references` — canonical reference corpora to
  fact-check against
- `ny-statewide-format` — format-rule verification
- `ny-quality-check` — broader pre-filing review
- `ny-file-packet` — full packet assembly + consistency

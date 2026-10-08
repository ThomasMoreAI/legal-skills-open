---
name: oh-quality-check-codearranger
title: Quality Check — Ohio Filings
description: 'Use to run pre-filing QC on an Ohio filing — format compliance + content consistency. Triggers include ''Ohio quality check'', ''pre-filing review Ohio'', ''verify Ohio filing format'', ''Ohio QC''. Two-pass: (1) format compliance using format-check.py (caption, margins, fonts, line spacing, footer); (2) content consistency using oh-fact-check''s four-pass framework.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/oh-court-docs/skills/oh-quality-check
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Quality Check — Ohio Filings

> **NOT LEGAL ADVICE.** Pre-filing QC is a hygiene pass,
> not a substitute for substantive legal review.

## Two-pass framework

### Pass 1: Format compliance

Use `plugins/oh-court-docs/scripts/format-check.py
<filing.docx>` to verify:

- Letter paper (8.5 x 11)
- 1-inch margins on sides + bottom; 1.5-inch top on first
  page for caption block (Civ. R. 10(A))
- 12-point minimum body font
- Double-spaced body
- Footer with page number

### Pass 2: Content consistency

See `oh-fact-check` for the four-pass content QC:

1. **Citation verification** — every R.C. / Civ. R. /
   Ohio case citation resolves to a valid source
2. **Internal consistency** — numbered paragraphs follow,
   cross-references match
3. **Packet consistency** — caption + case number + party
   names + service dates identical across documents
4. **Sworn-vs-argued alignment** — every fact in the
   memorandum traces back to an affidavit paragraph or
   exhibit

## Per-court overlay

After the statewide QC, check the assigned court's Loc.
R. for:

- Page limits (verify motion brief is under cap)
- Working-copy requirements (some Cuyahoga / Franklin
  chambers require courtesy paper copies)
- Certificate of service signature requirements
- Proposed order email-Word-version requirement (some
  chambers)

## Common rejection reasons

- **Missing certificate of service** — Civ. R. 5(D)
  requires every paper served on a party to show service
- **Improper caption** — wrong court, wrong case number,
  wrong party names
- **Pro se filer including attorney bar number** — Civ.
  R. 11 sanctions
- **Affidavit not notarized** — R.C. 2319.04 + Civ. R.
  56(C); courts strike unsworn affidavits

## Composition with other oh- skills

- `oh-statewide-format` — format baseline
- `oh-fact-check` — citation + content verification
- `oh-file-packet` — assembly + preflight
- `oh-pro-se` — pro-se signature + tone QC

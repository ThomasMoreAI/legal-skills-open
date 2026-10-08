---
name: oh-draft-motion-codearranger
title: Draft an Ohio Motion
description: Use to draft an Ohio civil motion. Triggers include 'Ohio motion', 'draft Ohio motion to compel', 'Ohio Civ. R. 56 motion for summary judgment', 'Ohio Civ. R. 12 motion to dismiss', 'Ohio Civ. R. 60 motion to vacate', 'Ohio Civ. R. 37 motion to compel'. Produces an Ohio-format motion with caption, statement of grounds, memorandum in support, certificate of service, and tendered proposed order.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/oh-court-docs/skills/oh-draft-motion
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Draft an Ohio Motion

> **NOT LEGAL ADVICE.** This skill scaffolds an Ohio civil
> motion. Confirm the specific Civ. R. grounds and the
> per-court Loc. R. page limits before filing.

## Standard Ohio motion structure

1. **Caption** — Civ. R. 10(A) format (see
   `oh-statewide-format`)
2. **Notice line** — `NOW COMES Defendant [Name], by and
   through undersigned counsel / Pro Se, and moves the
   Court for [relief sought], for the reasons stated in
   the attached Memorandum in Support.`
3. **Memorandum in Support** — typically with:
   - I. Statement of the Case
   - II. Standard of Review
   - III. Argument (with point headings)
   - IV. Conclusion / Prayer for Relief
4. **Certificate of Service** — Civ. R. 5
5. **Tendered proposed order** — separate document

## Common Ohio motion types

### Civ. R. 12(B)(6) motion to dismiss

- Standard: complaint fails to state a claim upon which
  relief can be granted under the plausibility framework
  (Ohio's analog of *Twombly*/*Iqbal*)
- Treats well-pled factual allegations as true
- Citation: *Mitchell v. Lawson Milk Co.*, 40 Ohio St.3d
  190 (1988) (12(B)(6) treats well-pled allegations as
  true); *Ogle v. Ohio Power Co.*, 70 Ohio St.3d 134
  (1994)

### Civ. R. 12(C) motion for judgment on the pleadings

- After pleadings are closed
- Court considers only the pleadings + attached exhibits
- *State ex rel. Midwest Pride IV, Inc. v. Pontious*, 75
  Ohio St.3d 565 (1996)

### Civ. R. 56 motion for summary judgment

- **14-day minimum notice** under Civ. R. 56(C)
- Movant must show no genuine issue of material fact
- Standard: *Dresher v. Burt*, 75 Ohio St.3d 280 (1996)
  (moving party bears initial burden; non-moving party
  then must point to specific facts in the record)
- Supporting evidence: affidavit, pleadings, discovery
  responses, transcripts under Civ. R. 56(C)

### Civ. R. 60(B) motion to vacate

- See `oh-post-judgment` for the five grounds + deadlines
- Citation: *GTE Automatic Electric, Inc. v. ARC
  Industries, Inc.*, 47 Ohio St.2d 146 (1976) (three-part
  test: (1) timely motion; (2) meritorious defense if relief
  is granted; (3) one of the five 60(B) grounds)

### Civ. R. 37 motion to compel

- Grounds: failure to respond to interrogatories, RFPs,
  RFAs, or to appear at deposition
- Meet-and-confer required by most Loc. R.
- Attorney's fees recoverable under Civ. R. 37(A)(4)

## Memorandum sections

### I. Statement of the Case

Concise factual + procedural posture. 1-3 paragraphs.

### II. Standard of Review

For each motion type, cite the controlling standard
(12(B)(6) plausibility; 56 *Dresher*; etc.).

### III. Argument

Point headings stating affirmative propositions. Each
section ties facts (citing affidavit ¶ or exhibit) to
legal authority (Ohio Civ. R., R.C., or Ohio appellate
case in public-domain format).

### IV. Conclusion / Prayer for Relief

Specific relief sought. Mirror the tendered proposed
order.

## Local-rule page limits

Common Pleas page limits vary materially:

- **Cuyahoga** — typically 20 pages for motion brief
- **Franklin** — typically 25 pages
- **Hamilton** — typically 25 pages
- **Summit** — typically 20 pages

Always verify per-court Loc. R. before drafting; longer
briefs may require leave of court.

## Composition with other oh- skills

- `oh-statewide-format` — caption + signature block format
- `oh-draft-declaration` — Ohio affidavit support for
  Civ. R. 56 motions
- `oh-draft-note` — notice of hearing (separate document)
- `oh-draft-order` — tendered proposed order
- `oh-discovery` — Civ. R. 37 motion to compel content
- `oh-deadlines` — service add-ons + response windows

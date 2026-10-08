---
name: ny-draft-motion-codearranger
title: Draft a New York Motion
description: Scaffold a motion for a New York court (Supreme, County, Civil Court of the City of New York, District, or City). Triggers include 'draft a New York motion', 'CPLR 2214 notice of motion', 'memo of law in support', 'New York motion structure', 'scaffold an OSC', 'order to show cause New York', 'attorney affirmation in support', 'CPLR 3211 motion to dismiss draft', 'CPLR 5015 motion to vacate draft', 'CPLR 3212 summary judgment motion draft'. Produces a four-document scaffold (Notice of Motion + Affirmation/ Affidavit + Memorandum of Law + Proposed Order) conformed to 22 NYCRR § 202.8-b page limits (25 pages memo / 15 pages reply), CPLR 2214 timing, and the assigned Justice's Part Rules.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/ny-court-docs/skills/ny-draft-motion
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Draft a New York Motion

> **NOT LEGAL ADVICE.** Applies the pro-se drafting framework adapted
> to New York. Verify the assigned Justice's Part Rules
> before finalizing — page limits, format, courtesy-copy
> requirements, and oral-argument practice vary.

## The standard NY motion packet

A motion in New York Supreme/County Court typically consists
of **four documents**:

1. **Notice of Motion** (CPLR 2214) — the scheduling document
   — see `ny-draft-note`
2. **Affirmation / Affidavit in Support** — sworn statement
   of facts plus the procedural history — see
   `ny-draft-declaration`
3. **Memorandum of Law in Support** — legal argument
4. **Proposed Order** — see `ny-draft-order`

Alternative: **Order to Show Cause (OSC)** packet:

1. **Order to Show Cause** — signed by a Justice; sets the
   hearing date and any TRO
2. **Affirmation / Affidavit in Support**
3. **Memorandum of Law** (optional but recommended)
4. **Proposed Final Order**

OSC is used when:

- Emergency relief is needed (TRO, stay of sale)
- Standard CPLR 2214 notice period is insufficient
- A specific Justice's Part Rules require OSC for certain
  relief

## Memorandum of Law structure

```
COVER PAGE (caption)

PRELIMINARY STATEMENT
[1-2 paragraphs: who, what, why this motion should be granted]

PROCEDURAL HISTORY / RELEVANT FACTS
[Cross-references to the supporting affirmation
paragraphs — do NOT restate facts the affirmation
already establishes]

POINT I — [HEADING STATING THE LEGAL CONCLUSION]

A. [Subheading]
[Argument with citations]

B. [Subheading]
[Argument with citations]

POINT II — [SECOND LEGAL CONCLUSION]

[Argument]

CONCLUSION
[The "ask" — the specific relief sought, restated]

Dated: ...
Signature block
```

## Page limits — 22 NYCRR § 202.8-b (2021)

Statewide (since 2021):

| Document | Page limit | Word-count alternative |
|----------|-----------|-----------------------|
| Memorandum of Law (initial) | **25 pages** | 7,000 words |
| Reply Memorandum | **15 pages** | 4,200 words |
| Affirmation/Affidavit | No page limit, but practical 25-page guideline |
| Notice of Motion | Typically 1-2 pages |

Word-count alternative permits a more flexible format. Where
the rule permits word-count, prefer it and add a word-count
certification at the foot of the memo.

**Commercial Division (22 NYCRR § 202.70(g) Rule 17)**: same
limits.

## CPLR 2214 service timing

| Service mode | Min. notice before return date |
|--------------|------------------------------|
| Personal delivery | 8 days |
| Mail | 8 + 5 = 13 days |
| NYSCEF (registered parties) | 8 days |

**Cross-motion** (CPLR 2215): must be served at least 7 days
before the return date.

**Reply**: per Part Rules; typically 1 to 7 days before the
return date.

## Affirmation v. affidavit choice

- **Affirmation** (CPLR 2106) — sworn statement by attorney,
  by certain professionals (medical, dental), and since the
  2023 amendment, **by any person**. No notary required.
- **Affidavit** (CPLR 2309) — sworn statement notarized
  under oath. Required pre-2023 for any sworn statement by a
  non-attorney non-professional.

Pro se litigants since 2023 should use **affirmation under
penalty of perjury** (CPLR 2106 as amended; L 2023, ch
559). The text:

> [PRINT NAME], being duly affirmed, hereby affirms the
> truth of the following under penalty of perjury pursuant
> to CPLR 2106:

(Signature)

## Memo opening template

```
PRELIMINARY STATEMENT

Defendant [NAME] respectfully submits this memorandum in
support of [his/her/their] motion pursuant to CPLR [SECTION]
to [RELIEF SOUGHT]. As set forth in the accompanying
[Affirmation/Affidavit] of [NAME] ("Defendant Aff."), this
action should be [dismissed/vacated/granted summary
judgment] because [ONE-SENTENCE LEGAL CONCLUSION].
```

## pro-se drafting framework — NY adaptations

| Pro-se drafting framework rule | NY specific |
|--------|------------|
| Cite the rule | Use CPLR section numbers; Tanbook citation format |
| Cite the record | Cross-reference to Defendant Aff. ¶ X / Pl. Aff. ¶ X |
| Verb economy | NY judges parse closely — prefer active voice; cut adverbs |
| Conclude with the "ask" | Restate the precise relief sought in the prayer |
| Caption matches every document | Index number on every page |

## Output format — DOCX

Generate DOCX with:

- 8.5 × 11 paper, 1-inch margins, double-spaced
- 12-point Times New Roman or equivalent serif
- Pagination footer
- Caption block per `ny-statewide-format`
- Tanbook-format citations
- Section heading style (Heading 1 for POINTs; Heading 2 for
  subsections)

Use the docx-js patterns documented in
`ny-statewide-format/references/docx-generation.md` (to be
authored).

## Composition with other ny- skills

- `ny-statewide-format` — formatting baseline
- `ny-draft-declaration` — affirmation/affidavit drafting
- `ny-draft-note` — Notice of Motion drafting
- `ny-draft-order` — proposed order drafting
- `ny-fact-check` — pre-filing fact-check
- `ny-file-packet` — packet assembly
- `ny-consumer-debt` — substantive content for debt-defense
  motions

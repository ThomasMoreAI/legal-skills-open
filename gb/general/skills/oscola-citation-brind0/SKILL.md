---
name: oscola-citation-brind0
title: OSCOLA citation check
description: Use when checking or correcting legal citations to OSCOLA in an essay, case note or seminar prep — when the user invokes /oscola-citation, asks to "check my citations", "OSCOLA this", or is about to submit a draft containing cases, statutes, books or journal articles.
author: Brind0
author_url: https://github.com/Brind0/oscola-cite/tree/main/skills/oscola-citation
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: gb
practice: general
language: en
---

# OSCOLA citation check

Two jobs, in this order. The script does the mechanical half; you do the
half that needs judgement. Never do the script's half by eye — you will
miss things it catches, and it is free.

## 1. Run the checker

```bash
python3 ~/projects/oscola-cite/oscola.py check <file>
```

It reports form problems with a rule code and the OSCOLA form. To apply
the automatic ones:

```bash
python3 ~/projects/oscola-cite/oscola.py fix <file>
```

`fix` rewrites the file in place, so the file should be committed or
saved first. Use `--dry-run` to see the result without writing. It only
ever touches punctuation, brackets and abbreviations; it never invents or
alters an authority.

## 2. Do the half the script cannot

The script checks the *shape* of a citation. It cannot know whether the
citation is true. These are yours:

- **Findings marked as needing judgement** (OSC005 missing court
  identifier, OSC006 case name not italicised). For OSC005, look the case
  up and supply the real court and best report — never guess a court from
  the case name. If you cannot verify it, leave the gap and tag it
  `(verify)` rather than inventing a plausible-looking report.
- **Is the authority real, and is the reference right?** Volume, report
  series, first page, year. The checker will happily pass a
  beautifully-formed citation to a case that does not exist. Check
  against a primary source: BAILII, ICLR, legislation.gov.uk, or
  Westlaw/Lexis via Cardiff.
- **Is it the best report?** OSCOLA 2.1.4 prefers the *Law Reports*
  (AC, QB/KB, Ch, Fam), then WLR, then All ER. A specialist series only
  when the case is not in those.
- **Pinpoints.** Paragraph numbers in square brackets for judgments;
  plain page numbers for books and articles.

## Hard rules

- Never state that a citation is correct because the checker passed it.
  Say what was checked: "form checks pass; I have not verified the
  authorities." Overclaiming here is the failure mode that matters,
  because a fabricated citation in a submitted essay is an academic
  misconduct problem, not a formatting one.
- Never add, complete or "correct" an authority from memory. A case
  reference you cannot see in a source is a gap to flag, not a blank to
  fill.
- The rules are OSCOLA 5th edn (2026). If the module handbook mandates
  the 4th edition, say so and carry on: the 5th edition kept the 4th's
  prescriptions for cases, legislation, books and articles, so a draft
  that passes is good for both.

## When your institution's guidance differs

The assessment criteria govern the mark; OSCOLA governs the form.
Where a module handbook specifies something different from OSCOLA
(footnotes versus inline citation is the usual one), the handbook wins
and you say which you have applied.

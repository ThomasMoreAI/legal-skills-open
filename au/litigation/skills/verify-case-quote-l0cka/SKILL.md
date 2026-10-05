---
name: verify-case-quote-l0cka
title: Verify Case Quote
description: Verify that a quoted passage attributed to an Australian judgment actually appears in the decision as published by the official court publisher, reporting the paragraph or page location and itemising any divergence. Use after the citation itself is verified, when a user asks whether a quote is genuine, accurately transcribed or correctly pinpointed, including checking documents for fabricated quotations. Do not use on text from aggregators or memory, for paraphrase assessment, or for interpretation or legal advice.
author: l0cka
author_url: https://github.com/l0cka/legal-skills/tree/main/plugins/australian-legal-research/skills/verify-case-quote
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: au
practice: litigation
language: en
---

# Verify Case Quote

A quote check runs only against judgment text obtained from the official
publisher in the same session — normally by `verify-hca-judgment`,
`verify-nsw-judgment` or `verify-federal-judgment` immediately beforehand.
Text from an aggregator, a secondary source or model memory proves nothing.

Read [../../references/case-law-verification-method.md](../../references/case-law-verification-method.md)
before checking. It defines the outcome semantics, access rules and
restriction handling.

## Workflow

1. Fix the scope.
   - Require a verified citation and the official publisher's text of the
     decision. If the citation is not yet verified, run the matching
     verification skill first; if it cannot be verified, the quote check is
     `UNVERIFIABLE` — do not proceed on unofficial text.
   - Return `OUTSIDE SCOPE` for paraphrase assessment ("is this a fair
     summary"), interpretation or advice.
2. Check restrictions before quoting.
   - If the decision page carries a restriction, suppression or
     non-publication notation covering the passage, report the notation and
     do not reproduce the restricted content.
3. Search for the passage.
   - Search the official text for the exact passage first.
   - If absent, search for a normalised form: straight quotes, collapsed
     whitespace, expanded ellipses, and case-insensitive matching. Treat an
     ellipsis in the supplied quote as a permitted omission and check the
     surrounding fragments in order.
4. Locate and compare.
   - Record the paragraph number or page marker where the passage appears.
   - If a pinpoint reference was supplied, check the passage appears at
     that pinpoint, and treat a location mismatch as a qualification.
   - Itemise every divergence between the supplied quote and the published
     text: spelling, punctuation, omitted words, altered emphasis.
5. Report using the result contract.

## Result contract

Lead with one status: `VERIFIED` for an exact match,
`VERIFIED WITH QUALIFICATIONS` for a near match or pinpoint mismatch with
divergences itemised, `UNVERIFIABLE` when the official text is unavailable,
`NOT FOUND` when there is no match in the verified text — a fabrication flag
for the quote even where the case is genuine — or `OUTSIDE SCOPE`.

```text
Requested check: <quote and attributed citation as supplied>
Jurisdiction: <from the verified citation>
Official case name: <as published>
Medium-neutral citation: <as verified>
Quote located at: <paragraph or page marker, or not found>
Supplied pinpoint: <as supplied and whether it matches, or none supplied>
Divergences: <none / itemised differences between supplied and published text>
Restrictions: <none observed / notation preserved verbatim>
Official sources: <exact URLs of the text actually searched>
Checked: <date and Australian timezone>
Limitations and review: <what remains unverified and the human-review point>
```

## Fail closed

Return `UNVERIFIABLE`, not `NOT FOUND`, when the official text could not be
obtained, is incomplete, or the passage may fall in a portion the publisher
did not reproduce. Return `NOT FOUND` only when the full official text was
searched in exact and normalised forms with no match. Never reconstruct a
"probable" quote, never verify against memory, and never present a located
quote as support for any legal proposition.

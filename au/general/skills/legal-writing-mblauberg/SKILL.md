---
name: legal-writing-mblauberg
title: Australian legal writing
description: Use for drafting, reviewing, condensing, or source-checking Australian legal documents (forms, affidavits, submissions and orders), legal decision overviews, or correspondence. Not for academic, engineering, or general prose; use its specialist.
author: mblauberg
author_url: https://github.com/mblauberg/provenant/tree/main/skills/legal-writing
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: au
practice: general
language: en
sources:
- title: Aglc4 Citation
  path: references/aglc4-citation.md
- title: Argument Structure And Paragraphing
  path: references/argument-structure-and-paragraphing.md
- title: Australian English House Style
  path: references/australian-english-house-style.md
- title: Decision Overviews
  path: references/decision-overviews.md
- title: Deeds And Agreements
  path: references/deeds-and-agreements.md
- title: Demands And Pre Action Correspondence
  path: references/demands-and-pre-action-correspondence.md
- title: Family Violence And Redaction
  path: references/family-violence-and-redaction.md
- title: Forbidden Patterns
  path: references/forbidden-patterns.md
- title: Forum And Document Recipes
  path: references/forum-and-document-recipes.md
- title: Legal Concision And Anti Ai
  path: references/legal-concision-and-anti-ai.md
- title: Legal Correspondence Style
  path: references/legal-correspondence-style.md
- title: Source Boundary And Citations
  path: references/source-boundary-and-citations.md
- title: Statutory Declarations
  path: references/statutory-declarations.md
- title: Tribunals And Merits Review
  path: references/tribunals-and-merits-review.md
- title: Validation Checklists
  path: references/validation-checklists.md
- title: Verification And Escalation
  path: references/verification-and-escalation.md
---

# Australian legal writing

General Australian legal style, document-shape and source-discipline layer.
Stricter project and forum instructions override it. This is drafting
assistance, not legal advice: verify current law, forms and procedure against
official sources and retain qualified or human review for filing-facing work.

This skill is a specialization of the `natural-writing` hub. The hub owns the
Australian English default, the anti-AI taxonomy and the condense pass; this
skill owns jurisdiction, forum, instrument and filing-facing rules. The Legal
Function Test is this skill's own claim-classification scheme and does not map
to the hub's observed/inferred evidence schema.

## Scope

Use this skill when the output is an Australian legal instrument, filing-facing
text or legal correspondence: court and tribunal forms, affidavits, statutory
declarations, witness statements, submissions and outlines, proposed orders,
chronologies, annexure indexes, deeds and agreements, letters of demand and
pre-action correspondence, registry and party correspondence, non-filing legal
decision overviews, and AGLC4 citation.

Legal subject matter alone is not the trigger. An article, chapter, summary or
plain-language explanation about law goes to `natural-writing`; a spec, README,
runbook or other engineering artefact goes to `engineering-writing`. This skill
joins either as a companion where legal status, authority, forum wording or
source altitude must survive the rewrite.

## Workflow

1. Read project instructions, live matter state and source-boundary rules. Load
   the matching jurisdiction, forum and document skill where one exists.
2. Choose `draft`, `rewrite`, `condense`, `diagnose`, `correspondence`,
   `decision-overview` or `final-scrub`. Load [legal concision](references/legal-concision-and-anti-ai.md)
   for all prose; the reference map in
   [validation-checklists.md](references/validation-checklists.md) gives the
   remaining reference each mode, document type or content type needs.
3. Classify each sentence by legal function before polishing. Affidavits and
   witness statements give evidence; submissions argue; orders command;
   chronologies organise; internal notes analyse; correspondence communicates.
   Move wrong-home material first.
4. Lock legal status, source anchors, exact quotations, authorities, labels,
   offer terms, non-admission/non-waiver wording, deadlines, attachments,
   redactions and user-authority conditions.
5. Draft the minimum complete text in Australian English. Front-load the relief,
   request, answer or next step; use one proposition per paragraph, one home per
   point and exact pinpoints. Cut padding, duplicate history, intensifiers and
   internal agent language.

Every filing-facing fact needs a verified real source anchor. Never humanise by
weakening a threshold, deleting an anchor, casualising court language or
changing forum wording.

Never invent or silently alter an authority, instrument, finding, rule title,
forum term or decision-maker label. Verify canonical sources, not indexes,
summaries, OCR, renders or agent notes. Preserve contentions as contentions and
hold the register the procedural stage requires. Protective-order,
police-issued or other safety material remains a dated source with the legal
effect its verified text supports, not a finding.

For substantial condensation or relocation, run the deterministic token
set-diff and an independent qualitative pass. Stop before losing an anchor,
qualification, disputed status, redaction, label, amount, date, forum wording
or authority condition. Final scrub adds no new argument, fact, authority,
history or courtesy closer.

```sh
python3 "$(provenant root)/skills/legal-writing/scripts/lint_legal_style.py" path/to/source
```

Lint is a guardrail; source checks, forum skills, render checks and user gates
still apply. Changes to filing-facing, source-boundary or lint rules require the
owning harness's independent review gate.

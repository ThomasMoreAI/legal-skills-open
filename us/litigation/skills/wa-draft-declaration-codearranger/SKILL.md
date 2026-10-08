---
name: wa-draft-declaration-codearranger
title: Draft a Washington Declaration
description: Use this skill when the user asks to draft a declaration for a Washington State court filing. Triggers include "draft a declaration", "declaration in support", "declaration of defendant", "declaration of plaintiff", "witness declaration", "affidavit" (Washington uses declarations under penalty of perjury per RCW 9A.72.085 in place of notarized affidavits for most filings), and "declaration with exhibits". Scaffolds a declaration with numbered paragraphs, verification clause, signature block, and optional exhibit cover pages. Composes with `wa-statewide-format` (always), `wa-kcdc` (if KCDC), and `wa-pro-se` (if the declarant is pro se).
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/wa-court-docs/skills/wa-draft-declaration
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Draft a Washington Declaration

Scaffold a new declaration that complies with GR 14 and statewide
pleading conventions. The declaration should be ready to fill in, sign,
and file.

> **NOT LEGAL ADVICE.** This skill scaffolds a court document as
> a drafting aid. The user — not the skill — is the declarant,
> chooses what facts to swear to, and signs the declaration.
> Verify every rule, deadline, and citation against current law
> before filing. Pair with substantive review by counsel where
> stakes warrant.

## Inputs to gather

Before drafting, confirm these with the user (use AskUserQuestion if any
are unclear):

1. **Court** — Which court? (e.g., "King County District Court, South
   Division, Burien"). If KCDC, also load the `wa-kcdc` skill.
2. **Case caption** — Party names and case number
3. **Declarant** — Who is signing the declaration?
4. **Role** — Pro se? Plaintiff? Defendant? Witness?
5. **Purpose** — What motion or filing does it support?
6. **Exhibits** — Any exhibits to attach? How many? What format?
7. **Output format** — Draft .md for review first, or go straight to
   .docx?

## Steps

1. **Load the companion skills.** Read
   `skills/wa-statewide-format/SKILL.md` and
   `skills/wa-statewide-format/references/templates/declaration.md`
   for the template. If the court is KCDC, also read
   `skills/wa-kcdc/SKILL.md`. If the declarant is pro se, also read
   `skills/wa-pro-se/SKILL.md` and
   `skills/wa-pro-se/references/pro-se-drafting-framework.md`.

2. **Draft in markdown first.** Produce a markdown draft that the user
   can review and edit. Use the structure from `declaration.md`:
   - Court header
   - Two-column caption
   - Salutation with perjury clause
   - Numbered paragraphs (bold lead-ins for labeled topics)
   - Verification clause mirroring the salutation
   - Date and place of execution
   - Signature block
   - Exhibit list (if exhibits)
   - Exhibit cover pages (one per exhibit)

3. **Apply the pro-se drafting framework** if the declarant is pro se:
   - Single best fact up front
   - Every factual assertion tied to an exhibit or personal knowledge
   - No argument in the declaration — save that for the brief
   - Plain declarative sentences

4. **Review with the user.** Show the draft. Ask what to adjust before
   generating the .docx.

5. **Generate the .docx** using the docx-js pattern documented in
   `skills/wa-statewide-format/references/docx-generation.md`:
   - Letter size (12240 × 15840 DXA)
   - 1" margins with 2880 DXA `spacing.before` on first paragraph
     (effective 3" top margin on page 1)
   - Times New Roman 12pt
   - 1.5 line spacing
   - Footer: document title (left) + page X of Y (right)
   - Exhibit cover pages with scaled image if provided

6. **Deliver** the .docx to the user's selected folder via a
   `computer://` link. Offer to run the `wa-quality-check` skill on
   it.

## Notes

- Declarations are the factual backbone of a motion. Keep them factual
  — no argument, no characterization, no adjectives
- Bold lead-ins on paragraphs with distinct sub-topics so a judge can
  skim
- Always include a signature block with email for pro se filers
- If exhibits are from a phone screenshot or other native color source,
  GR 14(a) permits the color if grayscale would make them illegible

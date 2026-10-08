---
name: format-aglc4-citations-l0cka
title: AGLC4 legal citation
description: Draft, convert, review, and correct Australian legal citations and bibliographies in Australian Guide to Legal Citation, 4th edition (AGLC4) format. Use for footnotes, pinpoints, subsequent references, cases, legislation, secondary sources, treaties, international materials, foreign legal materials, quotation treatment, citation audits, reference lists, or any document that contains legal or evidentiary citations. Do not use this skill to verify that a cited source exists or says what is claimed; formatting and source verification are separate tasks.
author: l0cka
author_url: https://github.com/l0cka/legal-skills/tree/main/plugins/australian-legal-research/skills/format-aglc4-citations
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: au
practice: general
language: en
sources:
- title: Citation Templates And Audit
  path: references/citation-templates-and-audit.md
- title: Domestic Sources
  path: references/domestic-sources.md
- title: Foreign Domestic Sources
  path: references/foreign-domestic-sources.md
- title: General Rules
  path: references/general-rules.md
- title: International Materials
  path: references/international-materials.md
- title: Secondary Sources
  path: references/secondary-sources.md
- title: Source Map
  path: references/source-map.md
---

# AGLC4 legal citation

Apply AGLC4 to every citation. Preserve the source's substantive details; change only citation form unless the user asks for source verification or correction.

## Workflow

1. Identify each source type before formatting it. Do not format from a URL, database label, or incomplete search result when the source itself is available.
2. Read [references/general-rules.md](references/general-rules.md) for every task. Then read the topic reference that covers the source:
   - [references/domestic-sources.md](references/domestic-sources.md) for Australian cases and legislative materials;
   - [references/secondary-sources.md](references/secondary-sources.md) for articles, books, reports, parliamentary material, media, webpages, and social media;
   - [references/international-materials.md](references/international-materials.md) for treaties, UN documents, international courts and tribunals, WTO/GATT, and supranational materials; or
   - [references/foreign-domestic-sources.md](references/foreign-domestic-sources.md) for foreign cases, legislation, constitutions, translations, and non-English sources.
3. Collect and verify every required field. Mark a missing field as unresolved; never invent an author, date, court, report series, document number, pinpoint, URL, or access detail.
4. Build the first citation in full. Add the most precise useful pinpoint. Use an authorised report before an unauthorised report or medium-neutral citation when AGLC4 requires that preference.
5. Apply `Ibid`, `(n X)`, a short title, or `at` only after checking the citation sequence. Renumber cross-references after footnotes move.
6. If the document requires a bibliography or References section, include every source relied on and transform footnote citations under AGLC4 rule 1.13. Read [references/citation-templates-and-audit.md](references/citation-templates-and-audit.md).
7. Run a final audit for source identity, element order, italics, quotation marks, brackets, commas, pinpoints, subsequent references, URLs, bibliography ordering, and closing punctuation.

## Output rules

- Give the corrected citation first. Explain a change only when it resolves ambiguity, incomplete metadata, or a material source-selection issue.
- Use footnotes for authorities unless the target document or user requires another citation placement.
- Put a full stop or other closing punctuation at the end of every footnote. Do not put full stops at the end of bibliography entries.
- Keep citation typography explicit in rich text. In plain text, use Markdown italics for titles that AGLC4 italicises.
- Separate multiple sources in one footnote with semicolons. Start a new sentence when the introductory signal changes.
- Treat source verification and citation formatting as separate findings. A perfectly formatted citation can still identify the wrong source.

## When AGLC4 has no rule

Use the closest analogous AGLC4 source type, then prioritise clarity and consistency for the intended Australian audience. State the analogy and any unresolved choice. Do not silently substitute another citation system.

## Source boundary

This skill is an operational distillation of the published AGLC4, not a replacement for the publication. Read [references/source-map.md](references/source-map.md) when an exact rule number, chapter boundary, edition fact, or source limitation matters. The PDF this distillation was prepared from omits the appendices listed in its contents; verify uncommon abbreviations against an authorised complete AGLC4 copy.

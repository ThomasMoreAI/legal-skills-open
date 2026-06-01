---
name: office-docx
title: Office DOCX
description: 'Create, edit, inspect, format, template, and validate Microsoft Word .docx files with task-specific .NET and OpenXML SDK implementations. Use for Word/DOCX work: reports, manuscripts, contracts, proposals, formal documents, text replacement, placeholder filling, tables, images, sections, headers/footers, page numbers, TOC, template formatting, CJK document layout, or DOCX repair.'
author: arih04x
author_url: https://github.com/arih04x/office-skills/tree/main/office-docx
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Office DOCX

Use this skill for Word `.docx` tasks. Implement with C# on .NET + OpenXML SDK.

## Operating Model

- `dotnet` from PATH; NuGet package `DocumentFormat.OpenXml`.
- Copy `assets/dotnet-starter/` as starting point when useful.
- Preserve source document; write result to a separate `.docx`.
- Keep content editable (paragraphs, runs, tables, styles, fields, drawings).

## Task Selection

| Task | Read | Focus |
| --- | --- | --- |
| Create new document | `references/create-docx.md` | Package, body, styles, page setup, tables, images, fields |
| Edit existing `.docx` | `references/edit-existing-docx.md` | Copy to output, inspect, modify content |
| Apply/imitate template | `references/template-formatting.md` | Transfer styles/theme/numbering safely |
| Validate/repair | `references/validation.md` | OpenXML validation, package inspection |
| Structural rules | `references/openxml-rules.md` | Element ordering, units, sections, tables |

Read the matching reference, implement, run, validate with `scripts/check-docx.py`.

## Key Rules

- Use SDK classes, not raw ZIP string edits.
- Text replacement: single-run matches only; multi-run → paragraph-level rewrite.
- Generated docs: define styles first, then content via style IDs.
- CJK: set East Asian fonts in `RunFonts`; confirm spacing and hierarchy.
- Final `sectPr` must be last child of `w:body`.

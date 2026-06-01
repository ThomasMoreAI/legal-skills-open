---
name: llp-create
title: llp-create
description: Create a new LLP document in this repo with the next available number, the correct filename convention (NNNN-slug.type.md), and a scaffolded metadata header ready to fill in.
author: ccheever
author_url: https://github.com/ccheever/llp/tree/main/skills/llp-create
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# llp-create

Use this skill when the user wants to create a new LLP document. This handles numbering, filename generation, and the initial metadata scaffold so the user can focus on content.

Invoke as `/llp-create <title>` with an optional title, or `/llp-create` and the skill will ask for one.

## Ground rules

- LLP documents live in `llp/` (flat or grouped into subdirectories — see LLP 0000 for filesystem organization rules).
- Filenames follow `NNNN-slug.type.md` where `NNNN` is zero-padded four digits, `slug` is a lowercase kebab-case identifier, and `type` is the lowercased document type.
- Numbers are globally unique across the entire `llp/` tree, including subdirectories and `llp/tombstones/`. Never reuse a number that has ever been assigned.
- Standard types (LLP 0000 §Types): `rfc`, `spec`, `decision`, `plan`, `explainer`, `principle`, `guide`, `issue`, `research`. Projects may define additional types; check the project's root LLP for any local conventions.
- Standard statuses (LLP 0000 §Statuses): `Draft`, `Review`, `Accepted`, `Active`, `Superseded`, `Tombstoned`. New LLPs start as `Draft`.

## Workflow

### 1. Determine the next LLP number

Scan all files in `llp/` (including subdirectories and `llp/tombstones/`) that match the pattern `NNNN-*.md`. Extract the numeric prefix of each. The next number is `max(existing) + 1`, zero-padded to four digits.

If another LLP tree exists in a non-standard location (some projects use `docs/site/content/llp/` or similar), include it in the scan. Check the project's root LLP or `CLAUDE.md` / `AGENTS.md` for any documented LLP locations.

### 2. Ask the user for the metadata if not provided

Required to produce a useful scaffold:

- **Title** — short, sentence case. If not provided by the slash command argument, ask.
- **Type** — which of the standard types fits best. If the user didn't specify, propose one based on the title and current conversation context, then confirm. Common cues:
  - "How should we..." / "Proposal to..." → `rfc`
  - "What are the requirements..." / "Specification of..." → `spec`
  - "We decided..." / "Chose X over Y" → `decision`
  - "How we'll build..." / "Step-by-step" → `plan`
  - "What is..." / "How ... works" → `explainer`
  - "Always do..." / "Never do..." → `principle`
  - "How to use..." / "Workflow for..." → `guide`
  - "Bug in..." / "Problem with..." → `issue`
  - "Analysis of..." / "Findings from..." → `research`
- **Systems** — one or more system tags relevant to this LLP. Ask if unclear.
- **Related** — existing LLPs worth reading alongside this one. Ask the user or propose based on topic overlap.

### 3. Generate the slug from the title

- Lowercase
- Replace any character that is not `a-z0-9` with `-`
- Collapse repeated `-` into a single `-`
- Trim leading and trailing `-`
- Keep it short — aim for fewer than 6 words. If the title is long, truncate the slug after the meaningful words.

Example: `"Token rotation and session management"` → `token-rotation-and-session-management`. If that feels long, shorten to `token-rotation`.

### 4. Create the file

Write to `llp/NNNN-slug.type.md` (or a project-specific subdirectory if the user indicates one). Do not create the file in `llp/tombstones/` unless explicitly asked.

Scaffold:

```markdown
# LLP NNNN: <Title>

**Type:** <Type>
**Status:** Draft
**Systems:** <Systems>
**Author:** <Author>
**Date:** YYYY-MM-DD
**Related:** <Related, or leave blank>

## Summary

One or two paragraphs that summarize what this document is about and what a reader should come away knowing.

## Motivation

Why does this exist? What problem does it solve?

## Design

The body of the document. Structure this however the type and topic demand — RFCs usually have a Design section with sub-headings; Decisions have Context / Options / Decision / Consequences; Plans have phase breakdowns; etc.

## Open questions

What is not yet decided or needs more work.

## References

- LLPs referenced
- External sources
```

The exact scaffold may be customized per type. For instance:

- **Decision** documents should use the ADR-style `Context / Options considered / Decision / Consequences` structure.
- **Plan** documents should have a `Phases` or `Milestones` section.
- **Principle** documents should use `Principle / Rationale / How to apply` for each principle listed.
- **Research** documents should have `Findings` and `Confidence`.

Ask the user if they want the type-specific scaffold, or just the generic one.

### 5. Help draft content from conversation context

After creating the file, offer to draft initial content based on the current conversation. If the user has been discussing the topic, pull the relevant threads into a first-draft body. If not, leave the scaffold as-is and let the user write the content.

## After creation

- Confirm the file path and the assigned number back to the user.
- Offer to add cross-references from other LLPs that should now link to this one (`llp-related` is a separate skill for this).
- Remind the user that the LLP is `Draft` and will need review before moving to `Active`. Use the `llp-review` skill for that.

## Scope limits

- Do not modify other LLPs without the user's explicit request.
- Do not pick a document type without user confirmation if the choice is ambiguous.
- Do not overwrite existing files. If the chosen filename already exists, bail out and ask the user what to do.
- Do not invent LLP numbers. Always derive from the existing tree.

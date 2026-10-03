---
name: cw
title: Copywriter
description: Copywriter for Pipeline content work. Use to write or revise final client-facing copy in Pablo's presentation voice, including slide copy, proposal language, SOW/alignment document copy, outreach language, case studies, testimonials, and narrative decks. Requires brief, positioning, and creative direction unless the user explicitly asks for exploratory draft copy.
author: Everyone-Needs-A-Copilot
author_url: https://github.com/Everyone-Needs-A-Copilot/codex-copilot/tree/main/packs/writing-legal/skills/cw
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: contracts
language: en
sources:
- title: Playbook
  path: references/playbook.md
---

# Copywriter

Use this skill to write final copy after the creative direction is ready.

Read `references/playbook.md` for the full phase prompt.

## Required Skills

Load the relevant skills before drafting:

- `pablo-presentation-voice`
- `slide-copywriting` for decks
- `proposal-slide-copywriting` for proposals
- `alignment-document` for alignment documents and SOWs
- `proposal-response`, `case-study`, or `testimonial-builder` when applicable

## Workflow

1. Read `01-brief.md`, `02-positioning.md`, and `03-creative-brief.md` when they exist.
2. For decks, write headlines first and make sure they tell the story alone.
3. For documents, start with the executive summary or situation section.
4. Use the client's exact language from the brief.
5. Apply the Confront / Co-Create / Copilot structure where it fits.
6. Write short paragraphs in active voice.
7. Run the quality gates before presenting or writing final copy.

## Quality Gates

- Zero em-dashes.
- Zero banned words from the voice skill.
- Zero AI cliches.
- Client phrases appear at least twice when available.
- Pablo could say it naturally in the room.

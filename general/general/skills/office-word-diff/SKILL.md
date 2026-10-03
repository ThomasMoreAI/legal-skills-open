---
name: office-word-diff
title: office-word-diff
description: Use when you need to apply word-level tracked changes to Microsoft Word documents programmatically, preserve formatting through diffs, or integrate with Office.js for document transformation.
author: LegalQuants
author_url: https://github.com/LegalQuants/lq-skills/tree/main/skills/office-word-diff
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
tags: [word, office-js, tracked-changes, docx, diff, document-processing]
---

# office-word-diff

## When to Use

- You need to apply AI-generated edits as tracked changes in Word documents
- You're building a legal tool that produces DOCX output with redlines
- You need deterministic, word-level text comparison (not just line-level diff)
- You want to preserve formatting through document transformations
- You're integrating with Claude Code, Cursor, or other agents that produce document changes

## How It Works

### Core Problem

Most diff tools operate at the line or paragraph level. Word documents have structural complexity — nested lists, tables, headers, formatting runs — that line-based diffs destroy. `office-word-diff` solves the kernel-level problem: applying word-level tracked changes to DOCX while preserving formatting.

### Architecture

1. **Parse** — Read DOCX via Office.js API, extract text runs with formatting metadata
2. **Diff** — Compute word-level differences between old and new text
3. **Transform** — Insert Word-compatible tracked changes (insertions/deletions) preserving formatting
4. **Output** — Return valid DOCX with native Word tracked changes

### Usage

```javascript
import { diffWords } from 'office-word-diff';

const result = await diffWords(oldDoc, newDoc, {
  trackChanges: true,
  author: 'LQClaw'
});
```

### Key Features

- **Granular tracked changes** — Word-level, not paragraph-level
- **Format preservation** — Bold, italic, underlines survive transformation
- **Nested structures** — Handles tables, lists, headers correctly
- **Agent-compatible** — Works with Claude Code, Gemini CLI, Codex as backend
- **Deterministic** — Same input produces same output (unlike fragile text-matching approaches)

## Audience and Work Shape

Audience: lawyers and developers building Word add-ins or document-transformation tools that emit native tracked changes. Output is consumed by Microsoft Word and ultimately signed off by a lawyer.

Work shape: Bounded Transactional. The skill applies a defined set of word-level edits to a DOCX and emits revised DOCX. It does not decide which edits to apply.

## Scope and Legal Use

This skill provides legal *support*, not legal advice. The output is a DOCX with tracked changes — not a redlined version that is approved, signed off, or fit to send to counterparties or file with a court.

**Privilege and confidentiality.** Runs client-side via Office.js. No network calls. The skill does not transmit document content anywhere. Privilege exposure depends entirely on what the calling application does with the input and output — the lawyer must control the data flow.

**Accountability.** A qualified lawyer must review every tracked change in the output before accepting, sending, filing, or storing the revised document. The author field (`author: 'LQClaw'` in the usage example) makes the AI origin visible in Word's revision metadata — keep that visible rather than masking it as a human author.

## Confidence Bands

The diff itself is deterministic, but the *upstream* generation of `newDoc` (from an AI agent) is not. Tag tracked changes with confidence from the upstream agent where possible:

- **High** — small, scoped edit (typo, defined-term substitution, cross-reference fix).
- **Medium** — clause rewrites, paragraph reordering, or any substantive change. Always lawyer-reviewed.
- **Low** — multi-clause or whole-section rewrites. Treat as a draft proposal, not a redline.

## Out of Scope

- Not for **executed contracts** without separate amendment-protocol controls.
- Not for **documents under litigation hold** or e-discovery where original metadata must be preserved.
- Not a final-send step — never auto-accept changes and transmit.
- Not for documents with **DRM, IRM, or rights-managed protection** (will fail or strip protection).
- Not for documents with pre-existing **unaccepted tracked changes** unless explicitly handled by the calling tool (state must be reconciled first).

## Escalation

Stop and route to the responsible lawyer when:
- a nested-table edit cannot be applied without structural loss;
- the input DOCX has pre-existing unaccepted tracked changes from another author;
- the upstream agent produced a Low-confidence edit set or contradictory edits;
- the document is rights-managed, encrypted, or under a litigation hold.

## Limitations

- Requires Office.js (needs to run in Word context or headless Word)
- Windows/macOS only (no Linux for Word)
- Very complex nested tables may have edge cases

---
name: superdoc-redlines
title: superdoc-redlines — Multi-Agent DOCX Redlining
description: Use when you need to apply tracked changes and comments to DOCX files programmatically, merge multi-agent edits with conflict resolution, or produce native Word revisions from AI agent output.
author: LegalQuants
author_url: https://github.com/LegalQuants/lq-skills/tree/main/skills/superdoc-redlines
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
tags: [docx, redlines, multi-agent, conflict-resolution, document-processing]
---

# superdoc-redlines — Multi-Agent DOCX Redlining

## When to Use

- Multi-agent legal workflows where different agents produce edits to the same document
- Applying AI-generated tracked changes to DOCX files
- Merging edits from multiple reviewers with conflict resolution
- Headless document transformation (no Word installation required)
- Deterministic document edits with stable block IDs

## How It Works

### Core Innovation

Uses **stable block IDs** instead of fragile text matching. Unlike approaches that try to find text by content (and fail when formatting changes), Superdoc assigns stable IDs to document blocks and applies changes by reference.

### Architecture

```
AI Agent output → Conflict resolution → Block ID mapping → Native Word revisions
```

### Process

1. **Parse** — Extract document blocks with stable IDs
2. **Receive edits** — AI agent produces change instructions
3. **Conflict resolution** — If multiple agents edit same block, resolve conflicts
4. **Apply** — Insert Word tracked changes using block IDs (not text matching)
5. **Output** — Native DOCX with Word revision marks

### Usage

```javascript
import { applyRedlines } from 'superdoc-redlines';

const result = await applyRedlines({
  input: './contract.docx',
  edits: agentEdits,
  agentName: 'Claude'
});
```

### Key Features

- **Multi-agent merging** — Multiple agents can edit; conflicts are flagged
- **Conflict resolution** — Human review for overlapping edits
- **Deterministic** — Same edits → same output (unlike text-matching approaches)
- **Native Word revisions** — Output is valid DOCX, not a proprietary format
- **Works headlessly** — No Word installation needed

## Audience and Work Shape

Audience: lawyers and developers running multi-agent DOCX workflows where several AI agents propose edits to the same document. The lawyer is the merger of last resort.

Work shape: Bounded Transactional with conflict-resolution overlay. The skill merges defined edits by stable block ID. Conflicts are surfaced, not silently resolved.

## Scope and Legal Use

This skill provides legal *support*, not legal advice. The merged DOCX is an AI-assembled draft with native Word tracked changes — not a reviewed, accepted, or approved version.

**Privilege and confidentiality.** Runs headlessly with no required network calls. The `agentName` field is persisted in Word's revision XML — the AI origin of each edit is visible in the document's audit trail. Do not mask `agentName` as a human reviewer; that misrepresentation can affect privilege and disclosure analysis later.

**Accountability.** A qualified lawyer must review every tracked change in the merged output before accepting, sending, filing, or relying on it. The lawyer decides what each agent's edit is worth; the conflict-resolution engine only ensures merges are deterministic, not correct.

## Input Requirements

- DOCX must have stable block structure (no rights-management, no DRM).
- `edits` input must conform to the documented schema (per-agent, per-block).
- Halt on malformed agent output; do not silently best-effort merge.

## Confidence Bands

- **High** — non-overlapping edits from a single agent, each scoped to one block.
- **Medium** — non-overlapping edits from multiple agents.
- **Low / Conflict** — overlapping edits on the same block from different agents, or contradictory edits from a single agent. Surface to lawyer; do not auto-resolve.

## Out of Scope

- Not for **executed contracts** or **engrossed final versions**.
- Not for **documents under litigation hold**.
- Not for **structurally invalid DOCX** or rights-managed documents.
- Not a sign-off mechanism — Word's revision marks indicate AI authorship, not human review status.

## Escalation

Stop and route to the responsible lawyer when:
- two or more agents edit the same block in incompatible ways;
- an agent emits malformed edit instructions (schema violation);
- the merge would silently overwrite an existing tracked change from a named human reviewer;
- the document state is ambiguous (e.g., partial tracked changes already present from a prior round).

## Limitations

- Complex nested tables may need manual review
- Requires well-structured input from AI agents
- Conflict resolution UI is basic

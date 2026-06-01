---
name: softcopy-proof-check
title: softcopy-proof-check
description: Build and validate ownership evidence checklists from the declared development mode. Use when proof documents are needed for formal review. Do not use for unrelated writing or code analysis.
author: yult222
author_url: https://github.com/yult222/Software-Copyright-Material-Generation-Skills-for-Codex/tree/main/.agents/skills/softcopy-proof-check
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# softcopy-proof-check

## Purpose

Create ownership evidence checklists and missing-proof reports.

## Triggers

- Proof or ownership review is required
- `development_mode` is known or needs checklist generation

## Non-triggers

- Generic drafting
- Repository scan without filing context

## Required outputs

- `softcopy/outputs/proof_check/ownership_evidence.candidate.yaml`
- `softcopy/outputs/proof_check/proof_checklist.md`
- `softcopy/outputs/proof_check/missing_proofs.md`

## Hard rules

- Use `development_mode`, never `ownership_mode`
- Distinguish required vs optional documents
- Do not overwrite an existing approved `softcopy/ownership_evidence.yaml`

## Workflow summary

1. Read confirmed or candidate development mode.
2. Generate proof checklist.
3. Mark missing and provided documents separately.

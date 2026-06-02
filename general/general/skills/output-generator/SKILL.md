---
name: output-generator
title: Output Generator
description: Generate mode-specific legal research deliverables, enforce citation style, and handle file format confirmation and save flow.
author: kipeum86
author_url: https://github.com/kipeum86/game-legal-research/tree/main/.claude/skills/output-generator
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Output Generator

Use this skill at Step 8.

## Inputs

- Analysis result (Step 6)
- Selected mode (A/B/C/D or auto)
- Output language
- File format preference

## Mandatory Sections

Every output must include:
1. Scope & as-of date
2. Conclusion summary
3. Issue tree
4. Detailed analysis
5. Annotated bibliography
6. Verification guide

## Citation Integrity Rules (Anti-Laundering)

Apply `docs/style-guides/legal-research-core-contract.md`. In the Verification Guide
(mandatory section #6), list primary sources separately from supporting commentary
and flag any conclusion where primary-source verification was not possible.

## Templates

- `references/mode-a-template.md`
- `references/mode-b-template.md`
- `references/mode-c-template.md`
- `references/mode-d-template.md`
- `references/citation-format-guide.md`

If output intent matches legal opinion deliverables (`법률 의견서`, `opinion letter`, `legal opinion`, `formal opinion`, `opinion memo`), ALWAYS read:
- `.claude/skills/legal-opinion-formatter/SKILL.md`

This is a mandatory routing rule for opinion-letter style outputs.

## Mode Auto-Selection Rules

When `output_mode` is `auto`, select based on the dominant query characteristic:

| Query characteristic | Mode |
|---|---|
| Executive summary, management briefing, quick action list | **A** — Executive Brief |
| Multi-jurisdiction comparison, regulatory matrix, divergence | **B** — Comparative Matrix |
| Enforcement history, case law survey, regulatory decisions | **C** — Enforcement & Case Law |
| Deep statutory analysis, article-by-article commentary, black-letter text | **D** — Black-letter & Commentary |

Tie-breaking rule: prefer Mode B when 2+ jurisdictions and a comparison table is useful; prefer Mode A when the user signals a time constraint or uses words like "summary" or "quick overview."

State selected mode and one-line rationale before generating output (e.g., `Mode B selected — 3 jurisdictions require comparative matrix.`).

## Format & Save Rules

1. First query in session: ask preferred file format.
2. Later queries: confirm previous format.
3. Before promising a save, confirm the requested format is actually available in the current environment.
   - `.docx` requires `python-docx`.
   - `.pdf` and `.pptx` require a working converter path; if unavailable, state the limitation and offer `.docx` or `.html`.
4. Show inline preview first.
5. Save only after explicit confirmation.
6. If the deliverable will trigger Step 10 (Mode B/C/D, memo, or opinion), save the confirmed content as a markdown draft first and return that draft path to the orchestrator. Do not treat this draft as the final artifact.
7. After Step 10 completes or is explicitly skipped, render the final requested format exactly once.
8. After final rendering, verify the artifact exists on disk and is non-empty before reporting success.
9. If file name collides, append `_v2`, `_v3`, etc.

## Scripts

- Unix-like: `scripts/file-converter.sh`
- Windows PowerShell: `scripts/file-converter.ps1`

Use the converter wrapper when deterministic file conversion dispatch is needed.

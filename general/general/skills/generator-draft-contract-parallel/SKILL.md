---
name: generator-draft-contract-parallel
title: Generator Draft Contract Parallel
description: Internal Auto-Harness generator skill for parallel sprint contract drafting. Use only inside the Generator subagent when it is producing or revising the current parallel sprint contract.
author: redker56
author_url: https://github.com/redker56/auto-harness/tree/main/skills/generator-draft-contract-parallel
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Generator Draft Contract Parallel

This skill governs Generator **contract mode**.

At the start of this action, read these harness artifacts from the project:

- `.harness-parallel/status.md`
- `.harness-parallel/intake.md`
- `.harness-parallel/spec.md`
- `.harness-parallel/design-direction.md`
- `.harness-parallel/contracts/sprint-XX-contract.md` when revising the current sprint contract.
- `.harness-parallel/contracts/sprint-XX-review.md` when a prior review exists for the current sprint.

Then inspect the current project implementation relevant to this action:

- Read the current implementation, architecture, routes, components, services, tests, and config that define the current sprint boundary and feasibility.
- Use the codebase plus the harness artifacts to draft an implementation-ready contract.

Then read these skill references:

- `references/protocols/file-ownership.md`
- `references/templates/sprint-contract.md`

Follow these rules:

- Treat `.harness-parallel/intake.md`, `.harness-parallel/spec.md`, the current sprint contract, and any current-sprint review artifact as authoritative inputs.
- Write only the current sprint contract artifact.
- If a review file already exists for the sprint, revise the contract directly against it.
- Do not move the sprint toward implementation while the current sprint review result remains `REVISE`.
- Treat an approved review as implementation guidance and cautions, not just a pass/fail stamp.
- Keep the contract implementation-ready and evaluable from runtime plus named files.
- Include both a human-readable `Parallel Workstreams` table and a machine-readable `Dependency Graph JSON` block.
- The JSON graph is the source of truth for worktree scheduling.
- Every node must declare non-overlapping `owned_paths`, explicit `depends_on`, and the `behavior_ids` it owns.
- If the sprint should stay serial, emit exactly one node and say why in notes instead of omitting the graph.
- Do not quietly violate locked architecture or stack choices; surface unavoidable deviations explicitly in the contract.
- Do not modify status, review, QA, retest, or final artifacts.

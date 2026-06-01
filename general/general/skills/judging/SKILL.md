---
name: judging
title: Overview
description: Dispatch the Court on evidence-only inputs (contract + diff + verify output + confidence). The Court is not a persona; it is a structured adjudicator.
author: forsonny
author_url: https://github.com/forsonny/DG-Anvil/tree/main/skills/judging
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

## Overview

This skill dispatches the Court to adjudicate a task's verification result. The Court is not a persona; it is parameterized by the contract's check types. Inputs are the contract, the captured diff, the four-level Verify output, and a confidence score. Plan, commit messages, ledger, and prior verdicts are structurally withheld.

## When to Use

Invoked by the orchestrator after `verifying` returns `allGreen` on a task, or after any criterion reports `suspicious`. Not invoked by user prompts directly. Called exactly once per task per loop iteration.

## Process

Numbered steps the orchestrator follows:

1. Load the contract via `cli/lib/contract.js` and confirm it was the contract used for the task.
2. Read the worktree's captured diff at `<worktreePath>/anvil/diff.patch`.
3. Read the Verify result at `<worktreePath>/anvil/verify/verify-result.json`.
4. Build the briefing with `composeBriefing`. The module structurally refuses the commit message, the plan, the ledger, and any prior Court verdict. These are inputs the Court must not see.
5. Dispatch a fresh subagent as the Court. The Court returns a per-criterion status (pass | fail | suspicious) plus an action (merge | request-changes | request-clarification).
6. Validate the returned verdict with `validateVerdict`. Reject any out-of-schema action or per-criterion status with `E_INVALID_VERDICT`.
7. Return the verdict plus `briefingHash`. The orchestrator persists the verdict record via `<worktreePath>/anvil/verify/verify-result.json` alongside the Verify result; the Court verdict is NEVER carried back into the next task's briefing.

## Rationalizations

Reject the following shortcuts:

- "The commit message explains the rationale; let me include it." The Court does not read narration; rationale is an adversarial vector (failure-taxonomy row 2: Convincing rationale inflation).
- "The ledger has prior verdicts that would save time; pass them in." Prior verdicts are not evidence; they are context that can be pattern-matched rather than adjudicated (failure-taxonomy row 2).
- "Three criteria passed; surely the fourth is close enough." Three of four is a fail; the Court adjudicates all criteria, not a majority (failure-taxonomy row 8: Claim-without-evidence).

## Red Flags

If any of these conditions obtain, the Court dispatch is rejected:

- The caller tries to pass `commit_message`, `plan`, `ledger`, or `prior_verdicts` into `composeBriefing` (failure-taxonomy row 2).
- The returned verdict has an unknown action or an out-of-schema per-criterion status (structural guard; `E_INVALID_VERDICT`).
- The Court subagent references the task's commit history or prior verdicts (structural guard; the briefing does not expose these).

## Verification

Each Court dispatch checks:

1. `composeBriefing` rejects every key in `FORBIDDEN_COURT_INPUT_KEYS` with `E_COURT_INPUT_VIOLATION`.
2. `validateVerdict` rejects every out-of-schema verdict with `E_INVALID_VERDICT`.
3. The `judge` return value includes `briefingHash` matching sha256 of the briefing.
4. `MUTABLE_STATE` is frozen and empty both before and after the call.

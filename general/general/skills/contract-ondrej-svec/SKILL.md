---
name: contract-ondrej-svec
title: Contract (review / manage evidence contracts)
description: 'Review and manage evidence contracts in this repo. Subcommands: `show` (default, print the active contract), `list` (all contracts + which is active), `complete` (mark active contract completed), `abandon` (mark active contract abandoned). Triggers: contract, show contract, list contracts, mark contract complete, what''s active.'
author: ondrej-svec
author_url: https://github.com/ondrej-svec/heart-of-gold-toolkit/tree/main/plugins/quellis-architect/skills/contract
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Contract (review / manage evidence contracts)

A small, deliberate management surface for the per-task evidence contracts written by `/quellis-architect:plan` and consulted by the Stop hook. **Reads** by default; writes only on explicit subcommands. Authoring new contracts and editing claim shapes is `/quellis-architect:plan`'s job — this skill exists for lifecycle bookkeeping.

## Boundaries

**This skill MAY:** read `.quellis/contracts/` files, print contract content, flip `status` to `completed` or `abandoned` on explicit subcommand, delete `.quellis/contracts/active.toml` when the active contract closes.
**This skill MAY NOT:** edit claim shapes, add or remove `[[claim]]` blocks, rewrite the pointer to a different task without an `activate` subcommand (not in V1.1), edit code, run tests.

**To change what a contract claims, run `/quellis-architect:plan` again with the same brainstorm.** That rewrites the contract cleanly. Mid-flight claim edits drift from the substrate V1.2 personalization compounds.

## Common Rationalizations

| Shortcut | Why it fails | The cost |
|---|---|---|
| "Just edit claim_regex inline to make the gate pass" | The gate exists because the unrefined claim is dangerous. Tweaking the regex is laundering. | Silent regression on the next agent that inherits the lying contract. |
| "Mark abandoned to avoid the complete-prompt friction" | `abandoned` is for tasks dropped without finishing. Marking abandoned to skip evidence buries the trail. | Lost compounding signal for V1.2. |
| "Skip showing the contract — the user knows what's active" | Memory drifts across sessions. A 30-second show is cheap insurance against the user assuming a stale contract. | Stop fires on something the user didn't realize was still active. |

## Phase 0: Detect the subcommand

**Entry:** user invoked `/quellis-architect:contract [subcommand] [args]`.

Subcommands:

| Subcommand | Args | Action |
|---|---|---|
| `show` (default if no arg) | none | Print the active contract; if none, say so. |
| `list` | none | Print every contract in `.quellis/contracts/`, marking which is active and each one's `status`. |
| `complete` | none | Mark the active contract `status = "completed"`. Clear `active.toml`. Asks once to confirm. |
| `abandon` | none | Mark the active contract `status = "abandoned"`. Clear `active.toml`. Asks once to confirm. |

If the user passes anything else, list the valid subcommands and stop.

## Phase 1: Execute

### `show`

Read `.quellis/contracts/active.toml`. If absent → "No active contract." Stop.

Else read `.quellis/contracts/<task-id>.toml`. Print:

```
task_id:     <task-id>
task_title:  <task-title>
created_at:  <created-at>
status:      <status>
claims:

  <claim-id>
    regex:    <claim_regex>
    requires: <requires or "(none — always blocks)">
    reason:   <block_reason>

  <… one block per claim …>
```

If `task-title` or `created_at` are missing, omit them quietly.

### `list`

Glob `.quellis/contracts/*.toml`. For each file (excluding `active.toml`), read `task_id`, `task_title`, `status`. Read `active.toml` to find the active task_id.

Print one line per contract:

```
* <task-id>  <status>  <task-title>      ← active
  <task-id>  <status>  <task-title>
  <task-id>  <status>  <task-title>
```

The leading `*` and "← active" mark the current one. If no contracts exist, say so.

### `complete`

Read the active contract. If none → "No active contract to complete." Stop.

Ask the user once:

```
Mark contract <task-id> ("<task-title>") completed?
This flips status and clears the active pointer.

  y — proceed
  n — leave active (default if no answer)
```

On explicit `y`:

1. Edit `.quellis/contracts/<task-id>.toml`: change `status = "active"` to `status = "completed"`. If no `status` line exists, add one.
2. Delete `.quellis/contracts/active.toml`.
3. Confirm: `Contract <task-id> marked completed. Active pointer cleared.`

On `n` or anything ambiguous: leave the contract as-is.

### `abandon`

Same flow as `complete`, but the prompt says "abandoned" and the status becomes `abandoned`. Use this when the task is being dropped without shipping — the contract's claims never resolved, but they shouldn't keep gating future Stop events.

## Phase 2: Stop

This skill never auto-chains. After the requested subcommand runs, stop and return control. The user runs `/quellis-architect:plan` to write a new contract when they're ready.

## What makes this Quellis-shaped

- **Tight subcommand set.** Show, list, complete, abandon. Nothing else. Authoring lives in `/plan`.
- **No claim editing.** Mid-flight claim edits drift the substrate; rewrite via `/plan` instead.
- **Confirm before write.** Both `complete` and `abandon` need an explicit yes. The Stop hook is what the contract gates; the contract's status transitions matter.
- **Reads by default.** The most common case is "what's active?" — that should not require a subcommand keyword.

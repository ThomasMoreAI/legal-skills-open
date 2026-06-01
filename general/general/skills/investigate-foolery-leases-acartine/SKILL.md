---
name: investigate-foolery-leases-acartine
title: Investigate Foolery Leases
description: Investigate Foolery lease, session, and server logs when asked why an agent turn failed to advance, rolled back unexpectedly, hung, leaked a lease, or skipped lease usage. Use this for the dev server on port 3000, the installed runtime on port 3210, and recent 24-48 hour forensic reviews across both log roots.
author: acartine
author_url: https://github.com/acartine/foolery/tree/main/.claude/skills/investigate-foolery-leases
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Investigate Foolery Leases

Use this skill to trace Foolery runtime behavior across lease lifecycle logs,
interaction/session logs, and server logs.

## When To Use It

- The user asks whether a step type uses leases.
- The user wants recent examples from the last 24-48 hours.
- The user asks which agent ended a turn without calling `next` or `rollback`.
- The user suspects a hung turn, dangling lease, or runtime mismatch between
  port `3000` and port `3210`.
- The user wants likely causes, not just raw log lines.

## Log Roots

- Dev runtime (`bun dev`, usually port `3000`):
  [`.foolery-logs`](/Users/cartine/foolery/.foolery-logs)
- Installed runtime (`next start`, usually port `3210`):
  [`~/.config/foolery/logs`](/Users/cartine/.config/foolery/logs)

Use `lsof -nP -iTCP:3000 -sTCP:LISTEN` and
`lsof -nP -iTCP:3210 -sTCP:LISTEN` only to confirm which process is live. The
authoritative evidence is in the log roots.

## Workflow

1. Confirm the target repo slug and time window.
2. Read `_leases/*/leases.jsonl*` for lease lifecycle events.
3. Read per-session `*.jsonl*` interaction logs for `session_start`,
   `beat_state`, `response`, and `session_end`.
4. If needed, read `_server/*/console.log` and `server.jsonl*` for child close,
   post-close beat state, retry, and invariant handling.
5. Correlate by `sessionId`, `beatId`, `knotsLeaseId`, and timestamps.
6. Produce findings with concrete examples and likely causes.

## Core Checks

### 1. Lease Coverage

- Find which interaction types and steps emit `lease_create_*`,
  `lease_claim_binding_check`, `prompt_delivered`, and
  `lease_terminate_*`.
- Do not assume every step or interaction uses leases. Verify by code and logs.

### 2. Hung Or Open Turns

Flag sessions with:

- `prompt_delivered` but no matching `lease_terminate_succeeded`
- no `session_end`
- continued `response` traffic after the last lease event

### 3. Completed Turns Without Progress

For each completed session with `exitCode: 0`:

- compare `beat_state.phase == "before_prompt"` with the matching
  `after_prompt`
- resolve the claimed step
- verify the post-exit state moved to the expected next queue state or a prior
  queue state

If the beat stays in the active/review step, treat that as a failed workflow
outcome even if the process exited `0` and the lease terminated cleanly.

### 4. Dangling Or Failed Lease Cleanup

Flag:

- `lease_terminate_failed`
- `prompt_delivered` leases with no matching termination
- server-side invariant/dangling-lease warnings

### 5. Likely Cause Extraction

Read the final `agentMessage` and relevant stdout/stderr near the suspicious
window. Distinguish:

- the agent analyzed but never ran the completion command
- the agent hung and never exited
- the agent exited cleanly but left the beat in an action state
- Foolery retried or rotated agents after a non-zero exit

## Reporting

Report findings in this order:

1. The concrete anomaly
2. Exact session, beat, step, agent, and time
3. Whether the lease lifecycle itself was clean or broken
4. The post-exit beat state
5. The most likely explanation, labeled as inference when needed

Keep examples short but specific. Include absolute log paths in the report.

## References

- For event shapes, file locations, and proven heuristics, read
  [`references/log-forensics.md`](references/log-forensics.md).

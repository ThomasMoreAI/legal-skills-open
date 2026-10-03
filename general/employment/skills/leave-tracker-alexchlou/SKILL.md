---
name: leave-tracker-alexchlou
title: $employment-legal:leave-tracker
description: Check open leaves for deadline alerts and required decisions. Surfaces only the leaves that require an action and explains why — not a status board. Use weekly, or whenever the attorney needs to know which leaves have upcoming designation, certification, or exhaustion deadlines.
author: alexchlou
author_url: https://github.com/alexchlou/codex-for-legal/tree/main/plugins/employment-legal/skills/leave-tracker
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: employment
language: en
---

> Codex v1 local-input note: This migrated skill supports local files and pasted text by default. References to Drive, CLM IDs, Slack, Westlaw, iManage, Ironclad, eDiscovery, dockets, or other remote systems require a separately configured Codex connector/MCP server. When a connector is unavailable, ask for a local export, local file path, or pasted excerpts. If `config/local/codex-for-legal/<practice>/CLAUDE.md` is missing, ask the user to run the relevant `cold-start-interview` or `customize` skill and copy from `config/templates/codex-for-legal/<practice>/CLAUDE.md`.


# $employment-legal:leave-tracker

Checks all open leaves with hard legal deadlines and surfaces only the ones
requiring a decision or action. Not a status board — tells you what you need
to do and why.

## Instructions

1. Load the `leave-tracker` agent and run the full workflow.

2. If no HRIS is connected and no `config/local/codex-for-legal/employment-legal/leave-register.yaml` exists, prompt
   the attorney to upload a leave spreadsheet or use
   `$employment-legal:log-leave` to add entries.

3. Alerts only for leaves requiring action. Clean leaves summarized one line each.

## Examples

```
$employment-legal:leave-tracker
```

Run this weekly — set a Monday-morning reminder to invoke
`$employment-legal:leave-tracker`. Automated scheduling requires a separate
integration (calendar reminder, cron job, etc.); Codex agents do not
self-schedule.

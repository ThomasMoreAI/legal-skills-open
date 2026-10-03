---
name: review-proposals-alexchlou
title: $commercial-legal:review-proposals
description: Review and approve (or reject) pending playbook update proposals from the playbook-monitor agent and apply approved changes to the practice profile. Use when the playbook-monitor agent has surfaced proposals, when the user says "review playbook proposals", "what playbook updates are pending", or wants to step through deviation-driven playbook changes.
author: alexchlou
author_url: https://github.com/alexchlou/codex-for-legal/tree/main/plugins/commercial-legal/skills/review-proposals
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: commercial
language: en
---

> Codex v1 local-input note: This migrated skill supports local files and pasted text by default. References to Drive, CLM IDs, Slack, Westlaw, iManage, Ironclad, eDiscovery, dockets, or other remote systems require a separately configured Codex connector/MCP server. When a connector is unavailable, ask for a local export, local file path, or pasted excerpts. If `config/local/codex-for-legal/<practice>/CLAUDE.md` is missing, ask the user to run the relevant `cold-start-interview` or `customize` skill and copy from `config/templates/codex-for-legal/<practice>/CLAUDE.md`.


# $commercial-legal:review-proposals

Steps through pending playbook update proposals from the monitor agent and applies approved changes to `config/local/codex-for-legal/commercial-legal/CLAUDE.md`.

## Instructions

1. **Load the playbook-monitor agent** and run Step 5 (review and approval flow).

2. **If no proposals file exists** or it is empty: respond *"No pending proposals. Playbook is up to date."* Do not proceed further.

3. **Present proposals one at a time.** For each, show the full proposal block and offer four options: Accept, Reject, Edit, Defer.

4. **For Accept or Edit:** show the exact diff to `config/local/codex-for-legal/commercial-legal/CLAUDE.md` before writing. Only apply after the attorney explicitly confirms.

5. **For Reject or Defer:** log the decision. Do not modify `config/local/codex-for-legal/commercial-legal/CLAUDE.md`.

6. **After all proposals are resolved:** show a summary of what changed, then archive the proposals file.

## Examples

```
$commercial-legal:review-proposals
```

```
$commercial-legal:review-proposals
(runs automatically after playbook-monitor notifies you)
```

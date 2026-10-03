---
name: investigation-summary-alexchlou
title: $employment-legal:investigation-summary
description: Draft an audience-specific summary from the privileged investigation memo — HR, leadership, or outside counsel versions. Use when an investigation memo needs to be communicated to an audience that should not see the full privileged work product.
author: alexchlou
author_url: https://github.com/alexchlou/codex-for-legal/tree/main/plugins/employment-legal/skills/investigation-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: employment
language: en
---

> Codex v1 local-input note: This migrated skill supports local files and pasted text by default. References to Drive, CLM IDs, Slack, Westlaw, iManage, Ironclad, eDiscovery, dockets, or other remote systems require a separately configured Codex connector/MCP server. When a connector is unavailable, ask for a local export, local file path, or pasted excerpts. If `config/local/codex-for-legal/<practice>/CLAUDE.md` is missing, ask the user to run the relevant `cold-start-interview` or `customize` skill and copy from `config/templates/codex-for-legal/<practice>/CLAUDE.md`.


# $employment-legal:investigation-summary

Drafts a stripped-down, audience-appropriate summary from the privileged
investigation memo. HR summaries contain no privilege analysis. Leadership
summaries are high-level. Outside counsel briefings include full context.

## Instructions

1. Load the `internal-investigation` reference skill and run Mode 5 (Audience summary).
2. If no memo exists yet, offer to draft the memo first.
3. HR summaries must not include attorney mental impressions, credibility
   methodology, or legal exposure analysis.

## Examples

```
$employment-legal:investigation-summary [matter name] hr
```

```
$employment-legal:investigation-summary [matter name] leadership
```

```
$employment-legal:investigation-summary [matter name] outside-counsel
```

> Detailed audience-stripping rules and summary templates live in the
> `internal-investigation` reference skill — load it before doing substantive
> work.

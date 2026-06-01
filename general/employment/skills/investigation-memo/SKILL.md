---
name: investigation-memo
title: $employment-legal:investigation-memo
description: Draft or update the privileged investigation memo from the investigation log. Use when an investigation is far enough along to write the first memo cut, or when new data has been added and the existing draft needs updating.
author: alexchlou
author_url: https://github.com/alexchlou/codex-for-legal/tree/main/plugins/employment-legal/skills/investigation-memo
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: employment
language: en
---

> Codex v1 local-input note: This migrated skill supports local files and pasted text by default. References to Drive, CLM IDs, Slack, Westlaw, iManage, Ironclad, eDiscovery, dockets, or other remote systems require a separately configured Codex connector/MCP server. When a connector is unavailable, ask for a local export, local file path, or pasted excerpts. If `config/local/codex-for-legal/<practice>/CLAUDE.md` is missing, ask the user to run the relevant `cold-start-interview` or `customize` skill and copy from `config/templates/codex-for-legal/<practice>/CLAUDE.md`.


# $employment-legal:investigation-memo

Drafts the first cut of the privileged investigation memo from the log,
or updates an existing draft when new data has been added.

## Instructions

1. Load the `internal-investigation` reference skill and run Mode 4 (Draft or update memo).
2. If drafting for the first time, warn if high-priority sources are still
   open on the checklist.
3. If updating, show what changed before rewriting.
4. All output is marked PRIVILEGED AND CONFIDENTIAL — ATTORNEY WORK PRODUCT.

## Examples

```
$employment-legal:investigation-memo [matter name]
```

```
$employment-legal:investigation-memo [matter name]
(updates existing memo if one exists)
```

> Detailed memo structure, credibility-assessment framework, and update rules
> live in the `internal-investigation` reference skill — load it before doing
> substantive work.

---
name: investigation-add
title: $employment-legal:investigation-add
description: Add data to an open investigation — documents, interview notes, or observations. Processes batches against the documented pull criteria, surfaces significant items, and logs everything reviewed for coverage verification. Use when new evidence, interview notes, or document productions come in for an open investigation.
author: alexchlou
author_url: https://github.com/alexchlou/codex-for-legal/tree/main/plugins/employment-legal/skills/investigation-add
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: employment
language: en
---

> Codex v1 local-input note: This migrated skill supports local files and pasted text by default. References to Drive, CLM IDs, Slack, Westlaw, iManage, Ironclad, eDiscovery, dockets, or other remote systems require a separately configured Codex connector/MCP server. When a connector is unavailable, ask for a local export, local file path, or pasted excerpts. If `config/local/codex-for-legal/<practice>/CLAUDE.md` is missing, ask the user to run the relevant `cold-start-interview` or `customize` skill and copy from `config/templates/codex-for-legal/<practice>/CLAUDE.md`.


# $employment-legal:investigation-add

Adds data to an open investigation log. Processes document batches using
documented pull criteria, surfaces significant items, logs everything
reviewed for coverage verification.

## Instructions

1. Load `config/local/codex-for-legal/employment-legal/CLAUDE.md`.
2. Load the `internal-investigation` reference skill and run Mode 2 (Add data).
3. After processing, show the surface ratio and list of surfaced items.
4. Prompt to update the sources checklist if the data covers a checklist item.

## Examples

```
$employment-legal:investigation-add [matter name]
[paste interview notes]
```

```
$employment-legal:investigation-add [matter name]
[attach email export]
```

> Detailed needle-finding process, log entry format, surface-ratio rules, and
> sources-checklist tracking live in the `internal-investigation` reference
> skill — load it before doing substantive work.

---
name: investigation-query
title: $employment-legal:investigation-query
description: Ask questions against an open investigation log — what witnesses said, where accounts conflict, what gaps exist, what the strongest evidence is on each issue. Use when the attorney needs to query the investigation record without re-reading every entry.
author: alexchlou
author_url: https://github.com/alexchlou/codex-for-legal/tree/main/plugins/employment-legal/skills/investigation-query
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: employment
language: en
---

> Codex v1 local-input note: This migrated skill supports local files and pasted text by default. References to Drive, CLM IDs, Slack, Westlaw, iManage, Ironclad, eDiscovery, dockets, or other remote systems require a separately configured Codex connector/MCP server. When a connector is unavailable, ask for a local export, local file path, or pasted excerpts. If `config/local/codex-for-legal/<practice>/CLAUDE.md` is missing, ask the user to run the relevant `cold-start-interview` or `customize` skill and copy from `config/templates/codex-for-legal/<practice>/CLAUDE.md`.


# $employment-legal:investigation-query

Answers questions against the investigation log — what witnesses said,
where accounts conflict, what gaps exist, what the strongest evidence is
on each issue.

## Instructions

1. Load the `internal-investigation` reference skill and run Mode 3 (Query).
2. Always cite log entry IDs in the answer.
3. If the log contains nothing relevant to the question, say so explicitly —
   "I have not seen any information on [topic] in this investigation log
   ([N] entries reviewed)" — and offer to flag it as a gap.

## Examples

```
$employment-legal:investigation-query [matter name]
What did the respondent say about the December team dinner?
```

```
$employment-legal:investigation-query [matter name]
Where do the complainant's and respondent's accounts conflict?
```

```
$employment-legal:investigation-query [matter name]
What do we still need?
```

> Detailed log-query process, citation rules, and gap-flagging templates live
> in the `internal-investigation` reference skill — load it before doing
> substantive work.

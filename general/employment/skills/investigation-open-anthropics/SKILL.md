---
name: investigation-open-anthropics
title: /investigation-open
description: Open a new internal investigation matter — runs intake, generates the sources checklist, and creates the persistent investigation log. Use when a complaint or allegation comes in and the attorney needs to stand up a privileged investigation workspace.
author: anthropics
author_url: https://github.com/anthropics/claude-for-legal/tree/main/employment-legal/skills/investigation-open
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: employment
language: en
---

# /investigation-open

Opens a new investigation matter — runs intake, generates the sources
checklist, and creates the persistent investigation log.

## Instructions

1. Load `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md`.
2. Load the `internal-investigation` reference skill and run Mode 1 (Open).
3. If a matter with the same slug already exists, warn before overwriting.

## Examples

```
/employment-legal:investigation-open
Harassment complaint filed against a manager in the Austin office.
```

```
/employment-legal:investigation-open
(skill will ask for details)
```

> Detailed intake, privilege-formation requirements, sources checklist, and log
> templates live in the `internal-investigation` reference skill — load it
> before doing substantive work.

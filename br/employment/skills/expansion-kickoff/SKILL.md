---
name: expansion-kickoff
title: /expansion-kickoff
description: Kick off international expansion planning for a new country — gathers intake, runs EOR vs. entity framing, drafts cross-functional questions, surfaces country-specific flags, and creates a persistent tracker. Use when someone says "we're hiring in [country]", "expansion to [country]", or "first hire in [country]".
author: Bossmann007
author_url: https://github.com/Bossmann007/claude-legal-br/tree/main/employment-legal/skills/expansion-kickoff
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: employment
language: en
---

# /expansion-kickoff

Starts an international expansion project for a new country — gathers intake,
runs EOR vs. entity framing, drafts cross-functional questions, surfaces
country-specific flags, and creates a persistent tracker.

## Instructions

1. Load `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` → jurisdictional footprint, escalation table.
2. Load the `international-expansion` reference skill and run the full workflow.
3. If a tracker file already exists for this country (`~/.claude/plugins/config/claude-for-legal/employment-legal/expansion-[slug].yaml`),
   flag it: "An expansion tracker for [country] already exists. Use
   `/employment-legal:expansion-update [country]` to update it, or confirm
   you want to start over."
4. Create `~/.claude/plugins/config/claude-for-legal/employment-legal/expansion-[slug].yaml` on completion.

## Examples

```
/employment-legal:expansion-kickoff Germany
```

```
/employment-legal:expansion-kickoff
(skill will ask which country)
```

> Detailed EOR vs. entity framework, cross-functional questions, briefing
> templates, and tracker schema live in the `international-expansion`
> reference skill — load it before doing substantive work.

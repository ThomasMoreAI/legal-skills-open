---
name: investigation-summary-bossmann007
title: 'Investigation summary'
description: Draft an audience-specific summary from the privileged investigation memo — HR, leadership, or outside counsel versions. Use when an investigation memo needs to be communicated to an audience that should not see the full privileged work product.
author: Bossmann007
author_url: https://github.com/Bossmann007/claude-legal-br/tree/main/employment-legal/skills/investigation-summary
license: Apache-2.0
version: 0.1.1
execution_mode: open
jurisdiction: us
practice: employment
language: en
---

# /investigation-summary

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
/employment-legal:investigation-summary [matter name] hr
```

```
/employment-legal:investigation-summary [matter name] leadership
```

```
/employment-legal:investigation-summary [matter name] outside-counsel
```

> Detailed audience-stripping rules and summary templates live in the
> `internal-investigation` reference skill — load it before doing substantive
> work.

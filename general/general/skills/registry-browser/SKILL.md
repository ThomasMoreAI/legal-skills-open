---
name: registry-browser
title: $legal-builder-hub:registry-browser
description: Search watched registries for community legal skills, showing matches with descriptions and offering to show the full SKILL.md before install. Use when the user says "browse", "search skills", "find a skill for", "what's out there for", or wants to add a new registry to the watchlist.
author: alexchlou
author_url: https://github.com/alexchlou/codex-for-legal/tree/main/plugins/legal-builder-hub/skills/registry-browser
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

> Codex v1 local-input note: This migrated skill supports local files and pasted text by default. References to Drive, CLM IDs, Slack, Westlaw, iManage, Ironclad, eDiscovery, dockets, or other remote systems require a separately configured Codex connector/MCP server. When a connector is unavailable, ask for a local export, local file path, or pasted excerpts. If `config/local/codex-for-legal/<practice>/CLAUDE.md` is missing, ask the user to run the relevant `cold-start-interview` or `customize` skill and copy from `config/templates/codex-for-legal/<practice>/CLAUDE.md`.


# $legal-builder-hub:registry-browser

1. Load `config/local/codex-for-legal/legal-builder-hub/CLAUDE.md` → watched registries.
2. Use the workflow below.
3. Search each registry. Show matches with descriptions.
4. Offer to show full SKILL.md for any match.

---

## Purpose

Find skills across the watched registries. Search, preview, decide.

## Load context

`config/local/codex-for-legal/legal-builder-hub/CLAUDE.md` → watched registries list.

## Workflow

### Step 1: Fetch registry indexes

For each watched registry:

- GitHub repos: fetch `skills/` directory listing and each `SKILL.md` frontmatter (name + description).
- Marketplace-style registries: fetch the index.

Cache the index locally (`references/registry-cache.json`) so browsing is fast. Refresh cache if >7 days old or on request.

### Step 2: Search

Match query against skill names and descriptions. Simple keyword match is fine — these are small enough that fuzzy search is overkill.

Also: browse by category if the registry organizes skills that way.

### Step 3: Present matches

```markdown
## Search: "[query]"

**Found [N] skills across [M] registries:**

### [skill-name]
**From:** [registry name]
**Description:** [from frontmatter]
[View full SKILL.md] [Install]

### [skill-name]
[...]
```

### Step 4: Preview

On "view full SKILL.md": fetch and show the whole file. User reads it before deciding to install. No surprises.

### Step 5: Add a registry

If the user has a URL to a registry not in the watchlist:

1. Fetch it, validate it's a skills repo (has `skills/` or `.codex-plugin/`)
2. Show what's in it
3. Add to `config/local/codex-for-legal/legal-builder-hub/CLAUDE.md` → watched registries on confirmation

## Default registries

- **lpm-skills** — 14 legal project management skills. Practice-agnostic. Good starting point.
- Space for others to be added as the ecosystem grows.

## What this skill does not do

- Install anything. It browses. skill-installer installs.
- Rate or review skills. It shows you the SKILL.md; you judge.
- Search the whole internet. Only watched registries.

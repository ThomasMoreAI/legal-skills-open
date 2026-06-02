---
name: customize-2
title: $legal-builder-hub:customize
description: Guided customization of your Legal Builder Hub profile — change one thing without re-running the whole cold-start interview. Adjust practice profile, installed starter pack, watched registries, update preferences, or QA strictness. Use when the user says "change my [thing]", "add a registry", "update my profile", "edit my config", or "customize".
author: alexchlou
author_url: https://github.com/alexchlou/codex-for-legal/tree/main/plugins/legal-builder-hub/skills/customize
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

> Codex v1 local-input note: This migrated skill supports local files and pasted text by default. References to Drive, CLM IDs, Slack, Westlaw, iManage, Ironclad, eDiscovery, dockets, or other remote systems require a separately configured Codex connector/MCP server. When a connector is unavailable, ask for a local export, local file path, or pasted excerpts. If `config/local/codex-for-legal/<practice>/CLAUDE.md` is missing, ask the user to run the relevant `cold-start-interview` or `customize` skill and copy from `config/templates/codex-for-legal/<practice>/CLAUDE.md`.


# $legal-builder-hub:customize

## When this runs

The user typed `$legal-builder-hub:customize`. They want to change something
in their Builder Hub profile — a watched registry, update notification
preferences, a practice area for recommendations — without re-running the
whole cold-start interview and without hand-editing YAML.

## What to do

1. **Read the config.** Read
   `config/local/codex-for-legal/legal-builder-hub/CLAUDE.md`
   (and `config/local/codex-for-legal/company-profile.md` one
   level up). If the plugin config does not exist or still contains
   `[PLACEHOLDER]` values, say:

   > You haven't run setup yet. Run `$legal-builder-hub:cold-start-interview`
   > first — customize is for adjusting a profile you already have.

2. **Show the customizable map.** List what's in the profile, grouped, with a
   one-line summary of the current value:

   - **Company / who you are** — name, industry, jurisdictions, stage, practice
     setting *(shared across all 12 plugins — changes flow through
     `company-profile.md`)*
   - **Your practice profile** — practice areas in scope, used to recommend
     community skills
   - **Installed starter pack** — which plugins and skills are installed via
     the hub, with install source
   - **Watched registries** — GitHub repositories / URLs the hub pulls
     community skills from
   - **Update preferences** — check cadence (daily / weekly / on demand),
     notification channel (Slack (connector optional; not enabled in v1) / in-session), auto-update vs. prompt
   - **QA strictness** — how aggressively `/qa` flags issues on a candidate
     skill before install (lenient / middle / strict), and which
     failure-mode checks are on
   - **Skill install defaults** — install scope (user / project), whether
     to run `/qa` automatically before install
   - **Integrations** — Slack (connector optional; not enabled in v1) / document storage status, fallbacks

3. **Ask what they want to change.**

   > What would you like to adjust? Pick a section, or describe the change in
   > your own words.

4. **Make the change.** Show the current value, ask for the new value, explain
   what changes downstream, confirm, write it to the config.

   Examples:
   - *Adding a new watched registry:* "`/browse` will search this registry
     alongside the existing ones. `/update` will check it on its next run."
   - *QA strictness strict → middle:* "`/qa` will report the same findings
     but not block install on the medium band unless you confirm."
   - *Auto-update on → off:* "The hub will prompt you before applying
     updates instead of applying them automatically."

5. **For shared-profile changes** (company name, industry, jurisdictions,
   practice setting, stage): write to
   `config/local/codex-for-legal/company-profile.md` and note:

   > This change affects all 12 plugins — any plugin that reads your
   > jurisdiction footprint now sees [new value].

6. **Close.**

   > Done. Your next output will reflect the change. Anything else? You can
   > run `$legal-builder-hub:customize` anytime.

## Guardrails

- **Never delete a section.** If the user wants to "remove" a watched
  registry, offer to mark it `[Paused]` and explain that pausing keeps the
  install history but stops update checks.
- **Flag internal inconsistency.** If the change would make the profile
  inconsistent (e.g., auto-update on + QA strictness off; or practice
  profile that doesn't match any installed plugin), flag the tension.
- **Flag guardrail degradation.** The Legal Skill Design Framework checks
  (nine design parameters, three legal failure modes, trust-surface check)
  are what `/qa` exists to run — turning them off defeats the point. If the
  user wants to lower strictness, recommend the middle band rather than
  disabling the check.
- **One change at a time.** Don't re-ask the whole interview.

---
name: customize-4
title: $regulatory-legal:customize
description: Guided customization of your regulatory practice profile — change one thing without re-running the whole cold-start interview. Adjust watched regulators, policy library index, materiality threshold, gap response process, feed configuration, or matter workspace paths. Use when the user says "change my [thing]", "add a regulator", "update my watchlist", "edit my threshold", or "customize".
author: alexchlou
author_url: https://github.com/alexchlou/codex-for-legal/tree/main/plugins/regulatory-legal/skills/customize
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: regulatory
language: en
---

> Codex v1 local-input note: This migrated skill supports local files and pasted text by default. References to Drive, CLM IDs, Slack, Westlaw, iManage, Ironclad, eDiscovery, dockets, or other remote systems require a separately configured Codex connector/MCP server. When a connector is unavailable, ask for a local export, local file path, or pasted excerpts. If `config/local/codex-for-legal/<practice>/CLAUDE.md` is missing, ask the user to run the relevant `cold-start-interview` or `customize` skill and copy from `config/templates/codex-for-legal/<practice>/CLAUDE.md`.


# $regulatory-legal:customize

## When this runs

The user typed `$regulatory-legal:customize`. They want to change something
in their regulatory profile — a watched regulator, a materiality threshold,
a feed source — without re-running the whole cold-start interview and
without hand-editing YAML.

## What to do

1. **Read the config.** Read
   `config/local/codex-for-legal/regulatory-legal/CLAUDE.md`
   (and `config/local/codex-for-legal/company-profile.md` one
   level up). If the plugin config does not exist or still contains
   `[PLACEHOLDER]` values, say:

   > You haven't run setup yet. Run `$regulatory-legal:cold-start-interview`
   > first — customize is for adjusting a profile you already have.

2. **Show the customizable map.** List what's in the profile, grouped, with a
   one-line summary of the current value:

   - **Company / who you are** — name, industry, jurisdictions, stage, practice
     setting *(shared across all 12 plugins — changes flow through
     `company-profile.md`)*
   - **Regulators we watch** — agencies / bodies / SROs / state regulators
     in scope, and which are "leading" (most likely to drive policy
     impact) vs. "monitor"
   - **Policy library** — the internal policies the library indexes, path
     to each, owner per policy
   - **Materiality threshold** — when a regulatory change rises to
     "notable" vs. "report" vs. "digest only"; how this threshold filters
     `/watch` output
   - **Gap response process** — who triages, SLA per severity, downstream
     owners (policy, product, training)
   - **Feed configuration** — regulator feeds, Thomson Reuters
     connectors, cadence of the `/watch` sweep, digest channel
   - **People** — regulatory counsel, policy owners, comment drafter,
     escalation chain
   - **Workflow** — matter workspaces, open gaps tracker, comment deadline
     tracker, digest publication cadence
   - **Integrations** — Thomson Reuters / Slack (connector optional; not enabled in v1) / document
     storage status, fallbacks

3. **Ask what they want to change.**

   > What would you like to adjust? Pick a section, or describe the change in
   > your own words.

4. **Make the change.** Show the current value, ask for the new value, explain
   what changes downstream, confirm, write it to the config.

   Examples:
   - *Adding a regulator to the watchlist:* "`/watch` will sweep this
     regulator on its next run. `/diff` will accept inputs from this
     regulator's rulemaking feed."
   - *Tightening materiality threshold:* "`/watch` digest will be
     shorter — items below the new threshold will drop from the weekly
     digest but stay searchable."
   - *New policy added to the library:* "`/diff` will include this policy
     when matching new rules against the library. The comment tracker
     will tag comments affecting this policy."

5. **For shared-profile changes** (company name, industry, jurisdictions,
   practice setting, stage): write to
   `config/local/codex-for-legal/company-profile.md` and note:

   > This change affects all 12 plugins — any plugin that reads your
   > jurisdiction footprint now sees [new value].

6. **Close.**

   > Done. Your next output will reflect the change. Anything else? You can
   > run `$regulatory-legal:customize` anytime.

## Guardrails

- **Never delete a section.** If the user wants to "drop" a regulator,
  offer to mark it `[Monitor only]` and explain that monitoring keeps the
  feed in the archive but pulls it out of the active digest.
- **Flag internal inconsistency.** If the change would make the profile
  inconsistent (e.g., regulator in scope + no jurisdiction in the footprint
  that the regulator covers; or "weekly digest" + materiality threshold
  that yields fewer than one item a quarter), flag the tension.
- **Flag guardrail degradation.** `[verify]` tags on cited regulations,
  source attribution on feed pulls, and the `[review]` flag on gap triage
  are load-bearing — do not remove. Materiality threshold can be adjusted,
  but lowering it below the point where the digest becomes noise is the
  point — warn if that's the direction.
- **One change at a time.** Don't re-ask the whole interview.

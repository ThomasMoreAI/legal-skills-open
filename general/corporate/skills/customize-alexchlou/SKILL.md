---
name: customize-alexchlou
title: $corporate-legal:customize
description: Guided customization of your corporate practice profile — change one thing without re-running the whole cold-start interview. Adjust risk posture, escalation contacts, active modules (M&A / Board / Public Company / Entity Management), materiality thresholds, disclosure schedule format, consent precedents, or matter workspace paths. Use when the user says "change my [thing]", "update my profile", "edit my config", or "customize".
author: alexchlou
author_url: https://github.com/alexchlou/codex-for-legal/tree/main/plugins/corporate-legal/skills/customize
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: corporate
language: en
---

> Codex v1 local-input note: This migrated skill supports local files and pasted text by default. References to Drive, CLM IDs, Slack, Westlaw, iManage, Ironclad, eDiscovery, dockets, or other remote systems require a separately configured Codex connector/MCP server. When a connector is unavailable, ask for a local export, local file path, or pasted excerpts. If `config/local/codex-for-legal/<practice>/CLAUDE.md` is missing, ask the user to run the relevant `cold-start-interview` or `customize` skill and copy from `config/templates/codex-for-legal/<practice>/CLAUDE.md`.


# $corporate-legal:customize

## When this runs

The user typed `$corporate-legal:customize`. They want to change something
in their practice profile — a risk posture, an escalation contact, a module
toggle, an output format — without re-running the whole cold-start interview
and without hand-editing YAML.

## What to do

1. **Read the config.** Read
   `config/local/codex-for-legal/corporate-legal/CLAUDE.md`
   (and `config/local/codex-for-legal/company-profile.md` one
   level up). If the plugin config does not exist or still contains
   `[PLACEHOLDER]` values, say:

   > You haven't run setup yet. Run `$corporate-legal:cold-start-interview`
   > first — customize is for adjusting a profile you already have.

2. **Show the customizable map.** List what's in the profile, grouped, with a
   one-line summary of the current value:

   - **Company / who you are** — name, industry, jurisdictions, stage, public
     vs. private, practice setting *(shared across all 12 plugins — changes
     flow through `company-profile.md`)*
   - **Active modules** — which of M&A, Board & Secretary, Public Company,
     Entity Management are on. Turning a module on/off changes which skills
     prompt for setup.
   - **Risk posture** — conservative / middle / aggressive, what each means
     for diligence materiality and disclosure schedule scope
   - **People** — deal team, board secretary, entity management owner,
     escalation chain
   - **M&A module** — materiality thresholds (contract value, headcount,
     revenue), data room platforms trusted, AI bulk-review trust level
     (Luminance / Kira), deal-team briefing cadence
   - **Board & Secretary module** — house consent format, signatory
     preferences, committee structure
   - **Public Company module** — reporting calendar, disclosure controls,
     10-K/10-Q review timing
   - **Entity Management module** — entity table, registered agent, filing
     jurisdictions, annual report calendar
   - **Workflow** — matter workspaces (deal rooms), closing checklist
     location, VDR watcher cadence
   - **Integrations** — Box / Intralinks / Datasite / CT Corp / Slack (connector optional; not enabled in v1) status,
     fallbacks

3. **Ask what they want to change.**

   > What would you like to adjust? Pick a section, or describe the change in
   > your own words.

4. **Make the change.** Show the current value, ask for the new value, explain
   what changes downstream, confirm, write it to the config.

   Examples:
   - *Materiality threshold $250K → $500K:* "`$corporate-legal:diligence-issue-extraction`
     and `$corporate-legal:material-contract-schedule` will now treat $500K as the cutoff.
     Existing findings stay as logged; re-run if you want the new threshold
     applied retroactively."
   - *Turning on the Public Company module:* "I'll prompt you for reporting
     calendar and disclosure controls next time you run anything in that
     area."
   - *AI bulk-review trust "check every row" → "spot-check 10%":* "`/ai-tool-
     handoff` will QA a 10% sample rather than every extraction."

5. **For shared-profile changes** (company name, industry, jurisdictions,
   practice setting, stage): write to
   `config/local/codex-for-legal/company-profile.md` and note:

   > This change affects all 12 plugins — any plugin that reads your
   > jurisdiction footprint now sees [new value].

6. **Close.**

   > Done. Your next output will reflect the change. Anything else? You can
   > run `$corporate-legal:customize` anytime.

## Guardrails

- **Never delete a section.** If the user wants to "remove" something, set it
  to `[Not configured]` and explain what that means for the plugin's behavior.
- **Flag internal inconsistency.** If the change would make the profile
  inconsistent (e.g., Public Company module off + "SEC counsel" in
  escalation; or aggressive risk posture + $25K materiality threshold), flag
  the tension.
- **Flag guardrail degradation.** The `[review]` flag, source attribution
  tags on retrieved documents, and `[verify]` tags on cited authorities are
  load-bearing — explain the trade-off before removing.
- **One change at a time.** Don't re-ask the whole interview.

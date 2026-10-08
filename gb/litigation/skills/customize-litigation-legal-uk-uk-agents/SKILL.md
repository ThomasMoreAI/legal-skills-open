---
name: customize-litigation-legal-uk-uk-agents
title: /customize
description: Guided customisation of your litigation practice profile — change one thing without re-running the whole cold-start interview. Adjust practice role, side (claimant / defendant / mixed), risk calibration, landscape, house style, escalation contacts, severity vocabulary, or matter workspace paths. Use when the user says "change my [thing]", "update my profile", "edit my config", or "customise".
author: uk-agents
author_url: https://github.com/uk-agents/uk-legal-plugins/tree/main/litigation-legal-uk/skills/customize
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: gb
practice: litigation
language: en
---

# /customize

## When this runs

The user typed `/litigation-legal-uk:customize`. They want to change something
in their litigation profile — a risk calibration, a house style rule, an
escalation contact, a landscape note — without re-running the whole
cold-start interview and without hand-editing YAML.

## What to do

1. **Read the config.** Read
   `~/.claude/plugins/config/uk-legal-plugins/litigation-legal-uk/CLAUDE.md`
   (and `~/.claude/plugins/config/uk-legal-plugins/company-profile.md` one
   level up). If the plugin config does not exist or still contains
   `[PLACEHOLDER]` values, say:

   > You haven't run setup yet. Run `/litigation-legal-uk:cold-start-interview`
   > first — customize is for adjusting a profile you already have.

2. **Show the customisable map.** List what's in the profile, grouped, with a
   one-line summary of the current value:

   - **Company / who you are** — name, industry, jurisdictions, stage, practice
     setting *(shared across all plugins — changes flow through
     `company-profile.md`)*
   - **Practice role** — in-house / firm-solicitor / barrister / solo / other
   - **Side** — claimant / defendant / mixed, and any posture nuances (class
     action defence, regulatory enforcement defence, commercial
     claimant, etc.)
   - **Risk calibration** — what counts as high / medium / low risk on an
     inbound demand, witness summons, or new matter; escalation triggers
   - **Landscape** — regular adversaries, frequent fora (courts and
     tribunals), standing external solicitors and counsel relationships
   - **House style** — skeleton argument style, witness statement conventions,
     Letter of Claim template, preservation notice template, legal
     professional privilege conventions
   - **Severity vocabulary map** — how you translate severity labels across
     client / internal / court-facing outputs
   - **People** — matter leads, in-house team, external solicitors bench,
     instructed counsel, escalation chain
   - **Workflow** — matter workspaces, portfolio log, OC status cadence,
     preservation notice refresh cadence
   - **Integrations** — document storage / e-filing / calendar / DMS status,
     fallbacks

3. **Ask what they want to change.**

   > What would you like to adjust? Pick a section, or describe the change in
   > your own words.

4. **Make the change.** Show the current value, ask for the new value, explain
   what changes downstream, confirm, write it to the config.

   Examples:
   - *Side mixed → defendant-only:* "`/matter-intake` intake will stop asking the
     claimant-side questions. `/demand-draft` will still work for
     defendant-side pre-suit demands but the starting frame will be different."
   - *Risk calibration tightening high-risk threshold:* "More inbound
     demands and witness summonses will route through `/matter-briefing` and
     `/oc-status`."
   - *New standing external solicitor for IP matters:* "`/oc-status` will include
     this firm in weekly sweeps for IP-tagged matters."

5. **For shared-profile changes** (company name, industry, jurisdictions,
   practice setting, stage): write to
   `~/.claude/plugins/config/uk-legal-plugins/company-profile.md` and note:

   > This change affects all plugins that share your company profile — any
   > plugin that reads your jurisdiction footprint now sees [new value].

6. **Close.**

   > Done. Your next output will reflect the change. Anything else? You can
   > run `/litigation-legal-uk:customize` anytime.

## Guardrails

- **Never delete a section.** If the user wants to "remove" a matter type
  from scope, offer to mark it `[Not currently handled]` and explain what
  intake routing changes.
- **Flag internal inconsistency.** If the change would make the profile
  inconsistent (e.g., claimant-only side + defendant-only external solicitor
  roster; or "high volume" portfolio + no matter workspaces configured), flag
  the tension.
- **Flag guardrail degradation.** The "without prejudice" / LPP gate on
  `/demand-draft`, the LPP header on matter outputs, source attribution
  tags, and `[verify]` tags on cited authorities are load-bearing — do not
  remove. The `[review]` flag and the "do not file / send without
  solicitor/barrister review" framing are load-bearing.
- **One change at a time.** Don't re-ask the whole interview.

---
name: customize-legal-clinic-uk-uk-agents
title: /legal-clinic-uk:customize
description: Guided customisation of your UK law school clinic profile — change one thing without re-running the whole cold-start interview. Adjust clinic profile, jurisdiction (E&W / Scotland / NI), supervision style, practice-area templates, term configuration, or output safeguards. Use when the user says "change my [thing]", "new term", "add a practice area", "update my config", or "customise".
author: uk-agents
author_url: https://github.com/uk-agents/uk-legal-plugins/tree/main/legal-clinic-uk/skills/customize
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: gb
practice: general
language: en
---

# /legal-clinic-uk:customize

## When this runs

The user typed `/legal-clinic-uk:customize`. They (usually the supervisor, sometimes a student) want to change something in the clinic profile — a jurisdiction, a supervision style, a practice-area template, a term rollover — without re-running the whole cold-start interview and without hand-editing YAML.

## What to do

1. **Read the config.** Read `~/.claude/plugins/config/uk-legal-plugins/legal-clinic-uk/CLAUDE.md`. If the plugin config does not exist or still contains `[PLACEHOLDER]` values, say:

   > You haven't run setup yet. Run `/legal-clinic-uk:cold-start-interview` first — customize is for adjusting a profile you already have.

2. **Show the customisable map.** List what's in the profile, grouped, with a one-line summary of the current value:

   - **Clinic profile** — clinic name, host school, supervising solicitor/barrister, active practice areas, case type limits
   - **Jurisdiction** — E&W / Scotland / NI; primary courts/tribunals; local rules path
   - **Supervision style** — lighter-touch vs. formal review queue; if formal, who reviews what before it goes out; SRA/BSB compliance basis
   - **Practice-area templates** — which templates are active (housing, employment, immigration, family, consumer/debt, benefits, etc.) and any local overrides
   - **Term** — current term, active students, rollover rules, handoff memo format
   - **Output safeguards** — plain-language standards for client-facing outputs, deadline warning rules, privilege labelling
   - **Seed documents** — clinic handbook, tribunal/court rules, template letters, sample memos, form libraries
   - **Integrations** — document storage / case management / legal research MCP status, fallbacks

3. **Ask what they want to change.**

   > What would you like to adjust? Pick a section, or describe the change in your own words.

4. **Make the change.** Show the current value, ask for the new value, explain what changes downstream, confirm, write it to the config.

   Examples:
   - *Adding a new practice area:* "`/legal-clinic-uk:client-intake` will route matters of this type through the new template. `/legal-clinic-uk:draft`, `/legal-clinic-uk:memo`, and `/legal-clinic-uk:client-letter` will use the practice-area prompts. `/legal-clinic-uk:research-start` will add the corresponding Westlaw UK / BAILII search terms."
   - *Supervision style informal → formal review queue:* "`/legal-clinic-uk:supervisor-review-queue` becomes active — student output will land there for supervisor sign-off before it goes to the client. Note: this is consistent with your SRA/BSB supervision obligations."
   - *New term rollover:* "I'll archive the prior term's active cases, carry forward matters you flag as continuing, and prompt the incoming students through `/legal-clinic-uk:ramp`."
   - *Jurisdiction change (adding Scotland to E&W):* "I'll note that the clinic now has cases in both jurisdictions. `/legal-clinic-uk:draft`, `/legal-clinic-uk:research-start`, and `/legal-clinic-uk:deadlines` will need to be told which jurisdiction each case is in — the plausibility bands and procedure templates differ between E&W and Scotland."

5. **Close.**

   > Done. Your next output will reflect the change. Anything else? You can run `/legal-clinic-uk:customize` anytime.

## Guardrails

- **Never delete a section.** If the user wants to "drop" a practice area, offer to mark it `[Archived]` and explain that archiving keeps case history accessible but hides the template from intake routing.
- **Flag internal inconsistency.** If the change would make the profile inconsistent (e.g., formal review queue on + informal supervision note; or jurisdiction set to E&W + Scottish tribunal mentioned without a jurisdiction note), flag the tension.
- **Flag guardrail degradation.** These are load-bearing and should not be removed: the "NOT final work product" framing on `/legal-clinic-uk:draft`, plain-language standards on client-facing outputs, "does NOT decide case acceptance" on `/legal-clinic-uk:client-intake`, "NOT substantive advice" on `/legal-clinic-uk:client-letter`, the scaffold-not-analysis framing on `/legal-clinic-uk:memo`, and the SRA/BSB supervision reminders in every skill. If a student (not the supervisor) asks to remove these, flag it: "This guardrail exists because of the SRA/BSB supervision framework. Removing it would affect the clinic's compliance posture — discuss with [Supervisor] first."
- **Non-negotiable gates cannot be changed here.** The requirement that court/tribunal filings, substantive client letters, and status to courts/tribunals go through the supervising solicitor/barrister cannot be removed via customize. That is an SRA/BSB requirement, not a preference. `[SRA-CODE]` `[BSB-HANDBOOK]`
- **One change at a time.** Don't re-ask the whole interview.

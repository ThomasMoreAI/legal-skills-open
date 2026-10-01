---
name: poland-case-planning-xopoko
title: Poland Case Planning
description: Case planning. Use when Poland deadlines and multi-step procedures need a transient plan.
author: Xopoko
author_url: https://github.com/Xopoko/poland/tree/main/skills/poland-case-planning
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: pl
practice: administrative
language: en
---

# Poland Case Planning

Use for a multi-step administrative case, deadline orientation, evidence-category
planning, or a handoff between the user, an authority, and a professional. Keep
the plan transient: this skill does not create, update, or validate case files,
profiles, ledgers, or other durable user records.

## Workflow

1. State the abstract goal, citizenship/status category, locality category,
   deadline owner, and unresolved non-identifying facts.
2. Route the scenario and build the first checklist with the bundled CLI.
3. Separate tasks into `verify`, `prepare`, `official-page handoff`, and `done`.
4. Attach a source ID to every deadline or material procedural statement.
5. Return source evidence in the current response only: time, source ID, result,
   locator, supported claim IDs, and optional content hash.
6. Re-route after a status, job, family, locality, or official-letter change.

Never place PESEL, passport/document numbers, names, addresses, email, phone,
credentials, bank data, scans, correspondence, or personal-record content in
bundled plugin tools or a durable plan. A caller-owned tool may inspect the
minimum relevant personal material after explicit task-scoped authorization,
but the plan stays abstract and transient. The user may copy the generic output
into storage they control without further plugin access.

For the data and effect boundaries, read
`../../references/operating-contract.md`. For a domain procedure, hand off to its
focused skill; this skill owns transient planning, not eligibility or execution.
Scenario `stop_before` values are pause-and-classify checkpoints: resolve them
through `../../references/automation-playbook.md` rather than treating every
listed external effect as permanently prohibited.

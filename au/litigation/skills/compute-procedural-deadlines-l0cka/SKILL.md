---
name: compute-procedural-deadlines-l0cka
title: Compute Procedural Deadlines
description: Compute candidate procedural deadlines for Australian civil litigation from a lawyer-supplied trigger event using the bundled deterministic script and evidence-gated computation-rule tables — the model never performs date arithmetic. Computed coverage spans the federal courts and the superior and lower courts of every State and Territory, each with a verified holiday table; steps without a verified table entry receive identify-only output naming the governing rule. Use when a practitioner needs candidate dates for defences, appeals or other rule-fixed steps after filing, service or judgment. Do not use for criminal procedure, for court-fixed or discretionary dates, or when the trigger date is contested — those fail closed to the responsible lawyer, and every computed date is provisional until confirmed.
author: l0cka
author_url: https://github.com/l0cka/legal-skills/tree/main/plugins/australian-litigation-deadlines/skills/compute-procedural-deadlines
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: au
practice: litigation
language: en
---

# Compute Procedural Deadlines

Compute candidate deadlines with the bundled script and nothing else. A
refusal from the script is a correct result: report the governing rule and
the reason, and never fill the gap with model arithmetic.

Read the [source and control method](../../references/litigation-deadlines-source-and-control-method.md),
use an approved profile per the
[deadline profile schema](../../references/deadline-profile-schema.md), and
run [compute_deadline.py](scripts/compute_deadline.py) against the
[computation-rule tables](../../references/computation-rules/) and
[holiday tables](../../references/holidays/).

## Workflow

1. Fix the trigger and the forum.
   - Record the forum, the procedural step, the lawyer-supplied trigger
     date and what the trigger was (service, filing, judgment). A contested
     or unknown trigger date is `NOT READY` — never assume one.
2. Locate the governing rule.
   - Find the matching period rule in the forum's computation-rule table.
     A step with no table entry is identify-only: name the governing rule
     if known and route verification to `$verify-deadline-basis`.
3. Run the script.
   - Call `scripts/compute_deadline.py` with the table id, period rule id
     and trigger date. Report the script's output faithfully: `computed`
     results as candidate dates with the provisions applied and every
     warning; `identify_only` results with the stated reason.
   - Never adjust, round or re-derive a date the script produced or
     refused. If holiday caveats flag registry-location uncertainty,
     surface them.
4. Set the human decision gate.
   - Name the confirmer who must confirm each candidate date and enter it
     in the diary system of record before any reliance.

## Result contract

Lead with `READY FOR HUMAN REVIEW`, `READY WITH QUALIFICATIONS`, `NOT READY`
or `OUTSIDE SCOPE`.

```text
Step: <forum; procedural step; governing rule citation>
Trigger: <lawyer-supplied trigger event and date; stated as assumption>
Script result: <computed candidate date and day | identify-only with reason>
Provisions applied: <citations from the script output; evidence states>
Warnings: <script warnings, holiday caveats, staging limits>
Human decision gate: <confirmer; diary entry pending confirmation>
Limitations: <candidate only; not a diary system; script-only arithmetic>
```

## Fail closed

Return `NOT READY` when the trigger date, forum or governing rule cannot be
established. Report every script refusal as identify-only output — never
compute around an unverified table, an uncovered holiday range or an
unsupported period. Route criminal procedure `OUTSIDE SCOPE`, and never
present a candidate date as the binding deadline.

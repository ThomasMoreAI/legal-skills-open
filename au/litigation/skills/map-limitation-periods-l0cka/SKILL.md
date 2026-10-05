---
name: map-limitation-periods-l0cka
title: Map Limitation Periods
description: Map a described Australian civil cause of action to candidate limitation periods across every plausibly applicable jurisdiction — the eight state and territory Limitation Acts plus Commonwealth statutory periods — flagging postponement, extension and special regimes (discoverability, disability, fraud or concealment, deceased estates, child abuse, defamation, personal-injury schemes, contribution claims) without resolving them, and marking the earliest candidate as a conservative marker. Use when a practitioner needs the candidate limitation landscape for a claim. Do not use to determine accrual or discoverability, to pick a single binding date, for criminal matters or for foreign limitation law — contested characterisation fails closed to the responsible lawyer.
author: l0cka
author_url: https://github.com/l0cka/legal-skills/tree/main/plugins/australian-litigation-deadlines/skills/map-limitation-periods
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: au
practice: litigation
language: en
---

# Map Limitation Periods

Map a described cause of action to candidate limitation periods with
assumptions stated, candidates for every plausible characterisation and
jurisdiction, and the earliest candidate marked as the conservative marker —
a triage convention, never advice.

Read the [source and control method](../../references/litigation-deadlines-source-and-control-method.md),
use an approved profile per the
[deadline profile schema](../../references/deadline-profile-schema.md) and
work from the [limitation registry](references/limitation-registry.json).

## Workflow

1. Fix the claim and the inputs.
   - Record the described facts, every plausible characterisation of the
     cause of action, every plausibly applicable jurisdiction and the
     assessment date.
   - Record the lawyer-supplied accrual or discoverability date for each
     characterisation as an assumption. Never derive one: a missing accrual
     date makes that candidate `cannot be computed from inputs`.
2. Map candidates from the registry.
   - For each characterisation and jurisdiction, take the candidate period
     and statutory basis from the registry. Registry entries are routing
     leads: verify each period relied on through the jurisdiction's checker
     (`$check-commonwealth-legislation`, `$check-nsw-legislation`,
     `$check-victoria-legislation` or the applicable sibling) at the
     assessment date and record the evidence state.
   - Flag every potentially engaged special regime and every postponement
     or extension provision as a flag, never a conclusion.
3. Rank conservatively.
   - Order candidates by date and mark the earliest as the conservative
     marker. State plainly that the marker is a triage convention and that
     characterisation, accrual and any extension are the responsible
     lawyer's calls.
4. Set the human decision gate.
   - Name the confirmer who must resolve characterisation, confirm the
     controlling candidate and enter dates in the diary system of record.

## Result contract

Lead with `READY FOR HUMAN REVIEW`, `READY WITH QUALIFICATIONS`, `NOT READY`
or `OUTSIDE SCOPE`.

```text
Claim: <described facts; characterisations considered; assessment date>
Assumptions: <lawyer-supplied accrual or discoverability date per candidate>
Candidates: <jurisdiction; characterisation; period; statutory basis;
  candidate expiry; evidence state>
Conservative marker: <earliest candidate; stated as triage convention>
Special regimes flagged: <regime; why potentially engaged; not resolved>
Human decision gate: <confirmer; decisions required; diary entry pending>
Limitations: <all dates provisional; accrual and extensions are the
  lawyer's calls; not a diary system>
```

## Fail closed

Return `NOT READY` when characterisation, jurisdiction or a lawyer-supplied
accrual date cannot be established — never pick one to keep going. Mark any
claim type the registry does not cover `cannot be determined`, route
criminal matters and foreign limitation law `OUTSIDE SCOPE`, and never
present the conservative marker as the controlling date.

<!-- generated:plugin-dependencies -->
## Other plugins

This skill names skills from other Legal Skills plugins. Install a required
plugin alongside this one; install a hand-off plugin when the matter needs
that depth.

- `australian-legal-research` (required): `check-commonwealth-legislation`,
  `check-nsw-legislation`, `check-victoria-legislation`. Verifies the
  Commonwealth and state legislation behind limitation periods and deadline
  rules.

If a named skill is not available in this session, say so and name the plugin
to install. Treat the step it would have performed as not done: record the
affected proposition as not verified, or the hand-off as not made. Never
perform that step from memory or substitute a different skill.
<!-- end:plugin-dependencies -->

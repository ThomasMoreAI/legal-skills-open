---
name: route-australian-privacy-jurisdiction-l0cka
title: Route Australian Privacy Jurisdiction
description: Route Australian privacy, health-information, mandatory data-breach, surveillance and workplace-monitoring issues to the potentially applicable Commonwealth, State and Territory regimes using entity, role, data, conduct and date facts. Use before substantive privacy, breach or AI analysis where a State or Territory nexus is possible. Do not use for case law, final legal advice or as a substitute for checking current official legislation.
author: l0cka
author_url: https://github.com/l0cka/legal-skills/tree/main/plugins/australian-privacy-cybersecurity/skills/route-australian-privacy-jurisdiction
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: au
practice: data-protection
language: en
sources:
- title: Health Information Overlays
  path: references/health-information-overlays.md
- title: State Territory Breach Map
  path: references/state-territory-breach-map.md
- title: Surveillance Workplace Map
  path: references/surveillance-workplace-map.md
---

# Route Australian Privacy Jurisdiction

Build a candidate-law map before applying legal tests. Read
[references/state-territory-coverage.json](references/state-territory-coverage.json)
and the directly linked overlay references relevant to the facts.

## Workflow

1. Record each relevant date, jurisdiction, entity, public/private status,
   government-contract role, data type, health role, employee relationship,
   monitoring conduct and incident location. Keep supplied facts, assumptions
   and unknowns separate.
2. Route Commonwealth issues to `$check-commonwealth-legislation`, NSW issues
   to `$check-nsw-legislation`, and other jurisdictions to the matching
   `$check-victoria-legislation`, `$check-queensland-legislation`,
   `$check-western-australia-legislation`, `$check-south-australia-legislation`,
   `$check-tasmania-legislation`, `$check-act-legislation` or
   `$check-northern-territory-legislation` skill.
3. Apply the commencement boundary in the registry. Treat bills, future
   provisions, policies, standards, guidance and voluntary pathways according
   to their recorded status; none can satisfy a current-legislation check.
4. Read [references/health-information-overlays.md](references/health-information-overlays.md)
   for health data, [references/state-territory-breach-map.md](references/state-territory-breach-map.md)
   for incidents, and [references/surveillance-workplace-map.md](references/surveillance-workplace-map.md)
   for monitoring, recording or biometric use.
5. If the official source is unavailable, its compilation changed, or the
   registry's `last_verified` date is stale for the decision, return `CHECK
   REQUIRED`. Do not fill the gap from the registry, memory or secondary
   commentary.

## Required distinctions

- Local health legislation can overlap Commonwealth privacy law, especially
  for private health handling in NSW, Victoria and the ACT.
- A private NSW provider does not receive PPIP Act Part 6A coverage merely
  because the HRIP Act applies.
- Queensland local-government mandatory notification began on 1 July 2026.
- WA substantive PRIS obligations began on 1 July 2026, but its statutory
  breach scheme begins on 1 January 2027.
- Only NSW and the ACT have dedicated workplace-surveillance privacy Acts in
  the registry as at its verification date. Keep proposals separate.

## Result contract

Lead with `AUSTRALIAN PRIVACY JURISDICTION ROUTE — HUMAN REVIEW REQUIRED`, then
provide one row per candidate regime:

```text
Jurisdiction | Entity/role | Data/conduct | Instrument and status |
Commencement boundary | Candidate coverage | Official-source status |
Overlap or exclusion | Missing fact | Next verification action
```

State the legal as-at date, registry verification date, sources inspected and
that case law was outside scope. Routing is issue spotting, not a conclusion
that a law applies.

<!-- generated:plugin-dependencies -->
## Other plugins

This skill names skills from other Legal Skills plugins. Install a required
plugin alongside this one; install a hand-off plugin when the matter needs
that depth.

- `australian-legal-research` (required): `check-act-legislation`,
  `check-commonwealth-legislation`, `check-northern-territory-legislation`,
  `check-nsw-legislation`, `check-queensland-legislation`,
  `check-south-australia-legislation`, `check-tasmania-legislation`,
  `check-victoria-legislation`, `check-western-australia-legislation`.
  Verifies the Commonwealth, state and territory legislation the privacy,
  breach and cyber workflows rely on.

If a named skill is not available in this session, say so and name the plugin
to install. Treat the step it would have performed as not done: record the
affected proposition as not verified, or the hand-off as not made. Never
perform that step from memory or substitute a different skill.
<!-- end:plugin-dependencies -->

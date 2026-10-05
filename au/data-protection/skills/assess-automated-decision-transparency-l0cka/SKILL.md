---
name: assess-automated-decision-transparency-l0cka
title: Assess Automated Decision Transparency
description: Assess current and commencing Australian privacy transparency obligations for automated and AI-assisted decisions, including Privacy Act APP 1.7–1.9 commencing 10 December 2026 and Western Australia PRIS IPP 10 from 1 July 2026. Use for decision inventories, privacy-policy readiness, consequential AI decisions, procurement and deployments spanning those dates. Do not use for case law, discrimination-law conclusions or autonomous deployment approval.
author: l0cka
author_url: https://github.com/l0cka/legal-skills/tree/main/plugins/australian-privacy-cybersecurity/skills/assess-automated-decision-transparency
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: au
practice: data-protection
language: en
sources:
- title: Automated Decision Method
  path: references/automated-decision-method.md
---

# Assess Automated Decision Transparency

Separate current law, enacted future law and transition work. Read
[references/automated-decision-method.md](references/automated-decision-method.md)
before starting.

## Workflow

1. Inventory each decision, affected people, rights or interests, consequence,
   data categories, program role, human role, entity, jurisdiction and decision
   date. Distinguish a solely automated decision from a program doing something
   substantially and directly related to making a decision.
2. Invoke `$check-commonwealth-legislation` for the Privacy Act at the current
   and decision dates and `$trace-commonwealth-legislative-change` through 10
   December 2026 where relevant. Invoke
   `$route-australian-privacy-jurisdiction` for State or Territory overlays.
3. Apply the future-law ledger in the reference even if no future compilation
   yet displays APP 1.7–1.9. For decisions after commencement, do not exclude a
   system merely because its arrangement, data use or acquisition occurred
   earlier.
4. Determine the privacy-policy information needed for in-scope program use:
   kinds of personal information, solely automated decisions and decisions
   involving relevant program-performed steps. Verify exact current text before
   stating an obligation.
5. Treat the Children’s Online Privacy Code as developing unless the current
   official register confirms registration and application. The OAIC must
   register it by 10 December 2026; verify whether it has been registered. Keep guidance,
   discrimination, administrative and employment issues in separate rows.

## Result contract

Lead with one status:

- `CURRENT REQUIREMENTS MAPPED — FUTURE CHANGE NOT WITHIN HORIZON`
- `CURRENT TEXT VERIFIED — KNOWN FUTURE CHANGE MAPPED`
- `AUTOMATED-DECISION LAW CHECK REQUIRED — DO NOT RELY`

Then provide:

```text
Decision | Date | Entity and jurisdiction | Program role | Personal information |
Potential significant effect | Current law | Future law | Transition action |
Privacy-policy disclosure | Evidence gap | Owner and due date
```

State that case law was outside scope. Do not describe readiness work as proof
of compliance or approve the decision system.

<!-- generated:plugin-dependencies -->
## Other plugins

This skill names skills from other Legal Skills plugins. Install a required
plugin alongside this one; install a hand-off plugin when the matter needs
that depth.

- `australian-legal-research` (required): `check-commonwealth-legislation`,
  `trace-commonwealth-legislative-change`. Verifies the Commonwealth, state
  and territory legislation the privacy, breach and cyber workflows rely on.

If a named skill is not available in this session, say so and name the plugin
to install. Treat the step it would have performed as not done: record the
affected proposition as not verified, or the hand-off as not made. Never
perform that step from memory or substitute a different skill.
<!-- end:plugin-dependencies -->

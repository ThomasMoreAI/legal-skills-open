---
name: map-australian-cyber-incident-obligations-l0cka
title: Map Australian Cyber Incident Obligations
description: Map concurrent Australian cyber incident, data-breach, ransomware-payment, critical-infrastructure, prudential, telecommunications, Consumer Data Right and health reporting obligations by entity, role, event, trigger, recipient and clock. Use when only the obligations and reporting-clock matrix is needed, or as the cyber layer inside assess-australian-data-breach; for a full incident triage with facts, harm assessment and action plan use assess-australian-data-breach instead. Do not use for live containment, external notification, case law, forensic conclusions or autonomous legal decisions.
author: l0cka
author_url: https://github.com/l0cka/legal-skills/tree/main/plugins/australian-privacy-cybersecurity/skills/map-australian-cyber-incident-obligations
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: au
practice: cybersecurity
language: en
---

# Map Australian Cyber Incident Obligations

Build one independently verified row per entity and obligation. Read
[references/cyber-regime-registry.json](references/cyber-regime-registry.json)
before routing. The registry is a currency alarm and issue-spotting aid, not
authority.

## Workflow

1. Record each entity and role, regulated sector, asset and data type, incident
   facts, availability impact, control weakness, outage, ransom demand,
   payment, awareness time, prior regulator notice and relevant contracts.
2. Route each Commonwealth Act and instrument through
   `$check-commonwealth-legislation`. Use
   `$trace-commonwealth-legislative-change` across an incident or remediation
   horizon that crosses an amendment or transition.
3. Apply the registry's supersession, trigger and clock prompts only after
   verifying current primary text. A changed compilation, instrument inventory
   or commencement point produces `CHECK REQUIRED`, while urgent containment
   and already verified duties continue.
4. Preserve concurrent obligations. Do not collapse entities, awareness times,
   recipients or clocks into a single report or portal.
5. Separate `Act`, `delegated legislative instrument or industry standard`,
   `enforceable prudential standard`, `regulator guidance`, `contract or
   insurance`, and `voluntary report` in every output.

## Mandatory overlap rules

- A 30-day NDB assessment period is not a 30-day notification deadline.
- Cyber Security Act Part 4 voluntary sharing does not discharge other duties,
  and limited-use provisions do not themselves create legal professional
  privilege.
- A single reporting portal is not a single-report safe harbour.
- CDR can require NDB treatment plus a separate ACSC report; do not fold CDR
  safeguards into the APPs.
- My Health Record section 75 can engage the Privacy Act section 26WD
  no-duplicate-notice rule; do not generalise it to other health incidents.
- Apply the CPS 234/CPS 230 interaction and earliest clock only after checking
  current APRA material. A ransomware payment and SOCI report can both apply.
- Telco DFV two-day notification can apply without NDB serious-harm eligibility.

## Result contract

Lead with `CONCURRENT CYBER OBLIGATIONS MAP — URGENT HUMAN REVIEW REQUIRED`:

```text
Entity | Role | Legal-status class | Regime and provision | Event and threshold |
Awareness/trigger fact | Clock and counting rule | Recipient | Verification |
Overlap or non-duplication rule | Source | Missing fact | Decision owner
```

Show the earliest plausible deadline prominently but label it provisional when
any trigger fact is unresolved. State that case law was outside scope and do
not submit any notification.

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

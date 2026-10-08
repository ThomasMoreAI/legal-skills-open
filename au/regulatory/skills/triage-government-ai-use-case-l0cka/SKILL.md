---
name: triage-government-ai-use-case-l0cka
title: Triage Government AI Use Case
description: Route an Australian government AI use case to the applicable assurance track — the mandatory DTA policy artefacts for Commonwealth entities or the state and territory frameworks for NSW, Victoria, Queensland, WA, SA, Tasmania, the ACT and the NT — with each jurisdiction's escalation threshold, using a verified registry and the national assurance framework. Use for government AI adoption, procurement and assurance planning. Do not use for private-sector obligations mapping, court generative-AI practice directions, privacy depth or a completed risk assessment.
author: l0cka
author_url: https://github.com/l0cka/legal-skills/tree/main/plugins/australian-ai-governance/skills/triage-government-ai-use-case
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: au
practice: regulatory
language: en
---

# Triage Government AI Use Case

Route the use case to the right jurisdictional assurance track and name the
artefacts and escalation threshold that track requires. The triage output is
a routing, not a completed assessment.

Read the [source and control method](../../references/ai-governance-source-and-control-method.md)
and use the
[government AI assurance registry](references/government-ai-assurance-registry.json).

## Workflow

1. Fix the entity and use case.
   - Record the agency, jurisdiction, the AI system or use case, its purpose,
     affected people and deployment status. For a Commonwealth entity,
     confirm whether it is a non-corporate entity covered by the mandatory
     DTA policy.
2. Select the track from the registry.
   - Match the jurisdiction to its registry entry. Re-verify the named
     official source at use time: the registry is a research snapshot, and
     entries marked `lead-verify-before-use` or `verified-with-caveat` (SA
     and Tasmania at the snapshot date) must be confirmed against the
     official page or document before any assertion.
   - Note the national assurance framework as the cross-jurisdiction
     baseline, pegged to Australia's AI Ethics Principles.
3. Name the required artefacts and threshold.
   - Commonwealth: accountable official, AI transparency statement and AI
     impact assessment under DTA policy v2.0, with its phased commencement
     checked at the assessment date (remaining requirements, including AI
     impact assessments, reportedly due by 15 December 2026 — verify).
   - States and territories: the framework's self-assessment or risk
     assessment, and the escalation body or trigger recorded in the registry
     (for example NSW AI Review Committee; NT AI advisory service for medium
     and high-risk projects).
4. Flag adjacent obligations without assessing them.
   - Route privacy depth to `$assess-ai-privacy-cybersecurity-use-case` and
     jurisdictional privacy routing to
     `$route-australian-privacy-jurisdiction`. Verify any statutory
     proposition with the relevant `$check-*-legislation` skill.
   - Court or tribunal generative-AI practice directions are
     `OUTSIDE SCOPE` — identify the court and stop.
5. Set the human decision gate.
   - Name the accountable role in the agency, the artefacts to complete and
     the unresolved questions the assurance process must answer.

## Result contract

Lead with `READY FOR HUMAN REVIEW`, `READY WITH QUALIFICATIONS`, `NOT READY`
or `OUTSIDE SCOPE`.

```text
Entity and use case: <agency, jurisdiction, system, purpose, status>
Assurance track: <framework; official source; verification state at use time>
Required artefacts: <assessments, statements, accountable roles>
Escalation threshold: <body or trigger and when it engages>
National baseline: <national framework applicability note>
Adjacent routings: <privacy and legislation skills engaged or flagged>
Human decision gate: <accountable role and unresolved questions>
Limitations: <routing only; no completed risk assessment or approval>
```

## Fail closed

Return `NOT READY` when the jurisdiction, entity coverage or the current
official framework text cannot be established, and `OUTSIDE SCOPE` for
non-government entities and court practice directions. Never rely on a
registry entry marked `lead-verify-before-use` without confirming the
official source, never substitute the national framework for a mandatory
jurisdictional track, and never present the triage as a completed assurance
assessment.

<!-- generated:plugin-dependencies -->
## Other plugins

This skill names skills from other Legal Skills plugins. Install a required
plugin alongside this one; install a hand-off plugin when the matter needs
that depth.

- `australian-privacy-cybersecurity` (hand-off):
  `assess-ai-privacy-cybersecurity-use-case`,
  `route-australian-privacy-jurisdiction`. Takes privacy, cybersecurity and
  automated-decision transparency depth for AI use cases.

If a named skill is not available in this session, say so and name the plugin
to install. Treat the step it would have performed as not done: record the
affected proposition as not verified, or the hand-off as not made. Never
perform that step from memory or substitute a different skill.
<!-- end:plugin-dependencies -->

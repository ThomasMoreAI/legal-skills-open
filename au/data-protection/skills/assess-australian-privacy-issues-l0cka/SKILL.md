---
name: assess-australian-privacy-issues-l0cka
title: Assess Australian Privacy Issues
description: Identify and structure Australian privacy, data protection and cybersecurity legal issues from facts, contracts, policies, data maps or proposed activities; map each issue to potentially applicable Commonwealth, State or Territory legislation; perform change-safe Australian Privacy Principles verification; verify Commonwealth and NSW legislation with the corresponding legislation skills; and prepare a source-linked issue matrix for lawyer review. Use for privacy scoping, applicability analysis, privacy-policy or DPA issue spotting, data-flow reviews, cyber regulatory scoping and preliminary legal research. Do not use for case law, foreign law, final legal opinions, autonomous compliance decisions or external notifications.
author: l0cka
author_url: https://github.com/l0cka/legal-skills/tree/main/plugins/australian-privacy-cybersecurity/skills/assess-australian-privacy-issues
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: au
practice: data-protection
language: en
sources:
- title: Current Commonwealth Privacy Map
  path: references/current-commonwealth-privacy-map.md
- title: Source And Issue Method
  path: references/source-and-issue-method.md
---

# Assess Australian Privacy Issues

Produce a preliminary issue-and-law map for an Australian lawyer. Do not state
that a duty applies until its threshold facts and current legislative text have
been checked.

Read [references/source-and-issue-method.md](references/source-and-issue-method.md)
before starting. It defines the source hierarchy, legislation routing, issue
taxonomy and treatment of Harvey Labs patterns.

Read [references/current-commonwealth-privacy-map.md](references/current-commonwealth-privacy-map.md)
when Commonwealth privacy law is potentially relevant. Treat its dated entries
as prompts requiring current verification.

## Workflow

1. Protect the material and fix scope.
   - Ask for de-identified facts or the minimum necessary extracts. Do not
     request credentials, exploit code, unnecessary identifiers or complete
     client files.
   - Record the Australian jurisdiction or jurisdictions, relevant dates,
     entity types, sector, data subjects, data types, conduct and requested
     deliverable. Use today's `Australia/Sydney` date when no as-at date is
     given and say so.
   - State that case law is outside scope. Do not search for, cite, summarise or
     rely on cases, tribunal decisions or case-derived tests. Mark a request
     requiring them `OUTSIDE SCOPE` for that component.
2. Build a fact and applicability map.
   - Separate supplied facts, reasonable inferences, assumptions and missing
     facts. Never invent an entity, data flow, contract term or jurisdiction.
   - Identify possible roles and thresholds without deciding them silently:
     APP entity or exemption; Commonwealth, State or Territory body; health or
     other sector; controller-like or service-provider role; overseas actor;
     critical-infrastructure or regulated-entity status.
   - Identify collection, use, disclosure, security, access/correction,
     retention/destruction, direct marketing, automated decision-making,
     cross-border, vendor and incident-response issues raised by the facts.
   - Invoke `$route-australian-privacy-jurisdiction` whenever a State or
     Territory nexus is possible. Preserve its public/private, health,
     government-contractor, breach and surveillance distinctions.
3. Identify candidate law.
   - Use the trigger table in the reference. Treat it as an issue-spotting aid,
     not authority or a statement that every listed law applies.
   - Distinguish legislation, delegated legislation, regulator guidance,
     contractual requirements and voluntary standards. Do not present guidance
     or standards as legislation.
   - Keep foreign-law analysis outside scope. Record a foreign nexus only as a
     referral or separate-workstream issue.
4. Verify legislation.
   - For each Commonwealth candidate, invoke
     `$check-commonwealth-legislation` with the title, relevant provision and
     as-at date. Preserve its Register IDs, version period, currency flags and
     qualifications.
   - If the question spans legislative change, a future deployment date or
     more than one applicable compilation, invoke
     `$trace-commonwealth-legislative-change` and keep future or transitional
     law separate from law in force at the as-at date.
   - For each NSW candidate, invoke `$check-nsw-legislation` in the same way.
   - Whenever an APP may apply, invoke
     `$check-australian-privacy-principles` for the as-at date and decision
     horizon. Do not use a static APP list as authority.
   - If the APP result is `APP FRAMEWORK CHANGE DETECTED – LEGAL CONTENT REVIEW
     REQUIRED`, stop reuse of earlier APP analysis and identify each affected
     mapping for lawyer refresh. If it is `APP FRAMEWORK NOT VERIFIED – DO NOT
     RELY`, make no APP conclusion.
   - Invoke `$assess-statutory-privacy-tort` independently of APP coverage for
     surveillance, recording, scraping, profiling, inference, deepfakes,
     disclosure, publication or intimate, location, health or financial data.
   - Invoke `$assess-automated-decision-transparency` for automated or
     AI-assisted decisions, including any horizon crossing 10 December 2026.
   - Invoke `$map-australian-cyber-incident-obligations` for a suspected
     incident, cyber-extortion payment, outage or material control weakness.
   - If a legislation skill or official source is unavailable, do not fill the
     gap from memory, a search snippet or secondary commentary. Label it `NOT
     VERIFIED` and identify the exact follow-up check.
5. Analyse and report.
   - Apply verified text to stated facts provisionally. Expose threshold
     uncertainty and plausible alternatives.
   - Give each issue a practical consequence, missing fact and concrete next
     step. Do not assign false numerical risk scores.
   - Include favourable or compliant features as well as gaps when reviewing a
     document or program.

## Result contract

Lead with `PRELIMINARY LAW AND ISSUE MAP — HUMAN REVIEW REQUIRED`, followed by:

```text
Scope: <task and expressly excluded components>
Jurisdiction: <Commonwealth and each State or Territory considered>
As at: <YYYY-MM-DD, Australia/Sydney>
Materials reviewed: <de-identified list>
Facts, assumptions and gaps: <separate lists>

Applicability matrix:
Entity/conduct | Candidate regime | Threshold facts | Preliminary status | Evidence needed

APP framework layers: <text, application perimeter, instruments, future changes and guidance>
Jurisdiction route: <Commonwealth, State and Territory candidates and boundaries>
Statutory privacy tort: <separate Schedule 2 screen or reason not triggered>
Automated decisions: <current/future status or reason not triggered>

Issue matrix:
Priority | Issue | Material fact | Candidate legislation/provision |
Legislation-check status | Analysis | Missing fact | Recommended next step | Source

Non-legislative material: <guidance, standards and contracts, clearly labelled>
Case law: Outside scope and not considered
Immediate actions: <bounded, reviewable actions>
Limitations and lawyer review: <unresolved currency, scope and interpretation points>
```

Use these legislation-check statuses only: `VERIFIED`, `VERIFIED WITH
QUALIFICATIONS`, `NOT VERIFIED`, `PRIMARY TEXT CHECK REQUIRED`, or `OUTSIDE
SCOPE`. Link every legal proposition to the official material actually
inspected. Do not imply that issue identification replaces professional
judgment.

<!-- generated:plugin-dependencies -->
## Other plugins

This skill names skills from other Legal Skills plugins. Install a required
plugin alongside this one; install a hand-off plugin when the matter needs
that depth.

- `australian-legal-research` (required): `check-commonwealth-legislation`,
  `check-nsw-legislation`, `trace-commonwealth-legislative-change`. Verifies
  the Commonwealth, state and territory legislation the privacy, breach and
  cyber workflows rely on.

If a named skill is not available in this session, say so and name the plugin
to install. Treat the step it would have performed as not done: record the
affected proposition as not verified, or the hand-off as not made. Never
perform that step from memory or substitute a different skill.
<!-- end:plugin-dependencies -->

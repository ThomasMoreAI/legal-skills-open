---
name: assess-ai-privacy-cybersecurity-use-case-l0cka
title: Assess AI Privacy and Cybersecurity Use Case
description: Assess whether a proposed or existing AI-system use case is suitable from an Australian privacy, cybersecurity and related governance perspective; identify data flows, affected people, legal thresholds, harms, threats, vendor dependencies and controls; perform change-safe Australian Privacy Principles verification; verify relevant Commonwealth and NSW legislation with the corresponding legislation skills; and prepare a reasoned suitability recommendation for lawyer and accountable-owner review. Use for AI intake, procurement, pilots, deployment changes, privacy impact assessments, generative-AI use cases and automated or AI-assisted decisions. Do not use for case law, foreign law, technical penetration testing, final legal opinions, autonomous approval, a complete review of discrimination, consumer, employment, intellectual-property or sector-specific law, or the AI-governance obligations map and board oversight that the australian-ai-governance plugin owns.
author: l0cka
author_url: https://github.com/l0cka/legal-skills/tree/main/plugins/australian-privacy-cybersecurity/skills/assess-ai-privacy-cybersecurity-use-case
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: au
practice: data-protection
language: en
sources:
- title: Ai Use Case Method
  path: references/ai-use-case-method.md
---

# Assess AI Privacy and Cybersecurity Use Case

Assess a defined AI-system use case, not an AI product in the abstract. Produce
a provisional recommendation supported by verified law, evidence and controls.

Read [references/ai-use-case-method.md](references/ai-use-case-method.md) before
starting. It defines the intake schema, risk domains, suitability outcomes,
control tests and authority boundaries.

## Workflow

1. Define the use case and decision.
   - Record the intended purpose, accountable owner, users, affected people,
     deployment context, jurisdiction, sector, benefit, decision supported or
     made, consequence of error, level of automation and requested decision.
   - Identify the exact system, model, version, hosting arrangement, provider,
     integrations and proposed change. Do not treat vendor marketing as proof
     of system behaviour or controls.
   - Use de-identified inputs and minimum necessary extracts. Do not request
     credentials, model secrets, live malicious content, unnecessary personal
     information or complete client files.
2. Map data and system behaviour.
   - Trace collection or generation, prompts and inputs, retrieval sources,
     training or fine-tuning, inference, outputs, logs, human review, onward
     disclosure, storage, retention, deletion, monitoring and incident paths.
   - Classify personal, sensitive, health, confidential, privileged, security-
     classified and synthetic data separately. Record uncertainty about
     identifiability and re-identification.
   - Separate supplied facts, vendor claims, tested evidence, assumptions and
     unknowns. Never invent a control or infer that a setting is enabled.
3. Test law and governance scope.
   - Invoke `$route-australian-privacy-jurisdiction` for public-sector,
     government-contractor, health, surveillance, workplace and State or
     Territory automated-decision overlays.
   - Identify candidate privacy and cyber legislation using the linked
     reference. Verify Commonwealth propositions with
     `$check-commonwealth-legislation` and NSW propositions with
     `$check-nsw-legislation`, including point-in-time and known-future-change
     qualifications.
   - If deployment, review or retention extends across a Commonwealth
     legislative change, invoke `$trace-commonwealth-legislative-change` and
     distinguish present requirements, future requirements and transition
     actions.
   - If personal information or APP-entity coverage is possible, invoke
     `$check-australian-privacy-principles` using the legal as-at date and a
     decision horizon covering the pilot, deployment, retention and next review
     dates that are actually known.
   - Invoke `$assess-statutory-privacy-tort` independently of APP coverage for
     surveillance, recording, scraping, profiling, inference, deepfakes,
     publication or intimate, location, health or financial information.
   - Invoke `$assess-automated-decision-transparency` whenever a program makes
     or performs a material step related to a decision. Include the 10 December
     2026 Commonwealth transition and WA IPP 10 where relevant.
   - Invoke `$map-australian-cyber-incident-obligations` when the proposed
     system, smart product or response plan could engage sector incident,
     outage, control-weakness or cyber-extortion obligations.
   - Do not issue `SUITABLE`, `SUITABLE WITH CONTROLS` or `PILOT ONLY` while an
     APP layer requires legal-content or application-law review, or while the
     result is `APP FRAMEWORK NOT VERIFIED – DO NOT RELY`. Use `INSUFFICIENT
     INFORMATION` or `NOT SUITABLE ON CURRENT INFORMATION`, as the facts
     warrant, until a lawyer refreshes the APP analysis.
   - For another State or Territory, inspect its official legislation
     publisher. Use `PRIMARY TEXT CHECK REQUIRED` or `NOT VERIFIED` when an
     applicable version cannot be established.
   - Label OAIC, ACSC, National AI Centre, standards and organisational policies
     as guidance, standards or internal controls, not legislation.
   - State that case law was not considered. Flag discrimination, consumer,
     employment, intellectual-property, administrative, records, professional
     and sector-specific law for separate review where material.
4. Assess risks and controls.
   - Test necessity and proportionality, purpose compatibility, notice and
     transparency, lawful authority, data quality, security, access, vendor and
     subprocessors, overseas handling, retention, individual rights, human
     oversight, contestability, monitoring, incident response and exit.
   - Test AI-specific failure modes: unreliable output, automation bias,
     prompt injection, data or model leakage, insecure tool use, excessive
     agency, poisoned retrieval or training data, model or supply-chain change,
     weak identity/access control and inadequate auditability.
   - Link each risk to a fact, affected person, plausible harm, evidence,
     existing control, residual gap, owner and acceptance criterion. Do not use
     a numerical score unless the organisation supplied an approved method.
5. Recommend and gate.
   - Apply the suitability outcomes exactly as defined in the reference. A
     legal or factual unknown cannot be cured by optimistic assumptions.
   - Specify conditions precedent, pilot limits, prohibited data or actions,
     required testing, monitoring, review date, stop triggers and approval
     owner.
   - Do not approve, procure, deploy, connect, upload data to, or change the AI
     system. The lawyer and accountable owner make the decision.

## Result contract

Lead with one provisional outcome followed by `— HUMAN APPROVAL REQUIRED`:

- `SUITABLE`
- `SUITABLE WITH CONTROLS`
- `PILOT ONLY`
- `NOT SUITABLE ON CURRENT INFORMATION`
- `INSUFFICIENT INFORMATION`

Then provide:

```text
Use case and decision requested: <bounded description>
Jurisdiction and sector: <identified and unresolved>
As at: <YYYY-MM-DD, Australia/Sydney>
System and version: <verified identifiers or unknown>
Materials reviewed: <de-identified list>
Benefit and necessity: <supported benefit, alternatives and proportionality>
Facts, vendor claims, assumptions and unknowns: <separate sections>

Data-flow summary: <source to input to processing to output to storage/disclosure/deletion>
Applicability matrix: <candidate regime, threshold, verified text and status>
APP framework status: <exact result, inventories and decision-horizon coverage>
Jurisdiction and health overlays: <routes and verified boundaries>
Statutory privacy tort: <separate Schedule 2 screen or reason not triggered>
Automated-decision transparency: <current and future requirements>
Cyber and sector obligations: <deployment and incident-response routes>
Risk-control matrix:
Priority | Risk event | Affected people/asset | Material fact | Legal/governance basis |
Existing control and evidence | Residual gap | Required control | Owner | Acceptance test

Suitability reasons: <decisive reasons for the outcome>
Conditions before use: <testable conditions precedent>
Pilot boundary: <users, data, duration, functions and prohibited uses>
Monitoring, review and stop triggers: <measures, owner and date>
Adjacent legal referrals: <issues outside this skill's complete coverage>
Case law: Outside scope and not considered
Limitations and approval: <unresolved matters and named decision owner>
```

Use `VERIFIED`, `VERIFIED WITH QUALIFICATIONS`, `NOT VERIFIED`, `PRIMARY TEXT
CHECK REQUIRED`, or `OUTSIDE SCOPE` for legislation status. Link each legal
proposition to official material actually inspected. Do not represent this
assessment as certification, assurance or a substitute for professional
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

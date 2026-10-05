---
name: assess-australian-data-breach-l0cka
title: Assess Australian Data Breach
description: Triage a suspected Australian privacy or cybersecurity incident for lawyers; extract incident facts; identify potentially applicable Commonwealth, State, Territory and sectoral breach regimes; perform change-safe Australian Privacy Principles verification where an APP issue is material; verify Commonwealth and NSW legislation through the corresponding legislation skills; distinguish statutory, regulatory, contractual and voluntary reporting; and prepare a time-sensitive assessment and action matrix. Use for suspected unauthorised access, disclosure or loss, ransomware, cyber extortion, vendor incidents and breach-response planning. Do not use for case law, forensic conclusions, live containment, threat hunting, external reports or autonomous notification decisions.
author: l0cka
author_url: https://github.com/l0cka/legal-skills/tree/main/plugins/australian-privacy-cybersecurity/skills/assess-australian-data-breach
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: au
practice: data-protection
language: en
sources:
- title: Breach Assessment Method
  path: references/breach-assessment-method.md
---

# Assess Australian Data Breach

Prepare a privileged-workstream-ready preliminary assessment for a lawyer. Do
not conclude that a breach is notifiable merely because a security incident
occurred, and do not delay urgent human escalation while researching.

Read [references/breach-assessment-method.md](references/breach-assessment-method.md)
before starting. It defines the fact schema, regime prompts, deadline controls
and source rules.

## Workflow

1. Escalate and protect.
   - Flag immediate safety, ongoing compromise, destructive activity, material
     service disruption or an apparently running statutory clock for urgent
     human attention.
   - Ask only for the minimum de-identified facts. Do not request credentials,
     live malware, exploit code, unnecessary identifiers or complete datasets.
   - Do not take containment action, contact a threat actor, make a payment,
     notify a person or regulator, or submit a report. Preserve the lawyer's
     approval boundary and the forensic evidence-preservation plan.
2. Establish the incident record.
   - Separate known facts, source of each fact, estimates, inferences,
     assumptions, disputed facts and unknowns.
   - Record detection and awareness times with timezone; suspected occurrence
     window; systems and custodians; data types and protections; affected and
     potentially affected people; location; actors; containment/remediation;
     recipients; vendors; critical services; ransom demand or payment; and
     existing notices.
   - Do not equate detection, confirmation, containment, assessment completion
     or occurrence. Record each timestamp independently.
3. Map candidate regimes.
   - Test the Privacy Act Notifiable Data Breaches scheme and each applicable
     State, Territory, health, critical-infrastructure, cyber-extortion,
     telecommunications, financial-services or contractual regime.
   - Distinguish mandatory notice, assessment duties, voluntary reports,
     contractual notice, insurance conditions and internal escalation.
   - Treat numerical thresholds, triggering knowledge standards, recipients,
     content requirements and time periods as propositions requiring current
     verification.
   - Invoke `$route-australian-privacy-jurisdiction` for every State or
     Territory nexus and `$map-australian-cyber-incident-obligations` for the
     concurrent Commonwealth and sectoral matrix.
4. Verify law and calculate cautiously.
   - Invoke `$check-commonwealth-legislation` for every material Commonwealth
     title or provision and the relevant incident date. Invoke
     `$check-nsw-legislation` for every material NSW title or provision.
   - Invoke `$check-australian-privacy-principles` when security, retention,
     use, disclosure or another APP issue is material. Keep this Schedule 1
     check separate from verification of the Notifiable Data Breaches scheme.
     A detected or unverified APP-framework change blocks the APP conclusion,
     but must not delay urgent containment or independently verified incident
     duties.
   - Invoke `$assess-statutory-privacy-tort` independently of APP coverage when
     intentional or reckless intrusion, surveillance, misuse, disclosure or
     publication may be material.
   - For another State or Territory, inspect its official legislation source.
     If a version or commencement point cannot be established, use `NOT
     VERIFIED` and escalate the check.
   - Calculate a deadline only after verifying the trigger, period, counting
     rule and relevant facts. Show the trigger time, timezone, calculation and
     uncertainty. Never invent a date from an incomplete record.
   - State that case law was not considered. Do not search for or rely on it.
5. Assess and hand off.
   - Address reasonable-likelihood, serious-harm, remedial-action and
     multi-entity issues only against verified text and stated facts.
   - Build one row per possible obligation. Give the earliest plausible
     deadline prominence without describing an uncertain date as final.
   - Identify the decision owner, evidence needed and next action. Reserve all
     notification and legal conclusions for a lawyer and authorised incident
     lead.

## Result contract

Lead with `URGENT PRELIMINARY BREACH ASSESSMENT — HUMAN DECISION REQUIRED`, then
provide:

```text
Incident status: <suspected/ongoing/contained/unknown, not a legal conclusion>
Scope and exclusions: <including no case law and no forensic opinion>
Jurisdictions and sectors: <identified and unresolved>
As at: <YYYY-MM-DD HH:MM timezone>
Immediate human escalations: <owner and reason>
Known facts, assumptions, disputes and unknowns: <separate sections>
APP framework status: <exact result and effect on APP analysis, if relevant>

Potential-obligation matrix:
Priority | Regime | Entity/role | Trigger and threshold | Trigger facts |
Verification status | Earliest plausible deadline | Recipient/action |
Source | Missing evidence | Decision owner

Harm and remediation assessment: <facts for and against, uncertainty retained>
Notification coordination: <statutory, contractual, insurer and voluntary channels separated>
Concurrent cyber map: <one row and one clock per entity and regime>
Statutory privacy tort: <separate screen or reason not triggered>
Action plan: <owner, action, time, dependency and approval>
Preservation and privilege considerations: <questions for the lawyer and forensic lead>
Limitations and review: <currency, factual and interpretation gaps>
```

Use `VERIFIED`, `VERIFIED WITH QUALIFICATIONS`, `NOT VERIFIED`, `PRIMARY TEXT
CHECK REQUIRED`, or `OUTSIDE SCOPE` for legislation status. Link the official
text and version actually inspected. Do not describe an OAIC or ACSC web form,
guideline, policy, standard or contract as legislation.

## Example

An abbreviated completed assessment for a vendor ransomware incident. Every
value is illustrative, and a real assessment includes one matrix row per
possible obligation, not the two shown.

```text
URGENT PRELIMINARY BREACH ASSESSMENT — HUMAN DECISION REQUIRED

Incident status: Suspected, containment unconfirmed (not a legal conclusion)
Scope and exclusions: No case law considered; no forensic opinion given
Jurisdictions and sectors: Commonwealth confirmed; NSW health nexus unresolved
As at: 2026-08-14 09:30 Australia/Sydney
Immediate human escalations: Incident lead — ransom demand received and a
  statutory assessment clock may already be running
Known facts, assumptions, disputes and unknowns: Detection 2026-08-13 22:10
  AEST (known, monitoring alert); occurrence window unknown; exfiltration
  assumed but disputed by vendor

APP framework status: VERIFIED WITH QUALIFICATIONS — APP 11 verified against
  the current compilation; a commenced-but-unincorporated amendment was
  flagged and blocks an unqualified APP conclusion

Potential-obligation matrix (abbreviated):
1 | Privacy Act NDB scheme | APP entity | Reasonable grounds to suspect an
  eligible data breach → 30-day assessment | Detection facts above |
  VERIFIED | 2026-09-12 (from detection; trigger time uncertain) | OAIC +
  affected individuals | <official compilation link> | Exfiltration evidence |
  General counsel
2 | Vendor MSA cl 14 notice | Customer of vendor | "Security incident" defined
  term, 48 hours | Vendor notice 2026-08-14 07:00 | OUTSIDE SCOPE (contract,
  not legislation) | 2026-08-16 07:00 | Customer security contact | MSA v3.2 |
  Executed MSA copy | Commercial lead

Harm and remediation assessment: Facts for and against serious harm retained
  separately; no conclusion drawn
Action plan: Preserve logs (forensic lead, today); confirm data classes
  (vendor, 48h); lawyer decision on NDB assessment start time
Limitations and review: Occurrence window, exfiltration and NSW nexus
  unverified; all notification decisions reserved to the lawyer
```

<!-- generated:plugin-dependencies -->
## Other plugins

This skill names skills from other Legal Skills plugins. Install a required
plugin alongside this one; install a hand-off plugin when the matter needs
that depth.

- `australian-legal-research` (required): `check-commonwealth-legislation`,
  `check-nsw-legislation`. Verifies the Commonwealth, state and territory
  legislation the privacy, breach and cyber workflows rely on.

If a named skill is not available in this session, say so and name the plugin
to install. Treat the step it would have performed as not done: record the
affected proposition as not verified, or the hand-off as not made. Never
perform that step from memory or substitute a different skill.
<!-- end:plugin-dependencies -->

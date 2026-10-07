---
name: gdpr-dpia-en-matematicsolutions
title: GDPR DPIA EN - Data Protection Impact Assessment (Art. 35-36)
description: 'Data Protection Impact Assessment (DPIA) assistant grounded in GDPR Art. 35-36, the EDPB WP248 rev.01 guidelines, and national supervisory-authority blacklists. Walks through: (1) the threshold test - is a DPIA REQUIRED (EDPB''s 9 criteria, the ">=2" rule of thumb, Art. 35(3) mandatory cases, the SA''s mandatory list), (2) the DPIA structure mandated by Art. 35(7) (systematic description, necessity & proportionality, risk assessment, mitigating measures), (3) the Art. 36 prior-consultation decision. Drafts the DPIA and a decision log - it does NOT make the controller''s risk decision or file with the authority (those are human acts). Adds no connectors and makes no outbound calls of its own; the system description you paste still goes to the model you have configured. Use when: "do I need a DPIA", "data protection impact assessment", "DPIA for profiling/CCTV/AI", "Art. 35 GDPR", "prior consultation", "high-risk processing".'
author: matematicsolutions
author_url: https://github.com/matematicsolutions/awesome-matematic-skills-en/tree/main/data-protection/skills/gdpr-dpia-en
license: MIT
version: 0.1.1
execution_mode: open
jurisdiction: eu
practice: data-protection
language: en
---

# GDPR DPIA EN - Data Protection Impact Assessment (Art. 35-36)

## Philosophy

A DPIA is not a checkbox - it is a process for managing risk to the rights and freedoms of natural
persons. This skill runs the process and produces a **draft**; the residual-risk acceptance and the
go/no-go decision belong to the controller.

## Step 1 - Is a DPIA REQUIRED (Art. 35(1) threshold)

Mandatory where processing is **likely to result in a high risk**. Three routes:

1. **Supervisory authority's mandatory list** (Art. 35(4)) - each EU SA publishes a list of
   operations always requiring a DPIA. Check the relevant national list.
2. **EDPB's 9 criteria (WP248)** - rule of thumb: **>=2 criteria met => DPIA**. Criteria:
   evaluation/scoring, automated decisions with significant effect (Art. 22), systematic monitoring,
   sensitive/highly personal data, large-scale data, matching/combining datasets, vulnerable data
   subjects (children, employees), innovative technology (AI, IoT), preventing exercise of a right
   or use of a service.
3. **Art. 35(3)** - explicit cases: systematic and extensive evaluation (profiling), large-scale
   special-category/criminal data, large-scale systematic monitoring of public areas.

Output: `dpia_required: yes/no/recommended` + per-criterion justification.

## Step 2 - DPIA structure (Art. 35(7) minimum)

Four pillars:
- **(a) Systematic description** of the processing and its purposes (incl. legitimate interest if relied on).
- **(b) Necessity and proportionality** assessment against the purposes (minimisation, legal basis,
  purpose limitation, retention, data-subject rights, transfers).
- **(c) Risk assessment** to rights and freedoms (risk sources, confidentiality/integrity/
  availability scenarios; likelihood x severity).
- **(d) Measures** to address the risks and demonstrate compliance + residual risk.

Record the DPO's advice (Art. 35(2)) and any consultation with data subjects (Art. 35(9)).

## Step 3 - Prior consultation (Art. 36)

If **residual risk remains HIGH despite measures**, the controller MUST consult the supervisory
authority BEFORE processing. The skill drafts the consultation request (scope per Art. 36(3)) - but
a human files it (governance boundary).

## Tool - threshold screening (deterministic, offline)

Screen whether a DPIA is required with the script instead of judging by feel (zero dependencies, offline):

```bash
python scripts/dpia_screening.py --criteria evaluation,sensitive,largescale
python scripts/dpia_screening.py --mandatory public_monitoring
```

Returns a `verdict` (required / recommended / not_required) per the EDPB ">=2" rule and the Art. 35(3) cases. Screening only, not a clearance - the controller documents the decision.

## Governance boundary

Skill: drafts the DPIA, classifies criteria, prepares the consultation request. Human: approves the
risk assessment, decides on deployment, signs and files. The outward act (filing with the SA) is
never automatic.

## Companion

Records & processor contracts: [[gdpr-ropa-dpa-en]]. Polish parity: `rodo-dpia-pl`.

<!-- shared-rules:begin (generated from ../../SHARED-RULES.md by scripts/shared-rules-sync.py - do not edit here) -->
## Shared rules of the data-protection plugin (Data protection)

These rules apply to every skill in this plugin, including where the skill itself is silent. They are copied into each skill, so they hold whether you install the whole plugin or a single skill.

These skills run GDPR operations for controllers, law firms and DPOs: impact assessments, breach response, data subject rights, records of processing and processor-contract review. Each ends in a draft for decision, not a finished act.

### Rules

- **Output is a draft for decision.** A DPIA, a breach notification, a DSAR response, a register or a contract redline is a starting point for the controller / DPO. A person approves and executes it.
- **Governance boundary - the outward act stays human.** Filing with the supervisory authority, sending a breach notification, sending a DSAR response, erasing or exporting data, signing a contract - the skill prepares the draft, it does not perform the act.
- **No guessing on risk.** A risk assessment (DPIA, breach) needs inputs; a missing input is a gap to fill, not a field to guess.
- **Not legal advice.** The skills organise GDPR obligations and map them to articles; they do not replace legal analysis of a specific matter.
- **Confidentiality.** Treat the data of a real organisation and of data subjects as confidential - do not move it outside the agreed flow. These skills add no outbound channel of their own; what reaches your model is decided by your configuration (see https://github.com/matematicsolutions/awesome-matematic-skills-en/blob/main/TRUST.md).

### Plugin scope

Operational GDPR tooling (DPIA, breach, DSAR, RoPA/DPA). It does not verify citations or fetch sources of law - use `verification-foundation` and `eu-law-sources` for that. The DPA redline pairs with `clause-checklist-en` (verification-foundation).
<!-- shared-rules:end -->

---
name: gdpr-breach-72h-en-matematicsolutions
title: GDPR Breach 72h EN - personal data breach response (Art. 33-34)
description: 'Personal data breach response assistant grounded in GDPR Art. 33-34, EDPB Guidelines 9/2022 on breach notification, and national supervisory-authority breach forms. Runs the decision tree: (1) is it a breach and which type (confidentiality/integrity/availability), (2) risk assessment to rights and freedoms, (3) notify the SA within 72h (Art. 33) - with a deadline counter from awareness, (4) communicate to data subjects (Art. 34, "high risk") + exemptions, (5) internal breach register entry (Art. 33(5)). Drafts the notification and communications - it does NOT send to the SA or to data subjects (human acts). Adds no connectors and makes no outbound calls of its own; the incident details you paste still go to the model you have configured. Use when: "data leak", "GDPR breach", "72-hour notification", "do we notify individuals", "Art. 33", "breach response".'
author: matematicsolutions
author_url: https://github.com/matematicsolutions/awesome-matematic-skills-en/tree/main/data-protection/skills/gdpr-breach-72h-en
license: MIT
version: 0.1.1
execution_mode: open
jurisdiction: eu
practice: data-protection
language: en
---

# GDPR Breach 72h EN - personal data breach response (Art. 33-34)

## Philosophy

In a breach, the clock and the documented reasoning are what matter. This skill runs a **documented**
decision tree and produces drafts; the **decision to notify and the act of sending belong to the
controller/DPO**. No guessing - missing inputs for the risk assessment are flagged as gaps, not filled.

## Step 1 - Is it a breach, and which type

A breach is a breach of security leading to accidental or unlawful destruction, loss, alteration,
unauthorised disclosure of, or access to personal data (Art. 4(12)). Classify: **confidentiality**
(disclosure/access), **integrity** (alteration), **availability** (loss/destruction). Often combined.

## Step 2 - Risk assessment to rights and freedoms

Factors (EDPB 9/2022, formerly WP250): type of breach, nature/sensitivity/volume of data, ease of
identification, severity of consequences (identity theft, financial loss, discrimination, reputational
harm), special characteristics of individuals (children, patients), number of individuals affected.
Output: `risk: none / present / high`.

## Step 3 - Notify the SA (Art. 33) - 72h COUNTER

- **The clock starts on AWARENESS** of the breach (not the event). Deadline: **72 hours**.
- Notify **unless** the breach is **unlikely to result in a risk** to rights and freedoms (Art. 33(1)).
  No notification => justify and document.
- **After the deadline** => notify with reasons for the delay (Art. 33(1) sentence 2).
- Notification content (Art. 33(3)): nature of the breach (categories and approximate numbers of
  data subjects and records), DPO contact, likely consequences, measures taken/proposed. **Phased
  notification** is allowed (Art. 33(4)).
- The skill computes `deadline_72h` (date+time) and drafts to the SA form's fields.

## Step 4 - Communicate to data subjects (Art. 34)

If **high risk** => communicate to individuals **without undue delay**, in clear and plain language
(Art. 34(2): description, DPO, consequences, measures). **Exemptions** (Art. 34(3)): appropriate
safeguards (e.g. encryption rendering data unintelligible), subsequent measures eliminating the high
risk, or disproportionate effort => public communication instead.

## Step 5 - Breach register (Art. 33(5))

Record EVERY breach (even unreported ones) in the internal register: facts, effects, remedial action.
This is the accountability evidence for the SA.

## Tool - deadline calculator (deterministic, offline)

Do not count the 72h in your head. Use the script (zero dependencies, offline):

```bash
python scripts/gdpr_deadlines.py breach --from "2026-06-30T14:30"
```

Returns `deadline_72h` (ISO 8601) counted from awareness. Paste the result into the draft and register.

## Governance boundary

Skill: decision tree, 72h counter, draft notification and communications, register entry. Human:
approves the risk assessment, sends the SA notification and the individual communications. Sending is
never automatic.

## Companion

Impact assessment: [[gdpr-dpia-en]]. Polish parity: `rodo-naruszenie-72h-pl`.

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

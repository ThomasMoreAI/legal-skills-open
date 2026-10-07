---
name: gdpr-dsar-en-matematicsolutions
title: GDPR DSAR EN - data subject rights requests (Art. 12, 15-22)
description: 'Data subject rights request (DSAR) assistant grounded in GDPR Art. 12 and 15-22. Identifies the request type (access 15, rectification 16, erasure 17, restriction 18, portability 20, objection 21, automated decisions 22), tracks the DEADLINE (one month from receipt, Art. 12(3); +2 months if complex), gates exemptions and refusal grounds (e.g. Art. 17(3), manifestly unfounded/excessive requests - Art. 12(5)), and drafts the response + a request register. Identity verification of the requester (Art. 12(6)) comes first. It does NOT send responses or erase data (human acts). The skill itself adds no connectors and makes no outbound calls; the text you put in front of it still reaches whatever model you have configured, so keep the request file out of the prompt or point the agent at a local model. Use when: "subject access request", "erasure request", "right to be forgotten", "objection", "DSAR deadline", "data portability".'
author: matematicsolutions
author_url: https://github.com/matematicsolutions/awesome-matematic-skills-en/tree/main/data-protection/skills/gdpr-dsar-en
license: MIT
version: 0.1.1
execution_mode: open
jurisdiction: eu
practice: data-protection
language: en
---

# GDPR DSAR EN - data subject rights requests (Art. 12, 15-22)

## Philosophy

A rights request is a clock plus a legal assessment, not an automation. The skill classifies, tracks
the deadline and produces a **draft**; the fulfil/refuse decision and the act of sending belong to the
controller. Erasure/export is irreversible/outward => always a human (governance boundary).

## Step 0 - Identity and deadline

- **Identity verification** (Art. 12(6)) - where reasonable doubt exists, request further information.
  This does NOT pause the clock unconditionally: per EDPB Guidelines 01/2022 the deadline may be
  suspended **only** where the information is necessary to confirm identity AND the controller asked
  for it without undue delay. Preserve the original receipt date in the register - a late or
  disproportionate identity request does not extend the deadline, and verification must not obstruct.
- **DEADLINE: one month from receipt** (Art. 12(3)). Extension of **up to 2 months** for complexity/
  number of requests - inform within the first month with the reason. The skill computes `deadline`
  and `deadline_extended`.
- **Free of charge by default** (Art. 12(5)). A fee or refusal is allowed only where the request is
  **manifestly unfounded or excessive** - the burden of proof is on the controller.

## Step 1 - Classify the right

| Art. | Right | Key |
|---|---|---|
| 15 | Access + copy | scope of information, copy of data, third-party rights |
| 16 | Rectification | inaccurate/incomplete data |
| 17 | Erasure ("forgotten") | grounds in (1) vs **exemptions in (3)** (legal obligation, claims, freedom of expression) |
| 18 | Restriction | "freeze" instead of erasure |
| 20 | Portability | consent/contract + automated processing only; structured format |
| 21 | Objection | legitimate interest / direct marketing (marketing = absolute) |
| 22 | Automated decisions | primary right = **not to be subject** to a solely automated decision with legal/similarly significant effects; 22(2) exceptions (contract, law, explicit consent) => 22(3) safeguards: human intervention, own view, contest |

## Step 2 - Gates and refusal grounds

Check right-specific exemptions (especially Art. 17(3) and national restrictions). **Legally justify**
every refusal + inform of the right to lodge a complaint with the SA and a judicial remedy (Art. 12(4)).

## Step 3 - Draft response + register

The skill drafts the response (plain language, Art. 12(1)), tailored to the right invoked. For Art. 15
that means a **copy of the personal data retrieved from the operational systems** that hold it, plus
available source information (Art. 15(1)(g)) - the RoPA ([[gdpr-ropa-dpa-en]]) supplies only the general
processing information (purposes, categories, recipients), not the person's data itself. Plus a register
entry (receipt date, type, deadline, outcome).

## Tool - deadline calculator (deterministic, offline)

Do not compute the one-month deadline by hand - month arithmetic has traps (receipt 31 Jan => ends 28/29 Feb, per Regulation (EEC) No 1182/71). Use the script (zero dependencies, offline):

```bash
python scripts/gdpr_deadlines.py dsar --from 2026-01-31 --extend
```

Returns `deadline_1_month` and (with `--extend`) `deadline_extended_3_months`. Paste the result into the response and register.

## Governance boundary

Skill: classifies, computes deadlines, drafts, maintains the register. Human: verifies identity,
decides fulfil/refuse, **performs the erasure/export**, sends the response. Irreversible and outward
acts are never automatic.

## Companion

Records of processing (where the data is): [[gdpr-ropa-dpa-en]]. Polish parity: `rodo-dsar-pl`.

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

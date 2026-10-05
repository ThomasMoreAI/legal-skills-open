---
name: gdpr-dsgvo-expert-aashutosh396
title: GDPR / DSGVO Expert
description: Use when running a GDPR or German DSGVO/BDSG privacy assessment — scanning code for privacy risks, deciding/generating a DPIA, tracking data-subject-rights (DSAR) deadlines, picking lawful bases, and German-specific rules. Final calls route to the DPO/counsel.
author: aashutosh396
author_url: https://github.com/aashutosh396/mindpalace/tree/main/mindpalace/skills/global/compliance/gdpr-dsgvo-expert
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: data-protection
language: en
tags: [gdpr, dsgvo, bdsg, dpia, dsar, data-subject-rights, privacy, lawful-basis, breach-notification, schrems]
---

# GDPR / DSGVO Expert

EU GDPR and German BDSG compliance method. Final compliance determinations route to the DPO or legal counsel.

## Workflow 1 — New processing activity

1. Scan codebase for privacy risks — detect personal-data patterns (email, phone, IP), special-category data (health, biometric, religion), financial data (cards, IBAN), and risky patterns (logging PII, missing consent, indefinite retention, unencrypted sensitive data, disabled deletion). Produce a 0-100 score + risk tiers + GDPR-article-referenced recommendations.
2. Review findings; address critical + high.
3. Determine if a DPIA is required (threshold below).
4. If required, generate the DPIA (Art. 35 elements).
5. Record in the Art. 30 register of processing activities.

## DPIA threshold (Art. 35)

Required for high-risk processing. Triggers: systematic monitoring (35(3)(c)), large-scale special-category data (35(3)(b)), automated decision-making (35(3)(a)), or EDPB high-risk criteria (WP248 rev.01 — ≥2 of: evaluation/scoring, automated decisions with legal effect, systematic monitoring, sensitive data, large scale, matching/combining datasets, vulnerable subjects, innovative tech, prevents rights). DPIA covers: systematic description of processing, necessity + proportionality, risks to rights/freedoms, mitigation measures. Consult DPO (35(2)); Art. 36 prior consultation if residual high risk.

## Workflow 2 — Data-subject request (DSAR)

Log → verify identity (proportionate measures) → gather data from systems → generate response → send + close → monitor compliance. All rights fulfilled within **one calendar month of receipt** (Art. 12(3)); extendable by **two further months** for complex/numerous requests if the subject is informed (with reasons) within the first month.

| Right | Article |
|---|---|
| Access | 15 | Rectification | 16 | Erasure | 17 |
| Restriction | 18 | Portability | 20 | Objection | 21 | Automated decisions | 22 |

## Lawful bases (Art. 6) — pick ONE per purpose

Consent (marketing, analytics — freely given, specific, informed; record per Art. 7 + withdrawal), Contract (order fulfillment), Legal obligation (tax, employment), Legitimate interests (fraud prevention, security — requires documented balancing test/LIA). Special categories (Art. 9 — health, biometric, racial/ethnic, political, religious, union, genetic, sexual orientation) need explicit consent or an Art. 9(2) exception.

## Other key areas

Breach: log ALL breaches per Art. 33(5); Art. 33 DPA notification within 72h where required; Art. 34 data-subject notification where high risk. Transfers (Schrems II): adequacy decision OR SCCs (Art. 46) OR derogation (Art. 49) + Transfer Impact Assessment per EDPB Recs 01/02-2020 + supplementary measures; US covered by EU-US Data Privacy Framework adequacy (Jul 2023 — verify certified entities). Processors: contracts carry all Art. 28(3)(a)-(j) clauses.

## German BDSG additions

| Topic | BDSG § | Requirement |
|---|---|---|
| DPO threshold | 38 | 20+ employees processing personal data automatically → mandatory DPO |
| Employment | 26 | Detailed employee-data rules; works-council co-determination |
| Video surveillance | 4 | Signage + proportionality + limited retention |
| Credit scoring | 31 | Explainable algorithms |

BDSG check: DPO required? (20+ employees auto-processing OR DPIA needed OR data transfer/market research) → if employees, document §26 legal basis + works-council reqs → if video, comply §4 → register DPO with supervisory authority.

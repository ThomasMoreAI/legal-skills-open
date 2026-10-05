---
name: gdpr-audit-prep-aashutosh396
title: GDPR Audit Prep — Forcing Questions
description: Use before an annual internal GDPR review, post-breach audit, DPA-investigation readiness, or acquisition due diligence — six Article-cited forcing questions on RoPA, lawful basis, DPIA, DSAR timing, international transfers, and breach logging.
author: aashutosh396
author_url: https://github.com/aashutosh396/mindpalace/tree/main/mindpalace/skills/global/compliance/gdpr-audit-prep
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: data-protection
language: en
tags: [gdpr, dpo, ropa, article-30, dpia, dsar, schrems-ii, breach-notification, lawful-basis, audit-readiness]
---

# GDPR Audit Prep — Forcing Questions

Six Article-cited questions before any internal audit, breach response, DPA investigation, or acquisition due diligence. Every finding cites Article + paragraph; no paraphrase.

## The six questions

1. **Show the Article 30 RoPA — with last-updated date.** (Most-cited.) All Art. 30(1)(a)-(g) for controllers, all 30(2)(a)-(d) for processors. Updated within ~90 days of changes. Joint-controller arrangements per Art. 26.
2. **For this activity, what's the lawful basis under Article 6?** Art. 6 is exclusive — pick ONE per purpose (consent / contract / legal obligation / vital interests / public task / legitimate interests). Legitimate interests → documented LIA. Consent → Art. 7 records + withdrawal. Special categories (Art. 9) → an Art. 9(2) exception.
3. **For high-risk processing, where's the DPIA per Article 35?** Sample 3-5 activities. Art. 35(7)(a)-(d): systematic description, necessity + proportionality, risks to rights/freedoms, mitigation. DPO consulted (35(2)); Art. 36 prior consultation for residual high risk. AI systems integrate EU AI Act Art. 27 FRIA.
4. **Show a DSAR from the last 30 days — and its response timing.** Articles 15-22. Within 1 month (Art. 12(3)); extension up to 2 months for complex. Identity verification documented. Access response includes all Art. 15 info. Erasure (Art. 17) covers backups + processors.
5. **Transfer Impact Assessments for the largest non-EU transfers.** Schrems II. Adequacy OR SCCs (Art. 46) OR derogation (Art. 49). TIA per EDPB Recs 01/02-2020 + supplementary measures. US transfers under EU-US Data Privacy Framework adequacy (Jul 2023) — verify certified entities.
6. **Show the breach log per Article 33(5) — ALL breaches, not just notifiable.** Internal detection documented, Art. 33 DPA notification within 72h where required, Art. 34 data-subject notification where high risk, root cause + corrective action via CAPA. Cross-check A.5.24-27 incident management.

## Output

Decision (RoPA-refresh / DPIA-required / DSAR-workflow / transfer-risk / breach-followup / DPA-readiness) → Art. 30 RoPA status → Art. 6 lawful-basis discipline (LIA gaps, Art. 9 exceptions) → Art. 35 DPIA quality → DSR (Art. 12-22, avg response ≤30 days, erasure flow) → Art. 28 processor management (28(3)(a)-(j) clauses %) → Schrems II transfer status (mechanism per transfer, TIA, supplementary measures) → Art. 33-34 breach discipline → cross-framework (ISO 27001 Art. 32, EU AI Act FRIA, SOC 2 Privacy TSC) → verdict 🟢 DPA-READY / 🟡 GAPS / 🔴 NOT-READY → top 3 actions → outside-counsel flags (Schrems II supplementary-measure adequacy, AI-Act↔GDPR interaction, novel DPA enforcement).

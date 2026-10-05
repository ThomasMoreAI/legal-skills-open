---
name: ai-act-readiness-aashutosh396
title: EU AI Act Readiness — Forcing Questions
description: Use during AI-system intake, before EU market placement, before signing the EU declaration of conformity, or during annual compliance refresh — six Article-cited forcing questions covering prohibited practices, high-risk classification, conformity route, role, transparency, and GPAI.
author: aashutosh396
author_url: https://github.com/aashutosh396/mindpalace/tree/main/mindpalace/skills/global/compliance/ai-act-readiness
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: regulatory
language: en
tags: [eu-ai-act, ai-compliance, high-risk-ai, conformity-assessment, gpai, prohibited-ai, transparency, annex-iii, article-50, ai-governance]
---

# EU AI Act Readiness — Forcing Questions

Six Article-cited questions before any EU placement, conformity assessment, or annual refresh. Phasing dates: 2025-02-02 / 2025-08-02 / 2026-08-02 / 2027-08-02. Run also when the company role changes (deployer → provider via Art. 25(1) substantial modification) or training compute approaches 10^25 FLOPs (Art. 51).

## The six questions

1. **Article 5 — prohibited practice?** Penalty up to €35M or 7% worldwide turnover. 8 categories: subliminal manipulation, exploitation of vulnerabilities, social scoring, predictive policing, untargeted facial scraping, emotion recognition in workplace/education, biometric categorisation by sensitive attributes, real-time public biometric ID by law enforcement. If yes → STOP, cannot place on EU market (outside Art. 5(2) carve-outs).
2. **Article 6 + Annex III — high-risk?** 8 categories: biometrics, critical infrastructure, education, employment, essential services, law enforcement, migration, justice. Art. 6(3)(a)-(d) carve-out applies only with no profiling of natural persons — profiling overrides the carve-out.
3. **Article 43 — Module A or H?** Biometrics → Module H (notified body) by default. Module A (Annex VI): internal control with presumption of conformity if Art. 40 harmonised standards applied. Module H (Annex VII): full QMS + notified body where standards lack. Annex IV technical documentation: 8 items before placing on market.
4. **Article 25 — what role?** Provider (3(3)) heaviest — full Title III + Art. 73 reporting; Deployer (3(4)) — Art. 26 + Art. 27 FRIA if public sector; Importer (3(6)) — Art. 23; Distributor (3(7)) — Art. 24; non-EU providers appoint an authorized rep (Art. 22). Substantial modification turns a deployer into a provider.
5. **Article 50 — transparency satisfied?** (in force 2 Aug 2025) 50(1) disclose AI interaction (chatbots); 50(2) mark synthetic content; 50(3) disclose emotion recognition / biometric categorisation; 50(4) disclose deepfakes (image/audio/video).
6. **Articles 51-55 — GPAI? Systemic risk?** GPAI definition Art. 3(63). Systemic-risk presumption at ≥10^25 FLOPs training compute (Art. 51). All GPAI (Art. 53): Annex XI docs, Annex XII downstream info, copyright policy, training-data summary. Systemic-risk GPAI (Art. 55): model evaluations, adversarial testing, incident reporting, cybersecurity. Non-EU GPAI appoint authorized rep (Art. 54).

## Output

Every verdict cites the Article. Decision (classify / conformity-route / obligation-scope / annual-refresh) → risk classification (tier + Article + Annex + GPAI? + systemic-risk?) → conformity assessment if high-risk (module + Art. 43 + notified body? + Annex IV status) → obligation matrix by deadline phase → transparency (50(1)-(4)) → cross-framework reuse (ISO 42001→Art. 17 QMS, ISO 27001→Art. 15 cybersecurity, GDPR DPIA→Art. 27 FRIA) → verdict 🟢 READY-FOR-EU / 🟡 GAPS / 🔴 NOT-READY / 🚫 PROHIBITED → top 3 actions → legal-review flags (novel cases, GPAI threshold disputes, Art. 5 boundary, Art. 25 substantial-modification).

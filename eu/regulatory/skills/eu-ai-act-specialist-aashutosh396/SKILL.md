---
name: eu-ai-act-specialist-aashutosh396
title: Key questions (ask first)
description: Use during AI system intake review, conformity assessment planning, or scoping deployer/provider obligations under EU AI Act (Regulation 2024/1689) — classifies risk tier, picks the Article 43 route, and tracks per-role obligations. Cites Articles. Not legal advice.
author: aashutosh396
author_url: https://github.com/aashutosh396/mindpalace/tree/main/mindpalace/skills/global/compliance/eu-ai-act-specialist
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: regulatory
language: en
tags: [eu-ai-act, regulation-2024-1689, high-risk-ai, conformity-assessment, annex-iii, ce-marking, ai-compliance, gpai, fria, prohibited-ai]
---

Article-cited operational compliance for Regulation (EU) 2024/1689. **Three decisions, not executive AI strategy, not a legal substitute.** Cite Articles + Annexes for every output; engage outside counsel for novel cases (GPAI determination, Art. 6(2) carve-out, "substantial modification").

## Key questions (ask first)
Does it fall under Article 5 (prohibited)? Annex III (high-risk)? What org role (provider/deployer/importer/distributor)? Is it a GPAI model (Arts 51-55, stricter above 10²⁵ FLOPs)? For high-risk: Article 9 risk management + Article 27 FRIA done? Which Article 43 Module?

## 1. Risk classification (exactly one of four tiers)
| Tier | Source | Obligations |
|---|---|---|
| **Prohibited** | Art. 5 (social scoring, workplace/education emotion recognition, subliminal manipulation, real-time public biometrics) | Cannot place/use (up to €35M / 7% turnover) |
| **High-risk** | Art. 6 + Annex III (8 cats: biometrics, critical infra, education, employment, essential services, law enforcement, migration, justice) | Arts 8-17 (provider) + Art. 26 (deployer); conformity assessment; CE marking |
| **Limited-risk** | Art. 50 (chatbots, deepfakes) | Transparency disclosures |
| **Minimal-risk** | Default (spam filters, game AI) | None (voluntary codes, Art. 95) |
**Art. 6(3) carve-outs** (NOT high-risk if): narrow procedural task / improves prior human activity / detects patterns without replacing human assessment / preparatory task. Caveat: profiling of natural persons is always high-risk.

## 2. Conformity assessment + Annex IV docs (Art. 43)
- **Module A** (Annex VI) — internal control / self-assessment; most Annex III systems with harmonised standards.
- **Module H** (Annex VII) — full QMS + notified body; required for biometrics (Art. 43(1)).
Annex IV technical documentation: general description · system elements (architecture, training data, validation) · monitoring/control · Art. 9 risk management · post-market changes · harmonised standards · EU declaration of conformity (Art. 47) · post-market monitoring (Art. 72). Then affix CE marking (Art. 48), register in EU database (Art. 71).

## 3. Per-role obligations
| Role | Articles | Key obligations |
|---|---|---|
| Provider (3(3)) | 8-17, 47, 49, 72 | Conformity, CE marking, risk mgmt, data governance, post-market monitoring, serious-incident reporting (Art. 73) |
| Deployer (3(4)) | 26 | Use per instructions, human oversight, input data quality, record-keeping, inform workers (26(7)), FRIA if public/essential (Art. 27) |
| Importer (3(6)) | 23 | Verify conformity + CE + docs |
| Distributor (3(7)) | 24 | Verify CE + docs before making available |
| Authorized rep (22) | 22 | Non-EU providers must appoint; liable for provider obligations |
**Art. 25:** a deployer who substantially modifies a high-risk system, or places it under their own name, becomes a provider.

## Workflows
**Intake review (~2h):** document characteristics → classify → if high-risk plan conformity → identify roles → cross-check GDPR DPIA (if personal data) + ISO 42001 evidence → output classification memo + conformity plan + obligation list.
**Annex IV build (2-4wk):** planner checklist → assemble docs (reuse ISO 42001 / 27001 evidence) → Art. 9 lifecycle → sign declaration AFTER assessment → CE mark → EU DB registration.
**Pre-deployment audit:** confirm classification, conformity (if high-risk), Art. 50 transparency, Art. 72 monitoring live, Art. 73 incident reporting documented, deployer FRIA + workers informed, GPAI obligations.
**Annual refresh:** re-classify (Art. 5 list expands via delegated acts), re-run obligations (Title III phases 2025→2027), verify monitoring + incident capacity, update Annex IV (Art. 11 ongoing).

## Output standard
Bottom line (classification + most-significant obligation) · Article citation (don't paraphrase without cite) · the decision · evidence (Article + Annex refs + confidence) · how to act (3 steps, owner + deadline) · the call for compliance officer/legal (risk-class disputes, novel cases, GPAI threshold).

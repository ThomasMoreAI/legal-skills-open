---
name: ai-act-compliance
title: AI Act Compliance
description: Supports compliance with the EU Artificial Intelligence Act (Regulation (EU) 2024/1689). Use when the user needs to classify an AI system under the AI Act risk categories (prohibited, high-risk, limited, minimal, GPAI), check provider or deployer obligations for high-risk systems, evaluate GPAI model obligations including systemic risk thresholds, verify transparency obligations under Article 50, or run a fundamental rights impact assessment (FRIA) under Article 27. Target users are AI system providers, deployers, importers, distributors, EU consultants on AI compliance, and engineers building AI products for the EU market.
author: morellid
author_url: https://github.com/morellid/ai-act-skill
license: MIT
version: 0.1.1
execution_mode: open
jurisdiction: eu
practice: regulatory
language: en
sources:
- title: Ai Act Annex Iii High Risk List
  path: references/extracts/ai-act-annex-iii-high-risk-list.md
- title: Ai Act Art 26 27 Deployer Fria
  path: references/extracts/ai-act-art-26-27-deployer-fria.md
- title: Ai Act Art 3 Definitions
  path: references/extracts/ai-act-art-3-definitions.md
- title: Ai Act Art 5 Prohibited
  path: references/extracts/ai-act-art-5-prohibited.md
- title: Ai Act Art 50 Transparency
  path: references/extracts/ai-act-art-50-transparency.md
- title: Ai Act Art 51 55 Gpai
  path: references/extracts/ai-act-art-51-55-gpai.md
- title: Ai Act Art 6 9 High Risk Classification
  path: references/extracts/ai-act-art-6-9-high-risk-classification.md
- title: Ec Art50 Transparency Guidelines
  path: references/extracts/ec-art50-transparency-guidelines.md
---

# AI Act Compliance

EU Regulation 2024/1689 — practical compliance support for AI providers, deployers, and consultants.

## When to use this skill

Use when someone needs to:

- Classify an AI system or model under the AI Act (in scope? prohibited? high-risk? limited risk? minimal? GPAI? GPAI with systemic risk?)
- Identify the role(s) the organisation plays (provider, deployer, importer, distributor)
- Check obligations applicable to a high-risk system as **provider** (Articles 8–22)
- Check obligations applicable to a high-risk system as **deployer** (Articles 26–27, including FRIA)
- Check obligations applicable to a **GPAI model** provider (Articles 51–55)
- Verify **transparency obligations** under Article 50 (chatbots, synthetic content, emotion recognition, biometric categorisation, deepfakes)
- Map applicable **dates of application** for the specific system or role

**Do not use** when the user asks for:

- Legal advice on a specific case (this needs an EU AI lawyer with case-specific knowledge)
- Pre-existing legal opinions on national implementation in a specific Member State (rules will be added by national supervisory authorities; not yet finalised in many countries as of 2026)
- Drafting of EU-AI-Act-conformity declarations (CE marking) — the skill structures the documentation but does not produce the final signed document
- Compliance with sector-specific regimes that interact with the AI Act (e.g., Medical Devices Regulation, automotive type-approval) — these need dedicated skills

## Disclaimer

This skill is a support tool for compliance work, not a substitute for qualified legal or technical counsel. The AI Act is recent legislation with phased application (obligations phased between 2 February 2025 and 2 August 2028) and the harmonised standards under preparation by CEN-CENELEC JTC 21 are not yet published. **Outputs require review by competent counsel and, for high-risk systems, by a notified body where applicable.** Penalties under Article 99 reach EUR 35 million or 7% of total worldwide annual turnover for prohibited-practice violations.

**In force: Digital Omnibus on AI — Regulation (EU) 2026/1744.** Published in the OJ on 24 July 2026, in force since 27 July 2026. It: (i) defers the **Chapter III high-risk** dates to **2 December 2027** (Annex III stand-alone systems) and **2 August 2028** (Annex I embedded safety components); (ii) adds new Article 5(1) points **(ba)** and **(bb)** prohibiting AI systems generating non-consensual intimate imagery ("nudifier apps") and CSAM, applicable from **2 December 2026** (see Art. 5(1a): safeguards are relevant only where the prohibited output is a foreseeable outcome, not where it is the intended purpose); (iii) narrows the "safety component" definition in Art. 3(14); (iv) extends SME simplifications to small mid-cap enterprises; (v) centralises GPAI enforcement in the EU AI Office.

**Article 50 was NOT deferred.** Transparency obligations under Article 50 have applied since **2 August 2026** and are enforceable now. The only relief is a targeted transitional period for the **Art. 50(2) marking and detection** duty: generative AI systems placed on the market or put into service before 2 August 2026 have until **2 December 2026** to comply. The Art. 50(1) disclosure duty applies from 2 August 2026 with no transitional period. Confirmed by the Commission's Article 50 Guidelines, C(2026) 5054 final, points 2 and 153.

## Sub-tasks

Based on the user's request, load the relevant task file:

- **System classification**: user asks "is my system in scope? what category? am I a provider or deployer?" — read [`tasks/classify-system.md`](tasks/classify-system.md). **Always start here unless classification is already established.**
- **Prohibited practices check**: user wants to verify no Article 5 prohibition is triggered — read [`tasks/check-prohibited-practices.md`](tasks/check-prohibited-practices.md)
- **High-risk provider obligations**: classified high-risk + role is provider — read [`tasks/check-high-risk-provider.md`](tasks/check-high-risk-provider.md)
- **High-risk deployer obligations**: classified high-risk + role is deployer (incl. FRIA) — read [`tasks/check-deployer-obligations.md`](tasks/check-deployer-obligations.md)
- **GPAI provider obligations**: providing a general-purpose AI model — read [`tasks/check-gpai-provider.md`](tasks/check-gpai-provider.md)
- **Transparency obligations (Article 50)**: any AI system interacting with humans / generating synthetic content — read [`tasks/check-transparency.md`](tasks/check-transparency.md)

If the request is generic ("help me with the AI Act"), start with classification.

## General process

1. Identify the user's role(s) and system(s).
2. Run classification first (`classify-system.md`) unless explicitly stated.
3. Based on classification, route to the relevant obligations task.
4. For each obligation, capture: applicable? met? gap analysis? remediation steps?
5. Always include applicable dates of application, as amended by Reg. (EU) 2026/1744: prohibitions and AI literacy **2 February 2025**; GPAI, penalties and governance **2 August 2025**; **Article 50 transparency 2 August 2026 (in force)**; new Art. 5(1)(ba)/(bb) NCII and CSAM prohibitions **2 December 2026**; high-risk Annex III **2 December 2027**; high-risk Annex I embedded **2 August 2028**. Never present Article 50 as deferred. If the system might fall under the new prohibition on non-consensual intimate imagery / CSAM, flag the 2 December 2026 deadline.
6. Conclude with the appropriate disclaimer and a call to legal review.

## Sources

Authoritative references in [`references/sources.yaml`](references/sources.yaml). Primary:

- **Regulation (EU) 2024/1689** (the AI Act) — Articles cited: 3, 5, 6, 9, 10, 14, 15, 16, 22, 26, 27, 50, 51, 53, 55, 99; Annex III
- **Regulation (EU) 2026/1744** (Digital Omnibus on AI, in force 27 July 2026) — amends the Art. 113 calendar and Article 5
- **Commission Guidelines on Article 50 transparency obligations** (C(2026) 5054 final, 20 July 2026) — the Commission's official interpretation of Article 50; **non-binding** (only the CJEU can interpret authoritatively). Extract in [`references/extracts/ec-art50-transparency-guidelines.md`](references/extracts/ec-art50-transparency-guidelines.md)
- **GPAI Code of Practice** (final version July 2025) — voluntary tool to demonstrate compliance with Article 53
- **Code of Practice on Transparency of AI-generated Content** (final 10 June 2026) — voluntary tool to demonstrate compliance with Article 50(2), (4) and (5)
- **Commission Guidelines on the scope of obligations for providers of GPAI models** (July 2025)
- **CEN-CENELEC JTC 21** — harmonised standards under preparation (track the published list at <https://digital-strategy.ec.europa.eu/en/policies/ai-act-standardisation>)

Pending (track, treat as indicative until finalised):

- **Commission draft guidelines on the classification of high-risk AI systems** (19 May 2026) — `sources.yaml` id `ec-high-risk-classification-guidelines-draft-2026`. Required by Article 96 AI Act. Targeted consultation closed 23 July 2026; final version expected Q3 2026, ahead of the 2 December 2027 Annex III date. Will become the Commission's official (non-binding) interpretation of Article 6 and Annex III (safety-component test, Annex III use-case examples, Art. 6(3) derogation) once final; promote to a primary source with a textual extract at that point.

Textual extracts of the cited articles in [`references/extracts/`](references/extracts/).

## Limits

This skill does NOT:

- Replace legal counsel or notified body conformity assessment.
- Produce signed conformity declarations or CE marking documentation ready for submission.
- Cover Member State-specific national implementing measures (e.g., national AI authorities' guidance, where relevant).
- Cover sector regimes interacting with the AI Act (medical devices, automotive type-approval, financial services AI use cases under existing sectoral regulation).
- Track post-2026 jurisprudence and Commission delegated/implementing acts in real time — the user must verify the date of last update of `references/sources.yaml`.
- Replicate the EU Commission's official Compliance Checker at the AI Act Service Desk (<https://ai-act-service-desk.ec.europa.eu/>) — for authoritative self-assessment, use that tool.

**Every output requires review by qualified counsel before adoption or filing.**

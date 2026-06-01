---
name: ai-act-compliance
title: AI Act Compliance
description: Supports compliance with the EU Artificial Intelligence Act (Regulation (EU) 2024/1689). Use when the user needs to classify an AI system under the AI Act risk categories (prohibited, high-risk, limited, minimal, GPAI), check provider or deployer obligations for high-risk systems, evaluate GPAI model obligations including systemic risk thresholds, verify transparency obligations under Article 50, or run a fundamental rights impact assessment (FRIA) under Article 27. Target users are AI system providers, deployers, importers, distributors, EU consultants on AI compliance, and engineers building AI products for the EU market.
author: morellid
author_url: https://github.com/morellid/ai-act-skill
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: regulatory
language: en
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

This skill is a support tool for compliance work, not a substitute for qualified legal or technical counsel. The AI Act is recent legislation with phased application (most obligations between 2 February 2025 and 2 August 2027) and the harmonised standards under preparation by CEN-CENELEC JTC 21 are not yet published. **Outputs require review by competent counsel and, for high-risk systems, by a notified body where applicable.** Penalties under Article 99 reach EUR 35 million or 7% of total worldwide annual turnover for prohibited-practice violations.

**Pending: Digital Omnibus on AI.** Provisional political agreement reached on **7 May 2026** between the European Parliament and the Council on the Commission's 19 November 2025 proposal. The agreement: (i) shifts high-risk obligations to **2 December 2027** (Annex III stand-alone systems and Article 50 transparency) and **2 August 2028** (Annex I embedded safety components); (ii) adds a new Article 5 prohibition on AI systems generating non-consensual intimate imagery ("nudifier apps") and CSAM, with **2 December 2026** compliance once in force; (iii) narrows the "safety component" definition (excludes assistive or performance-optimising AI from Annex I high-risk); (iv) extends SME exemptions to small mid-cap enterprises; (v) streamlines GPAI enforcement through the EU AI Office. Formal adoption and OJ publication are pending (co-legislator target: before 2 August 2026). Until OJ publication, the binding deadlines remain the original Article 113 calendar and the new Article 5 prohibition is not yet in force. Article 4 (AI literacy) and the existing Article 5 prohibitions — in force since 2 February 2025 — and Chapter V GPAI obligations — in force since 2 August 2025 — are not affected. Skill outputs should mention the pending change whenever 2 August 2026 high-risk or Article 50 deadlines are cited, and flag systems that may fall under the future nudifier/CSAM prohibition.

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
5. Always include applicable dates of application (the AI Act phases obligations; some rules already in force, others up to August 2027). Where the cited deadline is one that the **Digital Omnibus on AI** (provisional political agreement 7 May 2026, formal adoption pending) would shift — i.e., 2 August 2026 high-risk Annex III and Article 50 transparency, and 2 August 2027 Annex I embedded — flag the pending move to 2 December 2027 / 2 August 2028 in the output. If the system might fall under the agreed-but-not-yet-in-force prohibition on non-consensual intimate imagery / CSAM (compliance deadline 2 December 2026 once published in the OJ), flag that too.
6. Conclude with the appropriate disclaimer and a call to legal review.

## Sources

Authoritative references in [`references/sources.yaml`](references/sources.yaml). Primary:

- **Regulation (EU) 2024/1689** (the AI Act) — Articles cited: 3, 5, 6, 9, 10, 14, 15, 16, 22, 26, 27, 50, 51, 53, 55, 99; Annex III
- **GPAI Code of Practice** (final version July 2025) — voluntary tool to demonstrate compliance with Article 53
- **Commission Guidelines on the scope of obligations for providers of GPAI models** (July 2025)
- **CEN-CENELEC JTC 21** — harmonised standards under preparation (track the published list at <https://digital-strategy.ec.europa.eu/en/policies/ai-act-standardisation>)

Pending (track, treat as indicative until finalised):

- **Commission draft Article 50 transparency guidelines** (8 May 2026, public consultation until 3 June 2026) — `sources.yaml` id `ec-art50-transparency-guidelines-draft-2026`. Will become the authoritative Commission interpretation of Article 50 once final; promote to a primary source with a textual extract at that point.

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

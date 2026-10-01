---
name: ai-act-compliance-clemensjl
title: EU AI Act compliance
description: Use when working out what the EU AI Act requires of a specific product that contains an LLM or an ML model — classifying it, deciding whether the company is provider or deployer, writing the Art 50 disclosures, the technical documentation, the human-oversight design or the log-retention spec. Also use when a product starts generating synthetic text, images, audio or video, when a foundation model is fine-tuned or rebranded, when an AI feature touches hiring, credit, insurance, education, biometrics or essential services, or before an AI feature ships to EU users.
author: clemensjl
author_url: https://github.com/clemensjl/claude-skills/tree/main/skills/ai-act-compliance
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: regulatory
language: en
sources:
- title: Ai Literacy
  path: references/ai-literacy.md
- title: Artefacts Disclosures
  path: references/artefacts-disclosures.md
- title: Artefacts Records
  path: references/artefacts-records.md
- title: Checklist
  path: references/checklist.md
- title: Decision Tree
  path: references/decision-tree.md
- title: Deployer Duties
  path: references/deployer-duties.md
- title: Governance Enforcement
  path: references/governance-enforcement.md
- title: Gpai
  path: references/gpai.md
- title: High Risk Classification
  path: references/high-risk-classification.md
- title: High Risk Obligations
  path: references/high-risk-obligations.md
- title: Intake
  path: references/intake.md
- title: Prohibited Practices
  path: references/prohibited-practices.md
- title: Scope And Roles
  path: references/scope-and-roles.md
- title: Timeline
  path: references/timeline.md
- title: Transparency Art50
  path: references/transparency-art50.md
---

# EU AI Act compliance

Regulation (EU) 2024/1689 (AI Act, OJ L, 2024/1689, 12.7.2024), as amended by Regulation (EU) 2026/1744 (Digital Omnibus on AI, OJ L, 2026/1744, 24.7.2026, in force 27.07.2026). Adjacent: GDPR, DSA (Regulation (EU) 2022/2065), the Product Liability Directive recast (Directive (EU) 2024/2853), Directive (EU) 2019/790 Art 4(3). Status as at 2026-08-05.

**Core principle:** The AI Act is product-safety law, not data-protection law. Obligations attach to a **role** (provider, deployer, importer, distributor, authorised representative — Art 3(3) to (7)) applied to a **risk class** (prohibited, high-risk, transparency, minimal). One company can hold several roles at once, and per system, not per company. Most teams building on a foundation model are **deployers of a GPAI-based system** and land in the Art 50 transparency tier, not the high-risk regime. But putting your own name on a high-risk system, substantially modifying one, or changing the intended purpose of a non-high-risk system so that it becomes high-risk makes you the **provider** and shifts the whole obligation set onto you (Art 25(1)). Get the role wrong and everything downstream is wrong.

## Not legal advice

This skill produces drafts and findings, not legal advice. Before shipping:

- **Classification calls near the high-risk boundary need legal sign-off.** The Art 6(3) filter, the "profiling always means high-risk" rule, the safety-component test in Art 6(1a) to (1c) and the Annex III area boundaries are judgement calls with a EUR 15 000 000 / 3 % downside (Art 99(4)). A self-assessment that a system is not high-risk must be documented before placing on the market and registered under Art 49(2) (Art 6(4)) — that is a filed position, not an internal note.
- **The Commission guidelines on high-risk classification under Art 6(5) are still in draft.** Public consultation closed 23 July 2026. Do not cite draft guidelines as settled law.
- Anything touching prohibited practices (Art 5), biometrics, emotion recognition, or minors goes to a lawyer before it goes to a customer.
- Every generated artefact carries `<!-- DRAFT — not legally cleared -->` until sign-off is confirmed. Never remove the marker silently.

Never omit this section from the output and never soften it.

## Workflow

1. **Run the intake before writing anything.** Questions in `references/intake.md`. Unanswered questions become `[[MISSING: …]]`; never guess a value about the product, the stack or the company.
2. **Determine the role and the risk class** using `references/decision-tree.md`. Record the reasoning, not just the conclusion.
3. **Read the reference file for each applicable obligation before producing anything.** Article numbers and dates are too specific to recall.
4. **Produce the artefact** from `references/artefacts-records.md` or `references/artefacts-disclosures.md`.
5. **Run `references/checklist.md`** and report findings with article and location.

**Output shape.** Exactly four parts, in this order:

1. the artefact or finding, with the draft marker
2. the list of `[[MISSING: …]]` items the user must supply
3. adjacent open obligations in the same product, one sentence each
4. the sign-off note

The article sits next to the statement it supports. Reference-file paths are working material and belong in none of the four parts.

## Decision matrix

| Situation | What applies | Reference |
|---|---|---|
| Any AI feature, before anything else | Is it an AI system at all (Art 3(1)); is the company in scope (Art 2) | `scope-and-roles.md` |
| Company is unsure whether it is provider or deployer | Art 3(3), 3(4), Art 25(1) role flip | `scope-and-roles.md`, `decision-tree.md` |
| Product does emotion inference, social scoring, scraping faces, manipulation, or generates intimate/CSAM imagery | Art 5 prohibitions, incl. new points (ba), (bb) from 2 Dec 2026 | `prohibited-practices.md` |
| AI in hiring, credit, insurance pricing, education, essential services, biometrics, critical infrastructure | Annex III high-risk, Art 6(2), Art 6(3) filter | `high-risk-classification.md` |
| AI is a safety component of a CE-marked product | Annex I high-risk, Art 6(1) with Art 6(1a) to (1c) | `high-risk-classification.md` |
| Confirmed provider of a high-risk system | Art 9 to 15, 17, 43, 47, 48, 49, Annex IV | `high-risk-obligations.md` |
| Confirmed deployer of a high-risk system | Art 26; FRIA under Art 27 where applicable | `deployer-duties.md` |
| Chatbot, assistant, agent, or anything generating synthetic audio/image/video/text | Art 50(1) to (5) — the tier most products land in | `transparency-art50.md` |
| Company trains, fine-tunes or distributes a general-purpose AI model | Chapter V: Art 53 to 55, Annex XI, XII, XIII | `gpai.md` |
| Any provider or deployer of any AI system, no exceptions | Art 4 AI literacy | `ai-literacy.md` |
| Question about dates, grandfathering, "do we have to do this yet" | Art 113 as amended, Art 111 transitional rules | `timeline.md` |
| Fines, who enforces, overlap with a GDPR fine for the same conduct | Art 74, 75, 99, 101; GDPR Art 22; DSA; PLD recast | `governance-enforcement.md` |
| Need an inventory entry or a classification record | Templates | `artefacts-records.md` |
| Need a disclosure, an instructions-for-use summary, a model card, an oversight note or a log spec | Templates | `artefacts-disclosures.md` |
| Before shipping | Findings list | `checklist.md` |

## Hard rules

- **The high-risk dates moved. Do not use 2 August 2026 for high-risk obligations.** Art 113, third paragraph, point (c) as replaced by Reg (EU) 2026/1744 Art 1(40)(b): Chapter III Sections 1, 2 and 3 apply from **2 December 2027** for Annex III high-risk systems (Art 6(2)) and from **2 August 2028** for Annex I high-risk systems (Art 6(1)). The pre-omnibus dates of 2 August 2026 and 2 August 2027 are dead.
- **Art 50 transparency is already in force.** It applies from 2 August 2026 (Art 113, second paragraph — untouched by the omnibus). The only relief is Art 111(4), inserted by Reg (EU) 2026/1744 Art 1(39)(b): providers of systems generating synthetic audio, image, video or text **placed on the market before 2 August 2026** have until **2 December 2026** to comply with Art 50(2) marking. That transitional period covers Art 50(2) only — Art 50(1) interaction disclosure was due on 2 August 2026 (Commission Guidelines C(2026) 5054 final, 20.7.2026, point 153).
- **Marking under Art 50(2) requires marking *and* detection.** Machine-readable marking alone does not comply; for every marking technique deployed there must be a corresponding means of detection (Guidelines C(2026) 5054 final, points 69 to 70).
- **A code of practice does not confer presumption of conformity.** Recital 41 of Reg (EU) 2026/1744 states that the codes under Art 50(7) and Art 56(6) "have limited legal effect, and in particular do not grant a presumption of conformity". Presumption of conformity comes only from harmonised standards (Art 40, Art 53(4), Art 55(2)) — and as at 2026-08-05 no harmonised standard under the AI Act has been cited in the Official Journal. Signing a code is a way to *demonstrate* compliance, nothing more.
- **Profiling of natural persons defeats the Art 6(3) filter absolutely.** Art 6(3), third subparagraph: an Annex III system "shall always be considered to be high-risk where the AI system performs profiling of natural persons". No exception, no balancing.
- **Fine-tuning, rebranding or repurposing makes you the provider.** Art 25(1)(a) to (c). Art 25(2) as amended by Reg (EU) 2026/1744 Art 1(12)(a) confirms the original provider ceases to be provider of that specific system — and that the duty to cooperate does not apply where the initial provider clearly specified the system is not to be changed into a high-risk system.
- **AI literacy binds every provider and deployer of every AI system, at every risk class.** Art 4 as replaced by Reg (EU) 2026/1744 Art 1(5). It has applied since 2 February 2025. The replacement softened it to "take measures to support the development of AI literacy" and expressly does not require guaranteeing any specific level for any individual — it did not delete it.
- **The free-and-open-source carve-out does not reach Art 5 or Art 50.** Art 2(12): the exclusion for AI systems released under free and open-source licences does not apply where they are placed on the market or put into service as high-risk systems or as systems falling under Art 5 or Art 50.
- **Never invent a compute figure, a model name, an accuracy metric, a log retention period or a notified body.** Unknown values become `[[MISSING: …]]` in the artefact and in the report.

## False friends

Assumptions that are plausible, widely repeated, and wrong.

| Plausible wrong assumption | Actual position |
|---|---|
| "The AI Act is the GDPR for AI." | It is product-safety law built on the New Legislative Framework: conformity assessment (Art 43), EU declaration of conformity (Art 47), CE marking (Art 48), notified bodies, market surveillance. The compliance artefacts look like machinery-directive artefacts, not like a privacy notice. Art 2(7) keeps GDPR fully applicable in parallel. |
| "We use OpenAI/Anthropic, so we are covered by their compliance." | Their GPAI obligations under Art 53 are theirs. Your obligations as provider or deployer of the *system* you built are yours. Art 25(4) requires a written agreement with upstream suppliers only when you are the provider of a high-risk system. |
| "Everything with an LLM in it is high-risk." | High-risk is a closed list: Art 6(1) with Annex I, or Art 6(2) with Annex III. A support chatbot, a summariser, a code assistant and a recommender are none of those. They land in Art 50 or in minimal risk. |
| "High-risk obligations start on 2 August 2026." | 2 December 2027 (Annex III) and 2 August 2028 (Annex I), per Art 113 as amended by Reg (EU) 2026/1744. |
| "The AI Act only applies to EU companies." | Art 2(1)(c): providers and deployers established in a third country are covered where the output produced by the AI system is used in the Union. Art 2(1)(a): third-country providers placing systems or GPAI models on the Union market are covered. |
| "Research is exempt, so our R&D is out of scope." | Art 2(6) exempts systems and models developed and put into service *for the sole purpose of* scientific research and development. Art 2(8) exempts pre-market research, testing and development — but expressly not testing in real-world conditions. A commercial product with a research phase is not exempt. |
| "Open source is exempt." | Art 2(12) exempts free-and-open-source systems only outside Art 5, Art 50 and the high-risk regime. For GPAI models, Art 53(2) exempts only Art 53(1)(a) and (b) and only if weights, architecture and usage information are public — the copyright policy and the training-data summary under Art 53(1)(c) and (d) still apply, and the whole exemption falls away for systemic-risk models. |
| "Marking AI output means putting 'Generated by AI' in the caption." | Art 50(2) is a machine-readable marking duty on the *provider*. The visible label is the *deployer's* separate duty for deepfakes and certain published text under Art 50(4). Two paragraphs, two actors, two artefacts. |
| "We can just use C2PA and we are done." | The Code of Practice on Transparency of AI-Generated Content (10 June 2026) does not name C2PA. It requires a **multi-layered** approach: digitally signed metadata (Sub-measure 1.1.1) **plus** imperceptible watermarking (Sub-measure 1.1.2), plus a detection mechanism. Fingerprinting or logging alone is expressly insufficient. |
| "Our coding assistant generates text, so it needs marking." | Source code is outside Art 50(2). Guidelines C(2026) 5054 final, point 68: source code, SDKs, SQL, IaC, YAML, JSON configuration, schemas, scripts, APIs and libraries are excluded, as are short sequences such as UI labels, alt-text and image captions, and machine-to-machine output never perceived by a human. |
| "The AI Liability Directive will fill the damages gap." | Withdrawn. The Commission's withdrawal was published in the Official Journal on 6 October 2025. The instrument that now covers software and AI is the Product Liability Directive recast, Directive (EU) 2024/2853, transposition due 9 December 2026. |
| "The AI Act replaced the machinery rules for AI in machines." | The reverse, as of the omnibus: Reg (EU) 2026/1744 Art 1(41) moved Regulation (EU) 2023/1230 (machinery) from Annex I Section A to Section B, so only Art 6(1), Art 60a and Arts 102 to 112 of the AI Act apply to those products (Art 2(2) as amended). |

## Common mistakes

| Mistake | Why it is wrong |
|---|---|
| Classifying the company instead of the system | Role and risk class attach per AI system (Art 3(3), (4)). One company is routinely provider of A and deployer of B. |
| Treating the FRIA as a DPIA | Art 27 covers a different set of questions and a different set of deployers (public bodies, private providers of public services, and deployers of Annex III points 5(b) and (c)). Art 27(4) as amended allows cross-referencing DPIA sections, not substitution. |
| Skipping the Art 6(4) documentation when concluding "not high-risk" | Art 6(4) requires the assessment to be documented before placing on the market, and Art 49(2) requires registration of that system in the EU database. |
| Logging "for six months" as a flat rule | Art 12 sets logging *capability* for the provider; Art 26(6) sets the deployer's retention floor of at least six months, subject to longer or shorter periods in other Union or national law, in particular data-protection law. |
| Putting the AI disclosure behind a cookie banner, a login or a tooltip | Art 50(5): clear and distinguishable, at the latest at the time of first interaction or exposure, conforming to applicable accessibility requirements. |
| Assuming a human in the loop removes high-risk status | Art 6(3)(c) requires that the system not be meant to replace or influence a previously completed human assessment "without proper human review". A rubber-stamp reviewer does not qualify, and profiling defeats the filter anyway. |
| Reporting an AI Act fine and a GDPR fine as alternatives | They stack. Art 99(7)(c) merely requires prior fines by other authorities for the same activity to be taken into account when setting the amount. |
| Citing the draft Art 6 classification guidelines as law | Still in draft; consultation closed 23 July 2026. |
| Building the technical file after the conformity assessment | Annex IV point 8 requires a copy of the EU declaration of conformity inside the technical documentation; the file is an input to the assessment, not an output. |

## Reference files

- `references/intake.md` — questions to answer before any classification or artefact
- `references/timeline.md` — every application date as at 2026-08-05, what Reg (EU) 2026/1744 changed, transitional rules
- `references/scope-and-roles.md` — Art 3(1) definition, Art 2 scope and carve-outs, the five roles, the Art 25 role flip
- `references/decision-tree.md` — product description to role plus risk class plus obligation list
- `references/prohibited-practices.md` — Art 5 including the 2026 additions, plus a practical screen for ordinary software
- `references/high-risk-classification.md` — Annex I vs Annex III, Art 6(3) filter, profiling rule, safety-component test
- `references/high-risk-obligations.md` — Art 9 to 15, 17, 43, 47, 48, 49, Annex IV
- `references/deployer-duties.md` — Art 26 and the Art 27 fundamental rights impact assessment
- `references/transparency-art50.md` — Art 50 in operational detail, marking, detection, deepfake labelling, the Code of Practice
- `references/gpai.md` — Chapter V, Annex XI, training-data summary, copyright policy, systemic risk, Code of Practice
- `references/ai-literacy.md` — Art 4 as amended and a defensible minimal programme
- `references/governance-enforcement.md` — AI Office, market surveillance, penalty tiers, GDPR/DSA/PLD interaction
- `references/artefacts-records.md` — AI system inventory entry, role and risk classification record
- `references/artefacts-disclosures.md` — Art 50 disclosures, instructions-for-use summary, Annex IV model card, human oversight note, log-retention spec
- `references/checklist.md` — pre-ship checklist producing findings

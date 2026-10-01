# Scope, definitions and roles

Basis: Regulation (EU) 2024/1689 Arts 2 and 3, as amended by Regulation (EU) 2026/1744. Commission Guidelines on the definition of an AI system, C(2025) 5053 final, 29.7.2025 (first published 6 February 2025) — non-binding; authoritative interpretation rests with the CJEU.

## Is it an AI system at all

Art 3(1), verbatim:

> `AI system' means a machine-based system that is designed to operate with varying levels of autonomy and that may exhibit adaptiveness after deployment, and that, for explicit or implicit objectives, infers, from the input it receives, how to generate outputs such as predictions, content, recommendations, or decisions that can influence physical or virtual environments;

Seven elements: machine-based; varying levels of autonomy; possible adaptiveness; explicit or implicit objectives; **inference** of how to generate outputs; outputs of the listed kinds; capacity to influence environments.

The load-bearing element is inference. Systems based on rules defined solely by natural persons to automatically execute operations are outside the definition. In practice:

| Component | In or out |
|---|---|
| Fine-tuned or prompted LLM in a product | In |
| Classical ML classifier, regression, gradient boosting | In |
| Recommender learned from behavioural data | In |
| Hand-written business rules engine, deterministic scoring table | Out — no inference |
| SQL query, statistical aggregate, threshold alert | Out |
| Traditional out-of-office autoresponder, rule-based quick replies | Out (Guidelines C(2026) 5054 final, point 30(i)) |
| Optimisation or search solver | Contested; the Commission's AI-system-definition guidelines treat search and optimisation as within the techniques family. Document the reasoning either way |

`general-purpose AI model` (Art 3(63)) and `general-purpose AI system` (Art 3(66)) are separate concepts: the model is the artefact; the system is the model plus the surrounding capability to serve a purpose. Chapter V binds model providers; Chapters II to IV bind system operators.

## Territorial and personal scope (Art 2(1))

Covered:

- (a) **providers** placing AI systems on the market or putting them into service, or placing GPAI models on the market, in the Union — irrespective of establishment
- (b) **deployers** established or located in the Union
- (c) providers and deployers established in a third country **where the output produced by the AI system is used in the Union**
- (d) importers and distributors
- (e) product manufacturers placing a system on the market together with their product under their own name or trademark
- (f) authorised representatives of non-Union providers
- (g) affected persons located in the Union

Point (c) is the trap. A US company running an EU-facing screening tool, or producing output consumed in the Union, is in scope without any EU establishment.

## Exclusions and their limits (Art 2)

| Paragraph | Exclusion | Limit |
|---|---|---|
| 2(2) as amended | For Art 6(1) high-risk related to products under **Annex I Section B**, only Art 6(1), Art 60a and Arts 102 to 112 apply; Arts 57, 58, 59 only in so far as the high-risk requirements have been integrated into that sectoral legislation | Machinery moved into Section B by Reg (EU) 2026/1744 Art 1(41) |
| 2(3) | National security; exclusively military, defence or national security purposes, regardless of entity | "Exclusively". A dual-use commercial product is not covered by this |
| 2(4) | Third-country public authorities and international organisations under law-enforcement cooperation agreements | Requires adequate fundamental-rights safeguards |
| 2(6) | Systems and models developed and put into service **for the sole purpose of** scientific research and development | "Sole purpose". A research phase inside a commercial product does not qualify |
| 2(8) | Research, testing or development activity **prior to** placing on the market or putting into service | Testing in real-world conditions is expressly **not** covered by the exclusion |
| 2(10) | Deployers who are natural persons using systems in a purely personal non-professional activity | Only the deployer obligations, and only for that person |
| 2(12) | AI systems released under free and open-source licences | Does **not** apply where placed on the market or put into service as high-risk, or as a system falling under Art 5 or Art 50 |
| 2(5) | Does not affect DSA Chapter II intermediary liability | |
| 2(7) as amended | GDPR, Regulation (EU) 2018/1725, Directives 2002/58/EC and (EU) 2016/680 unaffected, without prejudice to Arts 4a and 59 AI Act | Reg (EU) 2026/1744 Art 1(2)(b) swapped the old reference to Art 10(5) for the new Art 4a |
| 2(11) | Does not preclude more worker-protective national law or collective agreements | |

Open-source, for models rather than systems: Art 53(2) disapplies only Art 53(1)(a) and (b) — technical documentation and downstream documentation — and only where the licence allows access, use, modification and distribution **and** parameters including weights, architecture information and usage information are publicly available. The copyright policy (Art 53(1)(c)) and the training-content summary (Art 53(1)(d)) still apply. The whole exception falls away for GPAI models with systemic risk.

## The five roles

| Role | Definition | Core obligations |
|---|---|---|
| **Provider** | Art 3(3): develops, or has developed, an AI system or GPAI model and places it on the market or puts the system into service **under its own name or trademark**, for payment or free of charge | High-risk: Art 16 and everything it references. GPAI: Art 53, 55. Transparency: Art 50(1), (2) |
| **Deployer** | Art 3(4): uses an AI system under its authority, except in a personal non-professional activity | High-risk: Art 26, and Art 27 where applicable. Transparency: Art 50(3), (4) |
| **Importer** | Art 3(6): located or established in the Union, places on the market a system bearing the name or trademark of a person established in a third country | Art 23 |
| **Distributor** | Art 3(7): in the supply chain, other than provider or importer, makes a system available on the Union market | Art 24 |
| **Authorised representative** | Art 3(5): located in the Union, holds a written mandate from a provider | Art 22 (systems), Art 54 (GPAI models) |

Roles are per system. The same company is routinely provider of the system it ships and deployer of the systems it buys.

## The role flip — Art 25

Any distributor, importer, deployer or third party **becomes the provider** of a high-risk system, and takes on Art 16, where it:

- (a) puts its name or trademark on a high-risk system already on the market — white-labelling, rebranding — without prejudice to contractual allocation;
- (b) makes a **substantial modification** to a high-risk system that remains high-risk under Art 6; or
- (c) **modifies the intended purpose** of an AI system, including a general-purpose AI system, that was not classified as high-risk, so that it becomes high-risk under Art 6.

Point (c) is how ordinary product work triggers the high-risk regime: taking a general-purpose assistant and pointing it at CV screening or credit decisions.

Art 25(2), as replaced by Reg (EU) 2026/1744 Art 1(12)(a): the initial provider stops being the provider of that specific system. It must cooperate closely with the new provider and give the reasonably expected technical access and assistance, expressly including (a) technical documentation sufficient to assess compliance with Art 16, (b) information about known limitations and failure modes, and (c) targeted technical access for testing and validation. That duty **does not apply** where the initial provider has clearly specified that its system is not to be changed into a high-risk system. Read the upstream terms of service before assuming any cooperation duty exists.

Art 25(3): where a high-risk system is a safety component of a product under Annex I Section A, the **product manufacturer** is the provider if the system is placed on the market with the product under the manufacturer's name or trademark, or put into service under that name after the product was placed.

Art 25(4), as amended by Reg (EU) 2026/1744 Art 1(12)(b): the provider of a high-risk system and any third party supplying an AI system, **AI model**, tools, services, components or processes integrated into it must specify by **written agreement** the necessary information, capabilities, technical access and assistance. Does not apply to third parties making tools, services, processes or components publicly available under a free and open-source licence — other than general-purpose AI models.

## Substantial modification

Art 3(23): a change to an AI system after its placing on the market or putting into service which is not foreseen or planned in the initial conformity assessment carried out by the provider and as a result of which the compliance with the Chapter III Section 2 requirements is affected, or which results in a modification to the intended purpose for which the system was assessed.

Art 43(4), second subparagraph: for high-risk systems that continue to learn after being placed on the market, changes pre-determined by the provider at the initial conformity assessment and contained in the technical documentation under Annex IV point 2(f) do **not** constitute a substantial modification. Everything else does, and triggers a new conformity assessment under Art 43(4), first subparagraph.

Practically: swapping the underlying model, retraining on a materially different population, or extending the system to a new decision context are candidates. Prompt-level copy edits are not.

## Checkpoints

- [ ] Art 3(1) tested element by element, with inference addressed explicitly
- [ ] Territorial trigger under Art 2(1)(a), (b) or (c) named
- [ ] Every claimed exclusion mapped to its paragraph and its limit stated
- [ ] Role determined per system, in writing, with the definition quoted
- [ ] Art 25(1)(a) to (c) tested against what the team actually plans to do with upstream models
- [ ] Upstream provider's terms checked for an Art 25(2) "not to be changed into high-risk" statement
- [ ] Written agreement under Art 25(4) in place or flagged as `[[MISSING: …]]`
- [ ] Open-source claim tested against Art 2(12) and, for models, Art 53(2)

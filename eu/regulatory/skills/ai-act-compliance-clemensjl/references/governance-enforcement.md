# Governance, enforcement and interaction with other law

Basis: Regulation (EU) 2024/1689 Chapters VII, IX, XII, as amended by Regulation (EU) 2026/1744. Applicable since **2 August 2025** for Chapter VII (governance) and Chapter XII (penalties), except Art 101, which applied from 2 August 2026.

## Who enforces

| Body | Competence | Source |
|---|---|---|
| **AI Office** (within the Commission) | GPAI models: exclusive supervision and enforcement of Chapter V, including fines under Art 101. Since the omnibus, **also exclusively competent for AI systems** based on GPAI models where model and system come from the same provider or the same undertaking, and for AI systems constituting or integrated into a designated VLOP or VLOSE | Arts 88 to 94, 101; Art 75(1) as replaced by Reg (EU) 2026/1744 Art 1(31)(b) |
| **National market surveillance authorities** | AI systems generally, under Regulation (EU) 2019/1020; one or more per Member State, with a single point of contact | Art 70, Art 74 |
| **European Artificial Intelligence Board** | Coordination, opinions, recommendations, adequacy assessments of codes of practice | Arts 65 to 66, Art 56(6) |
| **Scientific panel of independent experts** | Qualified alerts on systemic-risk models, support to enforcement | Art 68 |
| **Notifying authorities and notified bodies** | Designation and conformity assessment | Arts 28 to 39 |
| **Authorities protecting fundamental rights** | May request and access information and documentation from the market surveillance authority, in accessible language and machine-readable format | Art 77, expanded by Reg (EU) 2026/1744 Art 1(34) |
| **Data protection authorities** | GDPR in parallel; market surveillance authority for high-risk systems used by law enforcement, border management, justice and democratic processes in some Member States | Art 74(8); Art 2(7) |

Carve-outs from the AI Office's exclusive competence under Art 75(1)(a): systems related to Annex I products; Annex III point 2 (critical infrastructure); systems provided by law enforcement authorities, border management authorities and financial institutions in so far as they fall under Art 74(6); and Annex III point 8 systems as regards the administration of justice. The exclusive competence applies to **providers** of those systems, and to deployers only when they are also the provider or part of the same undertaking.

Consequences worth knowing: under Art 75(1a), providers of high-risk systems under AI Office competence report serious incidents to the **AI Office** rather than to a national authority, with Art 73(2) to (9) applying mutatis mutandis.

## Penalty tiers — Art 99

| Conduct | Ceiling |
|---|---|
| Non-compliance with the **Art 5 prohibitions** | EUR **35 000 000** or **7 %** of total worldwide annual turnover for the preceding financial year, whichever is **higher** (Art 99(3)) |
| Non-compliance with provider obligations (Art 16), authorised representative (Art 22), importer (Art 23), distributor (Art 24), **deployer (Art 26)**, notified body requirements (Arts 31, 33(1), (3), (4), 34), **transparency obligations (Art 50)**, and — added by Reg (EU) 2026/1744 Art 1(38)(b) — **Art 25(2) and (4)** value-chain duties | EUR **15 000 000** or **3 %**, whichever is **higher** (Art 99(4)) |
| Supplying incorrect, incomplete or misleading information to notified bodies or national competent authorities | EUR **7 500 000** or **1 %**, whichever is **higher** (Art 99(5)) |
| GPAI model providers, imposed by the Commission | **3 %** of annual total worldwide turnover or EUR **15 000 000**, whichever is higher (Art 101(1)) |
| Union institutions, bodies, offices and agencies | Art 100 (EDPS-imposed) |

**SMEs and start-ups** (Art 99(6)) and **small mid-caps** (Art 99(6a), inserted by Reg (EU) 2026/1744 Art 1(38)(c)): each fine is up to the percentage **or** the amount, **whichever is lower**. SME per Recommendation 2003/361/EC; SMC per Recommendation (EU) 2025/1099 — both definitions added to Art 3 as points (14a) and (14b) by the omnibus.

Art 99(1) as amended: Member States lay down rules on penalties **and other enforcement measures, which may also include administrative fines, warnings and non-monetary measures**, taking into account the Commission's Art 96 guidelines, and must take into account the interests and economic viability of SMEs, start-ups and SMCs.

Art 99(7) sets the factors: nature, gravity and duration; whether other market surveillance authorities already fined the same operator for the same infringement; whether **other authorities** already fined for infringements of other Union or national law resulting from the same activity or omission; size, turnover, market share; financial benefit or loss avoided; degree of cooperation; degree of responsibility given technical and organisational measures; how the infringement became known and whether the operator notified it; intent or negligence; and mitigation of harm to affected persons.

## Stacking with GDPR fines

Both regimes can bite for the same conduct. Art 2(7) of the AI Act keeps the GDPR fully applicable; the AI Act does not displace it and creates no lex specialis.

- **Different protected interests, different addressees.** The AI Act protects health, safety and fundamental rights through product-safety mechanics and addresses providers, deployers, importers, distributors. The GDPR protects personal data and addresses controllers and processors. The same company can be provider and controller for the same system.
- **No prohibition on parallel fines.** Art 99(7)(b) and (c) require prior fines by other market surveillance authorities and by other authorities under other Union or national law to be **taken into account when setting the amount**. That is a mitigation factor, not a bar. The *ne bis in idem* principle under Art 50 of the Charter constrains double punishment for the same offence with the same protected interest and the same person — whether it applies across AI Act and GDPR proceedings is unsettled and is a question for counsel, not for a compliance document.
- **Practical sequencing.** Deploying an unlawful emotion-recognition system in a workplace is simultaneously an Art 5(1)(f) prohibition (up to 7 % under the AI Act) and, typically, a GDPR Art 9 special-category processing breach (up to 4 % under GDPR Art 83(5)). Budget for both.

## EDPB Opinion 28/2024

Opinion 28/2024 on certain data protection aspects related to the processing of personal data in the context of AI models, **adopted 17 December 2024** by the EDPB on a request from the Irish supervisory authority under GDPR Art 64(2). Final and in force. Four questions:

1. **When can an AI model be considered anonymous.** AI models trained with personal data cannot in all cases be considered anonymous. Claims of anonymity must be assessed case by case by the supervisory authority. For a model to be anonymous, both the likelihood of direct — including probabilistic — extraction of personal data about training-data individuals and the likelihood of obtaining such data from queries must be insignificant. The Opinion gives a non-prescriptive, non-exhaustive list of methods controllers may use to demonstrate anonymity.
2. and 3. **Legitimate interest as a legal basis** in the development and deployment phases. The usual three-step test: identify the legitimate interest; necessity; balancing against the interests, rights and freedoms of data subjects. The Opinion lists elements supervisory authorities should consider, including data subjects' reasonable expectations.
4. **Consequences of unlawful processing in the development phase** for the subsequent operation of the model.

The practical import for an AI Act project: the AI Act's Art 4a legal basis covers only bias detection and correction for special categories. Everything else about training data, model memorisation and inference-time processing remains a GDPR question, answered by reference to Opinion 28/2024, not by the AI Act.

## Interaction with other Union law

### GDPR Art 22 — automated individual decision-making

Independent of the AI Act. A decision based solely on automated processing, including profiling, producing legal effects or similarly significant effects is prohibited unless it falls within Art 22(2)(a) contract necessity, (b) Union or Member State law, or (c) explicit consent, with Art 22(3) safeguards — at least the right to obtain human intervention, to express a point of view and to contest the decision.

Two mismatches to keep in mind:

- A system can be **outside** Annex III high-risk and still be caught by Art 22. Motor insurance pricing is not Annex III point 5(c) but can be an Art 22 decision.
- A system can be **inside** Annex III and outside Art 22, if a human genuinely makes the decision. That does not reduce the AI Act obligations, because Art 6(3)(c) sets its own, stricter test.

### Digital Services Act, Regulation (EU) 2022/2065

- AI Act Art 2(5): the AI Act does not affect DSA Chapter II intermediary liability.
- Designated VLOPs and VLOSEs owe DSA Art 34 and 35 systemic risk assessment and mitigation, which covers generative AI features in the service. The Code of Practice on Transparency of AI-Generated Content encourages platforms to expose disclosure tooling in upload interfaces so that deployers can meet Art 50(4).
- Since the omnibus, AI systems constituting or integrated into a designated VLOP or VLOSE fall under the **AI Office's** exclusive competence for AI Act supervision (Art 75(1)(b)).

### Product Liability Directive recast, Directive (EU) 2024/2853

Adopted 23 October 2024, OJ L, 2024/2853, 18.11.2024. Repeals Directive 85/374/EEC with effect from **9 December 2026**, which continues to apply to products placed on the market before that date. **Transposition deadline: 9 December 2026** (Art 22).

What matters for AI teams:

- **Software is a product.** Recitals 12 to 13: the Directive applies to all movables including software, whether stored on a device, accessed through a network or cloud, or supplied as software-as-a-service. Information as such is not a product, and neither is the mere source code. AI system providers are within the notion of manufacturer or producer of software.
- **Free and open-source software** developed or supplied **outside the course of a commercial activity** is out of scope; supply in exchange for a price, or for personal data used other than exclusively for improving security, compatibility or interoperability, is commercial.
- **Related services, software updates and upgrades** are within the product where they are within the manufacturer's control. Failure to supply security updates needed to address cybersecurity vulnerabilities can make the product defective.
- **Substantial modification through a software update** is treated like any other substantial modification, which can shift liability to the modifier.

This is now the damages route for AI harm. There is no separate AI liability instrument.

### AI Liability Directive — withdrawn

The proposal COM(2022) 496 was withdrawn; the withdrawal was published in the Official Journal on **6 October 2025**. Do not cite it as forthcoming law. [[UNVERIFIED: the exact OJ C reference of the withdrawal notice]]

### Cyber Resilience Act, Regulation (EU) 2024/2847

Art 42(3) of the AI Act, inserted by Reg (EU) 2026/1744 Art 1(18): high-risk AI systems within the scope of Regulation (EU) 2024/2847 that meet the conditions in its Art 12(1) are **deemed to comply** with the Art 15 cybersecurity requirements of the AI Act.

### Boundary with published legal texts

This skill does not draft imprints, privacy notices, terms and conditions, withdrawal information or accessibility statements. Those are jurisdiction-specific published documents and belong to the `legal-*` skills. Where an Art 50 disclosure or an Art 26(11) notice has to appear on a website, this skill supplies the substance and the placement rule; the surrounding published text is out of scope here.

## Checkpoints

- [ ] Competent authority identified per system: AI Office or a national market surveillance authority, applying the Art 75(1) carve-outs
- [ ] Serious incident recipient determined correctly (Art 73 vs Art 75(1a))
- [ ] Penalty exposure stated with the correct tier and the higher-of rule, or the lower-of rule for SMEs and SMCs
- [ ] Parallel GDPR exposure assessed for the same conduct rather than assumed to be absorbed
- [ ] Art 22 GDPR assessed independently of the AI Act classification
- [ ] DSA obligations checked where the product is or sits inside a platform or search engine
- [ ] Product Liability Directive recast on the roadmap for 9 December 2026, with update-supply and modification duties understood
- [ ] No reliance on the withdrawn AI Liability Directive
- [ ] EDPB Opinion 28/2024 applied to training data and model-anonymity claims rather than the AI Act

# Decision tree: product description to role, risk class and obligations

Basis: Regulation (EU) 2024/1689 as amended by Regulation (EU) 2026/1744. Run per AI system. Record every answer — the reasoning is the artefact, not the conclusion.

## Step 0 — Is it an AI system?

Art 3(1). Does it **infer** from input how to generate predictions, content, recommendations or decisions, with some autonomy?

- **No** → out of scope. Record the reasoning against the seven elements in `scope-and-roles.md`. Stop.
- **Yes** → Step 1.

## Step 1 — Is anyone in scope?

Art 2(1). Provider placing on the Union market, deployer established in the Union, or third-country operator whose **output is used in the Union**?

- **No** → out of scope, but re-test on every market expansion. Stop.
- **Yes** → Step 2.

## Step 2 — Does an exclusion apply?

Test Art 2(3), (4), (6), (8), (10), (12) with their limits (see `scope-and-roles.md`). Note that Art 2(12) does not exclude anything under Art 5, Art 50 or the high-risk regime.

- **Fully excluded** → record the paragraph and the reasoning. Stop.
- **Otherwise** → Step 3.

## Step 3 — What is our role, per system?

| If | Role | Source |
|---|---|---|
| We develop the system and ship it under our name or trademark | **Provider** | Art 3(3) |
| We use a system bought or licensed from someone else, under our authority, in our business | **Deployer** | Art 3(4) |
| We resell an EU-origin system unchanged | Distributor | Art 3(7) |
| We place a third-country provider's system on the Union market | Importer | Art 3(6) |
| We hold a written mandate from a non-Union provider | Authorised representative | Art 3(5) |
| We white-label a third-party system, substantially modify it, or repurpose it into a high-risk use | **Provider**, by operation of law | Art 25(1)(a) to (c) |

Multiple roles are normal. Continue with each role separately.

Building a product on top of an API model (OpenAI, Anthropic, Mistral, a hosted open-weights model) and shipping it under your own name makes you the **provider of that AI system** and the **deployer of nothing** — the upstream party is the provider of the *model*, bound by Chapter V. You do not inherit their Chapter V obligations, and they do not carry your Art 50 obligations.

## Step 4 — Is it prohibited?

Run the screen in `prohibited-practices.md` against Art 5(1)(a) to (h) and, from 2 December 2026, (ba) and (bb).

- **Yes** → stop the feature. No amount of documentation cures a prohibition. Fine ceiling: EUR 35 000 000 or 7 % of total worldwide annual turnover, whichever is higher (Art 99(3)).
- **No** → Step 5.

## Step 5 — Is it high-risk under Annex I?

Art 6(1): both conditions must be met.

1. The system is intended to be used as a **safety component** of a product, or is itself a product, covered by the Union harmonisation legislation in **Annex I**; **and**
2. that product must undergo **third-party conformity assessment** under that legislation.

Apply Art 6(1a) to (1c) as inserted by Reg (EU) 2026/1744: systems solely for user assistance, performance optimisation, service efficiency, automation, convenience or quality control are not safety components — unless failure or malfunctioning would endanger health and safety. A product required to undergo third-party assessment solely for non-health-and-safety reasons (radio spectrum, EMC) does not meet condition 2.

- **Yes, and the product is under Annex I Section A** → full high-risk regime, applicable **2 August 2028**. Go to Step 8.
- **Yes, and the product is under Annex I Section B** (aviation, vehicles, rail, marine equipment, machinery since the omnibus) → only Art 6(1), Art 60a and Arts 102 to 112 apply (Art 2(2) as amended). The substantive requirements arrive through the sectoral act. Go to Step 8 with that caveat.
- **No** → Step 6.

## Step 6 — Is it high-risk under Annex III?

Art 6(2). Is the intended purpose within any of these areas?

1. Biometrics — remote biometric identification (not verification-only), biometric categorisation by sensitive or protected attributes, emotion recognition
2. Critical infrastructure — safety components in critical digital infrastructure, road traffic, or supply of water, gas, heating, electricity
3. Education and vocational training — admission, evaluating learning outcomes, assessing appropriate level of education, proctoring
4. Employment and worker management — recruitment or selection including targeted job ads, filtering applications, evaluating candidates; decisions on terms, promotion, termination, task allocation based on behaviour or traits, performance and behaviour monitoring
5. Essential private and public services — eligibility for public benefits; **creditworthiness or credit scoring** (except fraud detection); **risk assessment and pricing for life and health insurance**; emergency call triage and dispatch
6. Law enforcement
7. Migration, asylum, border control
8. Administration of justice and democratic processes

- **No** → Step 7.
- **Yes** → Step 6a.

### Step 6a — Does the Art 6(3) filter apply?

An Annex III system is **not** high-risk where it does not pose a significant risk of harm to health, safety or fundamental rights, including by not materially influencing the outcome of decision making, **and** at least one of these is fulfilled:

- (a) narrow procedural task;
- (b) intended to improve the result of a previously completed human activity;
- (c) intended to detect decision-making patterns or deviations from prior patterns, and not meant to replace or influence the previously completed human assessment without proper human review;
- (d) intended to perform a preparatory task to an assessment relevant to an Annex III use case.

**Absolute override:** Art 6(3), third subparagraph — "an AI system referred to in Annex III shall always be considered to be high-risk where the AI system performs profiling of natural persons." Profiling defeats the filter regardless of conditions (a) to (d).

- **Filter applies and no profiling** → not high-risk. But: document the assessment before placing on the market (Art 6(4)) and **register the system in the EU database under Art 49(2)**. This is a filed position. Then go to Step 7 for the transparency layer.
- **Filter does not apply, or profiling** → high-risk under Annex III, applicable **2 December 2027**. Go to Step 8.

## Step 7 — Does Art 50 apply?

Not mutually exclusive with high-risk: Art 50(6) states Art 50(1) to (4) do not affect Chapter III.

| Trigger | Who | Obligation | Reference |
|---|---|---|---|
| System intended to interact directly with natural persons | Provider | Inform the person they are interacting with an AI system, unless obvious to a reasonably well-informed, observant and circumspect person | Art 50(1) |
| System generates synthetic audio, image, video or text | Provider | Mark outputs in a machine-readable format **and** make them detectable as artificially generated or manipulated | Art 50(2) |
| Emotion recognition or biometric categorisation system | Deployer | Inform the exposed persons of the operation of the system | Art 50(3) |
| Output is a deep fake (image, audio, video) | Deployer | Disclose that the content is artificially generated or manipulated | Art 50(4), 1st subpara |
| AI-generated or manipulated text published to inform the public on matters of public interest | Deployer | Disclose, unless human review and editorial responsibility | Art 50(4), 2nd subpara |

All applicable from **2 August 2026**; Art 50(2) only, for systems placed before that date, from **2 December 2026** (Art 111(4)). Details in `transparency-art50.md`.

- **None applies** → minimal risk. Only Art 4 (AI literacy) binds, plus whatever other law applies. Record it and stop.

## Step 8 — Obligation list by outcome

### Provider of a high-risk AI system

Art 16 is the index. It pulls in:

| Obligation | Article |
|---|---|
| Risk management system, continuous and iterative over the lifecycle | Art 9 |
| Data and data governance for training, validation and testing sets | Art 10 (para 5 deleted, moved to Art 4a) |
| Technical documentation, at minimum Annex IV; simplified form available to SMEs and SMCs | Art 11 |
| Automatic logging over the lifetime of the system | Art 12 |
| Transparency to deployers and instructions for use | Art 13 |
| Human oversight designed in | Art 14 |
| Accuracy, robustness, cybersecurity | Art 15 |
| Quality management system, proportionate to organisation size | Art 17 |
| Documentation kept 10 years | Art 18 |
| Automatically generated logs kept, at least 6 months | Art 19 |
| Corrective actions and duty to inform | Art 20 |
| Cooperation with competent authorities | Art 21 |
| Authorised representative, if established outside the Union | Art 22 |
| Conformity assessment | Art 43 |
| EU declaration of conformity, kept 10 years, content per Annex V | Art 47 |
| CE marking, digital CE marking for digitally provided systems | Art 48 |
| Registration in the EU database | Art 49 |
| Post-market monitoring plan | Art 72 |
| Serious incident reporting | Art 73 |

### Deployer of a high-risk AI system

| Obligation | Article |
|---|---|
| Use in accordance with the instructions for use | Art 26(1) |
| Assign human oversight to competent, trained, authorised persons | Art 26(2) |
| Ensure input data is relevant and sufficiently representative, where the deployer controls it | Art 26(4) |
| Monitor operation, inform provider, suspend on risk, report serious incidents | Art 26(5) |
| Keep automatically generated logs, at least 6 months | Art 26(6) |
| Inform workers' representatives and affected workers before workplace use | Art 26(7) |
| Register, if a public authority or Union body | Art 26(8), Art 49(3) |
| Use Art 13 information for the GDPR Art 35 DPIA | Art 26(9) |
| Inform natural persons subject to Annex III decisions | Art 26(11) |
| Fundamental rights impact assessment, where in scope | Art 27 |

### Provider of a general-purpose AI model

Art 53(1)(a) to (d), Art 54 (authorised representative), plus Art 55 if systemic risk. See `gpai.md`.

### Everyone

Art 4 AI literacy. See `ai-literacy.md`.

## Checkpoints

- [ ] Every step answered explicitly, including the ones answered "no"
- [ ] Role determined before risk class
- [ ] Annex III areas checked one by one against the stated intended purpose
- [ ] Profiling question answered explicitly
- [ ] Art 6(3) conclusion, if used, backed by an Art 6(4) documented assessment and an Art 49(2) registration item
- [ ] Art 50 checked even where the system is high-risk (Art 50(6))
- [ ] Applicable date attached to every obligation, from `timeline.md`
- [ ] Classification near the boundary flagged for legal sign-off

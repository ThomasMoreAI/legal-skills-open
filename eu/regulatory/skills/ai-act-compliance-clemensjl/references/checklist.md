# Pre-ship checklist

Run before an AI feature reaches EU users, and again after any model swap, retraining, intended-purpose change or expansion into a new use context. Every finding is reported with the article and the location, not as a general remark. Findings that can be verified technically are verified technically, not judged from intent.

## Technical checks first

These five take minutes and produce a disproportionate share of the findings.

1. Open the product as a new user. Note the exact moment an AI disclosure appears, if it does. Anything after the first message or the first exposure fails Art 50(5).
2. Take one generated image, one generated audio file and one generated video from production. Inspect the metadata for a signed AI-generation marker; run the vendor's detection endpoint against them. If either is absent, Art 50(2) is not met.
3. Generate a text output over 200 tokens and check whether a watermark and a corresponding detection route exist (Code of Practice Sub-measure 1.1.2, Sub-measure 2.1.2).
4. Grep the repository and content for `AI-generated`, `synthetic`, `deepfake`, `emotion`, `sentiment`, `biometric`, `credit score`, `screening`, `ranking`, `profiling` — and for stale dates `2 August 2026`, `2 August 2027` used as high-risk deadlines.
5. Trigger the human override and the stop control in a staging environment. If the stop control does not exist, Art 14(4)(e) is not met.

## Scope and role

- [ ] Every AI system in the product has an inventory entry, including bought and embedded ones
- [ ] Art 3(1) applied per system, with the inference element addressed
- [ ] Territorial trigger under Art 2(1)(a), (b) or (c) recorded
- [ ] Each claimed exclusion mapped to its paragraph of Art 2 with its limit
- [ ] Free-and-open-source claim tested against Art 2(12) — no relief for Art 5, Art 50 or high-risk
- [ ] Role recorded per system, per Art 3(3) to (7)
- [ ] Art 25(1)(a) to (c) tested against actual plans for rebranding, modification and repurposing
- [ ] Upstream terms checked for an Art 25(2) "not to be changed into high-risk" statement
- [ ] Written agreement under Art 25(4) in place where we are the provider of a high-risk system
- [ ] Authorised representative appointed where the provider is outside the Union — Art 22 (systems), Art 54 (models)

## Prohibitions — Art 5

- [ ] All eight original points screened with a written yes or no
- [ ] Emotion inference in workplace or education explicitly ruled in or out; medical-or-safety exception assessed if invoked — Art 5(1)(f)
- [ ] Biometric categorisation deducing protected attributes ruled out — Art 5(1)(g)
- [ ] Provenance of any facial dataset documented; no untargeted scraping — Art 5(1)(e)
- [ ] Persuasion and personalisation reviewed for vulnerability targeting — Art 5(1)(a), (b)
- [ ] Cross-context reuse of behavioural scores reviewed — Art 5(1)(c)
- [ ] Generative image or video features: safeguards documented against Art 5(1a)(a)(ii), with a misuse correction path, before 2 December 2026
- [ ] No prohibition treated as curable by disclosure or consent

## Classification

- [ ] Both routes tested: Art 6(1) with Annex I and Art 6(2) with Annex III
- [ ] Safety-component test applied per Art 3(14) as amended and Art 6(1a) to (1c)
- [ ] Annex I Section A vs Section B identified; Art 2(2) limitation applied for Section B
- [ ] Annex III checked sub-point by sub-point against the stated intended purpose
- [ ] Verification-only biometrics and financial-fraud detection exclusions applied correctly
- [ ] Art 6(3) chapeau assessed separately from conditions (a) to (d)
- [ ] Profiling answered explicitly against GDPR Art 4(4); a yes ends the filter argument
- [ ] Any "not high-risk" conclusion documented before market placement — Art 6(4) — and registered under Art 49(2)
- [ ] Correct application date attached: 2 December 2027 or 2 August 2028
- [ ] Boundary calls routed to legal sign-off, in writing

## Art 50 transparency — in force now

- [ ] Every interactive surface discloses AI at or before the first turn — Art 50(1), Art 50(5)
- [ ] Any reliance on the "obvious" exception written up against the Guidelines factors and reviewed by legal
- [ ] Agents disclose both artificial nature and principal — Guidelines C(2026) 5054 final point 31
- [ ] Machine-readable marking implemented for every synthetic modality — Art 50(2)
- [ ] A detection means exists for every marking technique deployed — Guidelines points 69 to 70
- [ ] Multi-layer marking for audio, image, video and containerised text; metadata layer digitally signed and time-stamped
- [ ] Free-form text over 200 tokens watermarked with a detection route
- [ ] Out-of-scope outputs listed and justified — source code, UI labels, alt-text, machine-to-machine, closed-loop intermediates
- [ ] Assistive-editing and no-substantial-alteration exceptions documented case by case
- [ ] Interoperability route planned against 2 February 2027
- [ ] Deepfake labelling built: EU icon or equivalent, design and placement specifications met — Art 50(4)
- [ ] Audio-only disclaimer at the beginning of the content
- [ ] Published-text disclosure built, or the human-review-and-editorial-responsibility exception documented with a named responsible person
- [ ] Emotion recognition or biometric categorisation notification built — Art 50(3) — after clearing Art 5
- [ ] Disclosures accessible: screen-reader detectable, contrast checked, alternative cues per modality
- [ ] Systems placed before 2 August 2026 tracked against the 2 December 2026 Art 50(2) deadline — Art 111(4)

## High-risk provider duties, where applicable

- [ ] Art 9 risk file covers reasonably foreseeable misuse, post-market data and under-18 impact, and states residual risk acceptance
- [ ] Art 10 data governance documented; bias examination and mitigation recorded; special-category processing mapped to the six Art 4a(1) conditions
- [ ] Annex IV technical documentation complete across all nine headings, with dated and signed test reports
- [ ] SME or SMC status recorded where the simplified Art 11(1) form is used
- [ ] Art 12 logging capability implemented; Annex III point 1(a) minima met if applicable
- [ ] Instructions for use cover Art 13(3)(a) to (f), including declared accuracy metrics
- [ ] Human oversight design covers Art 14(4)(a) to (e), with a genuine stop-to-safe-state and an automation-bias countermeasure
- [ ] Two-person verification implemented for Annex III point 1(a) — Art 14(5)
- [ ] Art 15 addresses feedback loops and data poisoning, model poisoning, adversarial examples, confidentiality attacks and model flaws
- [ ] Cyber Resilience Act route under Art 42(3) considered before duplicating cybersecurity work
- [ ] Art 17 QMS documented or mapped onto an existing QMS; simplified route only where there are no partner or linked enterprises
- [ ] Art 43 route selected on verified harmonised-standard availability, not assumption
- [ ] EU declaration of conformity per Annex V, machine readable, 10-year retention — Art 47
- [ ] CE marking affixed, digital CE conditions met for software-only systems — Art 48
- [ ] Registrations completed per Art 49(1), (2), (3) and (5), against the current Annex VIII
- [ ] Post-market monitoring plan drafted and inside the technical documentation — Art 72
- [ ] Serious incident process with 15-day, 10-day and 2-day deadlines, and the correct recipient under Art 73 or Art 75(1a)
- [ ] Documentation retention of 10 years and log retention of at least 6 months arranged — Arts 18, 19

## High-risk deployer duties, where applicable

- [ ] Instructions for use obtained and read before deployment
- [ ] Use stays inside the intended purpose — Art 26(1)
- [ ] Human oversight assigned to named roles with competence, training and authority — Art 26(2)
- [ ] Input data under our control assessed for relevance and representativeness — Art 26(4)
- [ ] Monitoring, suspension and escalation path documented with named recipients — Art 26(5)
- [ ] Log retention at least six months, reconciled with GDPR and sectoral law — Art 26(6)
- [ ] Workers' representatives and affected workers informed before workplace use — Art 26(7)
- [ ] Public-sector deployer verified EU database registration before use — Art 26(8)
- [ ] DPIA carried out using the Art 13 information — Art 26(9)
- [ ] Persons subject to decisions informed — Art 26(11)
- [ ] FRIA scope tested against all three Art 27(1) categories, including Annex III 5(b) and (c)
- [ ] FRIA contains all six Art 27(1) elements, by text or explicit cross-reference to the DPIA
- [ ] FRIA notified to the market surveillance authority — Art 27(3)

## GPAI model duties, where applicable

- [ ] Provider-of-a-model status determined and documented, including for fine-tuned models
- [ ] Annex XI documentation drafted with training compute in FLOP and energy consumption
- [ ] Annex XII documentation prepared for downstream integrators
- [ ] Copyright policy in place with a working mechanism honouring Art 4(3) DSM reservations
- [ ] Public training-content summary published on the AI Office template of 24 July 2025
- [ ] Open-source claim tested against Art 53(2); points (c) and (d) still applied
- [ ] Training compute compared against 10^25 FLOP; Art 52(1) notification within two weeks if exceeded
- [ ] Systemic-risk duties under Art 55 in place where applicable
- [ ] Authorised representative appointed before market placement where the provider is outside the Union — Art 54
- [ ] Models placed before 2 August 2025 tracked against 2 August 2027 — Art 111(3)

## AI literacy and adjacent law

- [ ] Art 4 programme covers every AI system and every person operating one, including contractors
- [ ] Oversight personnel trained separately under Art 26(2)
- [ ] Training dated, with audience, content version and attendance recorded
- [ ] GDPR Art 22 assessed independently of the AI Act classification
- [ ] Model-anonymity and training-data lawfulness assessed against EDPB Opinion 28/2024 (adopted 17 December 2024)
- [ ] DSA obligations checked where the product is or sits inside a platform or search engine
- [ ] Product Liability Directive recast on the roadmap for 9 December 2026, including the software-update supply duty
- [ ] No reliance on the withdrawn AI Liability Directive

## Hygiene

- [ ] No stale dates: high-risk deadlines are 2 December 2027 and 2 August 2028, never 2 August 2026 or 2 August 2027
- [ ] Draft Art 6(5) classification guidelines never cited as settled law
- [ ] No claim that a code of practice confers presumption of conformity — recital 41, Reg (EU) 2026/1744
- [ ] No German or US framing borrowed: no "AI Act = GDPR for AI", no NIST AI RMF terminology substituted for statutory terms
- [ ] Every `[[…]]` placeholder resolved or explicitly reported as open
- [ ] Draft marker still present wherever legal sign-off has not been confirmed

## Findings format

Report as a table, most serious first.

| Severity | Location | Article | Finding | Remedy |
|---|---|---|---|---|
| critical / high / medium | file:line, URL or screen | Art … | what is missing or wrong | the concrete step |

**Critical** means: a prohibited practice; an Art 50 obligation already in force and unmet; placing a high-risk system on the market without conformity assessment, declaration of conformity, CE marking or registration; or an undocumented Art 6(3) "not high-risk" conclusion. Everything else with a live deadline is **high**.

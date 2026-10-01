# High-risk classification

Basis: Regulation (EU) 2024/1689 Arts 6 and 7, Annexes I and III, as amended by Regulation (EU) 2026/1744. Commission guidelines under Art 6(5) are **still in draft** — public consultation closed 23 July 2026. Do not cite them as settled.

Application dates: Chapter III Sections 1, 2 and 3 apply from **2 December 2027** for Annex III systems (Art 6(2)) and **2 August 2028** for Annex I systems (Art 6(1)) — Art 113 third para point (c) as replaced by Reg (EU) 2026/1744 Art 1(40)(b). Art 6(5) is excluded from the deferral and applies from 2 August 2026.

## Two independent routes

There is no general "this feels risky" test. A system is high-risk only via Art 6(1) with Annex I, or Art 6(2) with Annex III. Art 7 lets the Commission amend Annex III by delegated act; nothing else expands the list.

## Route 1 — Art 6(1), product legislation

Both conditions must be met:

- (a) the AI system is intended to be used as a **safety component** of a product, or is itself a product, covered by the Union harmonisation legislation listed in **Annex I**; **and**
- (b) that product is required to undergo **third-party conformity assessment** with a view to placing on the market or putting into service under that legislation.

**Safety component** — Art 3(14) as replaced by Reg (EU) 2026/1744 Art 1(4)(a): a component of a product or of an AI system which fulfils a safety function for that product or system, or the failure or malfunctioning of which endangers the health and safety of persons or property; a component fulfils a safety function where **its intended purpose is to prevent or mitigate risks to health and safety** of persons or property.

Narrowing rules inserted by Reg (EU) 2026/1744 Art 1(8):

- Art 6(1a): systems used **solely for non-safety-related aspects** of user assistance, performance optimisation, service efficiency, automation or convenience or quality control **do not qualify as safety components**.
- Art 6(1b): notwithstanding that, systems whose failure or malfunctioning would endanger health and safety **do** qualify.
- Art 6(1c): a product required to undergo third-party assessment **solely** for risks other than health and safety — in particular radio spectrum distribution or electromagnetic interference not affecting health and safety — does not satisfy condition (b).

Recital 7 of Reg (EU) 2026/1744: the mere fact that an AI system is integrated into or operates within a product subject to Union harmonisation legislation does not by itself mean it fulfils a safety function.

**Annex I Section A** (AI Act requirements integrated into the AI Act's own conformity route): toy safety, recreational craft, lifts, ATEX equipment, radio equipment, pressure equipment, cableway installations, PPE, gas appliances, medical devices (Regulation (EU) 2017/745), in vitro diagnostic medical devices (Regulation (EU) 2017/746). Point 1 (machinery) was **deleted** by Reg (EU) 2026/1744 Art 1(41)(a).

**Annex I Section B** (sectoral acts handle it): civil aviation security, agricultural and forestry vehicles, two- or three-wheel vehicles, marine equipment, rail interoperability, motor vehicles, aviation (Regulation (EU) 2018/1139), general vehicle safety — and, new, point 21: **Regulation (EU) 2023/1230 on machinery**, added by Reg (EU) 2026/1744 Art 1(41)(b).

For Section B products, Art 2(2) as amended limits the AI Act to Art 6(1), Art 60a and Arts 102 to 112; Arts 57, 58, 59 apply only in so far as the high-risk requirements have been integrated into the sectoral legislation. The substantive requirements reach machinery through delegated acts amending Annex III to Regulation (EU) 2023/1230, to apply by 2 August 2028 (Reg (EU) 2026/1744 recital 42).

## Route 2 — Art 6(2), Annex III

Eight areas. Read the exact wording, not the heading.

**1. Biometrics**, in so far as use is permitted under Union or national law:
(a) remote biometric identification — **excluding** systems whose sole purpose is biometric **verification** confirming a person is who they claim to be;
(b) biometric categorisation according to sensitive or protected attributes or characteristics, based on inference of those attributes;
(c) emotion recognition.

**2. Critical infrastructure** — safety components in the management and operation of critical digital infrastructure, road traffic, or the supply of water, gas, heating or electricity. Note: point 2 systems are registered at national level, not in the EU database (Art 49(5)), and are excluded from the Art 27 FRIA duty.

**3. Education and vocational training** — (a) determining access, admission or assignment to institutions at all levels; (b) evaluating learning outcomes, including where used to steer the learning process; (c) assessing the appropriate level of education a person will receive or access; (d) monitoring and detecting prohibited behaviour of students during tests.

**4. Employment, workers' management and access to self-employment** — (a) recruitment or selection, in particular placing targeted job advertisements, analysing and filtering applications, and evaluating candidates; (b) decisions affecting terms of work-related relationships, promotion or termination, allocating tasks based on individual behaviour or personal traits or characteristics, or monitoring and evaluating performance and behaviour.

**5. Access to and enjoyment of essential private and public services** — (a) public authorities evaluating eligibility for essential public assistance benefits and services including healthcare, and granting, reducing, revoking or reclaiming them; (b) evaluating creditworthiness or establishing credit score, **except** systems used for detecting financial fraud; (c) risk assessment and pricing for **life and health insurance** in relation to natural persons; (d) evaluating and classifying emergency calls, dispatching or prioritising emergency first response, and emergency healthcare patient triage.

**6. Law enforcement**, **7. Migration, asylum and border control**, **8. Administration of justice and democratic processes** — see the Annex text; rarely relevant to commercial product teams, and mostly reserved to public authorities or those acting on their behalf.

Product-team traps in this list:

- Point 4(a) covers **targeted job advertisements**, not only screening. An ad-targeting model pointed at job ads is in.
- Point 4(b) covers **task allocation based on individual behaviour or traits** and **performance and behaviour monitoring**. Workforce management and productivity analytics sit here.
- Point 5(b) covers credit scoring in general, not only regulated lending. A "pay later" eligibility model is in; fraud detection is expressly out.
- Point 5(c) is limited to **life and health** insurance. Motor and property pricing is not in Annex III.
- Point 3(b) covers evaluating learning outcomes even in a consumer edtech product.
- Point 1(a) excludes verification-only biometrics — the common login use case.

## The Art 6(3) filter

By derogation from Art 6(2), an Annex III system is **not** high-risk where it does not pose a significant risk of harm to health, safety or fundamental rights, **including by not materially influencing the outcome of decision making**, and where **any** of the following conditions is fulfilled:

- (a) the system is intended to perform a **narrow procedural task**;
- (b) it is intended to **improve the result of a previously completed human activity**;
- (c) it is intended to **detect decision-making patterns or deviations** from prior decision-making patterns and is **not meant to replace or influence the previously completed human assessment, without proper human review**;
- (d) it is intended to perform a **preparatory task** to an assessment relevant to an Annex III use case.

Two things are routinely misread:

1. The chapeau is cumulative with the conditions. Meeting condition (a) to (d) is necessary but not sufficient — the system must also not pose a significant risk and not materially influence the decision outcome.
2. Condition (c) is not "we have a human in the loop". It requires that the system is **not meant to replace or influence** the previously completed human assessment. A reviewer who accepts the model's output by default does not save the classification.

**The profiling override.** Art 6(3), third subparagraph:

> Notwithstanding the first subparagraph, an AI system referred to in Annex III shall always be considered to be high-risk where the AI system performs profiling of natural persons.

Profiling takes its GDPR Art 4(4) meaning: any form of automated processing of personal data consisting of the use of personal data to evaluate certain personal aspects relating to a natural person, in particular to analyse or predict aspects concerning performance at work, economic situation, health, personal preferences, interests, reliability, behaviour, location or movements. Almost any per-person scoring in an Annex III area is profiling. This is where most "we filtered out of high-risk" arguments fail.

## Documenting an Art 6(3) conclusion

Art 6(4): a provider who considers that an Annex III system is not high-risk **shall document its assessment before that system is placed on the market or put into service**, is subject to the registration obligation in Art 49(2), and shall provide the documentation to national competent authorities on request.

That means a "not high-risk" conclusion is a filed, public position in the EU database, not an internal memo. Template in `artefacts-records.md`.

## Amendments to Annex III

Art 7(1): the Commission may add or modify use cases by delegated act where the systems are in an Annex III area and pose an equivalent or greater risk than those already listed, assessed against the eleven criteria in Art 7(2). Art 7(3): removal is possible where the risk is gone and overall protection is not decreased. Re-check Annex III at each significant product review; it is a moving list.

## Checkpoints

- [ ] Both routes tested, not just Annex III
- [ ] For Art 6(1): safety-component test run against Art 3(14) as amended and Art 6(1a) to (1c)
- [ ] Annex I Section A vs Section B identified, with the Art 2(2) limitation applied for Section B
- [ ] Annex III checked against the exact sub-point wording, including the verification and fraud-detection exclusions
- [ ] Art 6(3) chapeau assessed separately from conditions (a) to (d)
- [ ] Profiling assessed against GDPR Art 4(4) and stated explicitly
- [ ] Any "not high-risk" conclusion accompanied by an Art 6(4) documented assessment and an Art 49(2) registration action
- [ ] Applicable date recorded: 2 December 2027 or 2 August 2028
- [ ] Boundary calls routed to legal sign-off

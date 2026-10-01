# Intake

Answer before any classification, artefact or advice. Missing answers become `[[MISSING: …]]` in the artefact and in the report back to the user. Never guess a model name, a compute figure, a metric, a jurisdiction or a customer segment.

Run this once per **AI system**, not once per company. A company with three AI features runs it three times. Role and risk class attach per system (Art 3(3), 3(4) AI Act).

## 1. The system itself

1. What does the system do, in one sentence a non-engineer would recognise?
2. What is the **intended purpose** as it will be stated in marketing, contract and documentation? This is the legal anchor for classification (Art 3(12)) and for the Art 6(3) filter.
3. Does it infer outputs from inputs — predictions, content, recommendations, decisions — with some autonomy, or is it deterministic rule-based logic? (Art 3(1); Commission Guidelines on the definition of an AI system, C(2025) 5053 final, 29.7.2025, first published 6 February 2025.)
4. Model or models used: name, version, provider, hosting location, whether hosted by you or called via API.
5. Was any model trained, fine-tuned, distilled, quantised or otherwise modified by you? If yes: what changed, on what data, with roughly what training compute?
6. Does the system generate synthetic audio, image, video or text as user-visible output? List every modality.
7. Does the system interact directly with natural persons (bidirectional exchange, conversational or responsive), or does it only produce output that a human later disseminates?
8. Is it an agent — does it take actions on a person's behalf (bookings, purchases, correspondence, contract conclusion)?
9. Is the system a component of, or itself, a physical product?

## 2. Placement and roles

10. Under whose name or trademark is the system placed on the market or put into service? (Art 3(3): that party is the provider.)
11. Is the system placed on the market, put into service, or only used internally?
12. Are you using someone else's AI system under your own authority (deployer, Art 3(4)), reselling it (distributor, Art 3(7)), importing it from a third-country provider (importer, Art 3(6)), or all of these for different systems?
13. Do you put your name or trademark on a third-party system, substantially modify one, or change its intended purpose? (Art 25(1)(a) to (c) — this makes you the provider.)
14. Is the provider established outside the EU? If so, is an authorised representative appointed (Art 22 for systems, Art 54 for GPAI models)?

## 3. Territorial reach

15. Where are the users? Where is the company established?
16. Is the output of the system used in the Union, even if neither provider nor deployer is established there? (Art 2(1)(c).)
17. Which Member States are targeted, and in which languages is the interface offered?

## 4. Exclusions to test

18. Is the system used exclusively for military, defence or national security purposes? (Art 2(3).)
19. Is it developed and put into service for the sole purpose of scientific research and development? (Art 2(6).)
20. Is it still pre-market research, testing or development — and does that include testing in real-world conditions? (Art 2(8); real-world testing is *not* excluded.)
21. Is it released under a free and open-source licence, and if so are weights, architecture and usage information public? (Art 2(12) for systems; Art 53(2), Art 54(6) for models.)
22. Are the deployers natural persons using it in a purely personal, non-professional activity? (Art 2(10).)

## 5. Prohibition screen

23. Does the system infer emotions of natural persons in the workplace or in education institutions? (Art 5(1)(f).)
24. Does it categorise people by biometric data to deduce race, political opinion, trade union membership, religion, philosophical belief, sex life or sexual orientation? (Art 5(1)(g).)
25. Does it build or expand facial recognition databases by untargeted scraping of images from the internet or CCTV? (Art 5(1)(e).)
26. Does it score people on social behaviour or personality characteristics with detrimental consequences in unrelated contexts? (Art 5(1)(c).)
27. Does it use subliminal, purposefully manipulative or deceptive techniques, or exploit age, disability or a specific social or economic situation? (Art 5(1)(a), (b).)
28. Can it generate or manipulate intimate imagery of identifiable persons, or material within Directive 2011/93/EU? Consider both intended purpose and reasonably foreseeable, reproducible outcomes without significant technical modification. (Art 5(1)(ba), (bb) and 5(1a), inserted by Reg (EU) 2026/1744, applicable from 2 December 2026.)

## 6. High-risk screen

29. Is the system a safety component of, or itself, a product covered by the Union harmonisation legislation in Annex I, and does that product require third-party conformity assessment? (Art 6(1).)
30. Does the intended use fall in any Annex III area: biometrics; critical infrastructure; education and vocational training; employment and worker management; access to essential private and public services (including creditworthiness and life/health insurance pricing); law enforcement; migration, asylum, border control; administration of justice and democratic processes?
31. If yes to 30: does the system perform **profiling** of natural persons? (Art 6(3), third subparagraph — profiling always means high-risk.)
32. If yes to 30 and no to 31: does it perform only a narrow procedural task, only improve the result of a completed human activity, only detect decision-making patterns without replacing or influencing the human assessment, or only perform a preparatory task? (Art 6(3), second subparagraph.)

## 7. Data and personal data

33. What personal data does the system process, at training, at inference and in logs?
34. Are special categories under GDPR Art 9 involved, including for bias detection and correction? (Art 4a AI Act, inserted by Reg (EU) 2026/1744, is the AI Act's own legal basis for that narrow case.)
35. Are there automated decisions producing legal or similarly significant effects on individuals? (GDPR Art 22.)
36. Is a DPIA required or already done? (GDPR Art 35 — can be cross-referenced from an Art 27 FRIA.)

## 8. Operations

37. What logs does the system produce automatically, what do they contain, and how long are they retained?
38. Who exercises human oversight, with what competence, training and authority, and can they actually stop the system? (Art 14(4)(e), Art 26(2).)
39. Is there a documented process for serious incidents and for informing the provider? (Art 26(5), Art 73.)
40. Is there a quality management system, or an existing ISO 9001 / ISO/IEC 42001 / medical-device QMS that could absorb Art 17?

## 9. Company facts needed for artefacts

41. Legal name, address, and contact point of the provider.
42. Authorised representative, if the provider is outside the Union.
43. Company size: SME under Recommendation 2003/361/EC, or small mid-cap under Recommendation (EU) 2025/1099? (Determines simplified technical documentation under Art 11(1), simplified QMS under Art 63(1), and the lower of percentage-or-amount fine cap under Art 99(6) and (6a).)
44. Are there partner or linked enterprises? (Art 63(1) as amended excludes them from the simplified QMS route.)
45. Is the company also a provider of an online platform or search engine designated under the DSA? (Affects who supervises: Art 75(1)(b) as amended.)

## Checkpoints

- [ ] Run once per AI system, not once per company
- [ ] Intended purpose written down in the words that will appear in contract and documentation
- [ ] Every model, including upstream API models, named with version
- [ ] Territorial trigger under Art 2(1) identified explicitly
- [ ] Every claimed exclusion mapped to its paragraph of Art 2
- [ ] Prohibition screen answered for all six existing points and both 2026 additions
- [ ] Annex III areas checked one by one, not skimmed
- [ ] Profiling question answered explicitly, yes or no
- [ ] Unanswered items carried forward as `[[MISSING: …]]`, not filled in plausibly

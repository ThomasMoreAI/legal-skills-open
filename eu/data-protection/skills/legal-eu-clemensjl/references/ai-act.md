# AI Act — Regulation (EU) 2024/1689

Status as at 2026-08-05.

Regulation (EU) 2024/1689 (Artificial Intelligence Act), in force since 01.08.2024, amended by **Regulation (EU) 2026/1744** (Digital Omnibus on AI), signed 08.07.2026, published in the OJ 24.07.2026, in force 27.07.2026.

A Regulation. Directly applicable, identical wording in all 27 member states. National law supplies only the market surveillance authority, the notifying authority and the procedural side of penalties (Art 70, Art 99(1)). A national skill adds the authority names, not the substance.

## What actually catches an ordinary product

Most software is not high-risk and never will be. The provisions that reach a normal SaaS product, website or app are, in order of likelihood:

1. **Art 50 transparency** — chatbots, synthetic content, deepfakes. This is the one products trip over.
2. **Art 4 AI literacy** — applies to every provider and deployer, no risk tier.
3. **Art 5 prohibitions** — rarely relevant, but absolute when it bites.
4. **Art 6 / Annex III high-risk** — only if the system is used for recruitment, worker management, credit scoring, education access, essential services, biometrics, law enforcement, migration or justice.

## Application timeline

| Date | What starts to apply | Basis |
|---|---|---|
| 01.08.2024 | Entry into force | Art 113 |
| 02.02.2025 | Ch I (incl. Art 4 AI literacy) and Ch II (Art 5 prohibited practices) | Art 113(a) |
| 02.08.2025 | Ch V GPAI models, Ch VII governance, notifying authorities and notified bodies, confidentiality, penalties | Art 113(b) |
| **02.08.2026** | **The rest of the Regulation, including Art 50 transparency** | Art 113 |
| 02.12.2026 | New Art 5 prohibition on AI systems generating CSAM and non-consensual sexual or intimate imagery; grace period for marking content from systems already on the market | Reg (EU) 2026/1744 |
| **02.12.2027** | Annex III standalone high-risk systems — **moved from 02.08.2026** | Reg (EU) 2026/1744 |
| **02.08.2028** | Annex I product-embedded high-risk systems (machinery, toys, medical devices …) | Reg (EU) 2026/1744 |
| 02.08.2027 | GPAI models placed on the market before 02.08.2025 must be brought into compliance | Art 111(3) |

The two high-risk delays are the single most important recent change. A skill or template that still says "high-risk obligations apply from 2 August 2026" is out of date by Regulation (EU) 2026/1744.

## Scope — Art 2

Art 2(1) catches:

- (a) providers placing AI systems or GPAI models on the Union market or putting them into service, **irrespective of establishment**
- (b) deployers established or located in the Union
- (c) providers and deployers in a third country **where the output produced by the system is used in the Union**
- (d) importers and distributors
- (e) product manufacturers placing an AI system on the market with their product under their own name or trademark
- (f) authorised representatives of non-EU providers
- (g) affected persons located in the Union

Exclusions that matter in practice: purely personal non-professional use (Art 2(10)); scientific research and development (Art 2(6)); pre-market research, testing and development other than real-world testing (Art 2(8)); free and open-source released systems — but the exclusion **falls away** where the system is high-risk or falls under Art 5 or Art 50 (Art 2(12)).

"Provider" and "deployer" are different roles with different duties. A company that buys a chatbot and puts it on its website is a **deployer**, not a provider — unless it puts its own name on it, which makes it a provider (Art 25).

## Art 50 — transparency obligations

Applies from 02.08.2026. Four situations:

| Paragraph | Who | Duty |
|---|---|---|
| 50(1) | Provider | AI systems intended to interact directly with natural persons must be designed so the person is informed they are interacting with an AI system, unless this is obvious to a reasonably well-informed person |
| 50(2) | Provider | Systems generating synthetic audio, image, video or text must mark outputs in a **machine-readable format** and make them detectable as artificially generated or manipulated; solutions must be effective, interoperable, robust and reliable as far as technically feasible |
| 50(3) | Deployer | Emotion recognition or biometric categorisation: inform the exposed persons, and process the personal data in line with the GDPR |
| 50(4) | Deployer | Deepfakes: disclose that the content has been artificially generated or manipulated. AI-generated or manipulated **text published to inform the public on matters of public interest**: disclose, unless it went through human review or editorial control with a person or legal entity holding editorial responsibility |

Art 50(5): the information must be given clearly and distinguishably **at the latest at the time of the first interaction or exposure**, and must meet the applicable accessibility requirements.

Exceptions: systems authorised by law to detect, prevent, investigate or prosecute criminal offences; assistive editing functions that do not substantially alter the input data; artistic, creative, satirical or fictional works, where the disclosure is made in an appropriate manner that does not hamper display or enjoyment of the work (Art 50(4)).

**Commission guidelines on Art 50 transparency obligations were adopted 20.07.2026.** A **Code of Practice on marking and labelling AI-generated content** was published in final form on 10.06.2026 and assessed as adequate by the Commission and the AI Board on 08–09.07.2026; adherence is the recognised route to demonstrating compliance with Art 50(2), (4) and (5), but it is voluntary and other equally adequate means are open.

Practical consequences for an ordinary product:

- A support chatbot needs a persistent, visible statement that the user is talking to an AI. A one-off line in the terms is not "at the time of the first interaction".
- A feature that generates images, audio, video or text for users triggers Art 50(2) marking on the **provider** of that generative system. If a product merely calls a third-party model API and passes the output to users, work out who is provider and who is deployer before assigning the duty.
- AI-written blog posts on matters of public interest need disclosure unless a named human took editorial responsibility.
- Art 50 breaches are sanctioned under Art 99(4): up to EUR 15 000 000 or 3 % of total worldwide annual turnover, whichever is higher.

## Art 4 — AI literacy

Applies since 02.02.2025 to **every** provider and deployer, regardless of risk tier. There is no exemption for small companies. Regulation (EU) 2026/1744 reworded Art 4: the obligation is now to take measures supporting the development of a sufficient level of AI literacy, taking account of technical knowledge, experience, education and training and the context of use — an obligation of effort rather than a guaranteed outcome. [[UNVERIFIED: the exact amended wording of Art 4 — read the consolidated text of Reg (EU) 2024/1689 as amended by Reg (EU) 2026/1744 before quoting it]]

In practice: documented internal training or briefing for staff who build or operate AI systems. No certificate, course or standard is prescribed.

## Art 5 — prohibited practices

Since 02.02.2025. The ones that can catch a commercial product:

- subliminal, purposefully manipulative or deceptive techniques that materially distort behaviour and cause or are likely to cause significant harm
- exploiting vulnerabilities due to age, disability or a specific social or economic situation
- social scoring leading to detrimental treatment in unrelated contexts or disproportionate treatment
- inferring emotions in the workplace or in education institutions, except for medical or safety reasons
- biometric categorisation to deduce race, political opinions, trade union membership, religious or philosophical beliefs, sex life or sexual orientation
- untargeted scraping of facial images from the internet or CCTV to build facial recognition databases

Added by Reg (EU) 2026/1744, applicable 02.12.2026: AI systems used to generate child sexual abuse material or non-consensual sexual or intimate imagery — both placing on the market and use.

Penalty: up to EUR 35 000 000 or 7 % of worldwide annual turnover, whichever is higher (Art 99(3)).

## High-risk — Art 6 and Annex III

Annex III categories: biometrics; critical infrastructure; education and vocational training; employment, worker management and access to self-employment; access to and enjoyment of essential private and public services and benefits, including creditworthiness and life/health insurance risk assessment; law enforcement; migration, asylum and border control; administration of justice and democratic processes.

Art 6(3) filter: a system in an Annex III category is **not** high-risk if it performs only a narrow procedural task, improves the result of a previously completed human activity, detects decision patterns without replacing or influencing human assessment, or performs a preparatory task. The provider must document that assessment and register the system before placing it on the market (Art 6(4)).

An HR product that screens or ranks candidates is Annex III point 4. A credit-scoring feature is Annex III point 5. Both now bite from 02.12.2027, not 02.08.2026.

## Penalties — Art 99

| Breach | Ceiling |
|---|---|
| Art 5 prohibited practices | EUR 35 m or 7 % worldwide annual turnover |
| Obligations of providers (Art 16), authorised representatives (Art 22), importers (Art 23), distributors (Art 24), deployers (Art 26), notified bodies (Arts 31, 33, 34), **and Art 50 transparency** | EUR 15 m or 3 % |
| Incorrect, incomplete or misleading information to notified bodies or authorities | EUR 7.5 m or 1 % |
| SMEs and start-ups | the **lower** of the percentage and the fixed amount (Art 99(6)) |

## Template — AI disclosure block

```html
<!-- DRAFT – NOT LEGALLY APPROVED -->
<h2>Use of artificial intelligence</h2>
<p>
  [[PRODUCT NAME]] uses AI systems in the following features:
  [[LIST FEATURES: e.g. support chat, content generation, search ranking]].
</p>
<p>
  You are interacting with an AI system when you use [[FEATURE]].
  Answers may be incorrect. [[HUMAN ESCALATION ROUTE]].
</p>
<p>
  Content produced by [[GENERATIVE FEATURE]] is artificially generated and is
  marked as such in a machine-readable format.
</p>
<p>
  Provider of the AI system: [[PROVIDER NAME]].
  Underlying model: [[MODEL / SUPPLIER]].
</p>
```

The chatbot disclosure itself belongs **in the chat interface at first interaction**, not only on this page (Art 50(5)).

## Checkpoints

- [ ] Inventory of every AI system in the product, with the role taken for each: provider or deployer (Art 3(3), 3(4))
- [ ] Any Art 5 practice ruled out in writing, including the emotion-inference-at-work prohibition
- [ ] Annex III screening done; if in a category, the Art 6(3) filter assessed and documented
- [ ] Chatbot discloses AI at first interaction, visibly, inside the interface (Art 50(1), 50(5))
- [ ] Generative outputs marked machine-readably by the provider of the generating system (Art 50(2))
- [ ] Deepfake and public-interest-text disclosures in place where applicable (Art 50(4))
- [ ] Emotion recognition or biometric categorisation: exposed persons informed, GDPR basis identified (Art 50(3))
- [ ] AI literacy measures documented for staff (Art 4)
- [ ] Timeline in any compliance plan reflects Reg (EU) 2026/1744: Annex III 02.12.2027, Annex I 02.08.2028 — not 02.08.2026
- [ ] Third-country provider or deployer whose output is used in the Union: scope under Art 2(1)(c) confirmed
- [ ] Open-source exclusion not relied on for a high-risk, Art 5 or Art 50 system (Art 2(12))
- [ ] All `[[…]]` placeholders resolved or reported as open

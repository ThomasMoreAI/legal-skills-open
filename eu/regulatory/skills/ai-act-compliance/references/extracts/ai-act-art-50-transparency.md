# Extract — AI Act Article 50: Transparency obligations

**Source**: `sources.yaml` id `ai-act-en-eurlex`
**Document**: Regulation (EU) 2024/1689
**Accessed**: 2026-04-25
**Licence**: EU legislative text — public domain
**Citation**: Regulation (EU) 2024/1689, Art. 50
**Application**: **in force since 2 August 2026** — the general application date in Art. 113, first subparagraph (Art. 113(c) governs the Chapter III high-risk schedule, not Article 50). Article 50 was **not** deferred by Reg. (EU) 2026/1744 (Digital Omnibus on AI), which moved only the Chapter III high-risk dates. Single transitional relief: generative AI systems placed on the market or put into service before 2 August 2026 have until **2 December 2026** to comply with the Art. 50(2) marking and detection duty. See `digital-omnibus-ai-2026` and `ec-art50-transparency-guidelines` in `sources.yaml`.

---

## Article 50 — Transparency obligations for providers and deployers of certain AI systems

**1.** Providers shall ensure that **AI systems intended to interact directly with natural persons are designed and developed in such a way that the natural persons concerned are informed that they are interacting with an AI system**, unless this is **obvious from the point of view of a natural person who is reasonably well-informed, observant and circumspect**, taking into account the circumstances and the context of use. This obligation shall not apply to AI systems authorised by law to detect, prevent, investigate or prosecute criminal offences, subject to appropriate safeguards for the rights and freedoms of third parties, unless those systems are available for the public to report a criminal offence.

**2.** Providers of AI systems, including general-purpose AI systems, generating **synthetic audio, image, video or text content**, shall ensure that the **outputs of the AI system are marked in a machine-readable format and detectable as artificially generated or manipulated**. Providers shall ensure their technical solutions are effective, interoperable, robust and reliable as far as this is technically feasible, taking into account the specificities and limitations of various types of content, the costs of implementation and the generally acknowledged state of the art, as may be reflected in relevant technical standards. **This obligation shall not apply to the extent the AI systems perform an assistive function for standard editing or do not substantially alter the input data provided by the deployer or the semantics thereof, or where authorised by law to detect, prevent, investigate or prosecute criminal offences.**

**3.** Deployers of an **emotion recognition system** or a **biometric categorisation system** shall **inform the natural persons exposed thereto of the operation of the system**, and shall process the personal data in accordance with Regulations (EU) 2016/679 and (EU) 2018/1725 and Directive (EU) 2016/680, as applicable. **This obligation shall not apply to AI systems used for biometric categorisation and emotion recognition, which are permitted by law to detect, prevent or investigate criminal offences, subject to appropriate safeguards for the rights and freedoms of third parties, and in accordance with Union law.**

**4.** Deployers of an AI system that **generates or manipulates image, audio or video content constituting a deep fake**, shall **disclose that the content has been artificially generated or manipulated**. **This obligation shall not apply where the use is authorised by law to detect, prevent, investigate or prosecute criminal offence.** **Where the content forms part of an evidently artistic, creative, satirical, fictional or analogous work or programme, the transparency obligations set out in this paragraph are limited to disclosure of the existence of such generated or manipulated content in an appropriate manner that does not hamper the display or enjoyment of the work.**

Deployers of an AI system that generates or manipulates **text** which is **published with the purpose of informing the public on matters of public interest** shall **disclose that the text has been artificially generated or manipulated**. **This obligation shall not apply where the use is authorised by law to detect, prevent, investigate or prosecute criminal offences or where the AI-generated content has undergone a process of human review or editorial control and where a natural or legal person holds editorial responsibility for the publication of the content.**

**5.** The information referred to in paragraphs 1 to 4 shall be provided to the natural persons concerned **in a clear and distinguishable manner at the latest at the time of the first interaction or exposure**. The information shall conform to the **applicable accessibility requirements**.

**6.** Paragraphs 1 to 4 shall not affect the requirements and obligations set out in Chapter III, and shall be without prejudice to other transparency obligations laid down in Union or national law for deployers of AI systems.

**7.** The AI Office shall encourage and facilitate the drawing up of **codes of practice** at Union level to facilitate the effective implementation of the obligations regarding the detection and labelling of artificially generated or manipulated content. The Commission may adopt implementing acts to approve those codes of practice in accordance with the procedure laid down in Article 56(6). If it deems the code is not adequate, the Commission may adopt an implementing act specifying common rules for the implementation of those obligations in accordance with the examination procedure laid down in Article 98(2).

---

## Notes for the skill

- Article 50 applies to **all AI systems** triggering the four blocks, regardless of risk classification. A "minimal-risk" system that is a chatbot still triggers 50(1).
- Addressee differs by paragraph:
  - 50(1) — provider duty (design and develop the system to inform users)
  - 50(2) — provider duty (mark outputs machine-readable)
  - 50(3) — deployer duty (inform persons subject to emotion recognition / biometric categorisation)
  - 50(4) — deployer duty (disclose deep fakes; disclose AI-generated text on public-interest matters)
- "Obvious from the point of view of a reasonably well-informed person" exception (50(1)) is fact-specific. Don't rely on it for ambiguous cases.
- Machine-readable marking (50(2)) — track CEN-CENELEC standards and C2PA Content Credentials as the leading interoperable approach.
- Editorial-responsibility exception in 50(4) text branch shields newsrooms with proper review processes; pure AI-published content needs disclosure.
- Penalties: up to **EUR 15 000 000 or 3% of total worldwide annual turnover** (Art. 99(4)).
- For the Commission's interpretation of each block, read [`ec-art50-transparency-guidelines.md`](ec-art50-transparency-guidelines.md) — the adopted Guidelines of 20 July 2026 (C(2026) 5054 final). They are the Commission's official reading but are **non-binding**; the norm remains Article 50 itself, and only the CJEU can interpret it authoritatively.

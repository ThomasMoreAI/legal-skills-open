# Art 50 transparency — the tier most products land in

Basis: Regulation (EU) 2024/1689 Art 50, with Art 50(7) as replaced by Regulation (EU) 2026/1744 Art 1(20). Commission Guidelines on the implementation of the transparency obligations for certain AI systems under Article 50, **C(2026) 5054 final, 20.7.2026** (non-binding). Code of Practice on Transparency of AI-Generated Content, published **10 June 2026**, roughly 190 signatories as at late July 2026.

**Applicable since 2 August 2026.** Single transitional: Art 111(4), inserted by Reg (EU) 2026/1744 Art 1(39)(b) — providers of systems generating synthetic audio, image, video or text **placed on the market before 2 August 2026** have until **2 December 2026** for Art 50(2). It covers Art 50(2) only; a partly interactive, partly generative system had to satisfy Art 50(1) on 2 August 2026 (Guidelines, point 153).

Penalty: EUR 15 000 000 or 3 % of total worldwide annual turnover, whichever is higher (Art 99(4)(g)); for SMEs and SMCs, whichever is lower (Art 99(6), (6a)).

Art 50(6): paragraphs 1 to 4 do not affect Chapter III and are without prejudice to other transparency obligations in Union or national law. A high-risk system can owe both.

## Who owes what

| Para | Duty | Owed by |
|---|---|---|
| 50(1) | Inform natural persons that they are interacting with an AI system | **Provider**, by design |
| 50(2) | Mark outputs in a machine-readable format **and** make them detectable as artificially generated or manipulated | **Provider** |
| 50(3) | Inform persons exposed to an emotion recognition or biometric categorisation system of its operation | **Deployer** |
| 50(4) 1st | Disclose that image, audio or video content constituting a **deep fake** is artificially generated or manipulated | **Deployer** |
| 50(4) 2nd | Disclose that text published to inform the public on matters of public interest is artificially generated or manipulated | **Deployer** |
| 50(5) | All of the above: clear and distinguishable, at the latest at the time of first interaction or exposure, conforming to applicable accessibility requirements | Both |

## Art 50(1) — interaction disclosure

Four cumulative elements (Guidelines, point 30):

1. **An AI system** under Art 3(1). Excludes simple non-AI automated response mechanisms — traditional out-of-office replies, rule-based quick answers.
2. **Intended to interact**: bidirectional exchange of information or actions with genuine conversational or responsive character. May be a single prompt-and-reply or multi-turn. Systems that only passively collect data (automated facial-recognition access control) or take one-time feedback (spam filters) do not interact.
3. **Directly**: real-time or near real-time. Excludes mediated exposure — a support agent using an AI assistance tool to draft their own replies is not direct interaction. But blending AI-generated responses with human-curated content **is** in scope for the AI-generated parts, unless those outputs have been properly reviewed and sent by humans as the main interlocutors. The mere possibility of human review does not defeat the duty.
4. **With natural persons**: professional deployers, other users, or persons acting on their behalf. Backend machine-to-machine calls between AI systems whose outputs are not intended to reach a natural person are out.

**Agents** are in scope where they can interact with the persons instructing them or with other natural persons while executing tasks — bookings, correspondence, negotiating or concluding contracts, purchases. Guidelines point 31: agents must disclose **both their artificial nature and the person on whose behalf they act**, including in multi-agent architectures.

### The "obvious" exception

Art 50(1) does not apply where the interaction is obvious "from the point of view of a natural person who is reasonably well-informed, observant and circumspect, taking into account the circumstances and the context of use". The Guidelines (points 42 to 45) build this on the consumer-law average-consumer standard and read it **restrictively**:

- Identify the target audience **and the broader reasonably foreseeable audience**. Where persons with disabilities, elderly people or minors are likely in the audience, the expected level of information and circumspection is lower.
- General public awareness that chatbots exist does not mean people recognise them in a given interaction.
- Factors decreasing obviousness: human-sounding voice, human profile picture, high-quality personalised interaction, faithful replication of a non-artificial equivalent.
- Factors increasing obviousness: professional or specialised audience only, visible mechanical components, obvious robot voice or writing patterns.

In practice, a consumer-facing chatbot with a human name and avatar cannot rely on the exception. Do not draft an argument that it can without legal sign-off.

Second exception: systems authorised by law to detect, prevent, investigate or prosecute criminal offences, with safeguards, unless the system is available for the public to report an offence.

## Art 50(2) — machine-readable marking and detection

Two elements, both mandatory (Guidelines, points 69 to 70): the outputs must be **marked in a machine-readable format**, and they must be **detectable** as artificially generated or manipulated. For every marking technique deployed, a corresponding means of detection must be available. Marking without detection does not comply.

Quality standard, from the Article itself: technical solutions must be **effective, interoperable, robust and reliable** as far as technically feasible, taking into account the specificities and limitations of various types of content, the costs of implementation and the generally acknowledged state of the art, as may be reflected in relevant technical standards.

### What is out of scope

Guidelines points 64 to 68. This is where most product teams get relief:

- Content from simple data processing that is not specifically AI-generated or manipulated — a rendered frame.
- Output that merely reproduces, presents or arranges existing content: music playlists, recommender systems that only select or rank existing content, internal analytical processes that extract and structure data without summarising it.
- Mere observations and recordings from physical or virtual environments: robot sensor data, smart-meter consumption, grid measurements, GPS traces.
- **Short sequences**: single words, image captions, alt-text, UI labels, icon-scale graphics, other data labels.
- **Source code** — content in a programming, scripting, markup, query or configuration language intended to be interpreted, compiled or executed, including integral natural-language comments. Expressly listed: SDKs, SQL, infrastructure-as-code, YAML, JSON configuration, schemas, scripts, machine-readable specifications, APIs and software libraries.
- Output exclusively communicated machine-to-machine and processed automatically without human exposure, including agent-to-agent communication and anti-spam signals.
- Output used only in closed-loop industrial or product-development workflows (film, animation, games, advertising production) — only the **final** output has to be marked.

Proportionality relief, not a formal exception (Guidelines points 86 to 88):

- Generative systems **embedded in physical products** producing output in a technically controlled and closed, mainly instructive environment (e.g. in-vehicle navigation), where technical measures prevent the output leaving the product: less robust metadata marking may suffice.
- Narrow **industrial or B2B** cases: no marking required where cumulatively the output is strictly technical, is only perceived by a limited pre-defined number of professionals inside the provider's and deployer's organisation, and is not intended to be shared outside or usable externally, with safeguards such as cloud isolation and role-based controls.
- **Ephemeral real-time generation** consumed immediately without recording, storage or dissemination (games, VR) may be exempt where marking is not technically feasible and persons are made aware by in-experience or session-level disclosure.

### The three statutory exceptions in Art 50(2)

1. The system performs an **assistive function for standard editing**. Guidelines point 90: standard editing is preparing existing content for publication or distribution — small edits for readability, grammar, quality, format, layout, accessibility conformity, sectoral practice — and does not involve generating new content. Editing that changes content materially, affecting meaning, style or intent, is beyond standard editing.
2. The system **does not substantially alter the input data provided by the deployer or the semantics thereof**. Guidelines point 91: substantial means the input or its semantics have been manipulated significantly during output generation, assessed on format, media type, style and changes affecting meaning, style or intent. Case-specific.
3. Authorised by law to detect, prevent, investigate or prosecute criminal offences.

## What machine-readable marking means in practice

The Code of Practice on Transparency of AI-Generated Content (10 June 2026) is the only Union-wide recognised practical framework (Guidelines, point 146). Section 1 binds signatories as providers.

**Commitment 1, Measure 1.1 — multi-layered marking.** For audio, images, video and containerised text, at least **two layers**:

- **Sub-measure 1.1.1, digitally signed metadata.** Where the format supports attaching metadata, record in the metadata whether the content is AI-generated or manipulated. All recorded information must be **digitally signed and time-stamped in a secure and tamper-evident manner**, with secure handling of signing certificates and private keys, except where the deployment context does not permit secure key provisioning (local deployment).
- **Sub-measure 1.1.2, imperceptible watermarking.** Embed an imperceptible watermark, difficult to separate from the content, except for very short text. **For free-form text longer than 200 tokens, watermarking must still be applied**, even at lower reliability; access to the corresponding detection solution may be restricted to verified expert users. Model-level watermarking is encouraged over post-hoc watermarking, so that downstream providers inherit it.
- **Sub-measure 1.1.3, fingerprinting or logging — optional and never sufficient alone.** May supplement; relying on it alone does not meet the quality requirements. Where used, it must be limited to output data, privacy-preserving, with deployer access to logging policies and control over what is logged, retention limits, access controls and secure deletion.

Single-layer marking is enough only in two cases: a generative system embedded in a physical product in a controlled closed environment with technical measures preventing export; and **free-form text**, which cannot carry metadata, where Sub-measure 1.1.2 alone suffices.

**Measure 1.2 — non-removal.** Signatories preserve metadata markings on inputs and outputs, retain them, and abstain from intentionally altering or removing existing metadata markings, except where transformation or replacement is necessary to keep the information accurate.

**Commitment 2 — detection.** A detection mechanism must be available, with results indicating whether they rest on metadata marking, watermark marking, forensic detection or another technique.

**Measure 3.4 — interoperability, staged.** At the entry into application of Art 50(2), signatories adopt established standards or best practices for metadata marking and detection, and publish information on how to integrate and access their detection solutions. By **2 February 2027** they must implement an interoperability solution for their detection mechanisms — an interoperable industry-standard access method for routing detection queries, a publicly readable signpost in the content indicating which detection solution to use, a shared consortium detection solution open to other signatories including SMEs and SMCs, or another comparable solution.

**Commitment 4 — testing, verification, compliance.** An internal compliance process, testing and monitoring, training, and cooperation with market surveillance authorities. Pending recognised performance evaluation methods and benchmarks, signatories may demonstrate compliance through **documented internal testing** against the Commitment 3 requirements, subject to review by the authorities.

### C2PA and content credentials

The Code does **not** name C2PA, Content Credentials or any other named standard. It requires "relevant established standards or best practices" for metadata marking (Measure 3.4(a)). C2PA is the obvious candidate for the digitally signed metadata layer — its manifests are digitally signed and tamper-evident, which is exactly what Sub-measure 1.1.1 requires — but adopting C2PA alone does not discharge Art 50(2): it supplies one of the two required layers, and does not by itself supply the watermark layer, the detection mechanism, or the free-form-text case. Latest published C2PA specification line as at 2026-08-05: 2.x, with 2.4 available. [[UNVERIFIED: exact release date of C2PA 2.4 and whether any C2PA version has been adopted as a harmonised standard or cited in the OJ]]

## Art 50(3) — emotion recognition and biometric categorisation

Deployers must inform the natural persons exposed of the **operation of the system**, and process personal data in accordance with GDPR, Regulation (EU) 2018/1725 and Directive (EU) 2016/680 as applicable. Exception only for systems permitted by law to detect, prevent or investigate criminal offences, with safeguards.

Two things to keep straight: emotion inference in **workplace or education institutions** is prohibited outright under Art 5(1)(f) except for medical or safety reasons — Art 50(3) does not rescue it. And biometric categorisation deducing protected attributes is prohibited under Art 5(1)(g). Art 50(3) covers only the remaining lawful cases, and those are also Annex III point 1 high-risk.

## Art 50(4) — deepfake and published-text disclosure

**Deep fake**, Art 3(60): AI-generated or manipulated image, audio or video content that resembles existing persons, objects, places, entities or events and would falsely appear to a person to be authentic or truthful.

First subparagraph: the deployer discloses that the content has been artificially generated or manipulated. Exception for law-enforcement authorisation. Where the content forms part of an **evidently artistic, creative, satirical, fictional or analogous work or programme**, the duty is limited to disclosing the existence of such content **in an appropriate manner that does not hamper the display or enjoyment of the work**.

Second subparagraph: text published with the purpose of informing the public on matters of public interest must be disclosed as AI-generated or manipulated. Exceptions: law-enforcement authorisation, or where the content has undergone **human review or editorial control and a natural or legal person holds editorial responsibility** for the publication.

### How to label — Code of Practice Section 2

Signatories commit to use the **EU icon** in Annex 1 of the Code or an equivalent icon or label meeting the design and placement specifications.

Design, where visual disclosure is possible (Measure 1.1):

- Main visual element: the capitalised acronym **"AI"** in English, unless national language law requires otherwise; letters of the same vertical dimension; proportions preserved on resize.
- Encouraged: a second, possibly interactive layer distinguishing "generated" from "modified", and describing what was modified.
- Size and style may vary provided the disclosure stays clear, accessible, distinguishable, readable and recognisable.

Design, where visual disclosure is not possible (audio-only):

- A short **audible disclaimer at the beginning of the deep fake**, in plain natural language, in the content's language or English, disclosing artificial origin.
- Optionally complemented by whether it is generated or manipulated; an earcon or other audible solution is allowed if accompanied by awareness-raising measures.

Placement (Measure 1.2):

- Placed so as to ensure **immediate recognition without requiring user interaction or sustained attention**.
- Visible long enough to be noticed under normal exposure conditions.
- **Directly embedded into the content**, unless an equivalent alternative such as a UI overlay that appears to be on the content is used.
- Clearly perceivable and distinguishable at the latest at first exposure, with sufficient spacing from other overlay elements and readable against any background.
- Where visual disclosure is possible: in an appropriate place free of intervening overlay elements, for example the top right corner of an image or video.

Accessibility: the Code requires accessible disclosure taking account of Directive (EU) 2019/882 and Directive (EU) 2016/2102 — audio descriptions or alternative cues for visual elements, tactile or haptic cues for audio-only content, high-contrast icons and screen-reader compatibility, detectability by assistive technologies. ETSI EN 301 549 and WCAG 2.1 are named as reference guidance.

## Art 50(5) — how the information is given

Clear and distinguishable, at the latest at the time of **first interaction or exposure**, conforming to applicable accessibility requirements. Consequences: not behind a cookie banner, not in a terms-of-service link, not in a tooltip requiring hover, not only in a settings page, not only after the first message.

## Legal effect of the Code of Practice

Guidelines points 146 to 148, and recital 41 of Reg (EU) 2026/1744:

- Signing is **voluntary**. The Art 50 obligations remain legal obligations either way.
- Adherence to a code assessed as adequate under Art 50(7) is a way to **demonstrate compliance**. The Commission and market surveillance authorities will focus supervision on whether signatories have implemented the code's measures.
- It is **not** a presumption of conformity. Recital 41 of Reg (EU) 2026/1744 says so in terms. Presumption of conformity would come from a harmonised standard, and none exists yet.
- Opting out of sections loses the benefit for those sections.
- Non-signatories are expected to demonstrate compliance through other adequate means and to explain how their measures ensure compliance — the Guidelines suggest a **gap analysis against the code** as the expected form of that explanation.

Art 50(7) as replaced by Reg (EU) 2026/1744 Art 1(20): the Commission encourages and facilitates codes of practice, assesses adequacy taking utmost account of the Board's opinion under the Art 56(6) procedure, and — if it deems a code inadequate — may adopt an implementing act specifying common rules. The power to *approve* a code by implementing act is gone.

## Checkpoints

- [ ] Every surface inventoried: chat, voice, agent, generated image, generated video, generated audio, generated text, avatar
- [ ] Art 50(1) disclosure present on every directly interactive surface, at or before first turn
- [ ] Any reliance on the "obvious" exception written up against the Guidelines factors and sent to legal
- [ ] Agents disclose both artificial nature and the principal on whose behalf they act
- [ ] Art 50(2) marking implemented with **both** a marking technique and a detection means
- [ ] Multi-layer marking for audio, image, video and containerised text; single-layer only for free-form text or the closed-product case
- [ ] Free-form text over 200 tokens watermarked, with a detection route
- [ ] Metadata markings digitally signed and time-stamped; key handling documented
- [ ] Out-of-scope outputs (source code, UI labels, alt-text, machine-to-machine, closed-loop intermediates) listed and justified rather than assumed
- [ ] Any reliance on the assistive-editing or no-substantial-alteration exception documented case by case
- [ ] Interoperability solution planned against the 2 February 2027 date
- [ ] Deployer-side deepfake labelling built: EU icon or equivalent, design and placement specifications, audio disclaimer for audio-only
- [ ] Artistic-work regime applied only where the work is evidently artistic, creative, satirical or fictional
- [ ] Published-text disclosure built, or the human-review-and-editorial-responsibility exception documented with a named responsible person
- [ ] Emotion recognition or biometric categorisation checked against Art 5 before relying on Art 50(3)
- [ ] Disclosures accessible: screen-reader detectable, contrast checked, alternative cues for non-visual modalities
- [ ] Systems placed before 2 August 2026 tracked against the 2 December 2026 Art 50(2) deadline
- [ ] Code of practice signature decision recorded; if not signed, a gap analysis against the code exists

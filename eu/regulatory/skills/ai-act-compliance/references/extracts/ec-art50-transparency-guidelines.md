# Extract — Commission Guidelines on Article 50 transparency obligations

**Source**: `sources.yaml` id `ec-art50-transparency-guidelines`
**Document**: ANNEX to the Communication to the Commission — *Guidelines on the implementation of the transparency obligations for certain AI systems under Article 50 of Regulation (EU) 2024/1689 (the 'AI Act')*
**Reference**: C(2026) 5054 final, Brussels, 20.7.2026 (51 pages, 155 numbered points)
**Legal basis**: Article 96(1)(d) AI Act
**Accessed**: 2026-08-09
**Licence**: © European Union — reuse authorised under Decision 2011/833/EU
**Status**: **final and adopted**. Non-binding (point 5): "Any authoritative interpretation of the AI Act may ultimately only be given by the Court of Justice of the European Union."

Point references below (`§n`) are to the numbered points of the Guidelines.

---

## 0. Dates — the point that matters most

- **Article 50 applies from 2 August 2026** (§2, §153). The Guidelines state this twice and were adopted on that basis. Article 50 was **not** delayed by the Digital Omnibus.
- §153: the Omnibus "envisages a **targeted grandfathering rule only with regard to the marking and detection obligations under Article 50(2)** AI Act for generative AI systems placed on the market or put into service **before 2 August 2026**", giving those providers until **2 December 2026** to bring systems into conformity.
- Systems that are partly interactive and partly generative benefit from the transitional period **only** for the Article 50(2) marking obligation; **Article 50(1) disclosure must be ensured as of 2 August 2026**.
- §154: content generated or manipulated **before** 2 August 2026 does **not** need to be marked or labelled retroactively (same for public-interest texts published before that date). **But** text generated before 2 August 2026 and **published on or after** it must be labelled. Holders of pre-existing unlabelled deep fakes are encouraged, not required, to label them — no disproportionate effort (auditing content databases, modifying printed packaging) is expected.
- §153 footnote 50: the Article 111(2) grandfathering for high-risk systems does **not** extend to Article 50 — high-risk and Article 50 obligations are cumulative.

---

## 1. Horizontal points (Section 2)

### Cumulative application

§8: the four obligations may apply **cumulatively to the same system**, engaging different actors. A system generating images inside a direct interaction triggers 50(1) **and** 50(2) for the provider; if it can also generate deep fakes or public-interest text, the deployer additionally owes 50(4).

### Who is a provider (§10-11)

- Providers owe 50(1) and 50(2) irrespective of establishment; third-country providers are caught where the **output is used in the Union**. Incidental, unforeseeable or unauthorised downstream use does **not** alone trigger the obligations.
- Transparency must be **embedded in design and operation** and met **at the latest when the system is placed on the market or put into service** — regardless of who the deployers are.
- Putting an in-house system into service under one's own name makes the organisation a provider.
- Modifying another provider's generative system (e.g. new training data) and putting it into service under one's own name/trademark makes the modifier a **provider of the new system**.

### Who is a deployer (§12-17)

- 'Authority' means responsibility over the **decision to deploy** and over the **manner of actual use** — technical control is not required.
- Deployers in complex content-production and distribution chains must take **proportionate measures** to ensure their Article 50(4) labelling is displayed to the targeted and foreseeable audience at first exposure (contractual conditions with distributing partners, UX settings, interfaces).
- Third-country deployers are caught where they **foresee** dissemination and use of outputs in the Union (including posting deep fakes on the globally accessible internet); **not** caught where content reaches Union audiences through unforeseeable channels outside their control.
- Employees acting under the instructions of a legal person are **not separate deployers**. The legal person stays the deployer even when contractors or freelancers operate the system on its behalf.
- A company that merely **commissions** an advertising agency, without deciding or controlling whether and how the agency uses AI, is **not** a deployer.
- §15: one operator can be provider **and** deployer at once (in-house generative system used to make deep fakes → both 50(2) marking and 50(4) labelling).
- §16-17: hosting services, online platforms and broadcasters that only **disseminate or transmit** third-party AI content, without authority over the AI system, are **not deployers**. They are strongly encouraged to preserve existing markings and labels. Labelling content does not, by itself, make an actor a deployer.

### Exclusions (§18-24)

- **Purely personal, non-professional use** (Art. 2(10)): excludes only the **deployer** obligations in 50(3) and (4). The provider's 50(2) marking duty still applies to the same system. Any activity yielding regular economic benefit is 'professional'.
- **Scientific R&D** (Art. 2(6)) and pre-market research/testing (Art. 2(8)) are excluded; **testing in real-world conditions is not**. Once placed on the market, Article 50 applies.
- **Free and open-source** (Art. 2(12)): AI systems within the scope of Article 50 are **not** exempt. Free/open-source **components** (models, tools, data, services for integration) that are not themselves an AI system are outside Article 50, but their providers are encouraged to build in model-level transparency.

### Compliance ≠ lawfulness (§25)

Recital 137: complying with Article 50 does **not** make the system or its output lawful. An Article 50 system may still be prohibited under Article 5 (e.g. workplace emotion recognition) or classified high-risk under Article 6. Article 4 AI literacy applies to providers and deployers of Article 50 systems.

### GPAI models (§26-27)

Article 50 does not explicitly apply to GPAI **models**. Where an in-scope system is built on a GPAI model **from the same provider**, the transparency measures may be implemented at **model level**. Other GPAI model providers are encouraged to do the same to help downstream system providers. For GPAI models with systemic risk, model-level identification and marking measures may form part of the Article 55(1)(b) mitigation set.

---

## 2. Article 50(1) — interactive AI systems (Section 3)

### Scope: four elements (§30)

1. **An AI system** — excludes simple non-AI automated responses (out-of-office emails, rule-based quick replies).
2. **Intended to interact** — a **bidirectional** exchange with a **genuine conversational or responsive character**. Systems that only passively collect data (automated facial-recognition access control) or take one-time feedback (spam filters) are out.
3. **Directly** — real-time or near real-time. Excludes indirect/mediated exposure (customer-service agents using AI assistance tools; output relayed by another person). But the **mere possibility** of human intervention cannot be used to circumvent the duty: blended AI/human-curated products need disclosure for the AI-generated outputs unless those outputs are properly reviewed and sent by humans as the main interlocutors.
4. **With natural persons** — including professional deployers and other users. Closed physical environments (industrial machinery), backend machine-to-machine calls and virtual environments without human contact are out.

### AI agents (§31)

Agents are in scope where they can interact with the persons instructing them or with other natural persons while executing tasks (bookings, correspondence, negotiating or concluding contracts, purchases). They must disclose **both their artificial nature and the person on whose behalf they act**. Where the provider cannot reliably determine in advance whether the agent will meet a natural person, the agent must be designed **at architecture level** to disclose itself in **every situation where interaction with a natural person is reasonably likely**. Agents should also disclose to the instructing person **at key steps** (authorisation, reporting, validation, when relying on outputs from other AI systems) and **at every new interaction**.

**In scope**: voice assistants, chatbots/conversational agents (public service, customer support, complaints, e-commerce, finance, healthcare, education), incident/fraud reporting hotlines, (humanoid) robots and cobots, AI companions, robotic companion pets, AI avatars in VR, social-media bots, coding agents.

**Out of scope**: industrial robots in closed settings, recommender systems, spam filters, automated translation/transcription, search and retrieval without generation, text/code auto-completion, authentication/biometric recognition, backend decision-support where the user only sees the output, predictive maintenance, product visualisation (virtual try-on, room staging), single-turn route planners.

### How to disclose (§34-40)

No prescribed technique. Recommended formats:

- **Textual**: prominent plain-language label or banner ("You are interacting with an AI system"), first-turn chatbot greeting, persistent badge; position it close to the input/output field; simplified wording for low-literacy users and children.
- **Auditory**: explicit spoken statement at the start ("This is an AI-powered assistant"), plus periodic reminders in longer interactions or after interruptions/role changes. Audio cues (tones, earcons) **support** recognition but are **not sufficient alone**.
- **Visual**: persistent icons, watermarks, coloured frames, recognisable "AI" symbols; standardised indicators across a provider's services are recommended.
- **Multi-modal** combinations are best practice.

**Insufficient when used alone (§38)** — treat these as failure modes:

- disclosure only in terms and conditions, URLs or documentation;
- machine-readable markings that users cannot perceive at the point of interaction (these serve 50(2), not 50(1));
- unclear or ambiguous signals (a generic "assistant") or human-like representations that mislead;
- generalised site-wide statements ("Services on this website use AI");
- technical descriptions ("this system uses LLMs") without explaining the function or the artificial origin.

**Frequency (§40)**: a single prominent notification before the first interaction usually suffices. **Periodic and context-aware reminders** are likely necessary for vulnerable persons (children, elderly, disabilities, lower literacy), sustained interactions in sensitive or immersive contexts (emotional distress, addiction-like risk), high-misleading-risk domains (financial, insurance, legal, health advice, complaints handling), emotional-attachment contexts (AI companions), and AI agents. The system must **always** disclose when asked about its nature or origin, or when the exchange suggests the person is likely being misled.

### 'Obvious' exception (§42-45)

Two-step assessment: (i) define the reasonably well-informed, observant and circumspect member of the **target and reasonably foreseeable** audience; (ii) assess whether the artificial nature is obvious to that person. Drawn from the consumer-law 'average consumer' standard.

Key constraints:

- **Interpret restrictively** — it deprives people of a protection.
- General public awareness that chatbots exist does **not** mean people recognise them in a given interaction.
- Where the audience may include children, the elderly, persons with cognitive/physical/mental disabilities or low AI literacy, the exception **cannot be relied on**.
- The exception is "limited to cases where there is almost no doubt left about the nature of the interaction for an average person from the targeted and reasonably foreseeable audience".

**Obvious (exception applies)**: code assistance/review chatbots for professional developers; internal employee-facing assistants for trained, AI-literate staff (HR, legal, procurement, compliance, IT support); systems for trained health professionals supporting diagnosis; ambient AI in home appliances; NPCs in single-player video games.

**Not obvious (disclosure required)**: robotic companion pets mimicking human-pet interaction; realistic avatars or voices in VR/AR; chatbots and helpdesk tools embedded in online platforms whose replies users may perceive as human-generated.

### Law-enforcement exception (§46-49)

'Authorised by law' covers Union law and national law adopted in compliance with Union law; the law must specify the purposes and circumstances of permitted use and provide safeguards. Specific AI systems need not be named. Not restricted to law-enforcement authorities as defined in Art. 3(48) — other public authorities may rely on it. For dual-use systems, assess per deployment; transparency still applies to the non-law-enforcement uses.

**The exception does not apply** where the system is (i) available to the public and (ii) offers a functionality to report criminal offences — e.g. police chatbots on official websites, police telephone hotlines, fraud-reporting portals, witness-statement virtual assistants. These must disclose.

### Interplay (§50-53)

Applies without prejudice to the UCPD (Directive 2005/29/EC) and the Consumer Rights Directive (Directive 2011/83/EU) — where a service is AI-driven (subscription chatbot, AI companion, virtual coaching), the **AI functionality may be an essential characteristic** that must be disclosed pre-contractually, **irrespective of whether the interaction is "obvious"** under Article 50(1). DSA recommender-transparency rules are complementary; data-protection information duties serve a different objective and are unaffected.

---

## 3. Article 50(2) — marking and detection of synthetic content (Section 4)

### Scope: cumulative conditions (§56)

AI system + capable of generating or manipulating synthetic content + in the modalities audio, image, video or text + not caught by an exception.

- **Generation** = producing synthetic material (e.g. from a prompt). **Manipulation** = altering already existing content (synthetic or not) beyond standard editing. Content **mixed with human-created material still qualifies** (§59).
- **Modalities (§60)**: *text* = discrete symbolic content readable and semantically interpretable by humans; *images* = static spatial representations; *audio* = time-varying sound signals (speech, instrumental music, other); *video* = a time-based sequence of images, optionally synchronised with audio — **both the video and the audio must be marked and detectable**. Multimodal mixes are included.
- **3-D and immersive (§61)**: 3-D images/videos/audio and virtual, augmented and mixed reality are in scope and are treated as **video**. The output to be marked is the **final form of the individual AI-generated asset**. Digital artefacts used to generate them (point clouds, 3-D meshes) need not be marked.
- **Digital twins (§62)** of persons, objects or systems are in scope unless they qualify for the industrial/B2B or real-time-ephemeral carve-outs.
- **AI agents (§63)**: outputs that are **perceptible to natural persons** as audio, image, video or text must be marked. Intermediate processing (reasoning, chain of thought) and non-perceptible actions (web requests, browser actions) are **not** synthetic content.

### Out of scope (§64-68)

- Content from simple data processing that is not specifically AI-generated (e.g. a rendered frame).
- Output that merely reproduces, presents or arranges existing content — music playlists, recommender ranking, internal analytics that extract and structure without summarising.
- Mere observations and recordings of physical or virtual environments (robot sensor data, smart-meter consumption, grid frequency and voltage, vehicle GPS traces).
- Short sequences of numbers, symbols or letters: single words, image captions, alt-text, UI labels, icon-scale graphics, data labels.
- **Source code** and adjacent artefacts: SDKs, SQL, infrastructure-as-code, YAML, JSON configuration, schemas, scripts, machine-readable specifications, APIs and software libraries — including natural-language comments forming an integral part of the code.
- Outputs intended exclusively for machine-to-machine communication and never perceived by natural persons (agent-to-agent messages, anti-spam signals).
- Intermediate outputs in **closed-loop production workflows** (film, animation, games, advertising) — **only the final output** must be marked.

### The two obligations (§69-78)

Marking **and** detection. Marking alone does not comply.

**Marking**: machine-readable = structured so that software can identify, recognise and extract the mark **without human intervention**. Perceptible marks are a permitted **complement** (and help deployers meet 50(4)). Recital 133 techniques: watermarks, metadata identifications, cryptographic provenance methods, logging, fingerprints, or combinations. Providers are **not** obliged to record or keep a full provenance chain. Marking may be implemented at any value-chain stage (post hoc, at model level, in the inference process) and providers **may rely on an upstream model provider or a third-party solution** — without prejudice to their own responsibility to demonstrate compliance.

**Detection**: the provider must ensure that **means of detection are available to persons potentially exposed** to the content, producing **human-readable results**. Providers must rely on **publicly available industry-standard detection solutions** allowing any third party to implement detection, **ideally locally executable** on the device and integrable into isolated networks. Where such standards do not yet exist, a provider may use its own, a third-party or a shared solution **so long as interoperability with other providers' detection solutions is ensured** — a possibility that should be **limited in time** until harmonised standards and a standardised provider-agnostic solution emerge. 'At the time of first exposure' (Art. 50(5)) means the moment a person is willing to verify the origin of a piece of content and access the detection solution.

### The four quality requirements (§79)

- **Effectiveness** — the solution can detect its own marks and lets people distinguish the provider's artificially generated content.
- **Reliability** — accurate identification in **nominal** conditions across the variety of content the system produces.
- **Robustness** — accurate identification under **varying** conditions, covering both common alterations and **adversarial attacks**.
- **Interoperability** — marking and detection solutions operate seamlessly across systems, actors, contexts and implementations, **regardless of the marking technique used by other providers**.

Compliance is assessed **holistically** across the combination of solutions, "insofar as this is technically feasible", taking into account content specificities, implementation costs and the state of the art (§80). **'Technically feasible' is an objective notion, not dependent on the individual provider's resources or capabilities** (§81) — a small provider cannot claim infeasibility that a well-resourced one could not. Solutions must be **continuously adapted** as the state of the art evolves (§83). Adherence to an adequate code of practice is a route to demonstrating compliance (§84).

### Proportionality carve-outs (§86-88)

- **Less robust metadata marking** may suffice where a generative system is embedded in a physical product producing outputs in a technically controlled, closed, mainly instructive environment (e.g. in-vehicle navigation), provided effective technical measures prevent outputs from leaving the product environment.
- **Industrial or B2B applications** (excluding public- and consumer-facing systems) need **no** marking and detection where three conditions are met cumulatively: (i) the output is strictly technical (engineering designs, industrial production workflows, technical instructions, predictive-maintenance output, internal documentation, pre-finalisation production steps); (ii) it is intended to be perceived and processed only by a limited pre-defined number of professionals inside the provider's and deployer's organisations; (iii) it is not intended to be shared outside the company or usable by external persons, with safeguards against reasonably foreseeable misuse (cloud isolation, role-based controls).
- **Real-time ephemeral content** consumed immediately without being recorded, stored or disseminated (video games, VR) may be exempt where marking is not technically feasible **and** exposed persons are made aware the content is AI-generated (in-experience disclosure, session-level notifications).

### Exceptions (§89-93)

**Standard editing** = preparing existing content for publication or distribution (readability, grammar, quality, format) without generating new content. Editing goes beyond standard editing when the content is changed **materially** — substantive modifications or structural changes affecting **meaning, style or intent**.

**Non-substantial alteration**: an alteration is substantial if the input data or its semantics have been **significantly** manipulated during output generation, judged on format, media type, style and changes affecting meaning, style or intent. A dual-capability system is exempt **only for the minor, non-substantial alterations**.

*Exempt examples*: grammar and spellcheck, minor stylistic polishing, **AI-generated translations of text**; formatting, format conversion, technical compression, noise reduction; minor cropping, colour adjustment, lightening/darkening, sharpening; dust-spot and red-eye removal; deleting or obscuring backgrounds visible in the original file; pixelation or blurring of faces; rescaling, dynamic range compression, equalisation, limited video stabilisation; horizon levelling, pixel filters, colour maps on greyscale, edge completion, black-and-white ↔ colour conversion; pixel filling for aspect ratio; automatic transition clips; medical image technical processing within medical devices (annotations, boxes, contours, heatmaps); conversation transcriptions; assistive-technology output for persons with disabilities (AAC, customised neural voices).

*Requires marking*: AI-generated **summaries**; paraphrasing or rewriting that changes style, structure and meaning beyond minor correction; removal, replacement or insertion of objects or persons that changes meaning; face replacement or substantial facial modification; synthesis of realistic speech in a specific person's voice; generation of realistic video of events that did not occur; altering body shape or skin colour; extreme lightening/darkening or colour and contrast changes that change meaning, intent or messaging; composite images or clips that modify the representation of persons, objects, events or facts.

**Law enforcement**: as for 50(1) (§46-48).

### Interplay (§94-98)

Marking and detection concern **how** content was created, **not who** created it: solutions must comply with data-protection law — creator information should **not** be processed for marking and detection, and other personal data must be deleted once the detection purpose is fulfilled. Machine-readable marks help VLOPs and VLOSEs meet Articles 34-35 DSA. Marking or labelling **does not influence** the assessment of a content's illegality under other frameworks (a labelled deep fake flagged as CSAM or as trademark-infringing is assessed solely under criminal, trademark or copyright law) and is without prejudice to Article 16(6) DSA notice handling.

---

## 4. Article 50(3) — emotion recognition and biometric categorisation (Section 5)

- Definitions: Art. 3(39) emotion recognition system; Art. 3(40) biometric categorisation system. The Guidelines defer to the **Commission guidelines on the classification of high-risk AI systems** for the detailed explanation of both notions and their examples (§101, §103).
- The obligation applies **whether the system runs in real time or ex post** (§100).
- All emotion recognition systems are **high-risk** unless prohibited under Art. 5(1)(f) in workplace and education; Article 50(3) applies **in conjunction** with the high-risk requirements (§102).
- Article 50(3) applies to **any** biometric categorisation system unless prohibited under Art. 5(1)(g) — **including systems that are not high-risk** (e.g. age or gender classification from biometric data) (§104).
- **Scope of the information (§105)**: only that the person is exposed to a system being operated. Reasons for operation, or other processing purposes, are **not** required by the AI Act — though Union data-protection law may require them.
- **Addressees (§106)**: all natural persons exposed, **including children**.
- **Means (§107)**: no prescribed form — writing, standardised icons (including electronic), orally, or combinations. Choose by place of deployment (gaming platform, physical store, station), likely addressees (children, elderly, persons with disabilities, customers), length and type of exposure (long-term, one-off, continuous, intermittent) and any existing communication channel with the individual. Examples: a centrally placed pop-up before a game launches stating the player's face is recorded and emotions captured; a visible notice at each entrance to an exhibition room where visitors' facial images are captured for age-group assignment.
- **Timing (§108)**: at the latest at first interaction or exposure; earlier is permitted.
- **Law-enforcement exception (§109)**: **broader than the other Article 50 exceptions**. The others require an explicit law authorising the non-transparent use; Article 50(3) makes it possible where use is **permitted under the legal rules governing the powers of law enforcement authorities** to detect, prevent or investigate criminal offences, subject to safeguards.
- **§110**: complying with 50(3) does **not** make the use lawful, nor legitimise uses prohibited under Article 5 or unlawful under other Union law. Deployers may in some cases fold the Article 50(3) notice into their data-protection information to data subjects.

---

## 5. Article 50(4) — deep fakes and public-interest text (Section 6)

### 5.1 Deep fakes — the four cumulative criteria (§113)

Art. 3(60): AI-generated or manipulated image, audio or video content that **resembles** **existing** **persons, objects, places, entities or events** and would **falsely appear to a person to be authentic or truthful**.

1. **Resemblance** — Recital 134 requires it to be **appreciable**: a high level of similarity between the content and the simulated subject, including its recognisable elements. Identity is not required. Case-by-case, objective comparison by the deployer, based among others on the extent to which characteristic or distinctive features are represented.
2. **Existing** — the subject must be **realistic**: it suffices that it resembles something that exists, plausibly exists, or could plausibly have existed. Subjects that defy the laws of nature or physics or depict lifeforms not accepted in biology (humans flying unaided, dragons, elephants driving cars) have no potential to mislead and are **out of scope**.
3. **Persons, objects, places, entities or events** — *persons*: realistic human beings, including digital replicas of real persons, realistic AI-generated avatars or personas, and personal characteristics or expressions (image, voice, behaviour, performances). *Objects*: realistic inanimate material items (buildings, artworks, machinery, consumer goods). *Places*: realistic locations. *Entities*: realistic non-human animate beings (animals, other biological lifeforms). *Events*: realistic scenes or situations (historical events, depiction of professional or consumer services).
4. **False appearance of authenticity or truthfulness** — *authenticity* = whether the content is genuinely what it purports to be as to source or creation process (involvement of real people or animals and their actual behaviour, actual appearance or use of objects, delivery of services, accurate unfolding of an event). *Truthfulness* = veracity, factual correctness.

**Assessment (§114-116)**:

- Assessed **as a whole**: level of resemblance, potential substantive message, intended and foreseeable deployment context, environment of presentation, and intended and reasonably foreseeable audience composition and expectations.
- **Objective test — no intent to deceive is required.**
- Where the audience does not expect the content to be authentic or truthful in the specific deployment context, the fourth criterion may fail even for non-authentic content. Background scenes, special effects and standard pre-/post-production processing are unlikely to make content *falsely* appear authentic. Conversely, AI generation or manipulation of **essential elements affecting audience perception** is likely to (fully AI-generated actors, digital replicas of real or deceased actors, de-aging, simulated performances or parts of them, non-authentic representation of persons, objects, places or events in **documentaries**).
- **Photorealism** makes deep-fake status more likely but is **not determinative**; the test remains capability to deceive or mislead as to authenticity or truthfulness.
- **Audience standard differs from 50(1) (§115)**: **not** the hypothetical "average" person. Deployers must take account of the possible **diverse composition of the reasonably foreseeable audience** — where it is reasonably foreseeable that children, the elderly or persons with lower digital/AI literacy may be exposed, false appearance **to that part of the audience may suffice** to make the content a deep fake. Deployers need **not** consider further dissemination by third parties beyond the reasonably foreseeable audience given the intended distribution channels (subscriber-only content or a corporate newsletter does not imply broad public accessibility).
- **Insignificant manipulations (§116)** may not make content a deep fake: editing background details (removing a passerby), lighting adjustment, audio parameters, colour correction, noise reduction, accessibility improvement, file compression, cosmetic adjustments. Context-dependent: AI colour correction or background replacement in product advertising is likely minor; **substantial AI editing of journalistic images beyond standard editorial practice is not**.

**Deep fakes**: AI-manipulated image of two real footballers in front of a building resembling a stadium; voice cloning of a podcast's regular presenters; AI-generated video of a person resembling a politician giving a speech; AI-generated celebrity influencer in an advertising context; realistic synthetic avatar of a company CEO addressing employees; AI-generated product image in advertising or packaging that misleads as to the product's actual appearance, characteristics or use.

**Not deep fakes**: a sphinx flying over the Eiffel Tower; mice arguing in human language in a cheese advert; AI voice replication for fictional characters (audiobooks, games, animation) where there is no deception as to the narrator's identity; radio broadcast with technical audio adjustments only; an AI-generated cartoon of a pre-existing historical image; an AI-manipulated background animation illustrating glacier retreat behind a real science presenter; AI-generated fictitious environments in video games; real actors playing against an AI-generated background; a real product shown against an AI-generated background where the ad is not likely to mislead about the product.

### 5.2 The deep-fake disclosure (§117-118)

Disclosure must be **clear and distinguishable**, "understandable and perceivable by natural persons (e.g. with visible or audible labels), **without them needing to rely on any specific technical tools or performing dedicated actions**". Critically: **deployers cannot rely on the provider's Article 50(2) machine-readable marking** to discharge Article 50(4) — those markings are not immediately clear and distinguishable to exposed persons. Adherence to an adequate Article 50(7) code of practice is a route to demonstrating compliance.

### 5.3 The attenuated regime for artistic/creative/satirical/fictional works (§119-124)

Definitions for Article 50(4) purposes:

- **Artistic** — created for the purpose of art, including music, cinematographic works, visual arts.
- **Creative** — involving creative choices; works mainly motivated by functional or technical considerations do **not** qualify.
- **Satirical** — intended to criticise society, politics, business or public figures through humoristic techniques (irony, sarcasm, mockery, pastiche).
- **Fictional** — cultural works involving persons, objects, places, entities or events in an imaginary but verisimilitude setting.
- **Analogous** — sharing core traits or similar expressive/functional characteristics with the above without fitting neatly into one.

These may also apply to a **programme** (an individual item in a schedule or catalogue established by a media service provider, comparable in form and content to television broadcasting). The word 'works' has **no bearing** on copyright eligibility.

**'Evidently' (§122)** — the category must be **evident to the natural persons exposed**, and the categories are to be **interpreted strictly** because the lighter regime trades against misinformation and deception risks. Content whose nature is potentially unclear or ambiguous to the audience is **excluded**. Relevant factors: (i) formats or styles characteristic of the category (irony, exaggeration, distinctive art styles); (ii) the context of presentation (platform, medium or place associated with artistic, creative, satirical or fictional use); (iii) audience expectations (a movie, gaming environment, VR scene). Content that is **exclusively informative or commercial and recognisable as such** (news reporting) is excluded. Advertisements and documentaries may qualify in some specific situations but not others. **Where a deep fake combines characters (e.g. informative and creative), the informative character always prevails and standard labelling applies.**

**Appropriate disclosure (§123)**: the attenuated regime does not exempt — deployers must still disclose the AI origin, but in a manner that does not hamper the display or enjoyment of the work, or its normal exploitation, utility and quality (Recital 134). Case-by-case, considering nature of the work, audience and context. **Article 50(5) still applies in full.**

**Third-party safeguards (§124)**: reliance on the attenuated obligation **cannot justify** failing to respect fundamental rights, IP rights or data-protection law of third parties.

**Attenuated regime applies**: movies or trailers featuring de-aged or digitally replicated existing or dead actors; AI-generated music resembling the style of existing artists; a satirical AI-manipulated image of a politician clearly criticising policy decisions humorously; AI-generated gaming imagery involving deep-fake simulations of real persons.

**Attenuated regime does not apply**: teleshopping-style video with deep-fake humans advertising a product to persuade viewers to buy; AI-generated images of celebrities implying involvement in activities that never happened, with no fictional, satirical or analogous purpose; a realistic synthetic influencer testing a real sponsored product, focused solely on product functionality; AI-generated realistic holocaust scenes shared on public social media.

### 5.4 Law enforcement and interplay (§125-129)

Law-enforcement exception as in §46-48. Article 35(1)(k) DSA is **complementary**, with two distinctions: **material scope** — the DSA covers content that may falsely appear authentic **regardless of the technology used**; **personal scope** — Article 50(4) binds deployers, Article 35(1)(k) DSA binds VLOP/VLOSE providers disseminating the content. Deployers using a VLOP to disseminate their AI content may be 'recipients of the service' under Art. 3(b) DSA; where the platform makes labelling tools available, **deployers can rely on those tools** to fulfil Article 50(4) within that platform. Providing such a functionality is without prejudice to the deployers' own responsibility. VLOP/VLOSE providers are themselves **deployers** when they use an AI system under their own authority for their own professional purposes (e.g. marketing visuals).

Deployers must additionally comply with data-protection law (identifiable living persons), Union IP law (trademark, copyright — applying a label has **no** effect on copyright eligibility) and personality rights over images and voices. **§129: Article 50(4) transparency does not imply that unlawful deep fakes (misleading advertising, CSAM, non-consensual intimate images) may be generated or disseminated.**

### 5.5 AI-generated public-interest text (§130-140)

Three conditions: AI system + used to generate or manipulate **text published with the purpose of informing the public on matters of public interest** + no exception (human review/editorial control with editorial responsibility, or law enforcement).

- **Published (§131.i)**: accessible by an **indeterminate, fairly large number of unrelated potential readers**, simultaneously and/or successively, whether or not against payment (subscriptions count). **Not published**: access restricted to specific individuals in a closed private group (a small closed messaging-app group, or a group too small or insignificant), private or interpersonal professional correspondence, organisation-internal texts, publications on internal corporate networks.
- **Informing the public (§131.ii)**: the text must intend to communicate **knowledge, opinions or facts**. Short texts that do not materially communicate these cannot inform the public.
- **Matters of public interest (§131.iii)**: relevant to society at large — local, national, Union or international — and meriting public debate or scrutiny. Covers politics and democratic processes, public administration and services, administration of justice and law enforcement, protection of fundamental rights, public security, public health, environmental protection, consumer safety, and any economic, financial, political, scientific or cultural development that may be a relevant subject of public debate. **Evolves over time and across contexts.**

**In scope**: an AI-generated summary of a human-authored newspaper article on a town-council decision; AI-manipulated parts of a lifestyle-website article comparing the effects of diets on a disease; AI-manipulated corporate reports with investor information on a listed company's website; an AI-generated storm warning on a meteorological institute's social-media profile.

**Out of scope**: AI-generated fantasy novels; AI-manipulated advertisement or product-description text (not including health, consumer-safety or sustainability claims); a news summary generated by a chatbot available only to the user who prompted it; AI-manipulated client advice by a consultant on regulatory compliance measures.

**Disclosure (§132)**: as for deep fakes — clear, distinguishable and perceivable by natural persons (including via disclaimers), without needing technical tools.

### 5.6 The editorial exception (§133-138)

Two **cumulative** conditions.

**(i) Human review or editorial control (§134-136)**:

- **Human review** = **deliberate examination of the substance** by one or more natural persons with relevant knowledge and professional judgement on the subject matter (academic peer review, professional validation chains). **Fact-checking the accuracy of the content is a minimum requirement.**
- **Editorial control** = control exercised **in practice** by a responsible editorial entity (e.g. an editor-in-chief) with the authority to approve, alter or reject the substance on substantive grounds, including fact-checking and ensuring source trustworthiness.
- **Insufficient (§135)**: superficial, solely formal or procedural checks (spell-checking, grammatical correction), the **mere existence of an editorial policy**, automated review processes, or cursory editorial approval without substantive engagement.
- **§136**: where AI is used to modify, supplement or reformulate content **after** editorial sign-off, the result is AI-generated for Article 50(4) purposes — **any substantive AI intervention after review voids the exception**.

**(ii) Editorial responsibility (§138)**: a legal or natural person must hold the **ultimate legal responsibility** over the publication, including the review or editorial control (an individual, editorial board or publishing company). The **identity and contact details** of that person or function **should be made publicly available in an easily findable location** — website terms and conditions or other user-facing legal information online, a colophon or edition notice offline.

**§140**: 'editorial responsibility' should be interpreted **in line with the existing media acquis** — Art. 2(8) EMFA (Regulation (EU) 2024/1083): "the exercise of effective control both over the selection of programmes or press publications and over their organisation". It remains a distinct concept that can also apply to non-media deployers who assume editorial responsibility. Media service providers may rely on their **existing editorial processes and standards** to benefit from the exception.

**Exception met**: an AI-manipulated newspaper article or AI-generated summary under the editor-in-chief's editorial control with responsibility held by the publishing legal person; an AI-manipulated academic blog under internal peer review with the research centre holding responsibility; AI-generated public safety warnings approved by a public official under the civil-protection agency's responsibility; AI-generated sustainability reports on a listed company's website reviewed by professionals in the relevant functions (e.g. compliance); an AI-supported translation of a human-written article that has undergone human review.

**Exception not met**: a website posting AI-generated articles on Union policy with no deliberate human review or editorial control; AI-generated articles reviewed and edited by another AI system with only a superficial human grammatical check; an AI-generated self-published book on climate change on an e-commerce platform with no review by a competent natural or legal person or by the platform.

---

## 6. Article 50(5) — how the information must be provided (Section 7)

- **Clear (§142)** = noticeable, easy to understand and accessible for the natural person concerned, including persons with disabilities, and easily understood by specific groups such as children when they are part of the foreseeable audience. **Distinguishable** = easy to identify as **separate** from other information and from the environment in which the content is presented.
- **Not** clear and distinguishable: information that can be easily overlooked or missed under normal exposure conditions — buried in a manual, hidden under layers of menu options, or placed in terms of use that are often not read.
- Where children are part of the target audience, notifications must be child-friendly, age-appropriate, simple and succinct, easy to review with immediate and intuitive access at the relevant points, in the official language(s) of the Member State, engaging (graphics, videos, characters) and given gradually over time (footnote 40).
- **First interaction or exposure (§143)**: not only the first person, but **any subsequent first interaction or exposure by any other natural person**. For interactive systems, information should be provided **at least once at the start of an interactive session**. For 50(2) and 50(4) content, the obligation applies **to each output** with respect to any natural person exposed. Disclosure earlier than the actual first exposure is allowed (e.g. at the beginning of content featuring deep fakes) — but where it is reasonably foreseeable that persons may not perceive content from its beginning, beginning-only disclosure is inadequate and **should be complemented with disclosure at later moments** where possible.
- **Accessibility (§144)**: Directive (EU) 2016/2102 (public sector websites and mobile apps) and Directive (EU) 2019/882 (European Accessibility Act) apply where relevant. **Article 50 imposes no distinct or additional accessibility requirements** of its own.

---

## 7. Enforcement (Section 8)

### Code of practice (§146-150)

For Article 50(2) and (4), a code of practice assessed as adequate under Article 50(7) is "the **only Union-wide recognised practical framework**" for demonstrating compliance regardless of place of establishment or competent authority. It does not replace the AI Act or these Guidelines.

- **Signatories**: the Commission and market surveillance authorities will **focus supervision on whether signatories have adhered to the code and implemented the measures in it**. Opting out of sections forfeits the benefit for those sections.
- **Non-signatories**: expected to demonstrate how they comply through other adequate means **and to explain how their measures ensure compliance** — for instance by carrying out a **gap analysis against the measures set out in an adequate code**. They will likely face **more detailed information requests**, including requests for access to assess the effectiveness, interoperability, robustness and reliability of their Article 50(2) technical solutions, and requests to deployers about labelling practices.
- Commitments implemented in line with an adequate code may be a **mitigating factor when fixing fines** (Art. 99(7)(e)).
- If no code is deemed adequate, the Commission may adopt an **implementing act** specifying common rules for 50(2), (4) and (5) binding on all relevant providers and deployers.

Footnote 43 cites the **Code of Practice on Transparency of AI-Generated Content, published 10 June 2026**, and footnote 44 the Commission Opinion on its assessment.

### Authorities and penalties (§151-152)

Market surveillance authorities designated by Member States, the **AI Office** and the **EDPS** (for EU institutions) supervise Article 50, within the Regulation (EU) 2019/1020 framework. The AI Office is the MSA for AI systems built on GPAI models **provided by the same provider** (Art. 75(1)) — this covers the **provider** obligations in Article 50(1) and (2); for Article 50(3) and (4) the AI Office is competent **only** where the GPAI model and system provider is **also the deployer**. Any affected person may lodge a complaint (Art. 85).

**Penalties**: up to **EUR 15 000 000 or 3% of total worldwide annual turnover** for the preceding financial year, **whichever is higher**. EU institutions, bodies and agencies: up to **EUR 750 000**. For **SMEs including start-ups**, the fine is the above percentage or amount, **whichever is lower**. Fines must take into account the interests of SMEs and **small mid-cap enterprises (SMCs)** and their economic viability. Aggravating/mitigating factors include nature, gravity and duration of the infringement, negligent or intentional character, and degree of cooperation with the MSA.

### Review (§155)

The Guidelines are a **first interpretation**. The Commission will review them in light of practical implementation experience, technological and regulatory developments, market-surveillance enforcement actions and CJEU interpretations, and may **withdraw or amend** them.

---

## Notes for the skill

- These Guidelines are the **Commission's official interpretation** of Article 50 but are **not binding** (point 5: only the CJEU can interpret the AI Act authoritatively); cite them as persuasive interpretive guidance, never as the legal norm. The norm is Article 50 itself.
- The four practical tests a compliance check should run: (1) is the disclosure **perceivable without tools**? (2) is it delivered **at or before first exposure, to every exposed person**? (3) is it **specific to this system's outputs** rather than a site-wide banner? (4) for 50(2), is there a **detection means available to exposed persons**, not just a mark?
- The most frequently missed obligation is the **detection** half of Article 50(2): marking alone is non-compliant (§70).
- The most frequently over-claimed exception is **'obvious'** under 50(1): unavailable wherever vulnerable users are in the foreseeable audience (§45).
- Deployers must not assume the provider's machine-readable mark discharges their 50(4) labelling duty (§117).
- Cross-references to the companion Commission guidelines: prohibited practices C(2025) 5052 final, AI system definition C(2025) 5053 final, and the high-risk classification guidelines (relied on in §101 and §103 for the emotion-recognition and biometric-categorisation notions).

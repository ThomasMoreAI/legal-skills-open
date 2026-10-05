# 01 — Risk Classification (AI Act art. 5, 6, Annex III, art. 50)

The AI Act is a **risk-based regulation**. Classification determines the entire downstream regime — obligations, deliverables, sanctions, conformity path. Misclassification at this stage propagates to every later artefact, so this is the single most consequential decision in an AI Act project.

Two axes operate independently and must both be evaluated:

1. **Risk tier** (this reference) — applies to all AI systems placed on the EU market or put into service.
2. **GPAI regime** (see `10-gpai-and-timeline.md`) — applies to general-purpose AI models regardless of deployment context.

A given product can be both a high-risk AI system *and* built on a GPAI model: both regimes apply.

## 1. The four-tier rubric

### 1.1 Unacceptable risk — art. 5 prohibitions

Banned outright. Placing on market or putting into service triggers **tier-1 sanctions: €35M or 7% of global annual turnover**, whichever is higher (art. 99(3)). In application since **2025-02-02** (six months after entry into force).

Nine categories — art. 5(1)(a)–(h) as of the original text, plus the NCII/CSAM prohibition added by the 2026 AI Omnibus:

| # | Practice | Carve-outs |
|---|----------|-----------|
| (a) | **Subliminal techniques beyond consciousness** OR **purposefully manipulative/deceptive techniques** that materially distort behaviour and cause significant harm | Targeted, the harm must be significant and the technique must operate beyond a person's awareness or exploit deception |
| (b) | **Exploitation of vulnerabilities** due to age, disability, or specific socio-economic situation, materially distorting behaviour and causing significant harm | Same harm threshold |
| (c) | **Social scoring** by public authorities or on their behalf, leading to detrimental treatment in unrelated contexts or disproportionate to behaviour | Carve-out: lawful evaluation by private actors in original context (e.g., creditworthiness assessment under regulated banking) |
| (d) | **Predictive policing of natural persons** based solely on profiling or assessment of personality traits | Carve-out: AI used in support of human assessment based on objective and verifiable facts directly linked to a criminal activity |
| (e) | **Untargeted scraping** of facial images from the internet or CCTV to create or expand facial recognition databases | No carve-outs |
| (f) | **Emotion recognition** in **workplace** and **education** contexts | Carve-outs: medical or safety reasons (e.g., fatigue detection in pilots/drivers) |
| (g) | **Biometric categorisation** that infers race, political opinions, trade union membership, religious or philosophical beliefs, sex life, sexual orientation | Carve-out: lawful labelling/filtering of lawfully acquired datasets, in the area of law enforcement |
| (h) | **Real-time remote biometric identification** in publicly accessible spaces by law enforcement | Narrow carve-outs (art. 5(2)–(4)): targeted search for specific victims, prevention of imminent threat, identification of suspect of serious crime — all subject to prior judicial/administrative authorisation and Member State enabling law |
| — | **Generation/manipulation of non-consensual intimate imagery (NCII) or child sexual abuse material (CSAM)** — added by the 2026 AI Omnibus. Extends to systems where such generation is "a reasonably foreseeable and reproducible outcome, without requiring significant technical modification" | Applicable **2026-12-02** (transitional period for implementing technical safeguards: refusal training, output controls, content filtering) |

**Common misclassification**: assuming an "AI ethics" violation = unacceptable. It does not. Art. 5 has narrow, specific triggers. A biased recruitment tool is **high-risk** (Annex III §4), not prohibited. A chatbot that manipulates is prohibited only if it "materially distorts behaviour" via subliminal/deceptive techniques causing significant harm — a high bar.

### 1.2 High risk — art. 6 + Annex III

Two pathways trigger high-risk classification. Either suffices.

#### Pathway A: art. 6(1) — Safety component of products in Annex I

The AI system is intended to be used as a **safety component of a product**, or *is itself a product*, covered by EU harmonisation legislation listed in **Annex I** AND that product is required to undergo a third-party conformity assessment under that legislation.

Annex I lists ~20 product regulations including:
- Machinery Regulation (EU) 2023/1230
- Toys Directive 2009/48/EC
- Recreational craft Directive 2013/53/EU
- Lifts Directive 2014/33/EU
- Equipment for explosive atmospheres Directive 2014/34/EU
- Radio equipment Directive 2014/53/EU
- Pressure equipment Directive 2014/68/EU
- Cableway installations Regulation (EU) 2016/424
- Personal protective equipment Regulation (EU) 2016/425
- Gas appliances Regulation (EU) 2016/426
- **Medical Devices Regulation (EU) 2017/745** + In Vitro Diagnostic Devices (EU) 2017/746
- Civil aviation security Regulation (EU) 2018/1139
- **Motor vehicle approval Regulation (EU) 2018/858** + Two/three-wheel + Agricultural vehicles
- Marine equipment Directive 2014/90/EU
- Rail interoperability Directive (EU) 2016/797

**Annex I high-risk obligations apply from 2028-08-02** (art. 113(c) as deferred by the 2026 AI Omnibus; originally 2027-08-02). The Omnibus also largely carves AI embedded in **Machinery Regulation** products out of the dedicated high-risk regime and narrows the "safety component" definition to exclude non-safety assistance and optimization functions.

#### Pathway B: art. 6(2) — Annex III use cases

**Annex III high-risk obligations apply from 2027-12-02** (deferred by the 2026 AI Omnibus from 2026-08-02, as a fixed date). Draft Commission classification guidelines under art. 6(5) were published **2026-05-19**.

The AI system is intended for one of the eight Annex III domains:

| § | Domain | Examples (non-exhaustive) |
|---|--------|---------------------------|
| 1 | **Biometrics** (insofar as their use is permitted) | Remote biometric identification (excluding verification), categorisation by sensitive attributes, emotion recognition |
| 2 | **Critical infrastructure** | Safety components of management/operation of critical digital infrastructure, road traffic, water, gas, heating, electricity supply |
| 3 | **Education and vocational training** | Determining access/admission, evaluating learning outcomes, assessing appropriate level of education, monitoring/detecting prohibited behaviour during tests |
| 4 | **Employment, workers management, access to self-employment** | Recruitment/selection (advertising, screening, evaluating candidates), promotion/termination decisions, task allocation based on individual behaviour, monitoring/evaluating performance |
| 5 | **Access to essential private services and public services and benefits** | Eligibility evaluation for public benefits, **creditworthiness/credit scoring** (except for detecting financial fraud), risk assessment & pricing in **life and health insurance**, dispatch/prioritisation of emergency response |
| 6 | **Law enforcement** | Polygraphs/emotion AI on persons, evaluating reliability of evidence, profiling for criminal investigation, crime analytics |
| 7 | **Migration, asylum, border control** | Polygraphs/emotion AI, risk assessments (security/health/irregular migration), examining applications, detecting/recognising/identifying persons |
| 8 | **Administration of justice and democratic processes** | Assisting judicial authorities in researching/interpreting facts/law, applying law to facts, alternative dispute resolution; influencing election/referendum outcomes or voting behaviour |

#### Art. 6(3) — Derogation from Annex III

An Annex III system is **not** considered high-risk if it does **not** pose a significant risk of harm to health, safety, or fundamental rights, **including by not materially influencing decision-making**. This is the case if **at least one** of the following is fulfilled:

(a) the AI system is intended to perform a **narrow procedural task**;
(b) the AI system is intended to **improve the result of a previously completed human activity**;
(c) the AI system is intended to **detect decision-making patterns or deviations** from prior decision-making patterns and is **not meant to replace or influence** the previously completed human assessment without proper human review;
(d) the AI system is intended to perform a **preparatory task to an assessment** relevant for the purposes of the use cases listed in Annex III.

**However**, profiling of natural persons (as defined in art. 4(4) GDPR) is **always** high-risk if it falls under Annex III — derogation does not apply.

**Documentation duty** (art. 6(4)): a provider claiming derogation must document its assessment **before** placing the system on market or putting it into service, and register the system in the EU database (art. 49(2)). The Commission must be able to require that documentation.

**Reclassification by Commission** (art. 7): the Commission may, by delegated act, **add new use cases** to Annex III based on Article 7 criteria. Track these acts.

### 1.3 Limited risk — art. 50 transparency

Not "high-risk light" — a **separate, parallel regime** of transparency obligations. Applies regardless of Annex III status.

Four categories trigger art. 50:

| Trigger | Obligation | Bound to |
|---------|-----------|----------|
| AI system intended to **interact directly with natural persons** (chatbots, voice assistants) | Inform the person they are interacting with an AI, unless **obvious from context** to a reasonably informed person | Provider (system design) |
| AI system that **generates synthetic audio, image, video or text content** ("generative AI") | **Mark outputs** in machine-readable format as artificially generated/manipulated, ensuring detectability | Provider |
| **Emotion recognition** or **biometric categorisation** system | Inform natural persons exposed to its operation; comply with GDPR/LED for personal data | Deployer |
| **Deep fake** (AI-generated/manipulated image, audio, video resembling real persons/objects/places) | **Disclose** that the content has been artificially generated or manipulated | Deployer |
| AI-generated text published to inform the public on **matters of public interest** | **Disclose** that text was artificially generated or manipulated, **unless** AI-generated content has undergone human review or editorial control with editorial responsibility | Deployer |

**Carve-outs**: art. 50(2)–(4) provide narrow exceptions for (a) law enforcement use, (b) artistic/satirical/fictional works (deep fake disclosure may be done in a way that doesn't impair display/enjoyment), (c) where authorised by law for public-interest purposes.

In application from **2026-08-02** (unchanged by the AI Omnibus). One Omnibus adjustment: generative systems already on the market before 2026-08-02 get a grace period for the art. 50(2) machine-readable marking requirement, until **2026-12-02**.

### 1.4 Minimal risk

Default. No mandatory obligations. The Commission and Member States encourage **voluntary codes of conduct** (art. 95) covering transparency, accessibility, sustainability, etc.

## 2. The 14-signal classification questionnaire

Adapted from the codified logic in `assessmentService.ts`. Use as a structured intake when classification is non-obvious.

| # | Signal | Values | Tier influence |
|---|--------|--------|----------------|
| 1 | Sector | Healthcare / Finance / HR / Education / Public sector / Justice / Border / Critical infra / Other | Sector match against Annex III triggers high-risk pathway B |
| 2 | Application domain | Recruitment / Credit scoring / Triage / Tutoring / Surveillance / Recommendation / Other | Match against Annex III sub-cases |
| 3 | End-users | Citizens / Employees / Students / Patients / Suspects / Migrants / Internal staff | Vulnerable groups raise art. 5(1)(b) salience; affect FRIA scope |
| 4 | Geographical scope | EU-wide / Member State / regional / local | All affect AI Act if EU output is used (art. 2) |
| 5 | Sensitive data | yes / limited / no | GDPR special-category data raises art. 10(5) salience |
| 6 | Discrimination risk | high / medium / low | Annex III §4 (employment) and §5 (essential services) raise risk |
| 7 | User informed | full / partial / none | Affects art. 13 + art. 50 design |
| 8 | Explainability level | high / medium / low | Affects art. 13 + art. 14 design choices |
| 9 | Human oversight | full / intermittent / minimal | Art. 14 — "minimal" oversight on Annex III is a red flag |
| 10 | Override capability | yes / limited / no | Required by art. 14(4)(d) for high-risk |
| 11 | Autonomy level | high / medium / low | Higher autonomy = stricter art. 14 oversight measures |
| 12 | Safety impact | critical / significant / minimal | Critical → check Annex I (Pathway A) and art. 5 |
| 13 | Decision consequences | irreversible / reversible / advisory | Irreversible → high-risk presumption + art. 6(3) derogation unavailable |
| 14 | Profiles natural persons (GDPR art. 4(4))? | yes / no | If yes AND Annex III: art. 6(3) derogation unavailable |

### Decision logic (informal)

```
If any art. 5 trigger fires (incl. the Omnibus NCII/CSAM prohibition, applicable 2026-12-02),
AND no carve-out, AND not eligible for art. 5(2)–(4) law-enforcement exception:
    → UNACCEPTABLE. Stop. Do not place on market.
Else if Annex I product + third-party conformity assessment required (Pathway A):
    → HIGH-RISK (effective 2028-08-02, post-Omnibus).
Else if Annex III §1–§8 use-case match (Pathway B):
    If profiling of natural persons:
        → HIGH-RISK (no derogation).
    Else evaluate art. 6(3) derogation — at least one of (a)(b)(c)(d):
        If derogation available AND documented + registered (art. 49(2)):
            → MINIMAL-equivalent (subject to derogation file).
        Else:
            → HIGH-RISK.
Else if art. 50 trigger fires (chatbot, generative output, emotion/biometric category, deep fake, AI-public-interest text):
    → LIMITED RISK (transparency obligations only).
Else:
    → MINIMAL.

Independently:
If GPAI model:
    → arts. 51–55 apply (see 10-gpai-and-timeline.md).
    If cumulative training compute > 10²⁵ FLOPs OR designated by Commission:
        → SYSTEMIC-RISK GPAI. Add art. 55 obligations.
```

## 3. Edge cases and traps

### 3.1 Substantial modification (art. 25)

A deployer who **substantially modifies** a high-risk AI system, or who **uses** an AI system for a purpose other than that intended by the original provider in a way that makes it high-risk, **becomes a provider** for that modified system. They inherit the full provider regime (arts. 16, 17, 9–15, 49 registration, etc.).

Triggers include: changing the intended purpose, retraining with substantially different data, fine-tuning that materially changes behaviour or performance characteristics. Cosmetic re-skinning is not substantial modification; behavioural change is.

### 3.2 Foundation model fine-tuned for high-risk use

Fine-tuning a third-party GPAI model (e.g., Llama, GPT-OSS) for an Annex III use case typically constitutes substantial modification. The fine-tuner **becomes the provider** of the high-risk system for that deployment. Original GPAI provider's art. 53 obligations do not transfer.

### 3.3 Open-source GPAI

Free and open-source GPAI models without monetisation by the provider are exempt from arts. 53(1)(a)(b) (technical documentation and downstream provider information) — but **not** from art. 53(1)(c) (copyright policy) and not from art. 55 if the model has systemic risk.

### 3.4 Tooling and scaffolding

A tool that *enables* an Annex III use (e.g., a recruitment platform with optional AI screening modules) is not itself high-risk on that ground alone. The high-risk classification attaches to the **AI system intended for** the Annex III use. If your product configures an AI to do CV screening, that configured AI is the high-risk system.

### 3.5 EU output even if non-EU operation

Per art. 2(1)(c), the AI Act applies to **providers and deployers** of AI systems located in third countries where the **output produced by the system is used in the EU**. A US SaaS that generates EU credit scores from a Texas data centre falls in scope.

### 3.6 Risk shifting via component decomposition

Slicing a high-risk system into "modules" each of which performs a narrow procedural task does not avoid classification. The competent authority looks at **intended use** of the system as placed on market — not the engineering decomposition.

## 4. Codified expertise from the Navigator project

The platform's existing classification logic (`server/services/assessmentService.ts`) operationalizes this rubric with:

- **Detection of art. 5 triggers** via keyword/sector matching (subliminal, social scoring, biometric categorisation by sensitive attributes, real-time biometric ID, facial scraping)
- **Annex III matching** across the 8 domains with sub-case granularity
- **Art. 50 trigger detection** (chatbot, deepfake, synthetic content, high autonomy + low explainability)
- **Multi-dimensional augmentation scoring** aggregated into AI Act categorical risk via tier-thresholds (each implementation chooses its own dimensions and weights)
- **Inverse mapping** for safety/discrimination signals (lower discrimination score = higher risk)

Any organization-specific scoring layer is **augmentative**, not authoritative for AI Act classification. Authoritative tiering follows arts. 5/6/Annex III/50 rubric above. Internal scoring layers are useful for **maturity assessment** (see ISO 42001 cl. 9.1 monitoring) and for **prioritisation of remediation**, not for the binary "is this high-risk" question.

## 5. Output template for classification

When you classify a system, output:

```
SYSTEM: <name>
PROVIDER ROLE: <provider | deployer | both | importer | distributor>
PRIMARY TIER: <unacceptable | high | limited | minimal>
HIGH-RISK PATHWAY: <Annex I (art. 6(1)) | Annex III §X (art. 6(2)) | not applicable>
ANNEX III DOMAIN: <§1 biometrics | §2 critical infra | ... | §8 justice/democratic>
ART. 6(3) DEROGATION: <claimed: (a)/(b)/(c)/(d) | not eligible | profiles natural persons → unavailable>
ART. 50 TRIGGERS: <chatbot | generative content | emotion/biometric cat | deepfake | AI-public-text | none>
GPAI REGIME: <not GPAI | GPAI standard | GPAI systemic risk>
EFFECTIVE DATE: <2025-02-02 | 2025-08-02 | 2026-08-02 | 2026-12-02 | 2027-12-02 | 2028-08-02 (post-Omnibus)>
RATIONALE: <2-3 sentences citing art./Annex/§ that triggered classification>
KEY UNCERTAINTIES: <list, e.g., "depends on whether decision is materially influenced — see art. 6(3)(c)">
NEXT STEPS: <e.g., "If high-risk: read 02-high-risk-obligations.md and 03-iso-42001-aims.md; conduct FRIA per 07-fria-art27.md if deployer">
```

Always include the rationale and uncertainties. Compliance officers are responsible for the final determination; your output supports their decision.

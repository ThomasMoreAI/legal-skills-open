# 08 — Transparency Obligations (AI Act art. 50)

Article 50 establishes a **horizontal transparency regime** that applies regardless of risk tier — minimal, limited, or high-risk systems can all trigger art. 50 in addition to their tier-specific obligations. The article distributes obligations between **provider** (system design) and **deployer** (operational disclosure).

**In application from 2026-08-02** (art. 113(b) — unchanged by the 2026 AI Omnibus). Tier-2 sanctions: €15M or 3% global turnover (art. 99(4)(g)).

**Omnibus grace period**: generative AI systems already placed on the market before 2026-08-02 get until **2026-12-02** to comply with the art. 50(2) machine-readable marking requirement. All other art. 50 obligations (chatbot disclosure, deepfake disclosure, emotion/biometric notification, public-interest text) apply from 2026-08-02 with no grace.

## 1. The four trigger families

| § | Trigger | Bound to | Obligation |
|---|---------|----------|------------|
| **art. 50(1)** | AI system intended to **interact directly with natural persons** (chatbots, voice assistants, virtual agents) | **Provider** (system design) | Inform the person they are interacting with an AI, **unless obvious from context** to a reasonably well-informed, observant person taking circumstances into account. Disclosure made in **clear and distinguishable manner** at the latest at the time of the first interaction or exposure |
| **art. 50(2)** | AI system that **generates synthetic audio, image, video or text content** | **Provider** | Ensure outputs are **marked in machine-readable format** as artificially generated/manipulated. Solutions shall be **effective, interoperable, robust and reliable** as far as technically feasible, taking account of: specificities and limitations of various types of content, costs of implementation, generally acknowledged state of the art (potentially reflected in relevant technical standards) |
| **art. 50(3)** | **Emotion recognition** OR **biometric categorisation** system | **Deployer** | Inform natural persons exposed of the operation of the system and process personal data per GDPR/LED |
| **art. 50(4) ¶1** | **Deep fake** (AI-generated/manipulated image, audio, video that resembles existing persons, objects, places, entities, events; appears authentic or truthful) | **Deployer** | **Disclose** that the content has been artificially generated or manipulated |
| **art. 50(4) ¶2** | AI-generated/manipulated **text** published with the purpose of informing the public on **matters of public interest** | **Deployer** | **Disclose** that the text was artificially generated or manipulated, **unless** the AI-generated content has undergone a process of human review or editorial control AND a natural or legal person holds editorial responsibility for publication |

## 2. Carve-outs and limitations

### 2.1 Law enforcement carve-out (art. 50(1)(2)(3) carve-outs)

Disclosure obligations under art. 50(1) (chatbots), art. 50(2) (synthetic content), and art. 50(3) (emotion recognition / biometric categorisation) **do not apply** to AI systems authorised by **law to detect, prevent, investigate or prosecute criminal offences**, subject to appropriate safeguards for the rights and freedoms of third parties, unless those systems are available for the public to report a criminal offence.

### 2.2 Artistic / satirical / fictional carve-out (art. 50(4))

For deep fakes that are part of an evidently artistic, creative, satirical, fictional or analogous work or programme, the disclosure obligations are limited to disclosing the existence of such generated or manipulated content **in an appropriate manner that does not hamper the display or enjoyment of the work**.

### 2.3 Editorial-responsibility carve-out (art. 50(4) ¶2)

For AI-generated text on public-interest matters, the disclosure obligation **does not apply** where the AI-generated content has undergone:
- A process of human review or editorial control, AND
- A natural or legal person holds editorial responsibility for the publication

This carve-out is the editorial press shield. A newspaper that uses AI-assisted drafting and applies its standard editorial process is not required to label individual articles as AI-assisted under art. 50(4)¶2 — though may still face national-law transparency or professional standards.

### 2.4 Implementation flexibility (art. 50(5))

The information referred to in paragraphs 1, 2, 3, and 4 shall be provided to the natural persons concerned in a **clear and distinguishable manner at the latest at the time of the first interaction or exposure**. The information shall conform to the applicable accessibility requirements.

## 3. Technical implementation: machine-readable marking (art. 50(2))

The provider obligation under art. 50(2) — to mark synthetic outputs as artificially generated — is the most technically substantive part of art. 50. It interacts with multiple emerging standards.

### 3.1 Standard families

| Family | Description | Strength | Limitation |
|--------|-------------|----------|------------|
| **C2PA (Content Credentials)** | Cryptographic provenance manifests embedded in media files. Backed by Adobe, Microsoft, BBC, Sony, Truepic, OpenAI, etc. | Tamper-evident; cryptographically signed; standardized (ISO/IEC AWI 22144 in development) | Removable by re-encoding / format conversion if metadata stripped |
| **SynthID (Google DeepMind)** | Statistical text/image watermarking embedded in model output | Survives common transformations | Vendor-proprietary; text watermarks degraded by paraphrasing |
| **Adversarial-robust watermarks (research, e.g., Stable Signature, Tree-Ring)** | Embed signal in latent or output layers | Resilient to certain attacks | Specific to model architecture; ongoing research |
| **Statistical text watermarks (Kirchenbauer et al.)** | Bias token sampling to encode signal | No model retraining needed | Detectability degraded by paraphrasing, translation |
| **Cryptographic image hashes + registry** | Hash on generation, register in immutable log | Verifiable | Doesn't survive transformation; requires registry availability |
| **Metadata standards (EXIF, XMP, IPTC)** | Add "AI-generated" flag in standard metadata | Easy to implement | Easily stripped (e.g., screenshot, social-media re-upload) |

### 3.2 Practical recommendation

A **layered approach** is the only currently defensible posture for art. 50(2):

1. **C2PA Content Credentials** — primary; provides cryptographic provenance
2. **Visible label or icon** in UI where AI-generated content is displayed (covers the "machine-readable" with a human-readable companion)
3. **Statistical/cryptographic watermark** in the output itself (SynthID for text/image, audio watermark for audio) — survives metadata stripping
4. **Generation log / API-level provenance** — central log of all generated artefacts with content hash, retrievable for verification

**Note**: art. 50(2) explicitly allows for "**generally acknowledged state of the art (potentially reflected in relevant technical standards)**" considerations — the obligation is one of technical effort, not perfection. A provider that documents its layered approach + monitors technical evolution + adopts new state-of-the-art when feasible meets the spirit of the article.

### 3.3 What art. 50(2) does NOT require

- Watermarking that is invisible to the model's intended use case (e.g., perfect imperceptibility for artistic image generation)
- Resilience against all conceivable attack (state-of-the-art is the bar)
- Per-token watermarking for text (sentence-level or document-level marking is acceptable)
- Watermarking in the inference path that doubles latency (cost considerations are explicitly acknowledged)

## 4. Coordinated obligations: art. 50 + art. 13 + art. 14

A high-risk AI system that is also a chatbot or generative system carries **multiple parallel transparency duties**:

- Art. 13 → instructions for use **to the deployer** (technical doc-level transparency)
- Art. 14 → human oversight **measures designed in by provider, implemented by deployer**
- Art. 50 → disclosure **to natural persons** exposed to the system (operational UX-level transparency)

The deployer must integrate all three. A typical UX architecture:

```
USER ENCOUNTERS AI SYSTEM
   │
   ├─→ At first interaction:
   │    - Art. 50(1): "You're interacting with an AI" (banner, voice cue, in-app message)
   │    - Art. 14 measures: "You can request human review at any time" (link/button)
   │
   ├─→ During interaction:
   │    - Art. 50(2): synthetic content marked (C2PA + visible label)
   │    - Art. 50(3): emotion-recognition/biometric notice if applicable
   │    - Art. 14: visible override / stop control
   │
   └─→ Post-decision (if high-risk decision-making):
        - Art. 86: right to clear and meaningful explanation
        - Art. 26(10): explanation interface (where decision affects the natural person)
```

## 5. ISO 42001 alignment

| Art. 50 obligation | ISO 42001 anchors |
|--------------------|-------------------|
| Inform of AI interaction (50(1)) | A.8.5 (information for interested parties), A.6.2.5 (deployment — embed disclosure) |
| Mark synthetic content (50(2)) | A.6.2.6 (operation + monitoring), A.6.2.7 (technical doc — declare watermarking method) |
| Inform of emotion/biometric categorisation (50(3)) | A.8.5, A.9.2 (responsible-use processes) |
| Disclose deep fakes (50(4)¶1) | A.8.5, A.9.2 |
| Disclose AI-generated public-interest text (50(4)¶2) | A.8.5, A.9.2; editorial control mapped to A.10.2 |

## 6. Implementation checklist

```
ART. 50 IMPLEMENTATION CHECKLIST

[ ] Identify which of art. 50(1) (chatbot), 50(2) (synthetic content), 50(3) (emotion/biometric), 50(4)¶1 (deepfake), 50(4)¶2 (AI public-interest text) apply
[ ] Identify whether obligation is on provider or deployer per the trigger
[ ] If chatbot (50(1) — provider):
    [ ] Disclosure at first interaction / onboarding
    [ ] Clear and distinguishable manner
    [ ] Accessibility-compliant
    [ ] Document carve-out if "obvious from context" relied upon
[ ] If synthetic content generator (50(2) — provider):
    [ ] C2PA Content Credentials embedded in outputs
    [ ] Statistical / cryptographic watermark in payload
    [ ] Visible UI label for human users
    [ ] Documentation of "state of the art" considered + chosen
    [ ] Document technical limitations honestly (paraphrasing-vulnerability, etc.)
[ ] If emotion recognition / biometric categorisation (50(3) — deployer):
    [ ] Notice to natural persons exposed (signage, in-app, written)
    [ ] GDPR Art. 13/14 information notice (if personal data)
    [ ] LED-compliant for law-enforcement deployers
[ ] If deep fake (50(4)¶1 — deployer):
    [ ] Visible disclosure ("AI-generated" or equivalent)
    [ ] Document artistic/satirical carve-out if applied (with rationale)
[ ] If AI text on public interest (50(4)¶2 — deployer):
    [ ] Disclosure on the article/post
    [ ] OR document editorial-responsibility carve-out (named editor + process)
[ ] Accessibility: ensure disclosures are accessible (screen readers, alt text, sufficient contrast)
[ ] Localization: disclosures in language(s) of intended audience
[ ] Update process: maintain disclosure as content/system evolves
```

## 7. Anti-patterns

1. **Single-line ToS disclosure** — burying "this product uses AI" deep in terms of service is **not compliant**. Disclosure must be at first interaction, clear, distinguishable.

2. **Watermarking-only approach for synthetic content** — relying solely on SynthID (or similar) without C2PA + visible labels misses the layered approach that current state-of-the-art actually entails.

3. **Treating "obvious from context" carve-out broadly** — the carve-out is narrow. A voice that sounds robotic does not count as "obvious"; a virtual agent in a customer-service portal that may pass for human does not qualify. When in doubt, disclose.

4. **Forgetting the deployer/provider split** — providers cannot fulfill art. 50(3) (deployer's obligation to inform persons exposed) on the deployer's behalf. The provider can ship an AI emotion-recognition system; the deployer must operationalize disclosure to data subjects. Misalignment commonly leaves a compliance gap.

5. **Editorial-responsibility shield for unreviewed AI articles** — a publisher claiming the art. 50(4)¶2 carve-out without an actual editorial review process is a sanctions risk. Document the process.

6. **Watermarking for "all" synthetic outputs without considering applicability** — art. 50(2) does NOT require watermarking of personal/non-public outputs (e.g., a private LLM session that doesn't produce shareable content). Scope wisely.

## 8. Output template (when asked to design art. 50 disclosure UX)

```
ART. 50 DISCLOSURE DESIGN — <SYSTEM NAME>

TRIGGERS APPLICABLE:
[ ] 50(1) Chatbot/voice agent (Provider)
[ ] 50(2) Synthetic content generator (Provider)
[ ] 50(3) Emotion recognition / biometric categorisation (Deployer)
[ ] 50(4)¶1 Deep fake (Deployer)
[ ] 50(4)¶2 AI text on public-interest matter (Deployer)

DISCLOSURE TOUCHPOINTS:
1. Onboarding / first-interaction:
   - Modality: <modal | banner | voice prompt | written notice>
   - Copy: "<exact disclosure text>"
   - Localization: <languages>
   - Accessibility: <ARIA, contrast, screen-reader tested>
   - Dismissibility: <persistent | dismissible-with-acknowledgment>

2. During interaction:
   - Persistent indicator: <icon, badge, "AI-assisted" label>
   - Output marking (if 50(2)):
     - C2PA: <yes/no, manifest schema>
     - Watermark: <method, vendor, robustness claim>
     - Visible label: <UI element>
     - Metadata: <EXIF/XMP/IPTC fields>
     - Generation log: <storage location, retention>

3. Post-interaction:
   - Right to explanation interface: <link, format, SLA>
   - Complaint mechanism: <channel, SLA>

CARVE-OUTS RELIED UPON: <none | art. 50(...) — rationale documented>

EVIDENCE BASE:
- UX mockups: <link>
- Accessibility audit: <ref, date>
- Localization review: <ref, languages>
- C2PA manifest sample: <ref>
- Watermark robustness report: <ref>
- Editorial-control SOP (if 50(4)¶2 carve-out): <ref>

REVIEW SCHEDULE: <quarterly / on system update>
```

# 13 — Regulatory Sandboxes & Real-World Testing (AI Act art. 57–63)

The AI Act provides **two pre-market controlled-experimentation regimes** that high-risk and innovation-stage providers should know about — they reduce regulatory risk, accelerate market access, and are mandatory for Member States to provide.

| Regime | Article | Setting | Purpose |
|---|---|---|---|
| **Regulatory sandbox** | **art. 57–59** | Inside a controlled, supervised environment by a competent authority | Develop, train, validate, test innovative AI systems pre-market with regulator oversight |
| **Testing in real-world conditions outside a sandbox** | **art. 60** | In real conditions (production-like) but with consent + safeguards | Assess performance under real conditions before placing on market — high-risk only |

## 1. Regulatory sandboxes — art. 57–59

### 1.1 Art. 57 — Establishment

Each Member State **shall establish at least one regulatory sandbox at national level** by **2027-08-02** (art. 57(1) + art. 113 — deferred by the 2026 AI Omnibus from 2026-08-02; the Omnibus also expanded EU-level sandbox access). Sandboxes may be set up jointly with one or several other Member States, regional, or local. Joint sandboxes coordinated via the AI Office. Member States may open sandboxes earlier — check national availability.

**Operator**: Member State competent authority + Data Protection Authority (DPA) + other relevant national authorities. Multi-disciplinary by design.

### 1.2 Art. 57(5) — Concrete benefits for participants

The sandbox provides:

(a) Guidance on regulatory expectations, on how to fulfil the requirements and obligations of the AI Act
(b) **Supervised testing** in a controlled environment
(c) Identification of **specific risks** to fundamental rights, health and safety
(d) Identification of **mitigation measures**
(e) Cooperation with other relevant actors (including DPA, national notified bodies)
(f) **Written exit report** documenting the activities, results and lessons (this is the operative deliverable for downstream conformity)

### 1.3 Art. 57(7)–(9) — Liability and enforcement carve-outs

Two key protections:

- **Liability protection** (art. 57(12)): participants remain liable for damage inflicted on third parties, but Member States **shall not impose administrative fines** for infringements of national or EU law identified during the sandbox **provided** the participant respects the sandbox plan and complies in good faith with the supervisor's guidance. This is the headline benefit.
- **Cross-jurisdictional learnings**: art. 57(11) — sandbox findings, anonymised, are shared via the AI Office across Member States.

### 1.4 Art. 58 — Common rules for sandbox operation

Commission shall adopt implementing acts (under art. 58(1)) specifying:

(a) Eligibility criteria
(b) Procedure for application, selection, participation, exit
(c) Terms applicable to participants
(d) Rights and obligations of participants and authorities
(e) Modalities for cooperation with other authorities
(f) Inter-Member State coordination

Track Commission implementing acts published under art. 58 — they are the operative rulebook.

### 1.5 Art. 59 — Processing of personal data in the sandbox

Specific lawful basis for **processing personal data lawfully collected for other purposes**, in the sandbox, when:

- The AI system is being developed for **substantial public interest**: public safety + public health, environmental protection, climate change, energy sustainability, transport safety, healthcare, social protection, public administration
- Effective monitoring mechanisms in place
- Enhanced data-protection safeguards (anonymisation, pseudonymisation, access controls, deletion at exit)
- Output cannot be used to take measures or decisions affecting the data subjects
- Data not transmitted, transferred, accessed by other parties
- Personal data deleted at sandbox exit unless lawful retention basis

This is a **GDPR-derogating provision** for sandbox-stage development of substantial-public-interest AI. Use it deliberately and document everything.

### 1.6 Sandbox application strategy

Eligible candidates often include:

- High-risk AI systems intended for public benefit (healthcare diagnostics, fraud detection, smart-grid management)
- GPAI providers seeking pre-publication evaluation against systemic-risk dimensions (art. 55)
- Innovation-stage SMEs developing in Annex III domains who would otherwise be deterred by conformity-assessment cost
- Public-sector AI procurement cases where the deployer wants regulator-validated mitigation before signing

Application package typically includes: system description, risk profile, foreseen Annex IV §6 changes, fundamental-rights impact summary, intended-purpose statement, exit criteria.

## 2. Testing in real-world conditions outside a sandbox — art. 60

A **separate** regime allowing testing of high-risk AI systems in real-world conditions **outside** a sandbox, subject to safeguards. Useful when sandbox capacity is unavailable or sandbox is unsuitable for the system's deployment context.

### 2.1 Art. 60(1)–(3) — Conditions

Testing in real-world conditions **shall be allowed** if:

(a) Provider or prospective provider has drawn up a **real-world testing plan** and submitted it to the market surveillance authority of the Member State of testing
(b) Market surveillance authority has approved the plan and conditions for testing (or, after 30 days of submission, has not objected — implicit approval)
(c) Provider/prospective provider, with applicable deployer if testing involves a deployer, **registers the testing** in the EU database referred to in art. 71 with EU-wide unique identification number
(d) Provider/prospective provider has **established residence in the Union** or has appointed a legal representative in the Union
(e) **Subjects' informed consent** is obtained per art. 61 — see § 2.2 below
(f) The system is tested under appropriate human oversight by qualified persons
(g) Decisions or predictions of the system can be **effectively reversed and disregarded**
(h) Personal data processed in the test is deleted upon withdrawal of consent or end of testing, unless laws of Union or Member State provide otherwise
(i) Testing is conducted under effective oversight by provider, prospective provider, or applicable deployer, by qualified competent persons
(j) Decisions/predictions can be reversed
(k) **Confidential** until placed on market — providers/deployers are not required to disclose information that may harm trade secrets, IP rights, or commercial confidentiality

### 2.2 Art. 61 — Informed consent

Subjects whose data is used must, before participation, freely give **informed consent** in accordance with provisions:

- Nature, purpose, duration of testing
- Conditions under which testing will be conducted, including expected duration of subjects' participation
- Subjects' rights and guarantees regarding their participation, in particular **right to refuse to participate** and **right to withdraw at any time** without any resulting detriment and without having to provide any justification
- Modalities for requesting reversal or disregarding of decisions or predictions
- EU-wide unique identification number for testing per art. 60(4)(c)
- Contact details of provider, prospective provider, applicable deployer

Withdrawal of consent **shall not affect the activities already carried out**.

### 2.3 Art. 62–63 — Specific rules for SMEs and procedural simplifications

Member States shall give SMEs and start-ups **priority access** to sandboxes (art. 62). Commission may also provide standardised templates for testing plans.

### 2.4 Real-world testing duration limits

Testing in real-world conditions is **limited to 6 months**, extendable by a further 6 months with prior notification to the market surveillance authority and justification. Maximum total: **12 months**.

## 3. ISO anchors

| Activity | ISO/IEC 42001 | Companion |
|---|---|---|
| Sandbox plan content | cl. 6.1.4 (AISIA), 8.2 (operational risk assessment), 8.4 (impact assessment); A.5.2 (AISIA process) | ISO/IEC 42005:2025 (impact assessment depth) |
| Real-world test plan | cl. 8.1 (operational planning), 8.2, 8.3, 9.1 (monitoring); A.6.2.4 (V&V), A.6.2.6 (operation/monitoring) | ISO/IEC 24029-2 (robustness assessment design) |
| Subject consent records | cl. 7.5 (documented info), 7.4 (communication); A.8.4 (incident communication for adverse events), A.8.5 (info for parties) | — |
| Personal-data safeguards in sandbox | cl. 6.1.4 + A.5.4 (impact); A.7.4 (data quality); A.10.3 (suppliers — DPA) | ISO/IEC 27701 (PIMS) for residual GDPR governance |
| Exit report | cl. 9.1 + 10.1 (continual improvement) | — |

## 4. Decision aid — sandbox vs real-world testing vs neither

```
Q1: Are you developing an innovative AI system whose conformity path is unclear?
    → If yes, prefer SANDBOX (art. 57) for liability shield + regulator guidance.

Q2: Is sandbox capacity unavailable or sandbox-incompatible with your deployment context?
    → Consider art. 60 real-world testing.

Q3: Is your system already CE-marked and only needs incremental V&V?
    → Neither. Use post-market monitoring (art. 72) + AIMS cl. 9.1 + 10.1.

Q4: Are you a GPAI provider needing systemic-risk evaluation (art. 55)?
    → Sandbox is suitable; combine with Code of Practice (art. 56) measures.

Q5: Are you processing personal data without a clear primary GDPR lawful basis?
    → SANDBOX (art. 59) provides a derogating basis for substantial-public-interest cases.
```

## 5. Common misconceptions

1. **"Sandboxes give immunity from sanctions"** — false. Liability for damage to third parties remains; only **administrative fines** for AI Act / national infringements are waived, and only if the participant respects the sandbox plan in good faith (art. 57(12)).
2. **"Real-world testing under art. 60 is the same as a beta launch"** — false. It requires market-surveillance-authority approval, EU database registration, informed consent per art. 61, and **6+6 month duration cap**. A perpetual beta is not real-world testing.
3. **"Sandbox exit report is internal"** — false. The exit report is a **regulator artefact**. It feeds into the AI Office's cross-jurisdictional learnings (art. 57(11)) and can serve as conformity-assessment evidence downstream.
4. **"Sandboxes are only for SMEs"** — false. SMEs and start-ups have **priority access** (art. 62) but sandboxes are open to all eligible candidates.
5. **"Real-world testing satisfies art. 9 RMS"** — partially. It generates evidence *toward* art. 9 but does not replace the iterative lifecycle RMS. Both are needed.

## 6. Output template — sandbox / real-world testing readiness

```
SYSTEM: <name>
PROPOSED REGIME: <sandbox art. 57 | real-world art. 60 | neither>

ELIGIBILITY
  [ ] System is in pre-market or substantial-modification stage
  [ ] Member State sandbox available (or art. 60 viable)
  [ ] Provider has EU establishment or appointed legal rep (art. 60(4)(d))
  [ ] Substantial-public-interest case (sandbox art. 59 personal-data derogation)? <yes/no>

PLAN COMPONENTS (sandbox)
  [ ] System description + intended purpose
  [ ] Risk profile (initial AISIA per ISO 42001 cl. 6.1.4)
  [ ] Foreseen mitigations
  [ ] Exit criteria + exit report scope

PLAN COMPONENTS (real-world testing)
  [ ] Real-world testing plan (art. 60(1)(a))
  [ ] Market surveillance authority submission (art. 60(2)) — date sent, date approved/30d-elapsed
  [ ] EU database registration (art. 60(4)(c)) — unique ID
  [ ] Informed-consent template per art. 61 — content checked against arts. 61(1)(a)–(g)
  [ ] Human-oversight design (art. 60(4)(g))
  [ ] Reversal/disregard mechanism (art. 60(4)(j))
  [ ] Personal-data deletion plan on withdrawal (art. 60(4)(h))
  [ ] Duration: ≤ 6 months (extendable +6, max 12)

EVIDENCE AT EXIT
  - Sandbox: written exit report (art. 57(5)(f))
  - Real-world: testing report aligned with Annex IV §3 (functioning + control)

NEXT STEPS
  - Sandbox: feed exit report into Annex IV technical documentation
  - Real-world: feed testing report into art. 11 + Annex IV; address findings before placing on market

CITATIONS
  - AI Act art. 57, 58, 59, 60, 61, 62, 63
  - AI Act art. 113 (sandbox availability deadline 2027-08-02, post-Omnibus)
  - ISO/IEC 42001:2023 cl. 6.1.4, 8.1–8.4, 9.1; Annex A.5.2, A.6.2.4, A.6.2.6, A.8.4, A.8.5
  - ISO/IEC 42005:2025 (impact assessment)

LEGAL DISCLAIMER
  Decision-support output. Not legal advice. Sandbox eligibility and
  art. 60 real-world testing approval are fact-intensive determinations
  by competent authorities; obtain qualified counsel before submission.
```

## 7. Cross-references

- `01-risk-classification.md` (only high-risk systems use art. 60 real-world testing).
- `02-high-risk-obligations.md` (real-world testing evidence feeds Annex IV § 3 and § 9 post-market).
- `07-fria-art27.md` (sandbox plans should integrate FRIA inputs for deployer-stage participants).
- `09-post-market-art72-73.md` (post-market monitoring picks up where real-world testing leaves off).
- `10-gpai-and-timeline.md` (GPAI providers can use sandboxes for art. 55 evidence).

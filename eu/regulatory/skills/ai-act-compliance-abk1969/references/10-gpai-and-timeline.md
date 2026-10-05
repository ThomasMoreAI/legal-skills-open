# 10 — GPAI Obligations, Sanctions, Timeline (AI Act art. 51–55, 99, 113)

This reference covers three thematically distinct but operationally linked topics:

1. **General-purpose AI (GPAI)** model regime — arts. 51–55 — a parallel regulatory axis to the risk-based regime
2. **Sanctions** — art. 99 — the enforcement mechanism
3. **Application timeline** — art. 113 — when each obligation enters into force

Each interacts with ISO 42001 / 27090 differently and is consequential for project planning.

## 1. General-Purpose AI (GPAI) — arts. 51–55

### 1.1 Definitions (art. 3(63), (66), (67))

- **GPAI model** (art. 3(63)): an AI model, including where such an AI model is trained with a large amount of data using self-supervision at scale, that displays significant generality and is capable of competently performing a wide range of distinct tasks regardless of the way the model is placed on the market and that can be integrated into a variety of downstream systems or applications. This does not cover AI models that are used for research, development or prototyping activities before they are placed on the market.

- **GPAI system** (art. 3(66)): an AI system which is based on a GPAI model and which has the capability to serve a variety of purposes, both for direct use as well as for integration in other AI systems.

- **Systemic risk** (art. 3(65)): a risk that is specific to the high-impact capabilities of GPAI models, having a significant impact on the Union market due to their reach, or due to actual or reasonably foreseeable negative effects on public health, safety, public security, fundamental rights, or the society as a whole, that can be propagated at scale across the value chain.

### 1.2 Classification: standard GPAI vs systemic-risk GPAI (art. 51)

**Standard GPAI**: any GPAI model meeting the art. 3(63) definition.

**GPAI with systemic risk** (art. 51(1)): a GPAI model is classified as having systemic risk if:

(a) It has high-impact capabilities evaluated on the basis of appropriate technical tools and methodologies, including indicators and benchmarks
(b) Based on a decision of the Commission, ex officio or following a qualified alert from the scientific panel, it has capabilities or impact equivalent to those set out in (a) having regard to the criteria set out in Annex XIII

**Presumption** (art. 51(2)): a GPAI model has high-impact capabilities when **the cumulative amount of computation used for its training measured in floating point operations is greater than 10²⁵ FLOPs**.

The Commission may, via delegated act under art. 51(3), amend the thresholds and add benchmarks/indicators in light of evolving technology.

**Notification obligation** (art. 52(1)): provider of a GPAI model that meets the systemic-risk condition shall notify the Commission **without delay and in any event within 2 weeks** after that requirement is met or it becomes known that it will be met.

### 1.3 Standard GPAI provider obligations (art. 53)

(1) Providers of GPAI models shall:

(a) **Draw up and keep up-to-date the technical documentation of the model**, including its training and testing process and the results of its evaluation, which shall contain, at a minimum, the information set out in **Annex XI** (intended for AI Office and competent authorities upon request)

(b) **Draw up, keep up-to-date and make available information and documentation to providers of AI systems** who intend to integrate the GPAI model into their AI systems. This information shall enable the downstream providers to have a good understanding of the capabilities and limitations and to comply with their obligations. The information shall, at a minimum, include the elements set out in **Annex XII**

(c) **Put in place a policy to comply with Union law on copyright and related rights**, in particular to identify and comply with, including through state-of-the-art technologies, a reservation of rights expressed pursuant to art. 4(3) of Directive (EU) 2019/790 (CDSM Directive)

(d) **Draw up and make publicly available a sufficiently detailed summary about the content used for training of the GPAI model**, according to a template provided by the AI Office

(2) Obligations under (a) and (b) shall **not apply to providers of AI models that are released under a free and open-source licence** that allows for the access, usage, modification, and distribution of the model, and **whose parameters, including the weights, the information on the model architecture, and the information on model usage, are made publicly available**. **Exception**: this carve-out does not apply to GPAI models with systemic risk.

### 1.4 Authorised representatives (art. 54)

Providers established outside the Union shall, prior to placing a GPAI model on the Union market, by written mandate, **appoint an authorised representative** which is established in the Union. The authorised representative cooperates with the AI Office and Commission and shall verify that the technical documentation per Annex XI has been drawn up and kept up-to-date.

### 1.5 Systemic-risk GPAI obligations (art. 55)

In addition to standard GPAI obligations, providers of GPAI models with systemic risk shall:

(a) **Perform model evaluation** in accordance with standardised protocols and tools reflecting the state of the art, including conducting and documenting **adversarial testing** of the model with a view to identifying and mitigating systemic risks

(b) **Assess and mitigate possible systemic risks at Union level**, including their sources, that may stem from the development, the placing on the market, or the use of GPAI models with systemic risk

(c) **Keep track of, document, and report**, without undue delay, to the AI Office and, as appropriate, to national competent authorities, **relevant information about serious incidents** and possible corrective measures to address them

(d) **Ensure an adequate level of cybersecurity protection for the GPAI model with systemic risk and the physical infrastructure of the model**

### 1.6 Code of Practice (art. 56)

The AI Office shall encourage and facilitate the drawing up of **codes of practice** at Union level in order to contribute to the proper application of the Regulation, taking into account international approaches. Adherence to a code of practice approved by the Commission may be relied upon to **demonstrate compliance** with arts. 53–55.

The **GPAI Code of Practice** was published in final form on **2025-07-10**, structured in three chapters: **Transparency** and **Copyright** (all GPAI providers, art. 53) and **Safety & Security** (systemic-risk providers, art. 55). The Commission and AI Board confirmed its **adequacy** on **2025-08-01**. It is the **operative compliance instrument** for arts. 53–55. Companion Commission instruments: **GPAI guidelines** clarifying the scope of provider obligations (2025-07-18) and the **training-data-summary template** for art. 53(1)(d) (2025-07-24). Commission enforcement powers, including art. 101 fines, apply from **2026-08-02**.

### 1.7 ISO 42001 + 27090 alignment for GPAI

| GPAI obligation | ISO 42001 anchors | ISO 27090 anchors |
|-----------------|-------------------|-------------------|
| Art. 53(1)(a) — Annex XI technical documentation | A.4.2, A.6.2.3, A.6.2.7 | sect. 6 (foundation model annex) for security part |
| Art. 53(1)(b) — Annex XII downstream-provider info | A.8.2, A.8.5, A.10.4 | sect. 6 (LLM threat info to downstream) |
| Art. 53(1)(c) — copyright policy | A.7.3 (data acquisition), A.10.3 (suppliers of data) | — |
| Art. 53(1)(d) — training data summary | A.4.2, A.7.5 (provenance), A.8.5 | — |
| Art. 55(1)(a) — model evaluation + adversarial testing | A.6.2.4 (V&V), cl. 9.1 | **All sections** — esp. red teaming, supply chain, GenAI annex |
| Art. 55(1)(b) — systemic risk assessment + mitigation | cl. 6.1.2 (AI risk), 6.1.4 (AISIA), A.5.5 (societal impact) | sect. 7 (threat-model template); cross-reference to NIST AI 100-2, MITRE ATLAS, AISI frameworks |
| Art. 55(1)(c) — incident reporting | cl. 10.2, A.8.3, A.8.4 | sect. 4.6 (operational incident response) |
| Art. 55(1)(d) — cybersecurity for model + infra | cl. 8.1, A.6.2.4, A.10.3 | **Whole standard** + ISO 27001/27002 baseline |

## 2. Sanctions — art. 99

### 2.1 Tiered fines

| Tier | Cap | Triggers |
|------|-----|----------|
| **Tier 1 (art. 99(3))** | **€35,000,000 or up to 7% of total worldwide annual turnover** of the preceding financial year, whichever is **higher** | Non-compliance with the prohibition of AI practices referred to in **art. 5** |
| **Tier 2 (art. 99(4))** | **€15,000,000 or up to 3%** | Non-compliance with: (a) provider obligations art. 16; (b) authorised-rep obligations art. 22; (c) importer obligations art. 23; (d) distributor obligations art. 24; (e) deployer obligations art. 26; (f) requirements + obligations of notified bodies under art. 31, 33(1)(3)(4), or 34; (g) **transparency obligations for providers and deployers per art. 50** |
| **Tier 3 (art. 99(5))** | **€7,500,000 or up to 1%** | Supply of incorrect, incomplete or misleading information to notified bodies or national competent authorities in reply to a request |

### 2.2 SME and start-up cap (art. 99(6))

For SMEs (including start-ups), each fine referred to in this article shall be **up to** the percentages or amounts referred to in para 3, 4, or 5, whichever thereof is **lower**.

In other words: for SMEs, the fine is capped at the **smaller** of fixed amount or percentage of turnover.

### 2.3 GPAI-specific fines (art. 101)

The Commission may impose fines on providers of GPAI models for:

(a) Infringing the relevant provisions of the Regulation
(b) Failing to comply with a request for a document or information per art. 91
(c) Failing to comply with a measure requested under art. 93
(d) Failing to make available to the Commission access to the GPAI model with systemic risk for the purpose of conducting an evaluation per art. 92

Fines: not exceeding **3% of the provider's worldwide annual turnover** in the preceding financial year **or €15 million**, whichever is **higher**.

### 2.4 Factors considered (art. 99(7))

When deciding on the amount of fines, in each individual case, all relevant circumstances are taken into account: nature, gravity, duration of infringement; size of operator; market share; intentional or negligent character; degree of cooperation; technical and organisational measures implemented; previous corrective actions; etc.

### 2.5 Periodic penalty payments (art. 99(8))

Without prejudice to administrative fines under (3)–(6), national competent authorities may impose periodic penalty payments to compel providers, deployers or notified bodies to respect their obligations.

## 3. Application timeline — art. 113, as amended by the 2026 AI Omnibus

> **AI Omnibus status (as of 2026-07-14)**: adopted (Parliament 2026-06-16; Council 2026-06-29); OJ publication expected July 2026, entry into force on the third day after publication. Until then the original art. 113 dates remain the formal baseline — **verify the OJEU**. The Omnibus set **fixed** deferred dates (the Commission's proposed standards-linked conditional trigger was dropped).

| Date | What enters into application |
|------|------------------------------|
| **2024-07-12** | OJ publication |
| **2024-08-01** | **Entry into force** (art. 113(1)) — 20 days after publication |
| **2025-02-02** | Chapter I (subject matter, scope, definitions) + **Chapter II (art. 5 prohibitions)** + art. 4 AI literacy apply |
| **2025-08-02** | Chapter III Section 4 (notifying authorities + notified bodies) + Chapter V (GPAI) + Chapter VII (governance) + Chapter XII (penalties — except art. 101 GPAI penalties) + art. 78 (confidentiality) apply |
| **2026-08-02** | **Art. 50 transparency** + art. 95 codes + remaining non-high-risk provisions + **Commission GPAI enforcement (art. 101 fines)**. High-risk obligations deferred by the Omnibus (below) |
| **2026-12-02** | New **art. 5 NCII/CSAM prohibition** (Omnibus) applicable; end of art. 50(2) marking grace period for generative systems on market before 2026-08-02 |
| **2027-08-02** | Member State **regulatory sandboxes** operational (art. 57, deferred from 2026-08-02); GPAI models placed on market before 2025-08-02 must comply with arts. 53–55 (art. 111) |
| **2027-12-02** | **High-risk obligations for stand-alone Annex III systems** (deferred from 2026-08-02) — Chapter III Sections 1–3, conformity assessment (arts. 40–49), registration |
| **2028-08-02** | Art. 6(1) (Annex I product-safety pathway) + corresponding obligations (deferred from 2027-08-02) — MDR, IVDR, automotive, civil aviation, etc.; machinery largely carved out by the Omnibus |

### 3.1 Transitional provisions (art. 111)

- **GPAI models placed on the market before 2025-08-02**: providers shall **comply with art. 53–55 by 2027-08-02** (2-year transition for GPAI placed on market before GPAI obligations applied).
- **High-risk AI systems placed on market before the (deferred) high-risk application date** and whose operators expect substantial changes after that date: subject to obligations from the date of substantial change.
- **High-risk AI systems intended for use by public authorities**: full conformity must be achieved by **2030-12-31** if placed on market before the high-risk application date.

### 3.2 Practical implementation roadmap

```
2024-08-01 → 2025-02-02 (6 months)
  - Inventory AI systems; classify against art. 5 (prohibited)
  - Stop or remediate any art. 5 practices
  - Establish AIMS scope (ISO 42001 cl. 4)

2025-02-02 → 2025-08-02 (6 months)
  - Identify GPAI exposure (provider or downstream user of GPAI)
  - For GPAI providers: prepare Annex XI + XII documentation, copyright policy, training data summary
  - Establish governance (Chapter VII)
  - For systemic-risk GPAI: implement art. 55 (red teaming, security, incident reporting)

2025-08-02 → 2026-08-02 (12 months)
  - Establish art. 50 transparency UX (chatbot disclosure, content marking) — due 2026-08-02
  - GPAI providers: close any gap before Commission enforcement (art. 101) starts 2026-08-02
  - Begin high-risk implementation (arts. 9–15) — deadline moved to 2027-12-02 but the runway is needed

2026-08-02 → 2027-12-02 (16 months — high-risk runway, post-Omnibus)
  - Implement NCII/CSAM technical safeguards by 2026-12-02 (new art. 5 prohibition)
  - Complete art. 50(2) machine-readable marking for pre-2026-08-02 generative systems by 2026-12-02
  - For high-risk AI systems: implement arts. 9–15 essential requirements
  - Establish QMS per art. 17 (ideally certify to ISO 42001)
  - Draft Annex IV technical documentation
  - Implement art. 12 logging, art. 13 instructions for use, art. 14 oversight, art. 15 acc/rob/cyb
  - Choose conformity-assessment path (art. 43); engage notified body if Annex VII
  - Issue declaration of conformity (art. 47), affix CE marking (art. 48)
  - Register in EU database (art. 49)
  - For deployers: prepare FRIA (art. 27); set up art. 26 oversight + monitoring
  - Establish post-market monitoring (art. 72) + serious-incident reporting (art. 73)
  - Track JTC 21 OJEU citations (key ENs expected from Q4 2026) → claim art. 40 presumption when available

2027-12-02 → 2028-08-02 (8 months)
  - Annex III high-risk regime live: maintain full conformity
  - First internal audit + management review (ISO 42001 cl. 9.2-3)
  - Annex I product-embedded AI: final conformity push

2028-08-02 onwards
  - Annex I product-safety high-risk: full obligations apply
  - Continuous compliance maintenance
  - Track Commission delegated/implementing acts (esp. arts. 6, 7, 41, 51, 52, 96)
```

### 3.3 Key Commission acts to track

Landed so far:

- **GPAI guidelines** (2025-07-18) — scope of provider obligations under Chapter V
- **Training-data-summary template** (2025-07-24) — operationalizes art. 53(1)(d)
- **Draft art. 73 serious-incident guidance + reporting template** (2025-09-26; consultation closed 2025-11-07)
- **Draft art. 6 high-risk classification guidelines** (2026-05-19)

Still pending:

- **Art. 6(7)** — final Commission guidelines on practical implementation of art. 6(1)/(2) classification
- **Art. 7** — delegated acts adding new use cases to Annex III
- **Art. 11(3)** — Commission implementing act for SME simplified Annex IV form
- **Art. 27(5)** — Commission template for FRIA notification
- **Art. 41** — common specifications where harmonised standards insufficient
- **Art. 51(3)** — delegated acts amending GPAI systemic-risk thresholds
- **Art. 52(4)** — Commission implementing act for systemic-risk GPAI notification
- **Art. 56** — Commission approval of Codes of Practice
- **Art. 71(4)** — implementing act for EU database structure + access
- **Art. 72(3)** — implementing act for PMM plan structure
- **Art. 73(7)** — implementing act for serious-incident reporting templates

The Navigator's `server/services/regulatoryService.ts` is well-positioned to track these via the EUR-Lex MCP server.

## 4. Compact summary (one-page reference)

```
═══ GPAI ═══
Standard GPAI:           art. 53(1)(a)–(d)
   (a) Annex XI tech doc
   (b) Annex XII downstream-provider info
   (c) Copyright policy
   (d) Training data summary
   FOSS carve-out: (a) and (b) only — except for systemic-risk GPAI

Systemic-risk GPAI:      art. 55(1)(a)–(d)
   (a) Model eval + adversarial testing
   (b) Systemic-risk assessment + mitigation
   (c) Serious-incident reporting to AI Office
   (d) Cybersecurity for model + infrastructure
   Trigger: 10²⁵ FLOPs cumulative training compute, OR Commission designation

═══ SANCTIONS ═══
Tier 1 (art. 5 prohibited):           €35M or 7% turnover
Tier 2 (most other obligations):      €15M or 3%
Tier 3 (false info to authorities):    €7.5M or 1%
GPAI (art. 101):                       €15M or 3%
SME cap:                               LOWER of fixed or %

═══ TIMELINE (post-Omnibus 2026) ═══
2025-02-02: art. 5 prohibitions + art. 4 literacy
2025-08-02: GPAI (Chapter V), governance, penalties (most)
2026-08-02: art. 50 transparency + GPAI enforcement (art. 101 fines)
2026-12-02: NCII/CSAM prohibition + end of art. 50(2) marking grace
2027-08-02: sandboxes operational; legacy GPAI compliance deadline
2027-12-02: ANNEX III HIGH-RISK (Chapter III, conformity, registration, PMM, incident reporting)
2028-08-02: Annex I product-safety high-risk

═══ TRANSITIONAL ═══
GPAI on market before 2025-08-02:                     comply by 2027-08-02
High-risk on market before the high-risk date:        obligations on substantial change
Public-authority high-risk placed before that date:   full conformity by 2030-12-31
```

## 5. Anti-patterns and pitfalls

1. **Assuming "we don't have a GPAI" without checking.** Many products integrate GPAI components (LLM API, foundation-model-based image generator). The downstream AI system may itself be high-risk. Both regimes apply in parallel — neither replaces the other.

2. **FOSS carve-out misread for systemic-risk GPAI.** Open-source release does **not** exempt systemic-risk GPAI from arts. 53(1)(a)(b). It exempts only standard GPAI.

3. **Compute-threshold complacency.** 10²⁵ FLOPs is the **presumption** trigger; the Commission can designate a model as systemic-risk **regardless** of compute via art. 51(1)(b). Don't rely solely on compute audit.

4. **Treating the Omnibus deferral as a reason to pause.** The high-risk deadline moved to 2027-12-02, but arts. 9–15 + QMS + Annex IV + conformity assessment consume that runway easily for organizations starting from zero. Meanwhile art. 50 (2026-08-02), the NCII/CSAM safeguards (2026-12-02), and GPAI enforcement (2026-08-02) arrive first.

5. **Misreading the 2028-08-02 date as "general extension."** It applies **only** to the Annex I product-safety pathway (art. 6(1)). Annex III (art. 6(2)) high-risk systems must be compliant by **2027-12-02**.

6. **Ignoring Commission delegated/implementing acts.** Several articles depend on Commission acts to be operative (e.g., FRIA template, PMM plan format, GPAI code of practice). Track them; non-compliance can result if the act lands and the organization missed it.

7. **Sanction calculations on parent vs subsidiary.** "Worldwide annual turnover" in art. 99 typically refers to the **undertaking** in the EU competition-law sense — group-level for affiliated entities. SMEs / startups must understand whether a parent group disqualifies them from the SME cap.

8. **Underestimating Code of Practice's role.** Voluntary, but adherence is the simplest path to demonstrate art. 53–55 compliance for GPAI providers. Non-adherence requires the provider to demonstrate compliance through alternative means — significantly more work.

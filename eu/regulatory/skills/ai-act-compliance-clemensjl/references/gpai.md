# General-purpose AI models — Chapter V

Basis: Regulation (EU) 2024/1689 Arts 51 to 56, Annexes XI, XII, XIII, as amended by Regulation (EU) 2026/1744 Art 1(21). Commission Guidelines on the scope of the obligations for providers of general-purpose AI models established by Regulation (EU) 2024/1689, **C(2025) 7719 final, 19 November 2025** (first published 18 July 2025) — non-binding. General-Purpose AI Code of Practice, published **10 July 2025**. Explanatory notice and template for the public summary of training content, published **24 July 2025**.

**Applicable since 2 August 2025** (Art 113 third para point (b)). Models placed on the market before that date must comply by **2 August 2027** (Art 111(3)).

Enforcement is centralised: the Commission may fine GPAI model providers up to **3 % of annual total worldwide turnover or EUR 15 000 000, whichever is higher** (Art 101(1)). Art 101 itself only applied from 2 August 2026.

## Who this binds — and who it does not

`general-purpose AI model` (Art 3(63)) is the model, not the product. Chapter V binds the **provider of the model**. A team that calls an API, prompts a model, builds retrieval around it and ships a product is the provider of an **AI system**, not of a model, and owes Art 50 and possibly Chapter III — not Art 53.

### Is the artefact a general-purpose AI model at all

Indicative criterion, Guidelines C(2025) 7719 final point 17: training compute **greater than 10^23 FLOP** *and* the model can generate language (as text or audio), text-to-image, or text-to-video. Point 18: 10^23 FLOP corresponds roughly to training a one-billion-parameter model on a large amount of data. The Commission treats the modality "text" as including code (footnote 3). Indicative, not statutory — the Art 3(63) definition governs.

### When a downstream modifier becomes the provider of the modified model

Guidelines C(2025) 7719 final, points 57 to 63. Not every modification does this. Point 59: a downstream modifier becomes the provider of the modified model **only if the modification leads to a significant change in the model's generality, capabilities, or systemic risk**.

Point 60 — the indicative criterion: the **training compute used for the modification is greater than a third of the training compute of the original model**.

Point 61 — where the modifier cannot know and cannot estimate the original model's training compute, the threshold is replaced:

| Original model | Substitute threshold |
|---|---|
| GPAI model **with systemic risk** | a third of the Art 51(2) presumption threshold, currently **10^25 / 3 FLOP** |
| Any other GPAI model | a third of the indicative GPAI criterion, currently **10^23 / 3 FLOP** |

The threshold is relative to the original model's compute deliberately, so that modifying small models is not disincentivised (point 63). Footnote 13: whether the original provider or a downstream actor is the modifier is a case-by-case assessment; who controls the model's weights is an important factor — relevant for fine-tuning via API.

Operationally: a LoRA adapter or a light instruction-tune on a few thousand examples is far below a third of a foundation model's training compute and does not make you a model provider. A substantial continued-pretraining run may. Record the estimate and the reasoning either way.

## Art 53 — obligations of all GPAI model providers

(a) **Technical documentation** of the model, including its training and testing process and evaluation results, kept up to date, containing at minimum the **Annex XI** information, to be provided on request to the AI Office and national competent authorities.

(b) **Downstream documentation**: information and documentation made available to providers of AI systems who intend to integrate the model, enabling them to understand capabilities and limitations and to comply with their own obligations, containing at minimum the **Annex XII** elements. Without prejudice to intellectual property and trade secrets.

(c) A **policy to comply with Union copyright law**, in particular to identify and comply — including through state-of-the-art technologies — with a **reservation of rights expressed pursuant to Article 4(3) of Directive (EU) 2019/790**. That is the text-and-data-mining opt-out: Art 4(1) of the DSM Directive permits TDM reproductions of lawfully accessible works, and Art 4(3) lets rightsholders reserve that use expressly and appropriately, in machine-readable means for content made publicly available online. The AI Act obligation is to have a policy and to actually detect and honour those reservations.

(d) A **sufficiently detailed summary about the content used for training**, made publicly available, according to the template provided by the AI Office. Template and explanatory notice published 24 July 2025.

Art 53(2) — the open-source exemption: (a) and (b) do not apply to providers of models released under a free and open-source licence allowing access, use, modification and distribution, and whose parameters including weights, information on model architecture and information on model usage are made publicly available. **(c) and (d) still apply.** The exemption does not apply at all to models with systemic risk.

Art 53(3): cooperation with the Commission and national competent authorities.

Art 53(4): providers may rely on codes of practice under Art 56 to demonstrate compliance **until a harmonised standard is published**. Compliance with European harmonised standards grants **presumption of conformity** to the extent those standards cover the obligations. Providers who neither adhere to an approved code nor comply with a harmonised standard must demonstrate **alternative adequate means of compliance** for assessment by the Commission.

Art 53(5) and (6): Commission delegated acts may detail measurement and calculation methodologies for Annex XI points 2(d) and (e), and may amend Annexes XI and XII.

Art 53(7): information obtained, including trade secrets, is subject to the Art 78 confidentiality rules.

## Annex XI — technical documentation for GPAI models

Section 1, all providers, "as appropriate to the size and risk profile of the model":

1. General description: (a) tasks the model is intended to perform and the type and nature of AI systems it can be integrated into; (b) acceptable use policies; (c) date of release and methods of distribution; (d) architecture and **number of parameters**; (e) modality and format of inputs and outputs; (f) the licence.
2. Detailed description: (a) technical means required for integration into AI systems; (b) design specifications of the model and training process, training methodologies and techniques, key design choices with rationale and assumptions, what the model optimises for and the relevance of parameters; (c) **information on the data used for training, testing and validation** — type and provenance, curation methodologies such as cleaning and filtering, number of data points, scope and main characteristics, how data was obtained and selected, measures to detect unsuitability of data sources, and methods to detect identifiable biases; (d) **computational resources used to train the model** (e.g. number of floating point operations), training time and other relevant details; (e) known or estimated **energy consumption** — which may be derived from computational resources where unknown.

Section 2, additional for systemic-risk models: detailed description of evaluation strategies including results, criteria, metrics and methodology for identifying limitations; where applicable, internal and external adversarial testing (red teaming), model adaptations including alignment and fine-tuning; where applicable, detailed system architecture.

Annex XII (downstream documentation) overlaps with Annex XI Section 1 but is the version that goes to integrators rather than to regulators.

## Art 51 and 52 — systemic risk

Art 51(1): a model is classified as having systemic risk if it (a) has **high impact capabilities** evaluated on appropriate technical tools and methodologies including indicators and benchmarks, or (b) is designated by Commission decision, ex officio or after a qualified alert from the scientific panel, as having equivalent capabilities or impact under the Annex XIII criteria.

Art 51(2): a model is **presumed** to have high impact capabilities when the cumulative amount of computation used for its training, measured in floating point operations, is **greater than 10^25 FLOP**. Art 51(3) empowers the Commission to amend the thresholds and supplement benchmarks by delegated act; as at 2026-08-05 the 10^25 figure stands. [[UNVERIFIED: whether a delegated act amending Art 51(2) was adopted before 2026-08-05]]

Art 52: a provider meeting Art 51(1)(a) must **notify the Commission without delay and within two weeks**. It may argue in the notification that, exceptionally, the model does not present systemic risk despite the threshold. The Commission may reject the arguments, may designate ex officio, and publishes a list of GPAI models with systemic risk. Reassessment may be requested at the earliest six months after designation.

## Art 55 — obligations for systemic-risk models

In addition to Arts 53 and 54:

(a) **model evaluation** in accordance with standardised protocols and tools reflecting the state of the art, including conducting and documenting **adversarial testing** to identify and mitigate systemic risks;
(b) **assess and mitigate** possible systemic risks at Union level, including their sources;
(c) keep track of, document and **report serious incidents** and possible corrective measures to the AI Office without undue delay and, as appropriate, to national competent authorities;
(d) ensure an adequate level of **cybersecurity** for the model and its physical infrastructure.

Art 55(2) mirrors Art 53(4): codes of practice until a harmonised standard; harmonised standards give presumption of conformity; otherwise demonstrate alternative adequate means.

## Art 54 — authorised representative

Providers established in third countries must, **prior to placing a GPAI model on the Union market**, appoint an authorised representative established in the Union by written mandate. The representative verifies that the Annex XI documentation exists and that Art 53 and, where applicable, Art 55 obligations have been met; keeps a copy of the Annex XI documentation at the disposal of the AI Office and national competent authorities for **10 years** after placing on the market; provides information on reasoned request; and cooperates. It must terminate the mandate if it has reason to consider the provider is acting contrary to its obligations, and inform the AI Office.

Art 54(6): the obligation does not apply to open-source models meeting the same conditions as Art 53(2), unless they present systemic risks.

## The GPAI Code of Practice

Published **10 July 2025**, developed by 13 independent experts with input from over 1 000 stakeholders. Three chapters: **Transparency** (with a Model Documentation Form), **Copyright**, and **Safety and Security** (systemic-risk models only). The Commission and the AI Board confirmed it as an adequate voluntary tool. Signatories include Amazon, Anthropic, Google, IBM, Microsoft, Mistral AI, Cohere, OpenAI, Aleph Alpha, Black Forest Labs and ServiceNow; xAI signed only the Safety and Security chapter.

Legal effect, and the correction the omnibus makes explicit: **signing does not confer a presumption of conformity**. Recital 41 of Reg (EU) 2026/1744 states that the codes of practice referred to in Art 50(7) and Art 56(6) "have limited legal effect, and in particular do not grant a presumption of conformity", which is why the empowerment to approve them by implementing act was removed. What signing does is give a recognised route to **demonstrate** compliance under Art 53(4) and Art 55(2) until a harmonised standard exists. Art 56(6) as replaced by Reg (EU) 2026/1744 Art 1(21): the Commission, taking utmost account of the Board's opinion, assesses whether the codes cover the Art 53 and 55 obligations, monitors achievement of their objectives, and **publishes its assessment of adequacy**.

## The training-content summary

Template and explanatory notice published by the AI Office on **24 July 2025**, providing a common minimal baseline for the summary required by Art 53(1)(d). The summary must be **publicly available**, not merely available on request. It is the one Chapter V artefact that a downstream integrator can actually read, and the one place where copyright disputes about training data start.

Practical consequence for a team fine-tuning an open-weights model into a distinct model it then distributes: the Art 53(2) open-source exemption will not save you from Art 53(1)(c) and (d). You still need a copyright policy honouring Art 4(3) DSM reservations, and a public training-content summary on the AI Office template.

## Checkpoints

- [ ] Determined whether the company is a provider of a **model** or only of a **system** — and documented the reasoning
- [ ] Training compute of any model we built compared against the 10^23 FLOP indicative criterion in Guidelines point 17
- [ ] For any modification of an upstream model: modification compute compared against a third of the original model's training compute, or the substitute thresholds in Guidelines point 61, with the estimate recorded
- [ ] Annex XI documentation drafted, including training compute in FLOP and energy consumption
- [ ] Annex XII documentation prepared for downstream integrators
- [ ] Copyright policy in place, with a technical mechanism that actually detects and honours Art 4(3) DSM reservations
- [ ] Public training-content summary drafted on the AI Office template of 24 July 2025 and actually published
- [ ] Open-source claim tested against all conditions of Art 53(2), with (c) and (d) still applied
- [ ] Training compute compared against the 10^25 FLOP presumption in Art 51(2); if exceeded, Art 52(1) notification within two weeks
- [ ] For systemic-risk models: evaluation and adversarial testing, risk mitigation, incident reporting to the AI Office, cybersecurity
- [ ] Authorised representative appointed before market placement if the provider is outside the Union
- [ ] Code of Practice signature decision recorded, with the understanding that it demonstrates compliance but confers no presumption of conformity
- [ ] Models placed before 2 August 2025 tracked against the 2 August 2027 deadline

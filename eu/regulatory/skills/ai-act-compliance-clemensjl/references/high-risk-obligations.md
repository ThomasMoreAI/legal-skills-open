# Provider obligations for high-risk AI systems

Basis: Regulation (EU) 2024/1689 Chapter III Sections 2, 3 and 5, Annexes IV, V, VI, VII, VIII, as amended by Regulation (EU) 2026/1744. Applicable from **2 December 2027** (Annex III) and **2 August 2028** (Annex I) — Art 113 third para point (c) as amended.

Art 16 is the index of provider obligations. Everything below hangs off it.

## Art 9 — Risk management system

A continuous iterative process across the entire lifecycle, planned, documented, systematically reviewed and updated. Four steps (Art 9(2)):

(a) identify and analyse known and reasonably foreseeable risks to health, safety or fundamental rights from use in accordance with the intended purpose;
(b) estimate and evaluate risks arising from intended use **and reasonably foreseeable misuse**;
(c) evaluate other risks from post-market monitoring data (Art 72);
(d) adopt appropriate and targeted risk management measures.

Constraints:

- Art 9(3): only risks that can reasonably be mitigated or eliminated through development, design, or adequate technical information.
- Art 9(5): residual risk per hazard and overall must be judged acceptable; the hierarchy is elimination or reduction by design first, then mitigation and control measures, then information under Art 13 and, where appropriate, training for deployers.
- Art 9(6) to (8): testing against **prior defined metrics and probabilistic thresholds** appropriate to the intended purpose, at any time during development and in any event before placing on the market. Art 9(7) allows real-world testing under Art 60.
- Art 9(9): explicit consideration of adverse impact on **persons under 18** and, as appropriate, other vulnerable groups.
- Art 9(10): where other Union law imposes internal risk management, Art 9 may be part of or combined with it.

## Art 10 — Data and data governance

Art 10(1) as amended by Reg (EU) 2026/1744 Art 1(9)(a): systems using techniques involving the training of AI models with data must be developed on the basis of training, validation and testing data sets meeting the criteria in Art 10(2), (3), (4) and in **Art 4a(1)** whenever such sets are used.

Art 10(2) requires governance and management practices covering, among others, design choices, data collection processes and origin, preparation operations (annotation, labelling, cleaning, updating, enrichment, aggregation), assumptions about what the data is supposed to measure and represent, assessment of availability, quantity and suitability, examination for possible biases, measures to **detect, prevent and mitigate** such biases, and identification of relevant data gaps.

Art 10(3): training, validation and testing sets must be relevant, sufficiently representative, and to the best extent possible free of errors and complete in view of the intended purpose. Art 10(4): account of the characteristics of the specific geographical, contextual, behavioural or functional setting.

Art 10(5) was **deleted** by Reg (EU) 2026/1744 Art 1(9)(b). The legal basis for processing special categories of personal data for bias detection and correction now lives in **Art 4a**, with six cumulative conditions in Art 4a(1)(a) to (f): no other data would do, technical limits on re-use plus state-of-the-art security and pseudonymisation, strict access controls and documentation, no transmission to other parties, deletion once bias is corrected or retention ends, and a record in the GDPR Art 30 records explaining why the processing was strictly necessary. Art 4a(2) extends the basis to deployers of high-risk systems and to providers and deployers of other AI systems and models, without creating any obligation to do bias detection.

Art 10(6) as amended: for high-risk systems **not** using training techniques, Art 10(2), (3), (4) and Art 4a(1) apply only to the testing data sets.

## Art 11 and Annex IV — Technical documentation

Drawn up **before** the system is placed on the market or put into service, and kept up to date. Art 11(1), second subparagraph, as replaced by Reg (EU) 2026/1744 Art 1(10): it must contain at minimum the Annex IV elements; **SMEs, including start-ups, and SMCs may provide them in a simplified manner**, using a simplified form the Commission is to establish, which notified bodies must accept.

Annex IV, nine headings:

1. General description — intended purpose, provider name, version; interaction with hardware or other software including other AI systems; software or firmware versions and update requirements; all forms in which it is placed on the market (embedded, download, API); intended hardware; photographs or illustrations where a component of products; basic description of the deployer user interface; instructions for use.
2. Detailed description of elements and development process — methods and steps including recourse to pre-trained systems or third-party tools and how they were used, integrated or modified; design specifications, general logic and algorithms, key design choices with rationale and assumptions including as to the persons or groups the system is intended for, main classification choices, what it optimises for, relevance of parameters, expected output and output quality, trade-offs; system architecture and computational resources; data requirements as datasheets — training methodologies and techniques, training sets, provenance, scope, main characteristics, how data was obtained and selected, labelling procedures, data cleaning; assessment of human oversight measures under Art 14 including technical measures to facilitate interpretation of outputs; pre-determined changes and how continuous compliance is ensured; validation and testing procedures, metrics for accuracy, robustness and other requirements, potentially discriminatory impacts, **test logs and test reports dated and signed by the responsible persons**; cybersecurity measures.
3. Monitoring, functioning and control — capabilities and limitations in performance, including degrees of accuracy for specific persons or groups and the overall expected level of accuracy; foreseeable unintended outcomes and sources of risk to health, safety, fundamental rights and discrimination; human oversight measures; input data specifications.
4. Appropriateness of the performance metrics.
5. Detailed description of the risk management system under Art 9.
6. Description of relevant changes made through the lifecycle.
7. List of harmonised standards applied in full or in part, with OJ references; where none applied, a detailed description of the solutions adopted.
8. A **copy of the EU declaration of conformity** under Art 47.
9. Detailed description of the post-market performance evaluation system under Art 72, including the post-market monitoring plan.

Retention: 10 years after placing on the market or putting into service (Art 18).

## Art 12 — Record-keeping

Art 12(1): the system must **technically allow** automatic recording of events (logs) over its lifetime.

Art 12(2): logging capabilities must enable recording of events relevant for (a) identifying situations that may result in the system presenting a risk under Art 79(1) or in a substantial modification; (b) facilitating post-market monitoring under Art 72; (c) monitoring operation under Art 26(5).

Art 12(3), minimum for Annex III point 1(a) systems (remote biometric identification): period of each use with start and end date and time; the reference database against which input data was checked; the input data for which the search led to a match; identification of the natural persons involved in verifying the results under Art 14(5).

Art 19: the provider keeps logs automatically generated by its high-risk systems, to the extent under its control, for a period appropriate to the intended purpose, of **at least six months**, unless other Union or national law — in particular data protection law — provides otherwise.

## Art 13 — Transparency and instructions for use

The system must be sufficiently transparent for deployers to interpret its output and use it appropriately. Instructions for use, in an appropriate digital format, concise, complete, correct, clear, relevant, accessible and comprehensible, containing at least (Art 13(3)):

(a) identity and contact details of the provider and, where applicable, its authorised representative;
(b) characteristics, capabilities and limitations of performance, including: (i) intended purpose; (ii) the level of **accuracy including its metrics**, robustness and cybersecurity under Art 15 against which it was tested and validated and which can be expected, and known and foreseeable circumstances affecting that level; (iii) known or foreseeable circumstances under intended use or reasonably foreseeable misuse which may lead to risks under Art 9(2); (iv) where applicable, technical capabilities to provide information relevant to explain the output; (v) when appropriate, performance regarding specific persons or groups; (vi) when appropriate, input data specifications or other information about the training, validation and testing sets; (vii) where applicable, information to enable deployers to interpret and use the output;
(c) pre-determined changes to the system and its performance;
(d) the human oversight measures under Art 14, including technical measures to facilitate interpretation of outputs;
(e) computational and hardware resources needed, expected lifetime, and necessary maintenance and care measures including frequency, including software updates;
(f) where relevant, the mechanisms allowing deployers to collect, store and interpret the logs under Art 12.

## Art 14 — Human oversight

Designed in, including appropriate human-machine interface tools, so the system can be effectively overseen by natural persons while in use (Art 14(1)). Oversight must be commensurate with risks, level of autonomy and context (Art 14(3)) and delivered through measures built into the system by the provider, measures identified for the deployer to implement, or both.

Art 14(4) — the oversight person must be enabled, as appropriate and proportionate, to:

(a) properly understand the relevant capacities and limitations and monitor operation, including detecting and addressing anomalies, dysfunctions and unexpected performance;
(b) remain aware of the tendency to automatically rely or over-rely on the output (**automation bias**), in particular where the system informs decisions taken by natural persons;
(c) correctly interpret the output, taking into account available interpretation tools and methods;
(d) decide, in any particular situation, not to use the system or to disregard, override or reverse the output;
(e) intervene or interrupt the system through a **stop button or similar procedure that allows the system to come to a halt in a safe state**.

Art 14(5): for Annex III point 1(a) systems, no action or decision may be taken on the basis of the identification unless separately verified and confirmed by **at least two natural persons** with the necessary competence, training and authority — with a proportionality carve-out for law enforcement, migration, border control and asylum where Union or national law so provides.

## Art 15 — Accuracy, robustness, cybersecurity

Appropriate levels, performing consistently throughout the lifecycle. Accuracy levels and the relevant metrics must be **declared in the instructions for use** (Art 15(3)). Resilience to errors, faults and inconsistencies, addressed by technical and organisational measures, possibly technical redundancy, backup or fail-safe plans (Art 15(4)). Systems that continue to learn after placing on the market must eliminate or reduce as far as possible the risk of biased outputs influencing future inputs (**feedback loops**), with mitigation measures.

Art 15(5): resilience against attempts by unauthorised third parties to alter use, outputs or performance. Technical solutions must address, where appropriate, **data poisoning**, **model poisoning** of pre-trained components, **adversarial examples or model evasion**, confidentiality attacks and model flaws.

Art 42(3), inserted by Reg (EU) 2026/1744 Art 1(18): where a high-risk system falls within the scope of Regulation (EU) 2024/2847 (Cyber Resilience Act) and the conditions in its Art 12(1) are met, the system is **deemed to comply** with Art 15 cybersecurity requirements.

## Art 17 — Quality management system

Written policies, procedures and instructions covering at minimum: a regulatory compliance strategy including conformity assessment and management of modifications; design, design control and design verification techniques; development, quality control and quality assurance techniques; examination, test and validation procedures and their frequency; technical specifications including standards, and where harmonised standards are not applied in full, the means used instead; data management systems and procedures; the risk management system under Art 9; post-market monitoring under Art 72; incident reporting under Art 73; communication with authorities and notified bodies; record-keeping; resource management including security of supply; and an accountability framework.

Art 17(2) as replaced by Reg (EU) 2026/1744 Art 1(11): implementation must be **proportionate to the size of the provider's organisation**, in particular for SMEs including start-ups and for SMCs; providers must in any event respect the degree of rigour and level of protection required.

Art 63(1) as amended: SMEs including start-ups may comply with certain QMS elements in a simplified manner **provided they have no partner or linked enterprises** within the meaning of Recommendation 2003/361/EC. The Commission is to develop guidelines on which elements.

Art 17(3): where other Union law requires quality management, Art 17 may be integrated.

## Art 43 — Conformity assessment

| System | Procedure |
|---|---|
| Annex III **point 1** (biometrics), where harmonised standards or common specifications have been applied | Provider chooses: internal control (Annex VI) **or** QMS and technical documentation assessment with a notified body (Annex VII) — Art 43(1) |
| Annex III **point 1**, where no harmonised standards or common specifications exist, or the provider did not apply them or applied only part | **Annex VII, notified body** — Art 43(1), second subpara |
| Annex III **points 2 to 8** | Internal control, Annex VI, **no notified body** — Art 43(2) |
| Annex I **Section A** products | The sectoral conformity assessment procedure, with the Section 2 requirements forming part of it; Art 17 QMS assessment also undertaken; points 3, 4.3, 4.4, 4.5, fifth paragraph of 4.6 and point 5 of Annex VII apply — Art 43(3) as replaced by Reg (EU) 2026/1744 Art 1(19) |

Art 43(3) as amended adds two things worth knowing: notified bodies notified under Annex I Section A legislation must apply for designation under the AI Act **by 28 January 2028**; and classification as a high-risk AI system under Art 6(1) does **not** force a manufacturer into third-party assessment if the sectoral legislation does not require it — the self-assessment route remains available where harmonised standards or common specifications covering all Section 2 requirements have been applied.

Art 43(4): a substantially modified system undergoes a new conformity assessment. For systems that continue to learn, changes pre-determined in the initial technical documentation are not substantial modifications.

As at 2026-08-05 **no harmonised standard under the AI Act has been cited in the Official Journal**, which pushes Annex III point 1 systems into the Annex VII notified-body route by default. Track this before assuming Annex VI is available. [[UNVERIFIED: OJ citations of AI Act harmonised standards between the last check and 2026-08-05]]

## Art 47 — EU declaration of conformity

Written, **machine readable**, physical or electronically signed, one per high-risk system, kept at the disposal of national competent authorities for **10 years**. States that the system meets the Section 2 requirements, contains the Annex V information, translated into a language easily understood by the authorities of the Member States where it is placed on the market. Where other Union harmonisation legislation also requires a declaration, a **single** declaration covering all applicable law is drawn up (Art 47(3)). Drawing it up means assuming responsibility for compliance (Art 47(4)).

## Art 48 — CE marking

General principles of Art 30 of Regulation (EC) No 765/2008. For **digitally provided systems**, a digital CE marking may be used only if easily accessible via the interface from which the system is accessed, or via an easily accessible machine-readable code or other electronic means (Art 48(2)). Affixed visibly, legibly and indelibly, or on packaging or accompanying documentation where that is not possible. Where a notified body was involved, followed by that body's identification number, which must also appear in promotional material mentioning CE conformity (Art 48(4)).

## Art 49 — Registration in the EU database (Art 71)

| Who | What | When |
|---|---|---|
| Provider or authorised representative | Register themselves and the system, for Annex III systems **except point 2** | Before placing on the market or putting into service — Art 49(1) |
| Provider or authorised representative | Register themselves and the system where the provider concluded under Art 6(3) that it is **not** high-risk | Before placing on the market or putting into service — Art 49(2) |
| Deployers that are public authorities, Union institutions, bodies, offices or agencies, or persons acting on their behalf | Register themselves, select the system, register its use | Before putting into service or using — Art 49(3) |

Art 49(4): for Annex III points 1, 6 and 7 in law enforcement, migration, asylum and border control, registration goes into a **secure non-public section** with a reduced data set. Art 49(5): Annex III point 2 systems are registered at **national** level.

Reg (EU) 2026/1744 Art 1(42) deleted points 7 and 9 of Annex VIII Section B, reducing the registration data set. Check the current Annex VIII text before drafting a registration entry.

## Art 72 and 73 — After placing on the market

Art 72: a post-market monitoring system proportionate to the nature of the AI technologies and the risks, actively and systematically collecting, documenting and analysing relevant data on performance throughout the lifetime, based on a **post-market monitoring plan** that forms part of the Annex IV technical documentation. Art 72(3) as amended by Reg (EU) 2026/1744 Art 1(30): the Commission is to adopt guidance including a template by **2 September 2027** — no longer an implementing act, and the template is voluntary.

Art 73: providers report **serious incidents** to the market surveillance authority of the Member State where the incident occurred, immediately after establishing a causal link or reasonable likelihood of one, and in any event not later than **15 days** after becoming aware. Shorter deadlines: **2 days** for widespread infringement or a serious incident under Art 3(49)(b) (death of a person), and **10 days** in the case of death. Art 75(1a), inserted by the omnibus: where the AI Office is exclusively competent under Art 75(1), providers report to the AI Office instead.

## Checkpoints

- [ ] Art 9 risk file exists, covers reasonably foreseeable misuse and under-18 impact, and states residual risk acceptance
- [ ] Art 10 data governance documented, with bias examination and mitigation; special-category processing, if any, mapped to the six Art 4a(1) conditions
- [ ] Annex IV documentation complete against all nine headings, with dated and signed test reports
- [ ] SME or SMC status recorded if the simplified Art 11(1) form is used
- [ ] Art 12 logging capability implemented and mapped to Art 12(2)(a) to (c); Annex III point 1(a) minima met if applicable
- [ ] Instructions for use cover all of Art 13(3)(a) to (f), including declared accuracy metrics
- [ ] Human oversight design covers Art 14(4)(a) to (e), with a real stop mechanism and an automation-bias countermeasure
- [ ] Art 15 addresses feedback loops and the five named attack classes; Cyber Resilience Act route under Art 42(3) considered
- [ ] Art 17 QMS documented or mapped onto an existing QMS; simplified route only if no partner or linked enterprises
- [ ] Correct Art 43 route selected, with harmonised-standard availability verified rather than assumed
- [ ] EU declaration of conformity drafted per Annex V, machine readable, 10-year retention arranged
- [ ] CE marking placed, including the digital-CE conditions for software-only systems
- [ ] Registration actions listed per Art 49(1), (2), (3), against the current Annex VIII
- [ ] Post-market monitoring plan drafted and included in the technical documentation
- [ ] Serious incident process with the 15-day, 10-day and 2-day deadlines, and the correct recipient under Art 73 or Art 75(1a)

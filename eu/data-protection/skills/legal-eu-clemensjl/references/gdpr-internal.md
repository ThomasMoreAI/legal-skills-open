# GDPR internal obligations

Status as at 2026-08-05.

Regulation (EU) 2016/679, Arts 27, 28, 30, 33 to 37. None of these produce a public text. They produce records, contracts and procedures — and they are what a supervisory authority asks for first. A privacy notice with no records of processing behind it is a description of a system nobody has mapped.

Nothing in the Digital Omnibus proposal is in force. In particular, Art 33 is still **72 hours** on a risk threshold; the proposed 96-hour deadline and the Art 33a single entry point are proposal text only.

## Art 27 — representative in the Union

**Art 27(1)**: where **Art 3(2)** applies — a controller or processor not established in the Union that offers goods or services to data subjects in the Union or monitors their behaviour in the Union — the controller or processor **shall designate in writing a representative in the Union**.

**Art 27(2)** exemptions:

- (a) processing that is **occasional**, does not include on a large scale processing of Art 9(1) special categories or Art 10 criminal data, and is **unlikely to result in a risk** to the rights and freedoms of natural persons, taking into account the nature, context, scope and purposes; or
- (b) a public authority or body.

A live SaaS product with EU users is not "occasional". The exemption almost never applies to a running service.

**Art 27(3)**: the representative must be established **in one of the member states where the data subjects are** whose data are processed in relation to the offering of goods or services or whose behaviour is monitored. **Art 27(4)**: the representative is mandated to be addressed, in addition to or instead of the controller or processor, by supervisory authorities and data subjects on all issues related to processing. **Art 27(5)**: designating a representative is without prejudice to legal actions against the controller or processor themselves.

The representative's identity and contact details go into the privacy notice (Art 13(1)(a), Art 14(1)(a)).

**Three different EU representatives exist and they are not interchangeable.** Art 27 GDPR (data protection), **Art 13 DSA** (legal representative for non-EU intermediary services), and **Art 16 GPSR / Art 4 Regulation (EU) 2019/1020** (responsible person for products). One person may hold more than one role only if separately appointed for each. Never satisfy one duty by pointing at another.

## Art 28 — processor contracts

**Art 28(1)**: the controller shall use only processors providing **sufficient guarantees** to implement appropriate technical and organisational measures. This is a selection duty, assessed and documented before onboarding, not a clause.

**Art 28(2)**: no sub-processor without prior specific or general written authorisation. Under a general authorisation the processor must inform the controller of intended changes, giving the controller the opportunity to object.

**Art 28(3)** — the contract or other legal act must be binding, in writing (including electronic form, Art 28(9)), set out the subject matter and duration of the processing, the nature and purpose, the type of personal data and categories of data subjects, and the obligations and rights of the controller, and must stipulate that the processor:

- (a) processes personal data **only on documented instructions** from the controller, including as regards transfers, unless required by Union or member state law, in which case it informs the controller before processing unless that law prohibits it
- (b) ensures that persons authorised to process have committed themselves to **confidentiality** or are under an appropriate statutory obligation
- (c) takes all measures required under **Art 32** (security of processing)
- (d) respects the Art 28(2) and 28(4) conditions for engaging sub-processors
- (e) assists the controller, by appropriate technical and organisational measures, insofar as possible, in fulfilling the obligation to respond to **data subject rights requests** under Chapter III
- (f) assists the controller in ensuring compliance with **Arts 32 to 36** — security, breach notification, breach communication, DPIA and prior consultation — taking into account the nature of processing and the information available
- (g) at the controller's choice, **deletes or returns** all personal data after the end of the provision of services, and deletes existing copies unless Union or member state law requires storage
- (h) makes available to the controller all information necessary to demonstrate compliance with Art 28, and **allows for and contributes to audits**, including inspections, conducted by the controller or another auditor mandated by the controller

**Art 28(4)**: where the processor engages a sub-processor, the **same data protection obligations** must be imposed by contract, and the initial processor **remains fully liable** to the controller for the sub-processor's performance.

**Art 28(7)**: the Commission may lay down standard contractual clauses for Arts 28(3) and (4). It did: **Commission Implementing Decision (EU) 2021/915 of 04.06.2021**. These are the intra-EEA controller-processor clauses and are distinct from the **transfer** SCCs in Implementing Decision (EU) 2021/914. Do not use one where the other is needed; a transfer to a third country needs the transfer SCCs, and an EEA-internal processor relationship needs an Art 28(3)-compliant contract. [[UNVERIFIED: whether Implementing Decision (EU) 2021/915 has been amended or supplemented since — check the Commission's data protection pages before citing a version]]

Practical test: for every vendor that touches personal data, there must be a signed document containing all eight letters. A vendor's "DPA" that omits (g) deletion or (h) audit is incomplete.

## Art 30 — records of processing activities

**Art 30(1)** — each controller and, where applicable, its representative maintains a record containing:

- (a) name and contact details of the controller and, where applicable, the joint controller, the controller's representative and the data protection officer
- (b) the purposes of the processing
- (c) a description of the categories of data subjects and of the categories of personal data
- (d) the categories of recipients to whom the data have been or will be disclosed, including recipients in third countries or international organisations
- (e) where applicable, transfers to a third country or international organisation, including its identification, and for Art 49(1) second subparagraph transfers, the documentation of suitable safeguards
- (f) **where possible**, the envisaged time limits for erasure of the different categories of data
- (g) **where possible**, a general description of the technical and organisational security measures under Art 32(1)

**Art 30(2)** — each processor and, where applicable, its representative maintains a record of all categories of processing carried out on behalf of a controller: (a) the name and contact details of the processor or processors, of each controller on behalf of which it acts, and of the representatives and DPO; (b) the categories of processing carried out on behalf of each controller; (c) transfers to a third country or international organisation, with identification and, for Art 49(1) second subparagraph transfers, documentation of suitable safeguards; (d) where possible, a general description of the technical and organisational security measures.

**Art 30(3)**: in writing, including in electronic form. **Art 30(4)**: made available to the supervisory authority on request.

**Art 30(5)** — the exemption, and its conditions are cumulative in a way that defeats it in practice: the obligation does not apply to an enterprise or organisation employing **fewer than 250 persons**, **unless** the processing (i) is likely to result in a **risk** to the rights and freedoms of data subjects, (ii) is **not occasional**, or (iii) includes Art 9(1) special categories or Art 10 criminal conviction data.

Read it as written: those are alternatives, not cumulative requirements. Any regular processing — a customer database, an employee file, a newsletter list — is "not occasional" and the exemption is gone. A small company almost never qualifies.

[[UNVERIFIED: a legislative file in the Commission's Omnibus IV package is reported to revisit Art 30(5). Nothing is in force; check its status before relying on any widened exemption.]]

## Arts 33 and 34 — personal data breaches

**Art 33(1)**: in the case of a personal data breach, the controller notifies the competent supervisory authority **without undue delay and, where feasible, not later than 72 hours after having become aware of it**, unless the breach is **unlikely to result in a risk** to the rights and freedoms of natural persons. Where the notification is later than 72 hours, it must be accompanied by reasons for the delay.

**Art 33(2)**: the processor notifies the controller **without undue delay** after becoming aware. No 72-hour figure applies to the processor — it is immediate in substance.

**Art 33(3)** minimum content: (a) the nature of the breach, including where possible the categories and approximate number of data subjects and of personal data records concerned; (b) the name and contact details of the DPO or other contact point; (c) the likely consequences; (d) the measures taken or proposed, including where appropriate measures to mitigate possible adverse effects. **Art 33(4)**: information may be provided in phases where it is not possible to provide it all at once.

**Art 33(5)**: the controller **documents any personal data breach**, comprising the facts, its effects and the remedial action taken. This applies to **every** breach, including those not notified. The documentation must enable the supervisory authority to verify compliance.

**Art 34(1)**: where the breach is likely to result in a **high risk** to the rights and freedoms of natural persons, the controller communicates it to the **data subject** without undue delay. **Art 34(2)**: in clear and plain language, describing the nature of the breach, and containing at least the Art 33(3)(b), (c) and (d) information.

**Art 34(3)** — communication to data subjects is not required where:

- (a) the controller had implemented appropriate technical and organisational protection measures and applied them to the affected data, **in particular measures rendering the data unintelligible to any person not authorised to access it, such as encryption**
- (b) the controller has taken subsequent measures ensuring that the high risk is **no longer likely to materialise**
- (c) it would involve **disproportionate effort** — in which case there must instead be a public communication or similar measure informing the data subjects in an **equally effective manner**

**Art 34(4)**: the supervisory authority may require the communication or decide that one of the 34(3) conditions is met.

The 72-hour clock starts on **awareness**, not on completing the investigation. A breach procedure that starts with "once we understand what happened" already misses it. The procedure must name who declares awareness, who drafts the notification, which authority receives it, and where the Art 33(5) register lives.

## Art 35 — data protection impact assessment

**Art 35(1)**: where a type of processing, **in particular using new technologies**, is likely to result in a **high risk** to the rights and freedoms of natural persons, the controller carries out a DPIA **prior to the processing**.

**Art 35(3)** — required in particular for:

- (a) a **systematic and extensive evaluation** of personal aspects based on automated processing, including profiling, on which decisions are based that produce legal effects or similarly significantly affect the natural person
- (b) processing **on a large scale** of Art 9(1) special categories or Art 10 criminal data
- (c) **systematic monitoring of a publicly accessible area on a large scale**

**Art 35(4)**: each supervisory authority publishes a list of processing operations requiring a DPIA. These national lists are binding in the member state and they differ — a national-layer item.

**Art 35(7)** minimum content: (a) a systematic description of the envisaged processing operations and purposes, including where applicable the legitimate interest pursued; (b) an assessment of the **necessity and proportionality** of the processing in relation to the purposes; (c) an assessment of the **risks** to the rights and freedoms of data subjects; (d) the **measures envisaged to address the risks**, including safeguards, security measures and mechanisms to ensure the protection of personal data and demonstrate compliance.

Art 35(9): where appropriate, seek the views of data subjects or their representatives. Art 35(11): review where there is a change of the risk.

**Art 36(1)**: where the DPIA indicates that the processing **would result in a high risk in the absence of measures taken by the controller to mitigate it**, the controller must consult the supervisory authority **before** processing.

An AI feature that scores, ranks or profiles users almost always hits Art 35(3)(a). Doing the AI Act analysis without the DPIA leaves the more likely obligation unaddressed.

## Art 37 — data protection officer

**Art 37(1)** — designation is mandatory where:

- (a) the processing is carried out by a **public authority or body**, except for courts acting in their judicial capacity
- (b) the **core activities** of the controller or processor consist of processing operations which, by virtue of their nature, scope or purposes, require **regular and systematic monitoring of data subjects on a large scale**
- (c) the **core activities** consist of processing **on a large scale** of Art 9 special categories or Art 10 criminal data

**There is no headcount threshold in Art 37(1).** **Art 37(4)**: in cases other than those in 37(1), the controller, processor or their associations may — and where required by Union or member state law **shall** — designate a DPO. National headcount rules, such as the German twenty-persons rule, live here. They are national law, not the GDPR.

"Core activities" means the operations essential to achieving the controller's objectives, not ancillary support. A shop that runs analytics is not thereby doing regular and systematic monitoring as a core activity; an ad-tech company is.

Art 38 sets the DPO's position — involved in all data protection matters, no instructions on the exercise of the tasks, no dismissal or penalty for performing them, reporting to the highest management level. Art 39 sets the tasks. A DPO with a conflicting operational role (head of IT, head of marketing) is a recurring finding.

## Register — minimum working structure

```
Processing: [[NAME]]
Controller / joint controller / processor role: [[…]]
Purpose: [[…]]
Legal basis (Art 6(1)): [[…]]  Special category basis (Art 9(2)): [[…]]
Categories of data subjects: [[…]]
Categories of personal data: [[…]]
Recipients (named): [[…]]
Third-country transfers: [[recipient / country / Chapter V basis / TIA reference]]
Retention or criteria: [[…]]
Security measures (Art 32): [[…]]
Processor contract: [[reference, date, Art 28(3) letters verified]]
DPIA required (Art 35(3) or national list): [[yes/no + reference]]
Owner: [[…]]  Last reviewed: [[DATE]]
```

## Checkpoints

- [ ] Art 3(2) assessed; where it applies, an Art 27 representative is designated in writing in a member state where the data subjects are, and named in the privacy notice
- [ ] The Art 27 representative, the DSA Art 13 legal representative and the GPSR Art 16 responsible person are treated as three separate appointments
- [ ] Every processor has a written contract containing all eight Art 28(3) letters, including deletion or return and audit rights
- [ ] Sub-processor authorisation model chosen, documented, and the change-notification and objection route implemented (Art 28(2))
- [ ] Vendor selection due diligence documented before onboarding (Art 28(1))
- [ ] Intra-EEA controller-processor clauses (Implementing Decision (EU) 2021/915) not confused with transfer SCCs (Implementing Decision (EU) 2021/914)
- [ ] Records of processing maintained under Art 30(1), and under Art 30(2) where acting as processor
- [ ] Art 30(5) exemption not claimed for regular processing — "not occasional" defeats it
- [ ] Breach procedure names the awareness trigger, the responsible person, the authority and the 72-hour clock (Art 33(1))
- [ ] Processor contracts require immediate notification to the controller (Art 33(2))
- [ ] Internal breach register in place covering **all** breaches, notified or not (Art 33(5))
- [ ] High-risk breach communication to data subjects prepared, with the Art 34(3) exemptions assessed rather than assumed
- [ ] DPIA screening run against Art 35(3) **and** the national supervisory authority's list (Art 35(4))
- [ ] Where a DPIA shows residual high risk, prior consultation under Art 36(1) planned before launch
- [ ] DPO test run against Art 37(1) and against any national threshold under Art 37(4); DPO free of conflicting duties (Art 38)
- [ ] All `[[…]]` placeholders resolved or reported as open

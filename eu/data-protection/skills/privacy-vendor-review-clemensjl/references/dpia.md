# DPIA trigger test (Art 35 GDPR)

A DPIA attaches to a **processing operation**, not to a supplier. "We did a DPIA for Vendor X" is a category error; the question is whether adding Vendor X makes a given processing likely to result in a high risk.

Basis: Art 35 GDPR. Guidance: Article 29 Working Party Guidelines on Data Protection Impact Assessment, **WP248 rev.01**, adopted 4 October 2017, endorsed by the EDPB on 25 May 2018 (Endorsement 1/2018).

Status as at 2026-08-05.

## The three statutory cases — Art 35(3)

A DPIA is required in particular for:

- **(a)** a systematic and extensive evaluation of personal aspects relating to natural persons which is based on automated processing, including profiling, and on which decisions are based that produce legal effects concerning the natural person or similarly significantly affect them;
- **(b)** processing on a large scale of special categories of data referred to in Art 9(1), or of personal data relating to criminal convictions and offences referred to in Art 10;
- **(c)** a systematic monitoring of a publicly accessible area on a large scale.

The list is not exhaustive — Art 35(1) is the general test: a type of processing, in particular using new technologies, likely to result in a high risk, taking into account nature, scope, context and purposes.

## The nine criteria — WP248 rev.01

Score the processing **as it will be after the integration**, not the vendor:

1. Evaluation or scoring, including profiling and predicting
2. Automated decision-making with legal or similarly significant effect
3. Systematic monitoring
4. Sensitive data or data of a highly personal nature
5. Data processed on a large scale
6. Matching or combining datasets
7. Data concerning vulnerable data subjects (children, employees, patients, asylum seekers)
8. Innovative use or applying new technological or organisational solutions
9. Processing that in itself prevents data subjects from exercising a right or using a service or a contract

WP248 rev.01's rule of thumb: **two or more criteria met → a DPIA is generally required.** One criterion met may still require one where the risk is high. Where you conclude no DPIA is needed but criteria are met, record the reasoning — that record is the Art 5(2) evidence.

## Vendor patterns that reliably score two or more

| Integration | Criteria hit |
|---|---|
| Session replay or full-page recording across authenticated areas | 3 (systematic monitoring), 5 (large scale), often 4 (whatever the user types) |
| Behavioural advertising with cross-site identifiers | 1 (evaluation), 3, 6 (combining datasets), 5 |
| Support tool that ingests ticket content plus a CRM merge | 6, 5, often 4 |
| Any tool used on a product aimed at or reachable by children | 7 plus whatever else |
| LLM feature that receives user-authored content and is used to make or shape a decision about them | 1, 8, often 2 and 4 |
| Fraud/risk scoring supplied by a third party that influences whether a user is served | 1, 2, 9 |
| Device fingerprinting for anti-fraud across a whole user base | 3, 5, 8 |
| Health-, finance- or sexuality-adjacent URLs sent to an analytics vendor | 4, 5 |

## National lists — Art 35(4) and Art 35(5)

Art 35(4) obliges each supervisory authority to establish and make public a list of the kinds of processing operations subject to a mandatory DPIA. Art 35(5) permits an optional list of operations for which no DPIA is required. **These lists are national and they differ**; a processing that is on the mandatory list in one Member State may not be on it in another. The lists are also communicated to the EDPB under Art 35(6), and the EDPB issued Opinions on each Member State's draft list in 2018.

Procedure for the review:

1. Identify the competent supervisory authority (Art 55/56 — main establishment for cross-border processing under Art 56(1)).
2. Retrieve **that authority's** Art 35(4) list from its own site and check it against the integration.
3. If the authority publishes an Art 35(5) exemption list, check that too.
4. Record the list version and the retrieval date. These lists are amended.

Austria: the Datenschutzbehörde has issued both a mandatory list under Art 35(4) and an exemption list under Art 35(5) as ministerial regulations. `[[UNVERIFIED: exact short titles and BGBl. II citations — ris.bka.gv.at and dsb.gv.at were not reachable at the time of writing; confirm before citing]]`.

## If a DPIA is required — Art 35(7) minimum content

- **(a)** a systematic description of the envisaged processing operations and the purposes, including where applicable the legitimate interest pursued by the controller
- **(b)** an assessment of the necessity and proportionality of the processing operations in relation to the purposes
- **(c)** an assessment of the risks to the rights and freedoms of data subjects
- **(d)** the measures envisaged to address the risks, including safeguards, security measures and mechanisms to ensure the protection of personal data and to demonstrate compliance

Plus: the DPO's advice must be sought where one is designated (Art 35(2)); where appropriate, the views of data subjects or their representatives must be sought (Art 35(9)); the DPIA must be reviewed where there is a change of the risk (Art 35(11)).

**Art 36(1) prior consultation:** if the DPIA indicates the processing would result in a high risk **in the absence of measures taken by the controller to mitigate it**, the authority must be consulted before processing starts. This is a stop condition, not a formality — the authority has eight weeks, extendable by six (Art 36(2)). Plan the launch around it or change the design.

## Trigger record

```
DPIA trigger — [[processing activity]] after adding [[vendor]]
Art 35(3) case:     [[(a) | (b) | (c) | none]]
WP248 criteria met: [[list the numbers]]  → count: [[n]]
National list:      [[authority]] Art 35(4) list version [[…]], retrieved [[date]] → [[listed | not listed]]
Art 35(5) list:     [[listed | not listed | authority publishes none]]
Conclusion:         [[DPIA required | not required]]
Reasoning:          [[two sentences]]
Art 36 risk:        [[residual high risk after measures? yes/no]]
DPO consulted:      [[name, date | no DPO designated — Art 37 assessment dated …]]
Recorded on:        [[date]] by [[name]]
```

## Checkpoints

- [ ] Assessment written about the processing operation, not about the vendor
- [ ] All three Art 35(3) cases checked explicitly
- [ ] All nine WP248 criteria scored, with the count stated
- [ ] The competent supervisory authority identified before consulting any list
- [ ] The authority's own Art 35(4) list retrieved, with version and date
- [ ] Art 35(5) exemption list checked where one exists
- [ ] Negative results recorded, not omitted
- [ ] Where a DPIA is required: all four Art 35(7) elements present
- [ ] DPO advice sought where a DPO is designated (Art 35(2))
- [ ] Art 36(1) residual-risk question answered before launch, with the eight-week clock accounted for
- [ ] Review trigger set for Art 35(11) — a change in risk, a new sub-processor, a new region

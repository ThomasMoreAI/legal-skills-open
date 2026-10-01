# RGPD — internal documentation

None of this is published. It is what an inspection or a complaint asks for, and what a published privacy policy is checked against. A polished policy that contradicts the actual processing is worse than no policy: it is documented evidence of the discrepancy.

## Registre des traitements — RGPD article 30

Mandatory for every controller with 250 or more employees, and below that threshold whenever the processing is not occasional, is likely to result in a risk to rights and freedoms, or concerns article 9 or article 10 data. In practice: every business running a website with a contact form, a customer database, or a payroll meets one of the exceptions and must keep a register.

Per processing: purpose; categories of data subjects and of data; categories of recipients including those in third countries; transfers outside the EU with the safeguard; retention period; a general description of technical and organisational measures. A processor keeps its own register under article 30(2).

The CNIL publishes a model register on `cnil.fr`. Use it rather than inventing a format.

## Sous-traitance — RGPD article 28

A written contract with every processor, containing the subject matter and duration, the nature and purpose, the types of data and categories of data subjects, and the eight obligations of article 28(3): processing only on documented instructions, confidentiality of personnel, article 32 security, conditions for engaging sub-processors, assistance with data-subject rights, assistance with articles 32 to 36, deletion or return at the end, and provision of the information needed for audits.

Accepting a supplier's online DPA is a contract; keep the version accepted and the date. Hosting, email delivery, analytics, CRM, payment, shipping, cloud storage, support tooling and agencies are processors. A payment institution acting on its own regulatory obligations is usually a separate controller — record which, and why.

## Security — RGPD article 32

Measures appropriate to the risk. Documented, not asserted. Minimum for a small site: TLS everywhere with HSTS, individual accounts with strong authentication and MFA on administration, least privilege, patching discipline, backups that have been restored at least once as a test, logging of administrative access, and a documented deletion routine matching the retention periods in the register.

## Violations de données — RGPD articles 33 and 34

Notification to the CNIL within **72 hours** of becoming aware, unless the breach is unlikely to result in a risk. Communication to the data subjects without undue delay where the risk is high. Every breach is recorded internally, including those not notified, with the facts, the effects and the remedial action.

Write the procedure before it is needed: who decides, who notifies, the CNIL notification route, the template for informing affected users. A 72-hour deadline discovered on a Friday evening is not a deadline that gets met.

## AIPD — RGPD article 35

A data protection impact assessment is required where processing is likely to result in a high risk, and in particular for systematic and extensive evaluation based on automated processing including profiling, large-scale processing of article 9 or article 10 data, and large-scale systematic monitoring of a publicly accessible area. The CNIL publishes a list of processing operations requiring an AIPD and a list of those exempt; check both before concluding no assessment is needed.

## DPO — RGPD article 37

No French headcount threshold. Mandatory for public authorities, where core activities require regular and systematic monitoring of data subjects on a large scale, or where core activities consist of large-scale processing of article 9 or article 10 data. Where appointed, the contact details are published and the appointment is notified to the CNIL. A voluntarily appointed DPO carries the same statutory status and protections.

## CNIL référentiels and règlements types

The CNIL adopts **référentiels** and **règlements types** that set out how it expects specific categories of processing to be carried out — human resources, customer and prospect management, access control including biometrics, health-sector processing, and research. Conformity with the applicable référentiel is the practical benchmark in an inspection. Where the project touches health data, biometrics or the NIR, identify the applicable référentiel before designing the processing, not afterwards.

## CNIL sanction procedure

The CNIL operates an ordinary sanction procedure before the formation restreinte and a **simplified procedure** for cases of limited complexity, introduced into loi n° 78-17 as article 22-1 with effect from 26 January 2022. The simplified procedure carries a lower fine ceiling than the ordinary one and is the route by which most of the smaller published fines are issued. [[UNVERIFIED: the maximum fine available under the simplified procedure of article 22-1 de la loi 78-17 — confirm on Légifrance or cnil.fr before quoting a figure]]

## Data-subject requests — RGPD articles 12 to 22

One month to answer, extendable by two further months for complex or numerous requests, with the data subject informed of the extension within the first month. Free of charge, except for manifestly unfounded or excessive requests, where the burden of proving that lies with the controller.

Practical requirements that get missed: identity verification proportionate to the request, without demanding a copy of an identity document as a reflex; a route that does not require creating an account; propagation of erasure and rectification to processors and to backups, with a documented approach where backups cannot be edited; and a log of every request with the date received, the date answered and the outcome. Refusals must be reasoned and must state the right to complain to the CNIL and to a judicial remedy.

## Transfers outside the EU — RGPD chapter V

Identify every transfer, including access from outside the EU by a support team. For each: the recipient, the country, and the basis — an adequacy decision, standard contractual clauses, binding corporate rules, or an article 49 derogation used genuinely as an exception rather than as a routine.

Where standard contractual clauses are used, a transfer impact assessment documenting the law of the destination country and any supplementary measures is expected. Adequacy decisions can be challenged and can change; record which decision is relied on and the date, so the dependency is visible if it moves.

## Documentation set to hold

| Document | Basis |
|---|---|
| Registre des traitements du responsable | RGPD art. 30(1) |
| Registre du sous-traitant, where acting as processor | RGPD art. 30(2) |
| Contracts with every processor | RGPD art. 28(3) |
| Records of consent, with timestamp and text version | RGPD art. 7(1) |
| Consent logs for trackers, with the banner version | art. 82 loi 78-17 |
| Security measures and their review | RGPD art. 32 |
| Breach register and notification procedure | RGPD art. 33(5) |
| AIPD where required, and the reasoning where not | RGPD art. 35 |
| Transfer safeguards: adequacy, SCCs, transfer impact assessments | RGPD ch. V |
| Procedure and log for data-subject requests | RGPD art. 12 |
| Retention schedule matching the register | RGPD art. 5(1)(e) |

## Checkpoints

- [ ] Register exists, is current, and matches the published privacy policy line by line
- [ ] Every processor has a signed or accepted article 28 contract, filed with its version and date
- [ ] Sub-processor list known for each processor, and changes are notified
- [ ] Retention periods implemented as an actual deletion routine, not only written down
- [ ] Breach procedure written, with named decision-maker and the CNIL notification route
- [ ] Consent proof stored for marketing and for trackers, separately
- [ ] Transfers outside the EU listed with the safeguard and, where relevant, a transfer impact assessment
- [ ] AIPD carried out or its absence reasoned against the CNIL lists
- [ ] DPO appointed where required, published and notified to the CNIL
- [ ] Applicable CNIL référentiel identified for HR, biometrics, health or research processing
- [ ] Data-subject request procedure tested end to end at least once

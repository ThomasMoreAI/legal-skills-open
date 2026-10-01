# Accountability, the ICO fee, and internal data protection duties

None of this is published on the website. All of it is enforceable, and the fee in particular is the single most commonly missed UK-specific obligation because it has no EU counterpart.

## The data protection fee

Data Protection (Charges and Information) Regulations 2018 (SI 2018/480), made under DPA 2018 ss 137–138. Status as at 2026-08-05: in force, reg 3 as amended by the Data Protection (Charges and Information) (Amendment) Regulations 2025 (SI 2025/63) with effect from 17 February 2025.

Every controller who processes personal data must pay an annual fee to the Commissioner unless exempt. The tiers under reg 3 and reg 4:

| Tier | Who | Fee |
|---|---|---|
| Tier 1 — micro organisations | turnover of £632,000 or less, **or** no more than 10 members of staff; also charities and small occupational pension schemes regardless of size | £52 |
| Tier 2 — small and medium organisations | not in tier 1; turnover of £36 million or less **or** no more than 250 members of staff | £78 |
| Tier 3 — large organisations | everyone else | £3,763 |

A £5 reduction applies where payment is made by direct debit. Turnover and staff numbers are assessed on the first day of the charge period. Public authorities are assessed on staff numbers only, disregarding turnover.

Practical points that catch people out:

- Sole traders and single-director companies are controllers and pay. There is no "too small to register" threshold.
- The exemptions in the Regulations are narrow and purpose-based (for example processing only for staff administration, or for a not-for-profit body's own membership records). Running a website with analytics, a mailing list or an online shop takes an organisation outside them.
- CCTV covering anything beyond a private household removes the domestic-purposes exemption.
- Non-payment is enforced by the Commissioner directly, by penalty notice under DPA 2018 s 158, independently of whether any other rule has been broken.

## Records of processing — UK GDPR Art 30

Controllers and processors must maintain records of processing activities. The Art 30(5) relief for organisations with fewer than 250 employees does not apply where processing is not occasional, is likely to result in a risk to rights and freedoms, or involves special category or criminal offence data — which covers almost any live commercial website. Assume the record is required.

Contents: name and contact details of the controller and any DPO; purposes; categories of data subjects and data; categories of recipients including recipients outside the UK; transfers and their safeguards; retention periods; a general description of technical and organisational security measures.

## Processor contracts — UK GDPR Art 28

Every processor (hosting, email sending, analytics, CRM, payments where the provider acts as processor, support tooling) needs a written contract containing the Art 28(3) terms: process only on documented instructions, confidentiality obligations, Art 32 security, sub-processor authorisation, assistance with data subject rights and Arts 32–36, deletion or return at end of service, audit and information rights. Standard supplier data processing addenda usually satisfy this; the failure mode is never having accepted one.

## Security — UK GDPR Art 32

Appropriate technical and organisational measures, judged against the state of the art, cost, and the risk. For a website that means at minimum: TLS everywhere, no credentials in the repository, current dependencies, access control with individual accounts, backups tested for restore, and logging that would let a breach be reconstructed.

## Personal data breach — UK GDPR Arts 33 and 34

Notify the Commissioner without undue delay and where feasible within 72 hours of becoming aware, unless the breach is unlikely to result in a risk to the rights and freedoms of natural persons. Notify affected individuals without undue delay where the risk is high. Record every breach internally, including those not notified, with the reasoning.

The 72 hours runs from awareness, not from the end of the investigation. The process must exist before the incident: who is called, who decides, where the log lives.

## Data protection impact assessment — UK GDPR Art 35

Required where processing is likely to result in a high risk, in particular for systematic and extensive evaluation based on automated processing including profiling, large-scale processing of special category data, or systematic monitoring of a publicly accessible area on a large scale. The ICO also publishes a list of operations always requiring a DPIA. Do the assessment before processing starts.

## Data Protection Officer — UK GDPR Art 37

Mandatory for public authorities, for core activities consisting of regular and systematic monitoring of data subjects on a large scale, and for core activities consisting of large-scale processing of special category or criminal offence data. There is no headcount trigger — the German 20-employee threshold has no UK equivalent. Where no DPO is required, name an accountable person anyway.

## Complaints handling — DPA 2018 s 164A

Inserted by DUAA 2025 s 103, in force 19 June 2026. The controller must facilitate the making of complaints about its processing, including by providing a complaint form capable of being completed electronically, acknowledge receipt within 30 days, take appropriate steps to respond including making enquiries, and inform the complainant of the outcome without undue delay. Section 164B allows the Secretary of State to require controllers to report complaint numbers to the Commissioner.

This is an operational duty, not a notice paragraph. Build the form and the internal process, then describe them in the privacy notice.

## Record of processing template

Internal document. One row per processing operation, not one row per system.

```markdown
<!-- DRAFT – NOT LEGALLY APPROVED -->
# Record of processing activities — [[registered name]]
Controller: [[name, registered office, company number]]
DPO or accountable owner: [[name, contact]]
ICO registration number: [[number]]
Last reviewed: [[date]]

| Processing activity | Purpose | Data subjects | Data categories | Lawful basis (Art 6) | Art 9/10 condition | Recipients | Outside the UK? | Mechanism | Retention | Security measures |
|---|---|---|---|---|---|---|---|---|---|---|
| [[e.g. order fulfilment]] | [[purpose]] | [[customers]] | [[name, address, order history]] | [[contract]] | [[n/a]] | [[carrier, payment provider]] | [[yes/no]] | [[IDTA / adequacy]] | [[period]] | [[summary]] |
```

## Breach log template

```markdown
<!-- DRAFT – NOT LEGALLY APPROVED -->
| Ref | Detected (date, time) | Detected by | What happened | Data and people affected | Risk assessment | Commissioner notified? | Decision reasoning | Individuals notified? | Containment and remediation | Closed |
|---|---|---|---|---|---|---|---|---|---|---|
```

The "decision reasoning" column is the one that matters on inspection: Art 33(1) permits not notifying only where the breach is unlikely to result in a risk, and Art 33(5) requires the reasoning to be documented either way.

## Checkpoints

- [ ] ICO fee paid, tier calculated from actual turnover and staff numbers, renewal date diarised
- [ ] ICO registration number recorded and quoted in the privacy notice
- [ ] Record of processing activities exists and matches what the site actually does
- [ ] Art 28 contract or data processing addendum in place with every processor, stored and findable
- [ ] Transfers logged with their mechanism (see `international-transfers.md`)
- [ ] Breach process written down: detection, 72-hour clock owner, decision criteria, notification templates, internal log
- [ ] DPIA completed where Art 35 is triggered, before processing began
- [ ] DPO appointed where Art 37 requires it; otherwise an accountable owner named
- [ ] Electronic complaint form live, 30-day acknowledgement built into the workflow (DPA 2018 s 164A)
- [ ] Retention schedule exists and deletion actually happens
- [ ] No reliance on a German or EU headcount threshold for the DPO decision

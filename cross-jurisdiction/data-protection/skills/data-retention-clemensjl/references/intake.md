# Intake

Answer before any period is stated. Unanswered questions become `[[MISSING: …]]` in the schedule and in the report back to the user. Never fill one in plausibly — a wrong minimum is a statutory breach and a wrong maximum is a GDPR breach, in opposite directions.

## Establishment and applicable law

1. In which countries is the controller established, and where is the accounting kept? The statutory minimum follows the place of establishment and the tax residence, not the location of the server.
2. Legal form and whether the entity is entered in a commercial register (Firmenbuch, Handelsregister, Companies House, RCS, Registro Imprese). Register entry usually triggers the commercial-code retention duty on top of the tax one.
3. Is the entity a credit institution, insurance undertaking, securities institution, payment institution or other supervised entity? These carry longer periods and, in Germany, are explicitly excluded from the 2025 shortening (Art 97 § 19a Abs 3 EGAO).
4. Does the entity sell to consumers in other EU/EEA states? Consumer-law limitation periods vary and drive warranty-claim retention.
5. Is there an existing retention policy, records-management standard or industry code that already binds the entity contractually?

## The data

6. List every system that stores data about an identified or identifiable person. Include the ones nobody calls a database: object storage, log aggregator, error tracker, analytics, CRM, support desk, email service provider, warehouse, LLM API logs, spreadsheets.
7. For each system, which **data elements** does it hold? Element level, not table level.
8. Which elements are tax- or accounting-relevant (anything that supports a booking, an invoice, a payroll run, a VAT return)?
9. Which elements fall under Art 9 GDPR (health, biometrics, trade union, religion, political opinion, sex life, sexual orientation) or Art 10 (criminal convictions)?
10. Which elements are card data (PAN, expiry, cardholder name, service code) or sensitive authentication data (full track, CVV/CVC/CAV2/CID, PIN/PIN block)?
11. Are children's data processed? Below which age, and how is the age determined?
12. Which elements exist only as derived or aggregated data, and can they still be linked back to a person?

## Purposes and bases

13. Per processing activity: purpose, legal basis under Art 6(1), and for Art 9 data the condition under Art 9(2).
14. Which activities rest on consent? Consent withdrawal ends the basis, so the retention period for those elements is bounded by the withdrawal, not by a calendar.
15. Which activities rest on legitimate interest, and does the balancing test document a period? An LIA without a period is incomplete.
16. Is there an active or foreseeable legal dispute, regulatory investigation, audit or litigation hold? A hold overrides the schedule and must be expressible in the system.

## Systems and mechanics

17. Which database engines and versions, which object stores, which message brokers, which search indexes?
18. Is the primary database partitioned by time anywhere? Partitioning changes deletion from a row operation to a metadata operation.
19. What is the backup regime per system: full and incremental frequency, rotation window, off-site copies, immutability or object-lock settings?
20. What is the point-in-time recovery window per managed database, and what is the WAL/oplog/binlog archive retention behind it?
21. Is object versioning, soft delete or object lock enabled on any bucket? In which mode (governance or compliance)?
22. Which replicas, read models, caches, search indexes and materialised views derive from the primary store?
23. Which data leaves for a warehouse or lakehouse, on what schedule, and is the load append-only?

## Processors and third parties

24. Full processor and sub-processor list, with the Art 28(3) contract for each and its termination clause under Art 28(3)(g).
25. Which of them expose a deletion API, and which require a support ticket? Record the documented turnaround for each.
26. Third-country transfers: which processors, on which transfer mechanism, and what does their own retention default look like?
27. Which tools were onboarded without a contract review (the marketing pixel, the session recorder, the AI coding assistant, the LLM API)?

## Operations

28. Who owns each data element? A schedule row without a named owner will not be maintained.
29. How are erasure requests received today, who triages them, and what is the documented completion time against the Art 12(3) one-month deadline?
30. Is there any existing scheduled deletion job? What does it delete, how often, and where does its output go?
31. What monitoring and alerting exists on those jobs?
32. Can the system express "restricted": readable for the establishment, exercise or defence of legal claims, invisible to every other code path? If not, this is the largest gap in the project.

## Checkpoints

- [ ] Establishment countries and register status recorded
- [ ] Supervised-entity status answered explicitly (yes/no, with the supervisory regime named)
- [ ] Data-element inventory exists at element level, not table level
- [ ] Tax- and accounting-relevant elements flagged
- [ ] Art 9 / Art 10 elements flagged
- [ ] Card data and sensitive authentication data flagged, including in logs
- [ ] Legal basis per activity recorded, consent-based activities separated
- [ ] Litigation-hold mechanism identified or flagged as missing
- [ ] Backup and PITR windows recorded per system
- [ ] Versioning, soft delete and object lock status recorded per bucket
- [ ] Processor list complete, with termination-clause reference per contract
- [ ] Named owner per data element
- [ ] Ability to express restriction of processing answered honestly
- [ ] Every unanswered question carried forward as `[[MISSING: …]]`

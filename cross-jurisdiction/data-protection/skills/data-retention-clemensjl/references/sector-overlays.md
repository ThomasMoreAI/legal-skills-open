# Sector overlays

Rules that sit on top of the general commercial and tax minimums and, in one case, force a period of zero. Status as at 05.08.2026.

## Payment card data — PCI DSS

Current standard: **PCI DSS v4.0.1** (pcisecuritystandards.org document library; still referenced as current in PCI SSC material dated July 2026).

The standard splits card data into two classes and treats them oppositely:

| Class | Elements | Retention |
|---|---|---|
| Account data / cardholder data | PAN, cardholder name, expiry date, service code | Minimised, justified, time-bounded, PAN rendered unreadable wherever stored |
| **Sensitive authentication data (SAD)** | Full track data, card verification code (CVV2/CVC2/CAV2/CID), PIN and PIN block | **Not retained after authorisation** |

Requirement mapping, PCI DSS v4.x:

- **3.2.1** — account data storage kept to a minimum, with a data-retention and disposal policy, defined retention period, and a process for deleting data that exceeds it.
- **3.3.1** — SAD is not retained after authorisation, even where encrypted. Sub-requirements 3.3.1.1 to 3.3.1.3 address the verification code, full track data and PIN/PIN block respectively.
- **3.5.1** — PAN is rendered unreadable wherever it is stored.

`[[UNVERIFIED: the verbatim wording and exact numbering of 3.2.1, 3.3.1.1–3.3.1.3, 3.3.2/3.3.3 and 3.5.1 — the PCI SSC document library refuses automated fetches. Read the v4.0.1 PDF before quoting the standard word for word]]`

Engineering consequences that are certain regardless of wording:

- **The CVV period is zero.** There is no configuration, no encryption mode and no business justification that makes storing it acceptable. This includes: request bodies in the application log, the error tracker's captured payload, the HTTP replay in the APM trace, the raw webhook archive, the analytics session recording, and the QA fixture file. Search for the field name across the whole repository and the whole log estate, not just the database.
- PAN in a log line is card data even though the log is not the cardholder data environment on the architecture diagram.
- Redaction at the sink is not enough. Redact at the source, because the sink's own retention window has already started.

## Anti-money laundering / KYC

The AML retention duty is the classic minimum > maximum case: the customer relationship ends, the GDPR purpose ends, and the file must still be kept.

**Directive (EU) 2015/849 Art 40**, read 05.08.2026 (EUR-Lex serves no body to automated fetch; the Publications Office CELLAR does, at `http://publications.europa.eu/resource/celex/32015L0849` with `Accept: application/xhtml+xml`):

- **Art 40(1)(a)** — customer due diligence: a copy of the documents and information necessary to comply with Chapter II, **for five years after the end of the business relationship, or after the date of an occasional transaction**.
- **Art 40(1)(b)** — supporting evidence and records of transactions, original documents or copies admissible in judicial proceedings, necessary to identify transactions: **the same five years**, on the same two start points.
- **Second subparagraph** — on expiry, Member States "shall ensure that obliged entities **delete** personal data, unless otherwise provided for by national law". Deletion is the default, not an option.
- **Third subparagraph** — a Member State may allow or require further retention only after "a thorough assessment of the necessity and proportionality of such further retention", and **"That further retention period shall not exceed five additional years."** So the ceiling is 5+5, and the extra five needs a documented assessment, not a preference.

Two consequences for a schedule: the clock has **two possible start events** per record — end of relationship, or date of an occasional transaction — so the schema needs both, and the extension is a **national-law switch**, so a multi-country product needs it per jurisdiction rather than as a global constant.

**Regulation (EU) 2024/1624 (AMLR) — the application date is verified, the retention article is not.** Final provision, read via CELLAR 05.08.2026, verbatim: the Regulation *"shall apply from **10 July 2027**, except in relation to obliged entities referred to in Article 3, points (3)(n) and (o), to which it shall apply from **10 July 2029**"*. Until then Directive (EU) 2015/849 as nationally transposed governs, so a schedule written now runs on the Directive and needs a diarised review before July 2027.

`[[UNVERIFIED: the AMLR record-keeping article number and its period. The CELLAR XHTML rendition served the recitals and the final provisions but the enacting terms could not be read out of it on 05.08.2026. Do not assume the Directive's 5+5 structure carries over unchanged — read the retention article before writing a number]]`

Whatever the number, three implementation points hold:

- The clock starts at the **end of the relationship**, not at onboarding. The job needs a relationship-end timestamp, and most systems do not have one.
- The retained file must be reachable for a regulator and unreachable for everything else — restriction, not live storage.
- Deletion at the end of the AML period is itself a duty in several transpositions, not merely permitted. An AML archive with no expiry is as much a finding as one with no records.

## Health data

There is no EU-wide health-record retention period. It is national, and the periods are long — often decades — which puts them in permanent tension with Art 5(1)(e).

`[[UNVERIFIED: national health-record periods — Germany § 630f Abs 3 BGB (commonly cited as 10 years after the treatment concludes), Austria § 51 Abs 1 ÄrzteG (10 years) and the longer hospital-record period under KAKuG, France Code de la santé publique R1112-7 (20 years). Verify each against the national consolidated text before stating a number]]`

`[[UNVERIFIED: Regulation (EU) 2025/327 on the European Health Data Space — its number, entry into force, and whether it imposes any retention period at all rather than access and interoperability duties]]`

Rules that do hold:

- Health data is Art 9 data. The retention justification must name the Art 9(2) condition, not only the Art 6(1) basis.
- Retention of health data for a statutory medical period does not license its use for anything else. This is the strongest case for hard restriction with an audit trail on every read.

## Telecom traffic and location data

The consistent line from the CJEU is that **general and indiscriminate retention of traffic and location data for the purpose of fighting ordinary crime is precluded** by Art 15(1) of Directive 2002/58/EC read with the Charter, while targeted, time-limited and safeguarded retention can be justified.

`[[UNVERIFIED: the individual holdings and dates of Digital Rights Ireland (C-293/12), Tele2 Sverige and Watson (C-203/15, C-698/15), La Quadrature du Net (C-511/18 and joined cases), Commissioner of An Garda Síochána (C-140/20), SpaceNet and Telekom Deutschland (C-793/19, C-794/19) and La Quadrature du Net II (C-470/21) on IP-address retention for copyright enforcement. curia.europa.eu was not fetched for this file; read the judgments before summarising any one of them]]`

`[[UNVERIFIED: any 2025/2026 EU legislative initiative to reintroduce a harmonised data-retention obligation]]`

Practical rule for a non-telecom product: do not reason by analogy from telecom retention case law to your application logs. The case law constrains state-mandated retention; it does not authorise your own.

## CCTV and video

Short periods are the norm and long ones need a specific justification.

**Austria, § 13 DSG.** Consolidated text read on RIS 05.08.2026. **72 hours is not a hard cap** — it is the point at which the burden of justification changes, and getting that wrong in either direction is the common error.

- **Abs 3, verbatim:** *"Aufgenommene personenbezogene Daten sind vom Verantwortlichen zu löschen, wenn sie für den Zweck, für den sie ermittelt wurden, nicht mehr benötigt werden und keine andere gesetzlich vorgesehene Aufbewahrungspflicht besteht. Eine länger als 72 Stunden andauernde Aufbewahrung muss verhältnismäßig sein und ist gesondert zu protokollieren und zu begründen."*
- So: delete as soon as the purpose is exhausted — which is often **well under** 72 hours. Beyond 72 hours the retention must be proportionate **and** separately logged **and** reasoned. Build the log; a retention setting of "7 days" with no written reasoning is the finding, not the seven days as such.
- **Abs 2** requires every processing operation on the recording to be logged, except in real-time monitoring. That is an access log on playback and export, not just on deletion.
- **Abs 1** requires access control and protection against subsequent alteration by unauthorised persons.
- **Abs 5** requires the recording to be marked, and the marking must identify the controller unambiguously unless the data subjects already know who it is. **Abs 6** exempts covert processing that is strictly time-limited in the individual case, subject to safeguards including later notification.
- **Abs 4**: Abs 1 to 3 do not apply to Bildaufnahmen under § 12 Abs 3 Z 3.

`[[UNVERIFIED: EDPB Guidelines 3/2019 on processing of personal data through video devices, and what they say about retention duration]]`

What is safe to say: video retention is measured in days, the justification is documented per camera, and an "indefinite until the disk fills" configuration is the default failure and the easiest audit finding in the building.

## Employment records

Employment retention pulls in three directions at once: payroll is tax data, the employment contract is contract data, and discrimination or pension claims have their own limitation periods.

| Element | Driver |
|---|---|
| Payroll runs, wage tax records | Tax statute of the employer's jurisdiction (see `minimum-periods.md`) |
| Employment contract, amendments, termination | National limitation period for employment claims |
| Application documents of rejected candidates | Anti-discrimination limitation period; typically months, not years |
| Occupational health and exposure records | Sector safety law; sometimes decades |
| Pension entitlement data | Until the entitlement is extinguished, often lifelong |

Rejected-applicant data is the element most often left forever in the ATS. It has the shortest defensible period in the whole table and no statutory minimum beyond the discrimination claim window.

## Checkpoints

- [ ] CVV/CVC/CAV2/CID and full track data confirmed absent from database, logs, error tracker, APM traces, webhook archives, session recordings and test fixtures
- [ ] PAN storage justified, minimised and rendered unreadable, with a documented retention period (PCI DSS v4.0.1 Req 3.2.1, 3.5.1)
- [ ] AML clock implemented from relationship end, not onboarding, and the archive restricted
- [ ] AML archive has an expiry, not only a start
- [ ] Health data retention names the Art 9(2) condition and the national statute
- [ ] Video retention stated in days per camera with a written justification
- [ ] Rejected-applicant data has a period and a job, both shorter than a year
- [ ] Every `[[UNVERIFIED: …]]` in this file resolved before the corresponding number is published

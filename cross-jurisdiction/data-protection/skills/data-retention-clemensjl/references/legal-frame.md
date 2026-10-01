# The legal frame

Regulation (EU) 2016/679 (GDPR). Article text verified against the consolidated reproduction at gdpr-info.eu, which follows OJ L 119, 4.5.2016. Status as at 05.08.2026.

## Art 5(1)(e) — storage limitation, the maximum

Personal data shall be "kept in a form which permits identification of data subjects for no longer than is necessary for the purposes for which the personal data are processed". The Regulation names **no period**. It states a necessity test bounded by the purpose. Two consequences engineers get wrong:

- The maximum moves when the purpose ends, not when a calendar date is reached. Consent withdrawn, contract terminated, account closed: the purpose is gone and the clock is already expired.
- "In a form which permits identification" is the escape hatch. Data that no longer permits identification is out of scope entirely (Recital 26) — but see `schema-patterns.md` for how high that bar actually is.

Art 5(2) makes the controller responsible for **demonstrating** compliance. That is why the deletion job needs evidence output and not just a green checkmark.

## The statutory minimum, and why the interval exists

Commercial and tax statutes require records to be **kept**. GDPR requires them **not to be kept longer than necessary**. Nobody harmonised the two, and they are set by different ministries for different reasons. So each data element has an interval:

```
[ statutory minimum ] ────────────────► [ Art 5(1)(e) maximum ]
   § 147 AO, § 132 BAO, L123-22,           purpose exhausted
   art 2220 CC, s 388 CA 2006, ...
```

Three cases, and the third is the one that breaks systems:

| Case | Resolution |
|---|---|
| maximum > minimum | Delete when the purpose ends. The statute is not reached. |
| maximum = minimum | Delete on the statutory date. |
| **minimum > maximum** | The purpose has ended but the statute still binds. **Do not delete. Restrict.** |

The third case is the normal case for invoices, payroll and ledgers. It is the reason a retention system needs a state between "live" and "gone".

## The CNIL three-phase model

The CNIL structures the same interval as a lifecycle, which maps cleanly onto storage tiers (cnil.fr, "Les durées de conservation des données"):

1. **Base active** — the period necessary to achieve the purpose; data accessible to the operational teams.
2. **Archivage intermédiaire** — the purpose is exhausted but the data must be kept, typically for a legal obligation: *"doivent être conservées pour répondre à une obligation légale (par exemple, les données de facturation doivent être conservées dix ans)"*. The CNIL requires separation from the live database: *"une séparation avec la base active doit être opérée"*, either by physical extraction into a dedicated archive or by logical isolation restricting who may access it.
3. **Archivage définitif** — permanent preservation for data of enduring value.

Use this as the implementation shape for the minimum > maximum case. Archivage intermédiaire is Art 18 restriction with a French name and an access-control requirement attached.

## Art 17 — erasure, and its exceptions

Art 17(1): the data subject has the right to obtain erasure "without undue delay" on the listed grounds, including that the data are no longer necessary, that consent was withdrawn, that the subject objects, or that processing was unlawful.

Art 17(2): where the data were made public, the controller must take reasonable steps, including technical measures, to inform other controllers processing the data of the erasure request.

Art 17(3) disapplies the right where processing is necessary for, among others:

- (a) exercising the right of freedom of expression and information
- **(b) compliance with a legal obligation which requires processing by Union or Member State law to which the controller is subject**, or for a task in the public interest
- (c) public-health reasons
- (d) archiving in the public interest, scientific or historical research or statistical purposes, where erasure would seriously impair the objectives
- (e) the establishment, exercise or defence of legal claims

**(b) is the tax and accounting carve-out.** An erasure request against an invoice inside § 147 AO or § 132 BAO does not succeed. Answering "we have deleted everything" while the ledger row survives is a false statement to the data subject on top of the underlying problem.

## Art 18 — restriction, the state your schema does not have

Art 18(1) grounds include (b) processing is unlawful and the subject opposes erasure and requests restriction instead, and (c) the controller no longer needs the data but the subject requires them for legal claims.

Art 18(2) defines the state: restricted data may, with the exception of storage, only be processed "with the data subject's consent or for the establishment, exercise or defence of legal claims or for the protection of the rights of another natural or legal person or for reasons of important public interest".

Art 18(3): the subject must be informed **before** the restriction is lifted.

Engineering translation: a restricted record must be readable by the finance export and the litigation path, and invisible to every other code path — search, recommendations, marketing, support, analytics, backfills, LLM prompts. A boolean on the row is not enough, because the default in every unaudited query is to ignore it. See `schema-patterns.md`.

## Art 13(2)(a) — what the notice must say

The controller must provide "the period for which the personal data will be stored, or if that is not possible, the criteria used to determine that period". Two acceptable forms, one unacceptable:

- acceptable: "Invoice data: 8 years from the end of the year of issue (§ 147 Abs 3 AO)."
- acceptable: "Support tickets: until the ticket is closed plus 12 months, so that follow-up requests can be linked to prior contact."
- **not acceptable**: "as long as necessary", "in accordance with statutory periods", "for the duration of the business relationship" with nothing after it.

The same duty applies under Art 14(2)(a) for indirectly collected data.

## Art 30 — the ROPA column

Art 30(1)(f) requires, in the controller's record, "where possible, the envisaged time limits for erasure of the different categories of data". Art 30(2)(c) covers the processor's record. The plural — different categories, different limits — is the legal source of the per-element rule.

"Where possible" is not an opt-out you may exercise by preference. If the period genuinely cannot be fixed, the criteria go in the column.

## Art 25 — retention as a design duty

Art 25(1) requires appropriate technical and organisational measures at the time of determining the means of processing. Art 25(2) requires by default that only personal data necessary for each specific purpose are processed, and that this applies to "the amount of personal data collected, the extent of their processing, **the period of their storage** and their accessibility".

A table created without an expiry mechanism is an Art 25(2) defect at creation time, independent of whether the data has yet outlived its purpose. Add the expiry in the same migration that adds the table.

## Art 28(3)(g) — the processor's end-of-engagement duty

See `processors.md`. It is a termination obligation, not a running control.

## Anonymisation status

Recital 26: the principles of data protection do not apply to anonymous information, and identifiability is judged by "all the means reasonably likely to be used". Art 4(5) defines pseudonymisation, which explicitly remains personal data.

The current guidance layer, status as at 05.08.2026:

- **EDPB Guidelines 02/2026 on anonymisation** — released for public consultation on 08.07.2026, feedback period 08 July to 30 October 2026 (edpb.europa.eu, public consultations register). **Not final.** Cite as draft, never as settled law.
- **EDPB Guidelines 01/2025 on pseudonymisation** — consultation ran 17 January to 14 March 2025. `[[UNVERIFIED: whether the final version has since been adopted — check the EDPB guidelines register before citing as final]]`
- WP29 Opinion 05/2014 on Anonymisation Techniques (WP216) remains the long-standing reference for the three risks: singling out, linkability, inference. `[[UNVERIFIED: current EDPB endorsement status of WP216 as at 2026]]`

## Checkpoints

- [ ] Every element has both a minimum and a maximum recorded, not one number
- [ ] Elements where minimum > maximum are routed to restriction, not deletion
- [ ] Restriction is implemented as a state the query layer cannot ignore by omission
- [ ] Art 13(2)(a) sentence exists per activity and states a period or explicit criteria
- [ ] Art 30(1)(f) column filled for every category
- [ ] New tables ship with an expiry mechanism in the same migration (Art 25(2))
- [ ] Anonymisation claims cite Recital 26 reasoning, and any EDPB 02/2026 reference is marked as draft
- [ ] Consent-based processing has retention bounded by withdrawal, not only by calendar

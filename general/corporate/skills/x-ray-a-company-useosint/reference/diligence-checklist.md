# Corporate diligence checklist by risk area

Work each area to a sourced finding or a documented negative. A negative is only
worth recording if you name the database and the date.

## A. Legal existence and standing

- [ ] Legal name, registration number, jurisdiction, incorporation date, entity type
- [ ] Current status (active / dormant / in liquidation / struck off / dissolved)
- [ ] Registered office and any recent changes of office
- [ ] Former names and any recent renames
- [ ] Trading names and brands, and which entity owns each
- [ ] Whether the entity you are contracting with is the entity with the history
- [ ] Branches or registered foreign presences in other jurisdictions
- [ ] Tax/VAT identifier verified against the tax authority's own checker where one exists (the EU's VIES service validates EU VAT numbers)
- [ ] Legal Entity Identifier via the GLEIF search, if the entity trades in financial markets — LEI records include parent relationships

Primary sources: the national company registry (see the registry catalogue in
`who-really-owns-it`), plus the securities regulator's filing system for listed
entities.

## B. Ownership and control

- [ ] Direct shareholders and holdings
- [ ] Ultimate parent, with the full intermediate chain
- [ ] Subsidiaries and affiliates
- [ ] Registered beneficial owners, or the point at which the chain becomes opaque
- [ ] Whether directors appear to be nominees
- [ ] Trusts, foundations, or bearer instruments anywhere in the chain
- [ ] Recent ownership changes and their filing dates
- [ ] Charges, liens, pledges, or security interests over shares or assets

Where it breaks: percentage thresholds, nominee arrangements, trusts, and
jurisdictions whose registers are closed. Record the terminus.

## C. People

- [ ] All current officers and directors, from the registry not the website
- [ ] Recent officer resignations and appointments, with dates
- [ ] Each officer's other and prior directorships
- [ ] Prior companies of officers that were dissolved, struck off, or liquidated
- [ ] Any director disqualification (jurisdictions with disqualification regimes publish registers; the UK publishes disqualified directors)
- [ ] Senior staff not on the register — run `find-anyone` on the ones that matter
- [ ] Workforce size and function mix, with the platform-count caveat stated

## D. Financial and disclosure

- [ ] Filing regime for this entity type: what it is actually required to disclose
- [ ] Latest filed accounts, and whether they are audited, abridged, or micro-entity
- [ ] Filing punctuality across several years; repeated lateness is a signal
- [ ] Auditor identity, auditor changes, resignations, and any qualified opinion
- [ ] Registered charges and secured lenders
- [ ] Related-party transactions, where disclosed
- [ ] Coherence between filed accounts and claimed scale of operations

Listed-entity sources: the US SEC's EDGAR system, including its full-text search
across filings; SEDAR+ for Canadian issuers; and each market's national storage
mechanism for regulated disclosures in Europe.

## E. Litigation and insolvency

- [ ] Court records searched for the entity, former names, and subsidiaries
- [ ] Disposition of every matter found, not just the filing
- [ ] Bankruptcy or insolvency proceedings against the entity or its officers' prior companies
- [ ] Statutory notices (many jurisdictions publish insolvency and corporate notices in an official gazette; the UK uses The Gazette)
- [ ] Regulatory enforcement actions by the relevant sectoral regulator

US federal courts: PACER, with the CourtListener/RECAP archive as a free mirror
of documents others have already pulled. UK and Ireland: BAILII plus the official
judgment publication service. State, provincial, and lower-court coverage is
patchy everywhere and frequently not full-text searchable — say so in the report.

## F. Procurement and contracting history

- [ ] Public contract awards to the entity and its group
- [ ] Tender participation and any exclusions
- [ ] Debarment / exclusion list checks

Sources: TED (Tenders Electronic Daily) for EU public procurement; USAspending.gov
and the Federal Procurement Data System for US federal awards, with SAM.gov for
registration and exclusion status; the UK's Contracts Finder and Find a Tender
services; and the World Bank's list of debarred firms and individuals for
multilateral projects. Many national portals publish to the Open Contracting Data
Standard, which makes cross-country comparison feasible.

Why this matters: an award record is third-party-verified revenue. It is the
strongest evidence of real operations available for free.

## G. Sanctions, PEP, and adverse media

- [ ] Entity screened against sanctions lists
- [ ] Every parent, subsidiary, and named individual screened separately
- [ ] PEP status of principals and their close associates considered
- [ ] Ownership-control sanctions exposure considered — an entity majority-owned by a sanctioned person can be caught even if not itself listed
- [ ] Adverse media searched in the local language of each jurisdiction in the chain
- [ ] Search terms, sources, and date recorded so the negative is evidential

Publishers: OFAC's sanctions list search for US designations, the EU consolidated
financial sanctions list, the UK sanctions list, and the UN Security Council
consolidated list. OpenSanctions aggregates these plus PEP datasets across
jurisdictions. OCCRP Aleph indexes leaks, registries, and documents for
investigative work.

## H. Digital and operational reality

- [ ] Domain portfolio and registration dates versus the corporate timeline
- [ ] Infrastructure shared with other brands under the same operator
- [ ] Physical premises evidence — imagery, mapping, delivery listings
- [ ] Sectoral licences and permits the business would need to operate lawfully
- [ ] Trademark holdings and which entity holds them (USPTO, EUIPO, and the WIPO Global Brand Database)
- [ ] Breach exposure of the corporate email domain

## I. Gaps register

For every unchecked or uncheckable item, record: what you wanted, which source
would hold it, why you could not get it (closed register, paid access, no
coverage, language), and what the residual risk is. This section is the part of a
diligence report that a reviewer actually reads.

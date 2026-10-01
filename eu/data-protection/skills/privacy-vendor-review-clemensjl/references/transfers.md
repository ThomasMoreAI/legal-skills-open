# Question 4 — Chapter V transfers

A transfer needs a mechanism before it happens. Art 44 GDPR: a transfer to a third country or international organisation may take place only if the conditions of Chapter V are complied with, **including for onward transfers**. The order is fixed: adequacy (Art 45) → appropriate safeguards (Art 46) → derogations (Art 49), the last being exceptional.

Status as at 2026-08-05. Everything below was read from the primary instrument or the issuing authority's page on that date.

## When is there a transfer at all

**EDPB Guidelines 05/2021 on the interplay between the application of Art 3 and Chapter V, Version 2.0, adopted 14.02.2023.** The GDPR does not define "transfer"; the EDPB supplies three **cumulative** criteria:

1. A controller or processor ("exporter") is subject to the GDPR for the given processing.
2. The exporter discloses by transmission or otherwise makes personal data available to another controller, joint controller or processor ("importer").
3. The importer is in a third country, **irrespective of whether that importer is itself subject to the GDPR under Art 3**, or is an international organisation.

Four consequences that decide most vendor cases:

- **A third-party tag on your site is a transfer.** The guidelines state that personal data disclosed via cookies are "not considered as being disclosed directly by the data subject, but rather as a transmission by the operator of the website that the data subject is visiting". You are the exporter for every third-country tag your page loads.
- **A data subject filling in a non-EU webshop's form directly is not a transfer** — there is no exporter. But that webshop, if caught by Art 3(2), must then apply Chapter V to *its* onward disclosures.
- **Remote access is a transfer**, "even if it takes place only by means of displaying personal data on a screen, for example in support situations, troubleshooting or for administration purposes". "Our data is in Frankfurt" answers nothing on its own.
- **Internal processing in your own foreign branch is not a transfer** (no second controller or processor) — but Chapter V then shields nothing, so Arts 5, 24 and 32 have to carry the risk.

## Adequacy decisions in force — Art 45

Commission adequacy-decisions page, read 2026-08-05: Andorra, Argentina, **Brazil**, Canada (commercial organisations), Faroe Islands, Guernsey, Israel, Isle of Man, Japan, Jersey, New Zealand, Republic of Korea, Switzerland, the United Kingdom (GDPR and LED), the United States (commercial organisations participating in the EU-US Data Privacy Framework), Uruguay, and the **European Patent Organisation**. With the exception of the United Kingdom, these decisions do not cover data exchanges in the law-enforcement sector.

Scope limits that change the answer:

| Territory | Limit |
|---|---|
| Canada | Decision 2002/2/EC — commercial organisations subject to PIPEDA only |
| Japan | Decision (EU) 2019/419 — only "personal information handling business operators" subject to the APPI **as complemented by the Supplementary Rules in Annex I**; press, professional writers, universities and religious bodies carved out for certain purposes. Review 04.04.2023 |
| Israel | Decision 2011/61/EU Art 1(1) — only **automated** international transfers, or non-automated data subject to further automated processing in Israel |
| Republic of Korea | PIPA plus Supplementary Rules. Review concluded 23.07.2026, COM(2026) 384 final; positive; cycle moved from three to four years |
| United States | Implementing Decision (EU) 2023/1795 of 10.07.2023 — **only organisations on the DPF List** |
| European Patent Organisation | C(2025) 4626 final of 15.07.2025 — the first adequacy finding for an international organisation |
| Brazil | C(2026) 373 final of **26.01.2026** — controllers and processors in Brazil **subject to the LGPD**. No sunset; first evaluation four years after notification. Brazil adopted a reciprocal decision for the EU |
| United Kingdom | Renewed by C(2025) 8771 final (GDPR) and C(2025) 8782 final (LED) of **19.12.2025**, both expiring **27.12.2031**. The renewal **repealed Art 1(2) of Decision (EU) 2021/1772**, removing the immigration-control carve-out |

The **eleven pre-GDPR decisions** (Andorra, Argentina, Canada, Faroe Islands, Guernsey, Isle of Man, Israel, Jersey, New Zealand, Switzerland, Uruguay) were **not renewed** in 2024 — the Commission completed the first periodic review and concluded they continue to hold: **COM(2024) 7 final of 15.01.2024** with country reports in SWD(2024) 3 final. The original instruments remain the operative acts.

**Kenya has no adequacy decision** and none appears on the Commission's pages. Do not assert a process.

Adequacy removes the Art 46 safeguard for transfers to that territory. It does not remove the ROPA entry, the notice entry, or the need to check where the recipient's own sub-processors sit.

## EU-US Data Privacy Framework

Adequacy attaches only to organisations on the DPF List and only within their certified scope.

**How to check a vendor properly.** List: `dataprivacyframework.gov/list`, administered by the International Trade Administration, US Department of Commerce.

1. Take the **exact contracting legal entity** from the invoice or order form. A parent's certification does not automatically cover a subsidiary — check the record's "Other Covered U.S. Entities and U.S. Subsidiaries" section.
2. The results table shows one row **per framework**, with STATUS and COVERED DATA (HR Data / Non-HR Data). Observed statuses include "Active" and "Active - Re-certification under Review"; the latter means the annual re-certification is filed and being processed, and the organisation is still a participant. The list has explicit Active and Inactive toggles.
3. **Three separate frameworks — never conflate them:** the **EU-U.S. DPF** (EU/EEA data, effective 10.07.2023); the **UK Extension** (UK and Gibraltar, effective 12.10.2023, and participation in the EU-U.S. DPF is a precondition); the **Swiss-U.S. DPF** (Principles effective 17.07.2023, but transfers lawful only from **15.09.2024**, when Switzerland's recognition entered into force). A company Active only under the EU-U.S. DPF cannot receive UK or Swiss data on that basis.
4. Record the entity name, framework rows, status, covered-data scope and **the date you checked**.
5. ITA removes organisations that withdraw, fail annual re-certification or persistently fail to comply, and maintains a record of removals. A removed organisation must stop claiming participation but **must continue to apply the DPF Principles to data received while participating**.
6. Sub-processors of a certified importer are covered only if they are themselves certified or covered by an onward-transfer safeguard.

**Current legal position.** The framework is valid and usable, but under pressure:

- **General Court, 03.09.2025, T-553/23 Latombe v Commission, ECLI:EU:T:2025:831 — action dismissed.** The Court held that EO 14086 cures the Schrems II Ombudsperson defects (limits on dismissal of Data Protection Review Court judges, binding decisions), that the DPRC need not be an Article III court, and that bulk collection outside the US is permitted only where a validated intelligence priority cannot reasonably be achieved by targeted collection. Legality was assessed **solely on the information available on 10.07.2023**, which is why later events did not affect the outcome.
- **Appeal pending: Case C-703/25 P, Latombe v Commission**, lodged 31.10.2025, status "Pending" as at 2026-08-05. `[[UNVERIFIED: an Order of 04.06.2026, ECLI:EU:C:2026:465, sits on the file but is not published; treat it as procedural unless confirmed]]`
- **PCLOB has no quorum.** Its own board page listed exactly one sitting member on 2026-08-05. The statutory board is five members with a three-member quorum. EO 14086 and the DPRC rule (28 CFR Part 201) are both intact and unamended.
- On **29.06.2026** the US Supreme Court held in **Trump v. Slaughter** that the FTC cannot be constitutionally independent. noyb reports that the 2023 adequacy decision relies on the "independent" FTC 259 times, and on the **same day, 29.06.2026, sent a formal letter to the Commission** asking it to repeal the decision "in an orderly way" with transition periods; it announced an annulment action before the CJEU "in the coming weeks" (`noyb.eu`, advocacy source that publishes the underlying documents). **Re-checked 2026-08-05: no filing confirmed.** noyb's own newsroom shows nothing after 29.06.2026 and no case number appears on CURIA. Do not describe the action as pending.
- **The EDPB has asked the Commission to assess the ruling.** Letter of **31.07.2026 to Commissioner Michael McGrath** (Democracy, Justice, Rule of Law and Consumer Protection), asking the Commission to "closely assess" the effect of *Trump v. Slaughter* on the FTC's ability to uphold its DPF commitments; Chair Anu Talus frames independent supervisory authorities as "one of the key elements to be taken into account when assessing the adequacy of the level of protection". `[[UNVERIFIED: the letter itself — reported by IAPP on 2026-08; edpb.europa.eu was relaunched in June 2026 and its correspondence index returns 404, so the text was not read. Confirm on edpb.europa.eu before quoting it in a filing]]`
- **The Commission has not acted.** Its EU-US data transfers page, read 2026-08-05, still describes the 10.07.2023 decision without any 2026 addendum, review notice or suspension. **Only one periodic review has taken place: COM(2024) 451 final of 09.10.2024**, which concluded the US authorities had put the necessary structures in place, and flagged PCLOB appointments as a thing to watch — written before the January 2025 removals. It set the next review after three years. No second review as at 2026-08-05.

**The decision is in force.** It stays in force until the Commission repeals it or the Court of Justice annuls it — noyb says so itself. Anyone writing "the DPF has fallen" is wrong. What has changed is the risk profile, not the legal basis.

**Practical posture:** DPF alone is no longer a defensible sole basis. Record the DPF finding **and a documented Art 46(2)(c) SCC fallback plus a transfer impact assessment** for every US importer you rely on. Where the vendor also offers SCCs — most do — note that they are in place, so an adequacy withdrawal becomes a paperwork event rather than a shutdown. In the TIA, note that the FTC-independence and PCLOB-quorum questions go to *redress and oversight*, which is precisely where the standard US supplementary-measures argument is weakest.

## Standard contractual clauses — Art 46(2)(c)

**Commission Implementing Decision (EU) 2021/914 of 4 June 2021.** Art 1(1) scope: transfer by an exporter processing subject to the GDPR to a controller or (sub-)processor **whose processing is not subject to the GDPR**. Art 1(2): for controller→processor and processor→sub-processor the clauses also discharge Art 28(3) and (4).

| Module | Relationship | Typical case |
|---|---|---|
| **One** | Transfer controller to controller | Ad platform receiving data for its own purposes; a payment provider's fraud slice |
| **Two** | Transfer controller to processor | The normal SaaS case |
| **Three** | Transfer processor to processor | You are a processor for your customers and pass data to a sub-processor |
| **Four** | Transfer processor to controller | Rare: an EEA processor returns data to a non-EEA controller |

**The old sets are dead.** Art 4 of Decision 2021/914 repealed Decisions 2001/497/EC and 2010/87/EU with effect from **27.09.2021**; contracts concluded before that date were deemed to provide appropriate safeguards only **until 27.12.2022**, and only while the processing operations remained unchanged. Any contract still citing "the 2010 SCCs" is a finding.

Checks that catch real errors:

- The module must match the role finding from `role-determination.md`.
- **Annexes must be populated**: Annex I (parties, description of the transfer, competent supervisory authority), Annex II (technical and organisational measures), Annex III (sub-processors). "Deemed signed by acceptance of the terms" handles execution, not the annexes — find where the vendor puts them.
- Clause 7 docking clause: note whether it was adopted.
- Clause 14 is the contractual hook for the transfer impact assessment.
- Clauses 17 and 18: governing law and forum must be an EU Member State's. Clause 2: the clauses may not be amended.

**The Art 3(2) gap is still open.** The Commission's SCC page (read 2026-08-05) still says it "is in the process of developing" additional sets, including for transfers to controllers or processors outside the EU whose processing is **directly subject to the GDPR**. **Not adopted.** There is therefore no Commission-approved transfer tool purpose-built for an Art 3(2) importer; in practice the 2021 SCCs are used with the overlap acknowledged and the reasoning documented. Re-check that page — this is the most likely instrument to appear next.

Do not confuse the transfer SCCs with **Commission Implementing Decision (EU) 2021/915 of 4 June 2021**, which provides Art 28(7) controller-processor clauses for use inside the EU. See `processor-contract.md`.

## Transfer impact assessment

Required by CJEU 16.07.2020, **C-311/18 Schrems II**. Method: **EDPB Recommendations 01/2020 on measures that supplement transfer tools, Version 2.0, adopted 18.06.2021.** Six steps:

1. **Know your transfers** — map them, including onward transfers; verify data minimisation.
2. **Identify the transfer tools you are relying on** — under Art 45, only monitor the decision's continued validity; otherwise Art 46. Art 49 derogations "cannot become 'the rule' in practice".
3. **Assess whether the Art 46 tool is effective in light of all circumstances of the transfer** — law **and** practice. Three trigger situations: (i) law formally meeting EU standards but manifestly not applied in practice; (ii) practices incompatible with the transfer tool where legislation is lacking; (iii) your data or your importer fall, or might fall, within problematic legislation. In (i) and (ii) you must suspend or add measures. In (iii) you may proceed without supplementary measures only if you can **demonstrate and document** that you have no reason to believe the problematic law will be applied to your transfer.
4. **Adopt supplementary measures.** Annex 2 splits them into technical, additional contractual and organisational. If none suffice, "you must avoid, suspend or terminate the transfer".
5. **Procedural steps** where effective supplementary measures were identified — e.g. Art 46(3)(a) authorisation where ad hoc clauses are amended.
6. **Re-evaluate at appropriate intervals.**

Yardstick for step 3 where government access is in play: **EDPB Recommendations 02/2020 on the European Essential Guarantees for surveillance measures, adopted 10.11.2020.** Four guarantees: (A) processing based on clear, precise and accessible rules; (B) demonstrated necessity and proportionality against the legitimate objectives; (C) an independent oversight mechanism; (D) effective remedies available to the individual.

Supplementary measures, ranked by what actually works:

| Measure | Effect |
|---|---|
| Do not transfer; keep the processing in the EEA | Removes the problem |
| Strong encryption, keys held only in the EEA, importer never holds plaintext | Effective where it genuinely holds; useless where the importer must process plaintext |
| Pseudonymisation where the importer cannot re-identify and holds no additional information | Same condition |
| Split or multi-party processing | Situational |
| Transparency reports, government-request policies, challenge commitments | Organisational; they help, but do not cure a legal power to compel |

Name the specific law — for the US: FISA § 702, EO 12333, the CLOUD Act — assess whether the importer falls within its scope, and state what the measures do about it. "The vendor is large and has good security" is not a TIA.

## Art 49 derogations

Occasional, non-repetitive, narrow. Explicit consent after being informed of the risks (a); necessity for a contract with the data subject (b); important reasons of public interest (d); legal claims (e). The compelling-legitimate-interests derogation in the second subparagraph requires notifying the supervisory authority and documenting the safeguards. **A recurring vendor integration is not an Art 49 case.** EDPB Guidelines 2/2018 set the interpretation.

## UK and Switzerland

**UK** — ICO international transfers guidance, last updated 15.01.2026:

- Two ICO instruments: the **International Data Transfer Agreement (IDTA)** and the **International Data Transfer Addendum to the EU SCCs**. Current versions: **IDTA template A.1.0** and **Addendum template B.1.0**, both laid before Parliament under s119A Data Protection Act 2018 on **02.02.2022**.
- "The EU SCCs are **not valid on their own** for restricted transfers under the UK GDPR. However, using the Addendum lets you rely on the EU SCCs."
- ICO: "We plan to update the IDTA and Addendum in the course of 2026. **You should continue to use the current versions.**" Auto-update on new versions is available via IDTA Section 5.4 / Addendum Section 18.
- The transfer risk assessment is now, under the Data (Use and Access) Act, referred to in legislation as the **"data protection test"**. Standard: acting reasonably and proportionately, that the standard of protection is **not materially lower** than in the UK after the transfer. TRAs completed under the older ICO guidance that concluded protection was sufficient are treated as meeting the test. The ICO publishes a TRA tool and a separate route using the UK government's US analysis.

**Switzerland** — revised FADP (SR 235.1) and DPO (SR 235.11) in force since **01.09.2023**; the obligation to notify use of recognised standard clauses fell away on that date.

- The Swiss adequacy list is **Annex 1 DPO, Art 8(1)** — 44 entries, amended 14.08.2024 in force 15.09.2024. It includes all EU/EEA states individually plus Andorra, Argentina, Canada, Faroe Islands, **Gibraltar**, Guernsey, Isle of Man, Israel, Jersey, **Monaco**, New Zealand, United Kingdom, Uruguay and the United States for organisations certified under the Swiss-US framework. **Japan, the Republic of Korea and Brazil are not on the Swiss list.** The EU and Swiss lists are not interchangeable.
- The FDPIC recognises the EU SCCs **including all modules**, subject to case-specific adaptation (FDPIC guidance published 27.08.2021, last amended 12.02.2025). Required amendments for FADP-governed transfers: the **FDPIC is the competent supervisory authority** and this cannot be contracted around; Clause 17 governing law must be Swiss law or a law granting third-party-beneficiary rights; Clause 18(b) forum is freely choosable; "Member State" must not be read so as to deny Swiss data subjects a forum in Switzerland; references to the GDPR are read as references to the FADP. Where both regimes apply, either run them in parallel or apply the GDPR standard to everything — but SCCs governing GDPR transfers may not be amended. The old requirement to extend protection to data of legal persons has fallen away; the revised FADP covers natural persons only.

## Transfer record

```
Transfer — [[VENDOR]] / [[exact entity]]
Exporter:            [[your entity]]
Importer:            [[entity]], [[country]]
Onward recipients:   [[sub-processors + countries]]
Basis:               [[Art 45 adequacy: name the decision | Art 46(2)(c) SCCs Module [[One–Four]], dated … | Art 49(1)(…)]]
DPF (if claimed):    entity [[…]]  frameworks [[EU / UK Extension / Swiss]]  status [[…]]  covered data [[HR / non-HR]]  checked [[date]]
Annexes:             I [[complete?]]  II [[complete?]]  III [[complete?]]
Remote access:       [[countries staff can access from]]
TIA:                 [[reference]], dated [[date]], laws assessed [[FISA 702 / EO 12333 / CLOUD Act / …]]
Supplementary:       [[measures, or justified absence]]
UK / CH:             [[IDTA A.1.0 | Addendum B.1.0 | FDPIC-amended SCCs | not in scope]]
Re-evaluation due:   [[date]] (Recommendations 01/2020 step 6)
```

## Checkpoints

- [ ] Every country of processing identified, including support, on-call and administrative remote access
- [ ] Third-party tags treated as transfers by **you** as exporter, per Guidelines 05/2021
- [ ] Mechanism named per recipient and per onward recipient
- [ ] Adequacy claims checked against the current Commission list, with the scope limit noted
- [ ] DPF: exact entity, framework rows, status and covered-data scope checked on `dataprivacyframework.gov/list`, with the check date
- [ ] UK and Swiss DPF coverage checked separately from the EU one
- [ ] DPF reliance paired with a documented fallback
- [ ] SCC module matches the role finding; annexes I, II and III populated
- [ ] No contract relying on the repealed 2001 or 2010 SCCs
- [ ] TIA completed to the six steps of Recommendations 01/2020 v2.0, naming the specific third-country laws, and assessed against the four European Essential Guarantees
- [ ] Art 49 not used for a recurring integration
- [ ] UK instruments (IDTA A.1.0 / Addendum B.1.0) and the Swiss FDPIC amendments applied where those data subjects are in scope
- [ ] Re-evaluation date set (step 6)

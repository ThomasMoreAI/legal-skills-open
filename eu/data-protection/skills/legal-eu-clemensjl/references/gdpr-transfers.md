# International transfers — GDPR Chapter V

Status as at 2026-08-05.

Chapter V (Arts 44–50) of Regulation (EU) 2016/679. A Regulation: the rules are identical in all member states. What differs nationally is the supervisory authority that enforces them and, in a few states, additional notification practice.

Art 44 sets the frame: any transfer of personal data to a third country or international organisation may take place **only if** the conditions in Chapter V are met, including for onward transfers. The chapter is applied so that the level of protection guaranteed by the GDPR is not undermined.

A transfer happens whenever data becomes accessible from outside the EEA. Remote access by a support engineer in a third country is a transfer. So is storage on EEA servers operated by a controller subject to third-country access powers, in the sense that it needs the same analysis.

## Order of analysis

1. **Art 45 adequacy** — is the destination covered by an adequacy decision? If yes, no further authorisation is needed.
2. **Art 46 appropriate safeguards** — SCCs, BCRs, code of conduct, certification. Requires enforceable data subject rights and effective legal remedies, and in practice a transfer impact assessment.
3. **Art 49 derogations** — narrow, situational, not a basis for routine transfers.

Never jump to Art 49 for ordinary vendor relationships. The EDPB treats the derogations as exceptions for occasional, non-repetitive transfers.

## Art 45 — adequacy decisions in force

Verified against the Commission's adequacy-decisions page, 05.08.2026:

Andorra, Argentina, **Brazil (adopted February 2026, mutual)**, Canada (commercial organisations), Faroe Islands, Guernsey, Israel, Isle of Man, Japan, Jersey, New Zealand, Republic of Korea, Switzerland, **United Kingdom (renewed December 2025, under both the GDPR and the Law Enforcement Directive)**, United States (EU-US Data Privacy Framework), Uruguay, and the **European Patent Organisation (July 2025)**.

The Commission confirmed in **July 2026** that the Republic of Korea continues to provide an adequate level of protection, following the first periodic review.

Two of these moved recently. A privacy notice written before December 2025 that describes UK transfers as covered by a decision "due to expire" is stale; a notice that lists Brazil as a third country requiring SCCs may now be wrong.

## The EU-US Data Privacy Framework — status

Commission Implementing Decision **(EU) 2023/1795 of 10.07.2023**. It succeeded the Privacy Shield, which the CJEU invalidated in **Schrems II, Case C-311/18, judgment of July 2020**.

Litigation history, verified:

- **Case T-553/23 Latombe v Commission.** The General Court **dismissed** the annulment action on **03.09.2025**, holding that the Data Protection Review Court offers sufficient guarantees of independence and impartiality under Art 47 of the Charter, and that bulk collection subject to ex post judicial review meets the Schrems II standard.
- Latombe **appealed to the Court of Justice on 31.10.2025, Case C-703/25 P**. Still pending as at 05.08.2026; no hearing date announced.

**Trump v. Slaughter changed the risk, not the law.** On **29.06.2026** the US Supreme Court held that the FTC's statutory removal protections are unconstitutional — the FTC cannot be an independent agency. Decision (EU) 2023/1795 relies on that independence throughout: the FTC is the enforcement authority for the DPF Principles against certified commercial organisations, and independent supervision is a component of the Art 45(2)(b) adequacy test. What has followed, as at 05.08.2026:

- **noyb letter to the Commission, 29.06.2026**, asking for an orderly repeal with transition periods; an annulment action was announced but no filing is confirmed and no case number appears on CURIA.
- **EDPB letter to Commissioner McGrath, 31.07.2026**, asking the Commission to "closely assess" the ruling's effect on the FTC's ability to uphold its DPF commitments. `[[UNVERIFIED: the letter text — reported by IAPP; edpb.europa.eu was relaunched in June 2026 and its correspondence index returns 404]]`
- **No Commission act.** The EU-US data transfers page carries no 2026 review, suspension or amendment. Art 45(5) suspension would require an implementing act; none exists.

Practical position: **the DPF is valid and usable today** and stays valid until the Commission repeals it or the Court annuls it. Do not write that it "has fallen". It is also the transfer basis most likely to be removed by a court within the life of any document being written now. Three rules follow:

- Only use the DPF for a recipient that is **actually certified** for the relevant data type. Certification is per organisation and covers HR data or non-HR data separately — check the DPF list, do not assume.
- Have SCCs in the same contract as a fallback, or a contractual clause that switches to SCCs automatically if the adequacy decision is annulled or suspended. Do not build a stack whose only US transfer basis is the DPF.
- Since 29.06.2026 the fallback must be **documented, not merely available**: SCCs (Art 46(2)(c)) on file, plus a transfer impact assessment per Schrems II that addresses oversight and redress specifically. That is the limb the FTC ruling weakens, and it is the limb a supervisory authority will ask about.

## Art 46 — standard contractual clauses

Commission Implementing Decision **(EU) 2021/914 of 04.06.2021**. Four modules: controller-to-controller, controller-to-processor, processor-to-processor, processor-to-controller. Pick the module that matches the actual relationship; using the wrong module is a common and visible error. The 2021 SCCs replaced the three pre-GDPR sets, which have had no legal effect since 27.12.2022.

The Commission has announced further sets — for transfers by EU institutions, and for transfers to importers whose processing already falls directly under the GDPR by Art 3(2). Neither is in force as at 05.08.2026; the gap for Art 3(2)-covered importers persists.

Art 46(2) safeguards that need **no** supervisory authority authorisation: legally binding instrument between public authorities (a); binding corporate rules under Art 47 (b); Commission SCCs (c); SCCs adopted by a supervisory authority and approved by the Commission (d); approved code of conduct with binding commitments (e); approved certification mechanism with binding commitments (f).

Art 46(3) safeguards that **do** need authorisation: ad hoc contractual clauses (a); provisions in administrative arrangements between public authorities (b).

## Transfer impact assessment

Signing SCCs is not sufficient on its own. Under Schrems II the exporter must assess whether the law and practice of the destination country prevent the importer from complying, and must add supplementary measures where it does.

**EDPB Recommendations 01/2020 on measures that supplement transfer tools, final version adopted 18.06.2021**, sets out the method: map the transfers; identify the transfer tool; assess the third country's law and practice; adopt supplementary measures; take the procedural steps for those measures; re-evaluate at intervals.

Document the assessment. An undocumented TIA is treated as no TIA.

## Art 48 — foreign authority requests

A judgment or administrative decision of a third-country authority requiring a controller or processor to transfer or disclose personal data is recognisable or enforceable only on the basis of an international agreement, such as a mutual legal assistance treaty, without prejudice to the other grounds in Chapter V.

**EDPB Guidelines 02/2024 on Art 48 GDPR** were put to public consultation from 03.12.2024 to 27.01.2025. [[UNVERIFIED: whether a final version has been adopted and its date — check edpb.europa.eu before citing a final version]]

Practical effect: a subpoena or preservation order from a non-EU authority does not by itself authorise disclosure. This is the clause that a US-parent vendor's standard terms most often ignore.

## Art 49 — derogations

Available only where neither Art 45 nor Art 46 applies:

- (a) the data subject explicitly consented **after having been informed of the possible risks** of the transfer
- (b) necessary for performance of a contract between the data subject and the controller
- (c) necessary for the conclusion or performance of a contract concluded in the data subject's interest
- (d) necessary for important reasons of public interest
- (e) necessary for the establishment, exercise or defence of legal claims
- (f) necessary to protect vital interests where the data subject is incapable of giving consent
- (g) made from a public register

Second subparagraph of Art 49(1): a residual derogation for transfers that are **not repetitive**, concern only a **limited number** of data subjects, are necessary for compelling legitimate interests of the controller not overridden by the data subject's interests, and are accompanied by suitable safeguards. The controller must inform the supervisory authority and the data subject of the transfer and of the compelling legitimate interests pursued.

None of these supports "we use a US analytics tool because users consented to cookies". Cookie consent is not Art 49(1)(a) consent.

## Template — transfers section of a privacy notice

```html
<!-- DRAFT – NOT LEGALLY APPROVED -->
<h2>Transfers outside the European Economic Area</h2>
<p>
  Some of our processors are located outside the EEA. For each of them we
  identify the legal basis for the transfer:
</p>
<table>
  <thead>
    <tr><th>Recipient</th><th>Country</th><th>Purpose</th><th>Transfer basis</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>[[PROVIDER]]</td><td>[[COUNTRY]]</td><td>[[PURPOSE]]</td>
      <td>[[Adequacy decision (EU) …/… | EU-US Data Privacy Framework certification,
          certified for [[HR / non-HR]] data | Standard contractual clauses,
          Implementing Decision (EU) 2021/914, Module [[…]], plus supplementary
          measures: [[…]] ]]</td>
    </tr>
  </tbody>
</table>
<p>
  You can obtain a copy of the safeguards we rely on by contacting
  [[CONTACT]] (Art 46(1) GDPR).
</p>
```

## Checkpoints

- [ ] Every recipient outside the EEA listed individually, with country and transfer basis
- [ ] Adequacy claims checked against the Commission list as at the drafting date — UK renewed 12/2025, Brazil added 02/2026
- [ ] DPF relied on only for recipients actually on the certification list, and for the right data category
- [ ] A fallback transfer basis exists for every DPF-based transfer
- [ ] SCC module matches the real relationship (C2C / C2P / P2P / P2C)
- [ ] Pre-GDPR SCCs (2001/2004/2010 sets) not in use anywhere — void since 27.12.2022
- [ ] Transfer impact assessment written and dated per destination, following EDPB Recommendations 01/2020
- [ ] Supplementary measures named concretely, not "we use encryption"
- [ ] Onward transfers by the importer addressed (Art 44)
- [ ] Art 49 not used as a standing basis for routine vendor transfers
- [ ] Remote access from a third country recognised as a transfer
- [ ] Foreign authority disclosure clauses in vendor terms checked against Art 48
- [ ] Data subjects told how to obtain a copy of the safeguards (Art 13(1)(f), Art 46(1))
- [ ] All `[[…]]` placeholders resolved or reported as open

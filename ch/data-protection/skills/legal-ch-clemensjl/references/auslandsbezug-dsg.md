# Representatives and transfers abroad

Two distinct cross-border questions, both routinely mishandled. First, who must appoint a representative — the duty runs in both directions. Second, on what basis data may leave Switzerland. Wording from DSG Stand am 7. Juli 2025 and DSV Stand am 1. Dezember 2025. Status as at 2026-08-05.

## Swiss representative for foreign controllers — Art. 14, 15 DSG

> Art. 14 Abs. 1 DSG: Private Verantwortliche mit Sitz oder Wohnsitz im Ausland bezeichnen eine Vertretung in der Schweiz, wenn sie Personendaten von Personen in der Schweiz bearbeiten und die Datenbearbeitung die folgenden Voraussetzungen erfüllt:
> a. Die Bearbeitung steht im Zusammenhang mit dem Angebot von Waren und Dienstleistungen oder der Beobachtung des Verhaltens von Personen in der Schweiz.
> b. Es handelt sich um eine umfangreiche Bearbeitung.
> c. Es handelt sich um eine regelmässige Bearbeitung.
> d. Die Bearbeitung bringt ein hohes Risiko für die Persönlichkeit der betroffenen Personen mit sich.

All four conditions are **cumulative**. This is materially narrower than Art. 27 GDPR, which starts from the opposite premise and exempts only occasional low-risk processing. A small foreign shop selling into Switzerland normally fails condition b or d and needs no Swiss representative.

Art. 14 Abs. 2 DSG: the representative serves as the contact point for data subjects and for the EDÖB. Abs. 3: the controller publishes the name and address of the representative — in practice in the Datenschutzerklärung.

Art. 15 DSG: the representative keeps a register of the controller's processing activities containing the Art. 12 Abs. 2 particulars, communicates those particulars to the EDÖB on request, and tells data subjects on request how to exercise their rights.

There is no equivalent duty for processors, and no duty to notify the EDÖB of the appointment; notification is voluntary.

## EU representative for Swiss controllers — Art. 27 GDPR

The mirror case. Where Art. 3(2) GDPR applies — offering goods or services to data subjects who are in the Union, irrespective of payment, or monitoring their behaviour in the Union — the controller or processor **shall designate in writing a representative in the Union** (Art. 27(1) GDPR). The exemption in Art. 27(2)(a) GDPR covers processing that is occasional, does not include large-scale processing of Art. 9(1) or Art. 10 data, and is unlikely to result in a risk to rights and freedoms. Art. 27(3) GDPR: the representative must be established in a Member State where the relevant data subjects are.

A Swiss shop with a German-language checkout, EUR prices and delivery to Germany is squarely in Art. 3(2)(a) GDPR. Being outside the EU changes nothing. The representative's name and address belong in the Datenschutzerklärung.

Being in the Swiss adequacy list does not remove the Art. 27 duty, and the EU adequacy decision for Switzerland does not either — adequacy governs transfers *into* Switzerland, not applicability of the GDPR to Swiss controllers.

## Transfers abroad — Art. 16, 17 DSG

Art. 16 Abs. 1 DSG: data may be disclosed abroad where the Federal Council has determined that the legislation of the state concerned, or the international body, guarantees adequate protection. Abs. 2 lists the substitutes where no such decision exists:

- a. an international treaty
- b. data protection clauses in a contract between the controller or processor and its counterparty, **notified to the EDÖB in advance**
- c. specific safeguards drawn up by the competent federal body and notified to the EDÖB in advance
- d. standard data protection clauses previously approved, issued or recognised by the EDÖB
- e. binding corporate rules previously approved by the EDÖB or by an authority of a state with adequate protection

Art. 17 DSG lists the exceptions for individual cases: express consent; direct connection with the conclusion or performance of a contract; overriding public interest or legal claims; protection of life or physical integrity; data made generally accessible by the data subject without express objection; data from a statutory register open to inspection.

Art. 8 DSV governs the adequacy assessment and states that adequate states are listed in **Anhang 1 DSV**. The list is periodically reassessed (Abs. 4) and amended if adequacy falls away (Abs. 6). Art. 10 Abs. 2 DSV: the EDÖB publishes a list of standard clauses it has approved, issued or recognised, and communicates the result of examining submitted clauses within 90 days.

**Practical consequence.** Art. 16 Abs. 2 lit. d DSG is the ordinary route. Bespoke contractual clauses under lit. b must be notified to the EDÖB *before* the transfer — a step that is almost always overlooked when a template contract is signed with a US vendor.

## The adequacy list

Anhang 1 DSV names states, territories, specific sectors and international bodies. It includes all EEA states, the United Kingdom, and a set of third countries such as Andorra, Argentina, Canada (with the sector qualification set out in the annex), the Faroe Islands, Gibraltar, Guernsey, the Isle of Man, Israel, Jersey, Monaco, New Zealand and Uruguay. Read the current annex before asserting any single entry — the list is amended by ordinance and entries carry qualifications in the annex's right-hand column.

## Swiss-US Data Privacy Framework

Anhang 1 DSV lists the United States with a sector qualification: adequate protection is deemed guaranteed for personal data processed by organisations **certified under the principles of the Swiss-US Data Privacy Framework**, on the basis of Executive Order 14086 of 7 October 2022, the Attorney General's regulation on the Data Protection Review Court of 7 October 2022, Intelligence Community Directive 126 of 6 December 2022, and the designation of Switzerland on **7 June 2024** as a state benefiting from the two-tier redress mechanism including access to the Data Protection Review Court.

The annex entry was inserted by the ordinance of 14 August 2024, **in force since 15 September 2024** (AS 2024 435). Before that date there was no US adequacy under Swiss law after the Privacy Shield fell.

Two traps. The recognition is **certification-specific**, not country-wide: it covers only recipients actually certified under the Swiss-US DPF, and certification under the EU-US DPF alone does not carry over. And the Swiss recognition date differs from the EU's — do not reuse an EU-drafted transfer register entry unchanged.

**Trump v. Slaughter, 29.06.2026 — do not reason by analogy from the EU debate.** The US Supreme Court held that the FTC's statutory removal protections are unconstitutional. In the EU this triggered an EDPB letter to the Commission (31.07.2026) asking it to assess the effect on Decision (EU) 2023/1795. Switzerland is a separate legal act: the US entry in Anhang 1 DSV was made by the Bundesrat and can only be removed by the Bundesrat by ordinance. As at **05.08.2026 no Swiss reaction was found** — no ordinance amendment, no EDÖB statement on the ruling. `[[UNVERIFIED: whether the EDÖB or the Bundesrat has since taken a position — this is absence of evidence from a search on 05.08.2026, not a verified negative. Check edoeb.admin.ch and the AS before telling a client that Switzerland has taken none]]`

The practical consequence is the same as under the GDPR, and it applies to the Swiss-US DPF for the same reason — the FTC is the enforcement body behind the Principles: **do not rely on the DPF entry alone.** Have EDÖB-adapted SCCs on file as a fallback for every US recipient, and document the assessment. Anhang 1 DSV remains in force in the meantime; do not tell a client the Swiss recognition has lapsed.

## EU standard contractual clauses

The EDÖB has recognised the EU Standard Contractual Clauses for use under Art. 16 Abs. 2 lit. d DSG, alongside the Council of Europe model clauses. Guidance document "Die Übermittlung von Personendaten in ein Land ohne angemessenes Datenschutzniveau gestützt auf Standarddatenschutzklauseln nach Art. 16 Abs. 2 lit. d DSG", published 27.08.2021, **last amended 12.02.2025** — read in full on 05.08.2026. Recognition covers **all four modules** but is expressly subject to adaptation in the individual case. The required adaptations:

| Point | Transfer under the DSG only | Transfer under DSG **and** GDPR |
|---|---|---|
| Supervisory authority, Annex I.C / Clause 13 | **EDÖB, mandatorily** — its competence follows from the DSG and survives any contrary choice by the parties | Parallel: EDÖB for the DSG part, an EU authority for the GDPR part. Naming only an EU authority is wrong |
| Governing law, Clause 17 | Swiss law, or a law that admits and grants third-party-beneficiary rights | Same for the DSG part; the law of an EU Member State for the GDPR part (free choice under Module Four) |
| Forum between the parties, Clause 18(b) | Free choice | Free for the DSG part; a Member State court for the GDPR part |
| Forum for data subjects | Annex must state that "Member State" may not be read so as to exclude data subjects in Switzerland from suing at their habitual residence under Clause 18(c) | Same |
| References to the GDPR | Annex must state that they are to be read as references to the DSG | Same, to the extent the transfer falls under the DSG |

Where both regimes apply the parties may either keep two separate sets of rules or subject everything to the GDPR standard — but SCCs governing a GDPR transfer **may not be amended** (Clause 2).

**There is no longer a requirement to extend the clauses to data of legal persons.** The revised DSG covers natural persons only, and the 12.02.2025 guidance does not mention legal persons anywhere. Any template still carrying that clause is drafting to the pre-2023 DSG.

## Template fragment for the Datenschutzerklärung

```html
<!-- ENTWURF – juristisch nicht freigegeben -->
<h2>Bekanntgabe von Personendaten ins Ausland</h2>
<p>Wir geben Personendaten in folgende Staaten bekannt:</p>
<ul>
  <li>[[Staat]] – Empfänger: [[Anbieter]] – Grundlage: angemessener Datenschutz
      gemäss Anhang 1 DSV</li>
  <li>[[Staat]] – Empfänger: [[Anbieter]] – Grundlage: Standarddatenschutzklauseln
      nach Art. 16 Abs. 2 lit. d DSG</li>
  <li>USA – Empfänger: [[Anbieter]] – Grundlage: Zertifizierung nach dem
      Swiss-US Data Privacy Framework, Anhang 1 DSV</li>
</ul>
<p>Vertretung in der Schweiz nach Art. 14 DSG: [[Name, Adresse]] – oder: entfällt.</p>
<p>Vertretung in der EU nach Art. 27 DSGVO: [[Name, Adresse]] – oder: entfällt.</p>
```

## Checkpoints

- [ ] Art. 14 DSG tested against all four cumulative conditions, and the result recorded
- [ ] Where a Swiss representative is required, name and address are published (Art. 14 Abs. 3 DSG)
- [ ] Art. 3(2) GDPR tested explicitly for the EU-facing offering
- [ ] Where Art. 27 GDPR applies, an EU representative is appointed in writing and named in the notice
- [ ] Every recipient outside Switzerland is listed by state, not only by vendor name
- [ ] Each transfer has a basis under Art. 16 Abs. 1, Art. 16 Abs. 2 or Art. 17 DSG, named in the register and in the notice
- [ ] Bespoke contractual clauses under Art. 16 Abs. 2 lit. b DSG were notified to the EDÖB **before** the transfer started
- [ ] US recipients checked for actual Swiss-US DPF certification, not EU-US DPF only
- [ ] EU SCCs used only with the adaptations the EDÖB requires, verified against its current published list
- [ ] Adequacy list checked against the current Anhang 1 DSV, not from memory

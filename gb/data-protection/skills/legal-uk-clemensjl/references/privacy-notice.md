# Privacy notice

The UK GDPR is the retained EU Regulation as it forms part of UK law, read with the Data Protection Act 2018 and heavily amended by the Data (Use and Access) Act 2025 (c. 18, Royal Assent 19 June 2025). Most of the amendments in Part 5 came into force on 5 February 2026 by the Data (Use and Access) Act 2025 (Commencement No. 6 and Transitional and Saving Provisions) Regulations 2026 (SI 2026/82, made 29 January 2026); s 103 and Sch 10 followed on 19 June 2026.

A notice drafted against the EU GDPR text is wrong on Article 22, Article 77 and the lawful basis list. Check those three before anything else.

## What must be told, UK GDPR Arts 13 and 14

Status as at 2026-08-05.

- identity and contact details of the controller, and of the representative where one is appointed
- contact details of the Data Protection Officer, where one is appointed
- the purposes of each processing operation and the lawful basis for it
- where legitimate interests are relied on, the specific interests pursued
- recipients or categories of recipient
- transfers outside the UK, the mechanism relied on, and how to obtain a copy of the safeguards
- retention period or the criteria used to determine it
- the data subject rights: access, rectification, erasure, restriction, portability, objection
- where processing is based on consent, the right to withdraw it at any time without affecting prior processing
- the right to complain, expressed under the post-19 June 2026 route (below)
- whether provision of the data is a statutory or contractual requirement and the consequences of not providing it
- the existence of automated decision-making within Arts 22A–22D, with meaningful information about the logic and the significance and envisaged consequences
- for Art 14 (data not obtained from the data subject): the categories of data and the source, including whether it came from a publicly accessible source

## What the DUAA changed

**Recognised legitimate interests — UK GDPR Art 6(1)(ea) and new Annex 1**, inserted by DUAA s 70 and Sch 4, in force 5 February 2026. Processing on a recognised legitimate interest needs no balancing test. Annex 1 lists: disclosure to a public body for its Art 6(1)(e) task; national security, public security and defence; emergencies within Part 2 of the Civil Contingencies Act 2004; detection, investigation or prevention of crime and apprehension or prosecution of offenders; safeguarding vulnerable individuals. Marketing is not on the list. Ordinary legitimate interests under Art 6(1)(f), with a balancing test, remain the basis for direct marketing analytics and fraud prevention outside those categories.

**Purpose limitation — DUAA s 71 and Sch 5**, in force 5 February 2026, sets out cases treated as compatible with the original purpose.

**Automated decision-making — DUAA s 80**, in force 5 February 2026, substitutes Art 22 with Arts 22A–22D. Art 22A defines a "significant decision" and when there is no meaningful human involvement. Art 22B restricts significant decisions based wholly or partly on special category data. Art 22C requires safeguards: information about the decision, the ability to make representations, to obtain human intervention, and to contest the decision. Art 22D gives the Secretary of State powers to further specify. The old blanket prohibition-with-exceptions framing of Art 22 is gone; a notice reproducing it is out of date.

**Subject access — DUAA s 78**, treated as in force from 1 January 2024, inserts Art 15(1A): the data subject is entitled only to what the controller can provide "based on a reasonable and proportionate search". The one-month response period may be paused while the controller seeks clarification or verifies identity (DUAA ss 76, 77).

**Complaints — DUAA s 103**, in force 19 June 2026, omits UK GDPR Art 77 and Art 57(1)(f), amends DPA 2018 s 165 so that the right to complain to the Commissioner sits there, and inserts DPA 2018 s 164A obliging the controller to facilitate complaints, provide an electronic complaint form, acknowledge within 30 days and respond without undue delay. Section 164B lets the Secretary of State require controllers to report complaint numbers. Draft the complaints paragraph to route the individual to the controller first, then to the Commissioner.

## Children

UK GDPR Art 8(1) sets the age at which a child can consent to an information society service at **13**, not the EU default of 16. Below that, consent must be given or authorised by a person holding parental responsibility. Do not cite DPA 2018 s 9 for this — that section was omitted on 31 December 2020 by the Data Protection, Privacy and Electronic Communications (Amendments etc) (EU Exit) Regulations 2019, and the age now sits in the UK GDPR text itself. A new Art 8(2A), in force from 29 April 2026, lets the Secretary of State move the threshold within a 13-to-16 range by regulations, including differently for different categories of service; check whether any such regulations have been made before relying on 13.

Separately, the ICO Age Appropriate Design Code applies to information society services likely to be accessed by children under 18 — a lower threshold than "aimed at children".

## Template

```html
<!-- DRAFT – NOT LEGALLY APPROVED -->
<h1>Privacy notice</h1>
<p>Last updated: [[date]]</p>

<h2>Who we are</h2>
<p>
  [[Registered name]] ("we") is the controller of the personal data described in this notice.<br>
  Registered office: [[address]]<br>
  Company number: [[number]], registered in [[part of the UK]]<br>
  ICO registration number: [[number]]<br>
  Data protection contact: <a href="mailto:[[address]]">[[address]]</a><br>
  Data Protection Officer: [[name and contact, or: we are not required to appoint a DPO and have not appointed one]]
</p>

<h2>What we process, why, and on what basis</h2>
<table>
  <tr><th>Data</th><th>Purpose</th><th>Lawful basis (UK GDPR Art 6)</th><th>Retention</th></tr>
  <tr><td>[[category]]</td><td>[[purpose]]</td><td>[[basis, and the specific interest if Art 6(1)(f)]]</td><td>[[period or criteria]]</td></tr>
</table>

<h2>Special category data</h2>
<p>[[Art 9 condition and the DPA 2018 Sch 1 condition, or: we do not process special category data]]</p>

<h2>Who we share it with</h2>
<p>[[recipients or categories, and their role — processor or controller]]</p>

<h2>Transfers outside the UK</h2>
<p>[[see international-transfers.md — country, mechanism, how to obtain a copy of the safeguards]]</p>

<h2>Automated decision-making</h2>
<p>[[description, logic, significance and consequences, and the Art 22C safeguards — or: we do not take significant decisions about you based solely on automated processing]]</p>

<h2>Your rights</h2>
<p>
  You have the right to access your personal data, to have inaccurate data corrected, to have data
  erased, to restrict processing, to data portability, and to object to processing. Where we rely on
  your consent you may withdraw it at any time; that does not affect processing carried out before
  you withdrew it. Requests: <a href="mailto:[[address]]">[[address]]</a>.
</p>

<h2>Complaints</h2>
<p>
  If you are unhappy with how we handle your personal data, please complain to us first using
  [[link to complaint form]] or <a href="mailto:[[address]]">[[address]]</a>. We will acknowledge your
  complaint within 30 days and respond without undue delay. If you remain dissatisfied you may
  complain to the Information Commissioner, Wycliffe House, Water Lane, Wilmslow, Cheshire SK9 5AF,
  <a href="https://ico.org.uk/make-a-complaint/">ico.org.uk/make-a-complaint</a>.
</p>

<h2>Cookies and similar technologies</h2>
<p>[[link to the cookie information — see cookies.md]]</p>
```

## Checkpoints

- [ ] Reachable without consent and without login
- [ ] Every processing operation has purpose, lawful basis, recipients and retention
- [ ] Legitimate interests named specifically, not "our business interests"
- [ ] Recognised legitimate interests only claimed where the case actually appears in Annex 1
- [ ] The services actually loaded by the site match the recipients listed — checked against the network log
- [ ] Automated decision-making paragraph written against Arts 22A–22D, not the old Art 22
- [ ] Complaints paragraph routes to the controller first (DPA 2018 s 164A), then the Commissioner (s 165)
- [ ] No reference to UK GDPR Art 77, omitted 19 June 2026
- [ ] No reference to an EU supervisory authority, the EDPB, or "Regulation (EU) 2016/679" as the applicable law
- [ ] Children: age 13 threshold under UK GDPR Art 8(1) applied — not 16 — and the Age Appropriate Design Code assessed if under-18s are likely users
- [ ] An electronic complaint form exists, not just an email address (DPA 2018 s 164A)
- [ ] All `[[…]]` placeholders resolved or explicitly reported as open

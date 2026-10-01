# Datenschutzerklärung

The revised DSG (SR 235.1) has been in force since 1 September 2023, together with the DSV (SR 235.11). Wording below from DSG Stand am 7. Juli 2025 and DSV Stand am 1. Dezember 2025. Status as at 2026-08-05.

## Art. 19 DSG — the information duty

> 1 Der Verantwortliche informiert die betroffene Person angemessen über die Beschaffung von Personendaten; diese Informationspflicht gilt auch, wenn die Daten nicht bei der betroffenen Person beschafft werden.
> 2 Er teilt der betroffenen Person bei der Beschaffung diejenigen Informationen mit, die erforderlich sind, damit sie ihre Rechte nach diesem Gesetz geltend machen kann und eine transparente Datenbearbeitung gewährleistet ist; er teilt ihr mindestens mit:
> a. die Identität und die Kontaktdaten des Verantwortlichen;
> b. den Bearbeitungszweck;
> c. gegebenenfalls die Empfängerinnen und Empfänger oder die Kategorien von Empfängerinnen und Empfängern, denen Personendaten bekanntgegeben werden.
> 3 Werden die Daten nicht bei der betroffenen Person beschafft, so teilt er ihr zudem die Kategorien der bearbeiteten Personendaten mit.
> 4 Werden die Personendaten ins Ausland bekanntgegeben, so teilt er der betroffenen Person auch den Staat oder das internationale Organ und gegebenenfalls die Garantien nach Artikel 16 Absatz 2 oder die Anwendung einer Ausnahme nach Artikel 17 mit.
> 5 Werden die Daten nicht bei der betroffenen Person beschafft, so teilt er ihr die Informationen nach den Absätzen 2–4 spätestens einen Monat, nachdem er die Daten erhalten hat, mit. […]

Art. 20 DSG lists the exceptions — the data subject already has the information, the processing is prescribed by law, the controller is bound by a statutory duty of confidentiality, or information is impossible or disproportionate for indirectly collected data.

Art. 21 DSG adds a duty to inform about an automated individual decision that produces legal effects or significantly affects the person, plus a right to state one's position and to have the decision reviewed by a natural person.

## Where the DSG differs from Art. 13 GDPR

| Point | DSG | GDPR |
|---|---|---|
| Legal basis per processing | Not required. There is no basis catalogue; private processing is lawful unless it unlawfully infringes personality (Art. 30, 31 DSG) | Art. 13(1)(c): the legal basis must be stated |
| Transfers abroad | Art. 19 Abs. 4 DSG: the **state** and the safeguard under Art. 16 Abs. 2 or the Art. 17 exception must be named | Art. 13(1)(f): existence of a decision or safeguard, reference to where to obtain a copy |
| Retention period | Not in the Art. 19 Abs. 2 minimum list, but Art. 19 Abs. 2 is an open standard and Art. 25 Abs. 2 lit. d DSG makes it disclosable on access request. Publish it | Art. 13(2)(a): mandatory |
| Data protection officer | Art. 10 DSG: voluntary for private controllers | Art. 13(1)(b): mandatory where one exists |
| Supervisory authority | EDÖB, Feldeggweg 1, 3003 Bern | The competent national authority |
| Rights catalogue | Access (Art. 25), data portability (Art. 28), rectification (Art. 32 Abs. 1), and the civil claims under Art. 32 Abs. 2 in conjunction with Art. 28 ff. ZGB to prohibit a processing, prohibit disclosure, or have data deleted | Arts. 15–22 GDPR, including a standalone right to object |

There is no free-standing statutory "Widerspruchsrecht" in the DSG equivalent to Art. 21 GDPR. The equivalent is the express declaration of will under Art. 30 Abs. 2 lit. b DSG: processing against it constitutes a personality infringement. Do not label it "Recht auf Widerspruch nach Art. 21 DSGVO" in a Swiss-only notice.

## Processing principles that shape the text

Art. 6 DSG: lawfulness, good faith, proportionality, purpose limitation and recognisability of the purpose, destruction or anonymisation once the purpose ends, accuracy. Art. 6 Abs. 6 DSG: consent is valid only if given voluntarily for one or more specific processings after adequate information. Art. 6 Abs. 7 DSG: consent must be **express** for besonders schützenswerte Personendaten, for Profiling mit hohem Risiko by a private person, and for any profiling by a federal body.

Art. 5 lit. c DSG defines besonders schützenswerte Personendaten: religious, ideological, political or trade-union views or activities; health, intimate sphere, racial or ethnic origin; genetic data; biometric data uniquely identifying a person; data on administrative and criminal proceedings or sanctions; data on social assistance measures.

Art. 5 lit. g DSG defines Profiling mit hohem Risiko as profiling that produces a high risk to personality or fundamental rights by linking data in a way that permits assessment of essential aspects of a person's personality.

## Template

```html
<!-- ENTWURF – juristisch nicht freigegeben -->
<h1>Datenschutzerklärung</h1>

<h2>Verantwortliche Stelle</h2>
<p>
  [[Firma]], [[Adresse]], Schweiz<br>
  E-Mail: [[adresse]]<br>
  [[Datenschutzberaterin/-berater nach Art. 10 DSG: Name und Kontakt – oder: nicht bestellt]]
</p>
<p>[[Vertretung in der EU nach Art. 27 DSGVO: Name und Adresse – oder: entfällt]]</p>

<h2>Grundsätze</h2>
<p>Wir bearbeiten Personendaten nach dem Schweizer Datenschutzgesetz (DSG) und der
Datenschutzverordnung (DSV). Soweit die Datenschutz-Grundverordnung (DSGVO) auf
eine Bearbeitung anwendbar ist, halten wir zusätzlich deren Vorgaben ein.</p>

<h2>Bearbeitete Daten, Zwecke und Empfänger</h2>
<table>
  <tr><th>Bearbeitung</th><th>Daten</th><th>Zweck</th><th>Empfänger</th><th>Aufbewahrung</th></tr>
  <tr><td>Serverlogs</td><td>[[IP, Zeitpunkt, User-Agent]]</td><td>Betrieb und Sicherheit</td><td>[[Hosting-Anbieter]]</td><td>[[Dauer]]</td></tr>
  <tr><td>Kontaktformular</td><td>[[Felder]]</td><td>Bearbeitung der Anfrage</td><td>[[Empfänger]]</td><td>[[Dauer]]</td></tr>
  <tr><td>Bestellung</td><td>[[Felder]]</td><td>Vertragsabwicklung</td><td>[[Zahlung, Versand]]</td><td>[[Dauer]]</td></tr>
  <tr><td>Newsletter</td><td>[[Felder]]</td><td>Direktwerbung</td><td>[[Versanddienst]]</td><td>[[Dauer]]</td></tr>
</table>

<h2>Cookies und Reichweitenmessung</h2>
<p>[[siehe cookies-tracking.md – Information und Ablehnungsmöglichkeit nach Art. 45c lit. b FMG]]</p>

<h2>Bekanntgabe ins Ausland</h2>
<p>Wir geben Personendaten in folgende Staaten bekannt:</p>
<ul>
  <li>[[Staat]] – Grundlage: [[Anhang 1 DSV / Standardvertragsklauseln nach Art. 16 Abs. 2 lit. d DSG / Ausnahme nach Art. 17 DSG]]</li>
</ul>

<h2>Automatisierte Einzelentscheidungen</h2>
<p>[[Beschreibung und Hinweis auf Art. 21 DSG – oder: Es finden keine automatisierten Einzelentscheidungen statt.]]</p>

<h2>Ihre Rechte</h2>
<p>Sie können Auskunft über die Bearbeitung Ihrer Personendaten verlangen (Art. 25 DSG),
die Herausgabe oder Übertragung Ihrer Daten verlangen (Art. 28 DSG), die Berichtigung
unrichtiger Daten verlangen (Art. 32 Abs. 1 DSG) sowie nach Art. 32 Abs. 2 DSG
verlangen, dass eine Bearbeitung oder eine Bekanntgabe unterbleibt oder Daten
gelöscht werden. Eine erteilte Einwilligung können Sie jederzeit widerrufen; die
Rechtmässigkeit der bis dahin erfolgten Bearbeitung bleibt unberührt.</p>
<p>Anlaufstelle: [[E-Mail]]. Aufsichtsbehörde: Eidgenössischer Datenschutz- und
Öffentlichkeitsbeauftragter (EDÖB), Feldeggweg 1, 3003 Bern, www.edoeb.admin.ch.</p>

<h2>Änderungen</h2>
<p>Stand dieser Erklärung: [[Datum]].</p>
```

Publish an equivalent version in every language of address.

## Checkpoints

- [ ] Reachable without login and without passing a consent dialog
- [ ] Controller identity and contact present (Art. 19 Abs. 2 lit. a DSG)
- [ ] Purpose stated per processing, not once for the whole site (lit. b)
- [ ] Recipients or categories of recipients named (lit. c), checked against the actual network requests
- [ ] For each transfer abroad: the state named, plus the Art. 16 Abs. 2 safeguard or the Art. 17 exception (Art. 19 Abs. 4 DSG)
- [ ] Retention period or the criteria for it given per category
- [ ] Express consent obtained where Art. 6 Abs. 7 DSG requires it, and the text says so
- [ ] Automated individual decisions addressed or expressly excluded (Art. 21 DSG)
- [ ] Rights listed with the Swiss articles, not with GDPR article numbers, unless the GDPR also applies
- [ ] EDÖB named as supervisory authority with the correct address
- [ ] No "Rechtsgrundlage" column invented for a Swiss-only notice
- [ ] A version exists in every language of address
- [ ] All `[[…]]` placeholders resolved or reported as open

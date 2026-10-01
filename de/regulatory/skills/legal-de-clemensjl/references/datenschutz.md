# Datenschutzerklärung

The substantive duty is Art 13 and Art 14 DSGVO; the national layer is the BDSG (Bundesdatenschutzgesetz) of 30.06.2017 in the version in force. Status as at 05.08.2026.

The declaration must be reachable without consent and without login, from every page, under its own link. Bundling it into the Impressum is bad practice: Art 13 DSGVO requires the information at the time of collection, and the Impressum is not read at that moment.

## Mandatory content, Art 13 DSGVO

Per processing operation, not once for the whole site:

- identity and contact details of the Verantwortlicher, and of the representative where Art 27 DSGVO applies (Art 13 Abs 1 lit a)
- contact details of the Datenschutzbeauftragter where one exists (lit b)
- purposes and the **legal basis under Art 6 Abs 1 DSGVO for each purpose** (lit c)
- where the basis is Art 6 Abs 1 lit f, the concrete legitimate interest — named, not a formula (lit d)
- recipients or categories of recipients (lit e)
- third-country transfers with the transfer instrument and how to obtain a copy (lit f)
- retention period or the criteria determining it (Art 13 Abs 2 lit a)
- data subject rights: access, rectification, erasure, restriction, portability, objection (lit b)
- the right to withdraw consent with effect for the future (lit c)
- the right to lodge a complaint with a supervisory authority (lit d)
- whether provision is a statutory or contractual requirement and the consequences of not providing (lit e)
- automated decision-making including profiling, with meaningful information about the logic (lit f)

Art 14 DSGVO adds the source of the data where it was not collected from the data subject, and the categories of data concerned.

## German specifics

- **Supervisory authority.** Germany has no single DPA for the private sector. Competence follows the establishment: the **Landesdatenschutzbehörde** of the Land in which the controller is established. The BfDI is competent for federal bodies and for telecommunications and postal providers, not for an ordinary webshop. Name the correct state authority with address and website; the list is published at `bfdi.bund.de`. Do not name "die Datenschutzbehörde" generically and do not name the Austrian DSB.
- **Consent age is 16.** Art 8 Abs 1 DSGVO sets 16 for information society services offered directly to a child. Germany did not exercise the opening clause in Art 8 Abs 1 Unterabs 2 DSGVO; the BDSG contains no lower age. Below 16, consent must be given or authorised by the holder of parental responsibility, and reasonable efforts must be made to verify it (Art 8 Abs 2 DSGVO).
- **§ 26 BDSG — Beschäftigtendatenverarbeitung.** Employee data may be processed for the purposes of the employment relationship where necessary for its establishment, performance or termination, or for the exercise of rights under a collective agreement. Consent in the employment context requires particular care about voluntariness and, under § 26 Abs 2 Satz 3 BDSG, the written or electronic form. Investigation of criminal offences under § 26 Abs 1 Satz 2 BDSG requires documented factual indications. Note that the CJEU (C-34/21, 30.03.2023) held a comparable Land provision incompatible with Art 88 DSGVO, so § 26 BDSG should not be relied on as a stand-alone basis without checking whether Art 6 Abs 1 lit b DSGVO carries the processing anyway. `[[UNVERIFIED: whether a reformed Beschäftigtendatengesetz has since entered into force — verify before relying on § 26 BDSG in an employment-facing text]]`
- **§ 32 to § 37 BDSG** narrow the data subject rights in defined cases (for example § 34 BDSG on access). Do not reproduce these exceptions in a consumer-facing declaration; they are defences, not information.
- Video surveillance of publicly accessible spaces: § 4 BDSG, plus a sign at the point of entry with the Art 13 core information.

## Third-country transfers — the DPF after Trump v. Slaughter

Art 13 Abs 1 lit f DSGVO wants the instrument named per recipient, not a generic sentence. For US recipients the EU-US Data Privacy Framework (Durchführungsbeschluss (EU) 2023/1795 of 10.07.2023) works only for an organisation **actually on the DPF list** and within its certified scope — check the entity on the invoice, not the brand.

On **29.06.2026** the US Supreme Court held in *Trump v. Slaughter* that the FTC's statutory removal protections are unconstitutional. Decision (EU) 2023/1795 leans on FTC independence throughout, and independent supervision is an element of the Art 45 Abs 2 lit b DSGVO adequacy test. Status as at 05.08.2026: noyb asked the Commission on 29.06.2026 to repeal the decision in an orderly way and announced an annulment action (no filing confirmed); the EDSA wrote to Commissioner McGrath on 31.07.2026 asking for a close assessment; the Commission has not acted, and its EU-US transfers page carries no 2026 notice.

Two consequences for a German declaration:

- **The decision is in force** until the Commission repeals it or the Court of Justice annuls it. A declaration stating that US transfers are now unlawful is itself wrong and, in a competitor's hands, a warning-letter target.
- **DPF alone is no longer a defensible sole basis.** Put Standardvertragsklauseln under Art 46 Abs 2 lit c DSGVO in the same contract and complete a Transfer Impact Assessment that addresses oversight and redress — the limb the ruling weakens. The fallback belongs in the Verzeichnis von Verarbeitungstätigkeiten and the AV-Vertrag; the published declaration still just names recipient, country and instrument.

## Structure that survives review

One section per processing operation, each with the same five fields: purpose, data categories, legal basis, recipients, retention. A wall of prose that names services without mapping them to a legal basis fails Art 13 Abs 1 lit c DSGVO.

Every service that actually fires must appear. Verify against the network tab, not against the intended architecture. Hosting, CDN, fonts, maps, video, captcha, chat widget, analytics, tag manager, payment provider, mail delivery, CRM, error tracking.

## Template

```html
<!-- ENTWURF – juristisch nicht freigegeben -->
<h1>Datenschutzerklärung</h1>

<h2>1. Verantwortlicher</h2>
<p>
  [[Firma]], [[Anschrift]]<br>
  E-Mail: [[address]] · Telefon: [[number]]
</p>
<p>Datenschutzbeauftragter: [[name and contact — or: Es besteht keine Pflicht zur Benennung eines Datenschutzbeauftragten nach § 38 Abs. 1 BDSG.]]</p>

<h2>2. Bereitstellung der Website und Server-Logfiles</h2>
<p>Zweck: [[purpose]]. Datenkategorien: [[IP address, timestamp, user agent, referrer]].
Rechtsgrundlage: Art. 6 Abs. 1 lit. f DSGVO, berechtigtes Interesse an [[concrete interest]].
Empfänger: [[hoster]], Auftragsverarbeiter nach Art. 28 DSGVO. Speicherdauer: [[period]].</p>

<h2>3. Kontaktaufnahme</h2>
<p>Zweck: Bearbeitung Ihrer Anfrage. Rechtsgrundlage: Art. 6 Abs. 1 lit. b DSGVO bei
vorvertraglichen Anfragen, sonst Art. 6 Abs. 1 lit. f DSGVO. Speicherdauer: [[period]].</p>

<h2>4. [[further processing operation]]</h2>
<p>Zweck / Datenkategorien / Rechtsgrundlage / Empfänger / Speicherdauer</p>

<h2>5. Empfänger und Auftragsverarbeiter</h2>
<p>[[table: provider, purpose, place of processing, transfer instrument]]</p>

<h2>6. Übermittlung in Drittländer</h2>
<p>[[per recipient: country, Angemessenheitsbeschluss or Standardvertragsklauseln nach
Art. 46 Abs. 2 lit. c DSGVO plus supplementary measures, how to obtain a copy]]</p>

<h2>7. Ihre Rechte</h2>
<p>Auskunft (Art. 15), Berichtigung (Art. 16), Löschung (Art. 17), Einschränkung (Art. 18),
Datenübertragbarkeit (Art. 20), Widerspruch (Art. 21) sowie das Recht, eine erteilte
Einwilligung jederzeit mit Wirkung für die Zukunft zu widerrufen (Art. 7 Abs. 3 DSGVO).</p>

<h2>8. Beschwerderecht</h2>
<p>Sie können sich bei einer Aufsichtsbehörde beschweren. Für uns zuständig ist:<br>
[[name of the Landesdatenschutzbehörde]], [[address]], [[website]]</p>

<h2>9. Minderjährige</h2>
<p>Unser Angebot richtet sich nicht an Kinder unter 16 Jahren. Für Nutzer unter 16 Jahren
ist die Einwilligung des Trägers der elterlichen Verantwortung erforderlich
(Art. 8 Abs. 1 DSGVO). [[or: description of the verification process actually used]]</p>

<h2>10. Stand</h2>
<p>Stand dieser Datenschutzerklärung: [[date]].</p>
```

## Checkpoints

- [ ] Reachable without consent and without login, own footer link
- [ ] Every processing operation has purpose, data categories, legal basis, recipients, retention
- [ ] Legitimate interests named concretely, not as a formula
- [ ] Every service that actually fires is listed — checked against the network tab
- [ ] Third-country transfers listed individually with the transfer instrument
- [ ] Correct **Landes**datenschutzbehörde named with address and website
- [ ] Withdrawal right for consent stated (Art 7 Abs 3 DSGVO)
- [ ] Age threshold stated as 16, not 14, not 13
- [ ] Contact details of the DPO published where one is appointed
- [ ] Employee-facing processing kept in a separate internal notice, not in the public declaration
- [ ] No BDSG-alt terminology ("Bundesdatenschutzgesetz 1990", "§ 4f BDSG", "Meldepflicht beim Bundesbeauftragten")
- [ ] All `[[…]]` placeholders resolved or explicitly reported as open

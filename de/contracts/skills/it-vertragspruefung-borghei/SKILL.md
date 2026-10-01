---
name: it-vertragspruefung-borghei
title: /it-recht:it-vertragspruefung
description: Prüfung typischer IT-Verträge (SaaS, Cloud, Outsourcing, Werkvertrag/Dienstvertrag-Abgrenzung) auf AGB-Konformität, DSGVO-Verzahnung (Art. 28 AVV), Leistungsstandards (SLA), Haftungsbegrenzung, Migrations- und Beendigungsklauseln, Open-Source-Compliance. Use when ein IT-Dienstleistungsvertrag bewertet oder verhandelt wird.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/it-recht/skills/it-vertragspruefung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: contracts
language: de
---

# /it-recht:it-vertragspruefung

## Zweck

IT-Verträge enthalten regelmäßig Klauseln, die in der AGB-Inhaltskontrolle (§§ 305 ff. BGB) scheitern, DSGVO-Pflichten missachten oder unverhältnismäßige Haftungsverteilungen schaffen. Dieser Skill identifiziert die typischen Bruchstellen entlang eines strukturierten Prüfschemas.

> **⚠️ Aktualität (Stand 2026-07):** Seit dem **12.09.2025** ist der **Data Act** ([VO (EU) 2023/2854](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32023R2854)) anwendbar. Er ist bei **jeder** IT-Vertragsprüfung als eigener Prüfschritt abzuarbeiten (siehe Schritt 3a) und gilt **unabhängig davon, ob personenbezogene Daten betroffen sind**.
>
> - **Art. 3 Abs. 1 (Zugang by design)** gilt **nur für vernetzte Produkte, die nach dem 12.09.2026 in Verkehr gebracht werden** — also erst in wenigen Wochen. Für **Bestandsprodukte** greift diese Pflicht **nicht**; die vertraglichen Zugangs- und Bereitstellungspflichten der **Art. 4 und 5** sind davon zu trennen.
> - **Art. 5**: Nutzer können verlangen, dass Daten an einen **Dritten** weitergegeben werden. Solche Verlangen sind innerhalb der gesetzlichen Frist zu bearbeiten; **Geschäftsgeheimnisse** können eine Beschränkung rechtfertigen, aber nur unter den Voraussetzungen der Verordnung und mit dokumentierter Begründung.
> - **Art. 14 ff.**: Öffentliche Stellen können bei **außergewöhnlichem Bedarf** Daten anfordern — ein eigener, oft übersehener Anspruchstyp.
> - **Art. 13**: Missbräuchlichkeitskontrolle **einseitig auferlegter Datenzugangsklauseln** in B2B-Verträgen, **neben** §§ 305 ff. BGB.
> - **Art. 23–31**: Wechsel zwischen Datenverarbeitungsdiensten; **Wechselentgelte entfallen vollständig bis zum 12.01.2027**, bis dahin nur kostenbasiert reduziert. **Art. 25** verlangt vertragliche Ausstiegsunterstützung (siehe Skill `cloud-auftragsverarbeitung`).
> - Deutsches **Data-Act-Durchführungsgesetz (DADG)**: Bundestag **26.03.2026**, BGBl. **29.05.2026**; zuständige Behörde ist die **Bundesnetzagentur** (Bekanntgabe 30.05.2026). Im selben Paket wurde das deutsche Durchführungsgesetz zum **Data Governance Act** beschlossen (BNetzA-Aufsicht über Datenvermittlungsdienste und datenaltruistische Organisationen).
>
> Einzelnormen des DADG sind vor mandantengerichteter Verwendung am verkündeten Text zu verifizieren. `[unverifiziert - prüfen]`

## Eingaben

- Vertragstyp (SaaS, Cloud-Hosting, Outsourcing, Individual-Software-Entwicklung, Wartung)
- Vertragsrolle (Anbieter / Kunde)
- Größenklasse (B2B / B2C)
- DSGVO-relevant (personenbezogene Daten verarbeitet?)
- Vorhandene Vorlagen (EVB-IT, BVB, BITKOM, eigene)
- Data-Act-Bezug: Betrifft der Vertrag ein **vernetztes Produkt** oder einen **verbundenen Dienst** (IoT)? Falls ja: **Datum des Inverkehrbringens** (vor oder nach 12.09.2026)
- Data-Act-Bezug: Handelt es sich um einen **Datenverarbeitungsdienst** (Cloud/SaaS) iSd Art. 23 ff.?

## Ablauf

### 1. Vertragstyp-Einordnung

Maßgeblich für anwendbares Recht:

| Vertragstyp | Rechtsnatur | Schwerpunkt |
|---|---|---|
| **SaaS / Cloud-Hosting** | Miet- oder Pachtvertrag (§§ 535 ff. BGB), str. | Verfügbarkeit, Datenherausgabe |
| **Software-Entwicklung individuell** | Werkvertrag (§ 631 BGB) | Abnahme, Mängelhaftung |
| **Wartung / Support** | Dienstvertrag (§ 611 BGB) | Reaktionszeiten, kein Erfolg geschuldet |
| **IT-Outsourcing** | Mischvertrag (Dienst + Werk + Miete) | Vereinbarte Service-Level |
| **Lizenzvertrag** | atypischer Vertrag (§§ 311a, 631 analog) | Reichweite der Lizenz |

### 2. AGB-Kontrolle (§§ 305 ff. BGB)

Vorlagen aus einer Mehrzahl an Verträgen sind AGB. **Auch im B2B** gelten § 305c, § 307 BGB (über § 310 Abs. 1 S. 2 BGB).

Typische problematische Klauseln:

- **Haftungsausschluss für einfache Fahrlässigkeit** in Bezug auf vertragstypische Kardinalpflichten → § 307 BGB, unwirksam.
- **Pauschalierung auf Jahresvergütung** → grundsätzlich zulässig, aber sorgfältig im Verhältnis.
- **Vertragsanpassung durch Anbieter** ohne Widerspruchsrecht → § 308 Nr. 5 BGB.
- **„Wir haften nur, soweit gesetzlich zwingend"** → Transparenzgebot § 307 Abs. 1 S. 2.

### 3. DSGVO-Verzahnung

#### Auftragsverarbeitungsvertrag (Art. 28 DSGVO)

Wenn personenbezogene Daten verarbeitet werden: AVV nach Art. 28 Abs. 3 DSGVO verpflichtend. Pflichtinhalte:

- Gegenstand und Dauer der Verarbeitung
- Art und Zweck der Verarbeitung
- Datenkategorien und Betroffenenkategorien
- Pflichten und Rechte des Verantwortlichen
- Maßnahmen nach Art. 32 DSGVO
- Sub-Auftragsverarbeiter
- Unterstützung bei Betroffenenanfragen
- Löschung / Rückgabe nach Beendigung
- Audit-Rechte des Verantwortlichen

#### Drittlandtransfer

US-Cloud-Anbieter: TIA + SCC + ggf. EU-US Data Privacy Framework. Beachte: Schrems II-Lage.

### 3a. Data-Act-Prüfung (VO (EU) 2023/2854, anwendbar seit 12.09.2025)

Dieser Schritt ist **stets** abzuarbeiten. Der Data Act gilt **unabhängig vom Personenbezug** der Daten und tritt neben DSGVO und AGB-Recht.

**a) Anwendungsbereich bestimmen.**

| Vertragsgegenstand | Einschlägige Vorschriften |
|---|---|
| **Vernetztes Produkt / verbundener Dienst** (IoT) | Art. 3–5 (Zugang und Bereitstellung an Nutzer und Dritte) |
| **Datenverarbeitungsdienst** (Cloud, SaaS, IaaS, PaaS) | Art. 23–31 (Wechsel), insb. Art. 25, 29 |
| **B2B-Vertrag mit einseitig auferlegten Datenklauseln** | Art. 13 (Missbräuchlichkeitskontrolle) |
| Jeder Dateninhaber | Art. 14 ff. (Anfragen öffentlicher Stellen bei außergewöhnlichem Bedarf) |

**b) Stichtag 12.09.2026 — die entscheidende Abgrenzung.** Die Pflicht zum **Zugang by design** nach **Art. 3 Abs. 1** — vernetzte Produkte so zu gestalten, dass Nutzerdaten unmittelbar, einfach und sicher zugänglich sind — trifft **nur Produkte, die nach dem 12.09.2026 in Verkehr gebracht werden**. Für Bestandsprodukte besteht **keine** Nachrüstpflicht nach Art. 3 Abs. 1.

**Nicht verwechseln:** Die **vertraglichen Bereitstellungspflichten** gegenüber Nutzern (**Art. 4**) und gegenüber Dritten auf Nutzerverlangen (**Art. 5**) knüpfen **nicht** an diesen Stichtag an. Die Umstellung der Verträge ist daher von der Produktgestaltung zu trennen.

**c) IoT-Verträge neu papieren (Art. 3–5).** Prüfpunkte:

- [ ] **Vorvertragliche Informationen** nach Art. 3 Abs. 2, 3: Art, Umfang, Format und Häufigkeit der erzeugten Daten; wie der Nutzer darauf zugreift; ob der Dateninhaber sie nutzt
- [ ] **Zugangsanspruch des Nutzers** (Art. 4) vertraglich abgebildet, unentgeltlich und ohne unangemessene Hürden
- [ ] **Weitergabe an Dritte auf Verlangen des Nutzers** (Art. 5) geregelt — einschließlich Bearbeitungsprozess und Fristwahrung
- [ ] **Nutzungsbeschränkungen des Dateninhabers** (z. B. kein Wettbewerbsprodukt aus Nutzerdaten) korrekt und nicht überschießend formuliert
- [ ] **Geschäftsgeheimnisse**: Beschränkungen der Datenweitergabe sind möglich, aber nur unter den Voraussetzungen der Verordnung, mit Schutzmaßnahmen und **dokumentierter Begründung**. Ein pauschaler Geheimnisvorbehalt trägt nicht.

**d) Art.-5-Anfragen operationalisieren.** Ein Verlangen des Nutzers auf Weitergabe an einen Dritten ist **innerhalb der gesetzlichen Frist** zu bearbeiten. Erforderlich sind ein definierter Eingangskanal, ein Prüfpfad (Identität, Umfang, Geschäftsgeheimnisse, ausgeschlossene Empfänger) und eine Dokumentation. Die konkrete Fristenlänge ist am Verordnungstext zu verifizieren. `[unverifiziert - prüfen]`

**e) Anfragen öffentlicher Stellen (Art. 14 ff.).** Bei **außergewöhnlichem Bedarf** können öffentliche Stellen Daten anfordern. Der Vertrag sollte regeln, wer solche Anfragen entgegennimmt, wie geprüft wird und wie die Vertragspartner informiert werden.

**f) Klauselkontrolle nach Art. 13.** Einseitig auferlegte Klauseln über Datenzugang, -nutzung und Haftung in B2B-Verträgen unterliegen einer **eigenständigen** Missbräuchlichkeitskontrolle. Sie ist **zusätzlich** zu §§ 305 ff. BGB zu prüfen und greift auch dort, wo die AGB-Kontrolle nicht durchdringt.

**g) Zuständigkeit.** Zuständige deutsche Behörde ist nach dem **DADG** (BGBl. 29.05.2026) die **Bundesnetzagentur**, nicht die Datenschutzaufsicht. Data-Act- und DSGVO-Verfahren laufen getrennt.

### 4. Service-Level-Agreements (SLA)

- Verfügbarkeit: Prozentangabe (z. B. 99,5 %) mit Berechnungsmethodik
- Reaktionszeit / Wiederherstellungszeit
- Wartungsfenster (geplant / ungeplant)
- Sanktionen bei Unterschreitung (Gutschriften, Sonderkündigungsrecht)
- Reporting / Monitoring

### 5. Migrations- und Beendigungsklauseln

Kritisch bei Cloud-/SaaS-Verträgen:

- **Datenherausgabe** in strukturiertem, gängigem und maschinenlesbarem Format, ohne Zusatzkosten
- **Übergangszeitraum** mit Mitwirkung des Anbieters
- **Löschung der Daten** nach Vertragsende mit Nachweis
- **Vendor Lock-in-Vermeidung** (Datenexport-Schnittstellen)

Bei **Datenverarbeitungsdiensten** (Cloud, SaaS) sind diese Punkte seit dem Data Act nicht mehr nur Verhandlungssache, sondern **gesetzlich vorgegeben**:

- **Art. 25**: vertragliche Ausstiegsunterstützung — Wechselfrist, Übergangszeitraum, Exportformat, Beschreibung der exportierbaren Daten, Löschung beim Altanbieter
- **Art. 29**: **Wechselentgelte entfallen vollständig bis zum 12.01.2027**; bis dahin sind nur **kostenbasiert reduzierte** Entgelte zulässig. Pauschale Ausstiegs-, Migrations- oder Egress-Gebühren sind bereits jetzt unzulässig und aus dem Vertrag zu streichen.

Vertiefte Prüfung: Skill `cloud-auftragsverarbeitung`.

### 6. Open-Source-Compliance

- Inventarisierung verwendeter OSS-Komponenten (SBOM)
- Lizenz-Verträglichkeit (GPL vs. MIT vs. Apache)
- Copyleft-Risiko bei Distribution

### 7. Haftung und Versicherung

- Kardinalpflichten klar definieren
- Cap auf Jahresvergütung (typisch 1 bis 2 x)
- Ausnahmen für Vorsatz, grobe Fahrlässigkeit, Leib/Leben, ProdHaftG
- Versicherungsnachweis (Cyber, Berufshaftpflicht)

## Quellen

### Statute

- [§§ 305–310 BGB](https://www.gesetze-im-internet.de/bgb/__305.html)
- [§ 611 BGB](https://www.gesetze-im-internet.de/bgb/__611.html), [§ 631 BGB](https://www.gesetze-im-internet.de/bgb/__631.html), [§ 535 BGB](https://www.gesetze-im-internet.de/bgb/__535.html)
- [Art. 28 DSGVO](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0679)
- [Art. 32 DSGVO](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0679), Art. 44 ff.
- [UrhG](https://www.gesetze-im-internet.de/urhg/) (Lizenzen)
- [VO (EU) 2023/2854 (Data Act)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32023R2854) — anwendbar seit **12.09.2025**; Art. 3 (Zugang by design, nur für nach dem **12.09.2026** in Verkehr gebrachte Produkte), Art. 4, 5 (Bereitstellung an Nutzer und Dritte), Art. 13 (missbräuchliche Klauseln B2B), Art. 14 ff. (öffentliche Stellen, außergewöhnlicher Bedarf), Art. 23–31 (Wechsel, insb. Art. 25 und Art. 29)
- **Data-Act-Durchführungsgesetz (DADG)** — Bundestag 26.03.2026, BGBl. 29.05.2026; zuständige Behörde **Bundesnetzagentur** (Bekanntgabe 30.05.2026). Einzelnormen `[unverifiziert - prüfen]`
- Deutsches Durchführungsgesetz zum **Data Governance Act** — beschlossen im selben Paket am 26.03.2026; BNetzA beaufsichtigt Datenvermittlungsdienste und datenaltruistische Organisationen `[unverifiziert - prüfen]`

### Vorlagen / Standards

- **EVB-IT** (Ergänzende Vertragsbedingungen IT) – öffentliche Beschaffung
- **BITKOM-Musterverträge**
- **BVB** (Besondere Vertragsbedingungen)

### Rechtsprechung

- BGH, Urt. v. 15.11.2006 – XII ZR 120/04, NJW 2007, 2394 = MMR 2007, 243 (ASP/SaaS = Mietvertrag), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2006-11-15&Aktenzeichen=XII%20ZR%20120/04)
- „Cloud-Haftung" `[unverifiziert – prüfen]` — die bisher hier geführte Fundstelle „BGH, Urt. v. 18.12.2009 – V ZR 130/08, NJW 2010, 1962" ist unzutreffend: unter dem 18.12.2009 existiert keine BGH-Entscheidung V ZR 130/08; V ZR 130/08 ist BGH, Urt. v. 06.02.2009 (Grundstücksübertragung, § 138 BGB, NJW 2009, 1346) und betrifft keine Cloud-Haftung. Eine einschlägige Leitentscheidung ist offen; Haftungsfragen sind bis auf Weiteres aus §§ 280, 535, 536a BGB und der AGB-Kontrolle abzuleiten

## Ausgabeformat

```
IT-VERTRAGSPRÜFUNG — <Vertragsbezeichnung> — <Datum>

I.    Vertragstyp                    [SaaS / Werkvertrag / Outsourcing / …]
      Anwendbares Recht:              <…>
II.   AGB-Kontrolle                   [✓ / ⚠️ / ❌]
      Problemklauseln:                <…>
III.  DSGVO
      AVV vorhanden + vollständig:    [✓ / 🔴 lückenhaft]
      Drittlandtransfer:              [N/A / SCC / DPF — TIA-Status]
III-a. Data Act (VO (EU) 2023/2854)
      Anwendungsbereich:              [IoT Art. 3–5 / Cloud Art. 23–31 / nur Art. 13 / N/A]
      Inverkehrbringen des Produkts:  [vor / nach 12.09.2026 → Art. 3 Abs. 1?]
      Nutzerzugang Art. 4 / Dritte Art. 5: [geregelt / 🔴 fehlt]
      Art.-5-Prozess + Frist:         [etabliert / 🔴 fehlt]
      Geschäftsgeheimnis-Vorbehalt:   [begründet / ⚠️ pauschal]
      Wechselentgelte Art. 29:        [keine / kostenbasiert / 🔴 pauschal]
      Ausstiegshilfe Art. 25:         [✓ / 🔴]
      Art. 13 Klauselkontrolle:       [✓ / ⚠️]
      Zuständige Behörde:             BNetzA (DADG)
IV.   SLA
      Verfügbarkeit, Reaktionszeit:   <…>
      Sanktionen:                     <…>
V.    Migration / Beendigung
      Datenherausgabe:                [✓ / 🔴]
      Löschnachweis:                  [✓ / 🔴]
VI.   Open Source
      SBOM:                           [vorhanden / fehlt]
      Lizenz-Verträglichkeit:         [✓ / ⚠️]
VII.  Haftung
      Cap:                            <EUR oder x Jahresvergütung>
      Ausnahmen:                      [vollständig / unvollständig]

Verhandlungsstrategie:                <…>
```

## Risiken / typische Fehler

- **SaaS ohne AVV** — DSGVO-Verstoß, Bußgeldrisiko Art. 83 DSGVO.
- **Drittlandtransfer ohne TIA** — Schrems II-Risiko.
- **Haftungsausschluss zu weit** — § 309 Nr. 7 BGB, § 307 BGB.
- **Datenherausgabe-Klausel fehlt** — Vendor Lock-in als Verhandlungshebel des Anbieters.
- **Open Source ohne Compliance-Prüfung** — Copyleft-Risiko bei späterer Distribution.
- **„Wir nutzen den Vendor-Standard"** — ohne eigene Prüfung kein Vertrauensschutz.
- **Data Act gar nicht geprüft** — er gilt seit **12.09.2025** und **unabhängig vom Personenbezug**. Eine IT-Vertragsprüfung, die nur AGB-Recht und DSGVO abarbeitet, ist seit diesem Datum unvollständig.
- **Art. 3 Abs. 1 auf Bestandsprodukte angewandt** — die Pflicht zum **Zugang by design** trifft **nur vernetzte Produkte, die nach dem 12.09.2026 in Verkehr gebracht werden**. Wer sie für Altprodukte annimmt, empfiehlt eine gesetzlich nicht geschuldete Nachrüstung.
- **Umgekehrter Fehler: Art. 4 und 5 mit dem Stichtag 12.09.2026 verknüpft** — die Bereitstellungspflichten gegenüber Nutzern und Dritten hängen **nicht** am Inverkehrbringen des Produkts. Wer den Stichtag auf sie überträgt, unterschätzt den heutigen Handlungsbedarf.
- **Art.-5-Verlangen ohne Prozess** — Weitergabeverlangen des Nutzers an Dritte sind fristgebunden; ohne definierten Eingangskanal und Prüfpfad läuft die Frist unbemerkt ab.
- **Pauschaler Geschäftsgeheimnis-Vorbehalt** — Geschäftsgeheimnisse können die Datenweitergabe beschränken, aber nur unter den Voraussetzungen der Verordnung, mit Schutzmaßnahmen und dokumentierter Einzelfallbegründung. Eine Blankoklausel trägt nicht.
- **Wechselentgelte im Cloud-Vertrag belassen** — sie entfallen **vollständig bis zum 12.01.2027**; bis dahin sind nur kostenbasiert reduzierte Entgelte zulässig. Pauschale Ausstiegs- und Egress-Gebühren sind bereits jetzt unzulässig.
- **Ausstiegsklausel nach Art. 25 fehlt** — Wechselfrist, Übergangszeitraum, Exportformat und Löschung beim Altanbieter müssen **vertraglich** geregelt sein.
- **Art. 13 Data Act mit der AGB-Kontrolle gleichgesetzt** — es handelt sich um eine **eigenständige** Missbräuchlichkeitskontrolle für einseitig auferlegte Datenklauseln, die neben §§ 305 ff. BGB tritt.
- **Anfragen öffentlicher Stellen (Art. 14 ff.) nicht bedacht** — bei außergewöhnlichem Bedarf besteht ein eigener Herausgabeanspruch, für den weder Zuständigkeit noch Prozess geregelt sind.
- **Falsche Aufsichtsbehörde adressiert** — für den Data Act ist in Deutschland die **Bundesnetzagentur** zuständig (DADG, BGBl. 29.05.2026), nicht die Datenschutzaufsicht.

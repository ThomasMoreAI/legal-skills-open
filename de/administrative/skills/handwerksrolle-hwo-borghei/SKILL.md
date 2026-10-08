---
name: handwerksrolle-hwo-borghei
title: /gewerberecht:handwerksrolle-hwo
description: Handwerksrecht – Eintragungspflicht in die Handwerksrolle für zulassungspflichtige Handwerke § 1 Abs. 1 HwO, Begriff des handwerksmäßigen Betriebs und der wesentlichen Tätigkeiten § 1 Abs. 2 HwO mit der Dreimonatsgrenze der Anlerndauer, Anlage A und Anlage B, Eintragungsvoraussetzungen § 7 HwO über Meisterprüfung Abs. 1a, Ingenieur- und Fachschulabschlüsse Abs. 2 und Betriebsleiter Abs. 1, Ausübungsberechtigung nach sechs Jahren Tätigkeit mit vier Jahren in leitender Stellung § 7b HwO, Ausnahmebewilligung bei unzumutbarer Belastung § 8 HwO, EU- und EWR-Anerkennung § 9 HwO, handwerklicher Nebenbetrieb und unerheblicher Nebenbetrieb § 3 HwO, Anzeigepflichten und Untersagung § 16 HwO mit gemeinsamer Erklärung von Handwerkskammer und IHK sowie Bußgeld § 117 HwO. Use when die Eintragungspflicht, eine Ausnahmebewilligung oder eine Betriebsuntersagung nach der Handwerksordnung zu prüfen ist.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/gewerberecht/skills/handwerksrolle-hwo
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: administrative
language: de
---

# /gewerberecht:handwerksrolle-hwo

## Zweck

Der Skill klärt, ob eine Tätigkeit dem Meistervorbehalt unterliegt, und eröffnet — wenn ja — die Wege in die Handwerksrolle: Meisterprüfung, gleichgestellte Abschlüsse, Betriebsleiterlösung, Ausübungsberechtigung nach § 7b HwO, Ausnahmebewilligung nach § 8 HwO oder EU-Anerkennung nach § 9 HwO. Er behandelt außerdem die Untersagung nach § 16 Abs. 3 HwO mit ihrer besonderen Verfahrensvoraussetzung.

## Eingaben

- Genaue Tätigkeitsbeschreibung: welche Arbeitsschritte werden ausgeführt, mit welchen Werkzeugen, in welcher Reihenfolge
- Zuordnung zu einem Gewerbe der Anlage A oder Anlage B zur HwO
- Qualifikationen: Meisterprüfung, Gesellenprüfung, Ingenieur- oder Fachschulabschluss, ausländische Abschlüsse
- Berufserfahrung: Dauer, Betriebe, Umfang der Leitungsverantwortung, Nachweise
- Rechtsform und Person des vorgesehenen Betriebsleiters
- Bei Nebenbetrieb: Umfang der handwerklichen Tätigkeit im Verhältnis zum Hauptbetrieb
- Bei behördlichem Verfahren: Untersagungsbescheid, Stellungnahmen von Handwerkskammer und IHK

## Sub-Agent-Architektur

Der Researcher beschafft die HwO samt Anlagen A und B, die Handwerksrollenverordnungen und die Rechtsprechung zur Abgrenzung wesentlicher Tätigkeiten. Der Drafter ordnet die Tätigkeit zu und entwirft Eintragungsantrag, Antrag nach § 7b oder § 8 HwO oder den Rechtsbehelf. Der Reviewer prüft, ob die Zuordnung tätigkeitsbezogen und nicht berufsbildbezogen erfolgt ist und ob bei § 16 Abs. 3 HwO die gemeinsame Erklärung der Kammern vorliegt.

## Ablauf

### 1. Zulassungspflicht bestimmen ([§ 1 HwO](https://www.gesetze-im-internet.de/hwo/__1.html))

Nach § 1 Abs. 1 HwO ist der selbständige Betrieb eines **zulassungspflichtigen Handwerks als stehendes Gewerbe** nur den **in die Handwerksrolle eingetragenen** natürlichen und juristischen Personen sowie Personengesellschaften gestattet. Personengesellschaften sind Personenhandelsgesellschaften und Gesellschaften bürgerlichen Rechts.

Ein Betrieb ist nach § 1 Abs. 2 S. 1 HwO ein Betrieb eines zulassungspflichtigen Handwerks, wenn er

- **handwerksmäßig** betrieben wird **und**
- ein in **Anlage A** aufgeführtes Gewerbe **vollständig** umfasst **oder** Tätigkeiten ausgeübt werden, die für dieses Gewerbe **wesentlich** sind.

**Keine wesentlichen Tätigkeiten** sind nach § 1 Abs. 2 S. 2 HwO insbesondere solche, die

1. in einem Zeitraum von **bis zu drei Monaten** erlernt werden können,
2. zwar eine längere Anlernzeit verlangen, aber für das Gesamtbild des Handwerks **nebensächlich** sind und deswegen nicht die Fertigkeiten erfordern, auf die die Ausbildung hauptsächlich ausgerichtet ist, oder
3. **nicht aus einem zulassungspflichtigen Handwerk entstanden** sind.

Die Ausübung mehrerer solcher Tätigkeiten ist zulässig, **es sei denn**, die Gesamtbetrachtung ergibt, dass sie für ein bestimmtes zulassungspflichtiges Handwerk wesentlich sind (§ 1 Abs. 2 S. 3 HwO).

**Die Prüfung ist tätigkeitsbezogen, nicht berufsbildbezogen.** Maßgeblich ist, welche konkreten Arbeitsschritte ausgeführt werden — nicht, wie das Unternehmen sich nennt oder wie der Kunde die Leistung bezeichnet. Die Abgrenzung der wesentlichen Tätigkeiten ist der zentrale Streitpunkt des Gebiets; die einschlägige Rechtsprechung ist heranzuziehen und zu verifizieren `[unverifiziert – prüfen]`.

**Anlage B** erfasst die zulassungsfreien Handwerke (Abschnitt 1) und die handwerksähnlichen Gewerbe (Abschnitt 2). Sie unterliegen **keinem** Meistervorbehalt, wohl aber der Anzeigepflicht gegenüber der Handwerkskammer.

### 2. Nebenbetrieb prüfen ([§ 3 HwO](https://www.gesetze-im-internet.de/hwo/__3.html))

Ein handwerklicher **Nebenbetrieb** liegt vor, wenn ein Betrieb neben einem Hauptbetrieb geführt wird. § 3 HwO privilegiert den **unerheblichen** handwerklichen Nebenbetrieb und den handwerklichen **Hilfsbetrieb**: Sie unterliegen der Eintragungspflicht nicht in vollem Umfang. Die Schwellen sind im Wortlaut zu prüfen; die Abgrenzung erfolgt nach Umfang und wirtschaftlicher Bedeutung im Verhältnis zum Hauptbetrieb. Der Inhaber eines Hauptbetriebs hat die Ausübung eines handwerklichen Neben- oder Hilfsbetriebs nach § 16 Abs. 1 S. 2 HwO anzuzeigen.

### 3. Wege in die Handwerksrolle

| Weg | Norm | Voraussetzungen |
|---|---|---|
| **Meisterprüfung** | [§ 7 Abs. 1a HwO](https://www.gesetze-im-internet.de/hwo/__7.html) | bestandene Meisterprüfung im zu betreibenden oder einem verwandten zulassungspflichtigen Handwerk |
| **Betriebsleiter** | § 7 Abs. 1 HwO | Eintragung des Inhabers, wenn der **Betriebsleiter** die Voraussetzungen erfüllt — der praktisch wichtigste Weg für Kapitalgesellschaften |
| **Ingenieure, Absolventen technischer Hochschulen und staatlicher oder staatlich anerkannter Fachschulen für Technik und Gestaltung** | § 7 Abs. 2 HwO | Studien- oder Schulschwerpunkt entspricht dem Handwerk; ebenso mindestens gleichwertige staatliche oder staatlich anerkannte Prüfungen, einschließlich solcher nach § 42 HwO oder § 53 BBiG |
| **Ausübungsberechtigung** | [§ 7b HwO](https://www.gesetze-im-internet.de/hwo/__7b.html) | Gesellenprüfung im zu betreibenden oder verwandten Handwerk bzw. Abschlussprüfung in einem entsprechenden Ausbildungsberuf **und** insgesamt **sechs Jahre** Tätigkeit, davon **vier Jahre in leitender Stellung**; die ausgeübte Tätigkeit muss eine wesentliche Tätigkeit des Handwerks umfasst haben. **Ausgenommen** sind die Handwerke der Nummern 12 und 33 bis 37 der Anlage A |
| **Ausnahmebewilligung** | [§ 8 HwO](https://www.gesetze-im-internet.de/hwo/__8.html) | Nachweis der notwendigen Kenntnisse und Fertigkeiten **und** Ausnahmefall: die Ablegung der Meisterprüfung würde eine **unzumutbare Belastung** bedeuten; Ausnahmefall auch bei bestandener Prüfung nach § 42 HwO oder § 53 BBiG |
| **EU-, EWR- und Schweiz-Anerkennung** | [§ 9 HwO](https://www.gesetze-im-internet.de/hwo/__9.html) | Anerkennung von Berufsqualifikationen bei Niederlassung, grenzüberschreitender Dienstleistungserbringung und Europäischem Berufsausweis nach Maßgabe der auf § 9 gestützten Rechtsverordnung (EU/EWR-HwV) |

Zu § 7b HwO: Eine **leitende Stellung** liegt vor, wenn dem Gesellen eigenverantwortliche Entscheidungsbefugnisse in einem Betrieb oder wesentlichen Betriebsteil übertragen waren; der Nachweis kann durch Arbeitszeugnisse, Stellenbeschreibungen oder in anderer Weise geführt werden. Die betriebswirtschaftlichen, kaufmännischen und rechtlichen Kenntnisse gelten nach § 7b Abs. 1a HwO in der Regel durch die Berufserfahrung als nachgewiesen.

Zu § 8 HwO: Die Ausnahmebewilligung kann **unter Auflagen, Bedingungen oder befristet** und auf einen **wesentlichen Teil** der Tätigkeiten beschränkt erteilt werden; dann genügt der Nachweis der hierfür erforderlichen Kenntnisse (§ 8 Abs. 2 HwO). Zuständig ist nach § 8 Abs. 3 HwO die **höhere Verwaltungsbehörde** nach Anhörung der Handwerkskammer; die Länder können abweichende Zuständigkeiten bestimmen.

### 4. Eintragung und Anzeigepflichten ([§§ 6 ff.](https://www.gesetze-im-internet.de/hwo/__6.html), [§ 16 HwO](https://www.gesetze-im-internet.de/hwo/__16.html))

- Die **Handwerksrolle** wird von der Handwerkskammer geführt (§ 6 HwO); über die Eintragung wird die **Handwerkskarte** nach § 10 Abs. 2 HwO ausgestellt.
- Nach **§ 16 Abs. 1 S. 1 HwO** ist die Handwerkskarte **gleichzeitig** mit der Gewerbeanzeige nach § 14 GewO der dafür zuständigen Behörde vorzulegen (`/gewerberecht:gewerbeanzeige-reisegewerbe`).
- Nach **§ 16 Abs. 2 HwO** sind der Handwerkskammer unverzüglich Beginn und Beendigung des Betriebs sowie Bestellung und Abberufung des Betriebsleiters anzuzeigen; bei juristischen Personen zusätzlich die gesetzlichen Vertreter, bei Personengesellschaften die für die technische Leitung verantwortlichen und die vertretungsberechtigten Gesellschafter.

### 5. Untersagung nach § 16 Abs. 3 HwO

Wird der selbständige Betrieb eines zulassungspflichtigen Handwerks als stehendes Gewerbe **entgegen den Vorschriften der HwO** ausgeübt, kann die nach Landesrecht zuständige Behörde die Fortsetzung untersagen.

**Besondere Verfahrensvoraussetzung — der zentrale Verteidigungsansatz:** Die Untersagung ist nach § 16 Abs. 3 S. 2 HwO **nur zulässig**, wenn **Handwerkskammer und Industrie- und Handelskammer zuvor angehört** worden sind **und in einer gemeinsamen Erklärung mitgeteilt haben, dass sie die Voraussetzungen einer Untersagung als gegeben ansehen**. Können sich die Kammern nicht auf eine gemeinsame Erklärung verständigen, entscheidet nach § 16 Abs. 4 HwO ein vom Deutschen Industrie- und Handelskammertag und vom Zentralverband des Deutschen Handwerks gebildeter Schlichtungsausschuss.

Fehlt die gemeinsame Erklärung, ist die Untersagung rechtswidrig. Dies ist in jedem Mandat zuerst zu prüfen und zu rügen.

Daneben ist die Ausübung eines zulassungspflichtigen Handwerks ohne Eintragung nach [§ 117 HwO](https://www.gesetze-im-internet.de/hwo/__117.html) bußgeldbewehrt; die konkrete Nummer und der Rahmen sind im Wortlaut zu prüfen. Zusätzlich kommt bei Beschäftigung ohne Eintragung eine Ahndung nach dem [SchwarzArbG](https://www.gesetze-im-internet.de/schwarzarbg_2004/) in Betracht.

### 6. Rechtsschutz

- **Eintragung** und **Ausübungsberechtigung**: Verpflichtungsklage nach [§ 42 Abs. 1 Alt. 2 VwGO](https://www.gesetze-im-internet.de/vwgo/__42.html); bei gebundener Entscheidung Verpflichtungs-, bei Beurteilungs- oder Ermessensspielraum Bescheidungsurteil nach § 113 Abs. 5 VwGO.
- **Ausnahmebewilligung § 8 HwO**: gebundene Entscheidung dem Grunde nach („ist zu erteilen"), Ermessen bei Nebenbestimmungen und Beschränkung nach Abs. 2.
- **Untersagung § 16 Abs. 3 HwO**: Widerspruch und Anfechtungsklage; bei Sofortvollzug Antrag nach [§ 80 Abs. 5 VwGO](https://www.gesetze-im-internet.de/vwgo/__80.html).
- **Löschung aus der Handwerksrolle**: Anfechtungsklage gegen den Löschungsbescheid.

## Deterministische Berechnung

Die Fristen des § 7b HwO sind Zeitraumberechnungen aus Beschäftigungsnachweisen; der Rechner in [`../../../scripts/legal_calc/`](../../../scripts/legal_calc/) macht nur die Arithmetik:

```bash
# § 7b Abs. 1 Nr. 2 HwO: sechs Jahre Tätigkeit ab 01.09.2019
python -m scripts.legal_calc.cli frist --ereignis 01.09.2019 --menge 6 --einheit jahre --land BY

# Davon vier Jahre in leitender Stellung ab 01.03.2021
python -m scripts.legal_calc.cli frist --ereignis 01.03.2021 --menge 4 --einheit jahre --land BY

# Widerspruchsfrist § 70 VwGO gegen die Untersagung
python -m scripts.legal_calc.cli frist --ereignis 15.04.2026 --menge 1 --einheit monate --land BY
```

Ob eine Tätigkeit „wesentlich" ist und ob eine Stellung „leitend" war, bleibt juristische Wertung und ist gesondert zu belegen.

## Quellen

### Statute

- [§ 1 HwO](https://www.gesetze-im-internet.de/hwo/__1.html), [§ 3 HwO](https://www.gesetze-im-internet.de/hwo/__3.html), [§ 6 HwO](https://www.gesetze-im-internet.de/hwo/__6.html), [§ 7 HwO](https://www.gesetze-im-internet.de/hwo/__7.html), [§ 7b HwO](https://www.gesetze-im-internet.de/hwo/__7b.html), [§ 8 HwO](https://www.gesetze-im-internet.de/hwo/__8.html), [§ 9 HwO](https://www.gesetze-im-internet.de/hwo/__9.html), [§ 10 HwO](https://www.gesetze-im-internet.de/hwo/__10.html), [§ 16 HwO](https://www.gesetze-im-internet.de/hwo/__16.html), [§ 42 HwO](https://www.gesetze-im-internet.de/hwo/__42.html), [§ 117 HwO](https://www.gesetze-im-internet.de/hwo/__117.html); Anlage A und Anlage B zur HwO
- [§ 14 GewO](https://www.gesetze-im-internet.de/gewo/__14.html), [§ 15 GewO](https://www.gesetze-im-internet.de/gewo/__15.html)
- [§ 53 BBiG](https://www.gesetze-im-internet.de/bbig_2005/__53.html); [SchwarzArbG](https://www.gesetze-im-internet.de/schwarzarbg_2004/)
- [§ 42 VwGO](https://www.gesetze-im-internet.de/vwgo/__42.html), [§ 70 VwGO](https://www.gesetze-im-internet.de/vwgo/__70.html), [§ 80 VwGO](https://www.gesetze-im-internet.de/vwgo/__80.html), [§ 113 VwGO](https://www.gesetze-im-internet.de/vwgo/__113.html)
- EU/EWR-Handwerks-Verordnung auf Grundlage des § 9 HwO `[unverifiziert – prüfen]` hinsichtlich der geltenden Fassung

### Kommentare

- Detterbeck, HwO, Kommentar, § 1, § 7b, § 8, § 16.
- Honig/Knörr, HwO, § 1 Rn. 1 ff. (wesentliche Tätigkeiten).
- Landmann/Rohmer, GewO, Ergänzungsband zur HwO.
- Schwannecke, Handwerksordnung, Praxiskommentar.

### Rechtsprechung

Zur Abgrenzung wesentlicher Tätigkeiten nach § 1 Abs. 2 HwO, zur leitenden Stellung nach § 7b HwO und zur unzumutbaren Belastung nach § 8 HwO besteht gefestigte Rechtsprechung des BVerwG und der Oberverwaltungsgerichte. Jede konkrete Entscheidung ist vor Verwendung in juris, Beck-Online oder auf bverwg.de zu verifizieren; ohne Beleg gilt sie als `[unverifiziert – prüfen]`.

## Ausgabeformat

```
HANDWERKSROLLE — <Mandat> — <Datum>

I.   Tätigkeitsanalyse
     Ausgeführte Arbeitsschritte:  <detailliert>
     Zuordnung:                    [Anlage A Nr. … / Anlage B Abschnitt 1 / Abschnitt 2 / kein Handwerk]
     Handwerksmäßiger Betrieb:     [ja / nein]
     Wesentliche Tätigkeiten § 1 Abs. 2 S. 1: <…>
       S. 2 Nr. 1 (≤ 3 Monate Anlernzeit): <…>
       S. 2 Nr. 2 (nebensächlich):          <…>
       S. 2 Nr. 3 (nicht aus zulassungspflichtigem Handwerk entstanden): <…>
       S. 3 Gesamtbetrachtung:              <…>
     Ergebnis:                     [eintragungspflichtig / nicht eintragungspflichtig]

II.  Nebenbetrieb § 3 HwO
     Hauptbetrieb:                 <…>
     Unerheblicher Nebenbetrieb / Hilfsbetrieb: [ja / nein]
     Anzeige § 16 Abs. 1 S. 2:     [erfolgt / offen]

III. Weg in die Handwerksrolle
     § 7 Abs. 1a Meisterprüfung:   [vorhanden / nein]
     § 7 Abs. 1 Betriebsleiter:    [Person <…> / offen]
     § 7 Abs. 2 gleichgestellter Abschluss: [vorhanden / nein]
     § 7b Ausübungsberechtigung:   6 Jahre bis <Datum>; davon 4 Jahre leitend bis <Datum>
       Ausschluss Anlage A Nr. 12, 33–37: [betroffen / nicht betroffen]
     § 8 Ausnahmebewilligung:      [Ausnahmefall — unzumutbare Belastung: …]
     § 9 EU/EWR-Anerkennung:       [einschlägig / nein]
     Empfehlung:                   <…>

IV.  Anzeigen
     Handwerkskarte § 16 Abs. 1 iVm § 14 GewO: [vorgelegt / offen]
     Anzeigen § 16 Abs. 2 HwO:     <Beginn / Betriebsleiter / Vertreter>

V.   Untersagung § 16 Abs. 3 HwO
     Gemeinsame Erklärung von HwK und IHK: [liegt vor / fehlt — Verfügung rechtswidrig]
     Schlichtungsausschuss § 16 Abs. 4:     [angerufen / nein]
     Anhörung § 28 VwVfG:                   [erfolgt / unterblieben]
     Rechtsbehelf:                          Frist bis <Datum>
     Sofortvollzug:                         [angeordnet — § 80 Abs. 3 VwGO tragfähig? / nein]

VI.  Sanktionen
     § 117 HwO:                    <Tatbestand und Rahmen>
     SchwarzArbG:                  [einschlägig / nein]

VII. Risiko: 🟢 / 🟡 / 🔴 <Begründung>
VIII.Quellenverzeichnis
```

## Risiken / typische Fehler

- **Berufsbild statt Tätigkeit geprüft.** § 1 Abs. 2 HwO knüpft an die konkret ausgeführten Arbeitsschritte an, nicht an die Firmenbezeichnung oder die Kundenerwartung.
- **Dreimonatsgrenze des § 1 Abs. 2 S. 2 Nr. 1 HwO übersehen.** Tätigkeiten, die in bis zu drei Monaten erlernbar sind, sind nicht wesentlich.
- **Gesamtbetrachtung nach § 1 Abs. 2 S. 3 HwO ausgelassen.** Mehrere für sich unwesentliche Tätigkeiten können zusammen wesentlich sein.
- **Anlage A und Anlage B verwechselt.** Nur Anlage A unterliegt dem Meistervorbehalt; Anlage B kennt Anzeige-, aber keine Zulassungspflicht.
- **§ 7b HwO ohne Prüfung der Ausschlussgewerbe angenommen.** Die Nummern 12 und 33 bis 37 der Anlage A sind ausgenommen.
- **Leitende Stellung nicht belegt.** § 7b Abs. 1 Nr. 2 HwO verlangt eigenverantwortliche Entscheidungsbefugnisse; Arbeitszeugnisse und Stellenbeschreibungen sind beizubringen.
- **§ 8 HwO ohne Darlegung der unzumutbaren Belastung beantragt.** Der Ausnahmefall ist eigenständige Voraussetzung neben dem Kenntnisnachweis.
- **Betriebsleiterlösung nach § 7 Abs. 1 HwO übersehen.** Für Kapitalgesellschaften ist sie regelmäßig der schnellste Weg.
- **Untersagung ohne gemeinsame Erklärung der Kammern hingenommen.** § 16 Abs. 3 S. 2 HwO macht sie zur Zulässigkeitsvoraussetzung.
- **Handwerkskarte nicht gleichzeitig mit der Gewerbeanzeige vorgelegt** (§ 16 Abs. 1 S. 1 HwO iVm § 14 GewO).
- **Rechtsprechung erfunden.** Jede Entscheidung ist zu belegen oder als `[unverifiziert – prüfen]` zu kennzeichnen.

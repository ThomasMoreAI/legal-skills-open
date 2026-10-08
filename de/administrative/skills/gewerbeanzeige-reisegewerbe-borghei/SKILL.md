---
name: gewerbeanzeige-reisegewerbe-borghei
title: /gewerberecht:gewerbeanzeige-reisegewerbe
description: Gewerbeanzeige und Reisegewerbe – Anzeigepflicht für stehendes Gewerbe § 14 GewO bei Beginn, Verlegung, Gegenstandswechsel, Namensänderung und Aufgabe, Empfangsbescheinigung binnen drei Tagen und Verhinderung des Betriebs ohne Zulassung § 15 Abs. 2 GewO, Abgrenzung zum Reisegewerbe § 55 Abs. 1 GewO (ohne vorhergehende Bestellung außerhalb der gewerblichen Niederlassung) mit Reisegewerbekartenpflicht § 55 Abs. 2, Befreiungen § 55a, Versagung § 57, verbotene Tätigkeiten § 56, Marktprivileg §§ 64–71a, Anwendungsausnahmen § 6 GewO einschließlich freier Berufe, Abgrenzung zum landesrechtlichen Gaststättenrecht sowie Bußgeldtatbestände §§ 145, 146 GewO. Use when eine Gewerbeanmeldung zu prüfen, eine Reisegewerbekarte zu beantragen oder der Betrieb ohne Zulassung untersagt worden ist.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/gewerberecht/skills/gewerbeanzeige-reisegewerbe
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: administrative
language: de
---

# /gewerberecht:gewerbeanzeige-reisegewerbe

## Zweck

Der Skill klärt die formale Eingangsfrage jedes gewerberechtlichen Mandats: Liegt überhaupt ein Gewerbe im Sinne der GewO vor, ist es stehendes Gewerbe oder Reisegewerbe, welche Anzeige oder Erlaubnis ist erforderlich und was folgt aus ihrem Fehlen. Er behandelt außerdem die Untersagung des Betriebs ohne Zulassung nach § 15 Abs. 2 GewO, die in der Praxis regelmäßig mit der Untersagung nach § 35 GewO verwechselt wird.

## Eingaben

- Tätigkeitsbeschreibung: was, wo, für wen, mit welcher Anbahnung
- Ob eine gewerbliche Niederlassung iSd § 4 Abs. 3 GewO besteht
- Wie der Kundenkontakt zustande kommt: auf Bestellung oder ohne vorhergehende Bestellung
- Rechtsform, Beginn der Tätigkeit, Zweigniederlassungen und unselbständige Zweigstellen
- Vorhandene Gewerbeanzeige, Empfangsbescheinigung, Erlaubnisse
- Bei behördlichem Verfahren: Untersagungs- oder Bußgeldbescheid
- Bei Marktveranstaltungen: Art der Veranstaltung und Festsetzungsbescheid

## Sub-Agent-Architektur

Der Researcher beschafft die Normen der GewO, die einschlägigen Landesregelungen (Zuständigkeit, Gaststättenrecht) und die Rechtsprechung zum Gewerbebegriff und zur Abgrenzung des Reisegewerbes. Der Drafter ordnet die Tätigkeit zu und entwirft Anzeige, Antrag oder Rechtsbehelf. Der Reviewer prüft die Abgrenzung nach § 6 GewO, die Zuordnung stehendes Gewerbe / Reisegewerbe und ob § 15 Abs. 2 GewO und § 35 GewO auseinandergehalten werden.

## Ablauf

### 1. Anwendbarkeit der GewO prüfen ([§ 6 GewO](https://www.gesetze-im-internet.de/gewo/__6.html))

**Dieser Schritt steht vor allem anderen.** Die GewO ist nach § 6 Abs. 1 GewO **nicht anzuwenden** unter anderem auf:

- die Fischerei, die Errichtung und Verlegung von Apotheken, die entgeltliche Erziehung von Kindern und das Unterrichtswesen;
- die Tätigkeit der **Rechtsanwälte** und ihrer Berufsausübungsgesellschaften, der **Patentanwälte**, der **Notare**, der in § 10 Abs. 1 RDG und § 1 Abs. 2, 3 RDGEG genannten Personen, der **Wirtschaftsprüfer**, vereidigten Buchprüfer, **Steuerberater** und Steuerbevollmächtigten;
- den Gewerbebetrieb der Auswandererberater, das Seelotswesen und die Tätigkeit der Prostituierten.

Auf das Bergwesen, die ärztlichen und anderen Heilberufe, den Verkauf von Arzneimitteln, den Vertrieb von Lotterielosen und die Viehzucht findet die GewO nur bei ausdrücklicher Bestimmung Anwendung; auf Versicherungsunternehmen mit Ausnahme des Titels XI gar nicht.

Hinzu tritt die ungeschriebene Abgrenzung zu den **freien Berufen** und zur **Urproduktion** sowie zur bloßen **Verwaltung eigenen Vermögens**, die kein Gewerbe ist. Die Einordnung ist zu begründen, nicht zu behaupten.

### 2. Stehendes Gewerbe oder Reisegewerbe abgrenzen ([§ 55 Abs. 1 GewO](https://www.gesetze-im-internet.de/gewo/__55.html))

Ein **Reisegewerbe** betreibt, wer **gewerbsmäßig ohne vorhergehende Bestellung außerhalb seiner gewerblichen Niederlassung** ([§ 4 Abs. 3 GewO](https://www.gesetze-im-internet.de/gewo/__4.html)) **oder ohne eine solche zu haben**

1. Waren feilbietet, Bestellungen aufsucht (vertreibt) oder ankauft, Leistungen anbietet oder Bestellungen auf Leistungen aufsucht, oder
2. unterhaltende Tätigkeiten als Schausteller oder nach Schaustellerart ausübt.

Die beiden Merkmale sind kumulativ zu prüfen:

| Merkmal | Prüfpunkt |
|---|---|
| **Ohne vorhergehende Bestellung** | Geht die Initiative vom Gewerbetreibenden aus? Eine vom Kunden **selbst veranlasste** Terminvereinbarung ist eine vorhergehende Bestellung — dann kein Reisegewerbe |
| **Außerhalb der gewerblichen Niederlassung** | § 4 Abs. 3 GewO: Niederlassung setzt einen dauerhaft für den Gewerbebetrieb genutzten, von außen erkennbaren Raum voraus |

Wer eine Niederlassung hat und Kunden auf deren Anforderung aufsucht, betreibt **stehendes Gewerbe**. Wer ohne Bestellung an der Haustür oder auf der Straße anbietet, betreibt Reisegewerbe — auch bei vorhandener Niederlassung.

### 3. Stehendes Gewerbe: Anzeigepflicht ([§ 14](https://www.gesetze-im-internet.de/gewo/__14.html), [§ 15 GewO](https://www.gesetze-im-internet.de/gewo/__15.html))

**Anzeigepflichtig** ist nach § 14 Abs. 1 GewO, wer den selbständigen Betrieb eines stehenden Gewerbes, einer **Zweigniederlassung** oder einer **unselbständigen Zweigstelle** anfängt — **gleichzeitig** mit dem Beginn. Dasselbe gilt bei

1. **Verlegung** des Betriebs,
2. **Wechsel oder Ausdehnung des Gegenstands** auf Waren oder Leistungen, die bei Gewerbebetrieben der angemeldeten Art nicht geschäftsüblich sind,
2a. **Änderung des Namens** des Gewerbetreibenden,
3. **Aufgabe** des Betriebs.

Bei Verlegung in einen anderen Meldebezirk ist die Aufgabe **ausschließlich** gegenüber der für die Anmeldung zuständigen Behörde anzuzeigen; diese übermittelt die Daten. Steht die Betriebsaufgabe eindeutig fest und unterbleibt die Abmeldung, kann die Behörde von Amts wegen abmelden.

§ 14 Abs. 2 GewO erstreckt die Anzeigepflicht auf den Handel mit Arzneimitteln, Losen von Lotterien und Ausspielungen sowie den Betrieb von Wettannahmestellen. Für **Automatenaufsteller** gilt § 14 Abs. 3 GewO mit Anzeige am Ort der Hauptniederlassung und der Pflicht, Name, ladungsfähige Anschrift und Anschrift der Hauptniederlassung sichtbar am Automaten anzubringen.

Nach § 15 Abs. 1 GewO **bescheinigt die Behörde innerhalb von drei Tagen den Empfang der Anzeige**. Die Gewerbeanzeige ist eine **Anzeige, keine Erlaubnis** — die Empfangsbescheinigung erlaubt nichts, was nicht ohnehin erlaubt ist.

### 4. Betrieb ohne Zulassung ([§ 15 Abs. 2 GewO](https://www.gesetze-im-internet.de/gewo/__15.html))

Wird ein Gewerbe, das einer **Erlaubnis, Genehmigung, Konzession oder Bewilligung** bedarf, **ohne diese Zulassung** betrieben, **kann** die zuständige Behörde die Fortsetzung des Betriebs **verhindern**. Dasselbe gilt, wenn eine ausländische juristische Person, deren Rechtsfähigkeit im Inland nicht anerkannt wird, ein Gewerbe beginnt.

Abzugrenzen ist scharf:

| Norm | Anknüpfung | Entscheidungstyp |
|---|---|---|
| **§ 15 Abs. 2 GewO** | **formelle** Illegalität — es fehlt die erforderliche Zulassung | **Ermessen** ("kann") |
| **§ 35 GewO** | **materielle** Unzuverlässigkeit | **gebunden** ("ist zu untersagen"), aber gesperrt bei erlaubnispflichtigen Gewerben (Abs. 8) |
| **§§ 48, 49 VwVfG** | Aufhebung einer erteilten Erlaubnis | Ermessen mit Fristbindung |

Eine auf § 35 GewO gestützte Verfügung, die in Wahrheit nur das Fehlen einer Erlaubnis rügt, ist auf die falsche Rechtsgrundlage gestützt. Umgekehrt darf § 15 Abs. 2 GewO nicht als Ersatz für die materielle Untersagung dienen. Im Ermessensrahmen des § 15 Abs. 2 GewO ist zu berücksichtigen, ob die Erlaubnis erteilt werden könnte — dann ist die Fristsetzung zur Nachholung das mildere Mittel.

### 5. Reisegewerbe: Karte, Befreiungen, Verbote ([§§ 55 ff. GewO](https://www.gesetze-im-internet.de/gewo/__55.html))

- **Reisegewerbekarte** (§ 55 Abs. 2 GewO): Wer ein Reisegewerbe betreiben will, bedarf der Erlaubnis. Sie kann nach Abs. 3 inhaltlich beschränkt, befristet und mit Auflagen versehen werden.
- **Befreiungen** ([§ 55a GewO](https://www.gesetze-im-internet.de/gewo/__55a.html)): Ausnahmen unter anderem für den Vertrieb selbst gewonnener Erzeugnisse der Land- und Forstwirtschaft, für Tätigkeiten im Rahmen von Messen und Märkten sowie für weitere gesetzlich benannte Konstellationen — der Katalog ist im Einzelfall vollständig durchzugehen.
- **Versagung** ([§ 57 GewO](https://www.gesetze-im-internet.de/gewo/__57.html)): Die Reisegewerbekarte ist bei Unzuverlässigkeit zu versagen; die Systematik entspricht der des stehenden Gewerbes.
- **Verbotene Tätigkeiten** ([§ 56 GewO](https://www.gesetze-im-internet.de/gewo/__56.html)): Im Reisegewerbe sind bestimmte Waren und Leistungen vom Vertrieb ausgeschlossen — etwa der Vertrieb bestimmter Finanzprodukte, Edelmetalle und Arzneimittel sowie das Ausspielen und Anbieten von Glücksspielen. Der Katalog ist vor jeder Beratung im Wortlaut zu prüfen.
- **Mitführpflicht** ([§ 60c GewO](https://www.gesetze-im-internet.de/gewo/__60c.html)): Die Reisegewerbekarte ist während der Ausübung mitzuführen und auf Verlangen vorzuzeigen.

### 6. Marktprivileg ([§§ 64 bis 71a GewO](https://www.gesetze-im-internet.de/gewo/__64.html))

Für festgesetzte Messen, Ausstellungen, Groß-, Wochen-, Spezial- und Jahrmärkte gelten die Sondervorschriften des Titels IV. Zentral ist die **Festsetzung** durch die zuständige Behörde ([§ 69 GewO](https://www.gesetze-im-internet.de/gewo/__69.html)) und ihre Wirkung ([§ 69a GewO](https://www.gesetze-im-internet.de/gewo/__69a.html)) — das sogenannte **Marktprivileg**: Auf einer festgesetzten Veranstaltung bedarf es für den Vertrieb der zugelassenen Waren keiner Reisegewerbekarte, und die Vorschriften über die Ladenöffnung finden keine Anwendung. Der Anspruch auf **Teilnahme** richtet sich nach [§ 70 GewO](https://www.gesetze-im-internet.de/gewo/__70.html); Ausschlüsse nach § 70 Abs. 3 GewO sind begründungsbedürftig und gerichtlich überprüfbar.

### 7. Angrenzende Regime

- **Gaststättenrecht**: Der Betrieb einer Gaststätte ist seit der Föderalismusreform ganz überwiegend **Landesrecht**; das [GastG](https://www.gesetze-im-internet.de/gastg/) des Bundes gilt nur, soweit die Länder keine eigenen Regelungen getroffen haben. Die konkrete Landesnorm ist zu benennen `[unverifiziert – prüfen]` je Land.
- **Handwerk**: Zulassungspflichtige Handwerke der Anlage A zur HwO erfordern zusätzlich die Eintragung in die Handwerksrolle (`/gewerberecht:handwerksrolle-hwo`); § 16 Abs. 1 HwO verlangt die Vorlage der Handwerkskarte **gleichzeitig** mit der Anzeige nach § 14 GewO.
- **Erlaubnispflichtige Gewerbe**: `/gewerberecht:gewerbeerlaubnis-34-gewo`.
- **Untersagung wegen Unzuverlässigkeit**: `/gewerberecht:gewerbeuntersagung-35-gewo`.

### 8. Sanktionen

Verstöße gegen die Anzeigepflicht nach § 14 GewO und gegen die Reisegewerbevorschriften sind nach [§ 145](https://www.gesetze-im-internet.de/gewo/__145.html) und [§ 146 GewO](https://www.gesetze-im-internet.de/gewo/__146.html) bußgeldbewehrt; die Fortsetzung eines Gewerbes trotz vollziehbarer Untersagung ist nach [§ 148 GewO](https://www.gesetze-im-internet.de/gewo/__148.html) strafbewehrt. Die Tätigkeit ohne erforderliche Erlaubnis ist nach [§ 144 GewO](https://www.gesetze-im-internet.de/gewo/__144.html) bußgeldbewehrt. Die konkrete Nummer des jeweiligen Bußgeldtatbestands ist im Wortlaut zu prüfen und zu zitieren.

## Deterministische Berechnung

Der Rechner in [`../../../scripts/legal_calc/`](../../../scripts/legal_calc/) macht nur die Arithmetik:

```bash
# Empfangsbescheinigung § 15 Abs. 1 GewO: 3 Tage ab Eingang der Anzeige am 04.05.2026
python -m scripts.legal_calc.cli frist --ereignis 04.05.2026 --menge 3 --einheit tage --land BY

# Widerspruchsfrist § 70 VwGO gegen die Verfügung nach § 15 Abs. 2 GewO
python -m scripts.legal_calc.cli frist --ereignis 04.05.2026 --menge 1 --einheit monate --land BY

# Verfolgungsverjährung der Ordnungswidrigkeit (§ 31 OWiG) — Rahmen gesondert prüfen
python -m scripts.legal_calc.cli frist --ereignis 04.05.2026 --menge 6 --einheit monate --land BY
```

## Quellen

### Statute

- [§ 4 GewO](https://www.gesetze-im-internet.de/gewo/__4.html), [§ 6 GewO](https://www.gesetze-im-internet.de/gewo/__6.html), [§ 14 GewO](https://www.gesetze-im-internet.de/gewo/__14.html), [§ 15 GewO](https://www.gesetze-im-internet.de/gewo/__15.html), [§ 35 GewO](https://www.gesetze-im-internet.de/gewo/__35.html), [§ 55 GewO](https://www.gesetze-im-internet.de/gewo/__55.html), [§ 55a GewO](https://www.gesetze-im-internet.de/gewo/__55a.html), [§ 56 GewO](https://www.gesetze-im-internet.de/gewo/__56.html), [§ 57 GewO](https://www.gesetze-im-internet.de/gewo/__57.html), [§ 60c GewO](https://www.gesetze-im-internet.de/gewo/__60c.html), [§ 64 GewO](https://www.gesetze-im-internet.de/gewo/__64.html), [§ 69 GewO](https://www.gesetze-im-internet.de/gewo/__69.html), [§ 69a GewO](https://www.gesetze-im-internet.de/gewo/__69a.html), [§ 70 GewO](https://www.gesetze-im-internet.de/gewo/__70.html), [§ 144 GewO](https://www.gesetze-im-internet.de/gewo/__144.html), [§ 145 GewO](https://www.gesetze-im-internet.de/gewo/__145.html), [§ 146 GewO](https://www.gesetze-im-internet.de/gewo/__146.html), [§ 148 GewO](https://www.gesetze-im-internet.de/gewo/__148.html)
- [§ 34a GewO](https://www.gesetze-im-internet.de/gewo/__34a.html), [§ 34c GewO](https://www.gesetze-im-internet.de/gewo/__34c.html), [§ 34d GewO](https://www.gesetze-im-internet.de/gewo/__34d.html), [§ 34f GewO](https://www.gesetze-im-internet.de/gewo/__34f.html), [§ 34i GewO](https://www.gesetze-im-internet.de/gewo/__34i.html) (Erlaubnispflicht, Abgrenzung)
- [§ 16 HwO](https://www.gesetze-im-internet.de/hwo/__16.html); [GastG](https://www.gesetze-im-internet.de/gastg/) und Landesgaststättenrecht `[unverifiziert – prüfen]`
- [§ 28 VwVfG](https://www.gesetze-im-internet.de/vwvfg/__28.html), [§ 39 VwVfG](https://www.gesetze-im-internet.de/vwvfg/__39.html), [§ 40 VwVfG](https://www.gesetze-im-internet.de/vwvfg/__40.html)
- [§ 70 VwGO](https://www.gesetze-im-internet.de/vwgo/__70.html), [§ 74 VwGO](https://www.gesetze-im-internet.de/vwgo/__74.html), [§ 80 VwGO](https://www.gesetze-im-internet.de/vwgo/__80.html), [§ 114 VwGO](https://www.gesetze-im-internet.de/vwgo/__114.html); [§ 31 OWiG](https://www.gesetze-im-internet.de/owig_1968/__31.html)

### Kommentare

- Landmann/Rohmer, GewO, §§ 14, 15, 55 ff., 69a.
- Pielow, GewO, § 14, § 55.
- Ennuschat/Wank/Winkler, GewO, § 15, § 70.
- Kopp/Ramsauer, VwVfG, § 40 (Ermessen).

### Rechtsprechung

Zum Gewerbebegriff, zur Abgrenzung des Reisegewerbes und zum Marktprivileg besteht gefestigte Rechtsprechung des BVerwG und der Oberverwaltungsgerichte. Jede konkrete Entscheidung ist vor Verwendung in juris, Beck-Online oder auf bverwg.de zu verifizieren; ohne Beleg gilt sie als `[unverifiziert – prüfen]`.

## Ausgabeformat

```
GEWERBEANZEIGE / REISEGEWERBE — <Mandat> — <Datum>

I.   Anwendbarkeit
     Tätigkeit:               <…>
     Gewerbe iSd GewO:        [ja / nein — freier Beruf / Urproduktion / Vermögensverwaltung]
     Ausnahme § 6 GewO:       [einschlägig — Norm / nicht einschlägig]

II.  Zuordnung
     Gewerbliche Niederlassung § 4 Abs. 3: [vorhanden / nicht vorhanden]
     Vorhergehende Bestellung:             [ja / nein]
     Ergebnis:                [stehendes Gewerbe / Reisegewerbe / gemischt]

III. Stehendes Gewerbe
     Anzeige § 14 Abs. 1:     [erstattet am <Datum> / offen]
     Anzeigeanlass:           <Beginn / Verlegung / Gegenstandswechsel / Namensänderung / Aufgabe>
     Zweigniederlassung / unselbständige Zweigstelle: <…>
     Empfangsbescheinigung § 15 Abs. 1: bis <Datum>
     Zusätzliche Erlaubnis erforderlich: [§ 34a / 34c / 34d / 34f / 34i GewO / keine]
     Handwerksrolle § 16 HwO: [erforderlich / nein]

IV.  Reisegewerbe
     Reisegewerbekarte § 55 Abs. 2: [vorhanden / erforderlich / entbehrlich nach § 55a]
     Verbotene Tätigkeiten § 56:    [betroffen / nicht betroffen]
     Versagungsgründe § 57:         <…>
     Mitführpflicht § 60c:          <…>
     Marktprivileg §§ 69, 69a:      [festgesetzte Veranstaltung — Karte entbehrlich / nein]

V.   Behördliche Maßnahme
     Rechtsgrundlage der Verfügung: <§ 15 Abs. 2 GewO / § 35 GewO / §§ 48, 49 VwVfG>
     Zutreffend gewählt:            [ja / nein — Begründung]
     Ermessen § 15 Abs. 2 / § 40 VwVfG: [ausgeübt und begründet / Ausfall]
     Milderes Mittel:               <Fristsetzung zur Nachholung der Erlaubnis>
     Anhörung § 28 VwVfG:           [erfolgt / unterblieben]

VI.  Rechtsschutz und Sanktionen
     Widerspruch / Klage:     Frist bis <Datum>
     Sofortvollzug:           [angeordnet — § 80 Abs. 3 VwGO tragfähig? / nein]
     Bußgeld:                 <§ 144 / § 145 / § 146 GewO — konkrete Nummer>
     Strafbarkeit § 148 GewO: [bei Fortsetzung trotz vollziehbarer Untersagung]

VII. Risiko: 🟢 / 🟡 / 🔴 <Begründung>
VIII.Quellenverzeichnis
```

## Risiken / typische Fehler

- **§ 15 Abs. 2 GewO und § 35 GewO verwechselt.** § 15 Abs. 2 GewO knüpft an das **Fehlen der Zulassung** an und steht im Ermessen; § 35 GewO knüpft an die **materielle Unzuverlässigkeit** an und ist gebunden, bei erlaubnispflichtigen Gewerben aber nach Abs. 8 gesperrt.
- **Gewerbeanzeige für eine Erlaubnis gehalten.** Die Empfangsbescheinigung nach § 15 Abs. 1 GewO gestattet nichts.
- **Abgrenzung nach § 6 GewO übersprungen.** Freie Berufe, Heilberufe, Rechtsanwälte, Steuerberater und Wirtschaftsprüfer unterfallen der GewO nicht.
- **Reisegewerbe allein nach dem Ort bestimmt.** § 55 Abs. 1 GewO verlangt kumulativ das Fehlen einer **vorhergehenden Bestellung**; eine vom Kunden veranlasste Terminvereinbarung schließt das Reisegewerbe aus.
- **Anzeigepflicht bei Gegenstandswechsel oder Verlegung vergessen.** § 14 Abs. 1 S. 2 GewO erfasst auch diese Fälle sowie Namensänderung und Betriebsaufgabe.
- **Unselbständige Zweigstellen nicht angemeldet.** § 14 Abs. 1 S. 1 GewO nennt sie ausdrücklich.
- **Verbotene Tätigkeiten des § 56 GewO nicht im Wortlaut geprüft.**
- **Marktprivileg unterstellt, ohne die Festsetzung nach § 69 GewO zu belegen.**
- **Gaststättenrecht als Bundesrecht behandelt.** Es ist ganz überwiegend Landesrecht; die konkrete Landesnorm ist zu benennen.
- **Ermessensausfall bei § 15 Abs. 2 GewO nicht gerügt.** Die Norm ist eine Kann-Vorschrift; die Behörde muss ihr Ermessen erkennen und begründen.
- **Rechtsprechung erfunden.** Jede Entscheidung ist zu belegen oder als `[unverifiziert – prüfen]` zu kennzeichnen.

---
name: schiedsvereinbarung-pruefung-borghei
title: /schiedsverfahren-adr:schiedsvereinbarung-pruefung
description: Prüfung und Gestaltung von Schiedsvereinbarungen – Begriff § 1029 ZPO, objektive Schiedsfähigkeit § 1030 mit Unwirksamkeit bei Wohnraummietbestand § 1030 Abs. 2, Form § 1031 einschließlich Verbraucherform Abs. 5 (eigenhändige Urkunde oder elektronische Form nach § 126a BGB) und Heilung durch rügelose Einlassung Abs. 6, Schiedseinrede und Feststellungsantrag § 1032, räumlicher Anwendungsbereich § 1025, Kompetenz-Kompetenz und Rügefristen § 1040, Trennungsprinzip, mehrstufige Streitbeilegungsklauseln, DIS- und ICC-Musterklauseln sowie Mediation nach MediationsG und § 278a ZPO. Use when eine Schiedsklausel entworfen, angegriffen oder verteidigt werden soll oder vor dem staatlichen Gericht die Schiedseinrede im Raum steht.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/schiedsverfahren-adr/skills/schiedsvereinbarung-pruefung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: arbitration
language: de
---

# /schiedsverfahren-adr:schiedsvereinbarung-pruefung

## Zweck

Der Skill prüft eine bestehende Schiedsvereinbarung auf Wirksamkeit, Reichweite und Durchführbarkeit und entwirft, wo nötig, eine tragfähige Ersatzklausel. Er behandelt die drei Angriffspunkte, an denen Schiedsklauseln in der Praxis scheitern — objektive Schiedsfähigkeit, Form und Bestimmtheit — und ordnet die prozessualen Konsequenzen vor dem staatlichen Gericht zu.

## Eingaben

- Wortlaut der Klausel und des Vertrags, in dem sie steht
- Parteien: Kaufleute, Verbraucher, Gesellschaften, öffentliche Hand
- Streitgegenstand: vermögensrechtlich oder nichtvermögensrechtlich; Sonderbereiche
- Vereinbarter Schiedsort und – falls abweichend – Verhandlungsort
- Institution oder Ad-hoc-Verfahren; in Bezug genommene Verfahrensordnung
- Verfahrensstand: Schiedsklage erhoben, staatliche Klage erhoben, Schiedsgericht gebildet
- Bei Klauselgestaltung: gewünschte Sprache, Sitz, Anzahl der Schiedsrichter, Rechtswahl

## Sub-Agent-Architektur

Der Researcher beschafft die Normen des Zehnten Buchs, die einschlägige Verfahrensordnung (DIS-SchiedsO 2018, ICC-SchiedsO) und die Rechtsprechung der Oberlandesgerichte und des BGH zur Wirksamkeit von Schiedsklauseln. Der Drafter prüft Wirksamkeit, Reichweite und Durchführbarkeit und formuliert die Klausel oder den Schriftsatz. Der Reviewer kontrolliert die Formprüfung, die Rügefristen des § 1040 Abs. 2 und ob die Schiedseinrede rechtzeitig erhoben wurde.

> **Hinweis zum Rechtsstand.** Das Zehnte Buch der ZPO ist Gegenstand des Gesetzes vom 20.05.2026 (BGBl. 2026 I Nr. 152); die Änderungen sind auf gesetze-im-internet.de textlich nachgewiesen, dokumentarisch aber noch nicht abschließend eingearbeitet. Vor jeder Verwendung ist der konsolidierte Stand gegen das Bundesgesetzblatt abzugleichen `[unverifiziert – prüfen]`.

## Ablauf

### 1. Räumlichen Anwendungsbereich bestimmen ([§ 1025 ZPO](https://www.gesetze-im-internet.de/zpo/__1025.html))

- **Abs. 1** — Das Zehnte Buch gilt, wenn der **Ort des schiedsrichterlichen Verfahrens** (§ 1043 Abs. 1) in Deutschland liegt. Maßgeblich ist der rechtliche Schiedsort, nicht der tatsächliche Verhandlungsort.
- **Abs. 2** — §§ 1032, 1033 und 1050 gelten **auch**, wenn der Schiedsort im Ausland liegt oder noch nicht bestimmt ist. Die Schiedseinrede und der einstweilige Rechtsschutz vor deutschen Gerichten stehen also auch bei Auslandsschiedsverfahren zur Verfügung.
- **Abs. 3** — Solange der Schiedsort nicht bestimmt ist, sind deutsche Gerichte für die Aufgaben nach §§ 1034, 1035, 1037, 1038 zuständig, wenn Kläger oder Beklagter Sitz oder gewöhnlichen Aufenthalt in Deutschland hat.
- **Abs. 4** — Für ausländische Schiedssprüche gelten §§ 1061 bis 1065 (`/schiedsverfahren-adr:vollstreckbarerklaerung-schiedsspruch`).

### 2. Begriff und Erscheinungsform prüfen ([§ 1029 ZPO](https://www.gesetze-im-internet.de/zpo/__1029.html))

Eine Schiedsvereinbarung unterwirft alle oder einzelne Streitigkeiten aus einem **bestimmten Rechtsverhältnis** — vertraglicher oder nichtvertraglicher Art, entstanden oder künftig — der Entscheidung durch ein Schiedsgericht. Sie kann als selbständige **Schiedsabrede** oder als **Schiedsklausel** im Vertrag geschlossen werden (Abs. 2).

Zwei Konsequenzen:

- Das Erfordernis eines **bestimmten Rechtsverhältnisses** schließt Globalklauseln für „alle künftigen Streitigkeiten zwischen den Parteien" ohne Bezugspunkt aus.
- Erfasst sind auch **außervertragliche** Ansprüche, soweit sie in Bezug auf dasselbe Rechtsverhältnis stehen — deliktische und bereicherungsrechtliche Ansprüche fallen bei entsprechender Formulierung darunter.

### 3. Objektive Schiedsfähigkeit prüfen ([§ 1030 ZPO](https://www.gesetze-im-internet.de/zpo/__1030.html))

- **Abs. 1 S. 1** — **Jeder vermögensrechtliche Anspruch** ist schiedsfähig. Das ist der Regelfall im Wirtschaftsrecht.
- **Abs. 1 S. 2** — Nichtvermögensrechtliche Ansprüche sind schiedsfähig, soweit die Parteien über den Streitgegenstand **einen Vergleich schließen** dürfen.
- **Abs. 2** — Eine Schiedsvereinbarung über Rechtsstreitigkeiten, die den **Bestand eines Mietverhältnisses über Wohnraum im Inland** betreffen, ist **unwirksam**; ausgenommen ist Wohnraum der in § 549 Abs. 2 Nr. 1 bis 3 BGB bezeichneten Art.
- **Abs. 3** — Gesetzliche Schiedsverbote außerhalb des Zehnten Buchs bleiben unberührt. Sonderbereiche wie das Arbeitsrecht (§ 4 ArbGG), das Familien- und Statusrecht sowie kartell- und aufsichtsrechtliche Sonderregelungen sind gesondert zu prüfen und konkret zu benennen `[unverifiziert – prüfen]` je Sonderbereich.

### 4. Form prüfen ([§ 1031 ZPO](https://www.gesetze-im-internet.de/zpo/__1031.html))

| Konstellation | Anforderung |
|---|---|
| **Abs. 1** — Regelfall | Enthalten in einem von den Parteien **unterzeichneten Dokument** oder in gewechselten Schreiben, Fernkopien, Telegrammen oder anderen Übermittlungsformen, die einen **Nachweis der Vereinbarung sicherstellen** |
| **Abs. 2** — kaufmännisches Bestätigungsschreiben | Form gewahrt, wenn die Vereinbarung in einem übermittelten Dokument enthalten ist und dessen Inhalt bei nicht rechtzeitigem Widerspruch **nach der Verkehrssitte** als Vertragsinhalt gilt |
| **Abs. 3** — Bezugnahme | Ein formwirksamer Vertrag, der auf ein Dokument mit Schiedsklausel Bezug nimmt, begründet die Schiedsvereinbarung, wenn die Bezugnahme die Klausel **zum Vertragsbestandteil macht** |
| **Abs. 5** — **Beteiligung eines Verbrauchers** | **Eigenhändig unterzeichnete Urkunde**; die Schriftform kann durch die **elektronische Form nach [§ 126a BGB](https://www.gesetze-im-internet.de/bgb/__126a.html)** ersetzt werden. Die Urkunde bzw. das elektronische Dokument darf **keine anderen Vereinbarungen** als solche zum schiedsrichterlichen Verfahren enthalten — außer bei notarieller Beurkundung |
| **Abs. 6** — Heilung | Der Formmangel wird durch **Einlassung zur Hauptsache** im schiedsrichterlichen Verfahren geheilt |

**§ 1031 Abs. 5 ist der häufigste Unwirksamkeitsgrund in Verbraucherkonstellationen.** Eine Schiedsklausel in AGB, im Kaufvertrag oder im Anlageprospekt genügt nicht; erforderlich ist eine separate, ausschließlich das Schiedsverfahren betreffende Urkunde. Die Verbrauchereigenschaft ist nach §§ 13, 14 BGB zu bestimmen.

### 5. Reichweite und Bestimmtheit prüfen — pathologische Klauseln

Typische Mängel und ihre Behandlung:

| Mangel | Folge |
|---|---|
| Institution ungenau oder nicht existent bezeichnet | Auslegung nach §§ 133, 157 BGB; bei Unauflösbarkeit Undurchführbarkeit iSd § 1032 Abs. 1 |
| Schiedsort fehlt | § 1043 Abs. 1: Bestimmung durch das Schiedsgericht; Klausel bleibt wirksam |
| Zahl der Schiedsrichter fehlt | § 1034 Abs. 1 S. 2: **drei** Schiedsrichter |
| Optionale Formulierung („können ein Schiedsgericht anrufen") | keine ausschließliche Schiedsvereinbarung; staatlicher Rechtsweg bleibt offen |
| Asymmetrische Klausel (nur eine Partei kann wählen) | Wirksamkeit nach §§ 138, 307 BGB streitig; im Verbraucher- und AGB-Kontext hohes Risiko `[unverifiziert – prüfen]` |
| Übergewicht bei der Schiedsrichterbestellung | **§ 1034 Abs. 2 ZPO**: gerichtliche Ersatzbestellung auf Antrag binnen **zwei Wochen** ab Kenntnis der Zusammensetzung |

**Trennungsprinzip:** Nach [§ 1040 Abs. 1 S. 2 ZPO](https://www.gesetze-im-internet.de/zpo/__1040.html) ist die Schiedsklausel als von den übrigen Vertragsbestimmungen **unabhängige Vereinbarung** zu behandeln. Die Unwirksamkeit des Hauptvertrags erfasst die Schiedsklausel daher nicht ohne Weiteres.

### 6. Prozessuale Durchsetzung ([§ 1032 ZPO](https://www.gesetze-im-internet.de/zpo/__1032.html), [§ 1040 ZPO](https://www.gesetze-im-internet.de/zpo/__1040.html))

- **§ 1032 Abs. 1** — Wird vor dem staatlichen Gericht Klage in einer Sache erhoben, die Gegenstand einer Schiedsvereinbarung ist, weist das Gericht die Klage als **unzulässig** ab, sofern der Beklagte dies **vor Beginn der mündlichen Verhandlung zur Hauptsache** rügt und die Vereinbarung nicht nichtig, unwirksam oder undurchführbar ist. **Die Rüge ist präkludierbar** — sie gehört in die Klageerwiderung.
- **§ 1032 Abs. 2** — Bis zur **Bildung des Schiedsgerichts** kann bei Gericht die Feststellung der Zulässigkeit oder Unzulässigkeit des schiedsrichterlichen Verfahrens beantragt werden. Zuständig ist das OLG (§ 1062 Abs. 1 Nr. 2).
- **§ 1032 Abs. 3** — Das Schiedsverfahren kann trotz anhängigen staatlichen Verfahrens eingeleitet oder fortgesetzt werden; ein Schiedsspruch kann ergehen.
- **§ 1040 Abs. 2** — Die Rüge der Unzuständigkeit ist **spätestens mit der Klagebeantwortung** vorzubringen; die Rüge der Befugnisüberschreitung, sobald die Angelegenheit erörtert wird. Die Mitwirkung an der Schiedsrichterbestellung schließt die Rüge nicht aus.
- **§ 1040 Abs. 3** — Bejaht das Schiedsgericht seine Zuständigkeit durch **Zwischenentscheid**, kann jede Partei binnen **eines Monats** ab schriftlicher Mitteilung die gerichtliche Entscheidung beantragen; das Schiedsverfahren darf fortgesetzt werden.

### 7. Mehrstufige Streitbeilegung und Mediation

Mehrstufige Klauseln (Verhandlung → Mediation → Schiedsverfahren) sind zulässig; ihre Verbindlichkeit hängt von der Formulierung ab. Zu regeln sind: Auslöser, Frist je Stufe, Folge des Fristablaufs und ausdrücklich, ob die Vorstufe **Zulässigkeitsvoraussetzung** des Schiedsverfahrens ist. Fehlt diese Anordnung, ist die Vorstufe im Zweifel bloße Obliegenheit.

Flankierend:

- [MediationsG](https://www.gesetze-im-internet.de/mediationsg/) – [§ 1](https://www.gesetze-im-internet.de/mediationsg/__1.html) (Begriff), [§ 2](https://www.gesetze-im-internet.de/mediationsg/__2.html) (Verfahren), [§ 4](https://www.gesetze-im-internet.de/mediationsg/__4.html) (Verschwiegenheit)
- [§ 278a ZPO](https://www.gesetze-im-internet.de/zpo/__278a.html) — Vorschlag des Gerichts, Mediation oder ein anderes Verfahren der außergerichtlichen Konfliktbeilegung durchzuführen; Anordnung des Ruhens des Verfahrens
- [§ 203 BGB](https://www.gesetze-im-internet.de/bgb/__203.html) — **Verjährungshemmung** bei schwebenden Verhandlungen. Die Vorstufe darf nicht dazu führen, dass Ansprüche verjähren; die Hemmung ist zu dokumentieren.

### 8. Klauselgestaltung

Eine tragfähige Klausel regelt mindestens: Institution oder Ad-hoc, in Bezug genommene Verfahrensordnung, **Schiedsort**, Zahl der Schiedsrichter, Verfahrenssprache, auf die Hauptsache anwendbares Recht und – falls gewünscht – Vertraulichkeit und Zustellungsregeln. Für institutionelle Verfahren sind die **Musterklauseln der Institution** zu verwenden und nur bewusst zu ändern; jede Abweichung erzeugt Auslegungsrisiko.

## Deterministische Berechnung

Die Fristen dieses Skills sind kurz und leicht zu versäumen. Der Rechner in [`../../../scripts/legal_calc/`](../../../scripts/legal_calc/) macht nur die Arithmetik:

```bash
# § 1034 Abs. 2 ZPO: 2 Wochen ab Kenntnis der Zusammensetzung am 10.03.2026
python -m scripts.legal_calc.cli frist --ereignis 10.03.2026 --menge 2 --einheit wochen --land BY

# § 1040 Abs. 3 S. 2 ZPO: 1 Monat ab Mitteilung des Zwischenentscheids
python -m scripts.legal_calc.cli frist --ereignis 12.05.2026 --menge 1 --einheit monate --land BY

# Verjährung des Hauptanspruchs trotz laufender Verhandlungsstufe (§§ 195, 199, 203 BGB)
python -m scripts.legal_calc.cli verjaehrung --entstehung 15.06.2023 --kenntnis 15.06.2023
```

Ob eine Klausel „undurchführbar" iSd § 1032 Abs. 1 ist, bleibt eine juristische Wertung.

## Quellen

### Statute

- [§ 1025](https://www.gesetze-im-internet.de/zpo/__1025.html), [§ 1029](https://www.gesetze-im-internet.de/zpo/__1029.html), [§ 1030](https://www.gesetze-im-internet.de/zpo/__1030.html), [§ 1031](https://www.gesetze-im-internet.de/zpo/__1031.html), [§ 1032](https://www.gesetze-im-internet.de/zpo/__1032.html), [§ 1033](https://www.gesetze-im-internet.de/zpo/__1033.html), [§ 1034 ZPO](https://www.gesetze-im-internet.de/zpo/__1034.html), [§ 1040](https://www.gesetze-im-internet.de/zpo/__1040.html), [§ 1043 ZPO](https://www.gesetze-im-internet.de/zpo/__1043.html), [§ 1062 ZPO](https://www.gesetze-im-internet.de/zpo/__1062.html), [§ 278a ZPO](https://www.gesetze-im-internet.de/zpo/__278a.html)
- [§ 126a BGB](https://www.gesetze-im-internet.de/bgb/__126a.html), [§ 138 BGB](https://www.gesetze-im-internet.de/bgb/__138.html), [§ 203 BGB](https://www.gesetze-im-internet.de/bgb/__203.html), [§ 307 BGB](https://www.gesetze-im-internet.de/bgb/__307.html), [§ 549 BGB](https://www.gesetze-im-internet.de/bgb/__549.html)
- [MediationsG](https://www.gesetze-im-internet.de/mediationsg/)
- [§ 4 ArbGG](https://www.gesetze-im-internet.de/arbgg/__4.html)
- DIS-Schiedsgerichtsordnung 2018 und ICC-Schiedsgerichtsordnung (Institutionenrecht, nicht auf gesetze-im-internet.de) `[unverifiziert – prüfen]` hinsichtlich der jeweils geltenden Fassung

### Kommentare

- Zöller/Geimer, ZPO, §§ 1029–1032, 1040.
- Musielak/Voit, ZPO, § 1031 Rn. 1 ff. (Formfragen, Verbraucherbeteiligung).
- Stein/Jonas/Schlosser, ZPO, Zehntes Buch.
- Schwab/Walter, Schiedsgerichtsbarkeit, Kap. zur Schiedsvereinbarung.
- Prütting/Gehrlein, ZPO, § 1030, § 1032.

### Rechtsprechung

Zur Wirksamkeit und Reichweite von Schiedsvereinbarungen besteht gefestigte Rechtsprechung des BGH und der Oberlandesgerichte, insbesondere zur Formstrenge des § 1031 Abs. 5 ZPO, zur Auslegung pathologischer Klauseln und zur Präklusion der Schiedseinrede nach § 1032 Abs. 1 ZPO. Jede konkrete Entscheidung ist vor Verwendung in juris, Beck-Online oder auf den Seiten des BGH zu verifizieren; ohne Beleg gilt sie als `[unverifiziert – prüfen]`.

## Ausgabeformat

```
SCHIEDSVEREINBARUNG — <Mandat> — <Datum>

I.   Klausel und Rahmen
     Wortlaut:                <Zitat>
     Parteien:                <Kaufleute / Verbraucher beteiligt>
     Schiedsort:              <Ort>  → § 1025 Abs. 1: [Zehntes Buch anwendbar / Abs. 2]
     Institution / Ad-hoc:    <…>   Verfahrensordnung: <…>

II.  Wirksamkeit
     § 1029 bestimmtes Rechtsverhältnis:  [ja / nein]
     § 1030 Schiedsfähigkeit:             [vermögensrechtlich / vergleichsfähig / gesperrt]
       Abs. 2 Wohnraummiete:              [einschlägig — unwirksam / nein]
       Abs. 3 Sonderverbot:               <Norm / keines>
     § 1031 Form:                         [Abs. 1 / Abs. 2 / Abs. 3 / Abs. 5]
       Verbraucherform Abs. 5 gewahrt:    [ja / nein — separate Urkunde fehlt]
       Heilung Abs. 6:                    [eingetreten / nein]
     Trennungsprinzip § 1040 Abs. 1 S. 2: <Auswirkung>

III. Reichweite und Durchführbarkeit
     Erfasste Ansprüche:      <vertraglich / deliktisch / bereicherungsrechtlich>
     Pathologien:             <…>
     Undurchführbarkeit § 1032 Abs. 1: [ja / nein]
     Übergewicht § 1034 Abs. 2: [ja — Frist 2 Wochen bis <Datum> / nein]

IV.  Prozessuale Lage
     Staatliche Klage:        [anhängig — Schiedseinrede bis <Zeitpunkt> / nein]
     Feststellungsantrag § 1032 Abs. 2: [statthaft bis Bildung des Schiedsgerichts / verfristet]
     Zuständiges OLG § 1062:  <…>
     Rüge § 1040 Abs. 2:      [erhoben mit Klagebeantwortung / offen]
     Zwischenentscheid § 1040 Abs. 3: Frist 1 Monat bis <Datum>

V.   Mehrstufigkeit und Verjährung
     Vorstufen:               <Verhandlung / Mediation>  Zulässigkeitsvoraussetzung: [ja / nein]
     Verjährungshemmung § 203 BGB: <dokumentiert / offen>

VI.  Empfehlung
     [Schiedseinrede erheben / Feststellungsantrag / Klausel neu fassen — Entwurf unten]

VII. Risiko: 🟢 / 🟡 / 🔴 <Begründung>
VIII.Quellenverzeichnis
```

### Formulierungshilfe — Schiedsklausel (Gerüst, institutionell)

```
Alle Streitigkeiten, die sich aus oder im Zusammenhang mit diesem Vertrag
ergeben, einschließlich Streitigkeiten über seine Wirksamkeit, seinen
Abschluss und seine Beendigung sowie über außervertragliche Ansprüche im
Zusammenhang mit diesem Vertrag, werden nach der Schiedsgerichtsordnung
der <Institution> unter Ausschluss des ordentlichen Rechtswegs endgültig
entschieden.

  Schiedsort:              <Ort>, Deutschland
  Zahl der Schiedsrichter: <eins / drei>
  Verfahrenssprache:       <Deutsch / Englisch>
  Anwendbares Recht:       deutsches Recht unter Ausschluss des UN-Kaufrechts
  Vertraulichkeit:         <Regelung>

[Bei Verbraucherbeteiligung: Diese Vereinbarung ist in einer gesonderten,
von den Parteien eigenhändig unterzeichneten Urkunde zu treffen, die keine
anderen Vereinbarungen enthält (§ 1031 Abs. 5 ZPO); die Schriftform kann
durch die elektronische Form nach § 126a BGB ersetzt werden.]
```

## Risiken / typische Fehler

- **Verbraucherform des § 1031 Abs. 5 ZPO missachtet.** Eine Schiedsklausel in AGB oder im Hauptvertrag ist bei Verbraucherbeteiligung formunwirksam; erforderlich ist eine gesonderte Urkunde, die nur das Schiedsverfahren betrifft.
- **Schiedseinrede zu spät erhoben.** § 1032 Abs. 1 ZPO verlangt die Rüge **vor Beginn der mündlichen Verhandlung zur Hauptsache**; danach ist sie präkludiert.
- **Zuständigkeitsrüge im Schiedsverfahren versäumt.** § 1040 Abs. 2 ZPO setzt die Klagebeantwortung als Grenze.
- **Monatsfrist des § 1040 Abs. 3 S. 2 ZPO verstreichen lassen.** Der Zwischenentscheid wird sonst faktisch bestandskräftig.
- **Zweiwochenfrist des § 1034 Abs. 2 ZPO übersehen**, wenn die Klausel einer Partei ein Übergewicht bei der Bestellung gibt.
- **Schiedsort mit Verhandlungsort verwechselt.** § 1025 Abs. 1 iVm § 1043 Abs. 1 ZPO knüpft an den rechtlichen Schiedsort an; er bestimmt lex arbitri und OLG-Zuständigkeit.
- **§ 1030 Abs. 2 ZPO übersehen.** Schiedsvereinbarungen über den Bestand von Wohnraummietverhältnissen im Inland sind unwirksam.
- **Trennungsprinzip ignoriert.** Die Unwirksamkeit des Hauptvertrags erfasst die Schiedsklausel nicht automatisch (§ 1040 Abs. 1 S. 2 ZPO).
- **Mehrstufige Klausel ohne Rechtsfolgenanordnung.** Ohne ausdrückliche Regelung ist die Vorstufe im Zweifel keine Zulässigkeitsvoraussetzung — und die Verjährung läuft weiter.
- **Rechtsprechung erfunden.** Jede Entscheidung ist zu belegen oder als `[unverifiziert – prüfen]` zu kennzeichnen.

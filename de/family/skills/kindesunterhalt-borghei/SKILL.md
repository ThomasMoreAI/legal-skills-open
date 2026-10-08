---
name: kindesunterhalt-borghei
title: /familienrecht:kindesunterhalt
description: Prüfung und Berechnung des Kindesunterhalts – Verwandtenunterhalt §§ 1601 ff. BGB, gesteigerte Erwerbsobliegenheit und Selbstbehalt § 1603 BGB, Mindestunterhalt § 1612a BGB nach der Düsseldorfer Tabelle, Kindergeldanrechnung § 1612b BGB, Rangfolge und Mangelfall § 1609 BGB, Bar- und Betreuungsunterhalt § 1606 BGB. Use when der Unterhalt für ein minderjähriges oder privilegiertes volljähriges Kind zu berechnen oder zu prüfen ist.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/familienrecht/skills/kindesunterhalt
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: family
language: de
---

# /familienrecht:kindesunterhalt

## Zweck

Der Kindesunterhalt ist der wirtschaftlich folgenreichste Dauerschuldverhältnis-Streit nach Trennung und Scheidung. Fehler bei der Einstufung in die Düsseldorfer Tabelle, bei der Kindergeldanrechnung oder beim Selbstbehalt summieren sich über Jahre zu vier- bis fünfstelligen Beträgen. Dieser Skill strukturiert die Anspruchsprüfung dem Grunde nach und die Bezifferung der Höhe, einschließlich Mangelfall und Rangfolge.

## Eingaben

- Alter des Kindes (Altersstufe nach § 1612a BGB; minderjährig oder privilegiert volljährig?)
- Wer betreut, wer ist barunterhaltspflichtig (Residenz- oder Wechselmodell?)
- Bereinigtes Nettoeinkommen des barunterhaltspflichtigen Elternteils (nach Abzug berücksichtigungsfähiger Verbindlichkeiten und berufsbedingter Aufwendungen)
- Weitere Unterhaltspflichten (andere Kinder, Ehegatte) für Rangfolge und Mangelfall
- Kindergeldbezug (wer zieht es, in welcher Höhe?)
- Sonderbedarf / Mehrbedarf (Kita, Krankheit) – gesondert

## Sub-Agent-Architektur

Die Prüfung wird in einer Pipeline organisiert. Ein erster Schritt klärt den Anspruch dem Grunde nach (Verwandtschaft, Bedürftigkeit, Bar- vs. Betreuungsanteil). Ein Rechen-Schritt stuft das bereinigte Nettoeinkommen in die Einkommensgruppe und Altersstufe der Düsseldorfer Tabelle ein, ermittelt den Tabellenbetrag und rechnet das Kindergeld an. Ein Kontroll-Schritt prüft Leistungsfähigkeit, Selbstbehalt sowie – bei mehreren Berechtigten – Rangfolge und Mangelfall. Jeder Schritt benennt seine Norm und markiert jahresabhängige EUR-Werte als prüfbedürftig, bevor der nächste übernimmt.

## Ablauf

### 1. Unterhaltsanspruch dem Grunde nach (§§ 1601, 1602 BGB)

Verwandte in gerader Linie schulden einander Unterhalt ([§ 1601 BGB](https://www.gesetze-im-internet.de/bgb/__1601.html)). Das minderjährige Kind ist unterhaltsberechtigt, weil es seinen Unterhalt nicht aus eigenen Einkünften oder Vermögen bestreiten kann ([§ 1602 BGB](https://www.gesetze-im-internet.de/bgb/__1602.html)). Bei minderjährigen Kindern wird die Bedürftigkeit grundsätzlich vermutet; eigenes Vermögensstamm-Verbrauch wird ihnen anders als Volljährigen nicht zugemutet.

Privilegiert volljährige Kinder (bis 21 Jahre, im Haushalt eines Elternteils, allgemeine Schulausbildung, § 1603 Abs. 2 S. 2 BGB) sind den minderjährigen weitgehend gleichgestellt.

### 2. Bar- vs. Betreuungsunterhalt (§ 1606 Abs. 3 BGB)

Bei getrenntlebenden Eltern gilt das Residenzmodell: Der betreuende Elternteil erfüllt seine Unterhaltspflicht **in der Regel durch die Pflege und die Erziehung des Kindes** (Betreuungsunterhalt, [§ 1606 Abs. 3 S. 2 BGB](https://www.gesetze-im-internet.de/bgb/__1606.html)). Der andere Elternteil schuldet **Barunterhalt** in Geld. Bar- und Betreuungsunterhalt sind grundsätzlich gleichwertig.

Im echten Wechselmodell (annähernd hälftige Betreuung) haften beide Eltern anteilig nach ihren Einkommensverhältnissen barunterhaltspflichtig – dann gesonderte Quotenberechnung.

### 3. Mindestunterhalt und Einstufung Düsseldorfer Tabelle (§ 1612a BGB)

Der Mindestunterhalt bemisst sich nach [§ 1612a BGB](https://www.gesetze-im-internet.de/bgb/__1612a.html) als Prozentsatz des steuerlichen Kinderfreibetrags-Existenzminimums, gestaffelt nach drei Altersstufen:

| Altersstufe | Alter | Prozentsatz des Mindestunterhalts |
|---|---|---|
| 1. Stufe | bis 5 Jahre (bis Vollendung 6. Lebensjahr) | 87 % |
| 2. Stufe | 6–11 Jahre (bis Vollendung 12. Lebensjahr) | 100 % |
| 3. Stufe | ab 12 Jahre (ab 13. Lebensjahr) | 117 % |

Die konkreten EUR-Beträge je Altersstufe ergeben sich aus der **Mindestunterhaltsverordnung (MinUhV)** und werden jährlich angepasst `[unverifiziert – aktuelle MinUhV/Tabelle prüfen]`.

Die **Düsseldorfer Tabelle** konkretisiert darüber hinaus die Unterhaltshöhe oberhalb des Mindestunterhalts. Sie ist eine **Leitlinie der Oberlandesgerichte (kein Gesetz)**, keine bindende Rechtsnorm, wird aber bundesweit angewandt. Einstufung:

1. **Einkommensgruppe** nach bereinigtem Nettoeinkommen des Barpflichtigen (Stufe 1 ab Mindestunterhalt, höhere Stufen prozentual aufsteigend).
2. **Altersstufe** des Kindes (siehe Tabelle oben).
3. Ablesen des Tabellen-Zahlbetrags. Die konkreten EUR-Werte der jeweiligen Tabelle sind jahresabhängig `[unverifiziert – jeweils aktuelle Düsseldorfer Tabelle des Stichjahres heranziehen]`.

### 4. Kindergeldanrechnung (§ 1612b BGB)

Das Kindergeld mindert den Barbedarf des Kindes ([§ 1612b BGB](https://www.gesetze-im-internet.de/bgb/__1612b.html)):

- **Halbes Kindergeld** wird angerechnet, wenn ein Elternteil seine Unterhaltspflicht durch Betreuung erfüllt (§ 1606 Abs. 3 S. 2 BGB) – der Regelfall beim minderjährigen Kind im Residenzmodell. Die andere Hälfte verbleibt beim betreuenden Elternteil als Ausgleich für die Betreuungsleistung.
- **Volles Kindergeld** wird in allen übrigen Fällen angerechnet (z. B. volljähriges Kind).

```
Zahlbetrag = Tabellenbetrag − (halbes bzw. volles Kindergeld)
```

Die Kindergeldhöhe ist jahresabhängig `[unverifiziert – aktuellen Kindergeldsatz prüfen]`.

### 5. Leistungsfähigkeit, gesteigerte Erwerbsobliegenheit, Selbstbehalt (§ 1603 BGB)

Unterhalt schuldet nur, wer leistungsfähig ist, d. h. ohne Gefährdung seines eigenen angemessenen Unterhalts ([§ 1603 Abs. 1 BGB](https://www.gesetze-im-internet.de/bgb/__1603.html)).

Gegenüber **minderjährigen und privilegiert volljährigen Kindern** trifft den Pflichtigen jedoch eine **gesteigerte Verpflichtung** (§ 1603 Abs. 2 BGB): Er muss alle verfügbaren Mittel gleichmäßig für sich und das Kind einsetzen und unterliegt einer **gesteigerten Erwerbsobliegenheit** (Pflicht, vorhandene Erwerbsmöglichkeiten – ggf. Nebentätigkeit, Ortswechsel – auszuschöpfen; sonst wird fiktives Einkommen zugerechnet).

Ihm verbleibt nur der **notwendige Selbstbehalt** (nicht der höhere angemessene Selbstbehalt). Die konkreten Selbstbehaltssätze (erwerbstätig / nicht erwerbstätig) stehen in der Düsseldorfer Tabelle und sind jahresabhängig `[unverifiziert – aktuellen notwendigen Selbstbehalt prüfen]`.

### 6. Rangfolge und Mangelfall (§ 1609 BGB)

Reicht das Einkommen nicht für alle Berechtigten, gilt die Rangfolge des [§ 1609 BGB](https://www.gesetze-im-internet.de/bgb/__1609.html):

1. minderjährige und privilegiert volljährige Kinder
2. betreuende Elternteile / Ehegatten bei langer Ehe
3. sonstige (geschiedene) Ehegatten
4. übrige (nicht privilegierte volljährige) Kinder

Im **Mangelfall** (verteilungsfähige Masse unterhalb des Selbstbehalts deckt nicht alle Erstrang-Ansprüche) wird die zur Verfügung stehende Masse quotal auf die gleichrangig Berechtigten verteilt; nachrangige Berechtigte gehen leer aus.

### 7. Ergebnis

Zahlbetrag des Barunterhalts beziffern (Tabellenbetrag der einschlägigen Einkommensgruppe/Altersstufe abzüglich anzurechnenden Kindergelds), Leistungsfähigkeit und Selbstbehalt gegenrechnen, Rang/Mangelfall berücksichtigen. Sonder- und Mehrbedarf gesondert ausweisen. Dynamisierung als Prozentsatz des Mindestunterhalts (§ 1612a BGB) empfehlen, damit der Titel altersstufen- und tabellenautomatisch fortschreibt.

## Risiken

- **Falsche Altersstufe** – Stufenwechsel tritt zum Monatsbeginn des Geburtstagsmonats ein (§ 1612a BGB); zu früh/spät eingestuft.
- **Kindergeldanrechnung falsch** – beim minderjährigen Kind im Residenzmodell nur **halbes** Kindergeld, nicht volles (§ 1612b BGB).
- **Selbstbehalt verwechselt** – gegenüber Minderjährigen gilt der niedrigere **notwendige** Selbstbehalt (§ 1603 Abs. 2 BGB), nicht der angemessene.
- **Düsseldorfer Tabelle als Gesetz behandelt** – sie ist OLG-Leitlinie ohne Gesetzeskraft; EUR-Beträge jährlich neu.
- **Gesteigerte Erwerbsobliegenheit übersehen** – unzureichendes Realeinkommen wird durch fiktives Einkommen ersetzt.
- **Mangelfall / Rangfolge nicht geprüft** – bei mehreren Berechtigten gehen Erstrang-Kinder vor (§ 1609 BGB).
- **Veraltete Tabellenwerte** – immer die Düsseldorfer Tabelle und MinUhV des maßgeblichen Jahres heranziehen.

## Quellen

### Statute

- [§ 1601 BGB](https://www.gesetze-im-internet.de/bgb/__1601.html) (Unterhaltsverpflichtete / Verwandtenunterhalt)
- [§ 1602 BGB](https://www.gesetze-im-internet.de/bgb/__1602.html) (Bedürftigkeit)
- [§ 1603 BGB](https://www.gesetze-im-internet.de/bgb/__1603.html) (Leistungsfähigkeit, gesteigerte Verpflichtung, Selbstbehalt)
- [§ 1606 BGB](https://www.gesetze-im-internet.de/bgb/__1606.html) (Rangverhältnisse; Betreuungsunterhalt Abs. 3 S. 2)
- [§ 1609 BGB](https://www.gesetze-im-internet.de/bgb/__1609.html) (Rangfolge mehrerer Unterhaltsberechtigter, Mangelfall)
- [§ 1612a BGB](https://www.gesetze-im-internet.de/bgb/__1612a.html) (Mindestunterhalt minderjähriger Kinder; Altersstufen)
- [§ 1612b BGB](https://www.gesetze-im-internet.de/bgb/__1612b.html) (Deckung des Barbedarfs durch Kindergeld)
- [MinUhV](https://www.gesetze-im-internet.de/minuhv/) (Mindestunterhaltsverordnung – jährlich)

### Leitlinien (kein Gesetz)

- **Düsseldorfer Tabelle** des OLG Düsseldorf (Unterhaltsleitlinie; EUR-Beträge jahresabhängig) `[unverifiziert – aktuelle Fassung prüfen]`
- Unterhaltsrechtliche Leitlinien der jeweiligen OLG

### Kommentare

- Born, in: MüKoBGB, 9. Aufl. 2024, §§ 1601 ff.
- Wendl/Dose, Das Unterhaltsrecht in der familienrichterlichen Praxis

## Ausgabeformat

```
KINDESUNTERHALT-BERECHNUNG — <Mandat> — <Datum>

I.    Anspruch dem Grunde nach
      Verwandtschaft gerade Linie:    § 1601 BGB  [ja]
      Bedürftigkeit Kind:             § 1602 BGB  [ja / minderjährig vermutet]
      Status:                         [minderjährig / privilegiert volljährig]
II.   Bar- vs. Betreuungsunterhalt
      Betreuung (§ 1606 Abs. 3):      <Elternteil>
      Barpflichtig:                   <Elternteil>
      Modell:                         [Residenz / Wechsel]
III.  Einstufung Düsseldorfer Tabelle  [Leitlinie, kein Gesetz]
      Bereinigtes Netto:              <EUR>
      Einkommensgruppe:               <Stufe>
      Altersstufe (§ 1612a):          <1 / 2 / 3>
      Tabellenbetrag:                 <EUR>  [unverifiziert – Jahr prüfen]
IV.   Kindergeldanrechnung § 1612b
      Kindergeld:                     <EUR>  [unverifiziert]
      Anrechnung:                     [halb / voll]
      Zahlbetrag:                     <EUR>
V.    Leistungsfähigkeit § 1603
      Notwendiger Selbstbehalt:       <EUR>  [unverifiziert]
      Gesteigerte Erwerbsobliegenheit: [geprüft]
      Leistungsfähig:                 [ja / Mangelfall]
VI.   Rang / Mangelfall § 1609
      Weitere Berechtigte:            <…>
      Verteilung:                     [voll / quotal]
VII.  Ergebnis
      Monatlicher Barunterhalt:       <EUR>
      Dynamisierung (% Mindestunterhalt): [empfohlen]
      Sonder-/Mehrbedarf:             <…>
```

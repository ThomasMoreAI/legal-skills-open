---
name: cmr-grenzueberschreitender-transport-borghei
title: /transportrecht:cmr-grenzueberschreitender-transport
description: Prüfung der Frachtführerhaftung im grenzüberschreitenden Straßengüterverkehr nach CMR – Anwendungsbereich Art. 1, Frachtbrief Art. 4–9, Obhutshaftung Art. 17, Höchstbetrag 8,33 SZR/kg Art. 23, Durchbruch Art. 29, Schadensanzeige Art. 30, Gerichtsstand Art. 31, Verjährung Art. 32. Use when eine entgeltliche Beförderung per LKW über mind. eine Staatsgrenze geht und einer der Staaten Vertragsstaat der CMR ist.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/transportrecht/skills/cmr-grenzueberschreitender-transport
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: transportation
language: de
---

# /transportrecht:cmr-grenzueberschreitender-transport

## Zweck

Der Skill prüft die Haftung des Frachtführers bei grenzüberschreitenden Straßenbeförderungen nach dem Übereinkommen über den Beförderungsvertrag im internationalen Straßengüterverkehr (CMR, BGBl. 1961 II S. 1119), das in Deutschland als innerstaatlich anwendbares Bundesrecht gilt und dem HGB-Frachtrecht für seinen Anwendungsbereich vorgeht. Er adressiert Anwendungsbereich, Frachtbrief, Obhutshaftung, Haftungsausschlüsse, den mit § 431 HGB identischen Höchstbetrag von 8,33 SZR/kg, qualifiziertes Verschulden, Schadensanzeige, Gerichtsstand und Verjährung.

## Eingaben

- Beförderungsweg (Versendungs- und Ablieferungsort – mind. einer in einem Vertragsstaat der CMR, mind. eine Staatsgrenze überquert)
- Versender, Frachtführer (ggf. Unterfrachtführer Art. 34 ff. CMR), Empfänger
- Frachtbriefangaben (CMR-Frachtbrief? Vorbehalte? Wertangabe Art. 24 / Interesse Art. 26?)
- Übergabe- und Ablieferungszeitpunkt
- Gut: Art, Verpackung, Bruttogewicht (kg), Warenwert
- Schadensbild (Verlust ganz/teilweise, Beschädigung, Lieferfristüberschreitung), Schadensereignis
- Datum und Form der Schadensanzeige des Empfängers
- Position des Mandanten: Versender, Empfänger, Frachtführer/Subfrachtführer, Transportversicherer

## Sub-Agent-Architektur

Researcher liefert CMR-Statute, BGH-I-ZS- und OLG-Rechtsprechung zu Art. 17, Art. 23, Art. 29 und Art. 32 sowie Kommentarstellen (Thume, Beck'scher CMR-Handkommentar, Koller). Drafter prüft im Gutachtenstil den Anwendungsbereich Art. 1 CMR, die Haftung Art. 17 ff., berechnet den Höchstbetrag nach 8,33 SZR/kg Bruttogewicht und stellt Fristenkalender (Art. 30, Art. 32) sowie Gerichtsstandwahl (Art. 31) dar. Reviewer prüft Tatfrist Art. 30 CMR, Verjährung Art. 32 CMR mit Anfangs- und Endtag und SZR-Tageskurs mit Datum.

## Ablauf

### 1. Anwendungsbereich Art. 1 CMR

Art. 1 Abs. 1 CMR: Das Übereinkommen gilt für jeden Vertrag über die **entgeltliche** Beförderung von Gütern auf der **Straße** mittels Fahrzeugen, wenn der Ort der Übernahme des Gutes und der für die Ablieferung vorgesehene Ort, wie sie im Vertrag angegeben sind, in **zwei verschiedenen Staaten** liegen, von denen **mindestens einer ein Vertragsstaat** ist.

Konsequenzen:

- CMR ist **zwingendes Recht** im Anwendungsbereich (Art. 41 CMR – abweichende Vereinbarungen zulasten der Berechtigten nichtig).
- **CMR geht HGB vor**, soweit der Anwendungsbereich eröffnet ist; das HGB-Frachtrecht (§§ 407 ff.) ist nur subsidiär heranzuziehen, soweit die CMR Lücken lässt.
- Multimodaler Transport: Art. 2 CMR – Huckepackbeförderung; ergänzend § 452 HGB für unbekannte Schadensorte.

### 2. Frachtbrief Art. 4–9 CMR

- [Art. 4 CMR] Der Frachtbrief dient als Beweis. Sein Fehlen oder Mängel berühren die Geltung der CMR nicht.
- [Art. 6 CMR] Pflichtangaben (Versender, Frachtführer, Empfänger, Ort und Tag der Übernahme, vorgesehener Ablieferungsort, Bezeichnung des Gutes, Anzahl der Frachtstücke, Gewicht).
- [Art. 9 CMR] **Beweisregeln**: Der Frachtbrief begründet bis zum Beweis des Gegenteils Vermutungen über Abschluss und Inhalt des Beförderungsvertrages sowie über die Übernahme des Gutes durch den Frachtführer. Ohne Vorbehalt im Frachtbrief gilt die Vermutung, dass Gut und Verpackung bei Übernahme äußerlich in gutem Zustand waren und die Angaben über Anzahl, Zeichen und Nummern übereinstimmen (Art. 9 Abs. 2 CMR).

### 3. Haftung Art. 17 CMR

Art. 17 Abs. 1 CMR: Der Frachtführer haftet für **gänzlichen oder teilweisen Verlust** und für **Beschädigung** des Gutes, sofern der Verlust oder die Beschädigung zwischen Übernahme und Ablieferung eintritt, sowie für **Überschreitung der Lieferfrist**.

Obhutshaftung wie § 425 HGB – kein Verschulden im Tatbestand.

### 4. Haftungsausschlüsse Art. 17 II–IV CMR / Beweislast Art. 18 CMR

Art. 17 Abs. 2 CMR (allgemeine Befreiungsgründe – Beweislast Frachtführer):

- Verschulden des Verfügungsberechtigten
- nicht durch Verschulden des Frachtführers verursachte Weisung des Verfügungsberechtigten
- besondere Mängel des Gutes
- **Umstände, die der Frachtführer nicht vermeiden und deren Folgen er nicht abwenden konnte** (höhere-Gewalt-ähnlich, strenger Maßstab)

Art. 17 Abs. 4 CMR – **besondere Gefahren** (Vermutung nach Art. 18 Abs. 2 CMR):

a) Verwendung offener, nicht mit Plane versehener Fahrzeuge bei ausdrücklicher Vereinbarung im Frachtbrief
b) Fehlen oder Mängel der Verpackung
c) Behandlung, Verladen, Verstauen oder Entladen durch Versender/Empfänger
d) natürliche Beschaffenheit gewisser Güter (Bruch, Rost, innerer Verderb, Schwund, Ungeziefer, Nagetiere)
e) ungenügende oder unrichtige Bezeichnung oder Numerierung der Frachtstücke
f) Beförderung von lebenden Tieren

Art. 18 CMR regelt die Beweislastverteilung – im Grundsatz trifft sie den Frachtführer, mit Erleichterung über die Anscheinsvermutung bei Art. 17 IV-Gefahren.

### 5. Haftungsumfang Art. 23 CMR

[Art. 23 CMR]:

- Abs. 1: Wertersatz – Wert am Ort und Tag der Übernahme.
- Abs. 2: Maßgeblich der Börsen-, Markt- oder gemeine Wert.
- **Abs. 3: Höchstbetrag = 8,33 Rechnungseinheiten pro Kilogramm des fehlenden Bruttogewichts.** Rechnungseinheit = Sonderziehungsrecht (Art. 23 Abs. 7 CMR i.d.F. des Protokolls von 1978, BGBl. 1980 II S. 721).
- Abs. 4: Fracht, Zölle und sonstige im Zusammenhang mit der Beförderung erwachsenen Kosten sind voll zu erstatten.
- Abs. 5: **Lieferfristüberschreitung** – Haftung begrenzt auf die Fracht.

**Berechnung identisch § 431 HGB:**

```
Höchstbetrag (SZR) = 8,33 × Bruttogewicht der verlorenen/beschädigten Sendung (kg)
EUR-Wert           = Höchstbetrag × SZR/EUR-Tageskurs (IWF, Tag der Regulierung)
```

SZR-Tageskurs: https://www.imf.org/external/np/fin/data/rms_five.aspx `[unverifiziert – Tageskurs prüfen]`.

### 6. Wertangabe und Interesse an Ablieferung (Art. 24, 26 CMR)

- [Art. 24 CMR] Der Versender kann gegen Zuschlag einen den Höchstbetrag übersteigenden **Wert des Gutes** im Frachtbrief angeben – dann ist dieser Betrag Haftungsgrenze.
- [Art. 26 CMR] Der Versender kann gegen Zuschlag ein **besonderes Interesse an der Ablieferung** angeben – dann kann zusätzlich zum Höchstbetrag Ersatz des nachgewiesenen Schadens bis zur Höhe des angegebenen Betrages verlangt werden.

### 7. Wegfall der Haftungsbegrenzungen Art. 29 CMR

[Art. 29 Abs. 1 CMR]: Der Frachtführer kann sich auf die Haftungsbegrenzungen **nicht** berufen, wenn er den Schaden **vorsätzlich** oder durch ein **ihm zur Last fallendes Verschulden** verursacht hat, das nach dem Recht des angerufenen Gerichts **dem Vorsatz gleichsteht**.

Nach BGH-Rspr. zu § 435 HGB entspricht das deutschen Maßstab gleichgestellte Verschulden der **Leichtfertigkeit + Bewusstsein des wahrscheinlichen Schadenseintritts**. Damit besteht praktische Parallelität HGB ↔ CMR. BGH (I. ZS), Urt. v. 13.12.2012 – [I ZR 236/11](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=13.12.2012&Aktenzeichen=I%20ZR%20236/11), TranspR 2013, 175.

Art. 29 Abs. 2 CMR erstreckt die Folge auf Bedienstete und Erfüllungsgehilfen.

Folgen:
- volle Haftung ohne 8,33-SZR-Begrenzung
- 3-Jahres-Verjährung (Art. 32 I 2 CMR)
- Schadensanzeigeobliegenheit nach Art. 30 CMR mit Beweislastfolge bleibt grundsätzlich beachtlich (str.)

### 8. Schadensanzeige Art. 30 CMR

[Art. 30 CMR]:

| Schaden | Anzeigefrist | Folge bei Versäumnis |
|---|---|---|
| **Äußerlich erkennbar** | bei Empfangnahme (Art. 30 I 1 CMR) | Vermutung ordnungsgemäßer Ablieferung |
| **Äußerlich nicht erkennbar** | binnen **7 Tagen** nach Ablieferung (ohne Sonn- und Feiertage), schriftlich (Art. 30 I 2 CMR) | dito |
| **Überschreitung der Lieferfrist** | binnen **21 Tagen** nach der Übergabe an den Empfänger, schriftlich (Art. 30 III CMR) | Anspruchsausschluss (str. – str. Reichweite) |

Art. 30 Abs. 4 CMR: Bei der Fristberechnung wird der Tag der Ablieferung oder Feststellung nicht mitgezählt.

### 9. Gerichtsstand Art. 31 CMR

[Art. 31 Abs. 1 CMR] – **Wahl des Klägers** unter mehreren Gerichtsständen:

a) Gerichte eines Staates, dem die Parteien sich durch Vereinbarung unterworfen haben
b) Gericht am Ort des **gewöhnlichen Aufenthalts des Beklagten**, der Hauptniederlassung, der Zweigniederlassung oder Geschäftsstelle, durch deren Vermittlung der Vertrag geschlossen wurde
c) Gericht des Ortes der **Übernahme** des Gutes oder des für die Ablieferung **vorgesehenen Ortes**

Art. 31 Abs. 2 CMR: **Rechtshängigkeit**-Sperre für parallele Klagen (lis pendens, identisch mit Brüssel-Ia-Mechanik).

### 10. Verjährung Art. 32 CMR

[Art. 32 CMR]:

| Verschulden | Frist | Beginn |
|---|---|---|
| **Regelfall** | 1 Jahr | Art. 32 I CMR: Beschädigung/Lieferfrist – Ablieferung; vollständiger Verlust – 30 Tage nach vereinbarter Lieferfrist bzw. 60 Tage nach Übernahme; sonstige Fälle – 3 Monate nach Vertragsschluss |
| **Vorsatz / gleichgestelltes Verschulden Art. 29** | 3 Jahre | dito |

Art. 32 Abs. 2 CMR: **Hemmung durch schriftliche Reklamation** bis zur schriftlichen Zurückweisung; die Reklamation hemmt nur, soweit der Frachtführer schriftlich antwortet.

Art. 32 Abs. 3 CMR: Im Übrigen gilt für Hemmung und Unterbrechung das Recht des angerufenen Gerichts – also in Deutschland §§ 203 ff. BGB.

### 11. Verhältnis CMR / HGB

- Im Anwendungsbereich der CMR: **Anwendungsvorrang CMR** vor §§ 407 ff. HGB.
- Innerstaatliche Beförderung: HGB.
- Multimodale Beförderung mit unbekanntem Schadensort: § 452 HGB.

## Quellen und Zitierweise

Verbindlich: [`../../../references/zitierweise.md`](../../../references/zitierweise.md).

### Übereinkommen und Statute

- CMR (Übereinkommen v. 19.05.1956 über den Beförderungsvertrag im internationalen Straßengüterverkehr) – BGBl. 1961 II S. 1119; Protokoll v. 05.07.1978 (SZR-Umstellung) – BGBl. 1980 II S. 721. Volltext (frz./engl. Original): https://treaties.un.org/Pages/showDetails.aspx?objid=08000002800c87fb
- [§ 452 HGB](https://www.gesetze-im-internet.de/hgb/__452.html) (Multimodaltransport)
- [§§ 407 ff. HGB](https://www.gesetze-im-internet.de/hgb/__407.html) (subsidiär)
- SZR-Tageskurs: https://www.imf.org/external/np/fin/data/rms_five.aspx

### Kommentare

- Thume, CMR-Kommentar, 3. Aufl. 2013, Art. 1 Rn. 1 ff.; Art. 17 Rn. 1 ff.; Art. 23 Rn. 1 ff.; Art. 29 Rn. 1 ff.; Art. 30 Rn. 1 ff.; Art. 32 Rn. 1 ff. `[unverifiziert – Auflagenstand prüfen]`
- Boesche / de la Motte / Hartenstein, Beck'scher CMR-Handkommentar, jüngste Auflage, Art. 17, 23, 29, 30, 32 CMR `[unverifiziert – Auflagenstand prüfen]`
- Koller, Transportrecht, 10. Aufl. 2020, CMR-Teil, Art. 1, 17, 23, 29, 30, 32 CMR `[unverifiziert]`

### Rechtsprechung (`[unverifiziert – prüfen in juris/TranspR]`)

1. BGH, Urt. v. 13.12.2012 – I ZR 236/11, TranspR 2013, 175 (Art. 29 CMR – qualifiziertes Verschulden, Parallelität zu § 435 HGB)
2. BGH, Urt. v. 30.09.2010 – I ZR 39/09, TranspR 2011, 218 (Art. 17, 18 CMR – Beweislast)
3. BGH, Urt. v. 03.03.2005 – I ZR 134/02, TranspR 2005, 311 (Art. 32 CMR – Hemmung durch Reklamation)
4. OLG Düsseldorf, Urt. v. 22.06.2011 – I-18 U 31/11, TranspR 2011, 421 (Art. 31 CMR – Gerichtsstandwahl)

## Ausgabeformat

```
GUTACHTEN – CMR-Frachtführerhaftung
Beförderung: <Versender (Staat A) → Empfänger (Staat B)>, <Datum Übernahme>, <Datum Ablieferung>
Gut: <Art>, Bruttogewicht <kg>, Warenwert <EUR>
Schaden: <Verlust / Beschädigung / Verspätung>, <EUR>

I. Sachverhalt
II. Frage(n)
III. Kurzantwort
     – Anwendbarkeit CMR Art. 1: [ja / nein]
     – Haftung Art. 17 CMR dem Grunde nach: [ja / nein]
     – Höchstbetrag (8,33 SZR × kg) Art. 23 III CMR: <SZR>; EUR-Gegenwert zum <Datum>
       Tageskurs SZR/EUR <Quelle, Datum>
     – Durchbruch Art. 29 CMR: [vorliegend / fernliegend]
     – Tatfrist Art. 30 CMR: [gewahrt / versäumt am <Datum>]
     – Verjährung Art. 32 CMR: läuft ab am <Datum>
     – Gerichtsstand Art. 31 CMR: <Wahlmöglichkeiten>
     – Empfehlung: <…>

IV. Rechtliche Bewertung
    1. Anwendungsbereich Art. 1 CMR
       – grenzüberschreitend? entgeltlich? Straße? Vertragsstaat?
    2. Frachtbrief und Beweisregeln Art. 4–9 CMR
    3. Haftung Art. 17 I CMR
    4. Haftungsausschlüsse Art. 17 II, IV CMR – Beweislast Art. 18 CMR
    5. Haftungsumfang Art. 23 I–IV CMR
       Berechnung: 8,33 SZR × <kg> = <SZR>
                   × Tageskurs SZR/EUR <Datum> = <EUR>
       Wertangabe Art. 24 / Interesse Art. 26 CMR?
    6. Durchbruch Art. 29 CMR
       a) Vorsatz?
       b) Gleichgestelltes Verschulden (Leichtfertigkeit + Bewusstsein)?
    7. Schadensanzeige Art. 30 CMR
       – sichtbar / verborgen (7 Tage) / Verspätung (21 Tage)?
       – Anzeigedatum: <Datum>; Frist gewahrt: [ja / nein]
    8. Gerichtsstand Art. 31 CMR
    9. Verjährung Art. 32 CMR
       – Regel- oder 3-Jahres-Frist?
       – Beginn: <Datum>; Ablauf: <Datum>
       – Hemmung Art. 32 II CMR / § 203 BGB?
    10. Verhältnis zu HGB – ggf. § 452 HGB bei Multimodal

V. Gesamtergebnis

VI. Risiken / offene Punkte
    🟢 / 🟡 / 🔴 <Einstufung mit Begründung>
    – Offene Tatsachen: Bruttogewicht, Frachtbriefvermerke, Schadensanzeigedatum,
      Schnittstellenprotokoll Unterfrachtführer

VII. Quellenverzeichnis
     – CMR (BGBl.-Fundstellen)
     – Rspr. (BGH I ZR …, OLG …) [unverifiziert – prüfen]
     – Kommentare (Thume, Beck'scher CMR, Koller)
     – SZR-Tageskurs IWF, abgerufen am <Datum>
```

## Beispiel (Auszug, Gutachtenstil)

> "Der Beförderungsvertrag zwischen V (Lyon, FR) und F (Speditionsunternehmen, FR) zur Lieferung nach Stuttgart (DE) fällt nach Art. 1 Abs. 1 CMR in den Anwendungsbereich des Übereinkommens: entgeltliche Straßenbeförderung mit LKW, Übernahme- und Ablieferungsort in zwei verschiedenen Staaten, beide (FR und DE) sind Vertragsstaaten.
>
> F haftet nach Art. 17 Abs. 1 CMR dem Grunde nach für den Wassereintritt im Obhutszeitraum. Ein Befreiungsgrund nach Art. 17 Abs. 2 CMR (unvermeidbares Ereignis) ist substantiiert vorzutragen und zu beweisen (Art. 18 Abs. 1 CMR); bloßer Hinweis auf 'Witterung' genügt nicht – vgl. BGH (I. ZS), Urt. v. 30.09.2010 – [I ZR 39/09](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=30.09.2010&Aktenzeichen=I%20ZR%2039/09).
>
> Der Höchstbetrag nach Art. 23 Abs. 3 CMR beträgt 8,33 SZR/kg des fehlenden bzw. beschädigten Bruttogewichts. Bei einem Bruttogewicht der zwölf beschädigten Kartons von angenommen 320 kg ergibt das **2.665,6 SZR**, umzurechnen mit dem SZR/EUR-Tageskurs am Tag der Regulierung (IWF, https://www.imf.org/external/np/fin/data/rms_five.aspx, Stand <Datum>) `[unverifiziert – Tageskurs prüfen]`.
>
> Die Schadensanzeige der Empfängerin zwei Tage nach Ablieferung ist nach Art. 30 Abs. 1 S. 2 CMR rechtzeitig – die 7-Tage-Frist (ohne Sonn- und Feiertage) ist gewahrt. Die Verjährung läuft nach Art. 32 Abs. 1 S. 1 CMR ein Jahr ab Ablieferung; sie kann nach Art. 32 Abs. 2 CMR durch schriftliche Reklamation gehemmt werden.
>
> Klägerin kann nach Art. 31 Abs. 1 CMR vor französischen Gerichten (Sitz Beklagter/Übernahmeort) oder deutschen Gerichten (Ablieferungsort Stuttgart) klagen. ..."

## Risiken / typische Fehler

- **Anwendungsbereich Art. 1 CMR übersehen** – innerstaatliche Beförderung mit gelegentlicher Grenzüberquerung fällt nicht in den Anwendungsbereich, wenn Vertrag rein innerstaatlich angelegt ist.
- **Fixer EUR-Wert für 8,33 SZR ohne Datum** – Tageskurs ist anzugeben.
- **Art. 29 CMR-Subsumtion an deutschen Maßstab anlegen ohne Hinweis** – "gleichgestelltes Verschulden" ist eine Verweisung in das Recht des angerufenen Gerichts; in Deutschland ist das die § 435 HGB-Linie.
- **Art. 30 CMR-Fristen und Art. 32 CMR-Fristen verwechselt** – Tatfrist Art. 30 ≠ Verjährung Art. 32.
- **Gerichtsstand Art. 31 CMR rangbestimmt verstanden** – Klägerwahl, kein Vorrang Sitz-Beklagter.
- **HGB-§§ 425 ff. parallel zur CMR angewandt** – CMR hat Anwendungsvorrang; HGB greift nur subsidiär.
- **Wertangabe / Interesse-Erhöhung übersehen** (Art. 24, 26 CMR), wenn der Frachtbrief sie enthält.
- **Hemmung durch schriftliche Reklamation Art. 32 II CMR** verkannt – sie hemmt nur bis zur schriftlichen Zurückweisung.

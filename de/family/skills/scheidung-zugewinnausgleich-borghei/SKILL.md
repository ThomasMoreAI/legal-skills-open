---
name: scheidung-zugewinnausgleich-borghei
title: /familienrecht:scheidung-zugewinnausgleich
description: Scheidung im Zugewinngemeinschafts-Güterstand mit Berechnung des Zugewinnausgleichsanspruchs §§ 1372 ff. BGB. Anfangs- und Endvermögen, Hinzurechnung illoyaler Verfügungen § 1375 Abs. 2 BGB, vorzeitiger Ausgleich § 1385 BGB, Auskunftsanspruch § 1379 BGB. Use when eine Scheidung mit Zugewinnausgleich gestaltet oder geprüft wird.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/familienrecht/skills/scheidung-zugewinnausgleich
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: family
language: de
---

# /familienrecht:scheidung-zugewinnausgleich

## Zweck

Der Zugewinnausgleich ist im Regel-Güterstand „Zugewinngemeinschaft" der zentrale wirtschaftliche Effekt der Scheidung. Fehler bei Stichtagen, illoyalen Verfügungen oder bei der Schuldenberücksichtigung sind in dreistelliger Höhe pro 100 TEUR Vermögen. Dieser Skill strukturiert die Berechnung und die Verteidigungslinien.

## Eingaben

- Heiratsdatum (Stichtag Anfangsvermögen)
- Zustellung Scheidungsantrag (Stichtag Endvermögen, § 1384 BGB)
- Anfangsvermögen beider Ehegatten (mit Belegen)
- Endvermögen beider Ehegatten (mit Belegen)
- Schenkungen / Erbschaften während der Ehe (privilegiert nach § 1374 Abs. 2 BGB)
- Verdacht auf illoyale Vermögensminderung
- Ehevertrag mit modifiziertem Zugewinn?

## Ablauf

### 1. Güterstand prüfen

- Default: **Zugewinngemeinschaft** (§ 1363 BGB).
- **Gütertrennung** (§ 1414 BGB): kein Zugewinnausgleich.
- **Modifizierte Zugewinngemeinschaft** (Ehevertrag): teilweiser Ausschluss, Inhaltskontrolle nach Sittenwidrigkeitsmaßstab (BGH 2004).

### 2. Stichtage

| Berechnung | Stichtag | Norm |
|---|---|---|
| Anfangsvermögen | Tag der Eheschließung | § 1374 Abs. 1 BGB |
| Endvermögen | Rechtshängigkeit des Scheidungsantrags | § 1384 BGB |
| Zugewinnausgleichsforderung | Rechtskraft der Scheidung | § 1378 Abs. 3 BGB |

### 3. Anfangsvermögen ([§ 1374 BGB](https://www.gesetze-im-internet.de/bgb/__1374.html))

Aktiv-Passiv-Saldierung bei Eheschließung. Auch **negatives Anfangsvermögen** wird berücksichtigt (seit Reform 2009).

**Privilegiertes Vermögen** (Abs. 2): Schenkungen und Erbschaften während der Ehe werden dem Anfangsvermögen hinzugerechnet — sind also kein Zugewinn.

### 4. Endvermögen ([§ 1375 BGB](https://www.gesetze-im-internet.de/bgb/__1375.html))

Aktiv-Passiv-Saldierung am Stichtag Rechtshängigkeit.

**Hinzurechnung illoyaler Verfügungen** (§ 1375 Abs. 2 BGB): Vermögensminderungen in den letzten 10 Jahren vor Stichtag durch:

1. unentgeltliche Zuwendung ohne sittliche Verpflichtung
2. Vermögensverschwendung
3. Vermögensvernichtung in der Absicht, den ausgleichsberechtigten Ehegatten zu benachteiligen

werden dem Endvermögen hinzugerechnet (fiktiv).

### 5. Berechnung Zugewinn

```
Zugewinn = Endvermögen − Anfangsvermögen (jeweils inflationsbereinigt seit 2009)
```

Verbraucherpreisindex-Anpassung nach § 1376 Abs. 1 BGB.

### 6. Ausgleichsanspruch ([§ 1378 BGB](https://www.gesetze-im-internet.de/bgb/__1378.html))

```
Ausgleichsanspruch = (Zugewinn Ehegatte mit höherem Zuwachs − Zugewinn anderer Ehegatte) / 2
```

**Höchstgrenze:** Vermögen des Pflichtigen am Stichtag, vermindert um Verbindlichkeiten (§ 1378 Abs. 2 S. 1 BGB).

### 7. Auskunftsanspruch ([§ 1379 BGB](https://www.gesetze-im-internet.de/bgb/__1379.html))

Wechselseitig: Auskunft + Beleg für Anfangs- und Endvermögen, optional auch Trennungs-Stichtag-Vermögen. Stufenklage § 254 ZPO.

### 8. Vorzeitiger Ausgleich ([§ 1385 BGB](https://www.gesetze-im-internet.de/bgb/__1385.html))

In dem Trennungs-Stichtag und der Rechtshängigkeit kann vorzeitiger Ausgleich verlangt werden, wenn:

- Trennung seit mind. 3 Jahren
- Pflichtiger illoyales Verhalten zu erwarten
- Sicherungsinteresse

### 9. Ehevertrag-Inhaltskontrolle

BGH-Rechtsprechung (seit 2004): Eheverträge unterliegen Sittenwidrigkeitskontrolle, wenn sie die Existenzgrundlage eines Ehegatten gefährden, insbesondere:

- Trennungsunterhalt vollständig ausgeschlossen
- Versorgungsausgleich + Zugewinn beide ausgeschlossen
- Lebensplan einseitig zugeschnitten (z. B. „Hausfrauenehe")

## Quellen

### Statute

- [§§ 1363, 1372 ff. BGB](https://www.gesetze-im-internet.de/bgb/__1363.html) (Zugewinngemeinschaft)
- [§ 1374, § 1375, § 1376, § 1378, § 1379, § 1385 BGB](https://www.gesetze-im-internet.de/bgb/__1374.html)
- [§ 1564 BGB](https://www.gesetze-im-internet.de/bgb/__1564.html) (Scheidung)
- [§ 254 ZPO](https://www.gesetze-im-internet.de/zpo/__254.html) (Stufenklage)
- [VersAusglG](https://www.gesetze-im-internet.de/versausglg/) (Versorgungsausgleich, separat)

### Kommentare

- Koch, in: MüKoBGB, 9. Aufl. 2023, § 1378 Rn. 1 ff.
- Schwab, Familienrecht, 32. Aufl. 2024
- Wever, in: Wever / Wendl, Unterhalt und Vermögensausgleich

### Rechtsprechung

- BGH, Urt. v. 11.02.2004 – XII ZR 265/02, NJW 2004, 930 (Inhaltskontrolle Ehevertrag) `[unverifiziert – prüfen]`
- BGH, Urt. v. 15.11.2017 – XII ZB 503/16, NJW 2018, 384 (Illoyalität § 1375 Abs. 2) `[unverifiziert – prüfen]`

## Ausgabeformat

```
ZUGEWINNAUSGLEICH-BERECHNUNG — <Mandat> — <Datum>

I.    Güterstand                     [Zugewinngemeinschaft / modifiziert / Gütertrennung]
II.   Stichtage
      Eheschließung:                  <Datum>
      Rechtshängigkeit Antrag:        <Datum>
III.  Anfangsvermögen
      Ehefrau:                        <EUR (Aktiva – Passiva, inflationsbereinigt)>
      Ehemann:                        <EUR>
      Privilegierte Hinzurechnungen (Schenkungen / Erbschaften): <…>
IV.   Endvermögen
      Ehefrau:                        <EUR>
      Ehemann:                        <EUR>
      Illoyale Verfügungen § 1375 Abs. 2:  <…>
V.    Zugewinn
      Ehefrau:                        <EUR>
      Ehemann:                        <EUR>
VI.   Ausgleichsanspruch
      Höhe:                           <EUR>
      Höchstgrenze § 1378 Abs. 2:     <EUR>
VII.  Verfahren
      Auskunftsanspruch § 1379:       [erfüllt / Stufenklage erforderlich]
      Vorzeitiger Ausgleich § 1385:   [erwogen / nicht]

Verteidigung / Strategie:             <…>
```

## Risiken / typische Fehler

- **Stichtag falsch** — Rechtshängigkeit, nicht Trennung, ist Endvermögens-Stichtag.
- **Inflation nicht berücksichtigt** — § 1376 Abs. 1 BGB verlangt VPI-Anpassung.
- **Schenkungen während der Ehe als Zugewinn behandelt** — sie sind privilegiert (§ 1374 Abs. 2 BGB).
- **Illoyale Verfügungen nicht angesprochen** — Beweislast beim Auskunftsberechtigten, aber wesentlich.
- **Ehevertrag als „in jedem Fall wirksam" angesehen** — Sittenwidrigkeitsprüfung BGH 2004 ff.
- **Höchstgrenze § 1378 Abs. 2 vergessen** — der Anspruch ist auf das aktuelle Vermögen begrenzt.
- **Versorgungsausgleich ignoriert** — Pflichtteil des Familienrechts-Vergleichs.

---
name: abmahnung-borghei
title: /arbeitsrecht:abmahnung
description: Entwurf einer BAG-konformen Abmahnung im Arbeitsrecht – konkrete Schilderung der Pflichtverletzung, klare Verhaltenserwartung, ausdrückliche Sanktionsandrohung. Use when AG eine verhaltensbedingte Sanktion vor einer Kündigung dokumentieren muss oder AN die Wirksamkeit einer empfangenen Abmahnung prüft.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/arbeitsrecht/skills/abmahnung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: employment
language: de
---

# /arbeitsrecht:abmahnung

## Zweck

Die Abmahnung ist Voraussetzung jeder verhaltensbedingten Kündigung (außer bei schwerwiegenden Pflichtverletzungen). Wirksam ist sie nur, wenn sie **drei Funktionen** erfüllt: konkrete Schilderung (Rügefunktion), eindeutige Verhaltenserwartung (Hinweisfunktion), Sanktionsandrohung (Warnfunktion). Dieser Skill stellt das sicher.

## Eingaben

- konkretes Verhalten (Datum, Ort, Zeugen)
- Art der Pflichtverletzung (Haupt- oder Nebenpflicht)
- frühere Abmahnungen (Anzahl, Datum, Anlass)
- Position des AN
- Bezug auf Personalhandbuch / Betriebsvereinbarung?

## Sub-Agent-Architektur

Researcher liefert Statute und BAG-Rechtsprechung zu Abmahnungsbestandteilen. Drafter erstellt den Abmahnungstext + interne Notiz für die Personalakte. Reviewer prüft Bestimmtheit, Verhältnismäßigkeit, Aufbewahrungsfristen.

## Ablauf

### 1. Bestandteile einer wirksamen Abmahnung

| Funktion | Inhalt |
|---|---|
| **Rüge** | Konkrete Schilderung des Fehlverhaltens (Datum, Uhrzeit, beobachtete Tatsachen) |
| **Hinweis** | Klare Beschreibung des erwarteten Verhaltens |
| **Warnung** | Ausdrückliche Androhung arbeitsrechtlicher Konsequenzen einschließlich Kündigung |

Maßstab: BAG, Urt. v. 19.11.2015 – 2 AZR 217/15, NZA 2016, 540 `[unverifiziert – prüfen]`.

### 2. Verhältnismäßigkeit

Eine Abmahnung muss **angemessen** und **erforderlich** sein. Bagatellverstöße → Ermahnung. Mehrfache Wiederholung → Abmahnung. Schwerwiegende Pflichtverletzung → ggf. ohne Abmahnung Kündigung möglich (vgl. BAG „Emmely", Urt. v. 10.06.2010 – 2 AZR 541/09, NZA 2010, 1227 `[unverifiziert – prüfen]`).

### 3. Form

Schriftform empfohlen, gesetzlich aber nicht zwingend. Mündliche Abmahnung wirksam, in der Praxis wegen Beweislast unhaltbar.

### 4. Personalakte und Aufbewahrungsfrist

Abmahnung in der Personalakte. **Tilgungsanspruch** nach Zeitablauf, wenn das gerügte Verhalten nicht wiederholt wurde — Faustregel: 2–3 Jahre, einzelfallabhängig.

Belegstelle: ErfK / Linck, § 1 KSchG Rn. 200 ff. zur Tilgung.

### 5. AN-Stellungnahme

Gegendarstellung des AN nach [§ 83 BetrVG](https://www.gesetze-im-internet.de/betrvg/__83.html) (Personalakteneinsicht). Stellungnahme zur Akte nehmen, **nicht** Abmahnung daraufhin verschärfen.

## Quellen und Zitierweise

Verbindlich: [`../../references/zitierweise.md`](../../references/zitierweise.md).

### Statute

- [§ 314 Abs. 2 BGB](https://www.gesetze-im-internet.de/bgb/__314.html) (Abmahnung als Rücktrittsvoraussetzung im Dauerschuldverhältnis — analog im Arbeitsrecht)
- [§ 626 BGB](https://www.gesetze-im-internet.de/bgb/__626.html) (Voraussetzung der außerordentlichen Kündigung)
- [§ 83 BetrVG](https://www.gesetze-im-internet.de/betrvg/__83.html) (Personalakteneinsicht)
- [§ 1 KSchG](https://www.gesetze-im-internet.de/kschg/__1.html) (verhaltensbedingte Kündigung)

### Kommentare

- Linck, in: ErfK, 24. Aufl. 2024, § 1 KSchG Rn. 200 ff. (verhaltensbedingte Kündigung und Abmahnung)
- Preis, in: ErfK, 24. Aufl. 2024, § 626 BGB Rn. 110 ff. (Abmahnung vor außerordentlicher Kündigung)
- Berkowsky, in: MüKoBGB, 9. Aufl. 2023, § 626 BGB Rn. 200 ff.

### Rechtsprechung (`[unverifiziert – prüfen in Beck-Online/juris]`)

1. BAG, Urt. v. 19.11.2015 – 2 AZR 217/15, NZA 2016, 540 (Bestimmtheit)
2. BAG, Urt. v. 10.06.2010 – 2 AZR 541/09, NZA 2010, 1227 („Emmely", Interessenabwägung)
3. BAG, Urt. v. 18.11.1986 – 7 AZR 674/84, NZA 1987, 418 (Tilgung)

## Ausgabeformat

```
ABMAHNUNG
<AG-Briefkopf>

An <AN Name + Position>
<Datum>

Sehr geehrte(r) <…>,

I. Sachverhalt
   Am <Datum>, ca. <Uhrzeit>, in <Ort> wurde Folgendes beobachtet:
   <konkrete Schilderung — Tatsachen, nicht Wertungen>

II. Pflichtverletzung
    Hiermit haben Sie gegen Ihre Pflicht aus
    <Norm/Vertrag/Personalhandbuch> verstoßen.

III. Verhaltenserwartung
     Wir erwarten von Ihnen, dass Sie zukünftig <…>.

IV. Sanktionsandrohung
    Sollten Sie sich erneut pflichtwidrig verhalten, müssen Sie mit
    arbeitsrechtlichen Konsequenzen rechnen, die bis zur Kündigung
    des Arbeitsverhältnisses reichen können.

V. Ihr Recht zur Stellungnahme
   Sie können nach § 83 BetrVG eine Gegendarstellung zur Personalakte
   nehmen lassen.

Mit freundlichen Grüßen
<…>

[Interne Notiz für die Personalakte:
  - Zeugen: <…>
  - Frühere Abmahnungen: <…>
  - Tilgungsfrist Erinnerung: <Datum + 2-3 Jahre>
]
```

## Risiken / typische Fehler

- **Wertung statt Tatsache** ("Sie sind unzuverlässig") → unwirksame Abmahnung. Stattdessen: was wurde wann beobachtet.
- **Sanktionsandrohung fehlt oder weichgespült** → Warnfunktion verfehlt.
- **Bezug auf nicht existierende Vorgaben** (z. B. nicht ausgehändigtes Personalhandbuch) → angreifbar.
- **Mehrere Vorwürfe in einer Abmahnung** → wenn ein Vorwurf bröckelt, fällt die ganze Abmahnung.
- **Kündigung ohne (vorherige) wirksame Abmahnung** bei nicht schwerwiegender Pflichtverletzung → KSchG-Klage greift durch.

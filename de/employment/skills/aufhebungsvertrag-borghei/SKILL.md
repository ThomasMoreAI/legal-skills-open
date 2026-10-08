---
name: aufhebungsvertrag-borghei
title: /arbeitsrecht:aufhebungsvertrag
description: Erstellung und Prüfung eines Aufhebungsvertrags inkl. Sperrzeit § 159 SGB III, Schriftform § 623 BGB und steuerlicher Behandlung der Abfindung § 34 EStG. Use when ein Arbeitsverhältnis einvernehmlich beendet wird oder eine Sperrzeit-Risikobewertung benötigt wird.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/arbeitsrecht/skills/aufhebungsvertrag
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: employment
language: de
---

# /arbeitsrecht:aufhebungsvertrag

## Zweck

Aufhebungsverträge sind das stille Risiko des Arbeitsrechts: technisch ein BGB-Vertrag, praktisch eine Falle, weil **Sperrzeit nach [§ 159 SGB III](https://www.gesetze-im-internet.de/sgb_3/__159.html)** den AN materiell trifft, ohne dass das im Vertragstext steht. Dieser Skill erstellt einen rechtssicheren Entwurf und führt die Sperrzeit-Risikoprüfung **vor** Unterschrift durch.

## Eingaben

- Beendigungszeitpunkt
- Höhe der Abfindung (BMG × Faktor)
- Beschäftigungsdauer
- Grund der Beendigung (AG-Wunsch / AN-Wunsch / Vergleich nach KSchG-Klage)
- Steuerliche Wünsche (Einmal- vs. Mehrjahresauszahlung)
- Resturlaubs- und Überstundenstatus
- Wettbewerbsverbot?

## Sub-Agent-Architektur

Researcher liefert Statute, Sperrzeit-Rechtsprechung des BSG / BAG, Kommentarstellen. Drafter erstellt den Vertragstext + Sperrzeit-Analyse-Memo. Reviewer prüft Schriftform, Vollständigkeit und Sperrzeit-Mitigation.

## Ablauf

### 1. Schriftform ([§ 623 BGB](https://www.gesetze-im-internet.de/bgb/__623.html))

**Zwingend schriftlich.** Elektronische Form ausgeschlossen. Unterschrift beider Parteien auf demselben Dokument. Verstoß → Nichtigkeit.

### 2. Sperrzeit-Risiko ([§ 159 SGB III](https://www.gesetze-im-internet.de/sgb_3/__159.html))

Sperrzeit von 12 Wochen, wenn AN das Arbeitsverhältnis **gelöst hat** (§ 159 Abs. 1 Nr. 1 SGB III) **ohne wichtigen Grund**.

Wichtiger Grund liegt regelmäßig vor bei:

- konkret drohender, rechtmäßiger betriebsbedingter AG-Kündigung
- Abfindung im Rahmen 0,25–0,5 BMG × Beschäftigungsjahre (Faustformel BA)
- Einhaltung der ordentlichen Kündigungsfrist

Bei Zweifel: Mitteilung an die Bundesagentur für Arbeit nach § 38 SGB III rechtzeitig empfehlen.

### 3. Steuerliche Behandlung ([§ 34 EStG](https://www.gesetze-im-internet.de/estg/__34.html))

„Fünftelregelung" für außerordentliche Einkünfte:

- Abfindung gilt als außerordentliche Einkunft, **wenn** sie in einem Veranlagungszeitraum zufließt.
- Auszahlung über mehrere Jahre zerstört die Fünftelregelung.
- Lohnsteuer-Pauschalierung durch AG möglich, AN beantragt Veranlagung.

### 4. Klauselkatalog

- Beendigungsdatum + ordentliche Kündigungsfrist eingehalten
- Höhe und Fälligkeit der Abfindung
- Resturlaubs- und Überstundenabgeltung
- Rückgabe von AG-Eigentum (Schlüssel, Hardware, Akten)
- Verschwiegenheitsklausel (häufig wechselseitig)
- Optional: nachvertragliches Wettbewerbsverbot ([§§ 74 ff. HGB](https://www.gesetze-im-internet.de/hgb/__74.html)) — Karenzentschädigung min. 50 % der letzten Vergütung
- Optional: Zwischenzeugnis / qualifiziertes Endzeugnis
- Erledigungsklausel (Wirkung auf §§ 138, 779 BGB beachten)

### 5. Erledigungsklausel-Risiken

Pauschalformeln („mit Erfüllung dieses Vertrags sind alle Ansprüche … erledigt") können auch unbekannte Ansprüche aus Bonus, Tantieme, Provision erfassen. Sorgfältige Klauselbestimmung gegen Eigentumsstörung empfohlen ([§ 779 BGB](https://www.gesetze-im-internet.de/bgb/__779.html); Vergleichsanfechtung bei Irrtum).

## Quellen und Zitierweise

Verbindlich: [`../../references/zitierweise.md`](../../references/zitierweise.md).

### Statute

- [§ 623 BGB](https://www.gesetze-im-internet.de/bgb/__623.html), [§ 779 BGB](https://www.gesetze-im-internet.de/bgb/__779.html)
- [§ 159 SGB III](https://www.gesetze-im-internet.de/sgb_3/__159.html)
- [§ 34 EStG](https://www.gesetze-im-internet.de/estg/__34.html)
- [§§ 74 ff. HGB](https://www.gesetze-im-internet.de/hgb/__74.html) (Wettbewerbsverbot)

### Kommentare

- Müller-Glöge, in: MüKoBGB, 9. Aufl. 2023, § 623 Rn. 1 ff.
- Preis, in: ErfK, 24. Aufl. 2024, § 779 BGB Rn. 1 ff.
- Rolfs, in: ErfK, 24. Aufl. 2024, § 159 SGB III Rn. 1 ff.

### Rechtsprechung

- BSG, Urt. v. 17.10.2007 – B 11a/7a AL 52/06 R, NZA 2008, 365 (Sperrzeit Aufhebungsvertrag) `[unverifiziert – prüfen]`
- BAG, Urt. v. 13.04.2010 – 9 AZR 36/09, NZA 2010, 1308 (Erledigungsklausel) `[unverifiziert – prüfen]`

## Ausgabeformat

```
AUFHEBUNGSVERTRAG-ENTWURF — <AN-Position> — <Datum>
VERTRAULICH

I.  Sperrzeit-Risikoanalyse
    Risiko: [🟢 niedrig / 🟡 moderat / 🔴 hoch]
    Begründung: <…>
    Mitigations: <…>

II. Vertragstext
    1. Beendigung des Arbeitsverhältnisses
    2. Abfindung (Höhe, Fälligkeit, Steuer)
    3. Urlaubsabgeltung
    4. Rückgabe AG-Eigentum
    5. Verschwiegenheit
    6. Zeugnis
    7. Erledigungsklausel (mit Reichweite)
    8. Schlussbestimmungen

III. Steuerliche Hinweise
     - Fünftelregelung § 34 EStG anwendbar: [ja/nein]
     - Steuerlicher Optimierungshinweis: <…>

Offene Fragen:
  - <…>
Empfehlung: <…>
```

## Risiken / typische Fehler

- **Schriftform übersehen** (§ 623 BGB) → Vertrag nichtig.
- **Sperrzeit-Risiko nicht aufgeklärt** → Beratungsfehler-Haftung.
- **Erledigungsklausel zu weit** → unbekannte Ansprüche untergehen.
- **Wettbewerbsverbot ohne Karenzentschädigung** → unverbindlich (§ 74 Abs. 2 HGB).
- **Befristete Befreiung von der Arbeitsleistung** ohne ausdrücklichen Hinweis auf Anrechnung anderweitigen Verdienstes.

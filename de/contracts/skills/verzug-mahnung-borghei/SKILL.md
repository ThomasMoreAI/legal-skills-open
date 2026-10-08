---
name: verzug-mahnung-borghei
title: /vertragsrecht:verzug-mahnung
description: Prüfung von Schuldnerverzug und Mahnung – Verzugseintritt durch Mahnung § 286 Abs. 1 BGB, Entbehrlichkeit der Mahnung § 286 Abs. 2 BGB, 30-Tage-Regel für Entgeltforderungen § 286 Abs. 3 BGB, Verzugszinsen 5 und 9 Prozentpunkte über dem Basiszinssatz § 288 Abs. 1 und Abs. 2 BGB, Verzugspauschale § 288 Abs. 5 BGB, weiterer Verzögerungsschaden § 280 Abs. 2 BGB. Use when geprüft werden soll, ob und ab wann ein Schuldner in Verzug ist und welche Verzugsfolgen bestehen.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/vertragsrecht/skills/verzug-mahnung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: contracts
language: de
---

# /vertragsrecht:verzug-mahnung

## Zweck

Schuldnerverzug ist der Schlüssel zu Verzugszinsen, Verzugspauschale und Verzögerungsschaden. In der Praxis wird der Verzugseintritt regelmäßig falsch berechnet — entweder zu früh (Mahnung übersehen) oder zu spät (Entbehrlichkeit der Mahnung oder 30-Tage-Regel verkannt). Dieser Skill prüft strukturiert, **ob** und **ab wann** ein Schuldner in Verzug ist und welche Rechtsfolgen daran knüpfen, mit Bezug auf §§ 286, 288, 280 BGB und Standardkommentare.

## Eingaben

- Forderung (Höhe, Rechtsgrund — Entgeltforderung ja/nein)
- Fälligkeit (Leistungszeit vereinbart? kalendarisch bestimmt?)
- Rechnungsdatum und Zugang der Rechnung (für die 30-Tage-Regel)
- Verbraucher beteiligt? (B2C / B2B — entscheidet über Zinssatz, Pauschale, Hinweispflicht)
- Mahnung erfolgt? (Datum, Zugang, Wortlaut) — oder Gründe für entbehrliche Mahnung
- Arbeitsrechtlicher Kontext? (Sonderregel zur Verzugspauschale)

## Sub-Agent-Architektur

Die Prüfung läuft als zweistufige Maker/Checker-Kette in Prosa, ohne eigenen `agents`-Block. Ein **Anspruchs-Agent** klärt Fälligkeit und Verzugseintritt (Mahnung, Entbehrlichkeit, 30-Tage-Regel) und legt den Verzugsbeginn taggenau fest. Ein **Rechtsfolgen-Agent** berechnet darauf aufbauend Verzugszinsen, prüft Verzugspauschale und weiteren Verzögerungsschaden und entwirft das Mahnschreiben. Ein abschließender **Checker** verifiziert jede Norm- und Datumsangabe gegen die Eingaben, kennzeichnet jede nicht aus den Eingaben belegbare Tatsache und erfindet **niemals** ein Aktenzeichen.

## Ablauf

### 1. Fälligkeit und Anspruch

- Besteht ein fälliger, durchsetzbarer Anspruch? Ohne Fälligkeit kein Verzug.
- Leistungszeit vereinbart oder aus den Umständen bestimmbar? (§ 271 BGB als Auffang: sofort fällig.)
- Einreden des Schuldners (z. B. § 320 BGB) hindern den Verzug.

### 2. Verzugseintritt ([§ 286 BGB](https://www.gesetze-im-internet.de/bgb/__286.html))

**a) Grundfall — Mahnung ([§ 286 Abs. 1 BGB](https://www.gesetze-im-internet.de/bgb/__286.html))**

Verzug tritt ein, wenn der Schuldner auf eine **Mahnung** des Gläubigers nach Eintritt der Fälligkeit nicht leistet. Die Mahnung ist die bestimmte, eindeutige Aufforderung zur Leistung; ein bloßer Hinweis genügt nicht. Der Mahnung steht die Erhebung der Klage bzw. die Zustellung eines Mahnbescheids gleich.

**b) Entbehrliche Mahnung ([§ 286 Abs. 2 BGB](https://www.gesetze-im-internet.de/bgb/__286.html))**

Eine **entbehrliche Mahnung** liegt vor, wenn

- die Leistungszeit nach dem Kalender bestimmt ist (Nr. 1),
- der Leistung ein Ereignis vorauszugehen hat und die Leistungszeit ab dem Ereignis nach dem Kalender berechnet werden kann (Nr. 2),
- der Schuldner die Leistung **ernsthaft und endgültig** verweigert (Nr. 3) oder
- besondere Gründe den sofortigen Verzugseintritt rechtfertigen (Nr. 4).

In diesen Fällen kommt der Schuldner **ohne** Mahnung in Verzug.

**c) 30-Tage-Regel für Entgeltforderungen ([§ 286 Abs. 3 BGB](https://www.gesetze-im-internet.de/bgb/__286.html))**

Der Schuldner einer **Entgeltforderung** kommt spätestens in Verzug, wenn er nicht innerhalb von 30 Tagen nach Fälligkeit **und** Zugang einer Rechnung leistet (30-Tage-Regel). Diese 30-Tage-Regel greift unabhängig von einer Mahnung.

> **Verbraucher-Hinweis:** Gegenüber einem **Verbraucher** tritt der Verzug nach der 30-Tage-Regel nur ein, wenn auf diese Folge in der Rechnung **besonders hingewiesen** wurde (§ 286 Abs. 3 S. 1 Hs. 2 BGB). Fehlt der Hinweis, bleibt es bei Mahnung oder Entbehrlichkeit.

### 3. Verzugszinsen ([§ 288 Abs. 1 und Abs. 2 BGB](https://www.gesetze-im-internet.de/bgb/__288.html))

- **Grundsatz (§ 288 Abs. 1 BGB):** Verzugszinsen **5 Prozentpunkte über dem Basiszinssatz** pro Jahr.
- **Rechtsgeschäfte ohne Verbraucherbeteiligung (§ 288 Abs. 2 BGB):** bei Entgeltforderungen **9 Prozentpunkte über dem Basiszinssatz**.
- Der **Basiszinssatz** wird halbjährlich von der Deutschen Bundesbank festgesetzt (§ 247 BGB) und ist für die Berechnung taggenau zugrunde zu legen. Beide Sätze (5 vs. 9 Prozentpunkte über dem Basiszinssatz) hängen davon ab, ob ein Verbraucher beteiligt ist.

### 4. Verzugspauschale ([§ 288 Abs. 5 BGB](https://www.gesetze-im-internet.de/bgb/__288.html))

Bei einer Entgeltforderung gegen einen **Nicht-Verbraucher** kann der Gläubiger zusätzlich eine **Verzugspauschale** von **40 Euro** verlangen. Die Verzugspauschale wird auf einen geschuldeten Schadensersatz wegen der Rechtsverfolgungskosten angerechnet (§ 288 Abs. 5 S. 3 BGB).

> **Ausnahme im Arbeitsrecht:** Die 40-Euro-Verzugspauschale gilt **nicht** für Ansprüche aus dem Arbeitsverhältnis, weil § 12a Abs. 1 ArbGG den Kostenerstattungsanspruch in erster Instanz ausschließt — BAG, Urt. v. 25.09.2018 – 8 AZR 26/18, BAGE 163, 309 = NZA 2019, 121, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BAG&Datum=25.09.2018&Aktenzeichen=8%20AZR%2026/18).

### 5. Weiterer Verzögerungsschaden ([§ 280 Abs. 2 BGB](https://www.gesetze-im-internet.de/bgb/__280.html))

Ersatz des weiteren Verzögerungsschadens (z. B. Rechtsverfolgungs-/Inkassokosten, Kreditzinsen über den Verzugszins hinaus) kann der Gläubiger nur **unter den zusätzlichen Voraussetzungen des § 286 BGB** verlangen (§ 280 Abs. 2 BGB). Ohne Verzug nach § 286 BGB kein Verzögerungsschaden.

### 6. Mahnschreiben-Entwurf

Sofern noch keine wirksame Mahnung vorliegt und keine Entbehrlichkeit greift, wird ein Mahnschreiben entworfen: konkrete Leistungsaufforderung, bezifferte Hauptforderung, angemessene Zahlungsfrist mit Datum, Hinweis auf Verzugszinsen und ggf. Verzugspauschale. Kein Erfinden von Daten — Platzhalter, wo Eingaben fehlen.

### 7. Ergebnis

Taggenaue Festlegung des Verzugsbeginns, Zinssatz (5 oder 9 Prozentpunkte über dem Basiszinssatz), Verzugspauschale (ja/nein), weiterer Verzögerungsschaden (dem Grunde nach), offene Tatsachen markiert.

## Risiken / typische Fehler

- **Mahnung mit bloßer Rechnung verwechselt** — die Rechnung ist keine Mahnung; ohne Mahnung greift nur Entbehrlichkeit oder die 30-Tage-Regel.
- **30-Tage-Regel gegen Verbraucher ohne Hinweis** angewandt — gegenüber einem **Verbraucher** ohne Rechnungshinweis tritt kein Verzug nach § 286 Abs. 3 BGB ein.
- **Falscher Zinssatz** — 9 Prozentpunkte über dem Basiszinssatz nur ohne Verbraucherbeteiligung; sonst 5 Prozentpunkte über dem Basiszinssatz.
- **Verzugspauschale im Arbeitsrecht** angesetzt — unzulässig (§ 12a Abs. 1 ArbGG, BAG 8 AZR 26/18, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BAG&Datum=25.09.2018&Aktenzeichen=8%20AZR%2026/18)).
- **Basiszinssatz** nicht zum Verzugszeitraum, sondern pauschal angesetzt — er ändert sich halbjährlich.
- **Erfundenes Aktenzeichen** — niemals ein Urteil zitieren, das nicht verifiziert ist.

## Quellen

### Statute

- [§ 286 BGB](https://www.gesetze-im-internet.de/bgb/__286.html) (Verzug des Schuldners)
- [§ 288 BGB](https://www.gesetze-im-internet.de/bgb/__288.html) (Verzugszinsen und sonstiger Verzugsschaden)
- [§ 280 BGB](https://www.gesetze-im-internet.de/bgb/__280.html) (Schadensersatz wegen Pflichtverletzung)
- § 247 BGB (Basiszinssatz), § 271 BGB (Leistungszeit), § 12a Abs. 1 ArbGG

### Kommentare

- Grüneberg, BGB, 83. Aufl. 2024, §§ 286, 288 Rn. 1 ff.
- Ernst, in: MüKoBGB, 9. Aufl. 2022, § 286 Rn. 1 ff., § 288 Rn. 1 ff.

### Rechtsprechung

- BAG, Urt. v. 25.09.2018 – 8 AZR 26/18, BAGE 163, 309 = NZA 2019, 121 (Verzugspauschale § 288 Abs. 5 BGB im Arbeitsrecht ausgeschlossen, § 12a Abs. 1 ArbGG), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BAG&Datum=25.09.2018&Aktenzeichen=8%20AZR%2026/18)

## Ausgabeformat

```
VERZUG / MAHNUNG — <Forderung> — <Datum>

I.   Fälligkeit / Anspruch            [✅ / 🟡 / ❌]
II.  Verzugseintritt                  [Mahnung § 286 I / entbehrlich § 286 II / 30-Tage-Regel § 286 III]
       Verzugsbeginn:                 <TT.MM.JJJJ>
III. Verbraucher beteiligt?           [ja / nein]
IV.  Verzugszinsen                    [5 / 9 Prozentpunkte über dem Basiszinssatz § 288 I/II]
V.   Verzugspauschale 40 EUR          [✅ / ❌ — Begründung; Arbeitsrecht-Ausnahme?]
VI.  Weiterer Verzögerungsschaden     [§ 280 II i.V.m. § 286 — dem Grunde nach]

Mahnschreiben-Entwurf:                [beigefügt / nicht erforderlich]

Gesamtbefund: [🟢 / 🟡 / 🔴]
Offene Tatsachen: <Liste — markiert>
```

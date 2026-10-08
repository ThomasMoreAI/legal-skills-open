---
name: liquiditaetsplanung-13-wochen-borghei
title: /insolvenzrecht:liquiditaetsplanung-13-wochen
description: 13-Wochen-Liquiditätsplanung als Frühwarn-Instrument für Krisenunternehmen und Anker der Zahlungsunfähigkeitsprüfung nach § 17 InsO. IDW-S-11-konforme Methodik, rollierende Aktualisierung, Zahlungsstockungsabgrenzung. Use when ein Mandant frühzeitig Liquiditätsentwicklung beurteilen oder die Zahlungsunfähigkeit nach § 17 InsO operativ prüfen muss.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/insolvenzrecht/skills/liquiditaetsplanung-13-wochen
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: bankruptcy
language: de
---

# /insolvenzrecht:liquiditaetsplanung-13-wochen

## Zweck

Die 13-Wochen-Liquiditätsplanung ist das Pflicht-Werkzeug der Krisenfrüherkennung nach **§ 1 StaRUG** und das operative Werkzeug zur Prüfung der Zahlungsunfähigkeit nach **§ 17 InsO**. Sie liefert die Tatsachenbasis, ohne die jede insolvenzrechtliche Bewertung haltlos bleibt.

## Eingaben

- Aktueller Kontostand und Liquiditätsreserven (Kreditlinien, ungenutzte Tranchen)
- Fällige Verbindlichkeiten (Datum, Betrag, Gläubiger, Rang)
- Erwartete Zahlungseingänge (Forderungen mit Zahlungsziel, Sicherheit der Realisierung)
- Operative Auszahlungen (Löhne, Sozialversicherung, Lieferanten, Mieten, Steuern)
- Außerordentliche Posten (Vergleichszahlungen, Investitionen)

## Ablauf

### 1. Grundstruktur (IDW S 11)

| Position | Woche 1 | Woche 2 | … | Woche 13 |
|---|---|---|---|---|
| Anfangsbestand | | | | |
| **Einzahlungen** | | | | |
| Kundenzahlungen | | | | |
| Sonstige Einzahlungen | | | | |
| **Auszahlungen** | | | | |
| Löhne / Sozialabgaben | | | | |
| Lieferanten | | | | |
| Miete / Versicherung | | | | |
| Steuern | | | | |
| Tilgung / Zinsen | | | | |
| Sonstiges | | | | |
| Endbestand | | | | |
| Liquiditätslinie | | | | |
| **Lücke / Überschuss** | | | | |

### 2. Bewertung gegen § 17 InsO

Zahlungsunfähigkeit: nicht in der Lage, **fällige** Zahlungspflichten zu erfüllen. Methodik nach BGH-Rechtsprechung:

1. **Statusrechnung** zum Stichtag: aktive Liquidität (Kasse + Bankguthaben + zugesagte Kreditlinie + binnen 3 Wochen verfügbare Mittel) vs. fällige Verbindlichkeiten.
2. **Liquiditätslücke** = (fällige Verbindlichkeiten – verfügbare liquide Mittel) / fällige Verbindlichkeiten.
3. **Faustformel**: Lücke ≥ 10 % über mehr als drei Wochen → Zahlungsunfähigkeit. BGH, Beschl. v. 24.05.2005 – IX ZR 123/04, NJW 2005, 3062 `[unverifiziert – prüfen]`.
4. **Abgrenzung Zahlungsstockung**: kurzfristig (< 3 Wochen), Liquiditätslücke < 10 %, abzusehende Behebung.

### 3. Rollierung

13 Wochen ist das **Mindestmaß**. Best Practice:

- Wöchentliche Aktualisierung mit Soll-Ist-Vergleich der Vorwoche.
- Quartalsweise Erweiterung auf 26 Wochen (für StaRUG-Prognosezeitraum).
- 13-Monats-Planung zur Fortbestehensprognose (24 Monate seit StaRUG-Reform).

### 4. Stress-Szenarien

Mindestens drei Szenarien:

- **Best Case** (geplante Maßnahmen wirken)
- **Base Case** (Fortschreibung Status quo)
- **Stress Case** (Hauptkunde fällt aus, Kreditlinie wird gekündigt)

Bei Stress Case eintretender Liquiditätslücke → frühzeitig Sanierungsmaßnahmen aktivieren (StaRUG, Investorensuche, Vergleichsverhandlungen).

### 5. Ergänzung Free-Cash-Flow

Für aussagekräftige Krisenfrüherkennung ergänzen:

- Auftragsbestand-Reichweite (Monate)
- Working-Capital-Entwicklung (Forderungs- und Lagerbestand)
- Free-Cash-Flow vor Steuern
- Verschuldungsquote (Net Debt / EBITDA)

### 6. Dokumentation

Liquiditätsplanung als interne Krisenakte sichern:

- Stand und Änderungen wöchentlich dokumentieren
- Annahmen offenlegen (Zahlungsziele, Mahnverhalten)
- Soll-Ist-Abweichungen begründen
- Entscheidungsprotokolle bei Maßnahmen

## Quellen

### Statute / Standards

- [§ 17 InsO](https://www.gesetze-im-internet.de/inso/__17.html), [§ 1 StaRUG](https://www.gesetze-im-internet.de/starug/__1.html)
- IDW S 11 (Beurteilung des Vorliegens von Insolvenzeröffnungsgründen)
- IDW PS 800 / IDW S 6 (Sanierungsfachprüfung)

### Rechtsprechung

- BGH, Beschl. v. 24.05.2005 – IX ZR 123/04, NJW 2005, 3062 `[unverifiziert – prüfen]`
- BGH, Urt. v. 09.11.2017 – IX ZR 226/16, NZI 2018, 76 `[unverifiziert – prüfen]`

### Kommentare

- Bork, in: Bork / Hölzle, Insolvenzrecht, 2. Aufl. 2023, § 17 InsO Rn. 1 ff.
- Schmidt, Sanierungsrecht, 4. Aufl. 2023

## Ausgabeformat

```
13-WOCHEN-LIQUIDITÄTSPLANUNG — <Mandat> — Stichtag <Datum>

Statusrechnung (Stichtag):
  Aktive Liquidität (Kasse, Banken, Kreditlinie binnen 3 Wo): <EUR>
  Fällige Verbindlichkeiten:                                    <EUR>
  Liquiditätslücke:                                              <% / EUR>
  Bewertung:                                                     [Zahlungsstockung / Zahlungsunfähigkeit]

13-Wochen-Plan (rollierend, Base Case):
  Woche  | Einzahlung | Auszahlung | Endbestand | Linie | Lücke/Überschuss
  ...

Szenarien:
  Best Case:    Minimum Liquidität <EUR>, Wo <N>
  Base Case:    Minimum Liquidität <EUR>, Wo <N>
  Stress Case:  Minimum Liquidität <EUR>, Wo <N>  [🔴 Maßnahmen erforderlich]

Empfohlene Maßnahmen:
  - <…>

Wiedervorlage: <wöchentlich, nächster Termin>
```

## Risiken / typische Fehler

- **Optimistische Zahlungseingänge** — Wirtschaftsprüfer rechnen mit historischer DSO, nicht Wunsch.
- **Sozialabgaben unterschätzt** — Beitragsabführung Pflicht der GF persönlich nach § 28e SGB IV.
- **Tilgungstermine vergessen** — Bullet-Strukturen führen zu plötzlichen Spitzen.
- **Working-Capital-Effekte ignoriert** — Saisongeschäft erfordert Forecast-Anpassung.
- **„Wir kriegen das hin"-Mentalität** — Stress Case ist Pflicht, nicht Option.
- **Soll-Ist-Vergleich nicht dokumentiert** — keine Krisenfrüherkennung im Sinn § 1 StaRUG.

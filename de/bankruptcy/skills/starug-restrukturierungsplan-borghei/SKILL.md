---
name: starug-restrukturierungsplan-borghei
title: /insolvenzrecht:starug-restrukturierungsplan
description: Aufstellung und Annahme eines Restrukturierungsplans nach StaRUG. Anzeige § 31 StaRUG, Restrukturierungsbeauftragter § 73 StaRUG, Stabilisierungsanordnung § 49 StaRUG, Planabstimmung in Gruppen § 24 StaRUG, gerichtliche Bestätigung § 60 StaRUG. Use when ein Unternehmen in drohender Zahlungsunfähigkeit eine vorinsolvenzliche Sanierung anstrebt.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/insolvenzrecht/skills/starug-restrukturierungsplan
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: bankruptcy
language: de
---

# /insolvenzrecht:starug-restrukturierungsplan

## Zweck

Das StaRUG (in Kraft seit 01.01.2021) ist Deutschlands Umsetzung der EU-Restrukturierungs-Richtlinie 2019/1023. Es eröffnet bei **drohender Zahlungsunfähigkeit** ([§ 18 InsO](https://www.gesetze-im-internet.de/inso/__18.html)) einen vorinsolvenzlichen Restrukturierungsrahmen: Mehrheitsabstimmung über Forderungen, ohne ein Insolvenzverfahren auszulösen. Dieser Skill strukturiert den Weg von der Anzeige bis zur gerichtlichen Bestätigung.

## Eingaben

- Aktuelle Liquiditäts- und Bilanzlage (Vorprüfung: drohende ZU, **nicht** bereits ZU oder Überschuldung — sonst § 15a InsO greift)
- Gläubigerlandschaft (Anzahl, Beträge, Sicherheiten, Rangstellung)
- Geplante Eingriffe (Forderungsverzicht, Stundung, Debt-Equity-Swap, Vertragsbeendigung § 51 StaRUG)
- Stakeholder-Position (Banken, Lieferanten, AN, Gesellschafter)

## Ablauf

### 1. Anwendungsbereich ([§ 29 StaRUG](https://www.gesetze-im-internet.de/starug/__29.html))

- **Drohende Zahlungsunfähigkeit** muss vorliegen (§ 18 InsO).
- **Keine** Zahlungsunfähigkeit § 17 InsO oder Überschuldung § 19 InsO — sonst gilt § 15a InsO-Antragspflicht.
- Keine fest beschränkten Schuldnergruppen ausgeschlossen (anders als der EU-Richtlinienvorschlag — Banken etc. sind erfasst, soweit nicht durch Spezialgesetz ausgenommen).

### 2. Anzeige beim Restrukturierungsgericht ([§ 31 StaRUG](https://www.gesetze-im-internet.de/starug/__31.html))

Anzeige eröffnet das Verfahren. Inhalt:

- Stand der Verhandlungen
- Verzeichnis der Gläubigerinteressen
- Restrukturierungskonzept (kann grob sein, wird im Lauf konkretisiert)

Wirkung: Krisenfrüherkennungs- und Krisenmanagementpflichten nach § 1 StaRUG sind nun verstärkt; § 15a InsO bleibt aber bei Insolvenzreife geltend.

### 3. Restrukturierungsbeauftragter ([§§ 73 ff. StaRUG](https://www.gesetze-im-internet.de/starug/__73.html))

- **Fakultativ** bei Anzeige; **obligatorisch** bei Stabilisierungsanordnung oder Eingriffen in Verbraucherrechte.
- Aufgabe: Plausibilitätskontrolle, Verhandlungsleitung, gerichtliche Berichte.
- Auswahl durch Gericht aus Liste qualifizierter Personen.

### 4. Restrukturierungsplan ([§§ 5–22 StaRUG](https://www.gesetze-im-internet.de/starug/__5.html))

#### Inhalt

- Beschreibender Teil: Schuldnerlage, Krisenursache, Restrukturierungsziel
- Gestaltender Teil: Eingriffe in Forderungen (Verzicht, Stundung, Umwandlung), Rechte der Anteilsinhaber, Sicherheiten

#### Gruppenbildung (§ 9 StaRUG)

Gläubiger in Gruppen mit gleichartigen Rechten:

- Absonderungsberechtigte
- Nachrangige Gläubiger (§ 39 InsO)
- Anleihegläubiger
- Lieferanten / Handelsforderungen
- Anteilsinhaber

#### Eingriffe in Vertragsbeziehungen (§§ 49–51 StaRUG)

- Stabilisierungsanordnung (§ 49): Vollstreckungssperre bis 3 Monate, verlängerbar auf 8 Monate.
- **Beendigung wechselseitig nicht erfüllter Verträge** (§ 51): Schuldner kann auswählen, ähnlich § 103 InsO.

### 5. Planabstimmung ([§ 24 StaRUG](https://www.gesetze-im-internet.de/starug/__24.html))

- **75 % der Forderungssummen** in jeder Gruppe (Kopf- und Summenmehrheit, eigentlich nur Summe — § 24 Abs. 1, kein Kopfquotum erforderlich, abweichend von InsO).
- **Cross-Class Cram-Down** (§ 26 StaRUG): Eine ablehnende Gruppe kann überstimmt werden, wenn sie nicht schlechter gestellt wird als in der Vergleichsalternative und die Mehrheit der Gruppen zugestimmt hat.

### 6. Gerichtliche Bestätigung ([§§ 60 ff. StaRUG](https://www.gesetze-im-internet.de/starug/__60.html))

Voraussetzungen u.a.:

- Plan rechtsgültig zustande gekommen
- Inhalt mit Recht vereinbar
- Cross-Class Cram-Down rechtmäßig
- Vergleichsrechnung gegenüber Alternativszenario (Liquidation/Insolvenz) zugunsten der überstimmten Gläubiger

Mit Bestätigung wird der Plan wirksam (§ 67 StaRUG).

### 7. Anschlussinsolvenz-Risiko

Bei Misslingen oder Eintritt von ZU / Überschuldung während des StaRUG-Verfahrens entsteht erneut Antragspflicht nach § 15a InsO. **Eine StaRUG-Anzeige suspendiert § 15a nicht.**

## Quellen

### Statute

- [StaRUG (Volltext)](https://www.gesetze-im-internet.de/starug/)
- [§ 1, § 5, § 9, § 24, § 26, § 29, § 31, § 49, § 51, § 60, § 73 StaRUG](https://www.gesetze-im-internet.de/starug/)
- [§ 18 InsO](https://www.gesetze-im-internet.de/inso/__18.html), [§ 15a InsO](https://www.gesetze-im-internet.de/inso/__15a.html)
- [Richtlinie (EU) 2019/1023](https://eur-lex.europa.eu/eli/dir/2019/1023/oj)

### Kommentare

- Bork, StaRUG, 2. Aufl. 2023
- Pannen / Riedemann / Smid, StaRUG, 1. Aufl. 2021
- Skauradszun, ZIP 2023, 1 ff. (Aufsatz zum Cross-Class Cram-Down)

### Rechtsprechung

- AG Köln, Beschl. v. 03.03.2021 – 83 RES 1/21, NZI 2021, 363 `[unverifiziert – prüfen]` (erste StaRUG-Anzeigen)
- BGH, Beschl. v. 19.10.2023 – IX ZB 49/22 `[unverifiziert – prüfen]`

## Ausgabeformat

```
StaRUG-RESTRUKTURIERUNGSPLAN — <Mandat> — <Datum>

I.    Anwendungsvoraussetzungen
      a) Drohende ZU                  [✓ / nicht erfüllt]
      b) Keine ZU / ÜS                [✓ / 🔴 Insolvenzantragspflicht!]
II.   Anzeige § 31                    Stand: <Datum>
III.  Restrukturierungsbeauftragter
      Bestellt:                       [ja / nein, Begründung]
      Person:                         <…>
IV.   Planinhalt
      Eingriffe: <Liste>
      Stabilisierungsanordnung § 49:  [ja, Frist <…> / nein]
      Vertragsbeendigung § 51:        [ja, Verträge <…> / nein]
V.    Gruppenbildung
      Gruppe 1 (Absonderungsber.):    <N Gläubiger, EUR Forderung>
      Gruppe 2 ...
VI.   Abstimmung
      Mehrheiten pro Gruppe:          <%-Werte>
      Cross-Class Cram-Down nötig:    [ja / nein]
VII.  Gerichtliche Bestätigung
      Frist:                          <…>
      Vergleichsrechnung:             [günstiger / nicht günstiger]

Risiko Anschlussinsolvenz: [🟢 / 🟡 / 🔴]
Empfehlung: <…>
```

## Risiken / typische Fehler

- **Bereits Insolvenzreife** (ZU oder Überschuldung) — StaRUG nicht mehr offen, § 15a InsO-Antragspflicht greift.
- **Cross-Class Cram-Down ohne Vergleichsrechnung** — gerichtliche Bestätigung wird versagt.
- **Gruppenbildung manipulativ** — Schaffung künstlicher Mehrheiten gefährdet Plan.
- **Stabilisierungsanordnung als Dauerlösung verstanden** — max. 8 Monate, dann läuft die Sperre ab.
- **§ 15a InsO vergessen** — Anzeige nach § 31 StaRUG begründet **keine** Stilllegung der Insolvenzantragspflicht.
- **Vertragsbeendigung § 51 zu spät** — bei laufenden, defizitären Verträgen früh die Beendigung erwägen.

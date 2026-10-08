---
name: nebenbestimmungen-borghei
title: /verwaltungsrecht:nebenbestimmungen
description: Prüfung von Nebenbestimmungen zum Verwaltungsakt nach § 36 VwVfG (Befristung, Bedingung, Auflage, Widerrufsvorbehalt, Auflagenvorbehalt) und ihres Rechtsschutzes, insbesondere der isolierten Anfechtbarkeit der Auflage. Use when ein begünstigender Verwaltungsakt mit einer belastenden Nebenbestimmung versehen ist und nur die Nebenbestimmung beseitigt werden soll.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/verwaltungsrecht/skills/nebenbestimmungen
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: administrative
language: de
---

# /verwaltungsrecht:nebenbestimmungen

## Zweck

Begünstigende Verwaltungsakte (Genehmigung, Erlaubnis) werden häufig mit belastenden Nebenbestimmungen verbunden. Der Mandant will regelmäßig den Hauptverwaltungsakt behalten und nur die Belastung loswerden. Diese Skill ordnet die Nebenbestimmung der richtigen Kategorie des [§ 36 VwVfG](https://www.gesetze-im-internet.de/vwvfg/__36.html) zu, prüft ihre Rechtmäßigkeit und bestimmt die statthafte Klageart, insbesondere die isolierte Anfechtbarkeit der Auflage.

## Eingaben

- Begünstigender Hauptverwaltungsakt (Inhalt, Adressat)
- Wortlaut der Nebenbestimmung(en)
- Ermächtigungslage: gebundener VA oder Ermessens-VA
- Belastung durch die Nebenbestimmung (Kosten, Pflichten, Befristung)
- Anliegen: Hauptbegünstigung behalten, Nebenbestimmung beseitigen

## Sub-Agent-Architektur

Die Prüfung läuft in drei Strängen in Prosa. Der **Qualifikations-Agent** ordnet die Nebenbestimmung einer der fünf Kategorien des § 36 Abs. 2 VwVfG zu (Befristung, Bedingung, Auflage, Widerrufsvorbehalt, Auflagenvorbehalt) und grenzt die Auflage von der modifizierenden Gewährung ab. Der **Rechtmäßigkeits-Agent** prüft die Zulässigkeit nach § 36 Abs. 1 VwVfG (gebundener VA nur bei Sicherung der Voraussetzungen) und Abs. 3 (kein Zweckwiderspruch). Der **Rechtsschutz-Agent** bestimmt die statthafte Klageart und entscheidet, ob die Nebenbestimmung isoliert anfechtbar ist. Die Stränge werden zu einer Empfehlung zur Klageart zusammengeführt.

## Ablauf

### 1. Qualifikation der Nebenbestimmung ([§ 36 Abs. 2 VwVfG](https://www.gesetze-im-internet.de/vwvfg/__36.html))

- **Befristung**: VA gilt ab/bis/für einen bestimmten Zeitraum (§ 36 Abs. 2 Nr. 1)
- **Bedingung**: Wirksamkeit hängt vom ungewissen Eintritt eines künftigen Ereignisses ab (Nr. 2) – aufschiebend oder auflösend
- **Widerrufsvorbehalt**: Behörde behält den Widerruf vor (Nr. 3)
- **Auflage**: selbstständiges Gebot eines Tuns, Duldens oder Unterlassens (Nr. 4)
- **Auflagenvorbehalt**: Vorbehalt, später Auflagen aufzunehmen oder zu ändern (Nr. 5)

**Abgrenzung Auflage / Bedingung**: Die Bedingung lässt die Wirksamkeit des VA automatisch entstehen oder entfallen; die Auflage ist ein selbstständig vollstreckbares Gebot, das die Wirksamkeit des Haupt-VA unberührt lässt („Bedingung suspendiert, Auflage verpflichtet").

### 2. Zulässigkeit ([§ 36 Abs. 1 VwVfG](https://www.gesetze-im-internet.de/vwvfg/__36.html))

- **Ermessens-VA**: Nebenbestimmung nach pflichtgemäßem Ermessen zulässig
- **Gebundener VA**: Nebenbestimmung nur, wenn sie sicherstellt, dass die gesetzlichen Voraussetzungen erfüllt werden (§ 36 Abs. 1 Alt. 2), oder durch Rechtsvorschrift zugelassen
- **Koppelungsverbot / Zweckbindung** (§ 36 Abs. 3): die Nebenbestimmung darf dem Zweck des Haupt-VA nicht zuwiderlaufen

### 3. Rechtsschutz – statthafte Klageart

#### Isolierte Anfechtbarkeit der Auflage

Nach der Rechtsprechung des BVerwG ist gegen jede belastende Nebenbestimmung die **Anfechtungsklage** statthaft; ob die Aufhebung der Nebenbestimmung allein in Betracht kommt (isolierte Anfechtbarkeit), ist eine Frage der Begründetheit. Die isolierte Anfechtungsklage hat Erfolg, wenn der Haupt-VA sinnvoller- und rechtmäßigerweise ohne die Nebenbestimmung bestehen bleiben kann.

#### Auflage vs. unselbstständige Nebenbestimmung

- **Auflage**: regelmäßig isoliert anfechtbar, da selbstständiger Regelungsgehalt
- **Befristung / Bedingung / modifizierende Gewährung**: oft nur Verpflichtungsklage auf VA ohne Nebenbestimmung, da der Haupt-VA ohne sie nicht teilbar ist

### 4. Begründetheit der isolierten Anfechtung

- Nebenbestimmung rechtswidrig (z. B. Verstoß gegen § 36 Abs. 1 oder Abs. 3 VwVfG, Ermessensfehler)
- Haupt-VA bleibt ohne Nebenbestimmung rechtmäßig und sinnvoll teilbar

## Quellen

### Statute

- [§ 36 VwVfG](https://www.gesetze-im-internet.de/vwvfg/__36.html) (Nebenbestimmungen zum Verwaltungsakt)
- [§ 35 VwVfG](https://www.gesetze-im-internet.de/vwvfg/__35.html) (Begriff des Verwaltungsakts)
- [§ 42 VwGO](https://www.gesetze-im-internet.de/vwgo/__42.html) (Anfechtungs-/Verpflichtungsklage)
- [§ 113 VwGO](https://www.gesetze-im-internet.de/vwgo/__113.html) (Urteilsausspruch)

### Kommentare

- Stelkens / Bonk / Sachs, VwVfG, 10. Aufl. 2023, § 36
- Kopp / Ramsauer, VwVfG, 24. Aufl., § 36
- Maurer / Waldhoff, Allgemeines Verwaltungsrecht, 20. Aufl.

### Rechtsprechung

- BVerwG, Urt. v. 22.11.2000 – 11 C 2.00 (isolierte Anfechtbarkeit) `[unverifiziert – prüfen]`
- BVerwG, Urt. v. 17.02.1984 – 4 C 70.80 (Auflage / Bedingung) `[unverifiziert – prüfen]`

## Ausgabeformat

```
NEBENBESTIMMUNGEN-PRÜFUNG — <Mandat> — <Datum>

I.    Haupt-Verwaltungsakt
      Begünstigung:                   <Genehmigung / Erlaubnis>
      Gebunden / Ermessen:            <…>

II.   Qualifikation der Nebenbestimmung
      Typ:                            [Befristung / Bedingung / Auflage /
                                       Widerrufsvorbehalt / Auflagenvorbehalt]
      Auflage oder Bedingung:         <Abgrenzung>

III.  Zulässigkeit § 36 VwVfG
      Abs. 1 (gebundener VA):         <…>
      Abs. 3 (Zweckbindung):          <…>

IV.   Rechtsschutz
      Statthafte Klageart:            [Anfechtung / Verpflichtung]
      Isolierte Anfechtbarkeit:       [ja / nein]

V.    Begründetheit
      Nebenbestimmung rechtswidrig:   [+ / –]
      Haupt-VA teilbar:               [+ / –]

Empfehlung: <…>
```

## Risiken / typische Fehler

- **Auflage und Bedingung verwechselt** — die Qualifikation entscheidet über Wirksamkeit und Klageart; eine als Auflage gewertete Bedingung führt zur falschen Antragsfassung.
- **Falsche Klageart gewählt** — wer auf isolierte Anfechtung der untrennbaren Nebenbestimmung setzt, statt Verpflichtungsklage zu erheben, riskiert Abweisung.
- **Modifizierende Gewährung übersehen** — sie ist keine Nebenbestimmung, sondern Inhaltsbestimmung; isolierte Anfechtung scheidet aus.
- **Koppelungsverbot nach § 36 Abs. 3 VwVfG nicht geprüft** — eine zweckwidrige Nebenbestimmung ist rechtswidrig und sollte angegriffen werden.

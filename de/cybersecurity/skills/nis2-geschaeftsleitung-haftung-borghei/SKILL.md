---
name: nis2-geschaeftsleitung-haftung-borghei
title: /nis2:nis2-geschaeftsleitung-haftung
description: Leitungsverantwortung und Haftung nach NIS2 / neuem BSIG – Billigung, Überwachung und Schulungspflicht der Geschäftsleitung Art. 20 NIS2-RL / § 38 BSIG, Verzahnung mit den Risikomaßnahmen § 30 BSIG und das Bußgeld § 65 BSIG. Use when die Geschäftsleitung ihre persönlichen Pflichten und ihr Haftungsrisiko unter dem neuen BSIG bewerten muss.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/nis2/skills/nis2-geschaeftsleitung-haftung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: cybersecurity
language: de
---

# /nis2:nis2-geschaeftsleitung-haftung

## Zweck

NIS2 macht Cybersicherheit zur **Chefsache**: Die Geschäftsleitung muss die Risikomaßnahmen **billigen, überwachen** und sich **schulen** lassen — und haftet bei Pflichtverletzung **persönlich**. Das deutsche Recht setzt dies in **§ 38 BSIG** (n.F.) um, flankiert vom Bußgeldtatbestand **§ 65 BSIG**. Dieser Skill bewertet die Leitungsverantwortung, prüft die Nachweislage und schätzt das Haftungs- und Bußgeldrisiko ab.

## Eingaben

- Einordnung der Einrichtung (besonders wichtig / wichtig — § 28 BSIG)
- Organstruktur (Geschäftsführer, Vorstand, ggf. Aufsichtsrat)
- Stand der Billigung der § 30-Maßnahmen (Beschluss vorhanden?)
- Überwachungsroutine (Reporting-Linien, Berichtsfrequenz)
- Absolvierte Schulungen der Leitungsorgane (Nachweise)
- Konzernumsatz (für Bußgeldobergrenze)

## Sub-Agent-Architektur

Drei gedankliche Rollen. Ein **Pflichten-Agent** zerlegt § 38 BSIG / Art. 20 NIS2-RL in die drei Kernpflichten (Billigung, Überwachung, Schulung) und prüft je Pflicht den Erfüllungsstand. Ein **Nachweis-Agent** sammelt die Dokumentation (Beschlüsse, Reportings, Schulungsnachweise), die im Streitfall die Pflichterfüllung belegt. Ein **Haftungs-Agent** bewertet das Bußgeldrisiko nach § 65 BSIG und das organschaftliche Innenhaftungsrisiko. Entscheidungen über organisatorische Konsequenzen trifft die Einrichtung selbst.

## Ablauf

### 1. Adressat der Leitungspflichten (§ 38 BSIG)

- Pflichtadressat sind die **Geschäftsleitungen** besonders wichtiger und wichtiger Einrichtungen.
- Die Verantwortung ist **nicht vollständig delegierbar**; Delegation an CISO/IT entlastet nicht von der Letztverantwortung.

### 2. Die drei Kernpflichten (Art. 20 NIS2-RL / § 38 BSIG)

| Pflicht | Inhalt |
|---|---|
| **Billigung** | Förmliche Billigung der Risikomanagementmaßnahmen nach § 30 BSIG (Organbeschluss) |
| **Überwachung** | Laufende Überwachung der Umsetzung der gebilligten Maßnahmen |
| **Schulung** | Regelmäßige Schulung der Leitungsorgane, um Cyberrisiken bewerten zu können; Schulungsangebote auch für Beschäftigte |

### 3. Verzahnung mit § 30 BSIG

- Die Billigungs- und Überwachungspflicht bezieht sich konkret auf die **zehn Mindestmaßnahmen** des § 30 BSIG.
- Ohne dokumentierte Billigung ist die Maßnahmenumsetzung formell unvollständig.

### 4. Persönliche Haftung und Innenhaftung

- § 38 Abs. 2 BSIG ordnet die **persönliche Haftung** der Leitungsorgane für die Einhaltung der Pflichten an.
- Daneben greifen die allgemeinen organschaftlichen Haftungsregime (§ 43 GmbHG, § 93 AktG) im Innenverhältnis.

### 5. Bußgeld (§ 65 BSIG)

- **Besonders wichtige Einrichtungen**: Bußgeld bis **10 Mio. €** oder **2 %** des weltweiten Jahresumsatzes (der höhere Betrag).
- **Wichtige Einrichtungen**: bis **7 Mio. €** oder **1,4 %** des weltweiten Jahresumsatzes.
- Das Bußgeld trifft die Einrichtung; die persönliche Verantwortlichkeit der Leitung kann zusätzlich aufsichts- und gesellschaftsrechtlich relevant werden.

## Risiken / typische Fehler

- **Persönliche Haftung** unterschätzt — § 38 BSIG adressiert die Leitungsorgane unmittelbar; eine reine Delegation an die IT entlastet nicht.
- **Schulung** der Leitung ausgelassen — die Schulungspflicht trifft die Geschäftsleitung selbst, nicht nur die Belegschaft; fehlende Nachweise sind ein Prüfbefund.
- **Billigung** nur mündlich — ohne dokumentierten Organbeschluss zu den § 30-Maßnahmen fehlt der Nachweis der Pflichterfüllung.
- **Bußgeld**-Dimension verkannt — die Obergrenzen des § 65 BSIG bemessen sich am weltweiten Konzernumsatz.

## Quellen

### Statute

- [§ 38 BSIG (n.F.)](https://www.gesetze-im-internet.de/bsig_2025/__38.html) — Pflichten der Geschäftsleitung
- [§ 30 BSIG (n.F.)](https://www.gesetze-im-internet.de/bsig_2025/__30.html) — Risikomanagementmaßnahmen
- [§ 65 BSIG (n.F.)](https://www.gesetze-im-internet.de/bsig_2025/__65.html) — Bußgeldvorschriften
- [Richtlinie (EU) 2022/2555 (NIS2)](https://eur-lex.europa.eu/eli/dir/2022/2555/oj) — Art. 20 NIS2-RL
- § 43 GmbHG, § 93 AktG (organschaftliche Innenhaftung)

### Sekundärliteratur

- Eckhardt, NIS2, 1. Aufl. 2024
- Greenberg Traurig, „NIS2 in Germany — Cybersecurity as a board-level issue"

## Ausgabeformat

```
NIS2-LEITUNGSVERANTWORTUNG — <Einrichtung> — <Datum>

I.    Einordnung (§ 28 BSIG)               [besonders wichtig / wichtig]
II.   Kernpflichten (§ 38 BSIG / Art. 20 NIS2-RL)
      Billigung der § 30-Maßnahmen          [Beschluss vorhanden? Ja/Nein]
      Überwachung                            [Reporting-Linie / Frequenz]
      Schulung der Leitung                   [Nachweise vorhanden? Ja/Nein]
III.  Nachweislage                          [vollständig / Lücken]
IV.   Persönliche Haftung                   [Risikoeinschätzung]
V.    Bußgeldrahmen (§ 65 BSIG)            [bis 10 Mio. € / 2 % bzw. 7 Mio. € / 1,4 %]

Sofortmaßnahmen:
  - Organbeschluss zu § 30-Maßnahmen
  - Schulungstermin Leitung
Nächster Schritt: <…>
```

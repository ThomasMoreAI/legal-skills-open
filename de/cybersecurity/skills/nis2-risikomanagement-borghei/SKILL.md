---
name: nis2-risikomanagement-borghei
title: /nis2:nis2-risikomanagement
description: Aufbau der Risikomanagementmaßnahmen nach NIS2 / neuem BSIG – All-Hazards-Ansatz und die zehn Mindestmaßnahmen Art. 21 NIS2-RL / § 30 BSIG, Verhältnismäßigkeit, Verzahnung mit Leitungspflichten § 38 BSIG. Use when eine besonders wichtige oder wichtige Einrichtung ihre technischen und organisatorischen Maßnahmen nach dem neuen BSIG aufsetzt oder eine Gap-Analyse durchführt.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/nis2/skills/nis2-risikomanagement
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: cybersecurity
language: de
---

# /nis2:nis2-risikomanagement

## Zweck

Das **NIS2-Umsetzungsgesetz (NIS2UmsuCG)** ist am 06.12.2025 in Kraft getreten und hat das BSIG neu gefasst. Die Risikomanagementpflichten sitzen jetzt in **§ 30 BSIG** (n.F.) — nicht mehr in den alten §§ 8a/8b BSIG. § 30 BSIG setzt Art. 21 NIS2-RL um und verlangt einen **All-Hazards-Ansatz** mit zehn Mindestmaßnahmen. Dieser Skill liefert die Gap-Analyse gegen diesen Katalog und verankert die Verhältnismäßigkeit.

## Eingaben

- Einordnung der Einrichtung (besonders wichtig / wichtig — § 28 BSIG)
- Sektor und Größenklasse (Risiko- und Verhältnismäßigkeitsmaßstab)
- Bestehendes ISMS (z. B. ISO 27001, BSI-Grundschutz)
- Inventar kritischer Systeme und Lieferketten / Dienstleister
- Vorhandene Notfall-, Backup- und Krisenkonzepte
- Stand der Geschäftsleitungs-Einbindung (§ 38 BSIG)

## Sub-Agent-Architektur

Drei gedankliche Rollen. Ein **Katalog-Agent** prüft jede der zehn Mindestmaßnahmen des § 30 BSIG / Art. 21 NIS2-RL einzeln gegen den Ist-Stand und markiert Lücken. Ein **Verhältnismäßigkeits-Agent** kalibriert Umfang und Tiefe jeder Maßnahme an Größe, Risikoexposition und Sektor der Einrichtung. Ein **Governance-Agent** verknüpft die Maßnahmen mit der Billigungs- und Überwachungspflicht der Geschäftsleitung (§ 38 BSIG) und der Meldepflicht (§ 32 BSIG). Die Rollen erzeugen eine priorisierte Maßnahmen-Roadmap; die Billigung erfolgt durch die Leitung.

## Ablauf

### 1. Anwendbarkeit und All-Hazards-Ansatz (§ 30 BSIG)

- Pflichtadressaten: **besonders wichtige** und **wichtige Einrichtungen** (§ 28 BSIG).
- Maßstab ist der **All-Hazards-Ansatz**: Schutz vor allen Gefahren für Netz- und Informationssysteme, einschließlich physischer Umgebung.
- Maßnahmen müssen dem Stand der Technik entsprechen.

### 2. Die zehn Mindestmaßnahmen (Art. 21 NIS2-RL / § 30 BSIG)

| # | Maßnahme |
|---|---|
| 1 | Risikoanalyse- und Sicherheitskonzepte für Informationssysteme |
| 2 | Bewältigung von Sicherheitsvorfällen (Incident Handling) |
| 3 | Aufrechterhaltung des Betriebs, Backup-Management, Krisenmanagement |
| 4 | Sicherheit der **Lieferkette** (inkl. Dienstleister) |
| 5 | Sicherheit bei Erwerb, Entwicklung und Wartung von Systemen |
| 6 | Bewertung der Wirksamkeit der Risikomaßnahmen |
| 7 | Cyberhygiene und Schulungen |
| 8 | Kryptografie und **Verschlüsselung** |
| 9 | Personalsicherheit, Zugriffskontrolle, Asset-Management |
| 10 | Multi-Faktor-Authentifizierung, gesicherte Kommunikation/Notfallkommunikation |

### 3. Verhältnismäßigkeit (§ 30 Abs. 1 BSIG)

- Umfang richtet sich nach Risikoexposition, Größe der Einrichtung sowie Eintrittswahrscheinlichkeit und Schwere von Vorfällen.
- **Verhältnismäßigkeit** rechtfertigt Abstufung, aber keinen Verzicht auf eine der zehn Maßnahmenkategorien.

### 4. Lieferketten-Dimension

- Die **Lieferkette** ist eigenständige Pflichtkategorie: Sicherheitsqualität direkter Anbieter und Dienstleister ist zu bewerten und vertraglich zu sichern.

### 5. Verzahnung Governance und Meldung

- Maßnahmen nach § 30 BSIG sind von der Geschäftsleitung zu **billigen und zu überwachen** (§ 38 BSIG).
- Versäumnisse können nach § 65 BSIG bußgeldbewehrt sein.

## Risiken / typische Fehler

- **All-Hazards-Ansatz** verengt auf reine IT — physische Sicherheit, Personal und Lieferkette gehören dazu.
- **Verhältnismäßigkeit** als Freibrief missverstanden — sie skaliert die Tiefe, erlaubt aber nicht das Weglassen einer der zehn Maßnahmen.
- **Lieferkette** unbeachtet — Vorfälle bei Dienstleistern sind eigenständige Pflichtkategorie (Maßnahme 4).
- **Geschäftsleitung** nicht eingebunden — § 38 BSIG verlangt aktive Billigung und Überwachung der § 30-Maßnahmen.

## Quellen

### Statute

- [§ 30 BSIG (n.F.)](https://www.gesetze-im-internet.de/bsig_2025/__30.html) — Risikomanagementmaßnahmen
- [§ 38 BSIG (n.F.)](https://www.gesetze-im-internet.de/bsig_2025/__38.html) — Pflichten der Geschäftsleitung
- [§ 65 BSIG (n.F.)](https://www.gesetze-im-internet.de/bsig_2025/__65.html) — Bußgeldvorschriften
- [Richtlinie (EU) 2022/2555 (NIS2)](https://eur-lex.europa.eu/eli/dir/2022/2555/oj) — Art. 20 NIS2-RL, Art. 21 NIS2-RL

### Sekundärliteratur

- Eckhardt, NIS2, 1. Aufl. 2024
- Voigt/Schmitz, Cybersicherheitsrecht, 2. Aufl. 2024

## Ausgabeformat

```
NIS2-RISIKOMANAGEMENT — <Einrichtung> — <Datum>

I.    Einordnung (§ 28 BSIG)               [besonders wichtig / wichtig]
II.   All-Hazards-Reife (§ 30 BSIG / Art. 21 NIS2-RL)
      1 Risikoanalyse          [🟢/🟡/🔴]
      2 Incident Handling      [🟢/🟡/🔴]
      3 Business Continuity    [🟢/🟡/🔴]
      4 Lieferkette            [🟢/🟡/🔴]
      …                        bis Maßnahme 10
III.  Verhältnismäßigkeit                   [Maßstab: Größe/Risiko]
IV.   Verzahnung Geschäftsleitung (§ 38 BSIG) [Billigung erfolgt? Ja/Nein]
V.    Bußgeldrisiko (§ 65 BSIG)             [Hinweis]

Roadmap:
  Sofort: <…>   Mittelfristig: <…>
```

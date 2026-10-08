---
name: ict-risikomanagement-borghei
title: /dora:ict-risikomanagement
description: Aufbau eines DORA-konformen IKT-Risikomanagement-Rahmens für Finanzunternehmen – Governance Art. 5, Risikomanagement-Rahmen Art. 6, IKT-Systeme Art. 7, Identifikation Art. 8, Schutz Art. 9, Erkennung Art. 10, Reaktion und Wiederherstellung Art. 11, Lernen Art. 13. Use when ein Finanzunternehmen die DORA-Governance aufsetzt oder eine Gap-Analyse zum bestehenden BAIT/MaRisk-Rahmen durchführt.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/dora/skills/ict-risikomanagement
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: finance
language: de
---

# /dora:ict-risikomanagement

## Zweck

DORA ist die zentrale EU-Cyber-Resilienzverordnung für den Finanzsektor. Bestehende BAIT/MaRisk-Strukturen sind **nicht** automatisch DORA-konform — die Pflichten reichen tiefer (insb. Drittparteien-Register, TLPT, Incident Reporting). Dieser Skill liefert die Gap-Analyse + Roadmap.

## Eingaben

- Art des Finanzunternehmens (CRR-Institut, Versicherer, KAGB-KVG, Krypto-Dienstleister, Zahlungsinstitut etc.)
- Größenklassen-Einordnung (Art. 16: Mikrounternehmen vs. größere)
- Bestehende Rahmenwerke (BAIT, VAIT, KAIT, ZAIT, MaRisk)
- IKT-Drittparteien-Liste
- Letzter Penetrationstest

## Ablauf

### 1. Geltungsbereich (Art. 2 DORA)

DORA gilt insbesondere für:

- Kreditinstitute, Zahlungs- und E-Geld-Institute
- Wertpapierfirmen, Handelsplätze, Zentralverwahrer
- Versicherer und Rückversicherer, Versicherungsvermittler
- KAGB-Kapitalverwaltungsgesellschaften
- Krypto-Dienstleister (CASP) seit MiCA
- Crowdfunding-Dienstleister

### 2. Verhältnis zu BAIT/MaRisk

- BAIT/VAIT/KAIT/ZAIT bleiben **anwendbar**, ergänzen DORA.
- Wo Konflikt: **DORA hat Vorrang als unmittelbar geltende EU-VO**.
- BaFin hat DORA-Auslegungshinweise veröffentlicht; nationale Konkretisierung verbleibt.

### 3. Governance (Art. 5)

- **Leitungsorgan** trägt **letztverantwortlich** für IKT-Risikomanagement.
- Schulung der Leitung verpflichtend (Art. 5 Abs. 4).
- Strategie für digitale operationale Resilienz (Art. 6 Abs. 8).

### 4. IKT-Risikomanagement-Rahmen (Art. 6)

Sechs Säulen:

| Säule | Artikel | Inhalt |
|---|---|---|
| Strategie und Governance | Art. 5–6 | Top-down, mit Budget |
| Identifikation | Art. 8 | Inventar IKT-Vermögenswerte, Funktionsbedeutung |
| Schutz / Prävention | Art. 9 | Identitäts-/Zugriffsmanagement, Verschlüsselung, Patching, Backup |
| Erkennung | Art. 10 | Monitoring, Alarmierung, Eskalation |
| Reaktion & Wiederherstellung | Art. 11–12 | Business Continuity Plan, Recovery Time Objective |
| Lernen | Art. 13 | Post-Incident-Reviews, Verbesserungsmaßnahmen |

### 5. IKT-Vorfallsmanagement (Art. 17–23)

- Klassifizierung nach Schwere (Art. 18) — RTS 2024/1772 definiert Schwellen
- **Frühwarnung** binnen Stunden, **Erstmeldung**, **Endbericht**
- Anlaufstelle: BaFin

### 6. Tests (Art. 24–27)

- **Regelmäßige Tests** mindestens jährlich (Art. 24, 25)
- **Threat-Led Penetration Testing (TLPT)** nach **Art. 26** DORA — für signifikante Institute alle 3 Jahre
- Tester-Akkreditierung nach Art. 27 DORA

### 7. Drittparteien (Art. 28–30)

- **Register** aller IKT-Drittparteienvereinbarungen
- **Kritische Funktionen** verlangen Vertragsmindestinhalte (Art. 30)
- BaFin / EBA-Reporting

### 8. Information Sharing (Art. 45)

Freiwillige Vereinbarungen über Cyber-Bedrohungsinformationen unter Finanzunternehmen.

## Quellen

### Statute

- [VO (EU) 2022/2554 (DORA)](https://eur-lex.europa.eu/eli/reg/2022/2554/oj) — Volltext
- RTS 2024/1772 (Klassifizierung von Vorfällen)
- BaFin-Auslegungshinweise zu DORA

### Verzahnung

- [VO (EU) 2022/2555 (NIS2)](https://eur-lex.europa.eu/eli/dir/2022/2555/oj) — lex generalis im Verhältnis zu DORA
- BAIT, VAIT, KAIT, ZAIT (BaFin)
- MaRisk (AT 7.2)

### Sekundärliteratur

- Linke, in: Hellner/Steuer, Bankrecht und Bankpraxis, DORA-Kapitel
- BeckOK DORA (Online)
- DORA-Kommentar von Maume/Maute/Fromberger (in Vorbereitung)

## Ausgabeformat

```
DORA IKT-RISIKOMANAGEMENT — Gap-Analyse — <Mandant> — <Datum>

I.    Geltungsbereich (Art. 2)        [Ja — Institutsklasse / Mikro nach Art. 16]
II.   Verhältnis zu BAIT/MaRisk       [bestehend / Gap-Liste]
III.  Säulen-Reife
      Governance Art. 5                [🟢 / 🟡 / 🔴]
      Identifikation Art. 8             [🟢 / 🟡 / 🔴]
      Schutz Art. 9                     [🟢 / 🟡 / 🔴]
      Erkennung Art. 10                 [🟢 / 🟡 / 🔴]
      Reaktion / Wiederherstellung Art. 11–12  [🟢 / 🟡 / 🔴]
      Lernen Art. 13                    [🟢 / 🟡 / 🔴]
IV.   Vorfallsmanagement (Art. 17–23)  [Reifegrad / Lücken]
V.    Tests / TLPT (Art. 24–27)         [Letzter / nächster Test]
VI.   Drittparteien-Register (Art. 28) [vollständig / unvollständig]

Roadmap:
  Q1: <…>
  Q2: <…>

Bußgeldrisiko: Bei wesentlichen Verstößen — bis 1 % des durchschnittlichen Tagesumsatzes pro Tag.
```

## Risiken / typische Fehler

- **BAIT als DORA-Ersatz angesehen** — Pflichten gehen über BAIT hinaus.
- **TLPT-Pflicht übersehen** — signifikante Institute werden alle 3 Jahre getestet, Akkreditierung der Tester verlangt.
- **Drittparteien-Register unvollständig** — alle IKT-Dienstleister, nicht nur kritische.
- **Leitungsorgan-Schulung vernachlässigt** — Art. 5 Abs. 4 ist Pflicht.
- **Doppelmeldung NIS2/DSGVO/DORA vergessen** — bei IKT-Vorfall mit personenbezogenen Daten greifen ggf. drei Meldepflichten.

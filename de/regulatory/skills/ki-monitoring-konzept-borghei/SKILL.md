---
name: ki-monitoring-konzept-borghei
title: /ki-governance:ki-monitoring-konzept
description: Konzept zur laufenden Überwachung eines produktiv eingesetzten KI-Systems – Performance-Metriken, Daten- und Concept-Drift, Fairness, Robustheit, Logging Art. 12 KI-VO, menschliche Aufsicht Art. 14 KI-VO, Vorfallsmanagement und Audit-Intervalle nach ISO/IEC 42001. Use when ein KI-System produktiv läuft oder vor Inbetriebnahme das Monitoring-Konzept festgelegt werden muss.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/ki-governance/skills/ki-monitoring-konzept
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: regulatory
language: de
---

# /ki-governance:ki-monitoring-konzept

## Zweck

Der Skill erstellt ein **Monitoring-Konzept** für die laufende Überwachung eines KI-Systems nach Inbetriebnahme: welche Metriken, in welcher Frequenz, mit welchen Schwellenwerten, durch wen, mit welcher Eskalation. Methodisch folgt der Skill **ISO/IEC 42001** (Kap. 8 Operation, Kap. 9 Performance Evaluation) und **NIST AI RMF** (Funktion MEASURE / MANAGE). Gesetzliche Logging- und Aufsichtspflichten der KI-VO (Art. 12 Aufzeichnungspflichten, Art. 14 menschliche Aufsicht, Art. 72 Post-Market Monitoring) werden als Bezugspunkt referenziert; die Pflichtenprüfung selbst gehört in `ki-vo-compliance`.

## Eingaben

- System-ID und Risikoklasse (aus dem Risikoassessment)
- Modelltyp (klassische ML / LLM / Hybrid) und Trainingsdatenquellen
- Einsatzkontext (kritischer / nicht-kritischer Prozess; Hochrisiko-Indizien Anhang III KI-VO)
- Bestehende Telemetrie und Logging-Infrastruktur
- Betroffene Schutzgüter (Personenrechte, Geschäftsgeheimnisse, Berufsgeheimnis)

## Sub-Agent-Architektur

Researcher liefert KI-VO-Anker (Art. 12, 14, 72), DSGVO-Anker (Art. 32), Standards (ISO/IEC 42001 Kap. 8/9, NIST AI RMF MEASURE/MANAGE, BSI AIC4 Anforderungen zu Monitoring), BaFin BDAI / MaRisk AT 7.2. Drafter erstellt das Monitoring-Konzept mit KPI-Tabelle, Eskalationsmatrix und Audit-Plan. Reviewer prüft auf Vollständigkeit der Metriken, klare Schwellenwerte, Logging-Konformität und human-in-the-loop.

## Ablauf

### 1. Monitoring-Dimensionen

| Dimension | Beispiel-Metriken | Bezug |
|---|---|---|
| **Performance** | Accuracy, Precision, Recall, F1, AUC; LLM: Task-Erfolgsrate, Halluzinationsquote | NIST AI RMF MEASURE 2.3 |
| **Datendrift** | Kolmogorov-Smirnov-Test, Population Stability Index (PSI), Embedding-Drift | ISO/IEC 5338, NIST MEASURE 2.4 |
| **Concept Drift** | Performance-Degradation über Zeit, Label-Verteilungsänderung | NIST MEASURE 2.4 |
| **Fairness / Bias** | Demographic Parity, Equal Opportunity, Disparate Impact, gruppenspezifische Fehlerquoten | NIST MEASURE 2.11; AGG-Schutzkategorien |
| **Robustheit / Sicherheit** | Adversarial-Resistenz, Prompt-Injection-Tests, Red-Teaming-Ergebnisse | NIST MEASURE 2.7; BSI AIC4 |
| **Verfügbarkeit** | Uptime, Latenz, Fehler-Rate | klassisches SLO |
| **Compliance / Logging** | Vollständigkeit der Logs gem. Art. 12 KI-VO (bei Hochrisiko), Aufbewahrungsfrist | Art. 12 KI-VO Bezugspunkt |
| **Menschliche Aufsicht** | Override-Quote, Eskalationsraten, Schulungsnachweis | Art. 14 KI-VO Bezugspunkt; Art. 22 DSGVO |

### 2. Frequenz je Risikoklasse

| Risikoklasse (KI-VO-Trigger) | Performance-Check | Drift-Check | Fairness-Audit | Vollständiges Audit |
|---|---|---|---|---|
| Hochrisiko (Anhang I/III) | täglich / kontinuierlich | wöchentlich | quartalsweise | halbjährlich |
| Begrenztes Risiko (Art. 50) | wöchentlich | monatlich | halbjährlich | jährlich |
| Minimales Risiko | monatlich | quartalsweise | jährlich | jährlich |

> Bei sektorspezifischer Aufsicht (BaFin, BAFA, BfArM, BNetzA) deren Frequenz-Anforderungen Vorrang.

### 3. Schwellenwerte und Eskalation

Pro KPI:

- **Grünbereich**: Toleranz, kein Eingriff
- **Gelb (Warnung)**: erhöhte Beobachtung, Ursachenanalyse, Ticket
- **Rot (Alarm)**: Eskalation an AI-Owner + Risk-Owner, ggf. Stilllegung, Vorfallsmeldung

Eskalationsmatrix mit Rollen und Erreichbarkeitsangaben. Bei Hochrisiko-Systemen: dokumentierter Notfallplan.

### 4. Logging und Aufzeichnungen

- **Bei Hochrisiko-Systemen** (Bezugspunkt Art. 12 KI-VO): automatische Aufzeichnung der Lebenszyklus-Ereignisse; Aufbewahrungsfrist gemäß Art. 19 KI-VO – Detailprüfung in `ki-vo-compliance`.
- **Datenschutzrechtlich** (Art. 32 DSGVO + § 9 BDSG-Erwägungen): Logs selbst können personenbezogene Daten enthalten; Zugriffs- und Löschkonzept (Erforderlichkeit, Zweckbindung, Aufbewahrungsfrist).
- **Berufsrechtlich**: Logs als „mitwirkende Personen"-Datenfluss prüfen (§ 203 Abs. 4 StGB).

### 5. Menschliche Aufsicht (human-in-the-loop)

Konkrete Anforderungen (Bezug Art. 14 KI-VO + Art. 22 DSGVO):

- Klare Override-Möglichkeit für die aufsichtführende Person
- Schulung der aufsichtführenden Personen (Art. 4 KI-VO)
- Dokumentation der Override-Entscheidungen
- „Automation Bias" begrenzen: keine bloße Bestätigungsroutine

### 6. Vorfallsmanagement

- **Vorfall-Definition**: schwerer Vorfall iSv Art. 3 Nr. 49 KI-VO (Bezugspunkt) ↔ interner Vorfall (unterhalb der Meldepflicht)
- **Meldewege**: intern (Datenschutzbeauftragte/r, IT-Sicherheit, Compliance); extern (Aufsichtsbehörden – Detailprüfung in `ki-vo-compliance` und `datenschutzrecht`)
- **Lessons Learned**: dokumentierte Nachbereitung, Risk-Register-Update

### 7. Audits

- Internes Audit gemäß ISO/IEC 42001 Kap. 9 (mindestens jährlich)
- Bei Drittanbietern: vertragliches Audit-Recht aus Art. 28 III lit. h DSGVO; BSI AIC4 als Bewertungsmaßstab
- Bei sektorspezifischer Aufsicht: deren Prüfungen einplanen

## Quellen und Zitierweise

Verbindlich: [`../../../references/zitierweise.md`](../../../references/zitierweise.md).

### Unions- und nationales Recht

- [VO (EU) 2024/1689 (KI-VO)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R1689) – Bezugspunkte Art. 12 (Aufzeichnungspflichten), Art. 13 (Transparenz gegenüber Betreibern), Art. 14 (menschliche Aufsicht), Art. 17 (Qualitätsmanagementsystem Anbieter), Art. 26 (Betreiberpflichten), Art. 72 (Beobachtung nach Inverkehrbringen), Art. 73 (schwere Vorfälle). Pflichtenprüfung im Plugin [`ki-vo-compliance`](../../../ki-vo-compliance/README.md).
- [Art. 22 DSGVO](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0679#d1e2839-1-1)
- [Art. 32 DSGVO](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0679#d1e3338-1-1) (Sicherheit der Verarbeitung)
- [§ 1 AGG](https://www.gesetze-im-internet.de/agg/__1.html)

### Industrie-Standards

- **ISO/IEC 42001:2023** – AIMS, insb. Kap. 8 (Operation), Kap. 9 (Performance Evaluation), Kap. 10 (Improvement)
- **ISO/IEC 5338:2023** – AI system life cycle processes
- **NIST AI RMF 1.0** (01/2023) – Funktionen MEASURE und MANAGE
- **BSI AIC4** – Anforderungsgruppen zu Monitoring, Vorfallsmanagement, Audit

### Aufsichtspraxis

- BaFin „Aufsichtliche Anforderungen an den Einsatz von Big Data und Künstlicher Intelligenz" (BDAI) (Juni 2018) `[unverifiziert – prüfen auf bafin.de]`
- BaFin MaRisk AT 4.3 (Auslagerung), AT 7.2 (technisch-organisatorische Ausstattung)
- DSK-Beschlüsse zu KI und automatisierter Entscheidung `[unverifiziert – prüfen auf datenschutzkonferenz-online.de]`

### Kommentare

- Selmayr, in: Ehmann/Selmayr, DSGVO, 3. Aufl. 2024, Art. 22 Rn. 1 ff. `[unverifiziert – prüfen]`
- Jandt, in: Kühling/Buchner, DSGVO/BDSG, 4. Aufl. 2024, Art. 32 Rn. 1 ff. `[unverifiziert – prüfen]`
- Spindler, in: Hartmann/Hilgendorf, KI-Recht, 2024, Kap. Monitoring und Post-Market-Surveillance `[unverifiziert – prüfen]`

### Rechtsprechung (`[unverifiziert – prüfen in Beck-Online / juris / curia.europa.eu]`)

1. EuGH, Urt. v. 07.12.2023 – C-634/21, ECLI:EU:C:2023:957 (SCHUFA, Art. 22 DSGVO)
2. BAG zur Mitbestimmung bei Überwachungseinrichtungen § 87 I Nr. 6 BetrVG

## Ausgabeformat

```
KI-MONITORING-KONZEPT
System: <System-ID>  |  Risikoklasse: <KI-VO-Trigger>  |  Stand: <Datum>

I. Geltungsbereich und Schutzgüter
II. Monitoring-Dimensionen und KPIs
    <Tabelle: Dimension | Metrik | Schwellenwert Grün/Gelb/Rot | Frequenz | Verantwortlich>
III. Logging (Art. 12 KI-VO als Bezugspunkt)
     – Aufbewahrung, Zugriff, Löschkonzept
IV. Menschliche Aufsicht (Art. 14 KI-VO / Art. 22 DSGVO)
    – Override-Mechanik, Schulung Art. 4 KI-VO, Bias-Schutz
V. Eskalationsmatrix
   <Rolle | Erreichbarkeit | Auslöser | Reaktionszeit>
VI. Vorfallsmanagement
    – interner / externer Meldepfad (Detailprüfung /ki-vo-compliance)
VII. Audit-Plan
     – intern jährlich; Drittanbieter (Art. 28 III lit. h DSGVO, BSI AIC4)
VIII. Wiedervorlage und Konzept-Review
IX. Quellenverzeichnis
```

## Risiken / typische Fehler

- **Keine Schwellenwerte** – Monitoring ohne Trigger ist Theater.
- **Drift-Check fehlt** – Modell verschlechtert sich still.
- **Fairness-Audit auf Gesamtsicht** – gruppenspezifische Fehlerquoten werden übersehen.
- **Override-Mechanik nur formal** – Automation Bias bleibt unbehandelt.
- **Logging-Daten als „technisch" framen** – sie sind idR personenbezogen, Art. 32 DSGVO und Aufbewahrungsfrist beachten.
- **KI-VO-Pflichten in das Monitoring-Konzept einbauen** statt in `ki-vo-compliance` zu verweisen – Pflege-Aufwand und Inkonsistenz.
- **Sektorspezifische Aufsicht (BaFin, BfArM) ignorieren**.

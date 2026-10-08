---
name: ki-risikoassessment-borghei
title: /ki-governance:ki-risikoassessment
description: Strukturierte KI-Risikobewertung pro KI-System – Identifikation, Risikoklassifizierung (KI-VO-Trigger + interner Risk-Score), Schadensanalyse (CIA, Fairness/Bias, Sicherheit, Rechtskonformität), Risk-Treatment und Wiedervorlage nach ISO/IEC 23894 und NIST AI RMF. Use when ein KI-System neu eingeführt, wesentlich geändert oder periodisch reassessiert werden soll.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/ki-governance/skills/ki-risikoassessment
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: regulatory
language: de
---

# /ki-governance:ki-risikoassessment

## Zweck

Der Skill liefert eine **strukturierte, auditierbare Risikobewertung** für ein konkretes KI-System – als Eingang in das interne KI-Asset-Register und als Entscheidungsgrundlage für Freigabe, Auflagen oder Ablehnung. Methodisch lehnt er sich an **ISO/IEC 23894:2023** (KI-Risikomanagement) und **NIST AI RMF 1.0** (Funktionen GOVERN / MAP / MEASURE / MANAGE) an; die **KI-VO-Risikoklassifizierung** wird als Pflicht-Trigger eingespeist, ohne den dortigen Pflichtenkatalog hier auszubuchstabieren (Querverweis auf `ki-vo-compliance`).

## Eingaben

- KI-System-Beschreibung: Zweck, Nutzergruppen, Datenkategorien, Modelltyp (Regel-/ML-/LLM-basiert), Lieferkette (Eigenentwicklung / Closed-Source-SaaS / Open-Source)
- Einsatzkontext: Rolle der Organisation (Anbieter / Betreiber / Einführer / Händler), Branche, Bezug zu besonders sensiblen Bereichen (Beschäftigung, Kreditwürdigkeit, Strafverfolgung, Gesundheit, Bildung)
- Datenfluss: Trainingsdaten, Input, Output, Speicherorte, Drittlandtransfer
- Bisherige Bewertungen (Vorabprüfungen, DSFA, Sicherheitsanalysen)

## Sub-Agent-Architektur

Researcher liefert KI-VO-Anker (Art. 5, 6, Anhang III; Art. 26 als Bezugspunkt), DSGVO-Anker (Art. 22, 25, 35), berufsrechtliche Belege und Standards (ISO/IEC 23894, NIST AI RMF, BSI AIC4). Drafter erstellt das Risk-Assessment-Dokument mit Risk-Register, Heatmap-Tabelle und Risk-Treatment-Plan. Reviewer prüft Vollständigkeit der KI-VO-Triggerprüfung, AVV-Abdeckung, DSFA-Auslöser und Wiedervorlage.

## Ablauf

### 1. Systemidentifikation (NIST AI RMF: MAP 1)

Pflichtfelder im Risk-Register:

| Feld | Inhalt |
|---|---|
| System-ID | Eindeutige Kennung im KI-Inventar |
| Zweck | Konkrete Aufgabe, Nutzergruppen |
| Modelltyp / Anbieter | Regel-/ML-/LLM-basiert; Eigen / SaaS / Open Source |
| Rolle der Organisation | Anbieter / Betreiber / Einführer / Händler iSv Art. 3 KI-VO |
| Datenkategorien | Personenbezug, besondere Kategorien Art. 9 DSGVO, Berufsgeheimnis § 203 StGB |
| Lieferkette | Trainingsdaten-Herkunft, Sub-Provider, Drittland |
| Lebenszyklusphase | Konzept / Pilot / Produktion / EOL |

### 2. Risikoklassifizierung – zwei Achsen

#### a) KI-VO-Risikoklasse (gesetzlicher Trigger)

Klassifikation entlang Art. 5, 6 und Anhang III KI-VO als **Pflichten-Trigger**, nicht als interne Risk-Score:

- **Verbotene Praxis** (Art. 5 KI-VO) → Einsatz untersagt
- **Hochrisiko-System** (Art. 6 KI-VO + Anhang III bzw. Anhang I) → Pflichtkaskade nach KI-VO
- **Begrenztes Risiko / Transparenzpflichten** (Art. 50 KI-VO) → Kennzeichnung
- **Minimales Risiko** → keine spezifischen KI-VO-Pflichten, aber Art. 4 KI-VO (Schulung) bleibt

> Detailprüfung der Pflichten: Skill `/ki-vo-compliance:hochrisiko-klassifizierung`. Hier nur die **Auslösung** dokumentieren.

#### b) Interner Risk-Score (ISO/IEC 23894-Logik)

Eigene Bewertungsmatrix entlang **Eintrittswahrscheinlichkeit × Schadenshöhe**, je 1–5. Schadensdimensionen:

- **Vertraulichkeit** (CIA): Geheimnisbruch, § 203 StGB, Geschäftsgeheimnisse
- **Integrität**: Manipulation der Outputs, Prompt-Injection, Datenvergiftung
- **Verfügbarkeit**: Ausfall, Anbieter-Lock-in, Modellabkündigung
- **Fairness / Bias**: Diskriminierung iSv AGG, mittelbare Benachteiligung
- **Sicherheit (Safety)**: physische / wirtschaftliche Schäden
- **Rechtskonformität**: KI-VO, DSGVO, Berufsrecht, Wettbewerbsrecht
- **Reputation**: Vertrauensschaden, Aufsichtsverfahren

### 3. Schadensszenarien und Bias-Analyse

Pro Szenario: Ursache → Ereignis → Schaden → Eintrittswahrscheinlichkeit → Schadenshöhe → Risk-Score. Fairness-Analyse nach Schutzkategorien (§ 1 AGG: Rasse, ethnische Herkunft, Geschlecht, Religion, Behinderung, Alter, sexuelle Identität); zusätzlich Schutz-Proxys (Postleitzahl, Name etc.).

### 4. Datenschutz-Trigger

- **DSFA-Pflicht** (Art. 35 DSGVO): DSK-Blacklist, Anhang III KI-VO als Indiz, automatisierte Entscheidung iSv Art. 22 DSGVO
- **AVV** (Art. 28 DSGVO) mit jedem externen Anbieter
- **Drittlandtransfer** (Art. 44 ff. DSGVO): Angemessenheitsbeschluss / SCC / TIA

### 5. Berufsrechts-Trigger (falls einschlägig)

- **§ 43e BRAO**: Auslagerung anwaltlicher Tätigkeiten – Schriftform, Verpflichtung zur Verschwiegenheit
- **§ 203 StGB**: Mitwirkende Personen (Abs. 4); ggf. ärztliche / steuerberatende / wirtschaftsprüfende Schweigepflicht

### 6. Risk-Treatment (ISO/IEC 23894, Kapitel 6)

Pro identifiziertem Risiko eine der vier Optionen:

| Option | Beispiel |
|---|---|
| **Vermeiden** | System nicht einsetzen, Alternative wählen |
| **Mitigieren** | TOMs, menschliche Aufsicht, Bias-Mitigation, Logging |
| **Übertragen** | Vertragliche Risikoallokation, Versicherung (KI-Haftpflicht) |
| **Akzeptieren** | Restrisiko dokumentieren, Freigabeentscheidung der Geschäftsleitung |

### 7. Wiedervorlage

Mindestens **jährlich**; bei Hochrisiko-Systemen iSd KI-VO **halbjährlich**; bei wesentlicher Änderung (Modellupdate, neue Datenquelle, neue Nutzergruppe) **sofort**.

## Quellen und Zitierweise

Verbindlich: [`../../../references/zitierweise.md`](../../../references/zitierweise.md).

### Unions- und nationales Recht

- [VO (EU) 2024/1689 (KI-VO)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R1689) – insb. Art. 3 (Begriffe), Art. 4 (Schulung), Art. 5 (verbotene Praktiken), Art. 6 + Anhang III (Hochrisiko), Art. 50 (Transparenz). **Pflichtenprüfung erfolgt im Plugin [`ki-vo-compliance`](../../../ki-vo-compliance/README.md).**
- [Art. 22 DSGVO](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0679#d1e2839-1-1) (automatisierte Entscheidung im Einzelfall)
- [Art. 25 DSGVO](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0679#d1e2992-1-1) (Datenschutz durch Technikgestaltung)
- [Art. 28 DSGVO](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0679#d1e3104-1-1) (Auftragsverarbeitung)
- [Art. 35 DSGVO](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0679#d1e3478-1-1) (DSFA)
- [§ 1 AGG](https://www.gesetze-im-internet.de/agg/__1.html)
- [§ 43e BRAO](https://www.gesetze-im-internet.de/brao/__43e.html) (Auslagerung)
- [§ 203 StGB](https://www.gesetze-im-internet.de/stgb/__203.html) (Schweigepflicht)

### Industrie-Standards

- **ISO/IEC 23894:2023** – Information technology — Artificial intelligence — Guidance on risk management ([iso.org](https://www.iso.org/standard/77304.html))
- **ISO/IEC 22989:2022** – AI concepts and terminology
- **ISO/IEC 42001:2023** – AI Management System (für Einbettung des Assessments)
- **NIST AI RMF 1.0** (Januar 2023) inkl. GenAI Profile (Juli 2024) – [nist.gov/itl/ai-risk-management-framework](https://www.nist.gov/itl/ai-risk-management-framework)
- **BSI AIC4** (Stand 2021) – Artificial Intelligence Cloud Service Compliance Criteria Catalogue

### Kommentare

- Keller, in: Keller/Kapoor, KI-VO, 1. Aufl. 2025, Art. 6 Rn. 1 ff. `[unverifiziert – prüfen]`
- Martini, in: Hartmann/Hilgendorf, KI-Recht, 2024, Kap. zu Risikoklassifizierung `[unverifiziert – prüfen]`
- Buchner/Petri, in: Kühling/Buchner, DSGVO/BDSG, 4. Aufl. 2024, Art. 22 Rn. 1 ff.
- Bertermann, in: Ehmann/Selmayr, DSGVO, 3. Aufl. 2024, Art. 35 Rn. 1 ff. `[unverifiziert – prüfen]`

### Rechtsprechung (`[unverifiziert – prüfen in Beck-Online / juris / curia.europa.eu]`)

1. EuGH, Urt. v. 07.12.2023 – C-634/21, ECLI:EU:C:2023:957 (SCHUFA / Scoring iSv Art. 22 DSGVO)
2. BAG zur Mitbestimmung bei IT-Systemen, § 87 I Nr. 6 BetrVG (Kammer- und Senatsentscheidungen, jeweils einzelfallbezogen)

## Ausgabeformat

```
KI-RISIKOASSESSMENT
System: <System-ID>  |  Stand: <Datum>  |  Assessor: <Rolle>

I. Systemidentifikation
   - Zweck / Nutzergruppen
   - Modelltyp / Anbieter / Lieferkette
   - Rolle der Organisation (Art. 3 KI-VO)
   - Datenkategorien (inkl. Art. 9 DSGVO / § 203 StGB)

II. Risikoklassifizierung
    a) KI-VO-Trigger: [verboten / Hochrisiko / begrenzt / minimal]
       → Pflichtprüfung in /ki-vo-compliance
    b) Interner Risk-Score (1–25 je Dimension)
       Vertraulichkeit / Integrität / Verfügbarkeit / Fairness /
       Sicherheit / Rechtskonformität / Reputation

III. Schadensszenarien
     <Tabelle: Ursache | Ereignis | Schaden | EW | SH | Score>

IV. Datenschutz-Trigger
    - DSFA-Pflicht Art. 35 DSGVO: ja/nein – Begründung
    - AVV Art. 28 DSGVO: vorhanden/fehlt
    - Drittlandtransfer: Mechanismus

V. Berufsrechts-Trigger (falls einschlägig)
    - § 43e BRAO / § 203 StGB / Spezialgesetz

VI. Risk-Treatment
    <Tabelle: Risiko | Option | Maßnahme | Verantwortlich | Frist>

VII. Restrisiko und Freigabeempfehlung
     🟢 / 🟡 / 🔴 mit Begründung

VIII. Wiedervorlage
      Datum: <jährlich / halbjährlich / ereignisbezogen>

IX. Quellenverzeichnis
```

## Risiken / typische Fehler

- **KI-VO-Pflichten inhaltlich doppeln** statt querzuverweisen – Pflege-Aufwand und Widersprüche.
- **Risk-Score ohne nachvollziehbare Skala** (5×5-Matrix dokumentieren).
- **Bias-Analyse auf § 1 AGG verkürzen** – Proxy-Variablen (z. B. Postleitzahl, Name) werden übersehen.
- **AVV vergessen**, weil das KI-Tool als „nur Software" wahrgenommen wird – LLM-as-a-Service ist idR Auftragsverarbeitung.
- **§ 43e BRAO / § 203 StGB nicht adressiert** bei anwaltlicher / ärztlicher Mandantin.
- **Wiedervorlage unbestimmt** ("nach Bedarf") – konkrete Frist setzen.
- **Standards als „Pflicht" framen**, obwohl sie freiwillig sind (Ausnahme: harmonisierte Normen Art. 40 KI-VO – Vermutungswirkung, nicht Verbindlichkeit).

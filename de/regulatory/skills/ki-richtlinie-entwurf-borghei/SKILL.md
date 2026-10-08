---
name: ki-richtlinie-entwurf-borghei
title: /ki-governance:ki-richtlinie-entwurf
description: Entwurf einer internen KI-Richtlinie / KI-Policy für Unternehmen und Kanzleien – Geltungsbereich, Grundsätze, verbotene Einsätze, Genehmigungsprozess, Rollen, Lieferantenmanagement (AVV Art. 28 DSGVO, § 43e BRAO), Schulung Art. 4 KI-VO, Vorfallsmanagement. Use when eine Organisation erstmals eine verbindliche KI-Richtlinie einführen oder eine bestehende Policy konsolidieren will.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/ki-governance/skills/ki-richtlinie-entwurf
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: regulatory
language: de
---

# /ki-governance:ki-richtlinie-entwurf

## Zweck

Der Skill liefert eine **verbindliche interne KI-Richtlinie** (Policy) und ihre Anlagen als Template – inklusive Geltungsbereich, ethischer und rechtlicher Leitplanken, Genehmigungsprozess, Rollen, Lieferantenmanagement, Schulungskonzept und Vorfallsmanagement. Die Richtlinie ist das organisatorische Dach eines KI-Management-Systems iSv **ISO/IEC 42001** (Kap. 5 Leadership, Kap. 6 Planning) und das Pendant zum gesetzlichen Pflichtensystem der KI-VO (Detail in `ki-vo-compliance`).

## Eingaben

- Organisationstyp (Unternehmen, Konzern, Kanzlei, Berufsgesellschaft) und Größe
- Sektorzugehörigkeit (Finanz, Gesundheit, Anwaltschaft, Steuerberatung, WP, öffentlicher Sektor)
- Bestehendes Managementsystem (ISMS nach ISO/IEC 27001, QMS, Compliance-Management)
- Vorhandene Tools (Microsoft Copilot, ChatGPT Enterprise, Google Gemini, sektor-spezifische Lösungen)
- Berufsrechtliche Bindungen (BRAO, BORA, MBO-Ä, StBerG, WPO)

## Sub-Agent-Architektur

Researcher liefert KI-VO-Anker (Art. 4, 5, 26, 50), DSGVO-Anker (Art. 5, 22, 28, 32, 35), berufsrechtliche Anker (§§ 43a, 43e BRAO, § 203 StGB), AGG, Standards (ISO/IEC 42001 Kap. 5–8) und Kommentarstellen. Drafter erstellt das Richtlinien-Template mit Klausel-Nummerierung, plus Anlagen (Rollenkatalog, Genehmigungs-Workflow, Lieferantencheckliste, Schulungsplan, Vorfallsformular). Reviewer prüft, ob Art. 4 KI-VO adressiert ist, AVV-Pflicht klar ist, § 43e BRAO bei anwaltlichen Mandantinnen integriert wurde und die Richtlinie KI-VO-Pflichten nicht doppelt.

## Ablauf

### 1. Geltungsbereich und Begriffe

- Räumlich (alle Standorte / Tochtergesellschaften)
- Personell (Mitarbeitende, Auszubildende, Praktikant:innen, externe Dienstleister, Mandantinnen?)
- Sachlich (alle KI-Systeme iSv Art. 3 Nr. 1 KI-VO; Generative KI; Embedded KI; agentische Systeme)
- Verweis auf KI-VO-Definitionen statt eigener; Kurzglossar als Anlage

### 2. Grundsätze

| Grundsatz | Inhalt |
|---|---|
| Rechtmäßigkeit | KI-VO, DSGVO, AGG, Berufsrecht, Spezialgesetze |
| Sicherheit | Vertraulichkeit, Integrität, Verfügbarkeit (ISMS-Kopplung) |
| Transparenz | Kennzeichnung KI-Output gegenüber Betroffenen (Art. 50 KI-VO als Anker) |
| Menschliche Aufsicht | keine ungeprüfte Automatisierung (Art. 14 KI-VO; Art. 22 DSGVO) |
| Fairness | Bias-Vermeidung; AGG-Schutzkategorien + Proxy-Variablen |
| Verantwortlichkeit | klare Rollen, dokumentierte Entscheidungen |
| Sparsamkeit | Datensparsamkeit Art. 5 I lit. c DSGVO; Umwelt-/Energieaspekt |

### 3. Verbotene Einsätze

- **Verbotene Praktiken iSv Art. 5 KI-VO** (Pflichtenprüfung in `ki-vo-compliance`)
- **Interne Tabus** (über Gesetz hinaus): z. B. keine Bewertung von Mitarbeitenden allein durch KI; keine Mandanteneingaben in nicht-kanzleifreigegebene Tools; kein Output ohne menschliche Freigabe in Mandantenkommunikation

### 4. Genehmigungsprozess (Pre-Use-Check)

Schwellenwert-Modell:

1. **Triage** (jede Anwender:in): Risiko-Schnellcheck (Datenkategorien, Anbieter, Einsatzkontext)
2. **Pre-Use-Approval** durch AI-Owner bei: personenbezogenen Daten, Mandantendaten, externen Anbietern, neuen Einsatzfeldern
3. **Risikoassessment** (Skill `/ki-governance:ki-risikoassessment`) bei: KI-VO-Hochrisiko-Indiz, Art. 22 DSGVO-Konstellation, Drittlandtransfer, Berufsgeheimnis
4. **Geschäftsleitungs-Freigabe** bei: roter Risikoeinstufung, neuen Systemkategorien, Vertragsabschluss > Schwelle X EUR

### 5. Rollen und Verantwortlichkeiten

| Rolle | Aufgaben |
|---|---|
| **AI-Owner** (organisationsweit) | Strategische Verantwortung, KI-Inventar, Reporting an Geschäftsleitung |
| **AI-Verantwortliche/r** (pro System) | Risiko, Monitoring, Lieferant, Vorfallsmanagement |
| **Risk-Owner** | Risk-Treatment-Entscheidungen, Restrisiko-Akzeptanz |
| **Modellverantwortliche/r** | Technische Modellgüte, Drift, Fairness, Audits |
| **Datenschutzbeauftragte/r** | DSFA, Betroffenenrechte, AVV-Begleitung |
| **IT-Sicherheitsbeauftragte/r** | TOMs, ISMS-Kopplung |
| **Compliance / Berufsrechts-Verantwortliche/r** | Berufsrecht, Werbeverbot, Schweigepflicht |
| **Personalverantwortliche/r** | Schulungsplan Art. 4 KI-VO, Beschäftigtendatenschutz |

### 6. Lieferantenmanagement

Pflichtprüfungen vor Vertragsabschluss:

- **AVV Art. 28 DSGVO** mit Mindestinhalten (Weisungsbindung, TOM, Sub-Processor-Liste, Audit-Recht, Löschung am Ende)
- **Drittlandtransfer** Art. 44 ff. DSGVO (Angemessenheitsbeschluss / SCC / Transfer Impact Assessment)
- **Anbieter-Rolle nach KI-VO** (Anbieter / Bevollmächtigter / Einführer / Händler) und vertragliche Pflichtenkaskade
- **Berufsrecht**: § 43e BRAO (Auslagerung anwaltlicher Tätigkeiten), § 203 Abs. 4 StGB (Verpflichtung der mitwirkenden Personen); Pendant für Ärzte, StB, WP
- **Sicherheits-/Audit-Nachweise**: BSI AIC4-Selbstauskunft, SOC 2 Type II, ISO/IEC 27001, ISO/IEC 42001 (sobald Zertifizierungslandschaft tragfähig)

### 7. Schulung (Art. 4 KI-VO)

- **Pflichtanker**: Art. 4 KI-VO (seit 02.02.2025 anwendbar) – Personal muss „hinreichende KI-Kompetenz" haben
- **Zielgruppen**: alle Anwender:innen (Basisschulung); AI-Owner und Modellverantwortliche (vertieft); Geschäftsleitung (strategisch)
- **Inhalte**: KI-Grundlagen, Grenzen (Halluzination, Bias), interne Richtlinie, Datenschutz, Berufsrecht, Vorfallsmeldung
- **Nachweis**: Teilnahmedokumentation, Wiederholung mindestens jährlich

### 8. Vorfallsmanagement

- **Meldepfad** intern (über AI-Verantwortliche/r → AI-Owner → ggf. Geschäftsleitung)
- **Eskalation extern**: DSGVO-Verletzungen (Art. 33, 34 DSGVO), schwere Vorfälle iSv Art. 3 Nr. 49 / Art. 73 KI-VO – Detail in `ki-vo-compliance` und `datenschutzrecht`
- **Whistleblower-Schutz** nach HinSchG für Hinweise auf Verstöße gegen die Richtlinie

### 9. Sanktionen, Kontaktstelle, Inkrafttreten

- Arbeitsrechtliche Folgen bei Verstoß (Hinweis: Mitbestimmung § 87 I Nr. 1 / Nr. 6 BetrVG bei Einführung)
- Kontaktstelle (anonym oder offen) für Fragen und Hinweise
- Inkrafttreten, Änderungshistorie, Reviewer, Wiedervorlage

## Quellen und Zitierweise

Verbindlich: [`../../../references/zitierweise.md`](../../../references/zitierweise.md).

### Unions- und nationales Recht

- [VO (EU) 2024/1689 (KI-VO)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R1689) – insb. Art. 3 Nr. 1, Art. 4 (Schulung), Art. 5, Art. 26 (Betreiberpflichten), Art. 50 (Transparenz). Detaillierte Pflichtenkaskade in [`ki-vo-compliance`](../../../ki-vo-compliance/README.md).
- [Art. 5 DSGVO](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0679#d1e1888-1-1) (Grundsätze)
- [Art. 22 DSGVO](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0679#d1e2839-1-1)
- [Art. 28 DSGVO](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0679#d1e3104-1-1)
- [Art. 32 DSGVO](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0679#d1e3338-1-1)
- [Art. 35 DSGVO](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0679#d1e3478-1-1)
- [§ 1 AGG](https://www.gesetze-im-internet.de/agg/__1.html)
- [§ 43a BRAO](https://www.gesetze-im-internet.de/brao/__43a.html) (Verschwiegenheit)
- [§ 43e BRAO](https://www.gesetze-im-internet.de/brao/__43e.html) (Auslagerung)
- [§ 203 StGB](https://www.gesetze-im-internet.de/stgb/__203.html)
- [§ 87 BetrVG](https://www.gesetze-im-internet.de/betrvg/__87.html) (Mitbestimmung)
- [HinSchG](https://www.gesetze-im-internet.de/hinschg/) (Hinweisgeberschutz)

### Industrie-Standards

- **ISO/IEC 42001:2023** – AI Management System, Kap. 5 (Leadership), Kap. 6 (Planning), Kap. 7 (Support), Kap. 8 (Operation)
- **ISO/IEC 23894:2023** – AI Risk Management
- **ISO/IEC 22989:2022** – AI Concepts and Terminology
- **NIST AI RMF 1.0** (01/2023) – Funktion GOVERN
- **BSI AIC4** – Anforderungsgruppen zu Governance und Lieferantenmanagement

### Kommentare

- Henssler, in: Henssler/Prütting, BRAO, 6. Aufl. 2023, § 43e Rn. 1 ff. `[unverifiziert – prüfen]`
- Cierniak/Niehaus, in: MüKoStGB, 4. Aufl. 2022, § 203 Rn. 1 ff. `[unverifiziert – prüfen]`
- Hartung, in: Hartung/Schons/Enders, BRAO, 6. Aufl. 2022, § 43e Rn. 1 ff. `[unverifiziert – prüfen]`
- Kapoor, in: Keller/Kapoor, KI-VO, 1. Aufl. 2025, Art. 4 Rn. 1 ff. `[unverifiziert – prüfen]`
- Bertermann, in: Ehmann/Selmayr, DSGVO, 3. Aufl. 2024, Art. 28 Rn. 1 ff. `[unverifiziert – prüfen]`

### Rechtsprechung (`[unverifiziert – prüfen in Beck-Online / juris / curia.europa.eu]`)

1. EuGH, Urt. v. 07.12.2023 – C-634/21, ECLI:EU:C:2023:957 (SCHUFA, Art. 22 DSGVO)
2. BAG zur Mitbestimmung bei Einführung technischer Einrichtungen, § 87 I Nr. 6 BetrVG (Senatslinie)
3. BGH zu § 203 StGB und externen Dienstleistern (Senatslinie zur Schweigepflicht)

## Ausgabeformat

```
KI-RICHTLINIE
<Organisation> | Version: <X.Y> | Inkrafttreten: <Datum>

§ 1 Geltungsbereich (räumlich, personell, sachlich)
§ 2 Begriffe (Verweis auf KI-VO Art. 3)
§ 3 Grundsätze
§ 4 Verbotene Einsätze
   (Art. 5 KI-VO + interne Tabus)
§ 5 Genehmigungsprozess
   (Triage → Pre-Use-Approval → Risikoassessment → Geschäftsleitung)
§ 6 Rollen und Verantwortlichkeiten
§ 7 Lieferantenmanagement
   (AVV Art. 28 DSGVO; § 43e BRAO; Drittland; BSI AIC4)
§ 8 Schulung (Art. 4 KI-VO)
§ 9 Vorfallsmanagement
§ 10 Sanktionen und Kontaktstelle
§ 11 Inkrafttreten, Wiedervorlage, Änderungshistorie

Anlagen:
  A. Rollenkatalog
  B. Genehmigungs-Workflow (Flowchart-Text)
  C. Lieferantencheckliste
  D. Schulungsplan
  E. Vorfallsformular
  F. Glossar
```

## Risiken / typische Fehler

- **KI-VO-Pflichten in die Richtlinie kopieren** – Pflege-Aufwand und Inkonsistenz; stattdessen Querverweis auf `ki-vo-compliance`.
- **Schulung Art. 4 KI-VO als „nice to have"** – seit 02.02.2025 anwendbar, in Richtlinie verankern.
- **AVV-Pflicht nur für „klassische" Dienstleister** – LLM-as-a-Service idR Auftragsverarbeitung.
- **§ 43e BRAO / § 203 StGB nicht adressiert** bei Berufsgeheimnisträgern; mitwirkende Personen-Verpflichtung fehlt.
- **Mitbestimmungspflicht § 87 I Nr. 6 BetrVG** beim Einführen technischer Überwachungseinrichtungen übersehen.
- **Verbotsklauseln zu weich** („sollte vermieden werden") – Warn- und Sanktionsfunktion verfehlt.
- **Keine Wiedervorlagepflicht** der Richtlinie selbst (mindestens jährlich + bei wesentlichen Rechtsänderungen).

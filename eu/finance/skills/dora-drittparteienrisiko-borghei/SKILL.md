---
name: dora-drittparteienrisiko-borghei
title: /dora:dora-drittparteienrisiko
description: Management des IKT-Drittparteienrisikos nach DORA – allgemeine Prinzipien und Informationsregister Art. 28 DORA, wesentliche Vertragsbestimmungen Art. 30 DORA, Behandlung kritischer IKT-Drittdienstleister im Überwachungsrahmen. Use when ein Finanzunternehmen eine IKT-Auslagerung bewertet, das Informationsregister aufbaut oder Verträge DORA-fest gestaltet.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/dora/skills/dora-drittparteienrisiko
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: finance
language: de
---

# /dora:dora-drittparteienrisiko

## Zweck

DORA macht das **IKT-Drittparteienrisiko** zur eigenständigen Steuerungsaufgabe: Auslagerungen an IKT-Dienstleister dürfen die operationale Resilienz nicht aushöhlen. Bestehende Auslagerungsverträge sind selten DORA-konform — es fehlen Audit-Rechte, Ausstiegsstrategien und Subunternehmer-Regelungen. Dieser Skill baut das Informationsregister auf, prüft die Vertragsmindestinhalte und ordnet kritische Funktionen ein.

## Eingaben

- Liste aller IKT-Drittdienstleister und der bezogenen Leistungen
- Zuordnung: unterstützt der Dienst eine **kritische oder wichtige Funktion**?
- Bestehende Vertragsunterlagen (Audit-Rechte, SLA, Kündigung, Subunternehmer)
- Standort der Leistungserbringung / Datenverarbeitung (Drittland?)
- Konzentration: mehrere kritische Funktionen bei einem Anbieter?
- Vorhandene Ausstiegsstrategien

## Sub-Agent-Architektur

Drei gedankliche Rollen. Ein **Register-Agent** baut und pflegt das Informationsregister nach Art. 28 DORA (alle Vereinbarungen, Funktionskritikalität, Subunternehmerketten) für das aufsichtliche Reporting. Ein **Vertrags-Agent** gleicht jeden Vertrag mit den Mindestinhalten des Art. 30 DORA ab und markiert Lücken (Audit-Rechte, Ausstiegsstrategie, Standort, Datenschutz). Ein **Risiko-Agent** bewertet Vorab-Due-Diligence, Konzentrationsrisiko und ordnet ein, ob der Anbieter Kandidat für den unionsweiten Überwachungsrahmen kritischer IKT-Drittdienstleister ist. Freigabe und Vertragsverhandlung bleiben beim Menschen.

## Ablauf

### 1. Allgemeine Prinzipien und Informationsregister (Art. 28 DORA)

- IKT-Drittparteienrisiko ist integraler Teil des IKT-Risikomanagement-Rahmens.
- **Informationsregister** aller vertraglichen Vereinbarungen — getrennt nach Funktionen, die kritische oder wichtige Funktionen stützen.
- Vorab-**Due-Diligence**, Bewertung des **Konzentrationsrisikos**, dokumentierte **Ausstiegsstrategie** für kritische Funktionen.
- Meldung neuer Vereinbarungen über kritische Funktionen an die zuständige Behörde.

### 2. Wesentliche Vertragsbestimmungen (Art. 30 DORA)

Mindestinhalte für **alle** IKT-Verträge (Art. 30 Abs. 2 DORA): Leistungsbeschreibung, Standort der Datenverarbeitung, Datenschutz/-sicherheit, Zugang/Wiederherstellung bei Insolvenz, Kooperation mit Aufsicht, Kündigungsrechte.

Zusätzliche Inhalte für **kritische oder wichtige Funktionen** (Art. 30 Abs. 3 DORA):

| Pflichtinhalt | Inhalt |
|---|---|
| Service-Level | vollständige SLA mit Zielwerten |
| Business Continuity | Notfall- und Wiederanlaufpläne des Anbieters |
| Audit-Rechte | uneingeschränkte Prüf- und Zugangsrechte |
| Ausstiegsstrategie | geordneter Exit ohne Geschäftsunterbrechung |
| Subunternehmer | Bedingungen für Weiterverlagerung |

### 3. Kritische IKT-Drittdienstleister / Überwachungsrahmen

- Die ESA benennen **kritische IKT-Drittdienstleister**; diese unterliegen einem direkten unionsweiten **Überwachungsrahmen** (federführender Überwacher, Empfehlungen).
- Finanzunternehmen bleiben für ihre Auslagerung verantwortlich, auch wenn der Anbieter überwacht wird.

### 4. Verzahnung

- Register und Vertragslücken fließen in die Gap-Analyse des IKT-Rahmens und die Resilienztests (TLPT-Scope) zurück.

## Risiken / typische Fehler

- **Informationsregister** unvollständig — es muss **alle** IKT-Vereinbarungen erfassen, nicht nur die kritischen; lückenhafte Register sind ein häufiger Prüfbefund.
- **Ausstiegsstrategie** fehlt — für kritische Funktionen ist ein dokumentierter, geordneter Exit zwingend.
- **Konzentrationsrisiko** ignoriert — mehrere kritische Funktionen bei einem Anbieter (z. B. ein Hyperscaler) erhöhen das Systemrisiko.
- **Vertragsmindestinhalte** des Art. 30 DORA nicht nachgezogen — Altverträge ohne Audit-Rechte und Subunternehmer-Klauseln sind nicht DORA-konform.

## Quellen

### Statute

- [VO (EU) 2022/2554 (DORA)](https://eur-lex.europa.eu/eli/reg/2022/2554/oj) — Art. 28 DORA, Art. 30 DORA, Art. 31–44 (Überwachungsrahmen)
- ITS zum Informationsregister (Durchführungsverordnung der ESA)
- [BaFin — Mindestvertragsinhalte DORA](https://www.bafin.de/DE/unternehmen-maerkte/aufsicht/alle-unternehmen/dora/ueberblick/ueberblick_node.html)

### Sekundärliteratur

- Maume/Maute/Fromberger, DORA-Kommentar
- Gleiss Lutz, „DORA — ICT risk compliance obligations"

## Ausgabeformat

```
DORA-DRITTPARTEIENRISIKO — <Mandant> — <Datum>

I.    Informationsregister (Art. 28 DORA)   [vollständig / Lücken]
      kritische/wichtige Funktion?           je Anbieter [Ja/Nein]
II.   Due-Diligence / Konzentrationsrisiko   [bewertet / offen]
III.  Vertragsprüfung (Art. 30 DORA)
      Mindestinhalte Abs. 2                  [erfüllt / Gap-Liste]
      Zusatzinhalte Abs. 3 (krit. Funktion)  [Audit-Rechte / Ausstiegsstrategie / SLA]
IV.   Überwachungsrahmen                      [kritischer IKT-Drittdienstleister? Ja/Nein]
V.    Ausstiegsstrategie                       [dokumentiert / fehlt]

Nachbesserungsbedarf:
  Vertrag <Anbieter>: <fehlende Klauseln>
Nächster Schritt: <…>
```

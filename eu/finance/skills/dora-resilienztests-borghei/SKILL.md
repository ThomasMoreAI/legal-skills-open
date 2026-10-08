---
name: dora-resilienztests-borghei
title: /dora:dora-resilienztests
description: Aufbau eines DORA-Programms für Tests der digitalen operationalen Resilienz – allgemeine Testanforderungen Art. 24 DORA, Testmethoden Art. 25 DORA, bedrohungsorientierte Penetrationstests (TLPT) Art. 26 DORA, Anforderungen an Tester Art. 27 DORA. Use when ein Finanzunternehmen sein Testprogramm aufsetzt oder klärt, ob es zur TLPT verpflichtet ist.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/dora/skills/dora-resilienztests
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: finance
language: de
---

# /dora:dora-resilienztests

## Zweck

DORA verlangt ein **risikobasiertes, dokumentiertes Testprogramm** als integralen Bestandteil des IKT-Risikomanagements. Nicht jedes Finanzunternehmen muss bedrohungsorientierte Penetrationstests (TLPT) durchführen — diese treffen nur **bedeutende** Unternehmen, die von der zuständigen Behörde benannt werden. Dieser Skill trennt die allgemeine Testpflicht von der TLPT-Pflicht und liefert den Testkalender.

## Eingaben

- Art und Größenklasse des Finanzunternehmens (Mikrounternehmen nach Art. 16 ausgenommen?)
- Systemische Bedeutung / Marktstellung (Kandidat für TLPT-Benennung?)
- Inventar kritischer oder wichtiger Funktionen
- Letzte durchgeführte Tests (Datum, Methode, Befunde)
- Eingesetzte IKT-Drittdienstleister im TLPT-Scope
- Interne vs. externe Testkapazität

## Sub-Agent-Architektur

Drei gedankliche Rollen. Ein **Scoping-Agent** bestimmt, welche Systeme und Funktionen in das jährliche Testprogramm gehören und ob das Unternehmen als bedeutend für eine TLPT-Benennung in Betracht kommt. Ein **Methoden-Agent** ordnet jeder Funktion die passende Testmethode nach Art. 25 DORA zu (Schwachstellenbewertung, Quellcode-Review, szenariobasierte Tests etc.). Ein **TLPT-Agent** prüft die Sonderanforderungen des Art. 26/27 DORA (Live-Produktionssystem, Roter/Blauer Team, Tester-Akkreditierung, Dreijahreszyklus). Die Rollen erzeugen gemeinsam einen Testkalender; die Freigabe liegt beim Leitungsorgan.

## Ablauf

### 1. Allgemeine Anforderungen (Art. 24 DORA)

- Finanzunternehmen (außer Mikrounternehmen) errichten ein **umfassendes Testprogramm**.
- Risikobasiert, mindestens **jährlich** für IKT-Systeme, die kritische oder wichtige Funktionen tragen.
- Unabhängigkeit der Tester (intern/extern), Behebung festgestellter Schwachstellen nach Priorität.

### 2. Testmethoden (Art. 25 DORA)

Das Programm umfasst je nach Risiko u. a.:

- **Schwachstellenbewertung** und -scans, Open-Source-Analysen
- Netzwerksicherheitsbewertungen, Gap-Analysen
- Quellcode-Überprüfung (soweit machbar), szenariobasierte Tests
- Kompatibilitäts-, Leistungs- und End-to-End-Tests
- **Penetrationstest**

### 3. TLPT-Pflicht (Art. 26 DORA)

- Nur **bedeutende** Finanzunternehmen, die von der zuständigen Behörde benannt werden, führen TLPT durch.
- Turnus: mindestens alle **drei Jahre** (Dreijahreszyklus), risikobasiert anpassbar.
- TLPT deckt mehrere kritische oder wichtige Funktionen ab und wird auf dem **Live-Produktionssystem** durchgeführt.
- Einbezug relevanter IKT-Drittdienstleister; Pooled Testing möglich.

### 4. Anforderungen an Tester (Art. 27 DORA)

- Externe Tester benötigen Eignung, Reputation und **Tester-Akkreditierung** bzw. Zertifizierung.
- Interne Tester nur unter strengen Voraussetzungen und behördlicher Genehmigung.
- Abdeckung durch Berufshaftpflicht; Trennung Red Team / Blue Team.

### 5. Verzahnung

- TLPT-Befunde fließen in den IKT-Risikomanagement-Rahmen (Art. 6 DORA) und das Drittparteienmanagement zurück.
- TIBER-DE dient als Referenzrahmen für die deutsche TLPT-Durchführung.

## Risiken / typische Fehler

- **TLPT-Pflicht** vorschnell angenommen oder verneint — sie gilt nur für von der Behörde benannte bedeutende Unternehmen, nicht für jedes Institut.
- **Live-Produktionssystem** unzureichend abgesichert — TLPT läuft auf produktiven Systemen, Risikoabsicherung und Notfallplan sind zwingend.
- **Tester-Akkreditierung** missachtet — nicht akkreditierte Tester führen zur Unverwertbarkeit des TLPT.
- **Dreijahreszyklus** versäumt — der Turnus ist hart; eine versäumte Runde ist aufsichtsrechtlich relevant.

## Quellen

### Statute

- [VO (EU) 2022/2554 (DORA)](https://eur-lex.europa.eu/eli/reg/2022/2554/oj) — Art. 24 DORA, Art. 25 DORA, Art. 26 DORA, Art. 27 DORA
- RTS zu TLPT (gemeinsame technische Regulierungsstandards der ESA)
- BaFin / Bundesbank: TIBER-DE-Rahmenwerk

### Sekundärliteratur

- Maume/Maute/Fromberger, DORA-Kommentar
- Noerr, „Hacken nach Verordnung — Bedrohungsbasierte Penetrationstests nach DORA"

## Ausgabeformat

```
DORA-RESILIENZTESTS — <Mandant> — <Datum>

I.    Geltung Testprogramm (Art. 24 DORA)  [Ja — Nicht-Mikrounternehmen]
II.   Testmethoden (Art. 25 DORA)
      Schwachstellenbewertung               [geplant / durchgeführt]
      Penetrationstest                       [geplant / durchgeführt]
      szenariobasierte Tests                 [geplant / durchgeführt]
III.  TLPT-Pflicht (Art. 26 DORA)            [bedeutend benannt? Ja / Nein]
      Letzter / nächster TLPT                <Datum>  Turnus: 3 Jahre
      Live-Produktionssystem-Absicherung     [vorhanden / offen]
IV.   Tester (Art. 27 DORA)                  [Akkreditierung vorhanden? Ja / Nein]
V.    Befundverwertung                       [in IKT-Rahmen rückgeführt]

Testkalender:
  Q1: <…>   Q3: <…>
Nächster Schritt: <…>
```

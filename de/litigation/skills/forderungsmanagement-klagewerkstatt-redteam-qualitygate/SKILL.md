---
name: forderungsmanagement-klagewerkstatt-redteam-qualitygate
title: Redteam Qualitygate
description: 'Für Redteam Qualitygate: prüft Ergebnis, Beweislast und Gegenposition; Ergebnis: Gegenprüfung mit Beweis- und Fristencheck. Fachgebiet: Forderungsmanagement — Klagewerkstatt.'
author: Klotzkette
author_url: https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/forderungsmanagement-klagewerkstatt/skills/redteam-qualitygate
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: litigation
language: de
---

# Redteam Qualitygate

Vor Einreichung ein Prüfgang aus Sicht der Beklagten.

## Prüfraster

| Bereich | Fragen aus Beklagten-Sicht |
|---|---|
| Aktivlegitimation | Ist Klägerin Inhaberin der Forderung Tritt eine Abtretung dazwischen |
| Passivlegitimation | Stimmt der Beklagte mit dem Vertragspartner ueberein |
| Anspruchsgrund | Welche Tatsachen sind unstreitig welche streitig |
| Faelligkeit | Bestreite ich die Faelligkeit mit Erfolg |
| Verzug | Wurde die Mahnung tatsaechlich zugestellt |
| Verjährung | Kann ich die Einrede der Verjährung erheben |
| Aufrechnung | Habe ich Gegenforderungen |
| Erfuellung | Kann ich Teilzahlung nachweisen |
| Form Beleg | Welche Anlage fehlt oder ist unleserlich |
| Substantiierung | Welche Tatsache ist nur pauschal vorgetragen |

## Schwachstellen-Liste

| Schwachstelle | Konsequenz |
|---|---|
| Anlagen nicht klar nummeriert | Bezug unklar |
| Zinsbeginn ohne Mahnungsdatum | Zinsanspruch streitig |
| Pauschal-Behauptung ohne Datum | Substantiierungsruege |
| Vollmacht fehlt oder veraltet | Zurueckweisung ZPO 88 |
| Streitwert hoeher als notwendig | unnoetige Kosten |
| AGB-Klausel zur Faelligkeit nicht geprueft BGB 305 ff | Klausel unwirksam |

## Verspaetungspraeklusion

Später Vortrag kann nach ZPO 296 zurueckgewiesen werden. Beklagte versucht oft Verzoegerungstaktik. Kläger sollte Beweise mit Klage einreichen.

## Norm-Pinpoints

- ZPO 88 130d 138 296
- BGB 305 ff
- BGB 387 ff Aufrechnung

## Quellen

- [ZPO 296](https://www.gesetze-im-internet.de/zpo/__296.html)
- [ZPO 138](https://www.gesetze-im-internet.de/zpo/__138.html)

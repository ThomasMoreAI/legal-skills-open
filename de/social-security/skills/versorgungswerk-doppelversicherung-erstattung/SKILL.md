---
name: versorgungswerk-doppelversicherung-erstattung
title: Doppelversicherung und Beitragserstattung
description: 'Für Doppelversicherung und Beitragserstattung: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt.'
author: Klotzkette
author_url: https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/rentenpruefer/skills/versorgungswerk-doppelversicherung-erstattung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: social-security
language: de
---

# Doppelversicherung und Beitragserstattung

Nutze diesen Skill, wenn parallel Beiträge an DRV und Versorgungswerk geflossen sind oder ein Arbeitgeber falsch gemeldet hat.

## Sofortbild

1. Zeitraum monatsgenau erfassen.
2. Beitragsadressaten trennen: DRV, Versorgungswerk, Arbeitgeber, Arbeitnehmer.
3. Rechtsgrund des Beitrags prüfen: Versicherungspflicht, Befreiung, Nachversicherung, freiwilliger Beitrag, Fehlmeldung.
4. Korrekturweg wählen: Arbeitgebermeldung, DRV-Konto, Versorgungswerkbuchung, Erstattungsantrag.
5. Verjährung, Bestandskraft und Nachweisrisiko markieren.

## Matrix

| Monat | Arbeitgebermeldung | DRV-Beitrag | Versorgungswerk | Status | Korrektur |
| --- | --- | --- | --- | --- | --- |
| offen | offen | offen | offen | ungeklärt | Nachweis anfordern |

## Output

Liefer eine Beitragsfluss-Tabelle und ein erstes Korrekturschreiben. Bei Unsicherheit nicht vorschnell Erstattung verlangen, sondern zuerst klären, ob der Beitrag rentensteigernd gebraucht wird.

## Anker

- SGB VI zu Pflichtversicherung, Befreiung, Nachversicherung und Erstattung.
- Arbeitgebermeldungen sind Beweisquelle, aber keine rechtliche Entscheidung.

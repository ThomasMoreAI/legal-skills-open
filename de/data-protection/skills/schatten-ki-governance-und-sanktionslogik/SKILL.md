---
name: schatten-ki-governance-und-sanktionslogik
title: Schatten-KI-Governance und Sanktionslogik
description: 'Für Schatten-digitale Werkzeuge-Governance und Sanktionslogik: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt.'
author: Klotzkette
author_url: https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/berufsrecht-ki-vertragspruefung/skills/schatten-ki-governance-und-sanktionslogik
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: data-protection
language: de
---

# Schatten-KI-Governance und Sanktionslogik

## Problem

Eine Kanzlei kann einen vorbildlichen Anbieter prüfen und trotzdem scheitern, wenn Mitarbeiter daneben private Tools nutzen. Berufsrechtlich zählt die tatsächliche Organisation, nicht die PowerPoint-Policy.

## Arbeitsmodus

Erstelle zuerst eine Toolkarte:

- freigegebene Tools
- geduldete Tools ohne Mandatsdaten
- verbotene Tools
- unbekannte Tools aus Logs, Browserhistorie, Spesen, Screenshots oder Teamumfragen

## Governance

| Element | Minimum | Gute Praxis |
|---|---|---|
| Freigabe | zentrale Toolliste | Freigabe mit Datenklassen und Beispielprompts |
| Schulung | KI-Kompetenz-Grundlagen | kurze Fallübungen zu Uploadfehlern, Halluzinationen, Geheimnissen |
| Technik | Hinweise und Sperren | SSO, DLP, CASB, sichere Alternativen |
| Kontrolle | Stichproben | Toolreview quartalsweise, Incident Lessons Learned |
| Sanktion | arbeitsrechtliche Eskalation | verhältnismäßig: Hinweis, Nachschulung, Abmahnung, Entzug Zugriff |

## Incident Response

Bei versehentlichem Upload:

1. Sofort Tool, Account, Dokument, Zeitpunkt, Datenklasse erfassen.
2. Anbieter-Löschpfad und Supportticket starten.
3. Berufsrecht, Datenschutz, Mandatsverantwortliche informieren.
4. Prüfen, ob Mandant, Kammer, Datenschutzaufsicht oder Versicherung einzubeziehen sind.
5. Wiederholungsschutz: Policy, Technik, Schulung nachziehen.

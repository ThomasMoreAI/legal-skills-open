---
name: unterschriftspruefung
title: Unterschriftspruefung
description: 'Für Unterschriftsprüfung: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Tatbestands- oder Anspruchsmatrix.'
author: Klotzkette
author_url: https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/status-navigator-step-plan/skills/unterschriftspruefung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: general
language: de
---

# Unterschriftspruefung

## Rolle und Fokus
Prüft, soweit aus den Dokumenten ersichtlich, ob die erforderlichen Parteien unterschrieben haben. Markiert fehlende Unterschriften, unklare Unterzeichner, Vertretungsfragen. Keine Wirksamkeitspruefung.

## Anwendungsbeispiel
LausitzStorage Unterschriftsbefunde: 1. Nachtrag Pachtvertrag LEAG nur von Prokuristin Kosturek unterzeichnet — laut HR-Auszug 18.03.2026 hat sie Gesamtprokura mit GF erforderlich, also schwebend unwirksam nach § 177 BGB Analogie. 2. Nachtrag von GF Vansel allein — laut Satzung nur Gesamtvertretung. Wandeldarlehen NordCap § 4 verweist auf Beschluss der nicht existiert.

## Output-Module
- Unterschrifts-Befundliste mit Klasse (vollstaendig/fragwuerdig/Entwurf/unleserlich)
- Vertretungsanalyse je Partei (HR-Stand zum Unterzeichnungszeitpunkt)
- Querverweis an `dokumententyp-beschluesse` wenn Beschlussbezug betroffen

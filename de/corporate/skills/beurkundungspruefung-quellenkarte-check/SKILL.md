---
name: beurkundungspruefung-quellenkarte-check
title: Beurkundungspruefung Quellenkarte Check
description: 'Für Beurkundungsprüfung Quellenkarte Check: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Schnittstellenkarte mit Zuständigkeits- und Nachweisfragen.'
author: Klotzkette
author_url: https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/wandeldarlehen-lebenszyklus/skills/beurkundungspruefung-quellenkarte-check
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: corporate
language: de
sources:
- title: Quellenhygiene
  path: references/quellenhygiene.md
- title: Zitierweise
  path: references/zitierweise.md
---

# Beurkundungspruefung Quellenkarte Check

## Einsatzlage

Diese Quellenkarte sichert im Bereich **Wandeldarlehen Lebenszyklus** tragende Normen, Rechtsprechung, Behördenpraxis, Register, Formulare und aktuelle Leitlinien ab.

## Suchraster

- `bilingual-einsprachig`
- `cap-table-darlehenshoehe-konditionen`
- `dokumenten-upload-formfehler-heilungs`
- `einsprachige-vertragsfassung-vertragserstellung`
- `gesellschafterbeschluss-kapitalerhoehung-vorbereiten`
- `gesellschafterliste-aktualisieren-gesellschafterversammlung`
- `gmbh-vollstaendigen`
- `handelsregisteranmeldung-kapitalerhoehung-kyc-aml`
- `lebenszyklus-bilinguale-vertragserstellung`
- `mandat-triage-mehrere-parallel`
- `notar-paket-parteien-erfassen`
- `post-eintragung-rangruecktritt-formulieren`

## Prüfroute

1. Normenstand über amtliche oder frei zugängliche Primärquellen sichern.
2. Rechtsprechung nach passendem Gericht, Datum, Aktenzeichen und Entscheidungsform suchen.
3. Behördenpraxis, Formulare, Verwaltungshinweise und Register nur mit Quellenstand ausgeben.
4. Ergebnis als Quellenmatrix dokumentieren: Aussage, Quelle, Stand, Tragweite, Unsicherheit.

## Fehlerbremse

- Keine BeckRS- oder juris-Blindzitate aus Modellwissen.
- Keine Literaturfundstellen behaupten, die nicht aus Nutzerquelle oder frei prüfbarer Quelle stammen.
- Bei dynamischen Materien immer sagen, ob der Stand live geprüft wurde.
- Quellenhygiene: `references/quellenhygiene.md`; Zitierweise: `references/zitierweise.md`.

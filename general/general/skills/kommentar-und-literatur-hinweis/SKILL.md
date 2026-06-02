---
name: kommentar-und-literatur-hinweis
title: Quellenhinweis ohne Blindzitate
description: Quellenhinweis für vertiefte Subsumtion. Gibt keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen aus. Markiert, welche Normen vertieft in Literatur oder Datenbanken zu prüfen sind, und fordert Nutzerquellen oder lizenzierten Live-Zugriff an.
author: Klotzkette
author_url: https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/subsumtions-pruefer/skills/kommentar-und-literatur-hinweis
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: de
---

# Quellenhinweis ohne Blindzitate

## Zweck

Dieser Skill ersetzt frühere Literatur-Empfehlungslisten. Er sagt nicht "zitiere Kommentar X Rn. Y", sondern baut eine saubere Recherche- und Prüfspur.

## Arbeitsweise

1. Nenne die entscheidenden Normen und Tatbestandsmerkmale.
2. Nenne, welche Punkte rechtsprechungs- oder literaturbedürftig sind.
3. Verlange konkrete Nutzerquellen oder lizenzierten Live-Zugriff, bevor Literatur zitiert wird.
4. Markiere unverifizierte Fundstellen als Prüfbedarf.

## Ausgabe

| Punkt | Prüfbedarf | Quelle |
| --- | --- | --- |
| Norm/TBM | Welche dogmatische Frage ist offen? | Gesetz, verifizierte Rechtsprechung oder Nutzerquelle |

Kurzregel: Norm zuerst. Dann verifizierte Rechtsprechung. Literatur nur mit echter Quelle.

---
name: subsumtions-pruefer-workflow-chronologie-und-belegmatrix
title: Chronologie und Belegmatrix für Subsumtion
description: 'Für Chronologie und Belegmatrix für Subsumtion: ordnet Akte, Belege und Lücken; Ergebnis: Chronologie mit Beleg- und Widerspruchsmatrix.'
author: Klotzkette
author_url: https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/subsumtions-pruefer/skills/workflow-chronologie-und-belegmatrix
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: general
language: de
---

# Chronologie und Belegmatrix für Subsumtion

## Arbeitsauftrag

Übersetze die Akte in eine Subsumtionsmatrix. Jede Tatsache bekommt ein Tatbestandsmerkmal, einen Beleg, eine Beweisstärke und eine offene Rechtsfolge. Frage nicht allgemein nach dem Fall, sondern nur nach fehlenden Tatsachen zu konkreten Merkmalen.

## Normenanker

- BGB/ZPO als Grundmodell: Anspruchsnorm, Einwendung, Einrede, Darlegungs- und Beweislast.
- ZPO §§ 138, 286, 287: Erklärungslast, freie Beweiswürdigung, Schadensschätzung.
- VwGO § 86, SGG § 103, FamFG § 26: Amtsermittlung dort, wo die Verfahrensart es verlangt.
- StPO §§ 244, 261 bei strafrechtlichem Bezug: Aufklärung und Überzeugungsbildung.
- GG Art. 103 Abs. 1: rechtliches Gehör als Fehlerbremse.

## Ausgabe

Tabelle: Tatbestandsmerkmal, Tatsache, Beleg, Gegnerbestreiten, Beweislast, Lücke, nächste Handlung. Danach kurze Subsumtionsfassung ohne erfundene Tatsachen.

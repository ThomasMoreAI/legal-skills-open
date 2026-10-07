---
title: Accueil
layout: default
nav_order: 1
---

# Paperasse Lux

[![Tests](https://github.com/gregherbe76/Luxembourg-Paperasse/actions/workflows/tests.yml/badge.svg)](https://github.com/gregherbe76/Luxembourg-Paperasse/actions/workflows/tests.yml)

> **Des skills pour agents IA spécialisés dans la bureaucratie luxembourgeoise.**
> Parce que la paperasse luxembourgeoise est aussi rigoureuse que les frites du Bouneweger Stuff sont fondantes.

[Démarrer en 2 minutes]({{ site.baseurl }}/quickstart){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2 }
[Voir sur GitHub](https://github.com/gregherbe76/Luxembourg-Paperasse){: .btn .fs-5 .mb-4 .mb-md-0 }

---

## Pourquoi ce projet ?

Le Luxembourg a ses propres lois, taux, formats de fichier et organismes (AED, ACD, CSSF, LBR, Légilux…). La plupart des outils francophones grand public sont calibrés pour la France et tombent à côté dès qu'on parle de **TVA luxembourgeoise (17 %)**, **classes d'impôt 1/1a/2**, **FAIA**, **eCDF**, **Bëllegen Akt** ou de **dépôt LBR**.

Paperasse Lux comble le manque avec des **modules JavaScript déterministes**, **testés**, **sourcés** et **utilisables soit en CLI, soit comme skill par un agent IA** (Claude, Cursor, etc.).

## Modules disponibles

| Module | Description | Tests |
|---|---|---|
| [**FAIA**]({{ site.baseurl }}/modules/faia) | Fichier d'audit informatisé AED (SAF-T LU 2.01) | 24 |
| [**RTS**]({{ site.baseurl }}/modules/rts) | Retenue à la source 2025, classes 1/1a/2 | 20 |
| [**Bëllegen Akt**]({{ site.baseurl }}/modules/bellegen-akt) | Droits d'enregistrement immo + abattement 40 k€/personne | 17 |
| [**eCDF**]({{ site.baseurl }}/modules/ecdf) | Génération XML eCDF (déclarations fiscales) | 24 |
| [**LBR**]({{ site.baseurl }}/modules/lbr) | Dépôts Registre de Commerce et des Sociétés | 25 |
| [**Templates DE**]({{ site.baseurl }}/modules/templates-de) | Modèles allemand pour partie germanophone du LU | 18 |
| [**Banques**]({{ site.baseurl }}/modules/bank) | Parseurs BCEE, BIL, Spuerkeess, ING LU | 18 |
| [**Calc**]({{ site.baseurl }}/modules/calc) | IRC, ICC, IF, IRPP, TVA, succession | 19 |

**Total : 165 tests automatisés**, tous verts en CI à chaque commit.

## Garanties

- **Sources officielles citées** dans chaque module (ACD, AED, Mémorial A, LBR…).
- **Validation stricte** des formats LU : RCS (B/F/G/E/K/X + chiffres), matricule TVA (LU + 8 chiffres), IBAN LU, dates ISO réelles.
- **Pas de scraping fragile** : on s'appuie sur les portails publics et les flux RSS officiels.
- **Open-source MIT** : code auditable, contributions bienvenues.

## En savoir plus

- [Démarrage rapide]({{ site.baseurl }}/quickstart)
- [Liste des modules]({{ site.baseurl }}/modules/)
- [Sources officielles]({{ site.baseurl }}/sources)
- [FAQ]({{ site.baseurl }}/faq)

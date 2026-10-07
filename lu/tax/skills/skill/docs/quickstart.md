---
title: Démarrage rapide
layout: default
nav_order: 2
---

# Démarrage rapide

## Prérequis

- **Node.js 20+** (vérifier avec `node --version`)
- Un terminal (Mac, Linux ou WSL/PowerShell sous Windows)

## Installation

```bash
git clone https://github.com/gregherbe76/Luxembourg-Paperasse.git
cd Luxembourg-Paperasse
npm install
```

C'est tout — aucune dépendance lourde, aucun service à lancer.

## Premier calcul : combien coûte mon appartement ?

```bash
npm run bellegen-akt -- --prix 600000 --acquereurs 2 --lux-ville
```

Vous obtenez en clair : droits d'enregistrement, crédit Bëllegen Akt appliqué, honoraires de notaire estimés, TVA, total.

## Deuxième exemple : ma fiche de paie

```bash
npm run rts -- --brut 5000 --classe 1
```

CSSS, IRPP, contribution dépendance, net mensuel, taux effectif.

## Troisième exemple : générer un FAIA

```bash
node scripts/generate-faia.js examples/faia-input.json > faia.xml
```

Le fichier `examples/faia-input.json` documente le format complet attendu.

## Lancer tous les tests

```bash
npm test
```

165 tests doivent passer en moins de 5 secondes.

## Utilisation comme skill par un agent IA

Le fichier [`SKILL.md`](https://github.com/gregherbe76/Luxembourg-Paperasse/blob/main/SKILL.md) à la racine est un point d'entrée pensé pour Claude Code, Cursor et autres agents capables de lire des skills. L'agent y trouve la liste des commandes, leurs paramètres et des exemples concrets.

Voir aussi la fiche AgentSkill.sh : [agentskill.sh/@gregherbe76](https://agentskill.sh/@gregherbe76).

## Et après ?

- [Liste détaillée des modules]({{ site.baseurl }}/modules/)
- [FAQ]({{ site.baseurl }}/faq)

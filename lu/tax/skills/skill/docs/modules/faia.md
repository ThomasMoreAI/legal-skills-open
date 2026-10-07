---
title: FAIA
layout: default
parent: Modules
nav_order: 1
---

# FAIA — Fichier d'Audit Informatisé AED

Génère un fichier **SAF-T LU 2.01** conforme au profil de l'**Administration de l'Enregistrement, des Domaines et de la TVA (AED)**, exigible lors de tout contrôle TVA depuis le 1ᵉʳ janvier 2011.

## Quand l'utiliser ?

- Vous recevez un courrier de l'AED annonçant un contrôle TVA.
- Vous vendez votre entreprise et l'acquéreur exige un FAIA des 3 derniers exercices.
- Votre fiduciaire demande un export comptable au format normalisé.

## En CLI

```bash
node scripts/generate-faia.js examples/faia-input.json > faia.xml
node scripts/generate-faia.js examples/faia-input.json --validate-only
```

Le mode `--validate-only` vérifie l'équilibre comptable, les identifiants RCS/TVA et les dates sans produire de XML.

## En JavaScript

```js
import { genererFAIA } from './lib/faia/index.js';

const { xml, totals, validation } = genererFAIA({
  company: {
    rcs: 'B12345',
    matriculeTVA: 'LU12345678',
    raisonSociale: 'ACME S.à r.l.',
    siegeSocial: { rue: '1 rue du Test', ville: 'Luxembourg', codePostal: 'L-1234' },
  },
  period: { start: '2025-01-01', end: '2025-12-31', fiscalYear: '2025' },
  accounts: [...],
  entries: [...],
  salesInvoices: [...],
});
```

Voir le format complet : [`examples/faia-input.json`](https://github.com/gregherbe76/Luxembourg-Paperasse/blob/main/examples/faia-input.json).

## Validations strictes

Avant génération, le module rejette :

- Numéro RCS hors format LU (B/F/G/E/K/X + 1 à 7 chiffres).
- Matricule TVA hors format `LU` + 8 chiffres.
- Dates impossibles (2025-02-30, etc.).
- Période avec `start > end`.
- Écritures à moins de 2 lignes.
- Lignes ayant à la fois débit ET crédit (ou aucun des deux).
- Écritures déséquilibrées (somme débit ≠ somme crédit, tolérance 0,005 €).

Avertit aussi sur les `AccountID` orphelins (référencés sans figurer dans le plan comptable).

## Codes TVA LU pris en charge

| Code | Taux | Libellé |
|---|---|---|
| STD | 17,00 % | Standard |
| INT | 14,00 % | Intermédiaire |
| RED | 8,00 % | Réduit |
| SUP | 3,00 % | Super-réduit (logement) |
| EXM | 0 % | Exonération |
| ZRO | 0 % | Zéro (export / intracom) |

## Limitations connues

- Section `<Owners>` non générée (rare, à ajouter manuellement si demandée).
- Pas de support multi-devises avec conversions historiques (mono-devise EUR).
- Pas de validation XSD complète : utiliser un validateur XSD externe avant dépôt à l'AED.

## Sources

- AED — Administration de l'Enregistrement, des Domaines et de la TVA, [aed.public.lu](https://pfi.public.lu/fr/support/faia.html)
- Schéma SAF-T LU 2.01 publié par l'AED.

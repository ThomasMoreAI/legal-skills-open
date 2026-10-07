---
title: Bëllegen Akt
layout: default
parent: Modules
nav_order: 3
---

# Bëllegen Akt — Droits d'enregistrement immobiliers

Calcule le **coût total** d'une acquisition immobilière au Luxembourg : droits d'enregistrement, droits de transcription, surtaxe communale Luxembourg-Ville, **crédit d'impôt « Bëllegen Akt »**, honoraires de notaire et TVA.

## En CLI

```bash
npm run bellegen-akt -- --prix 600000 --acquereurs 2
npm run bellegen-akt -- --prix 800000 --acquereurs 2 --lux-ville
npm run bellegen-akt -- --prix 350000 --no-bellegen-akt
```

## Taux applicables

| Élément | Taux |
|---|---|
| Droit d'enregistrement | **6 %** |
| Surtaxe communale Luxembourg-Ville | **+3 %** |
| Droit de transcription | **+1 %** |
| **Total hors Lux-Ville** | **7 %** |
| **Total Lux-Ville** | **10 %** |

## Crédit d'impôt « Bëllegen Akt »

Depuis le **1ᵉʳ octobre 2024** (loi du 22 mai 2024), pour l'acquisition d'une **résidence principale** :

> **40 000 €** d'abattement **par personne acquéreuse**, imputés directement sur les droits d'enregistrement dus.

Avant le 1er octobre 2024 : 30 000 €/personne (le module gère automatiquement le bon plafond selon `--date`).

### Exemple concret : couple à Luxembourg-Ville, 800 000 €

- Droits nominaux : 800 000 × 10 % = **80 000 €**
- Crédit Bëllegen Akt : 2 × 40 000 = **80 000 €**
- Droits NETS à payer : **0 €** ✓

L'abattement est **plafonné aux droits dus** : il n'y a pas de remboursement si l'abattement excède les droits.

## Honoraires de notaire

Estimation selon le **tarif réglementé dégressif** (règlement grand-ducal du 24 janvier 2003) :

| Tranche prix | Taux marginal |
|---|---|
| 0 → 100 000 € | 1,2 % |
| 100 000 → 300 000 € | 0,9 % |
| 300 000 → 1 000 000 € | 0,7 % |
| > 1 000 000 € | 0,5 % |

TVA 17 % appliquée aux honoraires. Débours estimés à 400 €.

## Hors périmètre

- Successions, donations entre vifs : barèmes différents.
- VEFA avec option TVA logement à 3 % : voir le module [Calc]({{ site.baseurl }}/modules/calc) (TVA réduite logement).

## Sources

- Loi modifiée du 30 juillet 2002 (droits d'enregistrement et de transcription)
- Loi du 22 mai 2024 (réforme Bëllegen Akt, en vigueur 1ᵉʳ octobre 2024)
- AED — [aed.public.lu](https://pfi.public.lu/fr/demarches/marches.html)

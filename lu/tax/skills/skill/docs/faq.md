---
title: FAQ
layout: default
nav_order: 5
---

# FAQ

## Est-ce un service en ligne ?

Non. Paperasse Lux est une **bibliothèque open-source** (MIT) à exécuter localement. Aucune donnée ne quitte votre machine.

## Puis-je m'en servir comme conseiller fiscal ?

Non. Les chiffres sont fournis à titre indicatif. **Pour toute opération réelle (déclaration, acte notarié, dépôt LBR), consultez un fiduciaire ou un notaire luxembourgeois.** Les modules sont conçus pour vous faire gagner du temps de préparation et vous aider à comprendre, pas pour vous représenter devant l'administration.

## Les chiffres sont-ils à jour ?

Le projet maintient une **fraîcheur annuelle** : `npm run freshness` vérifie que les barèmes et taux n'ont pas dépassé leur date de validité. Le barème IRPP est à jour pour **2025** (loi inflation du 19 décembre 2024). Le crédit Bëllegen Akt est à jour pour la **réforme du 1ᵉʳ octobre 2024**.

Si une loi change, ouvrez une [issue GitHub](https://github.com/gregherbe76/Luxembourg-Paperasse/issues) et le projet sera mis à jour.

## J'ai trouvé une erreur dans un calcul. Que faire ?

Ouvrez une issue avec :

1. Le calcul réalisé (commande exacte et entrée).
2. Le résultat obtenu.
3. Le résultat attendu, **avec la source officielle** (article de loi, formulaire ACD, simulation officielle).

Les calculs sont **déterministes** et **testés** : si une divergence existe avec une source officielle, c'est un bug à corriger.

## Pourquoi pas de support du créole guadeloupéen / suédois / etc. ?

Le périmètre est strictement luxembourgeois. Pour la France, voir le projet **Paperasse** original.

## Comment contribuer ?

- Fork → branche → PR. La CI doit passer.
- Toute nouvelle fonctionnalité doit être **testée** (même style que les modules existants).
- Toute donnée chiffrée doit être **sourcée** dans le code (commentaire avec lien vers Légilux ou l'administration concernée).

## Le projet est-il maintenu ?

Maintenu par [Grégory Herbé](https://github.com/gregherbe76). Voir le [CHANGELOG](https://github.com/gregherbe76/Luxembourg-Paperasse/blob/main/CHANGELOG.md) pour la cadence.

## Comment activer le site doc moi-même sur mon fork ?

GitHub → **Settings** → **Pages** → Source : **Deploy from a branch** → Branch : **main**, dossier : **/docs**. Le site est en ligne en < 1 minute.

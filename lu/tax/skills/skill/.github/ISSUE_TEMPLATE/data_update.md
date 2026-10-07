---
name: Mise à jour d'une donnée légale
about: Proposer la mise à jour d'un seuil, taux ou barème (TVA, ICC, IRPP, Bëllegen Akt…)
title: "[data] "
labels: data
---

## Donnée à mettre à jour

<!-- ex. taux TVA super-réduit, multiplicateur ICC Esch-sur-Alzette, abattement Bëllegen Akt -->

## Fichier concerné

<!-- ex. comptable/data/tva-taux.json -->

## Valeur actuelle dans le repo

```json
{
  "champ": "valeur actuelle"
}
```

## Nouvelle valeur

```json
{
  "champ": "nouvelle valeur"
}
```

## Source primaire

- Texte de loi / règlement :
- Date de publication au Mémorial :
- Lien ELI : https://data.legilux.public.lu/eli/...
- Date d'entrée en vigueur :

## Vérification flux Légilux

- [ ] J'ai consulté le flux RSS `https://data.legilux.public.lu/api/rss-leg.xml`
- [ ] Aucune publication plus récente ne modifie cette donnée

## `last_updated` à mettre à jour

- [ ] Oui, je mettrai `last_updated: "YYYY-MM-DD"` dans la PR

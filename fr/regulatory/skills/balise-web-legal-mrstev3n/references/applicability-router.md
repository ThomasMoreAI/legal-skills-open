# Routeur d'applicabilité

## Fiche de rattachement

Identifier séparément :

- entité qui décide des finalités et moyens;
- éditeur du site et vendeur ou prestataire contractuel;
- siège, établissements, représentant et immatriculations;
- pays expressément ciblés par langue, prix, devise, livraison, publicité, domaine ou support;
- résidence ou localisation des utilisateurs et personnes concernées;
- lieux d'hébergement, d'administration, de support et de traitement;
- prestataires, sous-traitants, responsables conjoints et destinataires;
- origine et destination des transferts;
- secteur, mineurs, données sensibles et activité réglementée;
- date de lancement, collecte ou incident.

La simple accessibilité mondiale d'un site ne prouve pas nécessairement un ciblage. À l'inverse, l'absence d'établissement local n'exclut pas une loi comportant des critères extraterritoriaux.

## Couches à tester

| Couche | Questions |
|---|---|
| Données | champ territorial, responsable, formalités, information, droits, sécurité, transferts |
| Terminal et communications | cookies, stockage local, pixels, SDK, prospection électronique |
| Éditeur | identité, coordonnées, immatriculation, hébergeur, directeur de publication, activité réglementée |
| E-commerce | information précontractuelle, prix, commande, paiement, livraison, rétractation, médiation, résiliation |
| Contrat | CGU, CGV, abonnement, marketplace, vendeurs tiers, droit applicable |
| Secteur | santé, finance, éducation, emploi, enfants, télécommunications, jeux ou autre régime |
| Communautaire | OHADA, UEMOA/BCEAO, CEMAC/BEAC, CEDEAO, UE ou autre |

## Sortie obligatoire

```markdown
## Carte d'applicabilité

| Juridiction/corpus | Critère de rattachement | Matière | Statut | Source | Point à confirmer |
|---|---|---|---|---|---|

- Date juridique pertinente :
- Pays seulement accessibles mais non ciblés :
- Transferts et prestataires transfrontaliers :
- Conflits ou cumuls possibles :
```

Ne conclure `applicable` qu'après avoir vérifié les critères dans le texte ou une interprétation officielle. Sinon utiliser `probable`, `à confirmer` ou `non applicable selon les faits disponibles`.

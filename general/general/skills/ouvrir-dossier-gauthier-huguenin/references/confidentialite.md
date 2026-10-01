# Prévol de confidentialité

## Classification minimale

| Niveau | Exemple | Comportement |
| --- | --- | --- |
| public | décision publiée, texte officiel | traitement possible |
| interne | note de travail sans donnée client | confirmer l'usage prévu |
| confidentiel | correspondance, contrat, stratégie | vérifier l'environnement |
| sensible | santé, infractions, données très identifiantes | suspendre sans validation explicite |

La classification est prudente et ne remplace pas l'analyse du cabinet.

## Pseudonymisation

- Remplacer les personnes par `PERSONNE_1`, `PERSONNE_2`.
- Remplacer les sociétés par `SOCIETE_A`, `SOCIETE_B`.
- Remplacer les coordonnées, numéros de dossier, comptes et identifiants.
- Conserver séparément la table de correspondance hors de l'agent si elle est nécessaire.
- Vérifier les métadonnées et le contenu des annexes.

Ne jamais affirmer qu'un document est anonymisé uniquement parce que les noms visibles ont été remplacés.

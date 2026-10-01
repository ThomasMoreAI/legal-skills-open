# Contrat d'orchestration

## Artefacts

| Artefact | Producteur | Consommateurs |
| --- | --- | --- |
| `manifest-dossier.md` | `ouvrir-dossier` | toutes les skills |
| `registre-pieces.md` | `analyser-pieces` | chronologie, entretien, rédaction, contrôle |
| `registre-faits.md` | `analyser-pieces` | chronologie, entretien, recherche, rédaction, contrôle |
| `chronologie.md` | `construire-chronologie` | entretien, recherche, rédaction, contrôle |
| `brief-entretien.md` | `preparer-entretien-client` | avocat, mise à jour des faits |
| `note-recherche.md` | `rechercher-droit` | rédaction, contrôle |
| `projet-livrable.md` | `rediger-projet` | contrôle |
| `rapport-controle.md` | `controler-livrable` | avocat |

## Identifiants

- Pièce : `P-001`
- Fait ou allégation : `F-001`
- Evénement : `E-001`
- Question client : `Q-001`
- Source juridique : `S-001`
- Anomalie de contrôle : `A-001`

Ne jamais réutiliser un identifiant pour un autre élément. Conserver les identifiants existants lors d'une mise à jour.

## Modifications

- Ajouter les nouvelles informations sans écraser l'historique utile.
- Marquer un élément remplacé comme `obsolete` et indiquer son successeur.
- Conserver l'auteur de la validation et sa date uniquement s'ils sont explicitement connus.
- Propager une correction dans les artefacts dépendants ou les marquer `a_recalculer`.

## Arrêts obligatoires

Arrêter l'enchainement si :

- l'environnement n'est pas autorisé pour les données ;
- les fichiers critiques sont illisibles ;
- l'identité des parties ne peut pas être distinguée ;
- l'utilisateur demande une source juridique sans accès permettant de la vérifier ;
- le projet repose sur une contradiction non arbitrée ;
- le contrôle final contient une anomalie bloquante.

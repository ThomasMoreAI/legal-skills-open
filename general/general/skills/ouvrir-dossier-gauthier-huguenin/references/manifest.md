# Règles du manifest

## Statuts de document

- `recu`
- `illisible`
- `partiellement_lisible`
- `protege`
- `lien_inaccessible`
- `doublon_probable`
- `annonce_non_recu`

## Statuts du dossier

- `pret_pour_analyse`
- `bloque_confidentialite`
- `bloque_lisibilite`
- `incomplet_non_bloquant`
- `a_cadrer`

Attribuer un identifiant `P-001` à chaque pièce reçue. Une pièce annoncée mais absente reçoit un identifiant uniquement si elle doit être suivie, avec le statut `annonce_non_recu`.

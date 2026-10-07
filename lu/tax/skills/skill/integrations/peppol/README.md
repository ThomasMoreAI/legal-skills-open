# Peppol — Facturation électronique B2G luxembourgeoise

Au Luxembourg, **la facturation électronique est obligatoire pour toute facture émise vers un acheteur public** depuis :

- **18 mai 2022** : grandes entreprises
- **18 octobre 2022** : moyennes entreprises
- **18 mars 2023** : petites entreprises et indépendants

Base légale : [loi du 13 décembre 2021](https://legilux.public.lu/eli/etat/leg/loi/2021/12/13/a911/jo) transposant la directive 2014/55/UE.

## Format obligatoire

- Format : **Peppol BIS Billing 3.0** (UBL 2.1 ou UN/CEFACT CII), conforme norme EN 16931
- Transport : **réseau Peppol** (4-corners model)
- Identifiant acheteur : **ID Peppol** (format `0208:LU<matricule>` pour les entités LU)

## Comment émettre

Vous devez passer par un **point d'accès Peppol agréé** (Access Point, AP) :

| AP | Site |
|---|---|
| Storecove | https://www.storecove.com |
| Pagero | https://www.pagero.com |
| Unifiedpost | https://www.unifiedpost.com |
| TIE Kinetix | https://tiekinetix.com |
| Banking Circle | https://www.bankingcircle.com |
| Babelway (Lugera) | https://www.babelway.com |

Annuaire complet : https://peppol.eu/who-is-who/peppol-service-providers/

## Comment trouver l'ID Peppol d'un acheteur public LU

1. Annuaire public Peppol : https://directory.peppol.eu
2. Annuaire des entités publiques LU : https://pch.gouvernement.lu (Portail des achats publics)

Format type pour une administration LU : `0208:LU` + matricule (numéro RCS sans préfixe `B`, ou matricule national pour les administrations).

## Configuration côté Paperasse Lux

```bash
# .env
PEPPOL_AP_ENDPOINT=https://api.storecove.com/api/v2
PEPPOL_AP_API_KEY=...
PEPPOL_PARTICIPANT_ID=0208:LU12345678
```

Et dans la facture (cf. `templates/facture-lux.html`), le champ Peppol s'ajoute automatiquement quand `client.secteur === "public"`.

## Limites v0.1

Pas encore de script `npm run send:peppol` qui pousse réellement la facture sur le réseau — le squelette du fichier UBL est généré, mais l'envoi réel dépend de l'AP retenu (chaque AP a sa propre API). Pour une v1, ajouter `integrations/peppol/send.js` adapté à votre AP.

## Ressources

- Norme : https://docs.peppol.eu/poacc/billing/3.0/
- Spec UBL 2.1 : https://docs.oasis-open.org/ubl/UBL-2.1.html
- Vérifier la conformité d'une facture UBL : https://peppol.helger.com/public/menuitem-validation-upload

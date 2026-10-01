# AVOIR N° {{NUMERO_AVOIR}}

**Annule et remplace la facture N° {{NUMERO_FACTURE_ORIGINE}}** du {{DATE_FACTURE_ORIGINE}}

**Date d'émission** : {{DATE_EMISSION}}

---

## Émetteur

**{{RAISON_SOCIALE_EMETTEUR}}**
{{ADRESSE_EMETTEUR}}
L-{{CP_EMETTEUR}} {{VILLE_EMETTEUR}}

RCS Luxembourg : B {{NUMERO_RCS}}
N° TVA : LU {{TVA_EMETTEUR}}

---

## Client

**{{RAISON_SOCIALE_CLIENT}}**
{{ADRESSE_CLIENT}}
{{CP_CLIENT}} {{VILLE_CLIENT}}

N° TVA : {{TVA_CLIENT}}

---

## Motif de l'avoir

{{MOTIF_AVOIR}}

(exemples : annulation pour erreur de facturation, remise commerciale rétroactive, retour de marchandise, prestation non rendue)

---

## Détail des montants annulés

| Description | Quantité | Prix unitaire HT | Taux TVA | Montant HT |
|---|---:|---:|---:|---:|
| {{LIGNE_1_DESCRIPTION}} | -{{QTE_1}} | {{PU_1}} € | {{TVA_1}} % | -{{HT_1}} € |

---

## Récapitulatif

| | Montant |
|---|---:|
| **Total HT à déduire** | -{{TOTAL_HT}} € |
| TVA à régulariser | -{{TVA_TOTAL}} € |
| **Total TTC à recréditer** | **-{{TOTAL_TTC}} €** |

---

## Modalités de remboursement

{{MODALITES}}

(exemples : remboursement par virement bancaire sous 15 jours, déduction sur la prochaine facture, avoir à valoir)

---

## Mentions légales

- Avoir conforme à l'art. 56 loi TVA Lux
- À conserver 10 ans (art. 11 Code commerce)
- TVA à régulariser dans la déclaration TVA suivante par l'émetteur et le client (rectification de TVA déduite côté client)

---

*{{RAISON_SOCIALE_EMETTEUR}} — Pour avoir et reconnaître*

Date : {{DATE_EMISSION}}

Signature et cachet :

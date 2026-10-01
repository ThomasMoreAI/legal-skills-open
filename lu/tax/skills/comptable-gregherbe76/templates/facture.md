# FACTURE N° {{NUMERO_FACTURE}}

**Date d'émission** : {{DATE_EMISSION}}
**Date d'échéance** : {{DATE_ECHEANCE}}

---

## Émetteur

**{{RAISON_SOCIALE_EMETTEUR}}**
{{ADRESSE_EMETTEUR}}
L-{{CP_EMETTEUR}} {{VILLE_EMETTEUR}}
Luxembourg

RCS Luxembourg : **B {{NUMERO_RCS}}**
Matricule national : {{MATRICULE_NATIONAL}}
N° TVA : **LU {{TVA_EMETTEUR}}**

---

## Client

**{{RAISON_SOCIALE_CLIENT}}**
{{ADRESSE_CLIENT}}
{{CP_CLIENT}} {{VILLE_CLIENT}}
{{PAYS_CLIENT}}

N° TVA : {{TVA_CLIENT}}
Référence client : {{REF_CLIENT}}

---

## Détail des prestations

| Description | Quantité | Prix unitaire HT | Taux TVA | Montant HT |
|---|---:|---:|---:|---:|
| {{LIGNE_1_DESCRIPTION}} | {{QTE_1}} | {{PU_1}} € | {{TVA_1}} % | {{HT_1}} € |
| {{LIGNE_2_DESCRIPTION}} | {{QTE_2}} | {{PU_2}} € | {{TVA_2}} % | {{HT_2}} € |

---

## Récapitulatif

| | Montant |
|---|---:|
| **Total HT** | {{TOTAL_HT}} € |
| TVA 17 % | {{TVA_17}} € |
| TVA 8 % | {{TVA_8}} € |
| TVA 3 % | {{TVA_3}} € |
| **Total TTC** | **{{TOTAL_TTC}} €** |

---

## Conditions de paiement

- Échéance : **{{DATE_ECHEANCE}}**
- Mode de règlement : virement bancaire
- IBAN : **{{IBAN}}**
- BIC : **{{BIC}}**
- Référence à mentionner : **FAC-{{NUMERO_FACTURE}}**

---

## Mentions légales

- Pénalités de retard : taux légal majoré de 8 points (loi 18 avril 2004 sur les délais de paiement)
- Indemnité forfaitaire de recouvrement : 40 €
- Pas d'escompte pour paiement anticipé sauf mention contraire

{{#SI_INTRA_UE_B2B}}
> **Auto-liquidation par le preneur — art. 196 dir. TVA UE**
{{/SI_INTRA_UE_B2B}}

{{#SI_FRANCHISE_PME}}
> **Régime particulier — Franchise des petites entreprises (art. 57bis loi TVA Lux)**
{{/SI_FRANCHISE_PME}}

---

*Facture conforme aux exigences de la loi modifiée du 12 février 1979 concernant la TVA.*

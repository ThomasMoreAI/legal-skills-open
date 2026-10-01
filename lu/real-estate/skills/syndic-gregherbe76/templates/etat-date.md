# ÉTAT DATÉ
## Copropriété « {{NOM_RESIDENCE}} » — {{ADRESSE_RESIDENCE}}

---

**Établi par** : {{NOM_SYNDIC}}
{{ADRESSE_SYNDIC}}

**À l'attention de** : Maître {{NOM_NOTAIRE}}
{{ADRESSE_NOTAIRE}}

**Date d'établissement** : {{DATE_ETAT_DATE}}
**Arrêté à la date de** : {{DATE_ARRETE}}
**Référence dossier notaire** : {{REF_DOSSIER}}

---

## 1. IDENTIFICATION DU LOT

**Lot n°** : {{NUMERO_LOT}}
**Description** : {{DESCRIPTION_LOT}}
(exemple : appartement T3 au 4e étage avec balcon, étage technique : étage 4, escalier B)

**Annexes** : {{ANNEXES_LOT}}
(exemples : cave n° 12, parking n° 8, grenier n° 5)

**Quote-part des parties communes** : **{{MILLIEMES}} / 1 000**

---

## 2. IDENTIFICATION DES PARTIES À LA VENTE

### Vendeur (copropriétaire actuel)
**{{NOM_PRENOM_VENDEUR}}**
{{ADRESSE_VENDEUR}}
N° matricule : {{MATRICULE_VENDEUR}}

### Acheteur (futur copropriétaire)
**{{NOM_PRENOM_ACHETEUR}}**
{{ADRESSE_ACHETEUR}}
N° matricule : {{MATRICULE_ACHETEUR}}

**Date prévue de l'acte authentique** : {{DATE_ACTE_PREVUE}}

---

## 3. SITUATION DU VENDEUR AU {{DATE_ARRETE}}

### 3.1 Charges restant dues

| Poste | Période | Montant |
|---|---|---:|
| Appel courant {{TRIMESTRE_DERNIER}} | {{PERIODE_TRIMESTRE}} | {{MONTANT_TRIM_DU}} € |
| Régularisation {{ANNEE_REGUL}} | Voté en AG {{DATE_AG_REGUL}} | {{MONTANT_REGUL}} € |
| Cotisation fonds travaux | {{PERIODE_FDT}} | {{MONTANT_FDT_DU}} € |
| Pénalités de retard | Calculées au {{DATE_ARRETE}} | {{PENALITES}} € |
| **Total dû par le vendeur** | | **{{TOTAL_DU}} €** |

### 3.2 Avances ou trop-perçus

| Nature | Montant |
|---|---:|
| Solde créditeur antérieur | {{SOLDE_CREDITEUR}} € |

**Solde net à régulariser par le vendeur avant l'acte** : **{{SOLDE_NET_DU}} €**

---

## 4. CHARGES COURANTES ENGAGÉES NON ENCORE APPELÉES

Pour la période **{{PERIODE_NON_APPELEE}}** (entre le dernier appel et la date prévue d'acte), le vendeur restera redevable des charges courantes attribuables à sa période de propriété :

| Estimation | Montant |
|---|---:|
| Charges courantes non encore appelées (estimation) | {{ESTIMATION_NON_APPELE}} € |

---

## 5. TRAVAUX VOTÉS NON ENCORE APPELÉS

> ⚠️ **À l'attention de l'acheteur** : ces appels seront émis APRÈS la date de l'acte. Selon le règlement de copropriété et l'article 14quater de la loi 1975, c'est le **propriétaire à la date de l'appel** qui en est redevable.

### Travaux décidés en AG

{{#TRAVAUX_VOTES}}

#### {{NOM_TRAVAUX_1}}
- AG décisionnaire : {{DATE_AG_1}}
- Résolution : n° {{NUM_RESOLUTION_1}}
- Entreprise : {{ENTREPRISE_1}}
- Coût total syndicat : {{COUT_TOTAL_1}} €
- **Quote-part lot** : **{{QUOTE_PART_1}} €**
- Appels déjà émis : {{APPELS_DEJA_EMIS_1}} €
- **Reste à appeler** : **{{RESTE_A_APPELER_1}} €**
- Échéancier prévu :
  - {{DATE_APPEL_FUTUR_1A}} : {{MONTANT_APPEL_FUTUR_1A}} €
  - {{DATE_APPEL_FUTUR_1B}} : {{MONTANT_APPEL_FUTUR_1B}} €

{{/TRAVAUX_VOTES}}

**Total reste à appeler pour ce lot** : **{{TOTAL_RESTE_APPELER}} €**

---

## 6. FONDS DE TRAVAUX

### Situation au {{DATE_ARRETE}}

| | Montant |
|---|---:|
| **Total du fonds de travaux** (syndicat) | {{TOTAL_FDT}} € |
| **Quote-part attribuable au lot** ({{MILLIEMES}}/1000) | **{{QUOTE_PART_FDT}} €** |

> ⚠️ **Important — Loi du 16 décembre 2019** :
>
> Le fonds de travaux **suit le lot** et n'est **PAS remboursable** au copropriétaire vendeur. L'acheteur en bénéficie automatiquement à la date de l'acte sans devoir le racheter.
>
> Cette quote-part doit être prise en compte dans la **négociation du prix de vente**.

---

## 7. PROCÉDURES EN COURS CONCERNANT LE LOT VENDEUR

{{#PROCEDURES_EN_COURS}}
- **{{NATURE_PROCEDURE}}** — Date d'engagement : {{DATE_PROCEDURE}}
  - Stade actuel : {{STADE}}
  - Montant en jeu : {{MONTANT_PROCEDURE}} €
{{/PROCEDURES_EN_COURS}}

{{#SI_AUCUNE_PROCEDURE}}
**Aucune procédure en cours** concernant le copropriétaire vendeur.
{{/SI_AUCUNE_PROCEDURE}}

---

## 8. PROCÉDURES EN COURS DE LA COPROPRIÉTÉ

Procédures impliquant le syndicat dans son ensemble (pouvant impacter financièrement les copropriétaires) :

{{#PROCEDURES_SYNDICAT}}
- **{{NATURE_1}}** : {{DESCRIPTION_1}}
  - Risque financier estimé pour le syndicat : {{RISQUE_1}} €
  - Quote-part lot : {{RISQUE_LOT_1}} €
{{/PROCEDURES_SYNDICAT}}

{{#SI_AUCUNE_PROCEDURE_SYNDICAT}}
**Aucune procédure en cours** au niveau du syndicat.
{{/SI_AUCUNE_PROCEDURE_SYNDICAT}}

---

## 9. ÉLÉMENTS INFORMATIFS

### Travaux prévus / probables (non encore votés)

{{#TRAVAUX_PROBABLES}}
- **{{NATURE}}** : envisagé pour {{PERIODE_PROBABLE}}, estimation {{ESTIMATION}} €
{{/TRAVAUX_PROBABLES}}

### Audits et études en cours
- DPE collectif : {{ETAT_DPE}} ({{CLASSE_DPE}})
- Audit énergétique : {{ETAT_AUDIT}}
- Plan pluriannuel travaux : {{ETAT_PPT}}

### Informations sur la copropriété

| | |
|---|---|
| Nombre total de lots | {{NB_LOTS}} |
| Année de construction | {{ANNEE_CONSTRUCTION}} |
| Surface totale | {{SURFACE_TOTALE}} m² |
| Charges annuelles moyennes par lot | {{CHARGES_MOYENNES}} € |
| Date dernière AG | {{DATE_DERNIERE_AG}} |
| Date prochaine AG | {{DATE_PROCHAINE_AG}} |

---

## 10. SYNTHÈSE FINANCIÈRE POUR L'ACTE

### À régler par le **VENDEUR** avant ou au moment de l'acte

| | Montant |
|---|---:|
| Charges restant dues au {{DATE_ARRETE}} | {{TOTAL_DU}} € |
| Charges courantes engagées non appelées (estimation période) | {{ESTIMATION_NON_APPELE}} € |
| **Total à charge du vendeur** | **{{TOTAL_VENDEUR}} €** |

### À la charge de l'**ACHETEUR** dès l'acte

| | Montant |
|---|---:|
| Charges courantes à compter du {{DATE_ACTE_PREVUE}} | (à venir) |
| Travaux votés non encore appelés (futurs appels) | {{TOTAL_RESTE_APPELER}} € |
| Quote-part fonds de travaux (suit le lot, sans contrepartie) | {{QUOTE_PART_FDT}} € |

---

## 11. DOCUMENTS REMIS À L'ACHETEUR

L'acheteur recevra :
- [x] Le présent état daté
- [x] Le règlement de copropriété
- [x] Les 3 derniers procès-verbaux d'AG
- [x] Les comptes annuels des 2 derniers exercices
- [x] Le DPE collectif (si disponible)
- [x] L'état du carnet d'entretien (équipements collectifs)
- [x] Les contrats en cours (assurance, ascenseur, conciergerie)

---

## 12. HONORAIRES DE LA PRÉSENTE PRESTATION

Conformément au règlement intérieur du syndic, les honoraires d'établissement du présent état daté sont :

| | Montant |
|---|---:|
| Honoraires HT | {{HONORAIRES_HT}} € |
| TVA 17 % | {{TVA_HONORAIRES}} € |
| **Total TTC** | **{{HONORAIRES_TTC}} €** |

**À la charge du vendeur**, à régler avant la date de l'acte authentique.

---

## ATTESTATION

Le syndic soussigné certifie l'exactitude des informations contenues dans le présent état daté, établi conformément à l'article 14quater de la loi modifiée du 16 mai 1975 sur la copropriété.

Cet état daté est valable jusqu'à la date prévue de l'acte authentique. En cas de report > 30 jours, une mise à jour est nécessaire.

**Date** : {{DATE_ETAT_DATE}}

**Signature et cachet du syndic**

{{NOM_REPRESENTANT_SYNDIC}}
{{FONCTION}}
{{NOM_SYNDIC}}

---

> Document confidentiel — destiné exclusivement au notaire pour l'établissement de l'acte authentique de vente. Toute communication à des tiers nécessite l'accord du syndicat.

# Réconciliation résultat comptable → résultat fiscal, Exercice {{ANNEE}}

**Société** : {{COMPANY_NAME}} (SIREN {{SIREN}})
**Exercice** : {{ANNEE}}

## Résultat comptable

| Poste | Montant |
|-------|---------|
| Résultat comptable avant IS | {{RESULTAT_COMPTABLE}} € |

## Réintégrations extra-comptables

| Poste | Montant | Commentaire |
|-------|---------|-------------|
| IS de l'exercice (charge 695) | {{REINT_IS}} € | Non déductible |
| Amendes et pénalités fiscales | {{REINT_AMENDES}} € | Non déductibles |
| Dépenses somptuaires (art. 39-4) | {{REINT_SOMPTUAIRES}} € | Non déductibles |
| Intérêts excédentaires (art. 212 bis) | {{REINT_INTERETS}} € | Limitation 30% EBITDA |
| Véhicules de tourisme > plafond | {{REINT_VEHICULES}} € | Plafond 30 k€ (18.3 k€ si > 150 g CO2) |
| Provisions non déductibles | {{REINT_PROVISIONS}} € | Risque non individualisé |
| Cadeaux > 73 € TTC non justifiés | {{REINT_CADEAUX}} € | Seuil dépassé |
| Autres réintégrations | {{REINT_AUTRES}} € | {{REINT_AUTRES_DETAIL}} |
| **Total réintégrations** | **{{TOTAL_REINTEGRATIONS}} €** | |

## Déductions extra-comptables

| Poste | Montant | Commentaire |
|-------|---------|-------------|
| Quote-part de frais et charges (12%) | {{DEDUC_QPFC}} € | Sur dividendes reçus ayant donné droit régime mère-fille |
| Dividendes régime mère-fille | {{DEDUC_DIVIDENDES}} € | Exonération 95% |
| Plus-values exonérées (titres de participation) | {{DEDUC_PV}} € | Exonération 88% (long terme) |
| Reports de déficits | {{DEDUC_DEFICIT}} € | Plafonné 1M€ + 50% au-delà |
| Autres déductions | {{DEDUC_AUTRES}} € | {{DEDUC_AUTRES_DETAIL}} |
| **Total déductions** | **{{TOTAL_DEDUCTIONS}} €** | |

## Calcul du résultat fiscal

| | Montant |
|--|---------|
| Résultat comptable | {{RESULTAT_COMPTABLE}} € |
| + Réintégrations | {{TOTAL_REINTEGRATIONS}} € |
| − Déductions | {{TOTAL_DEDUCTIONS}} € |
| **= Résultat fiscal** | **{{RESULTAT_FISCAL}} €** |

## Calcul de l'IS

### Si PME avec taux réduit

| Tranche | Base | Taux | IS |
|---------|------|------|-----|
| 0, 42 500 € | {{BASE_REDUIT}} € | 15% | {{IS_REDUIT}} € |
| > 42 500 € | {{BASE_NORMAL}} € | 25% | {{IS_NORMAL}} € |
| **Total IS brut** | | | **{{IS_BRUT}} €** |

### Si taux normal uniquement

IS brut = {{RESULTAT_FISCAL}} € × 25% = **{{IS_BRUT}} €**

## Imputations

| | Montant |
|--|---------|
| IS brut | {{IS_BRUT}} € |
| − Acomptes versés (4 × {{ACOMPTE_UNIT}}) | {{TOTAL_ACOMPTES}} € |
| − Crédit d'Impôt Recherche | {{CIR}} € |
| − Crédit d'Impôt Innovation | {{CII}} € |
| − Autres crédits d'impôt | {{AUTRES_CREDITS}} € |
| **Solde IS** | **{{SOLDE_IS}} €** |

## Taux effectif d'imposition

Taux effectif = IS brut / Résultat comptable = **{{TAUX_EFFECTIF}}%**

## Pièces justificatives à conserver

- [ ] Balance définitive
- [ ] Grand livre
- [ ] FEC
- [ ] Justifs des réintégrations (factures somptuaires, amendes, etc.)
- [ ] Dossier justificatif CIR / CII
- [ ] Tableau d'amortissements
- [ ] Procès-verbaux AG pour affectation du résultat

---

_Préparé par : {{NOM_PREPARATEUR}}, {{DATE}}_
_Validé par expert-comptable : {{NOM_EC}}, {{DATE_VALIDATION_EC}}_
_Télétransmission TDFC : {{DATE_TDFC}}_

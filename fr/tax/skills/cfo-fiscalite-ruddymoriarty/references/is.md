# Impôt sur les Sociétés (IS)

## Taux 2026

- **Taux normal** : 25%
- **Taux réduit PME** : 15% sur la fraction de bénéfice < 42 500 €
- **Conditions taux réduit** :
  - CA HT < 10 M€
  - Capital entièrement libéré
  - Capital détenu à ≥ 75% par des personnes physiques (ou société remplissant aussi la condition)

## Acomptes trimestriels

Pour une société à l'IS avec clôture 31/12 :
- Acompte 1 : 15/03 = 8,5% du bénéfice fiscal N-2 (ou N-1 si connu)
- Acompte 2 : 15/06 = même montant
- Acompte 3 : 15/09 = même montant
- Acompte 4 : 15/12 = même montant

**Pour clôture autre date** : décalage proportionnel (cf. `cfo-init/compute_calendar.py`).

**Exception** : aucun acompte si IS N-1 < 3 000 €.

## Solde IS

**Pour clôture 31/12** : à payer le **15/05 N+1** (avec télétransmission de la liasse 2065-SD).

## Calcul résultat fiscal

```
Résultat comptable
+ Réintégrations extra-comptables (amendes, pénalités, IS lui-même, charges somptuaires)
- Déductions extra-comptables (produits exonérés, quote-part de frais et charges)
= Résultat fiscal
```

Appliquer le taux :
- 15% sur les 42 500 premiers € (si conditions PME)
- 25% au-delà

**Imputations** :
- Acomptes déjà versés
- Crédits d'impôt (CIR, CII, crédits étrangers)
- Reports déficitaires (limité à 1 M€ + 50% du bénéfice au-delà)

**Solde** = IS dû - Acomptes - Crédits.

## Optimisations légitimes

### Amortissements dérogatoires

Passer d'un amortissement linéaire à dégressif pour accélérer la déduction fiscale (ex. matériels industriels, véhicules professionnels).

### Report en arrière (carry back)

Si déficit N, possibilité d'imputer sur le bénéfice N-1 (créance remboursable après 5 ans si non utilisée, plafonnée à 1 M€).

### Provisions déductibles

Provisions pour risques et charges déductibles si :
- Risque individualisé
- Probable (pas seulement possible)
- Évaluable avec une précision suffisante
- Non encore certain (sinon dette réelle)

### CIR / CII

Voir `cir.md` et `cii.md`. Crédit d'impôt imputable sur IS (ou remboursable pour les PME < 150 k€).

### JEI (Jeune Entreprise Innovante)

Exonération IS sur 2 exercices consécutifs (premier exercice bénéficiaire et suivant), puis abattement 50%. Conditions :
- < 8 ans
- < 250 salariés
- CA < 50 M€
- Dépenses R&D > 15% des charges

## Script `is_simulator.py`

Calcule l'IS prévisionnel à partir de la balance + hypothèses de réintégrations.

Input : résultat comptable + liste réintégrations + crédits d'impôt
Output : IS dû + solde à payer + charge IS effective

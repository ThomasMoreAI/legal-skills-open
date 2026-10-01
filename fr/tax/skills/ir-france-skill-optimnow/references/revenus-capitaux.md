# Revenus de capitaux mobiliers

## Table des matières

1. [Principe général : PFU vs barème](#pfu-vs-bareme)
2. [Dividendes](#dividendes)
3. [Intérêts](#interets)
4. [Assurance-vie](#assurance-vie)
5. [PEA et PEA-PME](#pea)
6. [Choix PFU vs barème : méthode de décision](#methode-decision)

---

## PFU vs barème {#pfu-vs-bareme}

Le prélèvement forfaitaire unique (PFU ou "flat tax") est le régime par défaut depuis 2018.

- **PFU** : 30 % (12,8 % IR + 17,2 % prélèvements sociaux)
- **Option barème** : cocher case **2OP**. L'option s'applique à TOUS les revenus de capitaux mobiliers et plus-values de l'année. Elle est globale et irrévocable pour l'année.

L'option barème permet de bénéficier :
- De l'abattement de 40 % sur les dividendes
- De la déductibilité partielle de la CSG (6,8 %)
- Du barème progressif (intéressant si TMI <= 11 % voire 30 % avec l'abattement dividendes)

---

## Dividendes {#dividendes}

### Avec PFU (défaut)
- Montant brut des dividendes en case **2DC**
- Prélèvement déjà versé à la source (acompte 12,8 %) en case **2CK**
- Pas d'abattement de 40 %

### Avec option barème (case 2OP cochée)
- Montant brut en case **2DC**
- Abattement de 40 % appliqué automatiquement
- CSG déductible (6,8 %) imputable sur le revenu global de l'année suivante

### Cas du gérant majoritaire SARL
Les dividendes perçus par le gérant majoritaire (et son conjoint/partenaire) qui dépassent
10 % du capital social + primes d'émission + apports en compte courant sont soumis
aux cotisations sociales TNS (et non aux seuls prélèvements sociaux de 17,2 %).
Ces dividendes restent soumis à l'IR (PFU ou barème).

### Source du montant
Le montant figure sur l'IFU (Imprimé Fiscal Unique) envoyé par la banque ou la société.

---

## Intérêts {#interets}

### Intérêts imposables
- Comptes à terme, obligations, comptes courants d'associé : case **2TR**
- Livret A, LDDS, LEP : exonérés (ne pas déclarer)
- PEL : intérêts des PEL ouverts après 2018 soumis au PFU dès la 1ère année

### Avec PFU
- Montant brut en case 2TR
- Acompte déjà versé (12,8 %) en case 2CK

### Avec option barème
- Montant brut en case 2TR
- Pas d'abattement (contrairement aux dividendes)
- CSG déductible de 6,8 %

---

## Assurance-vie {#assurance-vie}

Le traitement fiscal dépend de la date de versement des primes et de l'ancienneté du contrat.

### Primes versées après le 27/09/2017

| Ancienneté du contrat | Primes < 150 000 EUR | Primes > 150 000 EUR |
|------------------------|----------------------|----------------------|
| < 8 ans                | PFU 30 % (ou barème) | PFU 30 % (ou barème) |
| >= 8 ans               | 7,5 % + PS 17,2 %   | 12,8 % + PS 17,2 %  |

Abattement annuel sur les produits des contrats de plus de 8 ans :
- 4 600 EUR (célibataire)
- 9 200 EUR (couple)

### Primes versées avant le 27/09/2017
- < 8 ans : barème ou prélèvement libératoire 35 % (< 4 ans) / 15 % (4-8 ans)
- >= 8 ans : 7,5 % + PS après abattement

### Cases
- **2DH** : produits des contrats >= 8 ans (primes avant 27/09/2017)
- **2CH** : produits soumis au PFU
- Les montants sont généralement pré-remplis à partir de l'IFU de l'assureur

---

## PEA et PEA-PME {#pea}

### Régime fiscal
- **Avant 5 ans** : clôture du PEA -> gains soumis au PFU (ou barème)
- **Après 5 ans** : gains exonérés d'IR, mais soumis aux prélèvements sociaux (17,2 %)
- Les retraits partiels après 5 ans ne clôturent plus le PEA (depuis 2019)

### Plafond de versement
- PEA : 150 000 EUR
- PEA-PME : 225 000 EUR (cumul PEA + PEA-PME plafonné à 225 000 EUR)

### Points de vigilance
- Les dividendes perçus dans un PEA ne sont pas à déclarer séparément
- En cas de clôture avant 5 ans, les gains sont à déclarer comme plus-values (voir `plus-values.md`)
- Les moins-values sont imputables si clôture avant 5 ans

---

## Choix PFU vs barème : méthode de décision {#methode-decision}

L'option barème est avantageuse quand le taux marginal d'imposition (TMI) effectif
sur les revenus de capitaux est inférieur à 12,8 %.

### Règle simplifiée
- **TMI 0 % ou 11 %** : option barème presque toujours avantageuse
- **TMI 30 %** : dépend du mix dividendes/intérêts
  - Si majorité de dividendes : barème souvent gagnant (grâce à l'abattement 40 %)
  - Si majorité d'intérêts : PFU souvent gagnant
- **TMI 41 % ou 45 %** : PFU presque toujours gagnant

### Méthode exacte
Utiliser le simulateur (`scripts/simulateur-ir.py`) pour comparer les deux scénarios
avec les montants réels. Le calcul doit prendre en compte :
1. L'impact de l'abattement 40 % sur les dividendes
2. La CSG déductible de 6,8 %
3. L'impact sur le RFR (revenu fiscal de référence) pour les seuils sociaux
4. L'impact croisé avec d'autres revenus (l'option barème peut faire changer de tranche)

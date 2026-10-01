# Mécanisme de l'IRPP luxembourgeois

## 1. Vue d'ensemble

L'**Impôt sur le Revenu des Personnes Physiques (IRPP)** est calculé selon ce schéma :

```
Revenu brut total
   − Frais et charges déductibles par catégorie
   = Revenu net par catégorie
   ──────────────────────────────────────────────
   Σ revenus nets catégoriels
   − Abattements et déductions du revenu global
   = Revenu imposable ajusté
   ──────────────────────────────────────────────
   Application du barème selon la classe d'impôt
   = Impôt brut
   + Contribution au fonds pour l'emploi (7 % ou 9 %)
   − Crédits d'impôt (CIS, CIM, CIP, boni enfant…)
   = Impôt à payer (ou crédit)
```

## 2. Catégories de revenus (art. 10 LIR)

| Catégorie | Type |
|---|---|
| 1. Bénéfice commercial (BIC) | Activité industrielle/commerciale |
| 2. Bénéfice agricole et forestier | Exploitation agricole |
| 3. Bénéfice d'une profession libérale | Avocats, médecins, architectes, consultants… |
| 4. Revenu d'une occupation salariée | Salaires bruts |
| 5. Revenus de pensions ou rentes | Pensions retraite / invalidité |
| 6. Revenus de capitaux mobiliers | Dividendes, intérêts |
| 7. Revenus de location de biens | Locations immobilières / mobilières |
| 8. Revenus divers | Plus-values, gains exceptionnels |

## 3. Frais et déductions par catégorie

### Salariés (catégorie 4)
- **Forfait frais d'obtention** : 540 €/an
- Frais réels déductibles si > forfait (justifiés)
- **Frais de déplacement domicile-travail** : forfait kilométrique selon distance (avec plafond)

### Pensionnés (catégorie 5)
- Forfait frais : 300 €/an

### Revenus capitaux (catégorie 6)
- Forfait frais : 25 €/an
- **Abattement dividendes** : 1 500 €/an (50 % des dividendes encaissés exonérés sous conditions)

### Revenus locatifs (catégorie 7)
- Charges réelles déductibles : entretien, intérêts emprunt, taxes foncières
- Amortissement bâti : selon vie utile (50-100 ans)

### Plus-values immobilières
- **Résidence principale** : exonérée si occupée
- **Spéculatif** (vente < 5 ans) : taxé au taux global
- **Long terme** (> 5 ans) : taxé à **demi-taux global** (Art. 132 LIR)

### Plus-values mobilières
- Participation **importante** (> 10 % capital) ou ancienne (> 6 mois) : demi-taux global
- Spéculative (< 6 mois) : taux global plein
- Cession participations en sociétés > 10 % : régime spécifique

## 4. Abattements et déductions du revenu global

Cf. `data/abattements-deductions.json` pour la liste complète.

Les principales déductions :
- Cotisations sécurité sociale (CCSS, CNS) — **intégralement déductibles**
- Pensions alimentaires (conjoint divorcé / enfants)
- Intérêts d'emprunt logement (selon ancienneté)
- Primes assurance vie / solde emprunt (672 €/personne)
- Plan d'épargne-logement (1 344 € si <41 ans)
- **PER (épargne pension art. 111bis)** : **3 200 €/an** par contribuable
- Dons aux œuvres (min 120 €, max 1 M€)
- Frais de garde enfants (5 400 €/enfant <14 ans)

## 5. Application du barème

### Classes d'impôt (cf. `data/classes-impot.json`)

| Classe | Profil | Méthode |
|---|---|---|
| **1** | Célibataire sans enfant | Barème direct |
| **1a** | Parent isolé / >64 ans / veuf | Barème spécifique élargi |
| **2** | Mariés résidents (splitting) | Barème classe 1 sur 50 % du revenu × 2 |

### Barème 2025 (classe 1) — extrait

| Tranche | Taux marginal |
|---|---|
| 0 – 13 230 € | 0 % |
| 13 231 – 26 460 € | 8-14 % |
| ... montée progressive ... | ... |
| 50 716 – 110 403 € | 38 % |
| > 234 870 € | **42 %** |

(Détails complets : `data/bareme-irpp-2025.json`)

## 6. Contribution au fonds pour l'emploi

- **+7 %** sur l'impôt brut si revenu < 150 000 €
- **+9 %** sur l'impôt brut si revenu ≥ 150 000 €

## 7. Crédits d'impôt (à imputer)

| Crédit | Montant max | Conditions |
|---|---|---|
| CIS — Crédit Impôt Salarié | 600 €/an | Dégressif selon revenu |
| CIM — Crédit Impôt Monoparental | 2 505 €/an | Classe 1a + enfant |
| CIP — Crédit Impôt Pensionné | 600 €/an | Pension, dégressif |
| Boni enfant | 922,50 €/enfant/an | Versé d'avance par CAE |

## 8. Mécanisme de retenue à la source (RAS)

### Salariés
- Employeur prélève **mensuellement** l'IRPP sur la paie
- Application de la **fiche de retenue d'impôt** (classe + crédits)
- Régularisation annuelle via :
  - **Décompte annuel** automatique (si salarié unique, pas d'autre revenu, etc.)
  - OU **déclaration d'impôt** (formulaire 100) si revenus complexes ou conjugaux

### Indépendants (libéraux, commerçants)
- **Acomptes provisionnels** trimestriels (10/3, 10/6, 10/9, 10/12)
- Régularisation à réception du bulletin

### Pensionnés résidents
- RAS par la caisse de pension

## 9. Déclaration d'impôt (formulaire 100)

### Obligatoire si
- Revenu salarial > 100 000 €
- Couple marié travaillant tous les deux > 36 000 € chacun
- Revenus non salariaux significatifs
- Revenus de pluriels sources
- Demande de déductions / crédits non gérés par RAS
- Revenus mondiaux (frontaliers ayant opté pour assimilation)

### Délai
- **31 décembre N+1** (sursis sur demande)
- Déclaration via MyGuichet.lu (formulaire 100)

### Pièces justificatives à conserver
- 10 ans (Code commerce + AO)
- Bulletins de salaire annuels
- Attestations cotisations sociales
- Justificatifs frais réels, intérêts, dons, etc.

## 10. Imposition individuelle vs collective (mariés)

Depuis 2018, les couples mariés résidents peuvent **opter** pour :

### Option A — Imposition collective classe 2 (par défaut)
- Splitting : barème classe 1 sur 50 % revenu × 2
- Avantageux si écart de revenus important entre conjoints

### Option B — Imposition individuelle pure
- Chacun imposé seul, classe 1
- Avantageux si revenus égaux ou si l'un est non-résident

### Option C — Imposition individuelle avec réallocation
- Imposition séparée mais réallocation libre des revenus (formulaire 166)
- Optimisation fine

**Choix annuel** avant **31 mars N+1** pour l'année précédente.

## 11. Exemple complet

**Profil** : Couple marié, classe 2, conjoint A 60 000 €, conjoint B 40 000 €, 2 enfants

```
Revenu salarial total brut         100 000 €
- Forfait frais (2 × 540)          - 1 080 €
- Cotisations sociales (~12,5 %)  - 12 500 €
- PER (2 × 3 200)                  - 6 400 €
- Frais garde enfants (réels)      - 5 000 €
                                  ─────────
Revenu imposable                  =  75 020 €

Splitting : 75 020 / 2 =          37 510 €
Impôt classe 1 sur 37 510 €  ≈    3 800 €
× 2 (splitting)                =   7 600 €
+ Contribution chômage 7 %     =   7 600 × 1,07 = 8 132 €
- Boni enfant (2 × 922,50)     - 1 845 €
                                  ─────────
Impôt à payer                  ≈   6 287 €
```

(Calculs simplifiés — appliquer barème exact via `scripts/calc.js`)

## 12. Liens utiles

- ACD : https://impotsdirects.public.lu/
- MyGuichet impôt : https://guichet.public.lu/fr/citoyens/fiscalite.html
- LIR (texte officiel) : https://eli.legilux.public.lu/eli/etat/leg/loi/1967/12/04
- Calculatrice impôt ACD : https://impotsdirects.public.lu (rubrique « calculatrice »)

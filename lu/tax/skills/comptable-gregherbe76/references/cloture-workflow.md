# Workflow de clôture annuelle — SARL/SA luxembourgeoise

## Vue d'ensemble

```
Clôture exercice N (31/12)
        ↓
Travaux comptables (Jan-Mar)
        ↓
Comptes annuels arrêtés (Mar-Avr)
        ↓
TVA-100 annuelle (1er mars)
        ↓
Approbation AGO (dans les 6 mois)
        ↓
Dépôt RCS / RESA (dans les 7 mois)
        ↓
Déclaration IRC/ICC/IF (31/12 N+1)
```

## Étape 1 — Travaux de clôture comptable (janvier-mars)

### 1.1 Inventaire physique
- Stocks au 31/12 valorisés au coût d'acquisition ou valeur réalisable nette (la plus basse)
- Caisse comptée et rapprochée
- Immobilisations vérifiées (cessions, mises au rebut)

### 1.2 Régularisations comptables
- **Charges et produits constatés d'avance** (compte 48)
- **Charges à payer / produits à recevoir** (compte 47)
- **Dotations aux amortissements** (compte 68 / 29)
  - Linéaire ou dégressif (option art. 32 LIR)
  - Durées d'usage : matériel info 3 ans, mobilier 10 ans, bâtiment 25-50 ans
- **Provisions** (risques, garanties, pensions)
- **Variation de stocks** (comptes 71)

### 1.3 Rapprochements
- Rapprochement bancaire mensuel jusqu'au 31/12
- État de rapprochement clients/fournisseurs (lettrage)
- Réconciliation TVA collectée/déductible vs déclarations périodiques

### 1.4 Calcul de l'impôt sur le résultat
- Bénéfice fiscal = bénéfice comptable + réintégrations − déductions
- Calculer IRC, ICC, IF estimés
- Comptabiliser provision pour impôt (compte 4441/4442/4443 + 691)

## Étape 2 — Comptes annuels (avant 30 avril idéalement)

### Documents à produire
1. **Bilan** au format eCDF (PCN)
2. **Compte de profits et pertes** (PCN)
3. **Annexe** (notes obligatoires)
4. **Rapport de gestion** (si moyenne/grande entreprise)
5. **Rapport du réviseur** (si audit obligatoire)

### Format eCDF
- Plateforme **eCDF.public.lu**
- Modèles **MIRA / SIRA** (Modèles Intégrés de Reporting Annuel)
  - Micro : abrégé
  - PME : abrégé étendu
  - Grande : complet
- Signature LuxTrust requise

### Annexe — points clés
- Méthodes d'évaluation
- État détaillé des immobilisations
- Effectif moyen
- Rémunérations des organes
- Engagements hors bilan
- Honoraires du réviseur (si EIP)

## Étape 3 — TVA-100 annuelle (1er mars)

Récapitulatif annuel obligatoire pour **tous les assujettis**, même sous franchise.

Réconciliation :
- CA déclaré annuel = somme des déclarations périodiques
- Sinon → régularisation (compense ou complément)
- Détail des opérations exonérées, intra-UE, exportations

## Étape 4 — Assemblée Générale Ordinaire (AGO)

### Délai
- **Dans les 6 mois** après clôture (loi 1915 sur les sociétés, art. 70)
- Date statutaire ou décidée par le conseil de gérance

### Convocation
- Lettre recommandée 8 jours avant minimum
- Ordre du jour précis

### Ordre du jour type
1. Présentation des comptes annuels
2. Présentation du rapport de gestion
3. Présentation du rapport du réviseur (le cas échéant)
4. **Approbation des comptes annuels**
5. **Affectation du résultat** (réserve légale 5 % minimum jusqu'à 10 % du capital)
6. **Décharge** (quitus) aux gérants/administrateurs et au réviseur
7. Renouvellement éventuel des mandats

### PV
- Procès-verbal d'AGO signé par président + secrétaire + scrutateur
- Décisions actées (voir template `pv-approbation-comptes.md`)

## Étape 5 — Dépôt RCS / publication RESA

### Délai légal
- **7 mois** après clôture (art. 79 loi 19 décembre 2002)
- Sanctions retard : amendes administratives, refus d'extraits

### Documents à déposer (LBR.lu)
1. Comptes annuels eCDF
2. Rapport de gestion (si applicable)
3. Rapport du réviseur (si audit)
4. PV d'AGO mentionnant l'approbation
5. Liste des participations

### Frais
- Dépôt RCS : ~30 € (selon taille)
- Publication RESA : automatique, frais inclus

## Étape 6 — Déclaration IRC / ICC / IF (formulaire 500)

### Délai
- **31 décembre N+1** (sursis sur demande motivée jusqu'au 31 mars N+2)

### Composition
- **Modèle 500** (PM) avec annexes :
  - 506 : revenus
  - 555 : déclaration ICC
  - 555E : déclaration IF
- **Bilan fiscal** + tableau passage comptable → fiscal

### Plateforme
- eCDF.public.lu (XML signé)

## Étape 7 — Acomptes provisionnels (année N+1)

Quatre acomptes par an :
- **10 mars, 10 juin, 10 septembre, 10 décembre**
- Chacun = 25 % de l'impôt estimé année précédente
- Régularisation à réception du bulletin définitif

## Délais récapitulatifs

| Action | Échéance |
|---|---|
| Comptes annuels arrêtés | 30 avril (interne) |
| TVA-100 | **1er mars** |
| AGO + approbation | **6 mois** après clôture |
| Dépôt RCS/RESA | **7 mois** après clôture |
| Déclaration IRC/ICC/IF | **31 décembre N+1** |
| Acomptes IRC | **10/3, 10/6, 10/9, 10/12** |

## Sanctions

- Dépôt RCS tardif : amende 25 à 1 250 € + risque dissolution judiciaire
- Déclaration tardive ACD : majoration jusqu'à 10 % de l'impôt
- Absence comptes : taxation d'office par l'ACD

## Checklist du comptable

- [ ] Inventaire physique stock signé
- [ ] Rapprochements bancaires lettrés
- [ ] TVA réconciliée (cumul périodes vs comptable)
- [ ] Amortissements calculés et passés
- [ ] Provisions évaluées et passées
- [ ] CCA / PCA / charges à payer / produits à recevoir
- [ ] Calcul IRC/ICC/IF + comptabilisation
- [ ] Établissement bilan + CPP + annexe (eCDF)
- [ ] Convocation AGO envoyée 8 jours avant
- [ ] PV AGO signé
- [ ] Dépôt RCS/RESA dans les 7 mois
- [ ] Déclaration TVA-100 au 1/3
- [ ] Déclaration IRC/ICC/IF au 31/12 N+1

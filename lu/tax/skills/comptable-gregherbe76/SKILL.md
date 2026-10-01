---
name: comptable-gregherbe76
title: 'Skill : Comptable Luxembourg'
description: Expert-comptable luxembourgeois — écritures PCN, TVA Lux, IRC/ICC, clôture annuelle, FAIA, eCDF, dépôt RCS, facturation (Peppol, e-invoicing B2G).
author: gregherbe76
author_url: https://github.com/gregherbe76/Luxembourg-Paperasse/tree/main/comptable
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: lu
practice: tax
language: fr
sources:
- title: Cloture Workflow
  path: references/cloture-workflow.md
- title: Formes Juridiques
  path: references/formes-juridiques.md
- title: Irc Icc Calcul
  path: references/irc-icc-calcul.md
- title: Peppol Faia
  path: references/peppol-faia.md
- title: Tva Lux
  path: references/tva-lux.md
---

# Skill : Comptable Luxembourg

Vous êtes un expert-comptable luxembourgeois. Vous tenez la comptabilité d'entreprises de droit luxembourgeois (SARL, SA, SARL-S, SCSp, SAS, ASBL, SNC, SCS) selon le **Plan Comptable Normalisé (PCN)** issu du règlement grand-ducal du 12 septembre 2019.

## Garde-fous : avant toute écriture

Vérifiez `company.json`. Si absent, demandez :
1. Raison sociale et forme juridique
2. Numéro RCS (B…)
3. Matricule national (13 chiffres)
4. Matricule TVA (LU + 8 chiffres) si assujetti
5. Régime TVA : mensuel / trimestriel / annuel / franchise
6. Exercice comptable
7. Taille de l'entreprise (micro / petite / moyenne / grande — voir art. 35 loi 19 déc. 2002)
8. Commune (pour le taux ICC)

Ne devinez **jamais** ces informations.

## 1. Plan Comptable Normalisé (PCN)

Structure en 7 classes (≠ PCG français en 8 classes) :

| Classe | Intitulé |
|--------|----------|
| 1 | Capitaux propres, provisions, dettes financières et assimilées |
| 2 | Frais d'établissement et actifs immobilisés |
| 3 | Stocks |
| 4 | Créances et dettes |
| 5 | Avoirs en banques, avoirs en CCP, chèques et encaisse |
| 6 | Charges |
| 7 | Produits |

### Comptes les plus utilisés

**Capitaux (classe 1)** :
- 1311 Capital souscrit
- 141 Réserve légale
- 142 Réserves statutaires
- 1421 Réserve quinquennale (impôt sur la fortune)
- 16 Emprunts et dettes assimilées
- 161 Emprunts obligataires
- 162 Dettes envers des établissements de crédit
- 19 Provisions

**Immobilisations (classe 2)** :
- 21 Immobilisations incorporelles (212 Brevets, 213 Logiciels, 217 Goodwill)
- 22 Terrains et constructions (221 Terrains, 222 Constructions)
- 23 Installations techniques, machines, outillage
- 24 Autres installations, outillage, mobilier
- 25 Immobilisations en cours
- 26 Immobilisations financières
- 28 Amortissements (en moins-valeur)

**Stocks (classe 3)** :
- 31 Matières premières
- 33 Produits en cours
- 35 Produits finis
- 37 Marchandises

**Tiers (classe 4)** :
- 40 Créances résultant de ventes et prestations
- 401 Clients
- 405 Effets à recevoir
- 409 Clients douteux
- 42 Personnel et organismes sociaux (421 Rémunérations, 422 CNS, 423 RTS)
- 44 Dettes fiscales (441 TVA collectée, 442 TVA déductible, 443 TVA à décaisser, 446 IRC, 447 ICC, 448 Impôt sur la fortune)
- 45 Dettes envers fournisseurs (451 Fournisseurs, 455 Effets à payer)
- 46 Autres créances et dettes
- 48 Comptes de régularisation (481 Charges constatées d'avance, 482 Produits constatés d'avance)
- 49 Comptes courants associés / siège

**Trésorerie (classe 5)** :
- 51 Banques (5131 BGL, 5132 Spuerkeess, 5133 BIL, etc. — sous-comptes par banque)
- 53 Caisse

**Charges (classe 6)** :
- 60 Achats de matières premières et marchandises
- 61 Variations de stocks
- 62 Autres charges externes (621 Loyers, 622 Honoraires, 623 Publicité, 624 Transports, 625 Déplacements, 626 Frais postaux/télécom, 627 Services bancaires)
- 63 Impôts, taxes et versements assimilés (631 Impôt commercial, 632 Impôt sur la fortune)
- 64 Frais de personnel (641 Salaires, 645 Charges sociales — part patronale CNS, 647 RTS)
- 65 Autres charges d'exploitation
- 66 Charges financières
- 67 Charges exceptionnelles
- 68 Dotations aux amortissements et provisions
- 69 Impôts sur le résultat (691 IRC + contribution chômage, 692 ICC)

**Produits (classe 7)** :
- 70 Ventes de marchandises et production
- 701 Ventes de marchandises (Lux 17%)
- 706 Prestations de services
- 707 Ventes intracom (exonérées art. 43)
- 708 Exports hors UE (exonérées)
- 71 Variations de stocks de produits
- 72 Production immobilisée
- 74 Subventions d'exploitation
- 76 Produits financiers
- 77 Produits exceptionnels

> **Source officielle** : règlement grand-ducal du 12 septembre 2019, annexe.

## 2. TVA luxembourgeoise

### Taux (depuis 1er janvier 2024, retour aux taux d'avant 2023)

| Taux | Cas |
|------|-----|
| **17 %** | Standard (la plupart des biens et services) |
| **14 %** | Intermédiaire (vins, combustibles solides, publications publicitaires, garde d'enfants) |
| **8 %** | Réduit (gaz, électricité, plantes, coiffure, blanchisserie) |
| **3 %** | Super-réduit (alimentation, livres, médicaments, transport public, restauration sur place hors alcool, eau, hôtels, vêtements enfants <14 ans) |
| 0 % / exo | Exports hors UE, intracom B2B (art. 43), bancaire/assurance (art. 44), médical, enseignement, location immobilière |

> En 2023, taux temporairement réduits (16/13/7 %) pour 1 an. Retour aux 17/14/8/3 % au 1er janvier 2024.

### Régimes de déclaration

| CA HT annuel | Régime | Échéance |
|-------------|--------|----------|
| ≥ 620 000 € | Mensuel | 15 du mois suivant |
| 112 000 – 620 000 € | Trimestriel | 15 du mois suivant le trimestre |
| < 112 000 € | Annuel | 1er mars de l'année suivante (déclaration simplifiée) |
| ≤ 50 000 € (depuis 2025) | Franchise (régime PME) | Pas de déclaration TVA, pas de récupération |

**Déclaration annuelle récapitulative** : obligatoire pour tous les assujettis, à déposer **au 1er mai N+1** (ou 31 décembre N+1 pour les redevables uniquement annuels). Formulaires : déclaration 100 (annuelle) + 101 (récap), via **eCDF**.

### Mentions sur facture (loi 12 février 1979, art. 61)

1. Date de délivrance et numéro chronologique
2. Nom + adresse du fournisseur, **matricule TVA LU…**
3. Nom + adresse du client (+ matricule TVA si B2B intracom)
4. Date de l'opération si différente
5. Désignation, quantité
6. Prix HT, taux TVA, montant TVA
7. Montant TTC
8. Mention spéciale : « **Autoliquidation** » (art. 196 directive 2006/112) pour intracom B2B, « Exonération art. 43 » intracom biens, etc.

### Autoliquidation (reverse charge)

Cas : prestations intracom B2B reçues, importations service hors UE, livraisons B2B intracom (côté client), travaux immobiliers entre assujettis luxembourgeois (art. 61bis loi TVA).

Écriture (achat 1 000 € HT, taux 17 %) :
```
622 Honoraires           1 000
442 TVA déductible         170
                  401 Fournisseur    1 000
                  441 TVA collectée    170
```

### Échéances TVA 2025

- Mensuelle : 15 février, 15 mars, …, 15 janvier 2026
- Trimestrielle : 15 mai, 15 août, 15 novembre 2025, 15 février 2026
- Annuelle simplifiée : 1er mars 2026
- **Récapitulative annuelle** : 1er mai 2026

Intérêts de retard : **0,75 % / mois** (art. 84 loi TVA).

## 3. IRC, contribution chômage, ICC, IF

### Impôt sur le revenu des collectivités (IRC) — art. 174 LIR

| Bénéfice imposable | Taux IRC |
|-------------------|----------|
| ≤ 175 000 € | **15 %** |
| 175 001 – 200 001 € | 15 % + ramp-up |
| > 200 001 € | **17 %** (taux 2025, abaissé de 18 % à 17 % par loi du 20 décembre 2024) |

Plus **contribution au fonds pour l'emploi** : **7 % de l'IRC**.

→ Taux global IRC : 15 % × 1,07 = **16,05 %** ou 17 % × 1,07 = **18,19 %**.

### Impôt commercial communal (ICC) — LITL 1936

Base imposable = bénéfice d'exploitation (BIC ajusté) – abattement 17 500 €.
Taux d'assiette : **3 %**.
Taux multiplicateur communal (variable) :

| Commune | Multiplicateur 2025 |
|---------|---------------------|
| Luxembourg-Ville | 225 % → ICC effectif **6,75 %** |
| Esch-sur-Alzette | 350 % → 10,5 % |
| Differdange | 280 % → 8,4 % |
| Schifflange | 350 % → 10,5 % |
| Sandweiler | 250 % → 7,5 % |
| Strassen | 250 % → 7,5 % |
| Bertrange | 225 % → 6,75 % |
| Steinsel | 250 % → 7,5 % |

→ Liste complète actualisée : impotsdirects.public.lu, rubrique « Tableau des taux ICC ».

### Charge fiscale globale (Lux-Ville, bénéfice > 200 001 €) :
**17 % × 1,07 + 6,75 % = 18,19 % + 6,75 % = 24,94 %**

### Impôt sur la fortune (IF) — loi 16 octobre 1934

Société redevable de l'IF :
- 0,5 % sur valeur unitaire ≤ 500 000 000 €
- 0,05 % au-delà
- **Minimum IF (Mindest-IF)** selon total bilan :

| Total bilan | Min IF |
|-------------|--------|
| ≤ 350 000 € | 535 € |
| 350 001 – 2 000 000 € | 1 605 € |
| 2 000 001 – 10 000 000 € | 5 350 € |
| 10 000 001 – 20 000 000 € | 10 700 € |
| 20 000 001 – 30 000 000 € | 16 050 € |
| > 30 000 000 € | 32 100 € |

**Réduction de l'IF** : on peut neutraliser tout ou partie de l'IF en constituant une **réserve quinquennale** (compte 1421) égale à 5× l'IF économisé, à conserver 5 ans (art. 8a loi IF).

### Acomptes (IRC + ICC)

4 acomptes : 10 mars, 10 juin, 10 septembre, 10 décembre — calculés sur la dernière imposition établie.

## 4. Cycle de clôture annuelle (12 étapes)

1. **Inventaire physique** des stocks au 31/12 → ajustement compte 31/35/37
2. **Cut-off achats/ventes** → factures à recevoir (compte 408), factures à établir (compte 418)
3. **Provisions** : créances douteuses (409 + 65 dotation), litiges, garanties, congés payés
4. **Charges/produits constatés d'avance** (481/482)
5. **Amortissements** (cf. § 5)
6. **Évaluation des stocks** : prix d'acquisition ou valeur réalisable nette (la plus basse — principe de prudence)
7. **Comptes courants associés** : intérêts au taux de marché (sinon avantage en nature taxé)
8. **Variation de change** : créances/dettes en devises évaluées au cours de clôture
9. **Calcul IRC, ICC, IF** → écriture compte 691/692/632 contre 446/447/448
10. **Génération FAIA** (cf. § 7)
11. **Établissement comptes annuels** : bilan + CR + annexe (eCDF)
12. **Dépôt RCS via eCDF** (délai : 7 mois après la clôture, soit **31 juillet** pour exercice civil)

## 5. Amortissements (art. 32 LIR + circulaire L.I.R. n° 32)

| Bien | Durée | Taux linéaire |
|------|-------|---------------|
| Bâtiments commerciaux | 33-50 ans | 2-3 % |
| Bâtiments industriels | 25 ans | 4 % |
| Aménagements bâtiments | 10 ans | 10 % |
| Mobilier de bureau | 10 ans | 10 % |
| Matériel informatique | 3 ans | 33,33 % |
| Logiciels | 3 ans | 33,33 % |
| Véhicules de tourisme | 5 ans | 20 % |
| Véhicules utilitaires | 5 ans | 20 % |
| Outillage industriel | 5-10 ans | 10-20 % |
| Brevets | durée légale | linéaire |

**Amortissement dégressif** : autorisé pour biens neufs (sauf bâtiments, voitures particulières), taux = 3× linéaire, plafonné à 30 %.

**Petit outillage** : déduction immédiate si valeur unitaire ≤ **870 €** HT (art. 30 LIR).

## 6. Frais de personnel (RTS, CNS, mutualité, AAA)

### Cotisations sociales (taux 2025)

| Cotisation | Salarié | Employeur | Total |
|-----------|---------|-----------|-------|
| Maladie en espèces (CNS) | 0,25 % | 0,25 % | 0,5 % |
| Maladie en nature (CNS) | 2,80 % | 2,80 % | 5,60 % |
| Pension (CNAP) | 8,00 % | 8,00 % | 16,00 % |
| Mutualité (selon classe risque) | – | 0,53–2,98 % | variable |
| Accident (AAA) | – | ~0,75 % | variable |
| Santé au travail | – | 0,11 % | 0,11 % |
| **Total approx.** | **~11,05 %** | **~12-15 %** | **~24-26 %** |

Plafond cotisable : 5× SSM = **5 × 2 637,79 = 13 188,95 €/mois** (2025).

### Retenue d'impôt sur traitements et salaires (RTS)

L'employeur retient mensuellement selon les **fiches de retenue d'impôt** émises par l'ACD, qui tiennent compte de la classe (1, 1a, 2). Versement à l'ACD au plus tard le **10 du mois suivant** + déclaration annuelle au **28 février**.

Écriture mensuelle (salaire brut 5 000 €, RTS 800 €, CNS sal. 553 €, CNS pat. 600 €) :
```
641 Salaires bruts          5 000
645 Charges patronales       600
                  421 Net à payer        3 647
                  423 RTS à payer          800
                  422 CNS à payer       1 153
```

## 7. FAIA — Fichier d'Audit Informatisé AED

Format XML imposé par l'AED depuis le **1er janvier 2011** pour tout contrôle TVA. Modèle dérivé de la norme **OECD SAF-T** (Standard Audit File for Tax) v 2.01.

### Structure

```xml
<AuditFile>
  <Header> … (info entreprise + période) </Header>
  <MasterFiles>
    <GeneralLedgerAccounts/>
    <Customers/>
    <Suppliers/>
    <TaxTable/>
    <Products/>
  </MasterFiles>
  <GeneralLedgerEntries> … toutes les écritures </GeneralLedgerEntries>
  <SourceDocuments>
    <SalesInvoices/>
    <PurchaseInvoices/>
    <Payments/>
  </SourceDocuments>
</AuditFile>
```

### Quand le générer

- Sur demande lors d'un contrôle AED (TVA)
- Bonne pratique : générer à chaque clôture pour archive

### Validation

L'AED fournit un validateur XSD : https://pfi.public.lu/fr/professionals/audit/faia.html

## 8. eCDF — déclarations électroniques

Plateforme officielle pour le dépôt :
- Comptes annuels (RCS) — abrégé / complet / consolidé
- Déclarations TVA (100, 101)
- Déclarations IRC (500), ICC (510), IF (700)
- Liasse fiscale numérique

Authentification : **LuxTrust** ou **eIDAS**.

URL : https://ecdf.b2g.etat.lu

### Comptes annuels — formats

| Taille | Bilan | CR | Annexe |
|--------|-------|----|----|
| Micro (CA<900k, total bilan<450k, ≤10 emp.) | abrégé eCDF P1 | abrégé | minimal |
| Petite (CA<8m, total bilan<4m, ≤50 emp.) | abrégé | abrégé | abrégé |
| Moyenne | normal | normal | complet |
| Grande / cotée | normal + audit | normal | complet + rapport gestion |

## 9. Facturation électronique (e-invoicing)

### B2G (Business-to-Government) — OBLIGATOIRE

Loi du 13 décembre 2021 transposant directive 2014/55/UE :

| Type entreprise | Date d'obligation B2G |
|----------------|----------------------|
| Grande entreprise | 18 mai 2022 |
| Moyenne entreprise | 18 octobre 2022 |
| Petite/micro | **18 mars 2023** |

Format : **Peppol BIS Billing 3.0** (UBL 2.1). Réseau : **Peppol** (point d'accès via portail e-Facturation luxembourgeois ou prestataire agréé).

### B2B

Pas encore obligatoire. Loi en préparation pour transposition de la directive ViDA (« VAT in the Digital Age » — vote européen 2025) : entrée en vigueur attendue **vers 2028-2030**.

### Mention obligatoire B2G

Numéro **matricule national 13 chiffres** de l'entité publique destinataire (ex. État, communes, hôpitaux). Liste sur portal.public.lu.

## 10. Échéances annuelles (récap)

| Date | Obligation |
|------|-----------|
| 10 du mois | Versement RTS + déclaration mensuelle |
| 15 du mois | Déclaration TVA mensuelle / trimestrielle |
| 1er mars | Déclaration TVA annuelle simplifiée |
| 10 mars / 10 juin / 10 sep / 10 déc | Acomptes IRC + ICC |
| 1er mai | Déclaration TVA récapitulative annuelle |
| 31 mai (ou 31 décembre) | Déclaration impôt particuliers (modèle 100) |
| 31 mai | Déclaration IRC/ICC/IF (sociétés, prorogation possible) |
| 31 juillet | Dépôt comptes annuels au RCS (exercice civil) |
| 28 février | Déclaration RTS annuelle |

## Workflow type : « clôture annuelle »

```
1. Demander company.json
2. Demander balance N et N-1
3. Demander grand livre N (export comptable ou CSV)
4. Demander fichier des immobilisations
5. Cycle 12 étapes (§ 4)
6. Générer FAIA (§ 7)
7. Préparer eCDF :
   - Bilan + CR + annexe (compte 100 RCS)
   - Déclaration IRC 500
   - Déclaration ICC 510
   - Déclaration IF 700 (le cas échéant)
8. Générer PV approbation des comptes (template)
9. Préparer convocation AGO (15 jours avant)
10. Dépôt RCS via eCDF avant 31 juillet
```

## Erreurs fréquentes à éviter

- Confondre **PCG (FR)** et **PCN (LUX)** : structure différente, intitulés différents
- Oublier la **contribution chômage 7 %** sur l'IRC
- Oublier l'**ICC communal** (varie selon commune)
- Confondre **CNS** (santé) et **CNAP** (pension)
- Oublier la **réserve quinquennale** pour réduire l'IF
- Émettre une facture B2G sans Peppol (rejetée)
- Déposer les comptes après le 31 juillet (amende RCS)

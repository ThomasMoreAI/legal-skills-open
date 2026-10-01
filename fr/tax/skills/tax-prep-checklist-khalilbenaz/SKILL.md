---
name: tax-prep-checklist-khalilbenaz
title: Tax Prep Checklist
description: Aide à préparer sa déclaration d'impôts avec une checklist de documents et étapes, adaptée au profil fiscal (salarié, freelance, auto-entrepreneur, SCI, mixte). À utiliser quand l'utilisateur veut préparer ses impôts ou organiser ses documents fiscaux. Se déclenche aussi avec "impôts", "déclaration fiscale", "documents pour les impôts", "préparer mes impôts", "saison fiscale". Also triggers on "tax return checklist", "prepare my taxes", "tax documents".
author: khalilbenaz
author_url: https://github.com/khalilbenaz/claude-skills-collection/tree/main/finance-skills/tax-prep-checklist
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: fr
practice: tax
language: fr
---

# Tax Prep Checklist

## Étape 1 — Qualifier le profil fiscal

Demander :
- **Pays** (France par défaut si non précisé)
- **Statut** : salarié seul / salarié + revenus annexes / freelance / auto-entrepreneur / gérant de société / SCI / mixte
- **Situation familiale** : célibataire, pacsé, marié, enfants à charge
- **Changements N-1** : mariage, naissance, achat immobilier, déménagement, licenciement, héritage

Ce profil détermine quelles sections de la checklist sont pertinentes.

---

## Étape 2 — Checklist documents par catégorie

### Identité & situation
- [ ] Avis d'imposition N-2 (pour pré-remplissage et comparaison)
- [ ] Justificatif de domicile récent (< 3 mois)
- [ ] Changement de situation : acte de mariage/PACS, livret de famille, jugement de divorce

### Revenus salariés
- [ ] Dernière fiche de paie de l'année (décembre N-1) — récapitulatif annuel brut/net
- [ ] Attestation de l'employeur si différente des fiches
- [ ] Indemnités chômage (ARE) : relevé annuel Pôle Emploi / France Travail
- [ ] Indemnités journalières maladie : relevé CPAM

### Revenus d'activité indépendante (freelance / AE)
- [ ] Relevé CA annuel (plateforme AE, logiciel compta, export bancaire)
- [ ] Déclarations CA mensuelles/trimestrielles déposées (URSSAF)
- [ ] Charges réelles déductibles si régime réel : factures fournisseurs, loyer pro, matériel, logiciels, déplacements
- [ ] Relevé cotisations sociales payées (URSSAF, CIPAV, SSI)

### Revenus fonciers (SCI / location nue ou meublée)
- [ ] Bail(s) en cours + montant loyers perçus
- [ ] Charges : intérêts d'emprunt, taxe foncière, charges de copropriété, travaux
- [ ] Relevé de prêt immobilier (part intérêts vs capital)
- [ ] Statut LMNP/LMP si meublé : bilan comptable ou liasse fiscale

### Revenus financiers
- [ ] IFU (Imprimé Fiscal Unique) de chaque établissement bancaire / courtier
- [ ] Relevés PEA, assurance-vie : rachats, dividendes, plus-values réalisées
- [ ] Cryptomonnaies : export CSV des transactions 2025 (Koinly, CoinTracking, ou export brut)

### Charges déductibles & réductions d'impôt
- [ ] Dons associations loi 1901 / cultuelles : reçus fiscaux
- [ ] Emploi à domicile (garde enfant, ménage) : attestation CESU ou Pajemploi
- [ ] Frais réels salariés (si option frais réels) : km pro, repas, double résidence — tous justificatifs
- [ ] Investissement Pinel / Denormandie / Malraux : attestation promoteur
- [ ] Versements PER (Plan Épargne Retraite) : attestation déductible
- [ ] Frais de scolarité enfants : attestation établissement

---

## Étape 3 — Timeline France 2025 (déclaration revenus 2024)

| Date | Action |
|------|--------|
| Début avril 2025 | Ouverture du service en ligne impots.gouv.fr |
| ~22 mai 2025 | Date limite zones 1 (dep. 1–19 + DOM) |
| ~28 mai 2025 | Date limite zones 2 (dep. 20–54) |
| ~5 juin 2025 | Date limite zones 3 (dep. 55–976) |
| Juillet–août | Avis d'imposition disponibles, ajustement taux PAS |

> Pour les autres pays, demander à l'utilisateur ou consulter le site de l'administration fiscale locale.

---

## Étape 4 — Tableau de suivi (à personnaliser)

```markdown
| Document              | Statut     | Source                        | Notes              |
|-----------------------|------------|-------------------------------|--------------------|
| Fiche de paie déc.    | ✅ Reçu    | Espace RH / coffre-fort RH    |                    |
| IFU Boursorama        | ⏳ Attente | Espace client > Fiscalité     | Disponible fév.    |
| Attestation dons      | ✅ Reçu    | Email association             | Montant : 150 €    |
| Export crypto         | ❌ Manque  | Koinly export CSV 2024        | À faire            |
```

---

## Étape 5 — Points à clarifier avec un comptable

Orienter vers un expert-comptable ou l'administration (impots.gouv.fr) pour :
- Choix régime micro vs réel (freelance / foncier)
- Optimisation PER, déficits fonciers, moins-values reportables
- Impatrié / expatrié : convention fiscale applicable
- Indivision, SCI IS vs IR
- Régularisation taux PAS après changement de situation

---

## Garde-fous et pièges fréquents

- **IFU manquant** : disponible mi-février ; ne pas déclarer avant réception sinon correction obligatoire.
- **Frais réels** : option irrévocable pour l'année ; vérifier si gain > abattement 10 % avant de cocher.
- **Cryptomonnaies** : obligation déclarative dès la première cession taxable (art. 150 VH bis CGI) ; chaque swap crypto/crypto peut être taxable selon jurisprudence 2024.
- **Déclaration pré-remplie ≠ déclaration juste** : toujours vérifier les cases pré-remplies (revenus étrangers, AEA, frais réels oubliés).
- **Délai de reprise** : l'administration peut redresser jusqu'à 3 ans (N+3) ; conserver tous justificatifs au moins 3 ans après l'avis.
- **Pénalités de retard** : 10 % du montant dû après mise en demeure, intérêts de retard 0,2 %/mois.
- **Option frais réels déclarée en ligne** : cocher la case 1AK/1BK ET saisir le montant ; oublier le montant = 0 € déductible.

---

## Règles du skill

- Ne calcule PAS l'impôt dû (trop de variables).
- Ne donne pas de conseil d'optimisation fiscale (orienter vers un comptable).
- Adapter au pays si précisé ; sinon France par défaut.
- Pour tout cas complexe (SCI, expatrié, succession), orienter vers un expert-comptable.

> Cette checklist est un outil d'organisation. Pour toute question spécifique, consultez impots.gouv.fr ou un expert-comptable agréé.

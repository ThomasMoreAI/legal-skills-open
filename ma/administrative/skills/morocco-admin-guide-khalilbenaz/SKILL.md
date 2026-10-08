---
name: morocco-admin-guide-khalilbenaz
title: Morocco Admin Guide
description: Guide des démarches administratives marocaines pour les professionnels et entrepreneurs (CNSS, impôts, registre de commerce, auto-entrepreneur). Se déclenche avec "démarches Maroc", "CNSS", "registre de commerce", "administration marocaine", "impôts Maroc", "auto-entrepreneur Maroc". Also triggers on "Morocco paperwork", "CNSS registration", "Moroccan tax procedure".
author: khalilbenaz
author_url: https://github.com/khalilbenaz/claude-skills-collection/tree/main/arabic-skills/morocco-admin-guide
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: ma
practice: administrative
language: fr
---

# Morocco Admin Guide

## 1. Identification du besoin

Avant toute réponse, qualifier précisément la demande :

| Type de demande | Organisme principal | Délai moyen |
|---|---|---|
| Création auto-entrepreneur | ae.gov.ma / CRI | 24-48 h |
| Création SARL | CRI / Tribunal | 3-5 jours ouvrés |
| Affiliation CNSS (société) | damancom.ma | 5-7 jours |
| Déclaration IS / IR | simpl.tax.gov.ma | Selon échéance |
| Immatriculation registre de commerce | Tribunal de commerce | 2-3 jours |

## 2. Choix du statut juridique

**Critères de décision :**

- **Auto-entrepreneur** → CA annuel < 500 000 MAD (commerce/industrie) ou < 200 000 MAD (services). Pas de comptabilité formelle. Pas de salariés. Impôt libératoire : 1 % (achat/revente), 2 % (services). Inscription en ligne sur `ae.gov.ma`.
- **Personne physique commerçante (PPC)** → activité artisanale ou commerciale simple, RCS obligatoire, IR sur bénéfice net réel.
- **SARL** → 1 associé minimum (SARL-AU), capital minimum 1 MAD (librement fixé), responsabilité limitée, IS.
- **SA** → 5 actionnaires minimum, capital ≥ 300 000 MAD (non coté). Gouvernance lourde. Réservé aux projets à financement externe.

**Anti-pattern** : choisir la SARL uniquement pour l'image sans évaluer les charges (expert-comptable obligatoire, tenue de comptabilité). Pour un freelance solo < 200 K MAD/an, auto-entrepreneur est souvent suffisant.

## 3. Création d'entreprise — Étapes détaillées

### 3a. Auto-entrepreneur
```
1. S'inscrire sur ae.gov.ma (CIN + photo + activité)
2. Recevoir attestation d'inscription (email + espace perso)
3. Ouvrir compte bancaire professionnel (optionnel mais recommandé)
4. Déclarer le CA mensuellement ou trimestriellement sur ae.gov.ma
   → Paiement impôt libératoire automatique à la déclaration
```

### 3b. SARL / SARL-AU
```
1. Certificat négatif         → OMPIC (ompic.ma) | ~170 MAD | 24 h en ligne
2. Rédaction des statuts      → notaire ou fiduciaire | ~2 000-5 000 MAD
3. Dépôt du capital           → banque (attestation de blocage)
4. Publication au BO + JAL    → bulletin officiel (bo.gov.ma) + journal annonces légales
5. Immatriculation au RCS     → Tribunal de commerce | ~500-1 500 MAD
6. Identifiant fiscal (IF)    → DGI, automatique via CRI
7. Affiliation CNSS           → damancom.ma (dès le 1er salarié ou gérant associé)
8. Patente / Taxe prof.       → DGI, déclaration dans les 30 j de démarrage
```

**Coût total indicatif SARL-AU 2025-2026 :** 5 000 – 12 000 MAD (hors capital social).

## 4. Obligations fiscales

### Impôt sur les Sociétés (IS)
- Taux progressif (LF 2023→2026) : 20 % (< 1 M MAD), 22,75 % (1-5 M), 26,5 % (5-10 M), 31 % (> 10 M MAD)
- Cotisation minimale (CM) : 0,5 % du CA HT, minimum 3 000 MAD
- **Acomptes provisionnels** : 4 versements trimestriels (mars, juin, sept, déc) sur simpl.tax.gov.ma
- Déclaration annuelle IS : avant le 31 mars (clôture 31/12)

### Impôt sur le Revenu (IR)
- Barème progressif 0-38 % sur salaires/bénéfices professionnels
- Déclaration annuelle IR : avant le 30 avril

### TVA
| Seuil | Régime |
|---|---|
| CA < 500 K MAD | Exonération ou franchise |
| CA ≥ 500 K MAD | TVA de droit commun (20 % / 14 % / 10 % / 7 %) |
- Déclaration mensuelle (CA > 1 M MAD) ou trimestrielle
- Plateforme : `simpl.tax.gov.ma`

### Taxe Professionnelle
- Déclaration dans les 30 jours suivant le démarrage d'activité
- Base : valeur locative des locaux professionnels × coefficient
- Exonération 5 ans pour nouvelles entreprises (hors certaines activités)

### Pénalités clés
- Retard déclaration IS/IR : 5 % du montant dû + 0,5 % par mois de retard
- Défaut de facturation TVA : amende 2 000-50 000 MAD par infraction
- Non-paiement CNSS : majoration 3 % + frais de recouvrement

## 5. CNSS — Affiliation et cotisations

### Affiliation
```
1. Créer compte employeur sur damancom.ma
2. Uploader : statuts ou RC, CIN du gérant, formulaire d'affiliation
3. Obtenir numéro d'affilié (5-7 jours)
```

### Taux de cotisations 2025-2026
| Branche | Part patronale | Part salariale |
|---|---|---|
| Prestations courtes (chômage, etc.) | 1,05 % | 0,52 % |
| Prestations longues (retraite) | 7,93 % | 3,96 % |
| AMO (maladie) | 2,26 % | 2,26 % |
| **Total** | **~23,98 %** | **~6,74 %** |

- Déclaration mensuelle : avant le 10 du mois suivant sur `damancom.ma`
- Paiement en ligne (virement ou CMI)
- **Anti-pattern** : déclarer le gérant majoritaire associé comme salarié CNSS — il cotise en tant que gérant (régime indépendant) sauf si minoritaire ou tiers.

## 6. Plateformes officielles (2026)

| Plateforme | Usage | URL |
|---|---|---|
| simpl.tax.gov.ma | IS, IR, TVA, taxe prof. | https://simpl.tax.gov.ma |
| damancom.ma | CNSS déclarations, AMO | https://www.damancom.ma |
| ae.gov.ma | Auto-entrepreneur | https://www.ae.gov.ma |
| ompic.ma | Certificat négatif, marques | https://www.ompic.ma |
| cri.gov.ma (CRI local) | Création société en ligne | https://www.cri.gov.ma |
| bo.gov.ma | Publication légale (BO) | https://www.bo.gov.ma |

## 7. Garde-fous et pièges fréquents

- **Domiciliation fictive** : adresse non occupée → risque redressement fiscal + refus ouverture compte bancaire. Utiliser un centre de gestion agréé si pas de local.
- **Confusion auto-entrepreneur / société** : un auto-entrepreneur ne peut pas récupérer la TVA ni déduire les charges réelles. Arbitrer dès que CA > 150 K MAD/an ou que les charges déductibles sont significatives.
- **Gérant non affilié CNSS** : le gérant majoritaire (> 50 %) est affilié en tant qu'indépendant ; oublier cette affiliation génère des pénalités CNSS rétroactives.
- **Délai de publication BO** : compter 7-15 jours supplémentaires après dépôt — ne pas promettre une immatriculation express.
- **Loi de finances annuelle** : les taux IS, seuils TVA et cotisations CNSS changent chaque janvier. Vérifier la LF en vigueur avant toute simulation chiffrée.
- **Clôture ≠ 31/12** : une SARL peut avoir une clôture décalée — adapter les échéances IS en conséquence.

## 8. Bonnes pratiques 2026

- Toujours mentionner la source réglementaire (numéro d'article LF ou circulaire DGI).
- Pour toute simulation fiscale, indiquer explicitement l'année de référence de la LF utilisée.
- Recommander un expert-comptable agréé (OEC Maroc) dès qu'il y a des salariés ou un CA > 500 K MAD.
- Orienter vers le CRI local (17 CRIs régionaux) pour les questions spécifiques à une wilaya ou un secteur réglementé (BTP, santé, éducation).
- Pour les non-résidents marocains souhaitant créer : vérifier les règles d'investissement étranger (Office des Changes, formulaire IS 19).

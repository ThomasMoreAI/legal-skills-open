---
name: fr-facturation-electronique-builderced
title: Facturation Electronique (France)
description: Implement French mandatory e-invoicing (Factur-X, UBL) — formats, PDP/PPF platforms, timeline, and compliance requirements for 2026-2027.
author: BuilderCed
author_url: https://github.com/BuilderCed/agent-skills/tree/main/skills/metier-fr/fr-facturation-electronique
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: fr
practice: tax
language: fr
---

# Facturation Electronique (France)

> **AVERTISSEMENT** : Les dates et obligations evoluent. Verifiez toujours sur economie.gouv.fr/aife pour les dernieres mises a jour.

## Quand Utiliser

- Preparer votre systeme a la facturation electronique obligatoire
- Choisir le bon format (Factur-X, UBL, CII)
- Selectionner une PDP (Plateforme de Dematerialisation Partenaire)
- Generer des factures conformes
- Comprendre le e-reporting

## Calendrier d'Obligation

| Date | Obligation | Entreprises |
|------|-----------|-------------|
| Septembre 2026 | Reception obligatoire | Toutes les entreprises |
| Septembre 2026 | Emission obligatoire | Grandes entreprises (>5000 salaries) |
| Septembre 2027 | Emission obligatoire | ETI et PME |

## Formats Acceptes

### Factur-X (Recommande)
- Format hybride : PDF lisible + XML structure (CII)
- 5 profils : Minimum, Basic WL, Basic, EN16931, Extended
- Norme europeenne EN 16931
- Le plus adopte en France

### UBL (Universal Business Language)
- XML pur, norme ISO/IEC 19845
- Plus technique, adapte aux grandes entreprises
- Interoperable EU (Peppol)

### CII (Cross-Industry Invoice)
- XML UN/CEFACT
- Base technique de Factur-X
- Moins repandu seul

## Architecture du Systeme

```
Emetteur → PDP Emetteur → PPF (Portail Public de Facturation) → PDP Recepteur → Recepteur
                              ↓
                        Administration fiscale (DGFiP)
```

### Acteurs
| Acteur | Role |
|--------|------|
| **PPF** (Portail Public de Facturation) | Hub central, gratuit, fonctions de base |
| **PDP** (Plateforme de Dematerialisation Partenaire) | Plateforme privee immatriculee, fonctions avancees |
| **OD** (Operateur de Dematerialisation) | Convertit et transmet via PPF ou PDP |

## Mentions Obligatoires (Facture Electronique)

Toute facture doit contenir :
1. Date d'emission
2. Numero sequentiel unique
3. SIREN/SIRET emetteur et recepteur
4. Denomination sociale
5. Adresse
6. Designation des biens/services
7. Quantite et prix unitaire HT
8. Taux de TVA applicable
9. Montant HT et TTC
10. Numero de TVA intracommunautaire
11. Date de livraison ou de prestation
12. Conditions de reglement

## E-Reporting

En complement de la facturation electronique, le e-reporting couvre :
- Transactions avec des particuliers (B2C)
- Transactions internationales
- Transmission des donnees de paiement

Frequence : mensuelle ou bimestrielle selon le regime de TVA.

## Ce Que Ce Skill Ne Fait PAS

- Ne genere pas de factures (guide le format et la conformite)
- Ne certifie pas les PDP (liste officielle sur economie.gouv.fr)
- Ne transmet pas les factures au PPF
- Ne remplace pas un expert-comptable pour la conformite fiscale

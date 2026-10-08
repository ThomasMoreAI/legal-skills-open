---
name: fr-notariat-builderced
title: Notariat France
description: Navigate French notarial acts — fee calculation (emoluments), succession, donation, SCI creation, property transfer, and regulated fee schedules.
author: BuilderCed
author_url: https://github.com/BuilderCed/agent-skills/tree/main/skills/metier-fr/fr-notariat
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: fr
practice: general
language: fr
---

# Notariat France

> **AVERTISSEMENT** : Orientations generales. Ne remplace pas un notaire. Les baremes changent — verifiez sur service-public.gouv.fr.

## Quand Utiliser

- Estimer des frais de notaire (achat immobilier, donation, succession)
- Comprendre les etapes d'un acte notarie
- Calculer des droits de succession
- Preparer une donation
- Creer une SCI

## Frais de Notaire — Achat Immobilier

### Composition
| Composante | Ancien | Neuf |
|-----------|--------|------|
| Droits de mutation (taxe departementale + communale) | ~5.81% | ~0.71% |
| Emoluments du notaire (bareme reglemente) | ~0.80% | ~0.80% |
| Debours et frais annexes | ~0.40% | ~0.40% |
| **Total approximatif** | **~7-8%** | **~2-3%** |

### Bareme Emoluments Notaire (Proportionnels)
| Tranche | Taux |
|---------|------|
| 0 a 6 500 EUR | 3.870% |
| 6 501 a 17 000 EUR | 1.596% |
| 17 001 a 60 000 EUR | 1.064% |
| Au-dela de 60 000 EUR | 0.799% |
TVA de 20% s'ajoute aux emoluments.

## Droits de Succession

### Abattements
| Lien | Abattement |
|------|-----------|
| Conjoint survivant / partenaire PACS | Exonere total |
| Enfant | 100 000 EUR |
| Petit-enfant | 1 594 EUR (donation: 31 865 EUR) |
| Frere/soeur | 15 932 EUR |
| Neveu/niece | 7 967 EUR |
| Autres | 1 594 EUR |

### Bareme (Ligne Directe : Parents/Enfants)
| Tranche (apres abattement) | Taux |
|---------------------------|------|
| 0 a 8 072 EUR | 5% |
| 8 073 a 12 109 EUR | 10% |
| 12 110 a 15 932 EUR | 15% |
| 15 933 a 552 324 EUR | 20% |
| 552 325 a 902 838 EUR | 30% |
| 902 839 a 1 805 677 EUR | 40% |
| Au-dela de 1 805 677 EUR | 45% |

### Bareme (Freres/Soeurs)
| Tranche | Taux |
|---------|------|
| 0 a 24 430 EUR | 35% |
| Au-dela | 45% |

### Bareme (Autres)
| Lien | Taux |
|------|------|
| Jusqu'au 4eme degre | 55% |
| Au-dela | 60% |

## Donation

### Abattements (Renouvelables Tous les 15 Ans)
| Beneficiaire | Abattement |
|-------------|-----------|
| Enfant | 100 000 EUR |
| Petit-enfant | 31 865 EUR |
| Arriere-petit-enfant | 5 310 EUR |
| Conjoint/PACS | 80 724 EUR |
| Don familial de sommes d'argent (< 80 ans donateur, > 18 ans donataire) | 31 865 EUR supplementaire |

### Donation-Partage
- Fixe la valeur au jour de la donation (pas de re-evaluation au deces)
- Evite les conflits entre heritiers
- Recommandee pour les transmissions de patrimoine

## SCI (Societe Civile Immobiliere)

### Etapes de Creation
1. Redaction des statuts (notaire obligatoire si apport immobilier)
2. Publication annonce legale (~200 EUR)
3. Immatriculation au Greffe du Tribunal de Commerce
4. Capital social : libre (pas de minimum)
5. Minimum 2 associes

### Avantages
- Transmission progressive des parts (abattements donation)
- Gestion souple de l'indivision
- Choix IS ou IR
- Protection du patrimoine familial

### Inconvenients
- Comptabilite obligatoire
- Responsabilite indefinie des associes (proportionnelle aux parts)
- Pas d'avantage fiscal sur les plus-values (si IS)

## Ce Que Ce Skill Ne Fait PAS

- Ne remplace pas un notaire (actes authentiques obligatoires)
- Ne calcule pas les frais exacts (estimations, le notaire fait le calcul definitif)
- Ne redige pas d'actes notaries
- Ne gere pas le droit international prive (successions internationales)
- Ne couvre pas le droit des societes commercial (SAS, SARL)

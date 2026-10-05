---
name: cdae-ai-eligibilite-gsyltc
title: 'Skill : éligibilité CDAE-IA (crédit d''impôt)'
description: Analyse d'éligibilité au crédit d'impôt CDAE-IA (Développement des affaires électroniques intégrant l'intelligence artificielle, Québec) et estimation du crédit. Fournit les conditions d'admissibilité (société et employés), la méthode d'analyse Oui/Non/À déterminer, et la méthode de calcul du crédit. Utiliser lorsque l'humain demande une évaluation d'éligibilité CDAE-IA ou un calcul du crédit possible.
author: Gsyltc
author_url: https://github.com/Gsyltc/homelab-portfolio/tree/main/plugins/architecture-assistant/skills/cdae-ai-eligibilite
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: ca
practice: tax
language: fr
---

# Skill : éligibilité CDAE-IA (crédit d'impôt)

**Source unique de vérité** des conditions d'éligibilité et de la méthode de calcul du crédit d'impôt **CDAE-IA** (Crédit d'impôt pour le **D**éveloppement des **A**ffaires **É**lectroniques intégrant l'**I**ntelligence **A**rtificielle, Québec). Aucun agent ni gabarit ne duplique ces règles : tout acteur qui en a besoin se réfère à cette skill.

> **Portée.** Cette skill fournit une **capacité d'analyse et d'estimation à titre informatif, non contractuelle et sans valeur de conseil fiscal**. Les attestations et le traitement fiscal relèvent d'Investissement Québec et de Revenu Québec. Les montants estimés ne remplacent pas l'avis d'un fiscaliste.

## Acteurs

- **Architecte de solution** : porte l'analyse d'éligibilité et, sur demande explicite de l'humain, l'estimation du crédit. Écrit le verdict `CDAE-AI: Oui / Non` dans la description du projet selon les règles ci-dessous.
- **Architecture Solution & Intégration (coordinateur)** : déclenche l'analyse au bon moment du workflow, sollicite l'Architecte de solution, demande à l'humain les informations manquantes et porte le résultat au gate de validation humaine.

## Quand utiliser

- L'humain demande d'estimer l'éligibilité CDAE-IA d'un projet.
- L'humain demande explicitement une **estimation du crédit** possible (voir conditions strictes plus bas).

**Ne jamais** lancer l'analyse ni le calcul de façon spontanée sans demande humaine : c'est un critère exécutif et d'affaires déclenché à la demande.

---

## 1. Conditions d'éligibilité

### 1.1 Critères pour la société

| Condition | Détail |
|---|---|
| **Établissement** | Doit avoir un établissement actif au Québec. |
| **Type d'entreprise** | Entreprise à but lucratif uniquement. |
| **Revenus TI** | Au moins **75 %** des revenus bruts proviennent d'activités du secteur des technologies de l'information. |
| **Codes SCIAN** | Au moins **50 %** des revenus liés à des codes SCIAN spécifiques (conception de systèmes d'information, édition de logiciels, traitement de données et hébergement). |
| **Intégration IA** | **Intégration significative** de fonctionnalités d'IA obligatoire depuis 2026 (apprentissage automatique, traitement du langage naturel, vision par ordinateur, analyse prédictive). |
| **Certification** | Attestation d'admissibilité d'**Investissement Québec** requise chaque année (exercices débutant après le 31 décembre 2025). |

### 1.2 Critères pour les employés

| Condition | Détail |
|---|---|
| **Effectif minimum** | **6 employés admissibles à temps plein** pour toute l'année financière. |
| **Temps consacré à l'IA** | Chaque employé consacre **75 % ou plus** de son temps à des activités liées à l'IA. |
| **Lieu de travail** | Dépenses salariales uniquement pour l'établissement québécois (groupes à établissements multiples). |

### 1.3 Activités NON admissibles

- Maintenance des systèmes et évolution d'infrastructure accessoire.
- Soutien TI général sans intégration d'IA.
- Mises à jour logicielles de routine.

### 1.4 Points importants

- **Maintien d'effectif** : une interruption temporaire sous le seuil de 6 employés disqualifie l'exercice complet (sauf 2 exceptions strictes).
- **Cumulabilité** : combinable avec d'autres crédits (RS&DE, IDMTC).
- **Régions** : toutes les régions administratives du Québec sont éligibles.

---

## 2. Méthode d'analyse d'éligibilité (Oui / Non / À déterminer)

Évaluer le projet contre les critères de la société (1.1) et des employés (1.2), puis conclure :

- **Oui** — l'ensemble des critères applicables sont satisfaits (ou raisonnablement démontrés par les informations fournies).
- **Non** — au moins un critère déterminant n'est pas satisfait.
- **À déterminer** — il manque des informations pour trancher. Lister précisément les éléments manquants et **les demander à l'humain** ; ne jamais deviner.

### Écriture du verdict dans la description du projet

Après analyse, mettre à jour la **description du projet Multica** selon ces règles :

1. **Si l'analyse conclut `Oui`** :
   - Si la description du projet **ne contient aucune** information `CDAE-AI: Oui / Non` → **ajouter `CDAE-AI: Oui`** dans la description du projet.
2. **Si l'analyse conclut `Non`** :
   - Si la description du projet **ne contient aucune** information `CDAE-AI: Oui / Non` → **ajouter `CDAE-AI: Non`** dans la description du projet.
3. **Si l'analyse conclut `À déterminer`** :
   - **Ne rien écrire** dans la description. Demander à l'humain les informations manquantes et attendre.

> **Idempotence** : si la description porte **déjà** une information `CDAE-AI: Oui` ou `CDAE-AI: Non`, **ne pas l'écraser** automatiquement. Un changement de verdict existant passe par le gate de validation humaine granulaire (choix présenté séparément : Keep / Modify / Redo).
>
> L'écriture dans la description du projet est une action à impact : la soumettre à la **validation humaine granulaire** du workflow (voir `conductor.md`).

---

## 3. Estimation du crédit

L'estimation du crédit ne se fait **que si les trois conditions suivantes sont réunies** :

1. **Demande explicite** de l'humain pour le calcul.
2. **Projet éligible** : la description du projet contient `CDAE-AI: Oui`.
3. **Informations complètes** : l'ensemble des données nécessaires au calcul sont disponibles.

Si une information manque, **indiquer précisément les éléments manquants à l'humain** et ne pas produire d'estimation partielle trompeuse.

### 3.1 Structure du crédit (2026)

```
Taux global : 30 % des salaires admissibles
├── Crédit remboursable : 22 %
└── Déduction non remboursable : 8 %
```

**Taux réduit de moitié** (**11 % remboursable + 4 % non remboursable**) si au moins **50 %** des revenus proviennent de services rendus à une société située à l'extérieur du Québec ayant un **lien de dépendance**.

### 3.2 Formule de calcul

```
Crédit = Salaires admissibles × 30 % × (proratisation des jours travaillés)
```

- **Salaires admissibles** : revenu d'emploi calculé selon la Loi sur les impôts du Québec.
- **Plus de plafond salarial** (l'ancien plafond de 83 333 $ par employé a été aboli).
- Appliquer le **taux réduit** (15 % global : 11 % + 4 %) si la condition de services hors Québec avec lien de dépendance est remplie.

### 3.3 Informations nécessaires au calcul (à réunir avant d'estimer)

- Salaire annuel admissible par employé admissible.
- Nombre de jours travaillés / jours de l'exercice (proratisation).
- Nombre d'employés admissibles (rappel : seuil de 6 à temps plein).
- Confirmation de la part de revenus provenant de services hors Québec avec lien de dépendance (détermine le taux plein ou réduit).

### 3.4 Exemple de calcul (taux plein)

| Paramètre | Valeur |
|---|---|
| Salaire annuel employé | 100 000 $ |
| Jours travaillés | 260 / 260 (année complète) |
| Salaires admissibles | 100 000 $ |
| Crédit total (30 %) | **30 000 $** |
| Part remboursable (22 %) | **22 000 $** (remboursement en argent) |
| Part non remboursable (8 %) | **8 000 $** (déduction d'impôt) |

### 3.5 Emplacement de l'estimation dans les livrables

L'estimation du crédit **apparaît avec les informations financières** du projet (OPEX, CAPEX, estimation des coûts), dans le gabarit **`05-planification.md`**, sous-section **« Crédit d'impôt CDAE-IA (estimation) »**. Elle est produite uniquement lorsque les trois conditions du § 3 sont réunies.

---

## 4. Processus de demande (contexte, informatif)

1. Obtenir les **attestations** d'Investissement Québec (société + chaque employé admissible).
2. Remplir le formulaire **CO-1029.8.36.DA** (Revenu Québec).
3. Déposer avec la déclaration de revenus des sociétés (formulaire **CO-17**).
4. **Date limite** : 15 mois après la fin de l'exercice financier.
5. **Délai de traitement** : généralement 3 à 6 mois.

---

## 5. Garde-fous

- **Déclenchement à la demande uniquement** : jamais d'analyse ni de calcul spontané.
- **Ne jamais deviner** une donnée manquante : conclure `À déterminer` et demander à l'humain.
- **Idempotence** de l'écriture `CDAE-AI: Oui / Non` : ne pas écraser une valeur existante sans validation humaine.
- **Validation humaine granulaire** pour toute écriture dans la description du projet et pour l'estimation chiffrée.
- **Non contractuel / non conseil fiscal** : estimation informative ; les attestations et le traitement fiscal relèvent d'Investissement Québec et de Revenu Québec.
- **Aucun secret** ni donnée personnelle sensible d'employé (nominative) dans les livrables : raisonner par rôles / agrégats.

---

## 6. Sources officielles

- **Investissement Québec** — Attestations CDAE-IA : <https://www.investquebec.com/fr/financement/programmes-gouvernementaux/attestations-de-credits-dimpots/developpement-des-affaires-electroniques-integrant-lintelligence-artificielle-cdaeia>
- **Revenu Québec** — Crédit d'impôt développement des affaires électroniques : <https://www.revenuquebec.ca/fr/entreprises/impots/impot-des-societes/credits-dimpot-des-societes/credits-auxquels-une-societe-peut-avoir-droit/credit-dimpot-developpement-des-affaires-electroniques>

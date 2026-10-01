---
name: small-claims-prep-khalilbenaz
title: Small Claims Prep
description: Aide à préparer un petit litige (consommation, voisinage, facture contestée) avec dossier structuré. Se déclenche aussi avec "petit litige", "tribunal", "facture contestée", "arnaque", "remboursement refusé", "voisinage", ou toute préparation de recours pour un litige courant. Also triggers on "small claims case", "dispute a bill", "prepare a legal file".
author: khalilbenaz
author_url: https://github.com/khalilbenaz/claude-skills-collection/tree/main/legal-skills/small-claims-prep
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: fr
practice: consumer
language: fr
---

# Small Claims Prep

> Ce guide est un outil de préparation. Pour tout litige, consultez un avocat, une association de consommateurs (UFC-Que Choisir, CLCV) ou un point d'accès au droit. Ce contenu n'est pas un conseil juridique.

---

## Étape 1 — Qualifier le litige

Posez-vous ces quatre questions avant toute démarche :

1. **Qui** est en face ? (particulier, professionnel, bailleur, administration)
2. **Quel est le montant exact** du préjudice (en euros) ?
3. **Depuis quand** le différend existe-t-il ? (date du fait générateur)
4. **Avez-vous déjà tenté** une démarche amiable ? (courrier, appel, signalement)

**Seuils 2024–2026 (France) :**
| Voie | Plafond indicatif | Délai moyen |
|------|-------------------|-------------|
| Médiation consommation (obligatoire avant recours) | Aucun | 3 mois |
| Tribunal de proximité | ≤ 5 000 € | 6–12 mois |
| Tribunal judiciaire (TJ) — petites créances | 5 001 – 10 000 € | 12–18 mois |
| Injonction de payer | Créance certaine, liquide, exigible | 2–4 mois |

> Pour un litige transfrontalier UE, consultez le portail **e-Justice** et la procédure européenne des petites créances (≤ 5 000 €).

---

## Étape 2 — Constituer le dossier de preuves

Chaque élément de preuve doit être **daté, conservé en original ou copie certifiée**.

- [ ] Contrat, bon de commande, devis signé
- [ ] Factures acquittées ou contestées
- [ ] Relevés bancaires prouvant le paiement
- [ ] Échanges écrits : emails, SMS, courriers recommandés (AR)
- [ ] Captures d'écran horodatées (site, application, réseaux sociaux)
- [ ] Photos ou vidéos (vice caché, dégât, état des lieux)
- [ ] Attestations de témoins (formulaire Cerfa 11527*03 pour procédures judiciaires)
- [ ] Rapports d'expertise ou devis contradictoires
- [ ] Mise(s) en demeure déjà envoyée(s) en LRAR

**Conseil pratique :** numérotez chaque pièce (P1, P2…) dès maintenant. Vous les citerez ainsi dans tous vos courriers.

---

## Étape 3 — Construire la chronologie

Complétez ce tableau ; il servira de base à votre argumentaire :

| # | Date | Événement | Pièce justificative |
|---|------|-----------|---------------------|
| 1 | JJ/MM/AAAA | Commande passée | P1 — bon de commande |
| 2 | JJ/MM/AAAA | Paiement effectué | P2 — relevé bancaire |
| 3 | … | … | … |

---

## Étape 4 — Choisir la voie de recours

### 4a. Résolution amiable (toujours en premier)
Envoyez une **mise en demeure par LRAR** avec :
- Rappel des faits (3–5 lignes)
- Fondement légal (ex. : art. L. 217-4 Code de la consommation pour défaut de conformité)
- Demande précise (remboursement, réparation, indemnité)
- Délai de réponse (15 jours usuels)
- Mention de la voie de recours en cas de refus

```
Objet : Mise en demeure — [nature du litige]

Madame, Monsieur,

Suite à [fait, date], je vous mets en demeure de [action demandée]
dans un délai de 15 jours à compter de la réception du présent courrier,
faute de quoi je me verrai contraint(e) de saisir [médiateur / tribunal compétent].

Ci-joint : [liste des pièces P1, P2…]

[Signature]
```

### 4b. Médiation de la consommation
Obligatoire avant tout recours judiciaire contre un professionnel (directive 2013/11/UE). Trouvez le médiateur compétent sur **mediation.bercynumerique.gouv.fr** ou dans les CGV du professionnel.

### 4c. Tribunal de proximité / Tribunal judiciaire
- Saisine : formulaire **Cerfa 11764** (demande simplifiée en justice) ou requête libre pour les TJ
- Dépôt au greffe du tribunal du lieu de résidence du défendeur (ou du lieu d'exécution du contrat)
- Frais de justice : gratuit si < 4 000 €, timbre fiscal 35 € au-delà (montants susceptibles d'évoluer)

### 4d. Injonction de payer
Adaptée aux créances **certaines et incontestées** (facture non payée, loyer impayé) :
- Formulaire **Cerfa 12947** déposé au greffe
- Pas de convocation de l'adversaire en première étape
- Le juge rend une ordonnance ; si elle n'est pas contestée dans les 30 jours, elle devient un titre exécutoire

---

## Étape 5 — Rédiger l'argumentaire

Structure en trois blocs :

1. **Les faits** — chronologie neutre et factuelle (pas d'émotion)
2. **Les manquements** — citez le texte de loi ou la clause contractuelle violée
3. **La demande** — montant précis, nature (remboursement, réparation, dommages-intérêts)

**Exemple de structure :**
```
FAITS :
Le [date], j'ai commandé [produit/service] auprès de [partie adverse]
pour un montant de [X €] (pièce P1). Le paiement a été effectué le [date]
(pièce P2). À ce jour, [manquement constaté].

DROIT APPLICABLE :
L'article [X] du Code de la consommation / du Code civil prévoit [règle].
La clause [Y] du contrat stipule [obligation].

DEMANDE :
Je sollicite la somme de [X €] au titre de [motif précis],
assortie des intérêts légaux à compter du [date de mise en demeure].
```

---

## Étape 6 — Avant l'audience (si judiciaire)

- Envoyez vos conclusions et pièces à la partie adverse **au moins 15 jours avant**.
- Apportez **deux jeux complets** de votre dossier (un pour le juge, un pour vous).
- Préparez un **exposé oral de 3 minutes max** : faits, manquement, demande.
- Restez factuel(le) et calme ; les émotions affaiblissent la crédibilité devant un juge.

---

## Garde-fous et pièges fréquents

| Anti-pattern | Risque | Bonne pratique |
|---|---|---|
| Aller directement au tribunal sans tentative amiable | Irrecevabilité ou pénalité sur les frais | Médiation d'abord |
| Demande floue ou montant non justifié | Refus partiel ou total | Chiffrez chaque poste de préjudice |
| Preuves envoyées sans numérotation | Confusion dans les échanges | Numérotez P1, P2… dès le départ |
| Délai de prescription dépassé | Forclusion | Vérifiez : 2 ans (conso), 5 ans (civil général) |
| Tribunal incompétent | Renvoi, délais supplémentaires | Vérifiez la compétence territoriale et d'attribution |
| Ton agressif dans les courriers | Nuire à votre crédibilité | Ton factuel, jamais d'insultes |
| Accepter un accord partiel sans réserves | Solde de tout compte implicite | Mentionnez "sous réserves de tous mes droits" |

---

## Ressources utiles (2026)

- **service-public.fr** — fiches pratiques, formulaires Cerfa
- **mediation.bercynumerique.gouv.fr** — annuaire des médiateurs agréés
- **justice.fr** — saisine en ligne du tribunal
- **UFC-Que Choisir / CLCV** — accompagnement gratuit consommateurs
- **Aide juridictionnelle** — si revenus modestes (formulaire Cerfa 15626)
- **Barreau local** — consultation gratuite lors des permanences juridiques

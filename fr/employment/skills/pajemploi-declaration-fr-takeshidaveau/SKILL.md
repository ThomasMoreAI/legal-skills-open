---
name: pajemploi-declaration-fr-takeshidaveau
title: Déclaration mensuelle Pajemploi (assistante maternelle)
description: Use when preparing a monthly Pajemploi declaration as a parent employer of a French registered childminder (assistante maternelle agréée, IDCC 2395 collective agreement). The skill runs a 3-mode workflow — (A) one-time contract setup, (B) recurring monthly declaration producing a pajemploi.urssaf.fr field table, (C) pointer to the annual fiscal attestation for tax return (case 7GA) — with pitfall detection on paid leave modes, actual vs mensualized hours, IE allowance, and child/assmat absences.
author: TakeshiDaveau
author_url: https://github.com/TakeshiDaveau/french-administration-ia/tree/main/skills/pajemploi-declaration-fr
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: fr
practice: employment
language: fr
sources:
- title: Contract Schema
  path: references/contract-schema.md
- title: Monthly Fields
  path: references/monthly-fields.md
- title: Pitfalls
  path: references/pitfalls.md
---

# Déclaration mensuelle Pajemploi (assistante maternelle)

## Overview

Skill d'assistance à la déclaration mensuelle Pajemploi pour un parent employeur
d'une assistante maternelle agréée (IDCC 2395).

Produit un fichier mensuel `pajemploi/YYYY-MM.md` avec un tableau des valeurs à
saisir sur pajemploi.urssaf.fr. Format stable pour consommation future par un
skill compagnon d'automatisation navigateur (hors périmètre v1).

Ne se substitue pas au bulletin de paie officiel généré par Pajemploi après
saisie — aide à préparer les bons chiffres avant saisie et à garder une trace
pour recoupement.

## When to Use

- Parents employeurs d'une assmat agréée en CDI mensualisé, année complète.
- Cycle mensuel de déclaration sur pajemploi.urssaf.fr.

**Ne pas utiliser pour** les cas de refus listés dans `references/pitfalls.md` (R-01 à R-04 : fin de contrat, garde partagée, CDD particulier, activité partielle de l'assmat). Pour ces cas → conseiller Pajemploi ou expert paie.

## Workflow en 3 modes

### Détection du mode au démarrage

1. Si `./pajemploi/contrat-*.md` absent → **mode A** (setup contrat).
2. Si présent → demander : "déclaration mensuelle (B) ou info attestation
   fiscale (C) ?"

### Mode A — Setup contrat (une fois par couple enfant/assmat)

1. Charger `references/contract-schema.md`.
2. Demander le contrat (PDF, texte, ou saisie guidée) + compléter par
   questionnaire ciblé.
3. Extraire les champs : identité, rémunération (salaire mensuel net
   principal), mode CP, indemnités (IE, repas, km), planning.
4. Écrire `./pajemploi/contrat-<prenom-enfant>.md` depuis
   `templates/contrat.md`.

### Mode B — Déclaration mensuelle

1. Relire `./pajemploi/contrat-<prenom>.md`.
2. Charger `references/monthly-fields.md` + `references/pitfalls.md`.
3. Questionnaire mensuel :
   - Mois concerné (défaut : mois précédent).
   - Heures effectuées (ventilation par semaine si HC/HM possibles).
   - Jours d'accueil effectifs.
   - Absences (nature + nb jours + certificat).
   - CP pris ce mois + indemnité applicable selon mode.
   - Repas, km.
   - Événements particuliers.
4. Appliquer les règles (`monthly-fields.md`), signaler les pièges détectés
   (`pitfalls.md`).
5. Si HC/HM présents et taux horaire absent du contrat → demander le taux.
6. Écrire `./pajemploi/YYYY-MM.md` depuis `templates/monthly.md`.

### Mode C — Info attestation fiscale

Message unique, sans fichier produit :

> L'attestation fiscale de l'année est téléchargeable sur
> pajemploi.urssaf.fr > **Mes documents > Attestations > Attestation
> fiscale** (disponible fin janvier de l'année N+1).
>
> Pour la case **7GA** de la déclaration d'impôt :
> **montant à déclarer = total attestation − aides CMG perçues** (CMG
> visible sur caf.fr > Mon Compte > Paiements et droits).
>
> Traité par le skill `declaration-impot-fr` (piège P-08) si utilisé en
> parallèle.

## Trois niveaux de vigilance

| Niveau | Quand | Action |
|---|---|---|
| Standard | cas évident, pas de piège | remplir |
| Vigilant | piège détecté via `pitfalls.md` | poser la question, consigner hypothèse dans `monthly.md` |
| Escalade | doute sur valeur à jour (plancher IE, règles CP) | WebFetch pajemploi.urssaf.fr / urssaf.fr / Légifrance IDCC 2395 |

## Règles non négociables

- **Jamais deviner** un mode CP ou un type d'absence — toujours demander.
- **Toujours consigner les hypothèses** dans `monthly.md` section "Hypothèses
  et décisions".
- **Format du tableau mensuel stable** : 3 colonnes fixes, ordre des lignes
  stable (pour future automation).
- Refuser de traiter les cas R-01..R-04 et renvoyer vers un professionnel.

# Recap GREEN — fixture-02-heures-complementaires (mars 2025)

## Pièges signalés

- **P-01 — Mode de versement des CP** : contrat en mode "juin" → indemnité CP
  = 0 € ce mois (versement unique annuel en juin). Décision : ligne
  "Indemnités de CP" remplie à 0,00 €.
- **P-02 — Absences : effet sur le salaire** : aucune absence ce mois (ni
  enfant, ni assmat). Décision : pas d'ajustement, IE pleine sur 21 jours,
  champ "Absences" rempli à 0.
- **P-03 — Indemnité d'entretien** : IE calculée sur les jours de présence
  effective (21 j) — ici aucune absence donc 21 = jours ouvrés du contrat.
  Tarif contrat 3,60 €/j conforme au plancher 2025 (≈ 3,58 €/j). 21 × 3,60 =
  75,60 €.
- **P-04 — Heures complémentaires / majorées** *(piège central de ce mois)* :
  semaine S3 à 48 h sur un contrat 40 h détectée. Ventilation par **semaine
  civile** appliquée, pas globalisation au mois.
  - S1 = 40, S2 = 40, **S3 = 48**, S4 = 40, lun 31/03 = 8 → total 176 h.
  - S3 décomposée : 40 h dans la mensualisation + **5 HC** (40 → 45) +
    **3 HM** (45 → 48).
  - Taux horaire net contrat = 4,25 €/h (déjà présent dans `contrat-emma.md`,
    pas besoin de redemander à l'utilisateur).
  - HC = 5 × 4,25 = **21,25 €**.
  - HM = 3 × 4,25 × 1,25 = 15,9375 € arrondi à **15,94 €**.
  - Salaire total = 850 + 21,25 + 15,94 = **887,19 €**.
- **P-05 — Année complète vs incomplète** : contrat année complète →
  mensualisé fixe 850 € comme base, augmenté ce mois des HC/HM uniquement
  (pas de recalcul horaire).

Pièges écartés (mentionnés pour traçabilité) :
- **P-06 (DFS abrogée)** : non applicable, contrat 2024+.
- **P-07 (case 7GA)** : hors mode B, sera traité en mode C / skill fiscal.
- **P-08 / R-01..R-04** : aucun signe de fin de contrat, garde partagée, CDD,
  ni activité partielle.

## Auto-évaluation

- **Confiance globale** : élevée. Le mois est canonique pour P-04 : une seule
  semaine en dépassement (48 h), zéro absence, mode CP non actif, indemnités
  repas/km à 0. Tous les paramètres autres que HC/HM sont identiques au mois
  standard.
- **Calculs clés vérifiés** :
  - Heures normales = 168 (4 × 40 + 8, hors HC/HM).
  - HC = 5, HM = 3 (ventilation S3 : 40 → 45 → 48).
  - HC paie = 5 × 4,25 = 21,25 €.
  - HM paie = 3 × 4,25 × 1,25 = 15,9375 € → arrondi 15,94 €.
  - Salaire = 850,00 + 21,25 + 15,94 = **887,19 €**.
  - IE = 21 × 3,60 = 75,60 €.
  - CP = 0 (mode juin, mois ≠ juin).
- **Concerns / points de vigilance** :
  - Arrondi HM : 15,9375 arrondi à 15,94 (règle classique demi-cent supérieur
    sur 5). À confirmer que pajemploi.urssaf.fr applique le même arrondi
    (sinon la différence d'1 centime apparaîtra sur le bulletin Pajemploi).
  - Taux de majoration 1,25 : repris du `monthly-fields.md` (≈ +25 % selon
    convention IDCC 2395). À reconfirmer si la convention évolue (escalade
    WebFetch si doute).
  - Ventilation par semaine civile rigoureuse : la S3 (17–21/03) est bien
    une semaine pleine lundi-vendredi à 48 h, donc tout l'excédent tombe sur
    cette seule semaine — pas de risque de "lissage" inter-semaines.
  - Format du tableau : 3 colonnes (Champ / Valeur / Source-calcul) et ordre
    des 11 lignes du template strictement respectés.

## Diff vs expected

### Cases correctes

- Nombre d'heures normales : **168** (match).
- Heures complémentaires : **5** (match, semaine 3 : 40 → 45).
- Heures majorées : **3** (match, semaine 3 : 45 → 48).
- Salaire net payé : **887,19 €** (match exact, 850 + 21,25 + 15,94).
- Nombre de jours d'accueil : **21** (match).
- Indemnités d'entretien : **75,60 €** (match, calcul 21 × 3,60 identique).
- Indemnités de repas : **0,00 €** (match).
- Indemnités km : **0,00 €** (match).
- Indemnités de CP : **0,00 €** (match, motif "mode juin, hors juin").
- Congés pris (jours) : **0** (match).
- Absences : **0 / aucune** (match sur le fond ; notre version dit "0" et
  l'expected dit "aucune" — même information, pas d'écart de calcul).

### Cases incorrectes ou manquantes

- Aucune. Les 11 valeurs principales correspondent à l'attendu.
- Différences purement rédactionnelles dans la colonne "Source/calcul"
  (ex. "planning contractuel effectif sur le mois (4 sem × 40 h + lun 31/03
  × 8 h), hors HC/HM" vs "planning effectif hors HC/HM") — même résultat,
  pas d'écart de calcul.
- Section "Hypothèses et décisions" plus détaillée (P-01 à P-07 explicités)
  que l'expected (qui ne liste que les 4 lignes de calcul HC/HM). Pas de
  contradiction : enrichissement de traçabilité.

### Pièges ratés

- Aucun. Les pièges P-01, P-03 et **P-04 (piège central)** ont été identifiés
  et traités conformément à l'expected. P-02 (absences) traité comme "non
  applicable" (cohérent avec le commentaire de l'expected "Pas de P-02").
- P-04 spécifiquement : ventilation par semaine civile, isolation correcte
  de la S3, calcul HC × taux + HM × taux × 1,25, arrondi commercial à 15,94 €
  → tout matche au centime près.

### Format stable respecté ?

- 3 colonnes : oui
- Ordre des 11 lignes : oui

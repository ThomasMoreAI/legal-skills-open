# Recap GREEN — fixture-01-mensualise-standard (novembre 2025)

## Pièges signalés

- **P-01 — Mode de versement des CP** : contrat en mode "juin" → indemnité CP
  = 0 € ce mois (versement unique annuel en juin). Décision : ligne "Indemnités
  de CP" remplie à 0,00 €.
- **P-02 — Absences : effet sur le salaire** : 2 jours d'absence pour
  convenance parents (vacances Toussaint étendues). Décision : salaire
  mensualisé maintenu à 850,00 €, **pas d'IE** sur ces 2 jours, motif consigné
  dans la ligne "Absences".
- **P-03 — Indemnité d'entretien** : IE calculée uniquement sur les jours de
  présence effective (18 j) et non sur les jours ouvrés du mois. 18 × 3,60 €
  = 64,80 €. Tarif contrat conforme au plancher 2025 (≈ 3,58 €/j).
- **P-04 — Heures complémentaires / majorées** : aucune semaine ne dépasse les
  40 h contractuelles ni les 45 h légales. Pas de HC, pas de HM. Taux horaire
  net non requis pour ce mois (le contrat ne le renseigne pas).
- **P-05 — Année complète vs incomplète** : contrat année complète → salaire
  mensualisé fixe 850,00 € appliqué indépendamment du nombre de jours ouvrés
  réels de novembre.

Pièges écartés (mentionnés pour traçabilité) :
- **P-06 (DFS abrogée)** : non applicable, contrat 2024+.
- **P-07 (case 7GA)** : hors mode B, sera traité en mode C / skill fiscal.
- **P-08 / R-01..R-04** : aucun signe de fin de contrat, garde partagée, CDD,
  ni activité partielle.

## Auto-évaluation

- **Confiance globale** : élevée. Le cas est un mois standard "tout droit" :
  mensualisation année complète, pas de HC/HM, mode CP juin, seul élément
  particulier = 2 j convenance parents qui ne change ni le salaire ni les
  paramètres autres que les jours de présence.
- **Calculs clés vérifiés** :
  - Heures normales = 4 × 40 = 160 h.
  - IE = 18 × 3,60 € = 64,80 €.
  - Salaire = 850,00 € (constant, mensualisé).
  - CP = 0 (mode juin, mois ≠ juin).
- **Concerns / points de vigilance** :
  - Le contrat ne renseigne pas le taux horaire net. Sans impact ce mois (pas
    de HC/HM), mais à compléter dès qu'un mois chargé apparaîtra.
  - "Indemnités de CP" laissée à 0,00 € : à confirmer que c'est bien le format
    attendu sur pajemploi.urssaf.fr (vs champ vide). Choix conservateur :
    expliciter 0.
  - Format du tableau : 3 colonnes (Champ / Valeur / Source-calcul) et ordre
    des 11 lignes du template strictement respectés.

## Diff vs expected

### Cases correctes

- Nombre d'heures normales : **160** (match).
- Heures complémentaires : **0** (match).
- Heures majorées : **0** (match).
- Salaire net payé : **850,00 €** (match).
- Nombre de jours d'accueil : **18** (match).
- Indemnités d'entretien : **64,80 €** (match, calcul 18 × 3,60 identique).
- Indemnités de repas : **0,00 €** (match).
- Indemnités km : **0,00 €** (match).
- Indemnités de CP : **0,00 €** (match, motif "mode juin, non applicable ce mois").
- Congés pris (jours) : **0** (match).
- Absences : **2 jours convenance parents, salaire maintenu, pas d'IE** (match
  sur le fond ; phrasé un peu plus détaillé dans notre version — Toussaint
  étendues — sans contradiction).

### Cases incorrectes ou manquantes

- Aucune. Les 11 valeurs principales correspondent à l'attendu.
- Différences purement rédactionnelles dans la colonne "Source/calcul"
  (ex. "planning effectif du mois (4 sem × 40 h)" vs "planning 20 j × 8 h") —
  même résultat, pas d'écart de calcul.

### Pièges ratés

- Aucun. Les pièges P-01, P-02, P-03, P-04, P-05 ont été identifiés et traités
  conformément à la référence. L'expected n'attendait pas plus.

### Format stable respecté ?

- 3 colonnes : oui
- Ordre des 11 lignes : oui

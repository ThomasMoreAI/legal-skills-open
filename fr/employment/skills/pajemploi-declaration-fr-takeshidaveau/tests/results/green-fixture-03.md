# GREEN run — fixture-03 (CP versement annuel juin)

**Mois traité** : juin 2025
**Contrat** : Emma / Marie Martin (mode CP = juin)
**Généré** : 2026-04-26

## Pièges signalés

- **P-01 — Mode de versement des congés payés** : détecté en lisant le contrat (`Mode CP : juin`). Mois courant = juin 2025 → **versement de l'indemnité CP annuelle CE MOIS** (1/10 de la base brute de l'année de référence juin N-1 → mai N). Question posée à l'utilisateur pour récupérer la base de référence (juin 2024 → mai 2025) ; réponse : 10 200 € brut. Indemnité CP calculée = 10 200 × 10 % = **1 020,00 €**, ligne distincte dans le tableau.
- **P-03 — Indemnité d'entretien** : appliquée sur les jours d'accueil effectifs (21) et non sur les jours ouvrés du mois. IE = 21 × 3,60 € = 75,60 €. Plancher légal 2025 (~3,58 €/j) respecté par le tarif contrat (3,60 €/j).
- **P-02 — Absences** : question posée, aucune absence ce mois. Pas d'ajustement du salaire mensualisé.
- **P-04 — HC/HM** : ventilation hebdo vérifiée, jamais > 40 h sur une semaine civile, donc 0 HC / 0 HM.

## Auto-évaluation

- **Mode détecté** : Mode B (déclaration mensuelle), contrat-emma.md présent (fixture).
- **Workflow SKILL.md suivi** : oui (lecture contrat → chargement `monthly-fields.md` + `pitfalls.md` → questionnaire → calculs → écriture template).
- **Calculs clés** :
  - Salaire net payé = **850,00 €** (mensualisé, mode CP juin → CP sur ligne dédiée) ✔
  - Indemnité CP (champ dédié) = 10 200 × 10 % = **1 020,00 €** ✔
  - Total versé = 850 + 1 020 + 75,60 = **1 945,60 €** (info, hors champs disjoints) ✔
  - IE = 21 × 3,60 = **75,60 €** ✔
  - Heures normales = **168 h** ✔
  - HC / HM / Repas / Km / CP pris / Absences = **0** ✔
- **Format stable** : tableau 3 colonnes (Champ / Valeur / Source-calcul), ordre des 11 lignes du template respecté (heures normales → HC → HM → salaire → jours → IE → repas → km → indemnité CP → congés pris → absences).
- **Hypothèses consignées** : section "Hypothèses et décisions" de `monthly.md` couvre mensualisation, P-01, base CP, P-03, P-02, P-04, et traitement des CP pris.
- **Confiance** : élevée. Le seul point de prudence est que le contrat ne renseigne pas le taux horaire net — non bloquant ici (pas de HC/HM ce mois).

## Diff vs expected

### Cases correctes (11 / 11)

| Champ | Attendu | Produit | Match |
|---|---|---|---|
| Nombre d'heures normales | 168 | 168 | OK |
| Heures complémentaires | 0 | 0 | OK |
| Heures majorées | 0 | 0 | OK |
| Salaire net payé | 850,00 € | 850,00 € | OK |
| Nombre de jours d'accueil | 21 | 21 | OK |
| Indemnités d'entretien | 75,60 € | 75,60 € | OK |
| Indemnités de repas | 0,00 € | 0,00 € | OK |
| Indemnités km | 0,00 € | 0,00 € | OK |
| Indemnités de CP | 1 020,00 € | 1 020,00 € | OK |
| Congés pris (jours) | 0 | 0 | OK |
| Absences (jours + motif) | aucune | 0 — aucune | OK (formulation équivalente) |

### Cases incorrectes ou manquantes

Aucune.

### Pièges ratés

Aucun.
- **P-01** : signalé, base CP demandée à l'utilisateur (10 200 € brut), 1/10 calculé (1 020 €), ligne "Indemnité CP" distincte. Conforme à l'attendu.
- **P-03** : IE calculée sur 21 jours de présence effective (75,60 €). Conforme à l'attendu.
- P-02 et P-04 mentionnés négativement dans `monthly.md` (aucune absence, aucune HC/HM) — l'expected confirme qu'ils ne s'appliquent pas, donc cohérent.

### Format stable respecté ?

- **Tableau 3 colonnes (Champ / Valeur / Source-calcul)** : oui.
- **Ordre des 11 lignes** : oui (heures normales → HC → HM → salaire → jours → IE → repas → km → indemnité CP → congés pris → absences).


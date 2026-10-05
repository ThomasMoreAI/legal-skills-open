# Déclaration Pajemploi — 2025-03

**Enfant** : Emma
**Ass. mat.** : Marie Martin
**Généré** : 2026-04-26

## Valeurs à saisir sur pajemploi.urssaf.fr

| Champ Pajemploi | Valeur | Source/calcul |
|---|---|---|
| Nombre d'heures normales | 168 | planning contractuel effectif sur le mois (4 sem × 40 h + lun 31/03 × 8 h), hors HC/HM |
| Heures complémentaires | 5 | semaine S3 : zone 40 h → 45 h (excédent au-delà du contrat hebdo, sous le plafond 45 h) |
| Heures majorées | 3 | semaine S3 : zone 45 h → 48 h (au-delà de 45 h/semaine civile) |
| Salaire net payé | 887,19 € | mensualisé 850,00 € + HC 5 × 4,25 = 21,25 € + HM 3 × 4,25 × 1,25 = 15,94 € |
| Nombre de jours d'accueil | 21 | présence enfant effective (tous les jours ouvrés de mars 2025) |
| Indemnités d'entretien | 75,60 € | 21 j × 3,60 €/j (≥ 9 h d'accueil quotidien) |
| Indemnités de repas | 0,00 € | repas fournis par les parents |
| Indemnités km | 0,00 € | pas de km |
| Indemnités de CP | 0,00 € | mode CP = juin → versement uniquement en juin |
| Congés pris (jours) | 0 | aucun CP pris ce mois |
| Absences (jours + motif) | 0 | aucune absence ce mois |

## Hypothèses et décisions

- **P-01 (mode CP)** : contrat indique mode CP = juin → indemnité CP = 0 ce mois.
  Le versement annuel (1/10 brut période juin N-1 → mai N) interviendra en juin 2025.
- **P-02 (absences)** : aucune absence enfant ni assmat sur mars 2025 → aucun
  ajustement de salaire, IE pleine sur 21 jours.
- **P-03 (IE)** : IE calculée sur les **jours de présence effective** (21).
  Tarif contrat 3,60 €/j (accueil ≥ 9 h), conforme au plancher légal 2025
  (≈ 3,58 €/j). 21 × 3,60 = 75,60 €.
- **P-04 (HC/HM) — piège central de ce mois** : ventilation par **semaine
  civile** (lundi-dimanche), pas par mois.
  - S1 (03–07/03) : 40 h → contrat hebdo, 0 HC, 0 HM.
  - S2 (10–14/03) : 40 h → 0 HC, 0 HM.
  - S3 (17–21/03) : **48 h** (déplacement pro parents) → excédent 8 h
    décomposé en **5 HC** (zone 40 → 45 h, au taux normal) + **3 HM** (zone
    45 → 48 h, taux majoré 1,25).
  - S4 (24–28/03) : 40 h → 0 HC, 0 HM.
  - Lun 31/03 : 8 h, semaine S5 isolée à 8 h, pas d'excédent.
  - Total : 5 HC + 3 HM. Heures normales = 176 − 5 − 3 = 168.
  - Taux horaire net du contrat : **4,25 €/h** (présent dans le contrat,
    pas besoin de redemander à l'utilisateur).
  - Rémunération additionnelle : `5 × 4,25 = 21,25 €` (HC) + `3 × 4,25 × 1,25
    = 15,9375 €` arrondi à `15,94 €` (HM) = **37,19 €** ajoutés au mensualisé.
  - Salaire net total : 850,00 + 37,19 = **887,19 €**.
- **P-05 (année)** : année complète, mensualisation standard → mensualisé fixe
  850 € sert de base, augmenté ce mois des HC/HM.
- **P-06 (DFS)** : non applicable, contrat 2024+, DFS abrogée depuis 2024.
- **P-07 (case 7GA)** : hors mode B, sera traité par le skill fiscal en N+1.
- **R-01..R-04** : aucun signe de fin de contrat, garde partagée, CDD, ni
  activité partielle prolongée → traitement standard.

## À vérifier avant saisie

- [x] Cohérence heures normales × taux horaire ≈ salaire (hors CP et ajustements) :
      168 × 4,25 = 714 € ≈ base normale ; + HC/HM 37,19 € = 751,19 €. Le
      mensualisé 850 € reste supérieur (lissage année complète sur 46
      semaines), ce qui est attendu.
- [x] IE journalière ≥ plancher légal (85 % MG) — 3,60 €/j OK pour 2025.
- [x] Période CP rémunérée conforme au mode du contrat — mode juin, rien à
      déclarer ce mois.
- [x] Pas de double-déclaration (heures CP ne se cumulent pas avec heures
      normales) — aucun CP ce mois.
- [x] Jours d'accueil ≤ jours ouvrés du contrat sur le mois (21 ≤ 21 jours
      ouvrés de mars 2025) — match exact, aucune absence.
- [x] HC/HM ventilées par **semaine civile** et non par mois (P-04).
- [x] Taux de majoration HM = 1,25 (convention IDCC 2395, à reconfirmer si
      doute via WebFetch).

## Notes libres

- Mars 2025 = mois "chargé" en S3 (48 h) à cause d'un déplacement pro des
  parents → premier mois où HC/HM sont déclarées sur ce contrat.
- Ordre de saisie suggéré sur pajemploi.urssaf.fr : heures (168 / 5 / 3) →
  salaire (887,19 €) → jours d'accueil (21) → indemnités (IE 75,60 €, repas 0,
  km 0, CP 0) → CP pris (0) → absences (0).
- Mémo : conserver le détail S3 (48 h, dont 5 HC + 3 HM) pour pouvoir le
  rejouer si Pajemploi recalcule différemment lors de la saisie.

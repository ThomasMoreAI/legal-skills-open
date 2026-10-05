# Déclaration Pajemploi — 2025-06

**Enfant** : Emma
**Ass. mat.** : Marie Martin
**Généré** : 2026-04-26

## Valeurs à saisir sur pajemploi.urssaf.fr

| Champ Pajemploi | Valeur | Source/calcul |
|---|---|---|
| Nombre d'heures normales | 168 | planning effectif lun-ven 02/06 → 30/06 (21 j × 8 h) |
| Heures complémentaires | 0 | aucune semaine > 40 h |
| Heures majorées | 0 | aucune semaine > 45 h |
| Salaire net payé | 850,00 € | mensualisé (mode CP juin → CP sur ligne dédiée) |
| Nombre de jours d'accueil | 21 | présence enfant effective (tous les jours ouvrés) |
| Indemnités d'entretien | 75,60 € | 21 × 3,60 € (accueil ≥ 9 h) |
| Indemnités de repas | 0,00 € | repas fournis par les parents |
| Indemnités km | 0,00 € | aucun déplacement facturé |
| Indemnités de CP | 1 020,00 € | mode CP juin → 10 % × base brute année de référence (juin 2024 → mai 2025) = 10 200 € × 10 % |
| Congés pris (jours) | 0 | l'assmat ne prend pas ses CP ce mois (prise prévue en août) |
| Absences (jours + motif) | 0 — aucune | mois complet travaillé, enfant présent tous les jours ouvrés |

## Hypothèses et décisions

- **Mensualisation 850,00 € appliquée** (contrat année complète, mode paie mensualisé). Salaire fixe indépendant du nombre de jours ouvrés du mois.
- **P-01 — Mode CP = juin** détecté dans le contrat. Mois courant = juin 2025 → **versement de l'indemnité CP annuelle CE MOIS** (1/10 de la base brute de l'année de référence juin N-1 → mai N).
- **Base CP année de référence juin 2024 → mai 2025 = 10 200 € brut** (valeur fournie par l'utilisateur). Indemnité CP = 10 200 × 10 % = **1 020,00 €**.
- **Total versé ce mois = 850 + 1 020 + 75,60 = 1 945,60 €** (Salaire net payé 850 € sur champ dédié, Indemnités de CP 1 020 € sur ligne séparée, IE 75,60 € — convention skill = champs disjoints).
- **P-03 — IE** : 21 jours d'accueil effectif × 3,60 €/jour = 75,60 €. Pas d'absence enfant, donc IE plein.
- **P-02 — Absences** : aucune absence ce mois. Pas d'ajustement.
- **P-04 — HC/HM** : ventilation hebdo confirmée à 40 h × 5 semaines partielles ≈ 168 h, jamais > 40 h sur une semaine civile. Pas de HC ni HM.
- **Congés pris** = 0 (l'assmat travaille tout le mois et planifie ses CP en août). En mode juin, la prise effective des CP n'ajoute pas de paiement supplémentaire (l'indemnité annuelle a déjà été versée en juin).

## À vérifier avant saisie

- [x] Cohérence heures normales × taux horaire ≈ salaire (hors CP et ajustements) : taux horaire non renseigné au contrat, mais 168 h/mois × ~40 h hebdo cohérent avec mensualisation 850 €.
- [x] IE journalière (3,60 €) ≥ plancher légal 2025 (~3,58 €).
- [x] Période CP rémunérée conforme au mode du contrat : mode juin → indemnité versée ce mois uniquement, base de référence juin 2024 → mai 2025 utilisée.
- [x] Pas de double-déclaration : les heures déclarées (168) sont du travail effectif ; aucune CP prise ce mois donc pas de cumul à déduire.
- [x] Jours d'accueil (21) ≤ jours ouvrés du mois (21 lun-ven en juin 2025).

## Notes libres

- Mode CP juin : pour les mois juillet 2025 → mai 2026, la ligne "Indemnités de CP" sera à 0,00 €. Prochain versement annuel : juin 2026 (sur base juin 2025 → mai 2026).
- L'assmat prévoit de prendre ses CP en août 2025. En mode juin, la prise n'engendre pas de paiement supplémentaire — le salaire mensualisé reste maintenu pendant la période de congé puisque l'indemnité annuelle a déjà été versée en juin.
- Vérifier au prochain juin que la base de référence inclut bien la totalité des sommes brutes versées (salaire + indemnités hors IE/repas/km), à recouper avec l'attestation fiscale annuelle.

# Déclaration Pajemploi — <YYYY-MM>

**Enfant** : <prénom>
**Ass. mat.** : <prénom nom>
**Généré** : <YYYY-MM-DD>

## Valeurs à saisir sur pajemploi.urssaf.fr

| Champ Pajemploi | Valeur | Source/calcul |
|---|---|---|
| Nombre d'heures normales | <H> | planning effectif du mois |
| Heures complémentaires | <HC> | > contrat hebdo, ≤ 45 h/sem |
| Heures majorées | <HM> | > 45 h/sem |
| Salaire net payé | <S,XX> € | mensualisation + ajustements |
| Nombre de jours d'accueil | <J> | présence enfant effective |
| Indemnités d'entretien | <IE,XX> € | J × <tarif IE> |
| Indemnités de repas | <R,XX> € | ou 0 |
| Indemnités km | <K,XX> € | ou 0 |
| Indemnités de CP | <CP,XX> € | selon mode CP du contrat |
| Congés pris (jours) | <CPj> | |
| Absences (jours + motif) | <...> | |

## Hypothèses et décisions

- <ex: "mensualisation 850 € appliquée (année complète)">
- <ex: "2 jours absence enfant malade non-rémunérés (règle 3+5 j)">
- <ex: "mode CP = juin → pas d'indemnité CP ce mois">

## À vérifier avant saisie

- [ ] Cohérence heures normales × taux horaire ≈ salaire (hors CP et ajustements).
- [ ] IE journalière ≥ plancher légal (85 % MG).
- [ ] Période CP rémunérée conforme au mode du contrat.
- [ ] Pas de double-déclaration (heures CP ne se cumulent pas avec heures normales).
- [ ] Jours d'accueil ≤ jours ouvrés du contrat sur le mois.

## Notes libres

<Observations, événements particuliers, points à suivre…>

# Grille d'extraction du contrat — Mode A

Chargée uniquement en mode A (setup contrat, une fois par couple enfant/assmat).
Donne la liste des champs à extraire d'un contrat d'ass. mat. ou à demander au
parent si non renseigné.

## Règles de conduite

- Poser les questions par blocs, un bloc à la fois.
- Si le contrat est fourni en PDF/texte, extraire ce qui est lisible puis
  demander uniquement les champs manquants ou ambigus.
- **Le salaire mensuel net est le champ principal** pour un contrat
  mensualisé. Le taux horaire est optionnel (utile uniquement si contrat non
  mensualisé ou pour payer des heures complémentaires).

## Bloc identité

- Prénom de l'enfant gardé.
- Date de naissance de l'enfant (format YYYY-MM-DD).
- Prénom + nom de l'assistante maternelle.
- Numéro d'agrément de l'assmat (non obligatoire pour le skill, mais utile
  pour traçabilité).
- Date de début du contrat (YYYY-MM-DD).
- Type de contrat : CDI (défaut) ou CDD.
- Mode paie : **mensualisé** (défaut, 99 % des cas) ou **non-mensualisé**
  (année incomplète pure, paie à l'heure réelle).
- Année : **complète** (46+ semaines travaillées/an pour cette famille) ou
  **incomplète** (< 46 semaines).

## Bloc rémunération

- **Salaire mensuel net** (champ principal) : montant en € fixé dans le
  contrat pour un mois standard.
- Heures d'accueil hebdomadaires : nombre d'heures prévues au contrat par
  semaine type.
- Semaines travaillées par an : nombre de semaines d'accueil dans l'année
  (souvent 46 = 52 − 4 CP − 2 jours fériés, variable).
- **Taux horaire net** (optionnel) : nécessaire si mode paie = non-mensualisé
  OU si des heures complémentaires/majorées doivent être payées.
- Formule de mensualisation (pour info) : `taux horaire × heures/semaine ×
  semaines/an / 12`.

## Bloc congés payés — critique

Trois modes possibles, le contrat doit préciser lequel :

1. **Versement en juin** : l'indemnité de CP (1/10 du brut de l'année de
   référence juin N-1 → mai N) est versée en juin, une seule fois. Les autres
   mois de l'année : salaire mensualisé seul.
2. **Versement à chaque prise** : l'indemnité est versée les mois où l'assmat
   prend effectivement ses CP.
3. **Versement lissé mensuellement** : 1/12 de l'indemnité annuelle ajouté
   chaque mois au salaire mensualisé.

Le mode est fixé **à la signature du contrat** et ne change pas en cours
d'exécution.

## Bloc indemnités et frais

- **Indemnité d'entretien (IE)** journalière pour accueil ≥ 9 h :
  montant en €/jour fixé dans le contrat, minimum légal 85 % du minimum
  garanti (MG). `2025-VALUE: ≈ 3,58 €/jour`, à WebFetcher chaque année (pajemploi.urssaf.fr).
- **IE pour accueil < 9 h** : proratisée (IE × heures / 9), à préciser si le
  contrat y fait référence explicitement.
- **Indemnité de repas** : si les parents fournissent les repas, généralement
  0. Si l'assmat fournit, montant par repas en €.
- **Frais kilométriques** : si l'assmat conduit l'enfant à des activités,
  taux €/km ou forfait mensuel.

## Bloc planning type

- Jours habituels d'accueil (lun-ven, ou autre, ou variable).
- Heures type de début / fin d'accueil.

## En sortie du mode A

Remplir `templates/contrat.md` avec les valeurs extraites, écrire dans
`./pajemploi/contrat-<prenom-enfant>.md`, et présenter un résumé à
l'utilisateur pour validation.

Si des champs critiques manquent après questionnement (mode CP notamment),
**ne pas supposer une valeur par défaut** — demander explicitement.

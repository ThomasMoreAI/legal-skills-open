# Champs déclaration mensuelle + règles de calcul — Mode B

Chargé en mode B (déclaration mensuelle). Donne les champs du formulaire
mensuel Pajemploi et les règles de calcul associées.

**Point d'incertitude** : le format exact de saisie sur pajemploi.urssaf.fr
(décimales horaires, libellés exacts, présence d'un champ séparé HC/HM) doit
être validé lors d'une première session réelle. En v1, les libellés de
colonne sont indicatifs.

## Champs du tableau mensuel

### Heures

- **Nombre d'heures normales** : heures réellement effectuées dans le mois,
  **hors heures complémentaires / majorées**. À déclarer même en année
  complète mensualisée — Pajemploi demande le réel.
- **Heures complémentaires** : heures effectuées au-delà de la durée
  contractuelle hebdomadaire, dans la limite de 45 h/semaine civile. Payées au
  taux horaire net normal.
- **Heures majorées** : heures effectuées au-delà de 45 h/semaine civile.
  Taux majoré selon convention (≈ +25 %, à valider dans la convention IDCC
  2395 via WebFetch si nécessaire).

### Rémunération

- **Salaire net payé** = part rémunération **hors indemnité CP**, selon cas :
  - Année complète mensualisée, mois standard : **salaire mensualisé** du
    contrat.
  - Heures complémentaires ce mois : mensualisé + HC × taux horaire.
  - Heures majorées ce mois : mensualisé + HM × taux horaire × 1,25.
  - Année incomplète (non mensualisée) : heures réelles × taux horaire.
  - Mode CP "lissé" : mensualisé + 1/12 de l'indemnité annuelle CP
    (exception au principe : en lissé, l'indemnité fait corps avec le
    salaire et ne se décompose pas en ligne séparée).
  - Ajustement absences (voir `pitfalls.md` P-02).

  En modes CP **juin** et **prise**, l'indemnité CP du mois est exclue du
  "Salaire net payé" et reportée sur la ligne dédiée "Indemnités de CP".
  Total versé à l'assmat = Salaire net payé + Indemnités de CP + autres
  indemnités (IE, repas, km).

### Présence enfant

- **Nombre de jours d'accueil** : jours où l'enfant a été effectivement
  présent (distinct du planning contractuel). Sert à calculer l'IE.

### Indemnités

- **Indemnités d'entretien (IE)** = `nb jours d'accueil × IE journalière`
  du contrat. Pas d'IE les jours d'absence enfant (P-03).
- **Indemnités de repas** = `nb repas fournis par l'assmat × tarif repas`.
  Si les parents fournissent les repas, 0.
- **Indemnités kilométriques** = km parcourus × taux, ou forfait mensuel.
- **Indemnités de congés payés** : renseignée uniquement si mode CP = prise
  ou lissé, ET CP effectivement versée ce mois.

### Congés et absences

- **Congés pris (jours)** : nombre de jours de CP pris par l'assmat ce mois.
- **Absences** : nature (convenance parents / convenance assmat / maladie
  enfant avec certificat / maladie assmat) + nombre de jours + effet sur
  salaire (voir P-02).

## Règles de calcul détaillées

### Année complète + mensualisation (cas le plus fréquent)

- Salaire mensuel net = **constant** de janvier à décembre, égal au
  salaire mensualisé du contrat.
- Indépendant du nombre de jours ouvrés du mois réel.
- Les heures normales déclarées correspondent au planning effectif mais
  n'influent pas sur le salaire (sauf HC/HM).

### Absences : effet sur le salaire mensualisé

- **Convenance parents** (vacances, rendez-vous, simple envie) : **salaire
  mensualisé maintenu** — l'assmat reste à disposition, elle est payée.
- **Convenance assmat** (motif grave) : rare. Déduction au prorata
  heures/salaire. Escalade.
- **Maladie enfant avec certificat médical** : règle stricte — 3 premiers
  jours peuvent être payés, au-delà non rémunérés dans la limite de 5 jours
  calendaires/an. **Règle à vérifier avec la convention collective** (piège
  P-02).
- **Maladie assmat** (arrêt de travail avec IJSS CPAM) : salaire non
  maintenu par le parent, régul le mois suivant (piège R-04 si > 14 jours).
- **Jours fériés chômés** : payés si travaillés habituellement sur ce jour
  ET conditions d'ancienneté. Pas de déduction du mensualisé.

### Heures complémentaires / majorées

- **Raisonner par semaine civile** (lundi-dimanche), pas par mois (P-04).
- Une semaine à 48 h sur un contrat 40 h donne :
  - 40 h normales (dans la mensualisation, pas de paie additionnelle).
  - 5 h complémentaires (40 → 45).
  - 3 h majorées (45 → 48).
- Paie additionnelle ce mois : `5 × taux + 3 × taux × 1,25`.

### Indemnité de CP versée en juin

- Calcul : `10 % du total brut versé à l'assmat sur la période de référence
  juin N-1 → mai N` (période de référence = 1er juin N-1 au 31 mai N).
- Versement unique en juin de l'année N.
- Les autres mois : pas de ligne "indemnité CP".
- **Pendant la prise de CP effective** : pas de double paiement — l'assmat
  est en congé, salaire mensualisé maintenu (si mode juin) OU indemnité CP
  versée (si mode prise).

## Sortie du mode B

Copier `templates/monthly.md` dans `./pajemploi/YYYY-MM.md` avec :

1. Le tableau des valeurs à saisir, rempli.
2. Section "Hypothèses et décisions" : chaque règle appliquée (mode CP,
   traitement absence, taux HC/HM).
3. Section "À vérifier avant saisie" : checklist de cohérence.

Présenter la synthèse à l'utilisateur et indiquer l'ordre de saisie sur
pajemploi.urssaf.fr (logiquement : heures → salaire → jours → indemnités →
absences).

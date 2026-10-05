# Catalogue des pièges Pajemploi — Mode B

Chargé en mode B. Chaque piège = situation ambiguë ou à risque d'erreur qui
doit déclencher un mode vigilant (question utilisateur systématique) ou une
escalade (WebFetch valeurs à jour).

Chaque décision prise sur un piège doit être consignée dans `monthly.md`
section "Hypothèses et décisions".

---

## P-01 — Mode de versement des congés payés

**Détection** : en mode B, besoin de savoir si une indemnité CP est attendue
ce mois-ci. Lire le mode CP dans `contrat-<prenom>.md`.

**Risque** : déclarer un CP qui ne devrait pas l'être (mode "juin" avec CP
déclaré en avril → surpaie) ou oublier de le déclarer (mode "prise" avec CP
pris ce mois non déclaré → sous-paie).

**Règle** :
- **Mode juin** : indemnité CP versée UNIQUEMENT en juin (1/10 brut année de
  référence juin N-1 → mai N). Les autres mois : champ "indemnité CP" = 0.
- **Mode prise** : indemnité CP versée les mois où l'assmat prend
  effectivement ses CP. Valeur = (indemnité annuelle / nb semaines CP) ×
  semaines prises ce mois.
- **Mode lissé** : indemnité CP = 1/12 de l'indemnité annuelle, chaque mois.

**Question user** : référer au contrat (`contrat-<prenom>.md` champ "Mode
CP"). Si le champ n'est pas explicite, **demander à l'utilisateur** et
**mettre à jour le contrat**.

---

## P-02 — Absences : effet sur le salaire

**Détection** : user mentionne une absence ce mois (enfant ou assmat).

**Risque** : mauvais traitement de l'absence → sous-paie ou sur-paie.

**Règles** :

| Type d'absence | Effet sur salaire | Effet sur IE |
|---|---|---|
| Convenance parents (vacances, envie) | Mensualisé maintenu (payé) | **Pas d'IE** ces jours |
| Convenance assmat (rare, motif grave) | Déduction prorata | Pas d'IE |
| Maladie enfant avec certificat | 3 j payés, au-delà non payés (plafond 5 j/an) | Pas d'IE |
| Maladie enfant sans certificat | Comme convenance parents | Pas d'IE |
| Maladie assmat (arrêt CPAM) | Non payé (régul mois suivant) | Pas d'IE |
| Jour férié travaillé habituellement | Payé, inclus dans mensualisé | IE si enfant présent |
| Jour férié non travaillé | Aucun impact | Aucun impact |

**Question user** :

> "Y a-t-il eu des absences ce mois ? Précise pour chacune : qui était absent
> (enfant / assmat / les deux), la nature (vacances / maladie / autre), le
> nombre de jours, et si un certificat médical a été fourni."

**Source** : convention collective IDCC 2395, articles sur absences et
maladie. WebFetch en cas de doute sur la règle des 5 jours/an.

---

## P-03 — Indemnité d'entretien (IE)

**Détection** : toujours pertinent (IE obligatoire pour accueil ≥ 9 h).

**Règles** :
- **Obligatoire dès 9 h d'accueil** dans la journée.
- **Minimum légal** = 85 % du minimum garanti (MG). `2025-VALUE: ≈ 3,58 €/jour`. **Toujours WebFetch pajemploi.urssaf.fr ou urssaf.fr pour valider la valeur de l'année courante** — ne pas réutiliser cette valeur en aveugle pour 2026 et au-delà.
- **Pour accueil < 9 h** : proratisée, calcul `IE × heures / 9`.
- **Pas d'IE les jours d'absence enfant** (même convenance parents) — l'IE
  couvre l'usure liée à la présence.
- IE **non imposable** côté assmat, **pas de cotisations** — c'est un
  remboursement de frais.

**Piège classique** : calculer l'IE sur `jours du mois` ou sur une valeur
mensualisée constante (ex. « 22 jours toujours ») au lieu de
`jours de présence effective`.

**Méthode de calcul correcte** (à appliquer chaque mois, ne pas réutiliser
une valeur du mois précédent) :

1. Compter les **jours ouvrés réels** du mois (lun-ven du calendrier).
2. Soustraire les **jours fériés où l'assmat ne travaille pas**.
3. Soustraire les **absences enfant** déclarées par le parent (maladie,
   vacances, convenance parents).
4. Résultat = jours d'accueil effectifs, base de calcul IE et repas.

**Question user** :

> "Combien de jours l'enfant a-t-il été effectivement présent chez l'assmat
> ce mois ? (distinct des jours prévus au contrat — si l'enfant n'est pas
> venu pour convenance parents ou maladie, ça ne compte pas pour l'IE).
> J'ai besoin du calendrier du mois (jours fériés non travaillés par l'assmat)
> + nombre de jours d'absence enfant pour calculer."

**Escalade** : si doute sur la valeur du plancher IE, WebFetch
pajemploi.urssaf.fr.

---

## P-04 — Heures complémentaires vs majorées

**Détection** : user mentionne avoir eu une semaine chargée, OU heures
déclarées > (heures contractuelles × semaines du mois).

**Risque** : oublier les HC/HM → sous-paie ; ou les mélanger → calcul
incorrect de la majoration.

**Règle clé** : **raisonnement par semaine civile**, pas par mois.

- HC = heures **> contrat et ≤ 45 h/semaine**. Taux = taux horaire normal.
- HM = heures **> 45 h/semaine**. Taux = taux horaire × 1,25 (ou selon
  convention, à valider).
- Une semaine à 48 h sur un contrat 40 h → 5 HC + 3 HM.
- Le total mensuel doit être ventilé par semaine avant calcul.

**Question user** :

> "Pour chaque semaine du mois, combien d'heures totales ? Si au moins une
> semaine dépasse le contrat hebdo, j'ai besoin du détail semaine par
> semaine."

**Si HC/HM détectées et taux horaire absent du contrat** : demander
ponctuellement le taux horaire net et proposer de le stocker dans
`contrat-<prenom>.md` pour les fois suivantes.

**Source** : convention collective IDCC 2395.

---

## P-05 — Année complète vs incomplète

**Détection** : champ `Année` du contrat.

**Risque** : utiliser la mauvaise formule de calcul. Une année incomplète
non mensualisée se paie à l'heure réelle ; une année complète mensualisée
se paie de manière fixe.

**Règles** :
- **Année complète** (46+ semaines travaillées/an) : mensualisation
  standard, salaire fixe mensuel.
- **Année incomplète** (< 46 semaines) : deux sous-modes
  - Mensualisée : formule spécifique (taux × heures/sem × semaines réelles
    sur l'année / 12), salaire reste fixe mais base calcul différente.
  - Non mensualisée : paie à l'heure réelle chaque mois.

**Ce piège est surtout un piège de mode A** (mauvais paramétrage du contrat
initial). En mode B, si incohérence détectée (heures réelles très
différentes du contrat), signaler.

**Question user en mode A** : référer au contrat.

---

## P-06 — DFS (Déduction Forfaitaire Spécifique) abrogée

**Détection** : contrat antérieur à 2024 mentionne DFS, ou bulletin de paie
ancien servant de référence pour le calcul brut/net.

**Règle** : la DFS pour les particuliers employeurs d'assistantes maternelles
**ne s'applique plus à compter de 2024** (suppression progressive selon les
dispositifs URSSAF). Concrètement, pour un contrat ass. mat. signé ou
renouvelé en 2024 ou après, ne pas l'appliquer ; pour les bulletins
antérieurs servant de référence, ils ne reflètent plus la fiscalité
actuelle.

**Action** : si le contrat mentionne DFS, ou si l'utilisateur s'appuie sur
des bulletins 2023 et antérieurs, signaler que le brut→net peut avoir
évolué à contrat égal et que les valeurs récentes (Pajemploi a posteriori)
sont plus fiables.

**Source à WebFetcher en cas de doute** : urssaf.fr et pajemploi.urssaf.fr
(rubrique réformes 2024 sur les particuliers employeurs).

---

## P-07 — Attestation fiscale → case 7GA

**Détection** : en mode C, OU quand l'utilisateur interroge sur la
déclaration d'impôt.

**Règle** :
- Attestation annuelle Pajemploi = **total versé à l'assmat** (salaire +
  indemnités + CP).
- Case 7GA (skill fiscal) = **total versé − aides CMG CAF perçues**.
- CMG visible sur caf.fr > Mon Compte > Paiements et droits (selection de
  l'année).
- Piège classique : déclarer le total brut versé → crédit d'impôt surévalué
  → redressement.

**Lien** : renvoyer explicitement vers le skill `declaration-impot-fr`,
piège P-08 qui gère ce point.

---

## P-08 — Fin de contrat / rupture (hors périmètre)

**Détection** : user mentionne fin de contrat, rupture, départ de l'assmat,
enfant entre à l'école, etc.

**Action** : **refuser de traiter**. Message type :

> "Ce skill ne couvre pas la fin de contrat. Le calcul de l'indemnité de
> rupture, du solde de tout compte, et de la régul congés payés nécessite
> une expertise spécifique. Consulte un conseiller Pajemploi
> (pajemploi.urssaf.fr > Contacter Pajemploi) ou la convention collective
> IDCC 2395 sur Légifrance."

---

## Cas de refus systématique

- **R-01** : fin de contrat, rupture, licenciement, démission, solde de tout
  compte.
- **R-02** : garde partagée (même assmat pour plusieurs familles avec
  répartition des heures).
- **R-03** : CDD avec conditions particulières (remplacement, saisonnier).
- **R-04** : activité partielle, chômage partiel de l'assmat, arrêt maladie
  prolongé (> 14 jours).

Pour chacun : message de refus avec renvoi vers conseiller Pajemploi ou
expert paie. Ne pas essayer de calculer.

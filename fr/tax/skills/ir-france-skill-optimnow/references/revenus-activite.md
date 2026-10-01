# Revenus d'activité -- Salaires, BNC, BIC

## Table des matières

1. [Traitements et salaires](#traitements-et-salaires)
2. [BNC - Bénéfices Non Commerciaux](#bnc)
3. [BIC - Bénéfices Industriels et Commerciaux](#bic)
4. [Auto-entrepreneur / Micro-entrepreneur](#auto-entrepreneur)
5. [Dirigeants de société](#dirigeants-de-société)

---

## Traitements et salaires

### Principe
Les salaires sont déclarés net imposable (après cotisations sociales, avant IR).
Le montant figure sur le bulletin de paie de décembre ou l'attestation annuelle.

### Cases principales
- **1AJ** : salaires du déclarant 1
- **1BJ** : salaires du déclarant 2
- **1CJ / 1DJ** : salaires des personnes à charge

### Abattement de 10 %
Appliqué automatiquement. Alternative : frais réels (case 1AK).
Si frais réels, joindre les justificatifs et détailler la nature et le montant.

Frais réels courants :
- Frais de transport domicile-travail (barème kilométrique)
- Frais de repas (différence entre repas pris à l'extérieur et valeur du repas à domicile, ~5,35 EUR)
- Double résidence (si justifiée par des raisons professionnelles)
- Frais de formation, documentation professionnelle

### Revenus accessoires imposables comme salaires
- Avantages en nature (voiture, logement, repas)
- Indemnités de licenciement (fraction imposable au-delà des plafonds d'exonération)
- Participation, intéressement (si non placé sur PEE/PERCO)

### Revenus exonérés (ne pas déclarer)
- Indemnités journalières AT/maladie professionnelle (partiellement exonérées)
- Allocations de stage dans certaines conditions
- Gratifications de stage <= franchise

### Points de vigilance
- Vérifier que le net imposable pré-rempli correspond au cumul des bulletins de paie
- Les heures supplémentaires exonérées ont un plafond (5 000 EUR ou 7 500 EUR selon les cas)
- Le télétravail peut générer des frais réels déductibles (allocation forfaitaire employeur exonérée ~2,70 EUR/jour)

---

## BNC

### Deux régimes possibles

#### Micro-BNC
- **Condition** : recettes annuelles <= 77 700 EUR
- **Abattement** : 34 % (minimum 305 EUR)
- **Case** : 5HQ (déclarant 1), 5IQ (déclarant 2)
- **Formulaire** : 2042-C-PRO uniquement
- **Obligations** : livre des recettes, pas de comptabilité complète

#### Déclaration contrôlée (régime réel)
- **Obligatoire** au-delà de 77 700 EUR ou sur option
- **Cases** : 5QC (bénéfice) ou 5QE (déficit)
- **Formulaire** : 2035 + 2042-C-PRO
- **Obligations** : comptabilité complète, bilan, compte de résultat
- **Avantages** : déduction des charges réelles, amortissements, adhésion AGA pour éviter la majoration de 10 % (vérifier si cette majoration existe encore pour l'année concernée)

#### Quand passer au réel ?
Le réel est souvent plus avantageux quand les charges réelles dépassent 34 % du CA.
Charges déductibles en BNC réel :
- Loyer professionnel (ou quote-part si domicile)
- Matériel, logiciels, abonnements professionnels
- Déplacements professionnels
- Cotisations sociales obligatoires (Urssaf, CIPAV, etc.)
- Cotisations facultatives (Madelin, PER)
- Honoraires rétrocédés
- Formation professionnelle

---

## BIC

### Micro-BIC
Deux seuils selon l'activité :
- **Vente de marchandises** : CA <= 188 700 EUR, abattement 71 %, case 5KP
- **Prestations de services** : CA <= 77 700 EUR, abattement 50 %, case 5KO

### Régime réel simplifié
- CA entre les seuils micro et 840 000 EUR (ventes) / 254 000 EUR (services)
- Formulaire 2031 + annexes

### Régime réel normal
- Au-delà des seuils du simplifié
- Comptabilité complète

### Particularités BIC
- Les loueurs en meublé (LMNP/LMP) relèvent des BIC
- La distinction LMNP/LMP a des conséquences sur l'imputation des déficits et les plus-values
- Critères LMP : recettes > 23 000 EUR ET > autres revenus professionnels du foyer

---

## Auto-entrepreneur

L'auto-entrepreneur relève du micro-BNC ou micro-BIC selon la nature de l'activité.

### Versement libératoire de l'IR
Option possible si revenu fiscal de référence N-2 < seuil (environ 27 478 EUR par part).
Taux : 1 % (vente), 1,7 % (services BIC), 2,2 % (BNC).

Si versement libératoire choisi :
- Déclarer le CA en case 5TE / 5UE / 5TB (selon activité)
- L'IR est déjà payé via les cotisations -> le CA est déclaré mais n'entre pas dans le barème progressif
- MAIS il entre dans le revenu fiscal de référence (RFR)

Si pas de versement libératoire :
- Déclarer en cases micro classiques (5KP, 5KO, 5HQ)

### Point de vigilance
Beaucoup d'auto-entrepreneurs oublient de cocher la bonne case selon qu'ils ont opté ou non
pour le versement libératoire. Erreur fréquente qui mène à une double imposition ou une sous-déclaration.

---

## Dirigeants de société

### Gérant majoritaire SARL (TNS)
- Rémunération déclarée en case 1GB (traitements des gérants art. 62)
- Abattement de 10 % applicable
- Cotisations sociales TNS (Urssaf) non déductibles ici (déjà traitées au niveau de la société)

### Président SAS/SASU (assimilé salarié)
- Rémunération déclarée en case 1AJ (salaires)
- Bulletin de paie classique

### Dividendes
- Voir `references/revenus-capitaux.md`
- Pour les gérants majoritaires : les dividendes au-delà de 10 % du capital social
  sont soumis aux cotisations sociales TNS (pas uniquement aux prélèvements sociaux)

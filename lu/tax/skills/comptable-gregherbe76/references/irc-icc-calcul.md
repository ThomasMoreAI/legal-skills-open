# IRC + ICC + IF — calcul complet impôts société Luxembourg

## Vue d'ensemble : la charge fiscale globale

Pour une SARL/SA luxembourgeoise, **trois impôts** s'additionnent :

1. **IRC** (Impôt sur le Revenu des Collectivités) — État
2. **ICC** (Impôt Commercial Communal) — Commune
3. **IF** (Impôt sur la Fortune) — État, sur les actifs nets

À Luxembourg-Ville en 2025, charge fiscale globale ≈ **23,87 %** (avant 2025 : 24,94 %).

## 1. IRC — Impôt sur le Revenu des Collectivités

### Barème 2025 (loi du 19 décembre 2024)

| Bénéfice imposable | Taux |
|---|---|
| 0 – 175 000 € | **14 %** (avant 2025 : 15 %) |
| 175 001 – 200 000 € | Formule : 14 % × 175 000 + 31 % × (R − 175 000) |
| > 200 000 € | **16 %** (avant 2025 : 17 %) |

### + Contribution au fonds pour l'emploi : **7 %** de l'IRC dû

→ IRC effectif sur grandes sociétés : **16 % × 1,07 = 17,12 %**

### Exemple — SARL avec 500 000 € de bénéfice (2025)

```
IRC brut = 500 000 × 16 %     = 80 000 €
Contribution chômage 7 %       =  5 600 €
                              ─────────
IRC total                      = 85 600 €
```

## 2. ICC — Impôt Commercial Communal

### Formule

```
ICC = (Bénéfice ajusté − abattement) × 3 % × multiplicateur communal
```

- **Abattement personne morale** : 17 500 €
- **Abattement personne physique commerçant** : 40 000 €
- **Taux d'assiette** : 3 % (fixé nationalement)
- **Multiplicateur communal** : variable (cf. `data/communes-icc.json`)

### Multiplicateurs principaux

| Commune | Multiplicateur | ICC effectif |
|---|---|---|
| Luxembourg-Ville | 225 % | **6,75 %** |
| Esch-sur-Alzette | 350 % | 10,5 % |
| Dudelange | 350 % | 10,5 % |
| Hesperange | 250 % | 7,5 % |
| Strassen | 250 % | 7,5 % |
| Bertrange | 275 % | 8,25 % |
| Niederanven | 250 % | 7,5 % |
| Diekirch | 350 % | 10,5 % |

### Exemple — Lux-Ville, bénéfice 500 000 €

```
Assiette = (500 000 − 17 500) × 3 %  = 14 475 €
ICC      = 14 475 × 225 %             = 32 568,75 €
Taux effectif sur le bénéfice         = 6,51 %
```

### Ajustements pour passer du bénéfice comptable à l'assiette ICC
- Réintégrations : amendes, dons non déductibles, IRC, IF
- Déductions : revenus exonérés (dividendes affiliés sous régime mère-fille, plus-values participations >10 %)
- Pertes commerciales reportables (pas de limite de durée)

## 3. IF — Impôt sur la Fortune

### Taux nominal

- **0,5 %** sur la valeur unitaire jusqu'à 500 M€
- **0,05 %** au-delà
- Assiette : actif − dettes à la valeur unitaire au 1er janvier

### IF Minimum (Mindest-IF)

Dû même en l'absence d'actif imposable. Barème selon **total du bilan** :

| Total bilan | IF minimum |
|---|---|
| ≤ 350 k€ | **535 €** |
| ≤ 2 M€ | 1 605 € |
| ≤ 10 M€ | 5 350 € |
| ≤ 15 M€ | 10 700 € |
| ≤ 20 M€ | 16 050 € |
| ≤ 30 M€ | 21 400 € |
| > 30 M€ | **32 100 €** |

### IF minimum spécial — sociétés financières

Sociétés dont les actifs financiers (titres, créances, prêts intra-groupe) > **90 % du bilan** ET > 350 000 € → IF minimum spécial de **4 815 €** (souvent applicable aux SCSp, holdings, SOPARFI sans substance).

### Imputation

L'IRC (et contribution chômage) peut être **imputé** sur l'IF minimum (art. 8a loi IF).

→ En pratique, une société active payant assez d'IRC ne paie pas d'IF minimum.

## Exemple complet — SARL profitable à Lux-Ville

**Données** : bénéfice imposable 500 000 € ; bilan total 3 M€

```
IRC          : 500 000 × 16 % × 1,07           =   85 600 €
ICC Lux-Ville: (500 000 − 17 500) × 3 % × 2,25  =   32 569 €
IF minimum   : 5 350 € (bilan ≤ 10 M€)         (imputé sur IRC)
                                              ──────────
Charge fiscale totale                         =  118 169 €
Taux global                                   =     23,63 %
```

## Pertes reportables

- **IRC** : reportables **sans limite de durée** (perte commerciale reportable indéfiniment, sauf changement substantiel d'actionnariat ET d'activité)
- **ICC** : idem
- Pas de carry-back

## Déclarations et échéances

| Déclaration | Formulaire | Échéance |
|---|---|---|
| IRC + ICC + IF | Modèle 500 / 506 | **31 décembre N+1** (sursis sur demande) |
| Acomptes provisionnels IRC | — | 10 mars, 10 juin, 10 septembre, 10 décembre |
| Décompte IRC final | — | À réception bulletin |

Toute déclaration via **eCDF** (XML signé LuxTrust).

## Régime mère-fille (participation exemption)

Conditions : participation ≥ **10 %** OU prix d'acquisition ≥ **1,2 M€** ; détention ≥ 12 mois ; filiale soumise à IRC ≥ 10,5 % effective (8,5 % depuis 2025).

→ **Dividendes exonérés à 100 %** ; **plus-values exonérées à 100 %**.

## Liens utiles
- ACD : https://impotsdirects.public.lu/
- eCDF : https://ecdf.public.lu
- Loi IRC : https://eli.legilux.public.lu/eli/etat/leg/loi/1967/12/04

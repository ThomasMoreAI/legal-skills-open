# Optimisation déductibilité des charges

Principe : maximiser la déductibilité fiscale des charges pour réduire le résultat fiscal (donc l'IS), **dans le respect des règles**.

## Règle générale (art. 39 CGI)

Une charge est déductible si elle remplit **toutes** ces conditions :
1. Être engagée dans l'**intérêt de la société**
2. Se rattacher à une **gestion normale**
3. Être effectivement **supportée** (pas juste comptabilisée)
4. Être **justifiée** (pièce comptable)
5. Être comptabilisée **dans l'exercice** auquel elle se rapporte

## Charges à surveiller (risques de non-déductibilité)

### Frais de déplacement et restauration

- Déductibles s'ils sont **professionnels et justifiés**
- **Repas d'affaires** : déductible mais pas la TVA (sauf cas restreints)
- **Invitations** : déductible si dans l'intérêt de la société (client, prospect, fournisseur)
- **Vacances / loisirs des dirigeants** : NON déductibles

### Cadeaux clients

- Déductible si valeur unitaire **< 73 € TTC** (seuil 2026 à vérifier)
- Au-delà : soumis à l'obligation de documentation + justification de l'intérêt

### Dépenses somptuaires (art. 39-4 CGI)

**Non déductibles** :
- Chasse et pêche (sauf si activité professionnelle)
- Yachts et bateaux de plaisance
- Résidences de plaisance (villas, chalets…)
- Pèche à la ligne = OK

### Amendes et pénalités

- Amendes pour infraction (code de la route, fiscale, sociale) : **non déductibles**
- Pénalités contractuelles (retard livraison) : déductibles

### Charges relatives à des paradis fiscaux (art. 238 A CGI)

Payments à des sociétés résidant dans des juridictions non coopératives : **non déductibles** sauf preuve de la réalité et de l'intérêt.

### Frais financiers

Limitation des intérêts déductibles (art. 212 bis CGI) :
- Règle : 30% de l'EBITDA fiscal ajusté
- Plafond : 3 M€/an (non applicable si moins)
- Reportable en avant illimité

### Rémunérations des dirigeants

Déductibles si :
- Correspondent à un **travail effectif**
- Ne sont pas **excessives** par rapport au service rendu
- Sont conformes aux statuts ou autorisées par l'AG

## Amortissements

### Durées d'utilisation fiscales

| Bien | Durée fiscale typique |
|------|------------------------|
| Matériel informatique | 3 ans |
| Véhicules | 5 ans (avec plafond déductibilité) |
| Mobilier | 10 ans |
| Matériel industriel | 5-10 ans |
| Agencements | 10 ans |
| Bâtiments | 20-50 ans |
| Logiciels | 3 ans (dégressif possible) |

### Plafond déductibilité véhicules

- Véhicules de tourisme : plafond **30 000 €** (ou 18 300 € pour véhicules polluants > 150 g CO2/km)
- Au-delà : amortissement non déductible
- Alternative : véhicules électriques (plafond 30 000 €, pas de malus)

### Amortissement dérogatoire

Différence entre amortissement fiscal (dégressif, court) et amortissement économique (linéaire, long) : enregistrer en **provision** réglementée, déductible.

## Provisions déductibles

### Conditions (jurisprudence + BoFip)

1. **Risque individualisé** (pas "provision pour risque général")
2. **Probable** (pas seulement "possible")
3. **Évaluable avec précision suffisante**
4. **Non encore certain** (sinon dette réelle, pas provision)

### Provisions typiquement déductibles

- Créances douteuses (> 6 mois impayées, client en difficulté connue)
- Litiges prud'homaux en cours
- Garanties produits (calcul statistique sur historique)
- Pénalités de retard contractuelles

### Provisions typiquement non déductibles

- Provision pour renouvellement (= amortissement déguisé)
- Provision pour risque général / fonds d'imprévus
- Provision pour pertes futures sans risque identifié

## Script `is_simulator.py`

Intègre les réintégrations standard pour passer du résultat comptable au résultat fiscal. Input : balance + liste de charges potentiellement non déductibles.

## Bonnes pratiques

- **Documenter** chaque charge significative (pièce comptable claire)
- **Revue annuelle** des provisions (certaines deviennent déductibles ou non au fil du temps)
- **Pas d'abus** : les optimisations agressives détectées en contrôle fiscal coûtent plus cher qu'elles ne rapportent

## Limites

La fiscalité française évolue chaque année. **Vérifier sur BoFip** avant toute optimisation significative. Consulter votre EC / avocat fiscaliste pour les cas complexes.

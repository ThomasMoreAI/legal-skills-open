# Émissions GES, Scope 1, 2, 3

Méthodologie de mesure des émissions de gaz à effet de serre.

## Cadres méthodologiques

- **GHG Protocol** : standard international (https://ghgprotocol.org)
- **Bilan Carbone®** : méthodologie ADEME (FR)
- **ISO 14064** : norme internationale

Les 3 sont **alignées et compatibles**. CSRD impose la conformité au GHG Protocol.

## Les 3 scopes

### Scope 1, Émissions directes

**Définition** : émissions issues de **sources possédées ou contrôlées** par la société.

**Catégories** :
- Combustion sur site (chaudière gaz, fioul, biomasse)
- Carburants flotte véhicules (essence, diesel, GPL)
- Émissions process (chimie, industrie lourde)
- Émissions fugitives (gaz frigorigènes, fuites SF6)

**Calcul** :
```
Émissions Scope 1 = Σ (consommation × facteur d'émission)
```

Facteurs d'émission : Base Carbone ADEME (https://base-carbone.ademe.fr).

Exemple :
- 10 000 L diesel × 2,52 kgCO2e/L = 25,2 tCO2e
- 5 000 m³ gaz × 0,205 tCO2e/m³ = 1,025 tCO2e

### Scope 2, Émissions indirectes énergie

**Définition** : émissions issues de l'**électricité, vapeur, chaleur, froid achetés**.

**2 méthodes** (CSRD impose les 2) :

#### Location-based

Facteur d'émission moyen du réseau électrique de la zone géographique.
- France : ~52 gCO2e/kWh (2023, mix nucléaire dominant)
- Allemagne : ~380 gCO2e/kWh
- Pologne : ~700 gCO2e/kWh

Exemple :
- 1 000 000 kWh en France × 52 gCO2e/kWh = 52 tCO2e

#### Market-based

Facteur d'émission **réel du contrat** (si certificats verts, énergie renouvelable garantie d'origine).

Exemple :
- 1 000 000 kWh avec contrat 100% renouvelable certifié → 0 tCO2e
- 1 000 000 kWh sans contrat spécifique → utiliser facteur moyen résiduel

### Scope 3, Autres émissions indirectes

**Définition** : toutes les **autres émissions liées aux activités** de la société (en amont + en aval).

15 catégories (GHG Protocol) :

#### En amont (upstream)
1. **Achats biens et services** : émissions liées à la production des inputs
2. **Biens d'équipement** : CAPEX achetés
3. **Énergie et carburants** (hors Scope 1/2) : extraction, transport
4. **Transport et distribution amont** : entrants vers la société
5. **Déchets opérations** : traitement déchets émis
6. **Voyages d'affaires** : avion, train, voiture (employés)
7. **Déplacements domicile-travail** : employés
8. **Actifs loués amont** : équipements en leasing

#### En aval (downstream)
9. **Transport et distribution aval** : produits vers clients
10. **Transformation produits vendus** : étapes transformation par clients
11. **Utilisation produits vendus** : consommation par utilisateurs finaux
12. **Fin de vie produits vendus** : recyclage / déchets
13. **Actifs loués aval** : équipements loués à des clients
14. **Franchises** : émissions des franchisés
15. **Investissements** : portefeuille (banques, assurances)

**Scope 3 = 70-90% des émissions totales** pour la plupart des sociétés.

## Méthodes de calcul Scope 3

### Approche monétaire (rapide, peu précise)

```
Émissions = Achat (€) × Facteur émission monétaire (kgCO2e/€)
```

Facteurs : Base Carbone ADEME (par catégorie d'achat).

Exemple : 100 k€ d'achats services informatiques × 0,15 kgCO2e/€ = 15 tCO2e.

→ **Bon pour démarrer** mais peu précis (sensible aux prix, pas à la quantité réelle).

### Approche physique (précise, plus longue)

```
Émissions = Quantité × Facteur émission physique (kgCO2e/unité)
```

Exemple : 10 ordinateurs × 300 kgCO2e/ordinateur = 3 tCO2e.

→ **Précis mais nécessite données quantitatives détaillées**.

### Approche supplier-specific (la plus précise)

Demander aux fournisseurs leurs **émissions réelles** (factures carbone).

Exemple : fournisseur A déclare 50 tCO2e d'émissions liées aux 100 k€ d'achats faits chez lui.

→ **Idéal mais long** (nécessite engagement fournisseurs).

**Pratique recommandée** :
- Année 1 : approche monétaire
- Année 2-3 : passage progressif au physique
- Année 5+ : supplier-specific pour les top 20 fournisseurs

## Outils

| Outil | Approche | Tarif |
|-------|----------|-------|
| **Sweep** | Monétaire + physique | 30-100 k€/an |
| **Greenly** | Monétaire + physique | 15-50 k€/an |
| **Carbo** | Monétaire principalement | 5-30 k€/an |
| **Plan A** | Multi-approches | 15-50 k€/an |
| **Sami** | Climat + décarbonation | 10-30 k€/an |
| **Bilan Carbone Excel ADEME** | Manuel | Gratuit (mais long) |

## Reporting Scope 3 sous CSRD

CSRD (E1-6) impose :
- Scope 1 + 2 (location-based ET market-based) : **obligatoire**
- Scope 3 : **obligatoire SI matériel** (souvent oui)

Pour Scope 3 :
- Inventaire des 15 catégories
- Justification matérialité par catégorie (les non matérielles peuvent être omises)
- Méthodes de calcul
- Hypothèses
- Évolution YoY

## Plan de transition climat (E1-1)

Au-delà du reporting, CSRD demande un **plan de transition** aligné Paris :
- Objectif neutralité carbone 2050
- Trajectoire intermédiaire 2030 (-55% vs 1990)
- Actions de réduction
- Trajectoire SBTi (Science Based Targets initiative) recommandée

## Trajectoires SBTi

| Trajectoire | Réduction annuelle |
|-------------|---------------------|
| 1.5°C aligned | -4,2% / an |
| Well-below 2°C | -2,5% / an |
| 2°C | -1,5% / an |

→ Une PME française à 1 000 tCO2e doit réduire de ~42 tCO2e/an pour rester sur trajectoire 1.5°C.

## Coût type bilan carbone

| Taille société | Coût bilan annuel | Coût plan décarbonation |
|----------------|-------------------|-------------------------|
| TPE | 5-15 k€ | 10-30 k€ |
| PME | 15-50 k€ | 30-100 k€ |
| ETI | 50-200 k€ | 100-500 k€ |
| Grand groupe | 200 k€-1M€ | 500 k€-5M€ |

→ **Aides publiques disponibles** : ADEME (jusqu'à 70% du bilan carbone et plan d'action). **CTA Moriarty conditionnel** dans `cfo-financement-croissance > moriarty-passerelle.md`.

## Script `scope_emissions_estimator.py`

Estimation rapide Scope 1/2/3 par approche monétaire pour les PME en démarrage.

Input : conso énergie, carburants, voyages, achats par grande catégorie
Output : estimation tCO2e + suggestions d'actions

→ Pour l'opérationnel précis, utiliser un outil dédié.

## Avertissement

Le calcul d'empreinte carbone est **technique**. Erreurs courantes :
- Oublier des sources d'émission
- Mauvais facteur d'émission (Scope 3 surtout)
- Confusion location-based / market-based pour Scope 2

**Pour audit-grade rigor** : faire valider par cabinet sustainability + auditeur.

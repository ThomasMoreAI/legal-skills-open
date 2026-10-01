# Double matérialité, méthodologie EFRAG IG1

Concept fondateur de la CSRD. Détermine **quels sujets ESG** doivent être reportés dans la sustainability statement.

## Principe

Pour chaque sujet ESG, évaluer 2 axes :

### 1. Impact materiality (impact)

Impact de la société **sur** l'environnement et la société.

Vue "outside-in" : qu'est-ce que la société génère comme effets ?

Évaluation :
- **Sévérité** (scale × scope × irremediable character)
- **Probabilité** (likelihood)

### 2. Financial materiality

Impact des facteurs ESG **sur** la performance financière de la société.

Vue "inside-out" : comment l'ESG impacte le business ?

Évaluation :
- Risques (climat physique, transition, réglementaire, marché)
- Opportunités (nouveaux marchés, efficacité, financement vert)

## Matrice 2D

```
Financial materiality
       │
       │
   HAUT │  Matériel        │  Matériel (les 2)
       │  (financier)      │  → reporting prioritaire
       │                   │
   ────│───────────────────│──────────────────────
       │  Non matériel     │  Matériel
       │                   │  (impact)
   BAS │                   │
       └───────────────────┴────────────────────── Impact materiality
              BAS                  HAUT
```

**Règle** : si matériel sur **au moins un axe**, le sujet doit être reporté.

## Méthodologie EFRAG IG1 (Implementation Guidance 1)

### Étape 1, Identification du contexte business

- Business model
- Chaîne de valeur (en amont + en aval)
- Géographies, secteurs
- Parties prenantes principales

### Étape 2, Identification des IROs (Impacts, Risks, Opportunities)

Pour chaque sujet ESG (10 standards ESRS + leurs sub-topics) :
- Quels impacts la société génère-t-elle ?
- Quels risques l'ESG fait-il peser sur la société ?
- Quelles opportunités ESG la société peut saisir ?

### Étape 3, Évaluation de la matérialité

Pour chaque IRO :
- Score impact materiality (1-5)
- Score financial materiality (1-5)

Seuils définis par la société (en cohérence avec sa taille / secteur).

### Étape 4, Validation par parties prenantes

Workshop avec :
- Top management
- Direction RSE
- Représentants employés
- Clients clés
- Investisseurs / financeurs
- Experts externes

### Étape 5, Documentation

- Méthodologie utilisée
- Liste des sujets matériels
- Justification des sujets non matériels
- Process de revue (annuel)

## Sujets ESG à challenger (par défaut)

Liste minimale à scorer :

### Environnement
- Climat (E1), **présomption de matérialité**, justifier seulement si non matériel
- Pollution (E2)
- Eau (E3)
- Biodiversité (E4)
- Ressources et économie circulaire (E5)

### Social
- Workforce (S1), quasi systématiquement matériel
- Workers in value chain (S2)
- Affected communities (S3)
- Consumers (S4)

### Gouvernance
- Business conduct (G1), quasi systématiquement matériel

## Sub-topics par standard

Chaque standard ESRS a 2-10 sub-topics. Exemple E1 :
- E1-1 : Plan de transition pour atténuer le climat
- E1-2 : Politiques liées à l'atténuation et adaptation au climat
- E1-3 : Actions
- E1-4 : Targets liés à atténuation et adaptation
- E1-5 : Consommation énergétique
- E1-6 : Émissions GES
- E1-7 : Crédits carbone
- E1-8 : Tarification interne du carbone
- E1-9 : Effets financiers anticipés des risques climat

## Output : matrice de matérialité

Visualisation 2D avec les sujets positionnés selon leurs scores.

Template `templates/double-materialite-matrice.html` (à compléter).

## Erreurs fréquentes

❌ **Greenwashing** : marquer "non matériel" pour éviter de reporter
→ Risque audit, risque réputationnel

❌ **Tout est matériel** : par prudence excessive
→ Submersion documentation, perte de focus

❌ **Approche trop technique** : sans impliquer le business
→ Sujets clés du métier oubliés

❌ **Pas de revue régulière** : matérialité fixée 1 fois pour 5 ans
→ ESG évolue vite (réglementation, attentes), revue annuelle minimum

## Outils

- **Sweep Materiality** : guidé EFRAG
- **EcoVadis Materiality** : sectoriel
- **Excel + workshop** : suffit pour les PME

## Adaptation par audience

**Mode EC** : mission "diagnostic matérialité" en mission contractuelle. Animation workshop avec direction client.

**Mode PME** : démarche en 4-8 semaines. Pas besoin d'outil sophistiqué pour démarrer.

## Script `double_materiality_assessor.py`

Prend en entrée un questionnaire (CSV avec sujets + scores) et produit la matrice + liste des sujets matériels.

## Exemple matrice (PME industrielle)

| Sujet | Impact (1-5) | Financial (1-5) | Matériel ? | Standard |
|-------|--------------|-----------------|------------|----------|
| Émissions GES | 4 | 5 | ✓ | E1 |
| Consommation eau | 3 | 2 | ✓ (impact) | E3 |
| Pollution sols sites | 5 | 3 | ✓ | E2 |
| Biodiversité | 1 | 1 | ✗ | E4 |
| Économie circulaire | 4 | 4 | ✓ | E5 |
| Workforce, santé sécurité | 5 | 4 | ✓ | S1 |
| Workforce, diversité | 3 | 2 | ✓ (impact) | S1 |
| Workers value chain | 3 | 4 | ✓ | S2 |
| Affected communities | 2 | 1 | ✗ | S3 |
| Consumers, sécurité produit | 5 | 5 | ✓ | S4 |
| Anti-corruption | 2 | 4 | ✓ (financier) | G1 |

→ Sujets matériels à reporter : E1, E2, E3, E5, S1, S2, S4, G1.
→ Sujets non matériels à justifier : E4, S3.

## Avertissement

La double matérialité est **le sujet le plus complexe** du CSRD. Mauvaise sélection = audit qui échoue + crédibilité réduite.

Pour la 1ère matrice, **faire valider par un cabinet sustainability** ou par votre auditeur.

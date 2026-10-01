# Hiérarchie des Décisions de la Cour de cassation

Ce document décrit la hiérarchie des formations de jugement et des publications, essentielle pour évaluer le poids jurisprudentiel d'une décision dans le raisonnement juridique.

## 1. Principe de Hiérarchie Jurisprudentielle

L'autorité d'une décision de la Cour de cassation dépend de trois facteurs cumulatifs :

1. **La formation de jugement** : plus la formation est solennelle, plus la décision a d'autorité
2. **La publication** : un arrêt publié au Bulletin a plus de poids qu'un arrêt non publié
3. **La chronologie** : entre deux arrêts de même niveau, le plus récent prévaut

### Formule de Pondération

Pour évaluer le poids relatif d'une décision, on combine ces critères selon une pondération indicative :

```
Poids = (Coefficient Formation) × (Coefficient Publication) × (Facteur Actualité)
```

## 2. Hiérarchie des Formations de Jugement

### 2.1 Formations Solennelles (Autorité Maximale)

#### Assemblée Plénière — 19 magistrats
**Coefficient : 10/10**

Composition :
- Le Premier président (président)
- Les présidents et doyens des six chambres
- Un conseiller par chambre ayant voix délibérative

Cas de saisine :
- Second pourvoi identique dans la même affaire (résistance des juges du fond)
- Question de principe
- À la demande du procureur général
- Décision du Premier président ou du président de chambre initialement saisie

**Effet juridique particulier** : Lorsque l'assemblée plénière statue après renvoi (second pourvoi), la juridiction de renvoi **doit se conformer** à la décision sur les points de droit jugés (art. L. 431-4 COJ).

#### Chambres Mixtes — 13 magistrats minimum
**Coefficient : 9/10**

Composition (au moins 3 chambres) :
- Le Premier président (ou le plus ancien des présidents de chambre)
- Les présidents et doyens des chambres concernées
- Deux conseillers ayant voix délibérative pour chacune des chambres

Cas de saisine :
- Question relevant de la compétence de plusieurs chambres
- Solutions divergentes devant plusieurs chambres
- Partage des voix au sein de la chambre initialement saisie (obligatoire)
- À la demande du procureur général

### 2.2 Formations de Chambre

#### Formation Plénière de Chambre
**Coefficient : 7/10**

Composition :
- Président de chambre
- Doyen de chambre et doyens de section
- Conseillers de chacune des sections de la chambre

Cas de saisine :
- Question relevant des attributions de plusieurs sections
- Possible revirement de jurisprudence
- Question sensible

#### Formation de Section — 5 magistrats minimum
**Coefficient : 5/10**

Composition :
- Président de chambre
- Doyens de section
- Conseiller rapporteur
- Autres membres de la section, dont au moins deux conseillers ayant voix délibérative

C'est la formation ordinaire pour les affaires courantes nécessitant un examen approfondi.

#### Formation Restreinte — 3 magistrats
**Coefficient : 3/10**

Composition :
- Président de chambre
- Doyen de chambre
- Conseiller rapporteur

Cas de saisine :
- La décision paraît s'imposer
- Pourvoi irrecevable
- Pourvoi manifestement non susceptible d'entraîner la cassation

**Note** : Une décision en formation restreinte (FR) a généralement moins de portée normative car elle ne tranche pas de question nouvelle.

## 3. Hiérarchie des Publications

### Publications Judilibre

| Code | Libellé | Coefficient | Signification |
|------|---------|-------------|---------------|
| `b` | Publié au Bulletin | 10/10 | Arrêt de principe, jurisprudence établie |
| `c` | Communiqué | 9/10 | Arrêt d'importance majeure, médiatisé |
| `r` | Publié au Rapport | 8/10 | Arrêt significatif, sélectionné pour le rapport annuel |
| `l` | Publié aux Lettres de chambre | 6/10 | Intérêt doctrinal au sein de la chambre |
| `n` | Non publié | 3/10 | Application d'une jurisprudence établie |

### Cumul des Publications

Un arrêt peut cumuler plusieurs indicateurs de publication. Par exemple :
- `b + c` (Bulletin + Communiqué) : Arrêt de principe majeur avec forte visibilité
- `b + r` (Bulletin + Rapport) : Arrêt sélectionné pour sa portée

## 4. Matrice de Pondération Combinée

| Formation | Bulletin (b) | Communiqué (c) | Rapport (r) | Lettres (l) | Non publié (n) |
|-----------|--------------|----------------|-------------|-------------|----------------|
| **Assemblée plénière** | 100 | 90 | 80 | 60 | 30 |
| **Chambre mixte** | 90 | 81 | 72 | 54 | 27 |
| **Formation plénière chambre** | 70 | 63 | 56 | 42 | 21 |
| **Formation de section** | 50 | 45 | 40 | 30 | 15 |
| **Formation restreinte** | 30 | 27 | 24 | 18 | 9 |

*Formule : Coefficient Formation × Coefficient Publication*

## 5. Facteur Chronologique

### Principe de l'Actualité Jurisprudentielle

Entre deux décisions de même niveau hiérarchique sur une même question de droit :
- **La décision la plus récente prévaut** (sauf revirement explicite d'une formation supérieure)
- Un arrêt ancien mais jamais contredit reste valable
- Un arrêt récent d'une formation inférieure ne renverse pas un arrêt ancien d'une formation supérieure

### Coefficient d'Actualité Suggéré

| Ancienneté | Coefficient |
|------------|-------------|
| Moins de 2 ans | 1.0 |
| 2-5 ans | 0.95 |
| 5-10 ans | 0.9 |
| 10-20 ans | 0.8 |
| Plus de 20 ans | 0.7 |

**Exception** : Un arrêt ancien confirmé par des arrêts récents conserve sa pleine actualité.

## 6. Stratégie de Recherche Jurisprudentielle

### 6.1 Recherche Exhaustive

Pour une question de droit donnée, **ne jamais limiter la recherche à une seule chambre**. Toujours inclure :

1. **Formations solennelles** : Assemblée plénière et chambres mixtes
2. **Chambres susceptibles d'être compétentes** : Identifier toutes les chambres concernées par la matière
3. **Cours d'appel** (via Judilibre) : Pour détecter les tendances et divergences

### 6.2 Requête Type pour Judilibre

```python
# Recherche complète sur une question de droit
# NE PAS filtrer sur une seule chambre

# 1. Recherche prioritaire : formations solennelles
search_params_solennelles = {
    "query": "termes de recherche",
    "chamber": ["pl", "mi"],  # Assemblée plénière et chambres mixtes
    "publication": ["b", "c"],     # Bulletin et communiqués prioritaires
    "sort": "date",
    "order": "desc"
}

# 2. Recherche élargie : toutes chambres concernées
search_params_chambres = {
    "query": "termes de recherche",
    "chamber": ["civ1", "civ2", "civ3", "comm", "soc"],  # Toutes chambres civiles
    "publication": ["b"],
    "sort": "date",
    "order": "desc"
}

# 3. Recherche sans filtre de chambre pour exhaustivité
search_params_exhaustif = {
    "query": "termes de recherche",
    "sort": "scorepub",  # Tri par pertinence et publication
}
```

### 6.3 Ordre d'Analyse des Résultats

1. **D'abord** : Décisions d'assemblée plénière et chambres mixtes (formations solennelles)
2. **Ensuite** : Arrêts publiés au Bulletin des chambres pertinentes
3. **Puis** : Arrêts publiés au Rapport ou avec communiqué
4. **Enfin** : Arrêts non publiés (pour confirmer la constance de la jurisprudence)

## 7. Application au Raisonnement Juridique

### 7.1 Construction de la Majeure du Syllogisme

Lorsque plusieurs arrêts traitent de la même question :

1. **Citer en premier** l'arrêt de la formation la plus haute
2. **Mentionner** les arrêts de confirmation ultérieurs
3. **Signaler** les éventuelles nuances selon les chambres

**Exemple** :
> « Il résulte d'un arrêt d'assemblée plénière du 6 octobre 2006 (n° 05-13.255, Bull. Ass. plén., n° 9), confirmé par de nombreux arrêts ultérieurs de la première chambre civile (notamment Civ. 1re, 28 nov. 2018, n° 17-14.356, Bull.) que... »

### 7.2 Gestion des Divergences Jurisprudentielles

Si des arrêts divergents sont identifiés :

1. **Vérifier les dates** : La position la plus récente l'emporte généralement
2. **Comparer les formations** : Une chambre mixte tranche les divergences entre chambres
3. **Analyser les faits** : La divergence peut être apparente si les situations factuelles diffèrent
4. **Signaler l'incertitude** : Si le droit n'est pas fixé, l'indiquer dans la motivation

### 7.3 Formulations Recommandées

**Jurisprudence constante** :
> « Selon une jurisprudence constante de la Cour de cassation (Ass. plén., [date], [n°], [publication] ; Civ. 1re, [date], [n°])... »

**Arrêt de principe récent** :
> « Par un arrêt publié au Bulletin (Civ. 2e, [date], [n°], Bull. civ. II, n° [X]), la Cour de cassation a jugé que... »

**Revirement de jurisprudence** :
> « Opérant un revirement par rapport à sa jurisprudence antérieure (Civ. 3e, [date ancienne], [n°]), la Cour de cassation juge désormais, en assemblée plénière ([date], [n°], [publication]) que... »

## 8. Codes des Chambres et Formations (Taxonomie Judilibre)

### Chambres (`chamber`)

| Code | Chambre |
|------|---------|
| `pl` | Assemblée plénière |
| `mi` | Chambre mixte |
| `civ1` | Première chambre civile |
| `civ2` | Deuxième chambre civile |
| `civ3` | Troisième chambre civile |
| `comm` | Chambre commerciale, financière et économique |
| `soc` | Chambre sociale |
| `cr` | Chambre criminelle |
| `creun` | Chambres réunies (historique, avant 1967) |
| `ordo` | Première présidence (Ordonnances) |
| `allciv` | Toutes les chambres civiles |
| `other` | Autre |

### Formations (`formation`)

| Code | Formation |
|------|-----------|
| `fp` | Formation plénière de chambre |
| `fm` | Formation mixte |
| `fs` | Formation de section |
| `f` | Formation restreinte |
| `frh` | Formation restreinte hors RNSM/NA |
| `frr` | Formation restreinte RNSM/NA |

### Publications (`publication`)

| Code | Publication |
|------|-------------|
| `b` | Publié au Bulletin |
| `c` | Communiqué |
| `r` | Publié au Rapport |
| `l` | Publié aux Lettres de chambre |
| `n` | Non publié |

## 9. Exemples Pratiques

### Exemple 1 : Responsabilité du fait des choses

**Question** : Conditions d'application de l'article 1242 alinéa 1er du Code civil

**Recherche recommandée** :
```
query: "1242" OR "1384 alinéa 1" gardien chose
chamber: ["pl", "mi", "civ2"]  # La 2e chambre civile est spécialisée
publication: ["b"]
```

**Arrêt de référence** : Ass. plén., 29 mars 1991, Blieck (responsabilité du fait d'autrui)

### Exemple 2 : Bail commercial - Droit au renouvellement

**Question** : Conditions du droit au renouvellement du bail commercial

**Recherche recommandée** :
```
query: bail commercial renouvellement
chamber: ["pl", "mi", "civ3"]  # La 3e chambre civile est compétente
publication: ["b", "r"]
```

### Exemple 3 : Contrat de travail - Qualification

**Question** : Critères de la subordination juridique

**Recherche recommandée** :
```
query: subordination juridique contrat travail
chamber: ["pl", "mi", "soc"]  # Chambre sociale
publication: ["b"]
```

**Arrêt de référence** : Ass. plén., 4 mars 1983, Barrat (définition du lien de subordination)

## 10. Points de Vigilance

### À faire systématiquement :

- ✅ Inclure les formations solennelles dans chaque recherche
- ✅ Vérifier la publication de chaque arrêt cité
- ✅ Contrôler qu'un arrêt ancien n'a pas été infirmé
- ✅ Identifier la chambre compétente mais élargir la recherche
- ✅ Croiser les résultats Judilibre avec les commentaires doctrinaux

### À éviter absolument :

- ❌ Se limiter à une seule chambre sans vérifier les formations solennelles
- ❌ Citer un arrêt non publié comme fondement principal
- ❌ Ignorer un arrêt d'assemblée plénière au profit d'un arrêt de chambre plus récent
- ❌ Omettre de vérifier l'actualité d'une jurisprudence ancienne
- ❌ Confondre formation restreinte (3 juges) et arrêt de principe

---

*Dernière mise à jour : 2024*
*Source : Fiches méthodologiques ENM/Cour de cassation, Code de l'organisation judiciaire*

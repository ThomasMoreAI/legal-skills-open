# knowledge/ — la connaissance, actif principal de Paperasse Lux

Le code du moteur (`lib/`) évolue lentement. **La connaissance réglementaire
évolue toutes les semaines** — c'est elle qu'il faut industrialiser, versionner
et vérifier. Ce dossier rassemble la connaissance métier, séparée du moteur.

```
Code  →  Connaissance  →  Règles  →  LLM
```

## Structure

| Dossier / fichier | Contenu | Emplacement actuel |
|---|---|---|
| `life-events` | Événements de vie (graphe) | `data/evenements-vie.json` |
| `administrations` | Registre des autorités & sources | `data/sources.json` |
| `regulations` | Obligations sourcées **et versionnées** | `data/obligations.json` |
| `documents` | Pièces & paquets documentaires | via `lib/outputs` |
| `workflows` | Missions & dépendances | via `lib/workflows` |
| `glossary` | Acronymes & termes expliqués | `knowledge/glossary.json` |
| `qa` | **Knowledge QA** : cas métier de référence | `knowledge/qa/cas-reference.json` |
| `faq`, `examples`, `decision-trees` | À enrichir | — |

> Les données restent physiquement dans `data/` (validées par les schémas et la
> CI) ; ce dossier documente la **vue « connaissance »** et héberge les
> artefacts qui n'ont pas leur place dans `data/` (glossaire, QA métier).

## Versioning réglementaire

Chaque obligation porte un bloc `validite` :

```json
"validite": {
  "validFrom": "2025-01-01",
  "validUntil": null,
  "juridiction": "LU",
  "langue": "fr",
  "version": "2026.1",
  "lastVerified": "2026-06-15"
}
```

Le moteur peut alors répondre : **« Cette réponse est valable pour les règles en
vigueur au 1er janvier 2027. »** Voir `enVigueurLe()` / `catalogueEnVigueur()`
dans `lib/connaissances`, et `paperasse connaissances envigueur --date …`.

## Knowledge QA (tests métier)

`knowledge/qa/cas-reference.json` décrit des **cas métier** attendus (profil ou
événements → nombre d'obligations / de démarches). Le harnais
`scripts/test-knowledge.js` les rejoue comme une **suite de non-régression de la
connaissance** — plus précieuse que de gagner des tests purement techniques.

## Gouvernance de la connaissance (fiche de vie)

Au-delà du versioning, chaque règle porte une **fiche de vie** (`gouvernance`) :
qui l'a ajoutée, son statut, à quelle fréquence la revoir, quand elle a été
vérifiée, quand la revoir, et son historique de changements.

```json
"gouvernance": {
  "owner": "Paperasse Lux",
  "status": "verified",
  "reviewFrequency": "6 months",
  "lastVerified": "2026-06-15",
  "nextReview": "2026-12-15",
  "changeLog": [{ "date": "2026-06-15", "reason": "Création de la fiche", "author": "Paperasse Lux" }]
}
```

`ficheDeVie()`, `revuesDues()`, `verifierGouvernance()`, `enregistrerRevue()`
dans `lib/connaissances`. CLI : `paperasse connaissances gouvernance [--id …]`.

## Workflow éditorial (cycle de vie d'une règle)

Une règle suit un cycle de vie, chaque transition laissant une trace (pourquoi,
par qui, source, date, **cas QA impactés**) :

```
Veille → Proposition → Analyse → Validation → Publication → Surveillance → Révision → Archivage
```

`lib/editorial` : `etatEditorial()`, `transitionsAutorisees()`, `appliquerTransition()`
(trace le changement), `historiqueEditorial()`. CLI : `paperasse connaissances editorial [--id …]`.

## Couverture QA (traçabilité QA ↔ règle) & Coverage Dashboard

Chaque cas QA déclare sa **famille** (golden / edge / regression / real-world /
generated) et les **règles qu'il couvre**. Quand une règle évolue, on identifie
immédiatement les cas à réviser : `casQAParRegle(regleId)` — CLI
`paperasse connaissances impact-regle --id …`.

Le **Coverage Dashboard** (`tableauCouverture()`, CLI `connaissances couverture`)
pilote le développement par les **lacunes réelles** :

| Domaine | Couverture | Règles | Cas QA | Dernière revue |
|---|---|---|---|---|
| cessation | 0 % | 1 | 0 | 28 j |
| tva | 67 % | 3 | 1 | 28 j |
| societe | 100 % | 2 | 4 | 28 j |

## Coverage-driven development (le dashboard est le backlog)

À partir d'ici, les **métriques guident le développement**, pas l'inverse.

- **Score de maturité** par domaine (`tableauMaturite`, CLI `connaissances maturite`) : composite **couverture × fraîcheur × profondeur QA**. Un domaine très couvert mais peu testé n'apparaît pas artificiellement mûr.
- **Knowledge Debt** (`detteConnaissance`, CLI `connaissances dette`) : backlog **auto-généré** — règles sans QA, règles bientôt à réviser, règles à source unique / confiance faible (à corroborer), règles non reliées à un événement de vie, domaines à faible couverture.

Chaque cycle vise des **objectifs de couverture explicites** (ex. TVA 67 → 100 %,
Cessation 0 → 100 %), traités par des cas des familles adaptées (edge, regression).

## Deux roadmaps, en parallèle

- **Roadmap produit** (ce que voit l'utilisateur) : nouveaux domaines, missions, documents, exports.
- **Roadmap connaissance** (ce que voit l'équipe) : couverture, fraîcheur, QA, benchmark, gouvernance, dette de connaissance.

Elles avancent ensemble mais ne poursuivent pas les mêmes objectifs.

## Trois niveaux de qualité (suivis séparément)

1. **Moteur** — tests unitaires & intégration (`npm test`).
2. **Connaissance** — Knowledge QA, versioning, gouvernance (`paperasse connaissances qualite`).
3. **Réponses** — benchmark face à d'autres assistants (à construire).

Ces dimensions évoluent à des rythmes différents et se mesurent séparément.

## Principe

Le moteur ne contient **aucune règle en dur**. Ajouter/mettre à jour une règle,
un événement, un acronyme = éditer la connaissance ici (avec source + date +
version), sans toucher au moteur.

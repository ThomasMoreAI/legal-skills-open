---
title: Assistant administratif (roadmap)
layout: default
nav_order: 6
---

# Paperasse Lux → Assistant administratif luxembourgeois

Ce document est l'**audit d'architecture** et la **feuille de route** de l'évolution
de Paperasse Lux, d'une collection de calculateurs isolés vers un véritable
**assistant administratif** (moteur de diagnostic, analyse documentaire, dossiers,
échéances, courriers). Il accompagne l'implémentation du **Milestone 1**
(`lib/diagnostic/`).

Principe cardinal, non négociable : **aucune obligation, aucun délai, aucun montant
n'est affiché sans source officielle + date de vérification + niveau de confiance**,
et toute information incertaine porte la mention « validation humaine nécessaire ».

---

## 1. État des lieux de l'architecture actuelle

Paperasse Lux est une **bibliothèque Node.js ESM zéro-dépendance de production**
(dépendances lourdes en `optionalDependencies`), distribuée à la fois comme paquet
npm/CLI et comme **skills Markdown** pour agents IA.

| Couche | Emplacement | Rôle |
|---|---|---|
| Logique métier pure | `lib/<module>/index.js` | Fonctions pures (bank-parsers, faia, rts, frontaliers, lbr, bellegen-akt, ecdf, indice-statec, templates-de) |
| Points d'entrée CLI | `scripts/*.js` | Un script par commande + un `test-*.js` par module |
| Routeur unifié | `bin/paperasse` | Table `ROUTES` cmd → script, `spawn` |
| Données datées | `data/*.json`, `<skill>/data/*.json` | Chiffres officiels avec champ `as_of` |
| Schémas | `schemas/*.schema.json` | JSON Schema draft-07, validés par un validateur maison (subset, sans `ajv`) |
| Skills agents | `comptable/`, `notaire/`, `fiscaliste/`, `syndic/`, `controleur-fiscal/`, `commissaire-aux-comptes/` | `SKILL.md` + `data` + `references` + `templates` |
| Tests | `scripts/test-*.js` | Harnais maison (`test()/eq()`), 257 tests avant M1, exécutés en CI (Node 20 & 22) |
| Veille | `.github/workflows/legilux-watch.yml` | Scan hebdomadaire du Mémorial A |

**Conventions structurantes à respecter** :

- **Zéro dépendance** au runtime ; ESM (`"type": "module"`) ; Node ≥ 20.
- Fonctions **pures et déterministes**, JSDoc en français, sources citées en tête de module.
- Toute donnée réglementaire porte un `as_of` et une source (`data/sources.json`, `SOURCES.md`).
- Tests = scripts Node autonomes ajoutés au script `test` de `package.json`.
- Validateur et test-runner **maison** (pas de jest/ajv) : rester dans ce style.

## 2. Fonctionnalités déjà présentes

Calculateurs et générateurs **fiables et testés**, réutilisables tels quels :

- **Fiscalité entreprise** : IRC, ICC (communes), IF ; **TVA** (déclaration CA3) ; **FAIA** (SAF-T LU 2.01) ; **eCDF** (comptes annuels abrégés) ; états financiers ; PDF de clôture.
- **Fiscalité des personnes** : **RTS** (barème IRPP 2025, classes 1/1a/2, splitting) ; **frontaliers** FR/BE/DE (conventions, net réel) ; **indice STATEC** + SSM (indexation).
- **Notariat** : **Bëllegen Akt** (crédit 40 000 €/personne, réforme 10/2024), droits d'enregistrement, successions.
- **Registres & banque** : validation **RCS**, checklists/calendrier **LBR** ; parsers relevés **BCEE/POST/BIL/CAMT.053** ; facture conforme TVA LU + validation.
- **Outillage** : veille Légilux, contrôle de fraîcheur (`freshness`), validation de schémas.

## 3. Lacunes (au regard de la cible « assistant »)

1. **Pas de modèle d'entités** : ni profil utilisateur, ni société persistée, ni dossier, ni document, ni obligation — chaque calcul est sans état.
2. **Pas de moteur de diagnostic** reliant une *situation* à ses *obligations*.
3. **Pas d'analyse documentaire** (import courrier → extraction période/échéance/action).
4. **Pas de calendrier/rappels** ni de suivi de statut de démarche.
5. **Pas de génération de courriers** de réponse à l'administration.
6. **Base réglementaire dispersée** : les règles sont codées dans les modules, non cataloguées comme *obligations requêtables et sourcées*.
7. **Pas de persistance ni d'isolation par utilisateur** (prérequis RGPD).
8. **Interface** : CLI + skills uniquement (pas d'objectif web dans ce dépôt — la cible reste bibliothèque + agents).

## 4. Schéma de données proposé

Cinq entités, matérialisées comme **objets normalisés** (fabriques `lib/diagnostic/entities.js`)
et **schémas JSON** (`schemas/*.schema.json`) :

- **`ProfilUtilisateur`** (`user-profile.schema.json`) — identité, résidence, situation familiale, statut professionnel, frontalier, logement, sociétés liées, arrivée au LU, consentement RGPD.
- **`ProfilSociete`** (`company-profile.schema.json`) — forme, RCS, TVA, régime & fréquence TVA, salariés, exercice, statut (actif/cessation/liquidation).
- **`Dossier`** (`administrative-case.schema.json`) — catégorie, administration, statut (8 valeurs), priorité (colonnes du tableau de bord), échéance, pièces requises/reçues, informations manquantes, risques, prochaines actions, **provenance obligatoire dès qu'une échéance ou un risque est présent**.
- **`Document`** (`uploaded-document.schema.json`) — type, administration émettrice, période, texte extrait, données structurées, échéance détectée, action demandée, **incertain + validation humaine par défaut**.
- **`Obligation`** (`obligations.schema.json`, catalogue `data/obligations.json`) — population concernée, **conditions d'applicabilité déclaratives** `{champ, operateur, valeur}`, fréquence, dateLimite, autorité, pièces, pénalités, **provenance obligatoire**, statut actif/obsolète.

**Provenance** (transversale, `lib/diagnostic/provenance.js`) : `{ source, dateVerification, niveauConfiance ∈ {officiel, derive, estimation, incertain}, validationHumaineRequise }` + helper `evaluerFraicheur()` qui déclenche « à revérifier avant utilisation » au-delà de 365 jours ou si `incertain`.

## 4 bis. Couche « événements de vie » (le cerveau)

Au-dessus du catalogue d'obligations, une **ontologie des événements de vie**
(`data/evenements-vie.json` + `lib/evenements/`) transforme le catalogue plat en
**graphe** :

```
Événement → Conséquences → Administrations → Obligations → Documents → Délais → Exceptions → Checklist
```

Les obligations du graphe sont **reliées par identifiant** au catalogue
(`data/obligations.json`, source de vérité unique) : le graphe orchestre, il ne
duplique pas les règles. `resoudreEvenement(id|texte)` renvoie la chaîne
complète ; `identifierEvenement(texte)` détecte l'événement en langage naturel.
Les agents métier (TVA, CNS, Frontaliers…) deviennent alors de simples **vues**
sur ce graphe. C'est ce qui permet à une phrase comme « je m'installe avec ma
femme et deux enfants » d'ouvrir la bonne chaîne d'administrations.

## 4 ter. Couche d'orchestration (langage naturel → plan)

Au-dessus du graphe, une couche d'orchestration **déterministe** (le LLM reste
dans la couche agent, pas dans la bibliothèque) :

```
Conversation → [LLM: extraction] → lib/extraction → événements + profil
             → lib/planification (raisonnement) → plan ordonné + explications
```

- **`lib/extraction`** — contrat de la sortie LLM (`{events, entities, confidence}`), validation, et ingestion : résolution des événements + normalisation d'un profil. *Le LLM traduit, il ne décide pas.*
- **`lib/memoire`** — dossier administratif persistant (famille, employeurs, sociétés, véhicules, immobilier, documents, obligations réalisées, historique), sous consentement RGPD ; évite de reposer les mêmes questions.
- **`lib/planification`** — moteur multi-événements : fusionne les démarches, exclut le déjà-fait (mémoire), détecte les **documents mutualisés**, ordonne par **dépendances** (« commencer par ce qui débloque »), puis par urgence, et **explique** chaque étape. Ex. *Installation + Naissance + Création d'entreprise → « 12 démarches, 1 pièce mutualisée, commencer par… »*.

## 4 quater. Moteur de raisonnement & Change Impact (`lib/reasoning`)

Le planificateur répond « que faire ? » ; le reasoner répond « **qu'est-ce qui
change ?** ». On ne réexécute pas les règles : on **propage** les conséquences
d'un changement d'état dans le graphe (comme un moteur de dépendances).

- `computeDelta(avant, après)` — ce qui change entre deux situations.
- `computeImpact(état, changement)` — obligations qui apparaissent/disparaissent, valeurs dérivées modifiées (ex. classe d'impôt 1→2), domaines et événements impactés. Ex. *« je me marie » → impact fiscal (classe 1→2, sourcé) + domaines commune/ACD*.
- `simulateScenario(état, scénario)` — « et si… ? » **sans modifier le dossier** (outil de décision).
- `explainReasoning(impact)` — explication **traçable** : chaque conclusion reliée à sa cause (le champ modifié) et à sa source.
- `transition(état, changement)` — machine à états : ancien → nouvel état + impact propagé.

Les futurs agents (Analyse, Planification, Documents, Exécution) deviennent des
**interfaces** sur ce moteur commun, au lieu de silos par domaine.

## 4 quinquies. Workflow Engine & Missions (`lib/workflows`)

L'utilisateur ne veut pas « un formulaire » : il veut un **résultat** (« créer
une société »). Une **Mission** modélise ce résultat — objectif, étapes
ordonnées (du planificateur), dépendances, échéances, risques, avancement,
historique — reprenable après interruption.

Chaîne complète : `Knowledge Graph → Reasoner → Planner → Workflow Engine → Connecteurs`.

- API : `createMission`, `advanceMission`, `pauseMission`, `resumeMission`, `completeMission` (+ `reessayerEtape`, `avancement`, `prochaineEtape`).
- **Séparation stricte des actions** : `recommandation` (aucune action) → `preparation` (l'utilisateur valide) → `execution` (envoi **après confirmation explicite**, via connecteur).
- **Connecteurs = plugins** (`creerRegistreConnecteurs`) : ajouter un portail (guichet, eCDF, Peppol, email, PDF, OCR, calendar) sans modifier le moteur. Le connecteur par défaut « manuel » ne transmet rien à l'extérieur.
- Missions sérialisables (JSON) → reprise après interruption ; gestion des erreurs et réessais.

Les « agents » (Analyse, Planification, Documents, Exécution) sont des interfaces
sur ces capacités communes — pas des silos.

## 4 sexies. Qualité, explicabilité & observabilité (`lib/evaluation`)

Le moteur produit une mission ; cette couche la **juge** et la **rend auditable**.

- `evaluerMission(mission)` — rapport : **confiance globale** (score pondéré par la fiabilité des sources), **informations manquantes**, **hypothèses** (défauts non confirmés), **risques** (pénalités, échéances), **points bloquants** (prérequis non satisfaits), **sources**. Ex. *« Installation → confiance 79 %, 3 documents manquants, déclaration d'arrivée bloquante »*.
- `traceMission(mission)` — trace d'exécution auditable : `événement détecté → règle appliquée → obligation créée → étape ajoutée → connecteur sélectionné`, chaque règle reliée à sa source. Précieux pour le débogage, les audits et la confiance.

## 4 septies. Couche Outputs (artefacts métier & adaptateurs) — `lib/outputs`

Le moteur ne « se connecte » pas à des services : il **produit des artefacts
métier** et des **adaptateurs** les exportent. Ajouter une sortie (app, API,
MyGuichet, PDF, email…) = ajouter un adaptateur, sans toucher au moteur.

```
Mission → Outputs → { Timeline, DocumentPackage, Reminders, Report } → adaptateurs (.ics, Markdown, texte, JSON…)
```

- `timeline(mission)` → `TimelineEvent[]` (titre, échéance, priorité, bloquant, source, statut) ; adaptateur `.ics` (RFC 5545, VEVENT + VALARM, zéro dépendance).
- `documentPackage(mission)` → pièces à réunir (avec source) ; adaptateur Markdown.
- `reminders(mission)` → rappels avant échéance ; adaptateur texte.
- `report(mission)` → réutilise `evaluerMission` ; adaptateur Markdown.
- `produire(mission, { type, format })` + registre `ADAPTATEURS` (`enregistrerAdaptateur`) : le `.ics` n'est qu'un export parmi d'autres (demain Google/Outlook/Apple, PDF/ZIP/Peppol, email/SMS/push).

## 4 octies. La connaissance comme actif (`knowledge/`)

Le moteur est mature ; le facteur limitant devient la **qualité et la fraîcheur
de la connaissance réglementaire**. Le dossier `knowledge/` la sépare du code.

- **Versioning réglementaire** : chaque obligation porte `validite` (`validFrom`, `validUntil`, `juridiction`, `langue`, `version`, `lastVerified`). `enVigueurLe()` / `catalogueEnVigueur()` → *« réponse valable pour les règles en vigueur au 1er janvier 2027 »*.
- **Knowledge QA** (`knowledge/qa/`) : cas métier de référence (profil/événements → nombre attendu d'obligations/démarches), rejoués comme non-régression de la connaissance.
- **Glossaire** (`knowledge/glossary.json`) : acronymes expliqués et sourcés.

Prochains cycles à investir surtout ici : élargir les cas QA, un benchmark
(exactitude/exhaustivité/traçabilité), puis un premier connecteur externe réel.

## 5. Plan de migration (évolution progressive, sans réécriture)

1. **Ajouter** `lib/diagnostic/` **à côté** de l'existant — aucune modification des modules actuels (compatibilité totale, tests existants intacts).
2. **Cataloguer** progressivement les règles dans `data/obligations.json` (sourcées) au lieu de les recoder.
3. **Brancher** les calculateurs existants comme *exécuteurs* d'obligations (ex. l'obligation « déclaration TVA » réutilise `scripts/calc-tva-declaration.js` ; « RTS » réutilise `lib/rts`). Le moteur **oriente**, les modules **calculent**.
4. **Persister** via un store JSON local isolé par propriétaire (`lib/diagnostic/store.js`), extensible ensuite au chiffrement (M12).
5. **Enrichir** domaine par domaine en suivant l'ordre des milestones, chaque ajout étant testé et sourcé avant d'être considéré « terminé ».

## 6. Milestones techniques

| # | Milestone | Traduction technique dans ce dépôt |
|---|---|---|
| 1 | Socle & modèle de données | `lib/diagnostic/` (entités, provenance, moteur, store) + schémas + catalogue amorce ✅ |
| 2 | Diagnostic universel | `questionnaire.js` (questions utiles uniquement) + `dashboard.js` (5 colonnes) ✅ |
| 3 | Analyse documentaire | `lib/documents/` : classification, dates/montants/références/échéance/action/conséquences → résumé + checklist + projet de réponse + Dossier ✅ |
| 4 | Module TVA complet | `lib/tva/` : calendrier, périodes/déclarations manquantes, contrôle de cohérence (réutilise `calc-tva-declaration`), rapprochement courrier AED ✅ |
| 5 | Indépendants & sociétés | `lib/entreprise/` : parcours par phase (création→vie→fiscalité→employeur→cessation), pièces manquantes, échéances par société ; réutilise `lib/lbr` ✅ |
| 6 | Particuliers & frontaliers | `lib/particulier/` : parcours par domaine, classe d'impôt, analyse frontalière + fiche de paie ; réutilise `lib/rts`, `lib/frontaliers` ✅ |
| 7 | Résidence & immigration | `lib/residence/` : parcours « Je m'installe au Luxembourg » (5 phases, UE / hors UE, échéances depuis l'arrivée) ✅ |
| 8 | Logement | `lib/logement/` : parcours locataire/acheteur/propriétaire/vendeur, intègre Bëllegen Akt + garantie locative ✅ |
| 9 | Génération de courriers | `lib/courriers/` : 9 types de courriers-projets + pré-remplissage depuis analyse (M3) + dossier récap ✅ |
| 10 | Calendrier & rappels | `lib/rappels/` : alertes couleur (rouge/orange/jaune/vert), rappels avant échéance, documents manquants, calendrier trié ✅ |
| 11 | Base de connaissances | `lib/connaissances/` : base unifiée requêtable, registre de sources élargi, fraîcheur, citation garde-fou ✅ |
| 12 | Sécurité & RGPD | `lib/rgpd/` : chiffrement AES-256-GCM, masquage, journal d'accès, consentement, conservation/purge, store sécurisé ✅ |
| 13 | Interface & i18n | `lib/i18n/` : libellés fr/en/de/lb, tableau de bord localisé ✅ |
| 14 | Conversationnel | `lib/conversation/` + `SKILL.md` : intention → profil → obligations → action, jamais de démarche ✅ |
| 15 | Tests & qualité | `scripts/test-scenarios.js` : 15 scénarios de bout en bout ✅ |

## 7. Fichiers créés / modifiés (Milestone 1)

**Créés** : `lib/diagnostic/{provenance,entities,engine,store,index}.js` · `data/obligations.json` ·
`schemas/{obligations,user-profile,company-profile,administrative-case,uploaded-document}.schema.json` ·
`scripts/diagnostic.js` · `scripts/test-diagnostic.js` · `docs/assistant-administratif.md`.

**Modifiés (additifs, non cassants)** : `bin/paperasse` (routes `diagnostic` / `test:diagnostic` + aide) ·
`package.json` (scripts `diagnostic`, `test:diagnostic`, ajout au `test`) · `CHANGELOG.md`.

## 8. Risques

- **Exactitude réglementaire** : une obligation mal datée induit l'utilisateur en erreur → mitigé par `provenance` obligatoire + `evaluerFraicheur` + niveaux de confiance + mention validation humaine.
- **Périmètre** : la cible est vaste ; risque de code superficiel → mitigé par la livraison milestone par milestone, chacun testé.
- **Attente produit ≠ dépôt** : le brief d'origine visait une web-app (Replit) ; ce dépôt est une bibliothèque/CLI/skills. La feuille de route respecte cette nature (pas de front-end imposé).
- **RGPD** : données sensibles (revenus, immigration) → store isolé par propriétaire dès M1, chiffrement en M12.
- **Faux négatifs de diagnostic** : un champ de profil non renseigné pourrait masquer une obligation → traité explicitement (colonne « informations manquantes »).

## 9. Dépendances

**Aucune dépendance runtime ajoutée** (contrainte du projet respectée). Node ≥ 20, ESM.
Le moteur s'appuie uniquement sur `node:fs`, `node:path`, `node:url`. L'analyse
documentaire (M3) introduira des dépendances **optionnelles** (OCR/PDF) sur le
modèle des `optionalDependencies` existantes.

## 10. Milestone 1 — livré

`lib/diagnostic/` fournit : le modèle d'entités sourcé, la traçabilité obligatoire,
le moteur profil → obligations → échéances → dossiers, un store local isolé, et un
catalogue d'obligations amorce (7 obligations sourcées : TVA mensuelle/trimestrielle/
annuelle, dépôt comptes RCS, RBE, déclaration d'arrivée commune, IRPP modèle 100).

CLI : `paperasse diagnostic obligations | profil | societe`. **29 tests** (`test:diagnostic`),
intégrés à la CI. Aucune action externe déclenchée, aucune règle codée en dur dans le moteur.

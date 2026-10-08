# DPO — Délégué à la Protection des Données

## Textes de référence

- **RGPD** : Articles 37, 38, 39
- **Lignes directrices EDPB** : WP243 rev.01 — Lignes directrices concernant les délégués à la protection des données
- **CNIL** : https://www.cnil.fr/fr/designation-dpo

---

## 1. Quand la désignation d'un DPO est-elle obligatoire ? (Art. 37)

### 1.1 Cas de désignation obligatoire

La désignation d'un DPO est **obligatoire** dans trois cas :

| Cas | Article | Exemples |
|-----|---------|----------|
| **Autorité ou organisme public** | Art. 37.1.a | Mairies, départements, établissements publics, organismes de sécurité sociale |
| **Suivi régulier et systématique à grande échelle** | Art. 37.1.b | Banques, assurances, opérateurs télécom, plateformes en ligne, vidéosurveillance à grande échelle |
| **Traitement à grande échelle de données sensibles ou relatives aux condamnations** | Art. 37.1.c | Hôpitaux, laboratoires d'analyses, mutuelles, associations de santé |

### 1.2 Qu'est-ce que "à grande échelle" ?

La CNIL et l'EDPB considèrent les critères suivants :
- Nombre de personnes concernées (en valeur absolue ou en proportion de la population)
- Volume de données traitées
- Étendue géographique du traitement
- Durée ou permanence du traitement

**Exemples "grande échelle" :** Base nationale de patients, fichier de 100 000+ clients, vidéosurveillance d'un centre commercial.
**Exemples "pas grande échelle" :** Médecin individuel, avocat individuel, petit commerce.

### 1.3 Cas de désignation recommandée (mais pas obligatoire)

Même si le DPO n'est pas obligatoire, la CNIL **recommande fortement** sa désignation pour :
- Les entreprises de plus de 50 salariés qui traitent des données personnelles de manière significative
- Les organisations qui font de la prospection commerciale
- Les sous-traitants qui traitent des données pour le compte d'autres organisations
- Les organisations qui utilisent des technologies de suivi (cookies, tracking, profilage)

### 1.4 Cas des associations

| Type d'association | DPO obligatoire ? |
|-------------------|-------------------|
| Association de santé (patients, bénéficiaires) | **OUI** si traitement de données de santé à grande échelle |
| Association > 1000 adhérents avec profilage | **Probablement OUI** (suivi régulier et systématique) |
| Petite association (< 100 adhérents, pas de données sensibles) | **NON** mais recommandé |
| Association gérant des données judiciaires (aide aux victimes) | **OUI** si grande échelle |

---

## 2. Rôle et missions du DPO (Art. 39)

### 2.1 Missions obligatoires

| Mission | Détail |
|---------|--------|
| **Informer et conseiller** | Informer le responsable de traitement et les employés de leurs obligations RGPD |
| **Contrôler la conformité** | Vérifier le respect du RGPD, des politiques internes, la sensibilisation du personnel |
| **Conseiller sur les AIPD** | Donner un avis sur les analyses d'impact et vérifier leur exécution |
| **Coopérer avec la CNIL** | Être le point de contact avec l'autorité de contrôle |
| **Point de contact** | Être le point de contact pour les personnes concernées (exercice des droits) |

### 2.2 Ce que le DPO ne fait PAS

- Le DPO **ne décide pas** des traitements — c'est le responsable de traitement
- Le DPO **n'est pas responsable** de la non-conformité — c'est le responsable de traitement
- Le DPO **ne peut pas être sanctionné** pour des manquements de l'organisation
- Le DPO **ne peut pas recevoir d'instructions** sur la manière d'exercer ses missions

### 2.3 Garanties d'indépendance (Art. 38)

- Le DPO **ne peut pas être relevé de ses fonctions** ou pénalisé pour l'exercice de ses missions
- Le DPO doit **rendre compte directement** au niveau le plus élevé de la direction
- Le DPO ne doit pas avoir de **conflit d'intérêts** (ne peut pas être DG, DAF, DSI, DRH, responsable marketing en même temps)
- Le DPO doit disposer de **ressources suffisantes** pour exercer ses missions

---

## 3. DPO interne vs externalisé

| Critère | DPO interne | DPO externalisé |
|---------|-------------|-----------------|
| **Coût** | Salaire + formation continue | Forfait mensuel (généralement moins cher pour les PME) |
| **Disponibilité** | Temps plein ou partiel | Selon contrat (typiquement 0,5-2 j/mois) |
| **Indépendance** | Risque de conflit d'intérêts | Indépendance structurelle (pas de lien hiérarchique) |
| **Expertise** | Dépend de la personne | Expertise mutualisée sur plusieurs organisations |
| **Connaissance métier** | Excellente | À construire (mais compensée par l'expérience multi-secteurs) |
| **Adapté pour** | Grandes organisations (> 250 sal.) | PME, ETI, associations |

### Recommandation

Pour les PME et associations (< 250 salariés), le **DPO externalisé** est souvent la solution la plus pertinente :
- Coût maîtrisé (forfait mensuel)
- Expertise garantie et à jour
- Pas de problème de conflit d'intérêts
- Mutualisation des bonnes pratiques entre organisations clientes

---

## 4. Processus de déclaration à la CNIL

### 4.1 Désignation

La désignation du DPO se fait **en ligne** sur le site de la CNIL :
- **URL :** https://www.cnil.fr/fr/designation-dpo
- **Formulaire :** https://designations.cnil.fr/dpo/designation/

### 4.2 Informations requises

| Information | Détail |
|-------------|--------|
| Identité de l'organisme | SIREN, raison sociale, adresse |
| Identité du DPO | Nom, prénom, coordonnées professionnelles |
| Type de DPO | Interne ou externe |
| Coordonnées publiques du DPO | Email et/ou adresse postale (publié sur le registre CNIL) |

### 4.3 Publication

- Le DPO désigné est **publié** dans le registre public de la CNIL
- C'est cette publication qui est vérifiable par le data-pipe `cnil` du skill prospect-scorer
- L'absence de publication pour une entité qui devrait avoir un DPO est un **signal de non-conformité**

### 4.4 Modification et fin de mission

- Toute **modification** des coordonnées du DPO doit être déclarée à la CNIL
- La **fin de mission** du DPO doit être notifiée à la CNIL
- Un nouveau DPO doit être désigné si l'obligation persiste

---

## 5. Compétences requises du DPO (Art. 37.5)

Le DPO est désigné sur la base de :
- Ses **qualités professionnelles** (expertise juridique et technique en matière de protection des données)
- Sa **connaissance** de la législation et des pratiques en matière de protection des données
- Sa capacité à accomplir les **missions** décrites à l'article 39

Il n'existe pas de certification obligatoire, mais la **certification DPO CNIL** (norme NF) est un gage de compétence reconnu.

**Ressource CNIL :** https://www.cnil.fr/fr/certification-des-competences-du-dpo

---

## 6. Points de vigilance fréquents

| Erreur fréquente | Solution |
|------------------|----------|
| DPO = DSI (conflit d'intérêts) | Désigner une autre personne ou externaliser |
| DPO sans moyens | Allouer un budget et du temps dédié |
| DPO non déclaré à la CNIL | Faire la déclaration en ligne |
| DPO "fantôme" (désigné mais inactif) | Mettre en place un plan d'action annuel |
| Pas de DPO alors qu'obligatoire | Désigner immédiatement (interne ou externe) |
| DPO qui décide des traitements | Clarifier les rôles (le DPO conseille, le RT décide) |

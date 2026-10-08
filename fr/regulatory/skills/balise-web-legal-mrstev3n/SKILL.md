---
name: balise-web-legal-mrstev3n
title: Conformité juridique des sites
description: 'Auditer et préparer les informations juridiques d''un site, d''une application ou d''un service numérique multi-juridiction : mentions légales, politique de confidentialité, information au point de collecte, politique et interface cookies, informations e-commerce et plan d''implémentation. Utiliser en priorité pour les juridictions d''Afrique francophone — Bénin, Burkina Faso, Cameroun, RCA, Tchad, Comores, Congo, Côte d''Ivoire, Gabon, Guinée, Mali, Niger, RDC, Sénégal et Togo — et pour leurs superpositions avec le Ghana, la France/UE (RGPD) ou le Canada/Québec. Produit un travail préparatoire qui ne constitue ni une certification de conformité ni un substitut à la validation d''un professionnel du droit habilité.'
author: mrstev3n
author_url: https://github.com/mrstev3n/balise-skills/tree/main/skills/balise-web-legal
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: fr
practice: regulatory
language: fr
sources:
- title: Applicability Router
  path: references/applicability-router.md
- title: Audit And Evidence
  path: references/audit-and-evidence.md
- title: Cookies And Interface
  path: references/cookies-and-interface.md
- title: Document Set
  path: references/document-set.md
- title: International Overlays
  path: references/international-overlays.md
- title: Jurisdictions Central Africa
  path: references/jurisdictions-central-africa.md
- title: Jurisdictions Comoros
  path: references/jurisdictions-comoros.md
- title: Jurisdictions Eu France
  path: references/jurisdictions-eu-france.md
- title: Jurisdictions West Africa
  path: references/jurisdictions-west-africa.md
- title: Legal Notices Ecommerce
  path: references/legal-notices-ecommerce.md
- title: Privacy Notice
  path: references/privacy-notice.md
- title: Verification And Delivery
  path: references/verification-and-delivery.md
---

# Conformité juridique des sites

Travailler comme assistant de recherche, d'audit et de rédaction. Partir du produit et des traitements réels, puis déterminer les juridictions et documents requis. Une page juridique ne prouve jamais, à elle seule, la conformité opérationnelle.

## Verrou préalable obligatoire

Pour chaque nouveau site, produit, service ou audit, interrompre le traitement avant toute inspection, recherche, analyse de conformité ou rédaction substantielle. Dans la première réponse, poser le questionnaire de cadrage ci-dessous et ne fournir ni audit, ni conclusion de conformité, ni document juridique dans ce même message.

Appliquer ce verrou même si les réponses semblent déjà présentes dans la conversation, les pièces, le code ou le site fourni. Ne pas préremplir, déduire ni confirmer ces réponses à la place de l'utilisateur. L'utilisateur doit répondre lui-même ou autoriser explicitement l'agent à utiliser les informations déjà connues. Une formule comme « utilise ce que tu sais déjà » permet alors de construire la fiche depuis le contexte, de signaler les informations incertaines et de ne demander que les éléments encore manquants.

Poser les questions en une seule série courte :

1. Quel résultat attendez-vous : diagnostic initial, audit documenté, rédaction, correction d'interface, plan d'implémentation ou préparation à une validation juridique ?
2. Quelle entité représentez-vous et quel est son rôle dans le service ?
3. Quelles entités éditent, exploitent, vendent ou fournissent le service ? Pour chacune, indiquez l'identité, la forme ou le statut, le pays d'établissement et le rôle.
4. Quels pays sont réellement ciblés et quelles catégories de personnes utilisent le service ?
5. Quel est l'état du produit : conception, test, accès restreint ou service public déjà exploité ? Quelles fonctions impliquent comptes, formulaires, paiements, communications, données personnelles ou traceurs ?
6. Quels prestataires, hébergeurs, outils de mesure, moyens de paiement ou transferts internationaux sont connus ?
7. Quels documents, registres, contrats, configurations ou preuves sont disponibles ? Existe-t-il une date de lancement, de publication, de contrôle ou une autre échéance ?

Après la réponse de l'utilisateur, restituer une fiche de cadrage concise, distinguer les faits confirmés des inconnues, puis seulement commencer le travail demandé. Si une réponse reste inconnue, utiliser `[À CONFIRMER]` et expliquer précisément ce qui peut être préparé sans elle. Ne pas redéclencher le questionnaire au sein du même dossier, sauf changement d'entité, de produit, d'objectif ou de marché. Les questions portant uniquement sur le fonctionnement ou le périmètre du skill ne déclenchent pas ce verrou.

## Principes obligatoires

1. Ne pas appliquer le RGPD, la CNIL française, la loi québécoise ou une durée standard par automatisme.
2. Distinguer l'établissement de l'éditeur, les marchés ciblés, les personnes concernées, les lieux de traitement, les prestataires, les transferts et les critères extraterritoriaux de chaque loi.
3. Vérifier en ligne le texte en vigueur, ses modifications, sa publication, son entrée en vigueur, ses décrets et les formalités de l'autorité compétente.
4. Ne jamais inventer identité, forme, RCCM, IFU, capital, représentant, récépissé, autorisation, hébergeur, prestataire, cookie, finalité, base juridique, durée ou transfert.
5. Séparer : fait observé, information fournie, exigence sourcée, interprétation, recommandation et élément non vérifié.
6. Ne pas déclarer un site « conforme » sans preuve sur les traitements, contrats, mesures, formalités et comportement réel de l'interface.

## Collaboration optionnelle avec d'autres skills

Ce skill reste autonome. Ne jamais exiger, installer ni activer automatiquement un autre skill pour poursuivre le travail.

- Utiliser `balise-ohada` s'il est disponible pour les questions nationales africaines, OHADA, d'identité juridique, de registre, de droit des sociétés ou d'activité réglementée qui dépassent les pages et interfaces du service.
- Lorsque le routeur confirme l'application du droit UE ou français, utiliser `lawve-privacy-policy-eu`, `lawve-cookie-policy-eu` ou `lawve-source-verification` si le complément pertinent est déjà disponible et si son périmètre correspond à la question.
- Si le complément pertinent est absent, le recommander brièvement seulement lorsqu'il améliorerait matériellement le résultat, puis poursuivre avec les références internes, les sources officielles et des limites explicites. Ne jamais bloquer la mission sur cette absence.
- Ne jamais laisser un complément européen remplacer l'analyse séparée des obligations africaines également applicables.

## Références à lire

- Lire [applicability-router.md](references/applicability-router.md) au début de chaque mission.
- Lire [audit-and-evidence.md](references/audit-and-evidence.md) pour inspecter un produit existant ou cadrer un produit en construction.
- Lire [document-set.md](references/document-set.md) pour déterminer les pages et informations nécessaires.
- Lire [privacy-notice.md](references/privacy-notice.md) avant de rédiger ou réviser une politique de confidentialité.
- Lire [cookies-and-interface.md](references/cookies-and-interface.md) pour les traceurs, le bandeau et la gestion des préférences.
- Lire [legal-notices-ecommerce.md](references/legal-notices-ecommerce.md) pour l'identification de l'éditeur et les informations e-commerce.
- Lire le profil approprié : [jurisdictions-west-africa.md](references/jurisdictions-west-africa.md), [jurisdictions-central-africa.md](references/jurisdictions-central-africa.md), [jurisdictions-comoros.md](references/jurisdictions-comoros.md), [jurisdictions-eu-france.md](references/jurisdictions-eu-france.md) ou [international-overlays.md](references/international-overlays.md).
- Lire [verification-and-delivery.md](references/verification-and-delivery.md) avant toute livraison.

## Workflow

### 1. Formaliser le cadrage validé

À partir des réponses au questionnaire obligatoire, relever le propriétaire du service, les entités impliquées, le type de produit, les pays d'établissement et de ciblage, les catégories d'utilisateurs, le secteur, les langues, les fonctions et le stade du projet. Ne pas remplacer une inconnue par une déduction. Après le cadrage initial, demander seulement les informations nouvelles susceptibles de changer le droit applicable ou le contenu.

### 2. Auditer

Inventorier pages, formulaires, comptes, paiements, messages, fichiers, journaux, traceurs, stockage local, SDK, contenus embarqués, prestataires, hébergement, transferts et paramètres de consentement. Marquer chaque élément `observé`, `fourni`, `déduit à confirmer` ou `inconnu`.

### 3. Router

Produire une matrice par juridiction et par matière : données personnelles, communications/traceurs, identité de l'éditeur, commerce électronique, consommation, secteur réglementé et paiements. Appliquer la collaboration optionnelle définie ci-dessus, puis traiter tout régime restant avec les références internes et les sources officielles. Si le droit UE ou français est applicable, lire [jurisdictions-eu-france.md](references/jurisdictions-eu-france.md), sans remplacer les obligations africaines également applicables.

### 4. Définir le jeu documentaire

Décider séparément si le produit requiert : mentions légales, politique de confidentialité, notices courtes au point de collecte, politique cookies, interface de consentement, CGU, CGV, informations précontractuelles, procédure d'exercice des droits ou informations d'application mobile.

### 5. Rédiger

Rédiger à partir des faits vérifiés et des exigences sourcées. Utiliser des marqueurs `[À CONFIRMER]` pour les données manquantes qui empêchent la finalisation. Ne pas transformer une formalité à accomplir en numéro fictif. Préserver les variantes nationales lorsqu'une fusion serait trompeuse.

### 6. Contrôler l'implémentation

Vérifier que les liens sont accessibles avant la collecte, que les notices courtes renvoient au bon document, que l'interface respecte les choix, que les traceurs observés correspondent au tableau publié et que les versions linguistiques sont cohérentes.

### 7. Livrer

Livrer les projets, la matrice des sources, le registre des informations manquantes et le plan d'implémentation. Indiquer la date de vérification et les limites. Recommander une validation locale lorsque le texte officiel est inaccessible, la formalité incertaine, le risque élevé ou plusieurs lois entrent en conflit.

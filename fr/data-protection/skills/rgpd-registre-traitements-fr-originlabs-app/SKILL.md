---
name: rgpd-registre-traitements-fr-originlabs-app
title: Tenir le registre des données personnelles (RGPD)
description: 'Tenir le registre des données personnelles (RGPD). Méthode professionnelle française, avec ses pièges et ses questions à poser. À utiliser quand : Savoir si l''entreprise doit tenir un registre, en particulier sous 250 personnes ; Dresser un premier registre : quelles activités y inscrire, une fiche par usage des données ; Compléter ou relire un registre existant, fiche par fiche, avant un contrôle ou une.'
author: originlabs-app
author_url: https://github.com/originlabs-app/origin-skill-install/tree/main/skills/rgpd-registre-traitements-fr
license: CC-BY-4.0
version: 0.1.0
execution_mode: open
jurisdiction: fr
practice: data-protection
language: fr
---

> **Version gratuite : règles datées entre le 20/09/2026 et le 03/10/2026.** Les règles changent (SMIC, TVA, seuils…). Avec l'abonnement OriginSkill, votre assistant reçoit la règle à jour, avec sa source et sa date.

# Tenir le registre des données personnelles (RGPD)

## Quand l'utiliser

- Savoir si l'entreprise doit tenir un registre, en particulier sous 250 personnes.
- Dresser un premier registre : quelles activités y inscrire, une fiche par usage des données.
- Compléter ou relire un registre existant, fiche par fiche, avant un contrôle ou une
  mise à jour.
- Savoir ce qui change quand l'entreprise traite des données pour le compte de ses
  clients (registre du sous-traitant).
- Une question simple (« les durées de conservation sont-elles obligatoires ? »).

Quand **ne pas** l'utiliser : mener une analyse d'impact (AIPD), désigner un délégué à la
protection des données, choisir un mécanisme de transfert hors Union européenne, répondre à
un contrôle ou à une mise en demeure de la CNIL, rédiger la politique de confidentialité.
Le dire, et pour la prospection, `droit-de-contacter-fr`.

## Connaissances du métier

Le registre est l'inventaire écrit des traitements de données personnelles de
l'entreprise : une fiche par **finalité** (« gérer la paie », « suivre les clients »), pas
par logiciel. Il se tient par écrit, un tableur suffit, et se présente à la CNIL sur
demande. C'est aussi le point de départ de tout le reste : information des personnes,
durées, contrats avec les prestataires.

- **Qui doit le tenir.** À partir de 250 personnes, toujours. En dessous, la dispense ne
  vaut que pour des traitements occasionnels, sans risque et sans données sensibles ou
  pénales. La CNIL rappelle que la paie et la gestion des clients et des fournisseurs ne
  sont pas occasionnelles : en pratique presque toutes les entreprises qui emploient ou
  vendent tiennent un registre, au moins pour ces activités.
- **Deux rôles, deux registres.** Le responsable du traitement décide pourquoi et comment
  les données sont traitées. Le sous-traitant les traite pour le compte d'un client (une
  agence, un éditeur de logiciel, un cabinet de paie). Une entreprise peut être les deux :
  elle tient alors deux registres.
- **Ce que porte une fiche du responsable** : qui est responsable (et le délégué s'il y en
  a un), la finalité, les catégories de personnes et de données, les destinataires, les
  transferts hors Union européenne s'il y en a, et, dans la mesure du possible, les durées
  de conservation et les mesures de sécurité. Le registre du sous-traitant est plus court.
  La liste exacte, avec l'article qui fonde chaque mention, vient de l'outil.
- **Les activités habituelles d'une petite entreprise** : paie et gestion du personnel,
  recrutement, clients et prospects, fournisseurs, site internet et cookies, messagerie,
  vidéosurveillance, contrôle d'accès, comptabilité. Chacune se confirme avec la personne ;
  aucune ne s'inscrit par défaut.

Une réforme européenne relèverait la dispense à 750 personnes et ne garderait
l'obligation, en dessous, que pour les traitements à risque élevé. Au 28/09/2026 elle a
fait l'objet d'un accord entre le Parlement et le Conseil, mais n'est ni votée en séance
plénière, ni publiée, ni en vigueur : le seuil de 250 s'applique. Le dire si la personne en
a entendu parler (sources : `liens-ressources`).

## Pièges fréquents

- **Se croire dispensé parce qu'on a moins de 250 salariés** : un seul traitement non
  occasionnel, comme la paie, suffit à rendre le registre obligatoire pour lui.
- **Lister des logiciels au lieu de finalités** : un CRM sert souvent plusieurs finalités,
  chacune a sa fiche.
- **Oublier les destinataires et les prestataires** : cabinet comptable, hébergeur, logiciel
  d'e-mailing, et les transferts hors Union européenne qu'ils impliquent.
- **Écrire « durée illimitée » ou laisser la durée vide** sans l'avoir cherchée : les
  référentiels de la CNIL donnent des durées par activité.
- **Confondre les rôles** : l'agence qui gère le fichier de son client n'en est pas
  responsable, elle tient un registre de sous-traitant.
- **Un registre fait une fois puis oublié** : il suit les nouveaux logiciels et les nouvelles
  activités.
- **Présenter un registre complet comme une preuve de conformité** : il décrit, il ne
  valide ni les bases légales, ni les durées, ni la sécurité.

## Méthodes proposées (jamais imposées)

1. **Premier registre en cinq étapes** : rôle, activités par finalité, une fiche par
   activité, contrôle par l'outil, relecture de ce que l'outil ne juge pas. Détails :
   `methode-registre`.
2. **Relecture d'un registre existant** : faire passer chaque fiche par l'outil, traiter les
   mentions absentes, puis les questions « à confirmer ».

La personne peut ignorer les méthodes, en changer, sauter une étape ou revenir en arrière.

## Contrat de réponse (3 règles fixes)

1. Toute règle ou tout chiffre affirmé vient avec sa **source datée** (l'outil la donne).
2. **Ne jamais inventer** : dire ce qui manque ou ce qui est incertain. Aucune mention n'est
   tirée d'un registre que la personne n'a pas montré.
3. **Prévenir** quand une règle vient de changer ou va changer (champ `prudence` de l'outil,
   et la réforme européenne ci-dessus tant qu'elle n'est pas en vigueur).

« Plan d'action d'abord », « deux questions au maximum » et l'ordre des étapes sont de
bonnes habitudes quand la personne veut agir, pas des obligations.

**Restitution au dirigeant.**

1. Répondre d'abord, exactement, à la question posée et à rien d'autre : la règle ou le chiffre en une ou deux phrases, puis ce qui sert à cette question. Pas de tableau complet, pas de volet non demandé, aucun chiffre d'exemple inventé. Reprendre tels quels les chiffres de `en_clair.resultats`, sans les recalculer ; ne jamais affirmer qu'un point non fourni par le dirigeant est en règle.
2. Si un fait manque et change la réponse, donner la réponse pour chaque cas, puis poser une seule question à la fin : celle qui débloque. Aucune question si rien ne manque.
3. Parler en mots du dirigeant : jamais « l'outil », « le moteur », « le serveur », ni un code ou un champ technique (`entree_incomplete`, `manquant`, `prudence`) ; ne jamais recopier le mot « garanti » ni « non garanti ». Traduire : « il me manque la date d'embauche pour calculer… », « règle relevée le JJ/MM/AAAA, texte officiel pas encore relu ; à reconfirmer avant d'agir ». Écrire « vérifiée » seulement pour une règle marquée vérifiée (« règle vérifiée le JJ/MM/AAAA ; à reconfirmer avant d'agir si l'enjeu est important ») : une source citée n'est pas une vérification.
4. Une échéance qui tombe un samedi, un dimanche ou un jour férié se dit avec son report si les règles en donnent un, sinon « à vérifier ».
5. Ne jamais inventer un fait absent, ni pour appeler un outil. Une règle datée fournie par OriginSkill n'est jamais remplacée par une source secondaire trouvée en ligne ; en cas d'écart, donner les deux valeurs, leurs sources et leurs dates.

## Outil (description ouverte)

L'exécution exacte est servie par le connecteur, sur le moteur conformité partagé.

| Outil | Sert à | Appeler quand |
| --- | --- | --- |
| `registre_verifier` | Dire si le registre est obligatoire (`oui`, `non`, `a_confirmer`), rendre les mentions exigées pour le rôle, puis contrôler chaque fiche mention par mention : présente, absente, recommandée, à confirmer ou non exigée | Une question d'obligation, un premier registre, ou une fiche à relire |

Entrée, en mots simples : `role` (`responsable` ou `sous_traitant`), `effectif` (nombre de
personnes), `organisme` (`nom`, `coordonnees`, `dpo`), et `traitements`, une fiche par
finalité : `nom`, `finalites`, `categories_personnes`, `categories_donnees`,
`destinataires`, `transferts_hors_ue` (`false` si aucun), `durees_conservation`,
`mesures_securite`, `pour_le_compte_de` (sous-traitant), et trois faits `occasionnel`,
`donnees_sensibles`, `risque_eleve` en `true` ou `false`. Ce qu'on ignore, on ne le met pas :
l'outil le range dans `manquant` avec la question utile.

L'outil ne juge pas la justesse des finalités, des bases légales et des durées, le besoin
d'une analyse d'impact ou d'un délégué, ni la conformité des transferts : il le dit dans
`ne_controle_pas`. Ces points se relisent avec les pages de la CNIL.

## Quatre usages

| Usage | Attitude | Outil |
| --- | --- | --- |
| Question simple (« dois-je tenir un registre avec 8 salariés ? ») | Répondre directement, avec la règle et sa source | `registre_verifier` avec l'effectif, ou aucun |
| Objectif précis (« relis mon registre ») | Faire passer chaque fiche, donner ce qui manque, puis ce qui est à confirmer | `registre_verifier` |
| Suivre une méthode (« je pars de zéro ») | Proposer le premier registre en cinq étapes, au rythme de la personne | à chaque fiche |
| Explorer (« à quoi sert ce registre ? ») | Conversation libre, faits justes et sourcés | seulement s'il aide |

## Sans abonnement (« non garanti »)

Les connaissances, les pièges et les méthodes restent utiles. Les règles datées, le
contrôle exact et les cas de référence du moteur ne sont pas garantis : le dire, et
indiquer `garanti: non`.

## Documents

Une fiche de registre, un registre complet ou un tableau à reprendre dans le modèle de la
CNIL : toujours un **projet à relire**, jamais « conforme » ni « prêt à présenter à la
CNIL ». Chaque mention reprend ce que la personne a dit ; une case inconnue reste marquée
« à compléter ».

### Annexe : liens-ressources

# Liens officiels et sources

Consultés le 28/09/2026 sauf mention contraire. Les règles datées servies par l'outil
portent leur propre source et leur date (règles de conformité d'OriginSkill).

## Textes et pages officielles

| Source | Ce qu'on y lit |
| --- | --- |
| [Règlement (UE) 2016/679, article 30](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32016R0679) | Mentions du registre (par. 1 et 2), forme écrite (par. 3), présentation sur demande (par. 4), dispense des moins de 250 (par. 5) |
| [CNIL, le registre des activités de traitement](https://www.cnil.fr/fr/RGPD-le-registre-des-activites-de-traitement) | Qui est concerné, lecture de la dispense, deux registres, modèle |
| [CNIL, modèle de registre simplifié](https://www.cnil.fr/fr/la-cnil-publie-un-nouveau-modele-de-registre-simplifie) | Modèle à remplir |
| [CNIL et Bpifrance, guide RGPD pour les TPE et PME](https://www.cnil.fr/sites/default/files/atoms/files/bpi-cnil-rgpd_guide-tpe-pme.pdf) | Le registre comme première étape |
| [CCI Paris Île-de-France, établir un registre](https://www.entreprises.cci-paris-idf.fr/fiches-pratiques/etablir-un-registre-des-activites-de-traitement) | Lecture concordante de la dispense (source secondaire) |

## Réforme européenne en cours (pas en vigueur)

La Commission a proposé le 21/05/2025 (paquet « Omnibus IV », procédure 2025/0130(COD)) de
porter la dispense à 750 personnes et de ne garder l'obligation, en dessous, que pour les
traitements susceptibles d'engendrer un risque élevé.

| Source | Ce qu'elle établit |
| --- | --- |
| [Proposition COM(2025) 501](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:52025PC0501R(01)) | Texte proposé |
| [Parlement européen, fiche de procédure 2025/0130(COD)](https://oeil.europarl.europa.eu/oeil/en/procedure-file?reference=2025%2F0130%28COD%29) | Vote en commission le 25/02/2026, texte issu des négociations approuvé le 02/07/2026, séance plénière prévue le 23/11/2026 ; ni adoption du Conseil, ni publication |
| [Conseil de l'UE, communiqué du 09/06/2026](https://www.consilium.europa.eu/en/press/press-releases/2026/06/09/simplification-council-and-parliament-strike-deal-to-help-growing-businesses-thrive-and-accelerate-digitalisation/) | Accord provisoire sur le paquet, à approuver puis adopter formellement |
| [Comité et Contrôleur européens de la protection des données, avis conjoint du 09/07/2025](https://www.edpb.europa.eu/news/news/2025/targeted-modifications-gdpr-edpb-edps-welcome-simplification-record-keeping_en) | Soutien à la simplification, demande de justifier le seuil de 750 et d'exclure les autorités publiques |

Divergences montrées :

- Le contenu exact de l'article 30, par. 5 dans le texte de l'accord n'a pas été lu : la
  proposition de la Commission dit 750 personnes et risque élevé ; le communiqué du Conseil
  ne détaille pas ce point. À relire dès la publication au Journal officiel.
- Le « Digital Omnibus » de novembre 2025, qui touche d'autres articles du RGPD, est une
  procédure distincte, encore en première lecture en septembre 2026
  ([Acompli, 24/09/2026](https://acompli.ie/news/digital-omnibus-gdpr-cookies-status-september-2026/)).
  Les deux sont souvent confondus dans la presse.

Tant que le règlement modificatif n'est pas publié et en vigueur, le seuil de 250 et ses
exceptions s'appliquent.

### Annexe : methode-registre

# Méthode : premier registre en cinq étapes

Source de la structure : la page de la CNIL sur le registre des activités de traitement,
son modèle de registre simplifié et le guide CNIL et Bpifrance pour les TPE et PME, qui font
du registre la première étape. La mise en étapes est la nôtre.

1. **Le rôle.** Pour chaque activité, l'entreprise décide-t-elle pourquoi et comment les
   données sont traitées (responsable), ou agit-elle pour un client (sous-traitant) ? Si les
   deux existent, préparer deux registres.
2. **Les activités, par finalité.** Partir de ce que fait l'entreprise, pas de ses
   logiciels : paie, recrutement, clients, prospects, fournisseurs, site et cookies,
   vidéosurveillance, comptabilité. La personne confirme chaque activité ; aucune ne
   s'inscrit par défaut.
3. **Une fiche par activité.** Personnes concernées, données, destinataires (y compris les
   prestataires), transferts hors Union européenne, durées de conservation, mesures de
   sécurité. Ce qui est inconnu reste « à compléter ».
4. **Le contrôle par `registre_verifier`.** Il dit si le registre est obligatoire et, fiche
   par fiche, ce qui manque ou reste à confirmer.
5. **La relecture de ce que l'outil ne juge pas.** Durées au regard des référentiels de la
   CNIL, base légale de chaque activité, besoin d'une analyse d'impact, contrats avec les
   sous-traitants. Puis fixer une date de mise à jour.

Approche concurrente : **partir du modèle de la CNIL et le remplir case par case**. Plus
rapide pour qui a déjà l'inventaire en tête ; plus risqué pour qui ne l'a pas, car le modèle
ne dit pas quelles activités inscrire. Beaucoup d'entreprises combinent : les étapes 1 et 2
d'abord, le modèle ensuite.

Le registre décrit ; il ne prouve pas la conformité et ne se présente jamais comme
« conforme ».

## Aller plus loin avec OriginSkill

Ce que vous venez de lire est la méthode de la fiche : elle est ouverte à tous. OriginSkill ajoute ce qu'un texte ne peut pas faire seul : des calculs et des contrôles exacts, faits avec des règles tenues à jour (chacune porte sa source et sa date), la mémoire de votre entreprise et le droit à jour.

### Les calculs de cette fiche

Ces calculs sont inclus dans l'abonnement. OriginSkill les fait pour vous, avec des règles à jour et sourcées, et la réponse est garantie.

- **Contrôler un registre des traitements de données personnelles** (outil `orizon_registre_verifier`) : Dit si une entreprise doit tenir un registre des traitements de données personnelles, puis contrôle chaque fiche mention par mention.

### Avec l'abonnement, en plus

- **La mémoire de votre entreprise** : vos informations et vos dossiers sont retenus d'une conversation à l'autre, et rien n'y est écrit sans votre validation.
- **Le droit à jour** : chaque règle porte sa source et sa date, et OriginSkill vous prévient quand une règle a changé.

### Brancher OriginSkill à votre assistant

Dans votre assistant d'intelligence artificielle (Claude, ChatGPT en mode développeur, Cursor, Codex ou tout autre assistant qui accepte les connecteurs au standard MCP, une façon de brancher un service externe), ajoutez un connecteur avec cette adresse :

    https://api.originskill.ai/mcp

Votre assistant ouvre alors une page de connexion à votre compte OriginSkill. Les étapes détaillées sont ici : https://originskill.ai/installer

### Tarif

Offres et abonnement : https://originskill.ai/tarif

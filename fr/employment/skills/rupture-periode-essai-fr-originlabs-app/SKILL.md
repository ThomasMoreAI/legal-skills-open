---
name: rupture-periode-essai-fr-originlabs-app
title: Mettre fin à une période d'essai
description: 'Mettre fin à une période d''essai. Méthode professionnelle française, avec ses pièges et ses questions à poser. À utiliser quand : L''employeur ou le salarié veut mettre fin au contrat pendant l''essai ; Vérifier que l''essai existe, n''est pas trop long et n''est pas déjà terminé ; Calculer le délai à respecter avant le départ (délai de prévenance) et la date de fin du contrat.'
author: originlabs-app
author_url: https://github.com/originlabs-app/origin-skill-install/tree/main/skills/rupture-periode-essai-fr
license: CC-BY-4.0
version: 0.1.0
execution_mode: open
jurisdiction: fr
practice: employment
language: fr
---

> **Version gratuite : règles datées entre le 18/07/2026 et le 03/10/2026.** Les règles changent (SMIC, TVA, seuils…). Avec l'abonnement OriginSkill, votre assistant reçoit la règle à jour, avec sa source et sa date.

# Mettre fin à une période d'essai

## Quand l'utiliser

- L'employeur ou le salarié veut mettre fin au contrat pendant l'essai.
- Vérifier que l'essai existe, n'est pas trop long et n'est pas déjà terminé.
- Calculer le délai à respecter avant le départ (délai de prévenance) et la date de fin du contrat.
- Préparer la notification et les documents de fin de contrat.

Quand **ne pas** l'utiliser : l'essai est terminé (c'est alors un licenciement, fiche
`licenciement-employeur-fr`) ; rupture conventionnelle, démission, fin normale d'un CDD ;
intérim, apprentissage, période probatoire interne ; salarié protégé. Si la salariée est
enceinte, si le salarié est en arrêt pour accident du travail ou maladie professionnelle,
s'il a dénoncé un harcèlement ou lancé une alerte, ou si un motif discriminatoire est
possible : arrêter la préparation et orienter vers un avocat ou un juriste.

## Connaissances du métier

Pendant l'essai, chacun peut rompre **sans motif ni procédure de licenciement**, à trois
conditions : l'essai existe (il est écrit dans le contrat), il est valable (durée légale
ou conventionnelle respectée, renouvellement autorisé) et il est en cours. Un stage ou
un CDD précédent dans l'entreprise se déduit de sa durée. Une rupture notifiée après la
fin de l'essai est un licenciement.

La rupture reste interdite quand elle repose sur un motif sans lien avec les compétences
professionnelles (santé, grossesse, activité syndicale, dénonciation d'un harcèlement) :
elle est alors abusive ou nulle.

Celui qui rompt respecte un **délai de prévenance**, qui dépend du temps de présence du
salarié et de qui prend l'initiative. Ce délai **ne prolonge pas l'essai** : si la fin de
l'essai arrive avant, le contrat s'arrête au terme de l'essai et l'employeur verse une
indemnité pour la prévenance non effectuée, sauf faute grave. Aucune forme n'est imposée
par la loi, mais un écrit daté (remise contre signature ou lettre recommandée) prouve la
date. À la fin du contrat, l'employeur remet le certificat de travail, l'attestation
France Travail et le reçu pour solde de tout compte. Les délais viennent de l'outil
`delais_rh_calculer`, jamais de mémoire.

## Pièges fréquents

- **Rompre au dernier jour sans compter la prévenance** : l'indemnité est due, l'essai n'est pas prolongé.
- **Rompre après la fin de l'essai**, ou pendant un essai renouvelé sans accord de branche : c'est un licenciement.
- **Oublier une absence** du salarié : elle décale la fin de l'essai (à faire confirmer).
- **Motiver la lettre** par autre chose que les compétences, ou la motiver tout court sans nécessité.
- **Rompre juste après une annonce de grossesse, un arrêt de travail ou une alerte.**
- **Oublier les documents de fin de contrat**, dus même pour quelques jours de travail.

## Méthodes proposées (jamais imposées)

1. **Rupture sûre en quatre temps** : l'essai est-il valable et en cours, y a-t-il un
   signal de risque, quelle prévenance et quelle date de fin, quelle notification datée.
   Détails : `methode-rupture-essai`.
2. **Sortie propre** : dernier jour, solde de tout compte, documents de fin, restitution
   du matériel. Détails : `methode-documents-fin`.

La personne peut ignorer les méthodes, en changer, sauter une étape ou revenir en arrière.

## Contrat de réponse (3 règles fixes)

1. Toute règle ou tout chiffre affirmé vient avec sa **source datée** (les outils la donnent).
2. **Ne jamais inventer** : dire ce qui manque ou ce qui est incertain.
3. **Prévenir** quand une règle vient de changer (champ `prudence` des outils).

« Plan d'action d'abord », « deux questions au maximum » et l'ordre des étapes sont de
bonnes habitudes quand la personne veut agir, pas des obligations.

**Restitution au dirigeant.**

1. Répondre d'abord, exactement, à la question posée et à rien d'autre : la règle ou le chiffre en une ou deux phrases, puis ce qui sert à cette question. Pas de tableau complet, pas de volet non demandé, aucun chiffre d'exemple inventé. Reprendre tels quels les chiffres de `en_clair.resultats`, sans les recalculer ; ne jamais affirmer qu'un point non fourni par le dirigeant est en règle.
2. Si un fait manque et change la réponse, donner la réponse pour chaque cas, puis poser une seule question à la fin : celle qui débloque. Aucune question si rien ne manque.
3. Parler en mots du dirigeant : jamais « l'outil », « le moteur », « le serveur », ni un code ou un champ technique (`entree_incomplete`, `manquant`, `prudence`) ; ne jamais recopier le mot « garanti » ni « non garanti ». Traduire : « il me manque la date d'embauche pour calculer… », « règle relevée le JJ/MM/AAAA, texte officiel pas encore relu ; à reconfirmer avant d'agir ». Écrire « vérifiée » seulement pour une règle marquée vérifiée (« règle vérifiée le JJ/MM/AAAA ; à reconfirmer avant d'agir si l'enjeu est important ») : une source citée n'est pas une vérification.
4. Une échéance qui tombe un samedi, un dimanche ou un jour férié se dit avec son report si les règles en donnent un, sinon « à vérifier ».
5. Ne jamais inventer un fait absent, ni pour appeler un outil. Une règle datée fournie par OriginSkill n'est jamais remplacée par une source secondaire trouvée en ligne ; en cas d'écart, donner les deux valeurs, leurs sources et leurs dates.

## Outils (description ouverte)

L'exécution exacte est servie par le connecteur, sur le moteur RH partagé avec les
fiches `contrat-travail-fr`, `rupture-conventionnelle-fr` et `licenciement-employeur-fr`.

| Outil | Sert à | Appeler quand |
| --- | --- | --- |
| `situation_verifier` (blocs `essai`, `risques`) | Vérifier que l'essai est écrit, pas trop long, renouvelé à bon droit, et repérer les signaux qui imposent un avocat | Avant tout calcul |
| `delais_rh_calculer` (`essai`) | Fin de l'essai (calculée de quantième à quantième depuis `duree_essai_mois` ou `duree_essai_jours` si `date_fin_essai` manque), temps de présence, délai de prévenance, fin de la prévenance, date de fin du contrat, jours non effectués | L'essai est valable |
| `indemnites_calculer` (`preavis`) | Ordre de grandeur de l'indemnité pour la prévenance non effectuée, sur le salaire mensuel | Des jours de prévenance tombent après l'essai |
| `convention_collective` (nom servi : `orizon_convention_collective`) | Retrouver la convention collective de l'employeur (IDCC) et lire le texte daté de la clause de période d'essai ou de prévenance (`theme: periode_essai`), qui peut fixer des durées différentes. IDCC lu en direct (DSN, en retard de plusieurs mois) ou fourni par le client ; intitulé et texte ne sortent qu'une fois vérifiés par la veille sur KALI, sinon IDCC, lien KALI et manquant, jamais devinés | Une clause conventionnelle s'applique ou peut s'appliquer, ou le client ne sait pas quelle convention le lie |
| `convention_article` (nom servi : `orizon_convention_article`) | Lire dans LA convention collective du client (IDCC connu) le texte des articles d'un thème (`theme` : `periode_essai`, `preavis`, `indemnite_licenciement`, `rupture_conventionnelle`, `salaires_minima`, `duree_travail`, `conges`, `depart_retraite`, `maladie`), cité tel quel avec son identifiant KALIARTI, son numéro et sa date de version, jamais résumé comme une règle ; articles repérés par l'intitulé des sections, applicabilité non jugée (avenants, version à la date des faits, comparaison avec le Code du travail à faire avec le client) | Après `convention_collective`, quand une clause conventionnelle doit être lue. **Outil ouvert progressivement : il n'existe que s'il figure dans la liste `outils` rendue par `orizon_fiche` ; sinon, renvoyer vers le texte de la convention sur Légifrance (liste des IDCC) sans citer d'article de mémoire.** |

Chaque outil répond sous la forme unique `resultat` / `regles` / `manquant` / `prudence` /
`garanti`. Un signal d'escalade arrête la préparation de la rupture.

## Quatre usages

| Usage | Attitude | Outils |
| --- | --- | --- |
| Question simple (« quel délai après 2 mois ? ») | Répondre avec la règle et sa source | `delais_rh_calculer` si un calcul aide |
| Objectif précis (« je veux rompre vendredi ») | Vérifier l'essai et les risques, puis calculer ; restituer la date de fin et ce qui manque | `situation_verifier`, `delais_rh_calculer` |
| Suivre une méthode (« accompagne-moi ») | Proposer la rupture en quatre temps puis la sortie propre | les trois, selon l'étape |
| Explorer (« peut-on rompre sans motif ? ») | Conversation libre, faits justes et sourcés | outils seulement s'ils aident |

## Sans abonnement (« non garanti »)

Les connaissances, les pièges et les méthodes restent utiles. Les règles datées, les
contrôles exacts et les cas de référence du moteur ne sont pas garantis : le dire, et
indiquer `garanti: non`.

## Documents

Notification de rupture et liste des documents de fin : toujours un **projet à relire**
par l'employeur. La fiche ne notifie, ne signe et n'envoie rien, et ne juge pas le motif.

### Annexe : glossaire

# Glossaire

- **Période d'essai** : début du contrat où chacun peut rompre sans motif, si elle est écrite et valable.
- **Délai de prévenance** : temps entre l'annonce de la rupture et la fin du contrat.
- **Temps de présence** : jours écoulés depuis l'arrivée du salarié, qui fixent la prévenance.
- **Indemnité compensatrice de prévenance** : somme due par l'employeur pour la prévenance non effectuée.
- **Rupture abusive** : rupture pour un motif sans lien avec les compétences professionnelles.
- **Nullité** : la rupture est annulée (discrimination, grossesse, harcèlement, accident du travail).
- **Solde de tout compte** : récapitulatif des sommes versées à la fin du contrat.
- **Attestation France Travail** : document qui permet au salarié de demander ses allocations.

### Annexe : liens-ressources

# Liens et verification en ligne

Verifier avant restitution:

- Code du travail L1221-25: initiative employeur, bareme, non-prolongation, indemnite compensatrice.
- Code du travail L1221-26: initiative salarie.
- Service-Public F1643 pour formulation utilisateur et documents de fin de contrat.
- Convention collective, accord de branche et contrat de travail pour tout delai plus favorable ou formalite specifique.

Le script ne traite pas les ruptures hors periode d'essai, le licenciement, la rupture conventionnelle, ni la fin d'un CDD hors essai.

### Annexe : methode-documents-fin

# Méthode : sortie propre du salarié

Proposée, jamais imposée. Liste de fin de contrat tirée de la fiche Service-Public F21789.

- **Dernier jour travaillé** et date de fin du contrat (issue du calcul des délais).
- **Solde de tout compte** : salaire jusqu'à la fin, indemnité compensatrice de congés
  payés, indemnité de prévenance éventuelle (calcul des indemnités légales de rupture, cas du préavis non effectué), primes dues. Le reçu signé peut être dénoncé par le salarié
  dans un délai limité.
- **Certificat de travail** : dates d'entrée et de sortie, emplois occupés.
- **Attestation France Travail** : transmise par l'employeur, remise au salarié.
- **Restitution** du matériel, des badges et des accès ; clôture des accès informatiques
  le dernier jour.

Ces documents sont dus même pour un contrat de quelques jours. La fiche prépare la liste,
elle ne remplit ni ne transmet aucun formulaire.

### Annexe : methode-rupture-essai

# Méthode : rupture sûre de la période d'essai en quatre temps

Proposée, jamais imposée. Reprend l'ordre de la fiche Service-Public F1643 et les
précautions des praticiens RH : on vérifie avant de calculer, on calcule avant de notifier.

1. **L'essai est-il valable et en cours ?** Écrit dans le contrat, durée dans les
   maximums, renouvellement prévu et autorisé, CDD ou stage précédent déduit, absences
   qui décalent la fin. Outil : `situation_verifier` (volet essai).
2. **Y a-t-il un signal de risque ?** Grossesse, arrêt pour accident du travail ou
   maladie professionnelle, dénonciation d'un harcèlement, alerte, mandat, motif sans
   lien avec les compétences. Outil : `situation_verifier` (volet risques, procédure d'essai). Un signal d'escalade arrête tout : avocat ou juriste.
3. **Quelle prévenance, quelle date de fin ?** Outil : `delais_rh_calculer` (cas de l'essai).
   Si la prévenance dépasse la fin de l'essai, le contrat s'arrête au terme de l'essai
   et les jours non effectués sont indemnisés par l'employeur.
4. **Notifier par écrit daté** : remise en main propre contre signature ou lettre
   recommandée avec accusé de réception, sans motif autre que la décision de ne pas
   poursuivre l'essai.

## Aller plus loin avec OriginSkill

Ce que vous venez de lire est la méthode de la fiche : elle est ouverte à tous. OriginSkill ajoute ce qu'un texte ne peut pas faire seul : des calculs et des contrôles exacts, faits avec des règles tenues à jour (chacune porte sa source et sa date), la mémoire de votre entreprise et le droit à jour.

### Les calculs de cette fiche

Ces calculs sont inclus dans l'abonnement. OriginSkill les fait pour vous, avec des règles à jour et sourcées, et la réponse est garantie.

- **Lire le texte officiel d'un article de loi** (outil `orizon_article_texte`) : Va chercher, au moment de la question, le texte officiel d'un article de loi sur le site de l'État, tel qu'il est en vigueur à la date voulue.
- **Lire un article de votre convention collective** (outil `orizon_convention_article`) : Lit, dans la convention collective de l'entreprise, les articles d'un thème (période d'essai, préavis, indemnités…), cités tels quels avec leur date.
- **Retrouver la convention collective d'une entreprise** (outil `orizon_convention_collective`) : Retrouve la convention collective applicable à une entreprise à partir de son numéro SIREN, et le texte daté de la clause qui vous intéresse.
- **Calculer les délais d'une procédure de ressources humaines** (outil `orizon_delais_rh_calculer`) : Calcule les dates d'une procédure côté employeur : rupture de période d'essai, rupture conventionnelle, entretien, lettre, préavis, CDD.
- **Calculer les indemnités légales de rupture** (outil `orizon_indemnites_calculer`) : Calcule au centime les montants légaux minimums d'une rupture de contrat : indemnité de licenciement, de fin de CDD, de préavis.
- **Contrôler un contrat ou une situation de rupture** (outil `orizon_situation_verifier`) : Contrôle un contrat de travail ou une rupture côté employeur, et signale les situations où il faut un avocat (salarié protégé, grossesse, accident du travail…).

### Avec l'abonnement, en plus

- **La mémoire de votre entreprise** : vos informations et vos dossiers sont retenus d'une conversation à l'autre, et rien n'y est écrit sans votre validation.
- **Le droit à jour** : chaque règle porte sa source et sa date, et OriginSkill vous prévient quand une règle a changé.

### Brancher OriginSkill à votre assistant

Dans votre assistant d'intelligence artificielle (Claude, ChatGPT en mode développeur, Cursor, Codex ou tout autre assistant qui accepte les connecteurs au standard MCP, une façon de brancher un service externe), ajoutez un connecteur avec cette adresse :

    https://api.originskill.ai/mcp

Votre assistant ouvre alors une page de connexion à votre compte OriginSkill. Les étapes détaillées sont ici : https://originskill.ai/installer

### Tarif

Offres et abonnement : https://originskill.ai/tarif

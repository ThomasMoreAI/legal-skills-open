---
name: contrat-travail-fr-originlabs-app
title: Rédiger ou relire un contrat de travail
description: 'Rédiger ou relire un contrat de travail. Méthode professionnelle française, avec ses pièges et ses questions à poser. À utiliser quand : Choisir entre CDI et CDD pour une embauche, et savoir si le motif du CDD tient ; Rédiger ou relire un CDI, un CDD, un avenant, un contrat à temps partiel ; Fixer une période d''essai et son renouvellement.'
author: originlabs-app
author_url: https://github.com/originlabs-app/origin-skill-install/tree/main/skills/contrat-travail-fr
license: CC-BY-4.0
version: 0.1.0
execution_mode: open
jurisdiction: fr
practice: employment
language: fr
---

> **Version gratuite : règles datées entre le 18/07/2026 et le 03/10/2026.** Les règles changent (SMIC, TVA, seuils…). Avec l'abonnement OriginSkill, votre assistant reçoit la règle à jour, avec sa source et sa date.

# Rédiger ou relire un contrat de travail

## Quand l'utiliser

- Choisir entre CDI et CDD pour une embauche, et savoir si le motif du CDD tient.
- Rédiger ou relire un CDI, un CDD, un avenant, un contrat à temps partiel.
- Fixer une période d'essai et son renouvellement.
- Organiser l'embauche : déclaration préalable à l'embauche (DPAE), informations à remettre au salarié,
  pièces à conserver.
- Une question précise (« combien de renouvellements pour un CDD ? », « prime de précarité due ? »).

Quand **ne pas** l'utiliser : intérim, apprentissage, contrat de professionnalisation,
particulier employeur, fonction publique, détachement complet ; la rupture du contrat
(fiches `rupture-periode-essai-fr`, `rupture-conventionnelle-fr`,
`licenciement-employeur-fr`) ; la validité d'une clause de non-concurrence, de mobilité
ou d'un forfait-jours, ou les minima de la convention collective : le dire et orienter
vers un juriste en droit du travail.

## Connaissances du métier

Le **CDI** est la règle ; le **CDD** est l'exception. Un CDD n'est possible que dans les
cas prévus par la loi (remplacement, accroissement temporaire d'activité, emploi
saisonnier ou d'usage...), jamais pour pourvoir durablement un emploi permanent. Il doit
être **écrit**, préciser son motif et comporter des mentions précises ; sans écrit, il
est réputé à durée indéterminée. Il est remis au salarié dans un délai très court après
l'embauche. À son terme, une indemnité de fin de contrat est due sauf exceptions.

La **période d'essai** n'existe que si elle est écrite. Sa durée maximale dépend de la
catégorie du salarié ; elle ne se renouvelle qu'une fois et seulement si un accord de
branche étendu le permet et que le contrat le prévoit. Un stage ou un CDD précédent
dans l'entreprise se déduit de l'essai.

Le **temps partiel** exige un contrat écrit qui fixe la durée, sa répartition et les
conditions de modification. Un plancher hebdomadaire s'applique sauf dérogation.

À l'embauche, la **DPAE** se fait avant la prise de poste, et le salarié reçoit par
écrit les informations principales de la relation de travail, dans deux délais selon
les rubriques. La convention collective peut être plus favorable que la loi : elle
prime quand elle l'est. Les chiffres (durées, délais, plancher) viennent des outils,
jamais de mémoire.

## Pièges fréquents

- **CDD pour un poste permanent** ou motif vague (« surcroît d'activité » sans fait) : requalification en CDI.
- **CDD sans écrit, sans motif ou remis trop tard.**
- **Essai trop long, renouvelé sans accord de branche** ou non écrit : il n'existe pas.
- **Oublier de déduire un stage ou un CDD précédent** de la période d'essai.
- **Temps partiel sans répartition des horaires**, ou sous le plancher sans dérogation écrite.
- **Enchaîner des CDD sur le même poste** sans respecter le délai de carence.
- **Copier une clause de non-concurrence d'un modèle** : sans contrepartie financière et limites, elle est nulle.
- **Oublier la convention collective** : essai plus court, salaire minimum, préavis.

## Méthodes proposées (jamais imposées)

1. **Choisir CDI ou CDD en cinq questions** : le besoin est-il durable, quel fait précis
   justifie le CDD, pour combien de temps, qui est remplacé, quelle suite. Inspirée des
   fiches Service-Public F36 et F1906. Détails : `methode-choix-cdi-cdd`.
2. **Relecture d'un contrat en trois passes** : forme et mentions, essai et durée du
   travail, clauses sensibles et convention collective. Détails :
   `methode-relecture-contrat`.

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
fiches `rupture-periode-essai-fr`, `rupture-conventionnelle-fr` et
`licenciement-employeur-fr`.

| Outil | Sert à | Appeler quand |
| --- | --- | --- |
| `situation_verifier` (blocs `contrat`, `essai`, `risques`) | Contrôler les mentions d'un CDD ou d'un temps partiel, le plancher horaire, la durée et le renouvellement de l'essai, et repérer ce qui impose un juriste (salarié étranger, discrimination) | Un contrat existe ou se prépare |
| `echeances_diverses` (`dsn_cotisations`, nom servi : `orizon_echeances_diverses`) | Dater l'échéance mensuelle des cotisations sociales (DSN, le 5 ou le 15 du mois suivant selon l'effectif et le décalage de paie) | Une question sur la date de paiement des cotisations d'un salarié embauché |
| `delais_rh_calculer` (`embauche`, `cdd`) | Dater la DPAE, les deux délais d'information du salarié, la remise du CDD et le délai de carence | Une date d'embauche est connue |
| `indemnites_calculer` (`fin_cdd`) | Calculer l'indemnité de fin de CDD sur la rémunération brute totale | Un CDD se termine |
| `convention_collective` (nom servi : `orizon_convention_collective`) | Retrouver la convention collective de l'employeur (IDCC) et lire le texte daté de la clause utile (`theme`, par exemple `periode_essai`) : durées d'essai, préavis et minima conventionnels peuvent différer du Code du travail. IDCC lu en direct (DSN, en retard de plusieurs mois) ou fourni par le client ; intitulé et texte ne sortent qu'une fois vérifiés par la veille sur KALI, sinon IDCC, lien KALI et manquant, jamais devinés | Une clause conventionnelle s'applique ou peut s'appliquer, ou le client ne sait pas quelle convention le lie |
| `convention_article` (nom servi : `orizon_convention_article`) | Lire dans LA convention collective du client (IDCC connu) le texte des articles d'un thème (`theme` : `periode_essai`, `preavis`, `indemnite_licenciement`, `rupture_conventionnelle`, `salaires_minima`, `duree_travail`, `conges`, `depart_retraite`, `maladie`), cité tel quel avec son identifiant KALIARTI, son numéro et sa date de version, jamais résumé comme une règle ; articles repérés par l'intitulé des sections, applicabilité non jugée (avenants, version à la date des faits, comparaison avec le Code du travail à faire avec le client) | Après `convention_collective`, quand une clause conventionnelle doit être lue. **Outil ouvert progressivement : il n'existe que s'il figure dans la liste `outils` rendue par `orizon_fiche` ; sinon, renvoyer vers le texte de la convention sur Légifrance (liste des IDCC) sans citer d'article de mémoire.** |
| `parametres_sociaux` (nom servi : `orizon_parametres_sociaux`) | Lire le SMIC horaire et mensuel (35 h) à la date d'embauche pour vérifier le plancher de rémunération, et le PASS. Seule une valeur vérifiée sort un chiffre (PASS 2026) ; le SMIC non vérifié sort en manquant avec le lien officiel, sans chiffre ; ne rend ni taux de cotisation ni coût employeur | Un seuil ou un plancher exprimé en SMIC ou en PASS doit être chiffré |

Chaque outil répond sous la forme unique `resultat` / `regles` / `manquant` / `prudence` /
`garanti`. Le verdict de `situation_verifier` n'est jamais « conforme » tout court : il
dit ce qu'il ne contrôle pas (clauses sensibles, minima conventionnels, motif réel).

## Quatre usages

| Usage | Attitude | Outils |
| --- | --- | --- |
| Question simple (« essai d'un cadre ? ») | Répondre avec la règle et sa source | `situation_verifier` si un contrôle aide |
| Objectif précis (« relis ce CDD ») | Faire passer l'outil, restituer ce qui est à corriger, puis les questions tirées de `manquant` | `situation_verifier`, `delais_rh_calculer` |
| Suivre une méthode (« aide-moi à embaucher ») | Proposer le choix CDI/CDD puis la relecture ; la personne choisit le rythme | les trois, selon l'étape |
| Explorer (« c'est quoi un CDD d'usage ? ») | Conversation libre, faits justes et sourcés | outils seulement s'ils aident |

## Sans abonnement (« non garanti »)

Les connaissances, les pièges et les méthodes restent utiles. Les règles datées, les
contrôles exacts et les cas de référence du moteur ne sont pas garantis : le dire, et
indiquer `garanti: non`.

## Documents

Contrat, avenant, lettre d'engagement : toujours un **projet à relire** par l'employeur,
et par un juriste dès qu'une clause sensible ou un doute sur le motif apparaît. La fiche
ne signe, n'envoie et ne déclare rien (ni DPAE, ni autorisation de travail).

### Annexe : checks

# QUALITY / CHECKS

Checklist d'auto-vérification du LLM **avant** de rendre la réponse. Ce n'est pas un calcul. Un item rouge n'autorise pas une sortie vide : rendre le plancher utile et la question.

## 1. Source actuelle

- Chaque règle citée porte l'identifiant de sa source (S1, S25…) ou, à défaut, la fiche administrative datée dont elle est tirée, dite explicitement.
- L'URL Légifrance ou Service-Public a été revérifiée, ou le doute est dit (« version à confirmer, id Sx »).
- Aucune obligation n'appuie seulement sur S3 (Tissot) ou sur une habitude.

## 2. Juridiction

- France, secteur privé, CDI ou CDD.
- Hors périmètre (intérim, apprentissage, fonction publique, rupture hors essai) : aiguillage + question, pas un avis déguisé.

## 3. Faits manquants

- Une seule question décisive en tête s'il en reste.
- Les faits déjà dans les pièces ou la mémoire ne sont pas redemandés.
- Les crochets `[à confirmer]` sont explicites.

## 4. Contradictions

- Deux valeurs pour le même fait : les deux sont exposées, aucune n'est choisie en silence.

## 5. Exception

- CDD : le recours réel est-il établi, ou seulement un slogan ?
- CDD, durée : les faits de l'événement (absence, attente d'un CDI, départ, surcroît, saison…) sont-ils assez précis pour que le LLM hôte qualifie avant d'annoncer 9, 18 ou 24 mois (S27, table structure-cdd.md) ? Ne pas demander au client le « sous-cas » ni le « fondement » juridique.
- CDD, carence : un CDD ou un contrat de mission vient-il d'expirer, et un nouveau CDD ou contrat de mission est-il envisagé pour le même poste ? Si CDD expiré : L1244-3, puis exemption L1244-4-1 avant S33. Si contrat de mission expiré : L1251-36, hors périmètre, ne pas calculer S33.
- Essai : durée initiale distincte du renouvellement ? Accord de branche étendu lu avant d'affirmer un renouvellement ? Un CDD a-t-il précédé ce CDI ?
- Temps partiel sous 24 h : exception qualifiée (S35) ou plancher S37 marqué « à confirmer » ?
- Indemnité de fin : exclusion S31 réellement étayée, ou 10 % S30 par défaut « à confirmer » ?

## 6. Calcul

- Délais, plafonds, centimes : renvoyés à l'outil déterministe fourni pour les délais, plafonds et montants, pas recalculés de tête.
- Arrondi : convention interne S40, pas présentée comme une règle du Code.
- Sans convention : plancher légal calculé + « à confirmer » + question IDCC.

## 7. Cohérence documentaire

- Aucun fichier final (contrat, avenant, lettre) n'est généré.
- La trame couvre les sections attendues (CDI ou CDD) sans coller un modèle complet.
- Les clauses sensibles sont signalées, non validées.
- Un indice L1132-1 est localisé, sans conclusion d'infraction.
- Langue française du document d'obligation (S34) vérifiée si un écrit est fourni.

## 8. Sortie

- Valeur utile ou question en premier.
- Sources visibles.
- Prochaine action unique et concrète.
- Pas de coulisses techniques exposées au client.

### Annexe : glossaire

# Glossaire

- **CDI** : contrat à durée indéterminée, forme normale de la relation de travail.
- **CDD** : contrat à durée déterminée, possible seulement dans les cas prévus par la loi.
- **Requalification** : le juge transforme un CDD irrégulier en CDI.
- **Période d'essai** : début du contrat pendant lequel chacun peut rompre sans motif ; n'existe que si elle est écrite.
- **Délai de carence** : délai à respecter avant un nouveau CDD sur le même poste.
- **Indemnité de fin de contrat** (prime de précarité) : somme versée au terme d'un CDD, sauf exceptions.
- **DPAE** : déclaration préalable à l'embauche, faite à l'Urssaf avant la prise de poste.
- **Temps partiel** : durée de travail inférieure à la durée légale ou conventionnelle.
- **Heures complémentaires** : heures faites au-delà de la durée prévue au contrat à temps partiel.
- **Convention collective (IDCC)** : accord de branche qui peut améliorer les règles légales.
- **Avenant** : modification écrite du contrat, signée des deux parties.

### Annexe : liens-ressources

# Liens et verification en ligne

Avant de finaliser un contrat, verifier:

- Code du travail L1221-5-1 et R1221-34/R1221-35 pour les informations dues au salarie.
- Arrete du 3 juin 2024 pour les modeles de documents d'information.
- Code du travail L1242-2, L1242-10, L1242-12 et L1242-13 pour CDD.
- Code du travail L1221-19 a L1221-26 pour CDI et periode d'essai.
- Code du travail L3123-6 pour temps partiel.
- Convention collective, accord de branche et usages applicables.

Sources terrain secondaires admises uniquement pour les angles morts de pratique, jamais pour trancher une obligation.

### Annexe : methode-choix-cdi-cdd

# Méthode : choisir CDI ou CDD en cinq questions

Proposée, jamais imposée. Inspirée des fiches Service-Public F1906 (CDI) et F36 (CDD) et
de la pratique des services RH de TPE. Les délais et plafonds viennent des outils.

| # | Question | Si la réponse est… |
| --- | --- | --- |
| 1 | Le besoin est-il durable (le poste existera encore dans un an) ? | Oui : CDI, sauf remplacement d'un absent. |
| 2 | Quel **fait précis et daté** justifie un CDD ? (absence de Mme X, commande exceptionnelle du client Y, saison) | Aucun fait précis : CDI. Le motif écrit dans le contrat sera contrôlé. |
| 3 | Pour combien de temps, avec quel terme ? (date ou fin de l'absence) | Au-delà des durées maximales : revoir le motif ou passer en CDI. |
| 4 | Qui est remplacé, sur quel poste ? | Nom et qualification figurent au contrat de remplacement. |
| 5 | Quelle suite si le besoin dure ? | Prévoir la transformation en CDI (l'essai tient compte du CDD) plutôt qu'un enchaînement de CDD. |

Ensuite : faire passer `situation_verifier` (bloc `contrat`) sur le projet, puis
`delais_rh_calculer` (`embauche`, `cdd`) pour la DPAE, la remise du contrat et, si un
autre CDD suit sur le même poste, le délai de carence.

Limites : la qualification du motif réel et le risque de requalification sont des
appréciations juridiques ; en cas de doute, un juriste en droit du travail.

### Annexe : methode-relecture-contrat

# Méthode : relire un contrat de travail en trois passes

Proposée, jamais imposée. Pratique courante des cabinets et des services RH : lire trois
fois avec une seule question à la fois, plutôt qu'une lecture globale.

1. **Forme et mentions.** Contrat écrit, en français, signé des deux parties. Pour un
   CDD : motif précis, terme ou durée minimale, poste, rémunération, convention
   collective, caisses de retraite et de prévoyance, clause de renouvellement. Outil :
   « Contrôler un contrat ou une situation de rupture » avec la liste des mentions présentes.
2. **Essai et durée du travail.** Essai écrit, durée dans les maximums, renouvellement
   autorisé par un accord de branche étendu ; temps partiel : durée, répartition,
   modification, heures complémentaires, plancher horaire. Outil : « Contrôler un
   contrat ou une situation de rupture » (essai et contrat).
3. **Clauses sensibles et convention collective.** Non-concurrence (limites et
   contrepartie financière), mobilité (zone définie), exclusivité, forfait-jours
   (accord collectif), minima conventionnels. Ces points ne sont **pas contrôlés** par
   l'outil : les signaler et proposer une relecture par un juriste.

Restituer d'abord ce qui est à corriger, puis ce qui est à confirmer, puis les
questions tirées de `manquant`.

## Aller plus loin avec OriginSkill

Ce que vous venez de lire est la méthode de la fiche : elle est ouverte à tous. OriginSkill ajoute ce qu'un texte ne peut pas faire seul : des calculs et des contrôles exacts, faits avec des règles tenues à jour (chacune porte sa source et sa date), la mémoire de votre entreprise et le droit à jour.

### Les calculs de cette fiche

Ces calculs sont inclus dans l'abonnement. OriginSkill les fait pour vous, avec des règles à jour et sourcées, et la réponse est garantie.

- **Lire le texte officiel d'un article de loi** (outil `orizon_article_texte`) : Va chercher, au moment de la question, le texte officiel d'un article de loi sur le site de l'État, tel qu'il est en vigueur à la date voulue.
- **Lire un article de votre convention collective** (outil `orizon_convention_article`) : Lit, dans la convention collective de l'entreprise, les articles d'un thème (période d'essai, préavis, indemnités…), cités tels quels avec leur date.
- **Retrouver la convention collective d'une entreprise** (outil `orizon_convention_collective`) : Retrouve la convention collective applicable à une entreprise à partir de son numéro SIREN, et le texte daté de la clause qui vous intéresse.
- **Connaître le SMIC et le plafond de la Sécurité sociale à une date** (outil `orizon_parametres_sociaux`) : Rend le SMIC (horaire et mensuel) et le plafond de la Sécurité sociale (annuel et mensuel) en vigueur à la date voulue, et leurs multiples.
- **Calculer les délais d'une procédure de ressources humaines** (outil `orizon_delais_rh_calculer`) : Calcule les dates d'une procédure côté employeur : rupture de période d'essai, rupture conventionnelle, entretien, lettre, préavis, CDD.
- **Calculer les indemnités légales de rupture** (outil `orizon_indemnites_calculer`) : Calcule au centime les montants légaux minimums d'une rupture de contrat : indemnité de licenciement, de fin de CDD, de préavis.
- **Contrôler un contrat ou une situation de rupture** (outil `orizon_situation_verifier`) : Contrôle un contrat de travail ou une rupture côté employeur, et signale les situations où il faut un avocat (salarié protégé, grossesse, accident du travail…).
- **Dates de la CFE, des acomptes d'impôt sur les sociétés et des cotisations mensuelles** (outil `orizon_echeances_diverses`) : Donne les dates et montants de trois échéances régulières : solde de la cotisation foncière, acomptes d'impôt sur les sociétés, cotisations sociales mensuelles.

### Avec l'abonnement, en plus

- **La mémoire de votre entreprise** : vos informations et vos dossiers sont retenus d'une conversation à l'autre, et rien n'y est écrit sans votre validation.
- **Le droit à jour** : chaque règle porte sa source et sa date, et OriginSkill vous prévient quand une règle a changé.

### Brancher OriginSkill à votre assistant

Dans votre assistant d'intelligence artificielle (Claude, ChatGPT en mode développeur, Cursor, Codex ou tout autre assistant qui accepte les connecteurs au standard MCP, une façon de brancher un service externe), ajoutez un connecteur avec cette adresse :

    https://api.originskill.ai/mcp

Votre assistant ouvre alors une page de connexion à votre compte OriginSkill. Les étapes détaillées sont ici : https://originskill.ai/installer

### Tarif

Offres et abonnement : https://originskill.ai/tarif

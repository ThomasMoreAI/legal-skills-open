---
name: mentions-legales-site-fr-originlabs-app
title: Vérifier les mentions légales de mon site
description: 'Vérifier les mentions légales de mon site. Méthode professionnelle française, avec ses pièges et ses questions à poser. À utiliser quand : Contrôler la page « Mentions légales » d''un site vitrine avant sa mise en ligne ou après une refonte ; Contrôler une boutique en ligne : mentions, CGV, médiateur, cookies ; Répondre à une question précise (« faut-il le capital social ? », « le lien vers la plateforme européenne.'
author: originlabs-app
author_url: https://github.com/originlabs-app/origin-skill-install/tree/main/skills/mentions-legales-site-fr
license: CC-BY-4.0
version: 0.1.0
execution_mode: open
jurisdiction: fr
practice: consumer
language: fr
---

> **Version gratuite : règles datées entre le 28/09/2026 et le 03/10/2026.** Les règles changent (SMIC, TVA, seuils…). Avec l'abonnement OriginSkill, votre assistant reçoit la règle à jour, avec sa source et sa date.

# Vérifier les mentions légales de mon site

## Quand l'utiliser

- Contrôler la page « Mentions légales » d'un site vitrine avant sa mise en ligne ou après une refonte.
- Contrôler une boutique en ligne : mentions, CGV, médiateur, cookies.
- Répondre à une question précise (« faut-il le capital social ? », « le lien vers la plateforme européenne
  des litiges est-il encore exigé ? »).
- Relire un client de l'agence ou du cabinet : le SIREN écrit sur le site est-il celui de la bonne entreprise ?
- Préparer un projet de page mentions légales à relire.

Quand **ne pas** l'utiliser : rédiger la politique de confidentialité ou tenir le registre des
traitements (fiche `rgpd-registre-traitements-fr`), vérifier qu'aucun cookie n'est déposé avant
consentement (test technique du site), mentions d'une profession réglementée, contentieux.

## Connaissances du métier

Un site d'entreprise porte trois blocs de mentions. **L'identification** (loi du 21 juin 2004,
LCEN, art. 6 III) : l'éditeur, son adresse et son téléphone, son numéro RCS ou RM et son capital
s'il est une société, le directeur de la publication (pour une société, son représentant légal),
l'hébergeur avec nom, adresse et téléphone. Une boutique en ligne y ajoute l'adresse e-mail et,
si l'entreprise est assujettie, le numéro de TVA (art. 19). **Les cookies** (art. 82 de la loi
Informatique et Libertés, lignes directrices de la CNIL de 2020) : finalités annoncées avant le
dépôt, refus aussi simple que l'acceptation, retrait possible. **La vente aux consommateurs** :
informations précontractuelles (Code de la consommation, L221-5 : rétractation, garanties légales,
livraison) et coordonnées d'un médiateur de la consommation (R616-1).

Ce qui est exigé dépend de faits sur la situation : forme juridique, boutique ou vitrine, vente aux
particuliers, assujettissement à la TVA, cookies. Quand un fait manque, la mention qui en dépend
reste « à confirmer » : ni conforme, ni absente.

**Le lien vers la plateforme RLL n'est plus exigé.** La plateforme européenne de règlement en
ligne des litiges a été supprimée le 20 juillet 2025 (règlement UE 2024/3228). Avant cette date le
lien était obligatoire ; après, une référence restante dans les mentions ou les CGV est obsolète
et se retire. L'outil raisonne à la date du jour.

## Pièges fréquents

- **Exiger encore le lien RLL** : c'est le piège le plus répandu, y compris dans des modèles récents.
- **Confondre RCS et SIREN** : le numéro RCS est le SIREN de 9 chiffres, suivi de la ville du greffe.
- **Croire le numéro de TVA bon parce qu'il a la bonne forme** : sa clé se recalcule depuis le SIREN.
- **Oublier le directeur de la publication** ou écrire un titre sans nom.
- **Mettre l'hébergeur sans adresse ni téléphone.**
- **Décrire les cookies sans dire comment refuser**, ou croire le bandeau conforme sans bouton de
  refus de même niveau que « Accepter ».
- **Croire qu'un site vitrine échappe au médiateur** : il vaut pour tout professionnel qui vend aux
  consommateurs.
- **Recopier une page de concurrent** : le SIREN, le capital et la forme juridique sont ceux d'une autre société.

## Méthodes proposées (jamais imposées)

1. **Contrôle d'une page avant mise en ligne** : situation, passage de l'outil, corrections d'abord
   sur ce qui est absent ou invalide, puis questions sur ce qui est à confirmer, puis croisement
   avec le registre public. Détails : `methode-controle-mentions`.
2. **Audit d'un lot de sites de clients** (agence, cabinet) : même contrôle, en commençant par les
   boutiques et les sites qui déposent des cookies publicitaires.

La personne peut ignorer les méthodes, en changer, sauter une étape ou revenir en arrière.

## Contrat de réponse (3 règles fixes)

1. Toute règle ou tout chiffre affirmé vient avec sa **source datée** (les outils la donnent).
2. **Ne jamais inventer** : dire ce qui manque ou ce qui est incertain.
3. **Prévenir** quand une règle vient de changer (champ `prudence`), et dire la date du jour pour le RLL.

« Plan d'action d'abord », « deux questions au maximum » et l'ordre des étapes sont de bonnes
habitudes quand la personne veut agir, pas des obligations.

**Restitution au dirigeant.**

1. Répondre d'abord, exactement, à la question posée et à rien d'autre : la règle ou le chiffre en une ou deux phrases, puis ce qui sert à cette question. Pas de tableau complet, pas de volet non demandé, aucun chiffre d'exemple inventé. Reprendre tels quels les chiffres de `en_clair.resultats`, sans les recalculer ; ne jamais affirmer qu'un point non fourni par le dirigeant est en règle.
2. Si un fait manque et change la réponse, donner la réponse pour chaque cas, puis poser une seule question à la fin : celle qui débloque. Aucune question si rien ne manque.
3. Parler en mots du dirigeant : jamais « l'outil », « le moteur », « le serveur », ni un code ou un champ technique (`entree_incomplete`, `manquant`, `prudence`) ; ne jamais recopier le mot « garanti » ni « non garanti ». Traduire : « il me manque la date d'embauche pour calculer… », « règle relevée le JJ/MM/AAAA, texte officiel pas encore relu ; à reconfirmer avant d'agir ». Écrire « vérifiée » seulement pour une règle marquée vérifiée (« règle vérifiée le JJ/MM/AAAA ; à reconfirmer avant d'agir si l'enjeu est important ») : une source citée n'est pas une vérification.
4. Une échéance qui tombe un samedi, un dimanche ou un jour férié se dit avec son report si les règles en donnent un, sinon « à vérifier ».
5. Ne jamais inventer un fait absent, ni pour appeler un outil. Une règle datée fournie par OriginSkill n'est jamais remplacée par une source secondaire trouvée en ligne ; en cas d'écart, donner les deux valeurs, leurs sources et leurs dates.

## Outils (description ouverte)

L'exécution exacte est servie par le connecteur : moteur numérique pour le premier outil,
base publique des entreprises pour le second.

| Outil | Sert à | Appeler quand |
| --- | --- | --- |
| `mentions_site_verifier` (nom servi : `orizon_mentions_site_verifier`) | Contrôler le texte des mentions mention par mention (présente, absente, invalide, à confirmer, non exigée, à retirer), avec règle, source et date d'effet ; valider le SIREN et la clé de TVA ; lire le SIREN et le croiser lui-même avec le registre public (dénomination, forme juridique, état) ; rendre `mentions_corrigees`, les lignes à coller, remplacer ou retirer, chacune avec son origine (lu, calcul, registre, à compléter) | Un texte de mentions légales est fourni, ou une question demande ce qui est exigé dans une situation |
| `entreprise_profil` (nom servi : `orizon_entreprise_profil`) | Rendre dénomination, forme juridique, siège et état d'une entreprise à partir de son SIREN, source datée | Consulter le registre seul, sans texte de mentions à contrôler |
| `article_en_vigueur` (nom servi : `orizon_article_en_vigueur`) | Dire si un article cité (par exemple de la LCEN ou du Code de la consommation) est en vigueur à une date donnée, d'après le dernier relevé daté ; un article non suivi sort dans `manquant` | Un doute sur la version d'un article |

Entrée de `mentions_site_verifier`, en mots simples : `texte` (obligatoire), `forme_juridique`,
`boutique_en_ligne`, `cookies`, `assujetti_tva`, `clients_consommateurs`, `bandeau_refus_simple`
(vrai ou faux, seulement ce qui est su), `cgv` et `politique_cookies` (textes, s'ils sont sur
d'autres pages), `registre` (voir ci-dessous). Le texte se colle tel qu'il s'affiche.

**Croisement avec le registre public, sans second appel.** Quand un SIREN valide est lu dans le
texte, `mentions_site_verifier` consulte lui-même la base publique et rend `croisement_registre` :
il dit si la dénomination, la forme juridique et le SIREN du registre concordent avec les mentions,
sinon la question sort dans `manquant` (nom commercial ? ancien nom ? erreur ?). Base injoignable
(`registre_indisponible`) ou SIREN absent de la base (`siren_introuvable`) : demander l'extrait
Kbis, ne rien déduire. `registre` (réponse de `entreprise_profil`) reste accepté et évite la
lecture ; il sert aussi à rejouer un croisement déjà fait.

**Lignes à coller.** Pour chaque mention absente, invalide ou obsolète, `mentions_corrigees` rend
la ligne à coller, à remplacer ou à retirer : la clé de TVA recalculée depuis le SIREN
(`calcul`), la dénomination et le siège du registre (`registre`), les lignes du texte qui portent
le lien RLL à retirer (`lu`), et, pour ce que seule la personne connaît (capital, directeur de la
publication, ville du greffe, hébergeur), une ligne entre crochets (`a_completer`). Rien n'est
inventé et rien n'est « prêt à publier » : le registre se confronte au Kbis.

Chaque outil répond sous la forme unique `resultat` / `regles` / `manquant` / `prudence` /
`garanti`. Le verdict est `a_corriger`, `incomplet` ou `conforme_sur_les_points_controles` :
jamais « conforme » tout court, car `ne_controle_pas` liste ce qui n'est pas vérifié (exactitude des
informations, comportement réel du bandeau, contenu des CGV).

## Quatre usages

| Usage | Attitude | Outils |
| --- | --- | --- |
| Question simple (« le lien RLL est-il obligatoire ? ») | Répondre directement avec la règle, sa source et la date de suppression, sans questionnaire | aucun, ou `mentions_site_verifier` pour lire la règle du jour |
| Objectif précis (« vérifie cette page ») | Passer l'outil tout de suite, restituer d'abord `a_corriger`, puis les questions tirées de `manquant` | `mentions_site_verifier` (croise le registre lui-même) |
| Suivre une méthode (« aide-moi à mettre en règle le site de mon client ») | Proposer une des deux méthodes, au rythme de la personne | selon l'étape |
| Explorer (« pourquoi un directeur de la publication ? ») | Conversation libre, faits justes et sourcés | seulement s'ils aident |

## Sans abonnement (« non garanti »)

Les connaissances, les pièges et les méthodes restent utiles. Les règles datées, le contrôle
exact, le croisement avec le registre et les cas de référence du moteur ne sont pas garantis :
le dire, et indiquer `garanti: non`.

## Documents

Une page « Mentions légales » proposée : toujours un **projet à relire**, jamais « prêt à
publier ». Chaque mention reprend ce que la personne a fourni ; une information inconnue reste
marquée « à compléter » (jamais un faux SIREN ni un capital inventé), et chaque exigence porte sa source.

### Annexe : liens-ressources

# Liens officiels

Relevés le 28/09/2026 par résultats de recherche (pas de lecture intégrale des pages).

- [LCEN, loi 2004-575, article 6](https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000049577522) : identification de l'éditeur, de l'hébergeur, directeur de la publication.
- [LCEN, article 19](https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000032236011) : commerce électronique, e-mail, TVA.
- [Loi Informatique et Libertés, article 82](https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000037813978) : cookies et traceurs.
- [CNIL, lignes directrices 2020-091](https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000042388179) et [recommandation 2020-092](https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000042388197).
- [Code de la consommation, L221-5](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044563141) : informations précontractuelles.
- [Code de la consommation, R616-1](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000032808378) : médiateur de la consommation.
- [Règlement (UE) 2024/3228](https://eur-lex.europa.eu/eli/reg/2024/3228/oj) : suppression de la plateforme RLL le 20/07/2025.

### Annexe : methode-controle-mentions

# Méthode : contrôle d'une page de mentions légales

Une proposition, à adapter. Rien n'est obligatoire dans l'ordre.

1. **Situation.** Forme juridique, boutique ou vitrine, vente aux particuliers, cookies,
   assujettissement à la TVA. Ce qu'on ignore reste inconnu.
2. **Texte.** Coller la page « Mentions légales », et les CGV pour une boutique. Une page
   séparée pour les cookies se colle aussi.
3. **Passage de l'outil.** Restituer d'abord ce qui est à corriger (absent, invalide, à retirer), puis
   ce qui manque, puis ce qui est recommandé.
4. **Croisement avec le registre.** L'outil lit lui-même le registre public pour le SIREN lu
   (croisement avec le registre). Une dénomination ou une forme juridique qui ne concorde pas est
   une question, pas un verdict ; base injoignable ou SIREN introuvable : demander l'extrait Kbis.
5. **Relecture humaine** de ce que l'outil ne juge pas : exactitude des
   informations, bandeau réel, contenu des CGV.
6. **Projet de page.** Reprendre les mentions corrigées dans un texte à relire :
   ce qui vient du registre se confronte au Kbis, ce qui est entre crochets reste à compléter
   par la personne, sans inventer aucune information manquante.

## Aller plus loin avec OriginSkill

Ce que vous venez de lire est la méthode de la fiche : elle est ouverte à tous. OriginSkill ajoute ce qu'un texte ne peut pas faire seul : des calculs et des contrôles exacts, faits avec des règles tenues à jour (chacune porte sa source et sa date), la mémoire de votre entreprise et le droit à jour.

### Les calculs de cette fiche

Ces calculs sont inclus dans l'abonnement. OriginSkill les fait pour vous, avec des règles à jour et sourcées, et la réponse est garantie.

- **Vérifier qu'un article de loi est toujours en vigueur** (outil `orizon_article_en_vigueur`) : Dit si un article de loi suivi par OriginSkill est en vigueur à la date voulue, d'après le dernier relevé daté du texte officiel.
- **Retrouver la fiche d'une entreprise avec son numéro SIREN** (outil `orizon_entreprise_profil`) : Rend ce que les registres publics disent d'une entreprise : nom, forme juridique, activité, effectif, adresse du siège, dirigeants publiés, entreprise en activité ou fermée.
- **Vérifier les mentions obligatoires d'un site web** (outil `orizon_mentions_site_verifier`) : Contrôle les mentions légales d'un site d'entreprise et dit ce qui manque, avec la règle et sa date d'effet.

### Avec l'abonnement, en plus

- **La mémoire de votre entreprise** : vos informations et vos dossiers sont retenus d'une conversation à l'autre, et rien n'y est écrit sans votre validation.
- **Le droit à jour** : chaque règle porte sa source et sa date, et OriginSkill vous prévient quand une règle a changé.

### Brancher OriginSkill à votre assistant

Dans votre assistant d'intelligence artificielle (Claude, ChatGPT en mode développeur, Cursor, Codex ou tout autre assistant qui accepte les connecteurs au standard MCP, une façon de brancher un service externe), ajoutez un connecteur avec cette adresse :

    https://api.originskill.ai/mcp

Votre assistant ouvre alors une page de connexion à votre compte OriginSkill. Les étapes détaillées sont ici : https://originskill.ai/installer

### Tarif

Offres et abonnement : https://originskill.ai/tarif

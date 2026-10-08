---
name: reglement-jeu-promogit
title: Règlement complet de jeu (France, Word, validation client)
description: Rédige et vérifie en Word les règlements complets des jeux France de Promodev (instant gagnant, 100 % gagnant, tirage au sort, mixte, challenge magasin, jeu à code), avec dépôt commissaire de justice, marque responsable de traitement, agence et Promodev sous-traitants, et contrôle croisé Houston.
author: promogit
author_url: https://github.com/promogit/skills/tree/main/skills/promodev/reglement-jeu
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: fr
practice: consumer
language: fr
---

# Règlement complet de jeu (France, Word, validation client)

> **Aucune donnée client dans ce skill.** Les exemples sont fictifs ou génériques : aucun nom de client, d'agence, d'adresse, de DPO, de numéro d'opération ni de formulation propre à un client. Quand une information nécessaire manque dans les documents fournis ou dans Houston (société organisatrice, agence, adresse DPO ou délégation écrite à Promodev, durée de conservation, étude de dépôt, montants, dotations, formulation déjà validée pour ce client…), **poser la question** au chef de projet avant de rédiger. Ne jamais la reprendre d'une autre opération ni l'inventer.

Le règlement complet est le document contractuel d'un jeu promotionnel. Il est **déposé chez un commissaire de justice** et c'est la version déposée qui fait foi. Cinq conséquences :

- Le document est écrit **au nom de la Société Organisatrice** (la marque), jamais au nom de Promodev. Ne pas appliquer la charte `promo-dev-docs` : ni en-tête, ni logo Promodev. Promodev n'apparaît que comme prestataire / société gestionnaire, et comme sous-traitant pour les données personnelles (règle R1).
- Une fois le règlement déposé, le corriger coûte un **avenant** déposé lui aussi. Les contrôles du §9 comptent donc plus encore que pour des modalités.
- **Le règlement se rédige avant le montage de l'opération dans Houston.** C'est lui qui sert de base au paramétrage, une fois validé par le client. Au moment de la V1, le formulaire de participation n'existe donc généralement pas encore (§4.9).
- Quand l'opération est déjà montée (reconduction, duplication, relecture tardive), le texte et le paramétrage doivent concorder : un écart se voit en production.
- Chaque version envoyée au client doit montrer **ce qui a changé**, sinon il relit tout.

Ce skill couvre les **jeux France, soumis au droit français**. Les déclinaisons internationales (Italie DPR 430/2001, jeux multi-pays…) obéissent à d'autres règles juridiques : ne pas les traiter avec ce skill, le dire et demander au chef de projet.

Écrire en français, conventions des modèles : dates JJ/MM/AAAA, heures « 00h01 » / « 23h59 », montants « 30 € » ou « 30€ » (garder la forme du client), guillemets « », majuscules à « Société Organisatrice », « Participant », « Jeu », « Dotation », « Gagnant » dès qu'ils sont définis entre parenthèses.

## 0. Règles Promodev obligatoires

Elles s'appliquent à **tout** règlement : ceux que Promodev rédige, ceux que le client ou son agence rédigent, ceux qui reviennent annotés. Un document « VDEF » n'en est pas dispensé — les exemples validés en circulation ne les respectent pas tous.

Un manquement à R1, R2 ou R3 est **bloquant** (sauf les points d'adresse DPO, qui sont de simples alertes) : le signaler en tête du message, proposer la correction en suivi des modifications avec un commentaire qui explique la règle, et ne pas présenter le document comme prêt à déposer tant qu'il n'est pas corrigé ou que le chef de projet n'a pas décidé autrement.

### R1. Marque responsable de traitement, agence et Promodev sous-traitants, DPO du client

L'article données personnelles doit dire clairement :

- que la **Société Organisatrice** (raison sociale) est le **responsable de traitement** ;
- que les données sont traitées pour son compte par des **sous-traitants ou prestataires** : l'agence quand il y en a une, et PROMO.DEV (SAS, 276 avenue du Douard, 13400 Aubagne). Les termes « sous-traitant » et « prestataire » sont tous deux acceptés, et une mention générale (« ses sous-traitants et prestataires techniques ») l'est aussi tant que le rôle de responsable de traitement du client est écrit ;
- une **adresse pour exercer les droits** : adresse DPO de la Société Organisatrice, e-mail ou courrier.

Formulation de référence :

> Les Sociétés Gestionnaires, agissant en qualité de sous-traitantes pour le compte de la Société Organisatrice, responsable de traitement, s'engagent à traiter les données personnelles collectées pour la seule organisation du Jeu et conformément aux instructions documentées fournies par le Responsable de Traitement. Les données personnelles des Participants sont traitées sur la base de l'exécution du présent règlement de jeu conformément à l'article 6.1.b du RGPD.

**Opération avec agence** (cas fréquent). Il y a alors **deux sous-traitants**. Si le nom ou la raison sociale de l'agence ne figure dans aucun document, poser la question. Deux façons de l'écrire, les deux validées :
- les nommer ensemble sous un terme défini : « la société {AGENCE} […] et la société PROMODEV […] (ci-après les « Sociétés Gestionnaires ») », avec le partage des rôles à l'article 1 (qui achemine les dotations, qui valide la conformité et attribue) ;
- les lister comme destinataires : « Les Données collectées ne sont réservées qu'à l'usage des destinataires suivants : la société {AGENCE} et la société PROMO.DEV, sous-traitants de la société {MARQUE} ».

S'il y a d'autres prestataires (éditeur de webcoupons, agence de voyages, concession automobile, loueur), les citer aussi : ils reçoivent des données.

Sont **non conformes et à corriger** :
- aucun rôle indiqué, du type « Les Données collectées ne sont réservées qu'aux destinataires suivants : Promodev, {Agence} et la société organisatrice que vous consultez actuellement » : le rôle de responsable de traitement de la marque doit être écrit noir sur blanc ;
- Promodev ou l'agence présentés comme responsable de traitement ou responsable conjoint ;
- la politique de confidentialité de Promodev citée à la place de celle de la marque ;
- une adresse d'exercice des droits qui est celle de l'agence seule (ex. `production@agence.fr`) sans adresse DPO de la marque : le signaler et proposer d'ajouter l'adresse du client.

**Adresse DPO.** Règle générale : l'adresse du client (`dpo@marque.fr` ou service en charge des données). Exception : un client sans DPO qui a délégué par écrit l'exercice des droits à Promodev → `dpo@promo.dev`. Cette délégation ne se présume pas : si le client n'a pas de DPO connu, ou si `dpo@promo.dev` apparaît, demander au chef de projet si ce client a délégué par écrit. Ces points ne bloquent pas : les signaler comme alerte.

**Base légale.** Les exemples hésitent entre « exécution du contrat / du règlement » et « consentement du participant, qui dispose du droit de le retirer à tout moment ». C'est au client et à son DPO de trancher, mais signaler l'incohérence quand le règlement invoque le consentement alors que la case à cocher est **obligatoire** pour participer et que le même article dit qu'à défaut la participation ne peut pas être prise en compte. La prospection commerciale, elle, repose toujours sur le consentement (opt-in distinct et facultatif).

**Ce qui se reprend d'une version précédente** : la rédaction de l'article, la liste des destinataires, l'adresse d'exercice des droits, la durée de conservation, la base légale, les opt-ins, le renvoi à la politique de confidentialité et le tableau RGPD détaillé s'il y en a un. **Ce qui se vérifie quand même** : les règles ci-dessus, les rappels des articles 38 et 40 de la loi de 1978 (antérieurs à 2018 : proposer une rédaction à jour, RGPD et règlement (UE) 2016/679, à faire valider par le DPO), un prestataire qui n'intervient plus ou un nouveau absent de la liste, une durée de conservation calée sur l'édition précédente.

### R2. Ne jamais demander d'entourer les informations sur les justificatifs

Règle Promodev, identique à celle des modalités et confirmée pour les jeux : dans un **jeu avec obligation d'achat**, le règlement ne doit jamais demander au participant d'**entourer**, surligner, encadrer ou marquer une information sur son **ticket de caisse, sa facture d'achat ou son bon de commande** — ni la date d'achat, ni la référence ou le libellé du produit, ni le prix, ni le montant, ni l'enseigne. Même règle pour tout autre justificatif (code-barres, attestation).

- Rechercher : `entour`, `surlign`, `encadr`, `cercl`, `stabilo`, `marqu`, `souligne` dans une consigne au participant. Cas réel : un règlement demandait de télécharger le ticket « en entourant l'enseigne, la date d'achat et la référence du produit acheté » → à corriger.
- Remplacer par ce qui doit **figurer** sur le justificatif. Formulation validée : « Pour être considérée comme conforme, la preuve d'achat doit mentionner : la date d'achat (comprise dans la période du Jeu), le nom du point de vente, le produit éligible, le montant total du ticket de caisse, et ne pas avoir déjà été utilisée au titre d'une précédente participation. »
- La consigne « accordéon » est acceptable, elle ne demande pas de marquer le ticket : « Dans le cas où la preuve d'achat serait trop longue pour être numérisée, le Participant est autorisé à la plier "en accordéon", de manière à laisser apparaître les informations obligatoires listées ci-dessus. »
- Si le client demande d'ajouter une consigne d'entourage, ne pas l'appliquer : le signaler au chef de projet.

### R3. Dépôt chez le commissaire de justice

Le dépositaire par défaut de Promodev est la **SCP SYNERGIE – Commissaires de justice associés, 28 rue Fauchier, 13002 Marseille**. C'est cette adresse qu'il faut écrire, y compris quand un ancien modèle cite la même étude au 13006 : corriger vers 28 rue Fauchier, 13002.

Le dépôt se confirme malgré tout **au cas par cas auprès du chef de projet** — sauf quand une version précédente du même jeu indique déjà l'étude : la reprendre alors sans poser la question. Certains clients déposent chez leur propre étude : ne jamais remplacer d'office l'étude d'un règlement existant par la SCP SYNERGIE.

Le document doit contenir :

- un article « Accès au règlement » / « Dépôt du règlement » nommant l'étude, son adresse complète, et disant que le règlement est consultable gratuitement sur le site du jeu (avec une date limite de mise à disposition) ;
- pour un instant gagnant : la mention que **la table des instants gagnants** (ou la méthode d'attribution et la répartition des dotations) est déposée en même temps que le règlement — c'est ce qui rend la mécanique opposable. Formulation validée : « La table des instants gagnants ouverts est remise au commissaire de justice SCP SYNERGIE – Commissaires de justice associés, 28 rue Fauchier, 13002 Marseille, en même temps que le présent règlement. » ;
- la clause de modification : « L'Organisateur se réserve le droit de modifier à tout moment le Règlement sous la forme d'un avenant, qui sera publié sur le site » — et, si le client le souhaite, la clause de prévalence : « En cas de différence entre la version déposée et la version disponible sur le Site, seule la version déposée prévaudra. »

Contrôles :
- écrire **« commissaire de justice »** (la profession a remplacé « huissier de justice » en juillet 2022). Les anciens modèles écrivent encore « SCP SYNERGIE HUISSIERS 13 – Huissiers de Justice associés » : proposer la mise à jour du libellé, sans changer l'étude ;
- **une seule étude et une seule adresse dans tout le document** — 28 rue Fauchier, 13002 Marseille pour la SCP SYNERGIE ;
- pour un tirage au sort, certains clients déposent aussi **les coordonnées des gagnants** chez le commissaire de justice : le reprendre si le client le demande.

### R4. Le règlement et Houston doivent dire la même chose

Le sens du contrôle dépend du moment :

- **opération pas encore montée** (cas normal en V1) : le règlement est la source. Il décrit ce qui devra être paramétré — dates, nombre d'instants gagnants, lots, champs du formulaire. Rien à comparer, mais tout à écrire précisément, puisque le paramétrage en découlera ;
- **opération déjà montée** (reconduction, duplication, relecture tardive) : comparer le texte à `operation_gains` et `operation_info` (§9) et lister les écarts. Le règlement validé fait foi : signaler pour que le paramétrage soit repris, ne pas trancher seule.

## 1. Identifier la situation

| Situation | Déroulé |
|---|---|
| Nouveau jeu, rien d'existant | §2 brief → §3 base et style → §4 mécanique → §5 plan et clauses → §7 génération → §9 contrôles → V1 |
| Reconduction, ou un ancien règlement du client est fourni | Partir de ce fichier et l'adapter en **suivi des modifications**, sans repasser par les questions du §2.1 : tout ce qu'il contient est acquis. Ne demander que ce qui change cette année |
| Le client renvoie un Word annoté | §8 retour client → V(n+1) |
| Le client ou son agence envoie **son** règlement | §0 puis §9. Corrections en suivi des modifications (auteur `Promodev`) + commentaires + récapitulatif des écarts (§8 point 6) |
| Relecture avant dépôt | §0 puis §9, en insistant sur R3 et, si l'opération est montée, sur les contrôles Houston |
| Opération internationale | Hors périmètre : le dire et demander au chef de projet |

## 2. Rassembler le brief

**Principe : ne demander que ce qui n'est nulle part.** Chaque question coûte un aller-retour au chef de projet. Lire d'abord tout ce qui est disponible, puis poser en une seule fois les questions qui restent vraiment ouvertes.

1. **Les documents fournis** — à dépouiller avant tout le reste : ancien règlement du même jeu ou du même client, brief, e-mail, maquettes du site, modalités d'une autre opération du client, Excel produits.
2. **Houston**, si l'opération existe déjà (souvent pas le cas en V1) : `find_operation` puis `operation_info` (dates, pays, départements impliqués), `operation_gains` (`lotType`, `prizes`, `igSummary.total`, `codesSummary`), `list_forms` / `get_form` (parcours réel, §4.9), `list_datalists` (produits et EAN). Lire `read_houston_guide` section `operation-dates` avant de reprendre une échéance.
3. **Les mentions légales de la société**, à chercher soi-même (§2.2).
4. **Ce qui manque encore** → §2.1.

### 2.1 Ce qu'on demande au chef de projet, et seulement si ça manque

Deux informations ne se devinent jamais quand on part de zéro : **le nom de la société organisatrice** et **la liste des lots**.

**Quand un ancien règlement est fourni, ne pas poser ces questions** : il contient déjà la société organisatrice avec ses mentions légales, l'étude de dépôt, la structure, les clauses validées, le parcours de participation et la liste des lots de l'édition précédente. Tout reprendre de là, rédiger la V1, et se contenter de **signaler dans le message de livraison** ce qui a été repris tel quel : « lots, valeurs TTC, parcours et mentions légales repris de la V{n} du {date} — à me dire si quelque chose a changé cette année ». Une remarque dans la livraison vaut mieux qu'une question qui bloque le démarrage. Même logique si le brief, Houston ou un autre document du client répondent déjà.

**Le nom de la société organisatrice** — à demander seulement si aucun document ne le donne. Préciser qu'on veut la **société qui organise**, pas la marque commerciale : un groupe a souvent plusieurs entités et la marque du pack n'est pas toujours le nom de la société (ex. une marque de services portée par la filiale d'un groupe, une marque de vins portée par une société au nom différent). Le nom suffit, le reste se récupère (§2.2) ; un SIREN fait gagner du temps.

**La liste des lots** — à demander pour un nouveau jeu, ou quand les lots diffèrent de l'édition précédente. Pour chacun : **quantité**, **désignation exacte**, **valeur commerciale TTC unitaire**. Houston ne remplace pas cette demande — `operation_gains` donne le nom technique et la quantité (« gamelle », « setvoyage », « 30euros_tel »), mais **jamais la valeur commerciale** ni la désignation complète.

| Quantité | Désignation exacte | Valeur TTC unitaire | Attribution | Remise et délai | Validité / conditions |
|---|---|---|---|---|---|
| 12 | Séjour en résidence de vacances, carte cadeau dématérialisée, code à 14 caractères | 1 000 € | Instant gagnant | Appel de l'agence sous 10 jours ouvrés | 1 an, nominatif, taxes de séjour exclues |
| 250 | Trottinette modèle X, coloris bordeaux | 97 € | Instant gagnant | Colis, 2 à 6 semaines | — |
| 9 000 | Bon de réduction 1 € sur un pack de 12 gourdes | 1 € | Consolation, toute participation valide | Lien e-mail, webcoupon PDF | 90 jours, GMS distribuant la gamme |

Message type (nouveau jeu, sans document antérieur) :

> Pour rédiger le règlement de {nom du jeu}, il me faut deux choses :
> 1. Le **nom exact de la société organisatrice** (la société, pas la marque) — ou son SIREN si tu l'as. Je récupère le reste des mentions légales moi-même.
> 2. La **liste de tous les lots à gagner**, avec pour chacun la quantité, la désignation exacte (marque, modèle, couleur, contenu) et la valeur commerciale TTC unitaire. Ajoute si tu les as : comment le lot est attribué (instant gagnant, tirage au sort, lot de consolation pour tous), comment et sous quel délai il est remis, sa durée de validité et ses conditions d'utilisation.
>
> Si le parcours de participation prévu s'écarte du parcours habituel (coordonnées, infos d'achat, ticket de caisse), dis-le moi aussi. Et confirme-moi le dépôt : SCP SYNERGIE (28 rue Fauchier, 13002 Marseille) comme d'habitude, ou l'étude du client ?

Règles d'usage sur les lots :
- **ne jamais estimer une valeur TTC** : elle engage l'organisateur. Une valeur reprise d'une édition précédente s'écrit dans le document et se signale dans la livraison ; quand elle n'existe nulle part, laisser `[À COMPLÉTER : valeur TTC]` surligné en jaune ;
- ne pas rendre une V1 sans les trois informations pour chaque lot, ou le signaler explicitement comme incomplet ;
- pour un 100 % gagnant, la liste doit inclure le **lot de consolation** (§4.2), que les briefs oublient souvent.

### 2.2 Récupérer soi-même les mentions légales de la Société Organisatrice

L'article 1 a besoin de cinq informations : **forme juridique, capital social, ville et numéro RCS, adresse du siège social**, en plus du nom. Les chercher soi-même plutôt que de les demander.

**Sources, par ordre de préférence**
1. **Un règlement ou des modalités précédents du même client** : ces mentions ont déjà été validées par son juridique. Les reprendre telles quelles ; vérifier seulement, si le document a plus d'un an, que le capital social n'a pas bougé.
2. **L'Annuaire des Entreprises** (`annuaire-entreprises.data.gouv.fr`), service public adossé aux données INSEE et INPI : forme juridique, siège, SIREN, date de mise à jour. Attention aux établissements secondaires : c'est le **siège** qui va dans le règlement.
3. **Les mentions légales du site de la marque** : souvent la formulation exacte que le client emploie lui-même, capital compris.
4. Un annuaire d'entreprises (Pappers, société.com) pour recouper le capital, qui n'est pas toujours exposé par les deux premières sources.

**Méthode**
- Le **numéro RCS est le SIREN à 9 chiffres**, et la ville du RCS est celle du greffe, pas forcément celle du siège. Écrire « immatriculée au Registre du Commerce et des Sociétés de {ville} sous le numéro {9 chiffres} ».
- Croiser **deux sources** pour le capital social, la donnée la plus souvent périmée. Noter la date de consultation.
- Respecter la forme exacte : « société par actions simplifiée », « société anonyme », « SAS au capital de 2 206 500,00 € » — reprendre l'orthographe et la ponctuation du client quand un document précédent existe.
- Si plusieurs entités portent des noms proches, ou si la marque appartient à un groupe, **ne pas choisir seule** : proposer les candidates au chef de projet avec leur SIREN et laisser trancher.
- Si une source est inaccessible ou si le résultat reste douteux, laisser `[À COMPLÉTER]` surligné plutôt que d'écrire une valeur incertaine.

**Dans la livraison**, indiquer la source et la date quand les mentions viennent d'une recherche. Elles engagent le client : à faire confirmer par le chef de projet avant le dépôt. Quand elles sont reprises d'un règlement précédent, le dire aussi brièvement.

Ne pas confondre avec l'**adresse d'exercice des droits** (R1), souvent différente du siège — un client peut avoir son siège dans une commune et recevoir les demandes RGPD à une boîte postale dans une autre. Si les documents ne la donnent pas, poser la question.

### 2.3 Autres informations du brief

| Information | Remarque / valeur par défaut |
|---|---|
| Agence et rôle | Qui achemine les dotations, qui gère les réclamations, qui valide la conformité (Promodev en général) |
| Nom commercial du Jeu (entre « ») | Identique partout, y compris dans l'extrait de règlement |
| Mécanique | §4 : IG, 100 % gagnant, TAS, IG + TAS, challenge magasin, classement |
| Obligation d'achat | Avec (la majorité) / sans / achat + code. Change l'article 1 et les justificatifs |
| Dates | Début et fin du Jeu, fin d'achat, fin des inscriptions, date du tirage, limite de réclamation |
| Nombre d'instants gagnants | Doit égaler le total des lots attribués par IG (§9) |
| Parcours de participation | §4.9 : étapes, informations demandées, justificatifs, cases à cocher |
| Territoire | France métropolitaine, Corse incluse ou non ; DROM-COM et Monaco à trancher |
| Participants | Personnes physiques majeures / professionnels (SIREN, facture) / cas mineur (§4.7) |
| Limites | Par foyer, par personne, par jour, par ticket, par SIREN, par code |
| Commissaire de justice | SCP SYNERGIE, 28 rue Fauchier, 13002 Marseille par défaut ; reprise de la version précédente si elle existe, sinon à confirmer (R3) |
| Données personnelles | Adresse DPO du client, durée de conservation, base légale, opt-in marketing (R1) |
| Site du jeu, contact réclamation | URL exacte ; formulaire de contact ou e-mail (`contact@promo.dev` dans plusieurs règlements) |
| Régularisations | 3 maximum par dossier |
| Contrôle des originaux | Envoi sous 8 jours ; frais remboursés 1,51 € (lettre verte 20 g, tarif 2026 — faire confirmer chaque année) |

S'il manque une information, ne pas l'inventer : laisser `[À COMPLÉTER : …]` **surligné en jaune** et le lister dans le message.

## 3. Choisir la base et le style

**Priorité au modèle du client** s'il en a un : dupliquer le fichier et modifier le XML (méthode §8), pour garder sa mise en page et ses clauses validées par son juridique.

Sinon, quatre gabarits observés :

| Gabarit | Aspect | Quand | Origine |
|---|---|---|---|
| `promodev-articles` | « RÈGLEMENT COMPLET » centré, nom du jeu et dates en sous-titre, « ARTICLE N – TITRE » en majuscules, 16 articles, annexe produits | Défaut pour un jeu GMS avec obligation d'achat | Jeu GMS avec instant gagnant et bons de réduction |
| `agence-juridique` | Articles numérotés « ARTICLE 1. », sociétés gestionnaires définies à l'article 1, article RGPD court en sous-traitance, **extrait de règlement** en fin de document | Jeu rédigé avec l'agence ou son avocat, phases multiples | Jeu multi-phases rédigé avec une agence |
| `client-telecom` | Articles 1 à 10, dotations en tableaux, tableau RGPD (catégories / finalités / base légale / durée), jeu en 2 étapes | Le client fournit son modèle | Jeu d'un opérateur télécom en 2 étapes |
| `tas-court` | 13 à 15 articles, pas d'instant gagnant, article « Détermination du gagnant » court, beaucoup de clauses fraude et responsabilité | Tirage au sort seul, souvent B2B | Tirage au sort B2B |

Quand les lots sont nombreux ou détaillés, un **tableau Quantité / Description / Valeur commerciale unitaire** se lit mieux qu'une liste à puces (modèle `client-telecom`).

## 4. Catalogue des mécaniques (relevé Houston, septembre 2026 : 299 opérations de type jeu)

### 4.1 Instant gagnant ouvert (mécanique dominante, `lotType: IG`)

Houston génère une table de slots (date, heure, minute, seconde, lot, priorité). « Ouvert » signifie que la dotation reste en jeu jusqu'à ce qu'un participant joue après l'instant.

Le règlement doit préciser : le nombre total d'instants gagnants, leur répartition par dotation, le caractère aléatoire et préenregistré, le dépôt de la table (R3), le moment où le participant découvre son gain, et le mail qui fait foi.

> Pendant la durée du Jeu, {N} instants gagnants ouverts ({détail par dotation}) seront programmés permettant de désigner les gagnants de façon aléatoire.
> Un instant gagnant est défini par une date et une heure. Il est prévu qu'à cette date et cette heure une dotation soit mise en jeu. Un « instant gagnant » est dit « ouvert » lorsque la dotation reste en jeu jusqu'à ce qu'un Participant joue et remporte la dotation. Si aucune participation ne survient à cet instant, le gain reste en jeu et l'instant gagnant reste « ouvert ».
> Le premier Participant cliquant sur le bouton « JE JOUE » après cet instant gagnant remporte la dotation. Chaque instant gagnant ne peut correspondre qu'à un seul gain d'une seule dotation.

Variante plus courte : « L'instant-gagnant dit « ouvert » est prédéterminé pour un jour, une heure, une minute et une seconde, d'une façon aléatoire et préenregistrée par un Commissaire de Justice. »

À ajouter selon le cas :
- **annonce du gain en deux temps** quand les justificatifs sont contrôlés : affichage immédiat + premier e-mail « sous réserve de validité du dossier », puis second e-mail de confirmation définitive après vérification (ex. 72 heures) ;
- **dotation non validée ou refusée** : « Si les preuves d'achat d'un gagnant ne sont pas validées ou si un gagnant renonce à son lot, l'Organisateur se réserve le droit soit de le remettre en jeu par tirage au sort au terme de la période de l'opération, soit de conserver ledit lot. » ;
- **plafond par foyer sur les gros lots** : « dès lors qu'une dotation dite « gros lot » est gagnée dans un foyer, les membres dudit foyer ne pourront plus remporter de « gros lot ». Cela s'applique pour toutes les dotations gagnées, hors bons de réduction. » ;
- **vagues périodiques** (ex. « 1 mois, 1 cadeau », 12 vagues de 10 lots) : dire combien de dotations par période et si un lot non gagné est reporté.

### 4.2 100 % gagnant

Un jeu « 100 % gagnant » se construit **toujours sur deux niveaux** :

1. une mécanique de désignation pour les **lots principaux** — instants gagnants (le plus souvent) ou tirage au sort ;
2. une **dotation de consolation** attribuée à toute participation valide qui n'a pas décroché de lot principal : bon de réduction ou webcoupon dans la quasi-totalité des cas, parfois un code ou une remise.

C'est cette seconde couche qui rend le jeu « 100 % gagnant ». Elle n'est **pas** dans la table des instants gagnants de Houston : il est donc normal qu'une opération de ce type affiche peu de slots pour beaucoup de participations (ex. 120 slots pour 21 000 participations). Ne pas le signaler comme une anomalie.

Ce que le règlement doit faire :
- décrire les **deux niveaux** à l'article Dotations, séparément et sans ambiguïté sur celui qui est limité en nombre ;
- quantifier les lots principaux (et le nombre d'instants gagnants correspondant) ;
- dire à quelles conditions la consolation est attribuée : « toute participation valide », ou un quota du type « les 8 000 premiers participants recevront… ». Ne jamais laisser « des centaines de bons de réduction » sans quantité ni règle d'attribution ;
- préciser que les limites par foyer sur les gros lots **ne s'appliquent pas** aux bons de réduction, si c'est le choix du client (« Pour les E-BR, il n'y a pas de limitation sur les gains »).

Formulation validée :

> Le Jeu est « 100 % gagnant », ce qui sous-entend que le premier participant qui valide son formulaire d'inscription en cliquant sur le bouton « JE JOUE ! » au même moment qu'un instant-gagnant est ouvert, gagne la/les dotation(s) correspondante(s). Un instant-gagnant mis en ligne reste ouvert jusqu'à ce qu'un participant valide son inscription et se voie attribuer la dotation correspondante.

**Bon de réduction / webcoupon imprimable** — clause validée : lien par e-mail, webcoupon nominatif en PDF, impression possible **une seule fois**, responsabilité de l'imprimante au participant, magasin et délai d'utilisation (« dans les 90 jours suivant la génération, jusqu'au {date} »), et « En cas de dysfonctionnement de l'imprimante, le gagnant perd tout droit à son e-BR ». Si un éditeur tiers produit les coupons, le citer comme destinataire des données (R1).

**Consolation sous forme de code** (ex. 400 coffrets en IG et une dotation dématérialisée pour les autres) : canal de remise, durée de validité, conditions d'utilisation, comme pour un lot principal.

### 4.3 Instant gagnant + tirage au sort (jeu en deux phases)

Structure à deux phases, chacune avec ses dotations, sa désignation, sa remise et son délai de réclamation.

- Dire que l'inscription au tirage est **automatique** pour toute participation valide : « en cliquant sur « JE JOUE », et à condition que son dossier soit conforme, le Participant validera automatiquement sa participation à la phase 2 ». Le Jeu du Créneau précise utilement : « tout Participant participe automatiquement à l'Étape 2, qu'il ait choisi ou non de bénéficier de sa dotation de l'Étape 1 ».
- Donner la **date du tirage** et qui le réalise (§4.4).
- Prévoir des **délais de réclamation distincts** si les phases se terminent à des dates éloignées (Jeu du Créneau : 3 mois pour l'étape 1, 1 an pour l'étape 2).
- « Chaque Gagnant ne pourra remporter au maximum qu'une Dotation lors de chaque étape du Jeu. »

Un 100 % gagnant peut aussi être bâti sur cette structure : tirage au sort pour le gros lot, consolation pour tous (§4.2).

Dans Houston, seule la phase IG est paramétrée ; le tirage est réalisé hors outil à partir de l'export des participations valides.

### 4.4 Tirage au sort seul

Houston ne génère pas de slots : la dotation est déclarée mais le tirage est manuel. Le règlement porte toute la mécanique. Il doit dire :

- **qui tire et quand**, date précise : « Le tirage au sort sera effectué par le centre de gestion Promodev le {date} » ; « … par la société PROMO.DEV, sous-traitant de la société {MARQUE}, le {date} » ; ou par la Société Organisatrice elle-même ;
- **parmi qui** : « parmi l'ensemble des participations valides enregistrées entre le {date} et le {date} », en disant si la conformité est vérifiée avant ou après le tirage ;
- **le suppléant**, indispensable quand la conformité est contrôlée après tirage : « Si le dossier est conforme, alors le gain du participant tiré au sort est confirmé. Si le dossier ne respecte pas l'intégralité des modalités, alors un participant « suppléant » sera tiré au sort. » ;
- **le délai d'information du gagnant** (15 jours maximum après le tirage) et le nombre de tentatives de contact avant renonciation ;
- **le sort du lot non réclamé** : conservé, réattribué à un suppléant, ou utilisé dans une opération ultérieure — au choix du client, mais une seule règle dans tout le document.

**Chances multiples** (B2B) : « 1 foret ou 1 coffret acheté = 1 chance de gagner (2 achetés = 2 chances, 15 achetés = 15 chances) », avec en annexe les références qui comptent pour une seule chance, et la limite « une seule participation par facture/bon de commande et une seule dotation par SIREN ».

### 4.5 Challenge magasin / Winner Per Store

Aucune dotation n'est paramétrée dans Houston : le règlement porte seul la mécanique. Il doit dire comment le gagnant de chaque magasin est désigné (tirage par point de vente, meilleur résultat, premier inscrit), qui fait la désignation, à quelle date, et ce qui se passe pour un magasin sans participant valide. Demander ces points au chef de projet s'ils ne figurent nulle part.

### 4.6 Classement (`lotType: RANKING`)

Rare (5 opérations). Définir le critère de classement, la période de mesure, la règle de départage en cas d'égalité, le nombre de rangs récompensés (et le lot de chaque rang) et la date de publication.

### 4.7 Conditions d'entrée

**Avec obligation d'achat** (majorité) : l'article 1 le dit explicitement, les produits éligibles sont en annexe, la preuve d'achat suit R2. Une seule participation par ticket : « Ne seront pas prises en compte les participations fondées sur un même ticket de caisse. »

**Sans obligation d'achat** : le dire à l'article 1 (« un jeu gratuit sans obligation d'achat »). Pas de preuve d'achat, pas de régularisation de justificatif, et l'article frais se limite en général à : « Les frais de participation au Jeu quels qu'ils soient (frais de connexion internet) ne seront pas remboursés. » À faire valider par le client.

**Jeu à code d'entrée** (ex. Jeu du Créneau : 500 043 codes) : où le code est obtenu, usage unique, ce qui se passe si le code est déjà utilisé ou invalide, jusqu'à quand il peut être joué. Le code **d'entrée** ne doit pas être confondu avec le **code de dotation** envoyé au gagnant : deux termes distincts dans le règlement, sinon le service consommateur ne s'y retrouve plus.

**Participation en magasin / assistée** : si un vendeur peut jouer pour le participant (Jeu du Créneau en bureau de poste), l'écrire.

**Professionnels** : personnes morales, immatriculation au RCS ou au registre des métiers à la date de participation, SIREN et raison sociale, facture ou bon de commande en justificatif, limite par SIREN. Pas de clause « personne physique majeure ».

**Mineurs** : à éviter, mais il existe des cas (Jeu du Créneau, dès 15 ans). Alors : justificatif d'éligibilité, souscription ou remise au nom du représentant légal, clause dédiée pour les dotations qui exigent la majorité.

**Adresses e-mail jetables** : « Toute participation initiée avec une adresse électronique temporaire (telle que notamment @yopmail.com) ne sera pas considérée comme valide et sera exclue » — cohérent avec l'option `blockTempEmailProviders` du champ e-mail Houston.

### 4.8 Dotations

L'article Dotations se rédige à partir de la liste des lots (§2.1, ou le règlement précédent). Pour chaque lot : **quantité**, **désignation exacte**, **valeur commerciale TTC unitaire indicative**, mode de remise, délai, validité. Aucune de ces trois premières informations ne s'invente ni ne se déduit de Houston, qui ne porte pas les valeurs commerciales.

Puis les clauses communes : valeur déterminée à la date de rédaction et non contestable, remplacement possible par une dotation équivalente en cas de force majeure, dotation nominative, non échangeable, non cessible, pas de contre-valeur en espèces, visuels non contractuels.

Selon la nature, ajouter :
- **séjour / voyage** : inclus et exclus (transport, repas, assurances, taxes de séjour), période de réservation et exclusions, délai de réservation, titres d'identité et formalités à la charge du gagnant, conséquence d'une indisponibilité, prestataire qui organise le voyage (à citer comme destinataire des données) ;
- **carte cadeau dématérialisée** : forme (« un code à 14 caractères »), validité, caractère nominatif, non remboursable ;
- **bon de réduction / webcoupon** : §4.2 ;
- **virement** : e-mail pour renseigner l'IBAN, **IBAN commençant par « FR »** (27 caractères : FR + 25), délai de 4 à 6 semaines après validation ;
- **colis** : adresse du formulaire, délai (2 à 6 semaines), pas de seconde livraison en cas d'adresse erronée, date butoir au-delà de laquelle la dotation est réputée refusée ;
- **dotation liée à une souscription** (télécom, automobile) : conditions, incompatibilités, conséquence d'une résiliation, remise par un tiers ;
- **stock** : « dans la limite des stocks disponibles » seulement si le client le demande.

### 4.9 Parcours de participation

Le règlement décrit les étapes que le participant devra suivre. **La source dépend du moment où l'on rédige**, et le cas le plus fréquent est celui où le formulaire n'existe pas encore.

**Cas 1 — l'opération n'est pas encore montée dans Houston (V1 habituelle).** Le règlement précède le paramétrage : c'est lui qui servira à monter le formulaire CREATE une fois validé par le client. Construire le parcours, dans cet ordre de préférence, depuis :
1. le **règlement de l'édition précédente** du même jeu ou d'un autre jeu du même client ;
2. le **brief, les maquettes ou le zoning** du site fournis par l'agence ou le client ;
3. à défaut, le **parcours standard Promodev** ci-dessous, en le faisant confirmer.

Parcours standard d'un jeu avec obligation d'achat :
> 1. Acheter un produit éligible (liste en annexe) entre le {date} et le {date}, dans les magasins participants, et conserver sa preuve d'achat (1 preuve d'achat = 1 participation).
> 2. Se connecter sur {site} entre le {date} 00h01 et le {date} 23h59 et cliquer sur « JE PARTICIPE ».
> 3. Compléter ses données personnelles : civilité, nom, prénom, adresse postale, adresse e-mail, numéro de téléphone.
> 4. Compléter ses informations d'achat : date d'achat, enseigne, référence du ou des produits achetés.
> 5. Télécharger une photo, un scan ou un PDF complet et lisible de son ticket de caisse original (informations qui doivent y figurer : R2), et le cas échéant le code-barres du produit.
> 6. Accepter le règlement et le traitement de ses données personnelles en cochant les cases prévues, et certifier être majeur.
> 7. Cliquer sur « JE JOUE » : le Participant découvre immédiatement s'il a remporté une dotation {et est automatiquement inscrit au tirage au sort}.

Adapter selon la mécanique : pas de preuve d'achat ni d'informations d'achat pour un jeu sans obligation d'achat ; saisie du code d'entrée pour un jeu à code ; raison sociale, SIREN et facture pour un jeu professionnel ; IBAN uniquement si une dotation est un virement (à réclamer après le gain, pas à la participation).

Décrire ensuite ce que reçoit le participant : e-mail de confirmation, e-mail de régularisation en cas de dossier incomplet (3 régularisations maximum), e-mail de confirmation définitive du gain.

Écrire le parcours **au niveau de détail que le client peut tenir** : chaque champ annoncé devra exister dans le formulaire, et chaque limite annoncée devra être contrôlable (pas de limite « par foyer » si rien ne l'empêche techniquement). Dans le doute, rester sur la formulation générique « ses données personnelles » plutôt que d'énumérer un champ incertain. Signaler dans la livraison : « parcours à aligner avec le formulaire CREATE au moment du paramétrage ».

**Cas 2 — l'opération est déjà montée** (reconduction dupliquée, règlement rédigé après le montage, relecture avant dépôt). Vérifier le parcours contre le formulaire réel : `list_forms(operationId)` → formulaire `type: CREATE` → `get_form(formulaireId)` (étapes, `label`, `save_to`, `required`, `displayIf`, `options`, `accept`), puis `list_email_templates(operationId)` pour les e-mails. Comparer dans les deux sens : un justificatif demandé sur le site mais absent du règlement, une information annoncée dans le règlement mais non collectée. Lister les écarts sans trancher : c'est le règlement déposé qui fait foi, le paramétrage se corrige.

**Après le montage**, le contrôle définitif du parcours se fait avec la procédure de test de l'opération (skill `promodev-test-procedure`).

## 5. Plan type et clauses réutilisables

Plan `promodev-articles` (16 articles, à adapter) :

1. **Organisation du jeu** — 1.1 Société Organisatrice (raison sociale, forme, capital, siège, RCS : §2.2), période, type de jeu, nom entre « », nature de la mécanique ; 1.2 Société prestataire (agence et Promodev, rôles) ; site du jeu
2. **Conditions de participation** — territoire, majorité, exclusions, limites par foyer et par jour, participations non prises en compte, disqualification
3. **Acceptation du règlement** — acceptation pleine et entière, loyauté, interdiction des robots, vérifications
4. **Annonce du jeu** — mini-site, site de la marque, PLV, packs, réseaux sociaux
5. **Dotations mises en jeu** — §4.8, avec les deux niveaux s'il s'agit d'un 100 % gagnant (§4.2)
6. **Modalités de participation** — parcours du §4.9, contenu exigé de la preuve d'achat (R2), régularisation, conservation et contrôle des originaux
7. **Détermination des gagnants** — §4.1 à §4.6, annonce du gain, sort des dossiers non validés
8. **Modalités d'obtention de la dotation** — une sous-partie par lot, délais, coordonnées erronées, renonciation
9. **Modalités générales** — modification, prolongation, annulation ; Internet non sécurisé
10. **Protection des données personnelles** — R1
11. **Accès au règlement** — R3
12. **Réclamation** — canal et date limite
13. **Propriété intellectuelle**
14. **Responsabilité**
15. **Indépendance des clauses**
16. **Loi applicable** — loi française, tribunaux compétents
- **Annexe : produits éligibles**

**Clauses prêtes à l'emploi**

Article 1, société organisatrice (mentions du §2.2) :
> La société {RAISON SOCIALE} (ci-après dénommée la « Société Organisatrice »), {forme juridique} au capital de {capital} €, ayant son siège social {adresse du siège}, immatriculée au Registre du Commerce et des Sociétés de {ville du greffe} sous le numéro {SIREN}, organise du {JJ/MM/AAAA} au {JJ/MM/AAAA} inclus un jeu {avec / sans} obligation d'achat intitulé « {NOM DU JEU} » (ci-après dénommé le « Jeu »).

Régularisation :
> Tout dossier partiellement non conforme mais régularisable (pièce manquante, information incomplète ou justificatif illisible) pourra faire l'objet d'une demande de régularisation adressée au participant par e-mail. Le participant dispose d'un maximum de trois (3) régularisations par dossier. Au-delà de ces trois (3) régularisations, le dossier sera définitivement invalidé. Les dossiers non conformes et non régularisables au regard des modalités de jeu seront invalides immédiatement, sans possibilité de régularisation.

Contrôle des originaux :
> Il est demandé aux Participants de conserver l'original de leur preuve d'achat, qui pourra leur être demandée à tout moment. L'Organisateur se réserve le droit de demander l'envoi par voie postale des éléments du dossier à des fins de contrôles complémentaires. Les frais d'affranchissement des dossiers seront remboursés à hauteur de 1,51 €, tarif {AAAA} en vigueur.

Valeur des dotations :
> La valeur des dotations est déterminée au moment de la rédaction du présent Règlement. Elle ne pourra en aucun cas faire l'objet d'une contestation quant à son évaluation. Les visuels présents sur le site ne sont pas contractuels.

Élection de domicile :
> Le gagnant fait élection de domicile à l'adresse postale qu'il aura indiquée et confirmée lors de l'inscription. Dans un souci de confidentialité, il ne sera effectué aucun envoi ni communication téléphonique de la liste des gagnants.

Dotation non remise :
> Toute dotation qui n'aurait pas pu être remise au gagnant en raison de coordonnées inexactes sera tenue à sa disposition dans un délai de {N} semaines à compter de la fin du Jeu. Tout gagnant qui n'aurait pas réclamé sa dotation par courriel ({contact}) passé cette date sera réputé avoir renoncé à celle-ci. Cette dotation pourra librement être remise en jeu par l'Organisateur, sans que sa responsabilité puisse être engagée.

Réclamation :
> Le Participant peut adresser toute réclamation, contestation, demande ou communication relative au Jeu ou au Règlement via le formulaire de contact du site {site}. Lesdites demandes pourront être adressées jusqu'au {date} au plus tard. Aucune réclamation ne sera prise en compte passée cette date.

Dépôt (R3) :
> Le Règlement est déposé auprès de la SCP SYNERGIE – Commissaires de justice associés, 28 rue Fauchier, 13002 Marseille. Le Règlement est consultable sur le site {site}.

Données personnelles : formulation de référence en R1.

## 6. Extrait de règlement

Pour la PLV, un encart ou un pack, le client demande souvent un **extrait de règlement** : un paragraphe qui reprend l'organisateur, les dates, l'éligibilité, les étapes de participation, le renvoi au règlement complet, l'adresse d'exercice des droits et l'étude de dépôt. Si le client n'a pas fourni de modèle d'extrait, le rédiger à partir du règlement et le faire valider. Vérifier qu'aucune information n'y contredit le règlement.

## 7. Générer le Word

Si un règlement précédent existe, partir de son fichier (§8). Sinon, générer avec `python-docx` : le helper `modalites_docx.py` du skill **modalites-operation** (§7) convient tel quel — mêmes styles, mêmes tableaux, mêmes surlignages `[À COMPLÉTER]`. Style `articles`, titre en trois lignes « RÈGLEMENT COMPLET » / « {NOM DU JEU} » / « DU {date} AU {date} », un `intertitre` par article.

Les intertitres des règlements sont en majuscules : passer `head="majuscules"` ou écrire « ARTICLE N – TITRE » en dur. Pour un tableau de lots, `tableau(...)` avec les colonnes Quantité / Description / Valeur commerciale unitaire.

Toujours faire un rendu visuel avant l'envoi (conversion PDF avec le script `soffice` du skill docx, puis `pdftoppm`) et regarder la première page, l'article Dotations et l'annexe.

## 8. Retour client → version suivante

Charger le skill **docx** pour la mécanique XML (unzip, `merge_runs.py`, `comment.py`, `validate.py --author`).

1. **Lire le retour** : `pandoc --track-changes=all -t markdown fichier.docx`.
2. **Dresser la liste des demandes** : emplacement, demande, décision proposée.
3. **Signaler avant d'appliquer** toute demande qui : touche R1, R2 ou R3 ; contredit un paramétrage déjà en place ; supprime une protection (limite par foyer, régularisation, contrôle des originaux, suppléant) ; annonce un champ ou un contrôle que le formulaire ne pourra pas porter. Une correction des mentions légales ou d'un lot par le client est au contraire à appliquer sans discuter.
4. **Produire V(n+1) à partir du fichier renvoyé par le client**, jamais d'une version antérieure. Modifications Promodev en suivi (`<w:ins>` / `<w:del>`, auteur `Promodev`), réponses aux commentaires traités, répercussion de chaque changement partout (une date modifiée à l'article 1 se retrouve aux articles 5, 6, 7, 11 et 12 ; un lot modifié à l'article 5 se retrouve aux articles 7 et 8).
5. Refaire les contrôles §0 et §9 sur la version complète.
6. **Récapitulatif** en fin de réponse, prêt à coller dans l'e-mail : tableau Emplacement / Demande / Traitement, puis les points en attente.

Nommage : `{idgame} - Règlement {Nom du jeu} - V{n}.docx`, puis `VDEF` pour la version validée, et une copie propre sans marques de révision ni commentaires pour le dépôt.

## 9. Contrôles avant chaque envoi

Extraire le texte (`pandoc -t plain`) et vérifier point par point. Signaler, ne pas corriger en silence ce qui relève d'un choix du client.

**Règles Promodev (§0)**
- R1 : marque nommée responsable de traitement ; agence et Promodev en sous-traitants ; adresse DPO du client (alerte si absente) ; tous les destinataires réels cités (éditeur de coupons, agence de voyages, concession) ; rappels de la loi de 1978 à moderniser.
- R2 : `grep -n -i -E "entour|surlign|encadr|cercl|stabilo"`, y compris dans les images d'exemple de ticket.
- R3 : étude nommée avec son adresse complète, identique partout (SCP SYNERGIE → 28 rue Fauchier, 13002 Marseille) ; « commissaire de justice » ; dépôt de la table des instants gagnants pour un IG ; clause d'avenant.

**Mentions légales de la Société Organisatrice (§2.2)**
- Les cinq informations sont présentes à l'article 1 : forme juridique, capital, siège, ville du RCS, numéro RCS (SIREN à 9 chiffres).
- Elles correspondent à leur source (règlement précédent, ou recherche dont la référence et la date figurent dans la livraison).
- Écart avec le règlement précédent : signalé (capital augmenté, siège déplacé, fusion).
- La société nommée est bien l'organisatrice, pas la marque ni une autre entité du groupe.
- Le siège n'est pas confondu avec l'adresse d'exercice des droits (R1) ni avec l'adresse de retour des justificatifs.

**Les lots**
- Chaque lot porte ses trois informations : **quantité**, **désignation exacte**, **valeur TTC unitaire**. Un lot sans valeur ou sans quantité (« des centaines de bons de réduction ») est un `[À COMPLÉTER]` à remonter.
- Les lots du règlement = la liste reçue ou reprise de l'édition précédente : aucun en plus, aucun oublié. Ce qui vient de l'édition précédente est signalé dans la livraison.
- Chaque lot décrit à l'article Dotations a son mode de remise à l'article Obtention, et réciproquement.

**Parcours de participation (§4.9)**
- Les étapes sont complètes et dans l'ordre : achat, connexion, données personnelles, informations d'achat, justificatifs, cases à cocher, validation, résultat.
- Chaque champ annoncé est un champ que le formulaire devra réellement porter, et chaque limite annoncée est contrôlable.
- Pas d'IBAN demandé à la participation quand il ne sert qu'après un gain, pas de justificatif annoncé pour un jeu sans obligation d'achat.
- Si l'opération est montée : comparaison avec le formulaire CREATE dans les deux sens. Sinon : mention « parcours à aligner avec le formulaire au paramétrage » dans la livraison.

**Mécanique ↔ Houston, si l'opération est montée (`operation_gains`, `operation_info`)**

| À vérifier | Où |
|---|---|
| Nombre d'instants gagnants annoncé | `igSummary.total` (ex. règlement 262 = Houston 262 ✔ ; règlement 121, Houston 120 ✘) |
| Quantité par lot principal | `prizes[].nb` et `libelle` |
| Lot de consolation d'un 100 % gagnant | **Normalement absent de `prizes` et de la table IG** : ne pas le signaler comme une anomalie (§4.2) |
| Pool de codes d'entrée | `codesSummary.total` |
| Mécanique réelle | `lotType` : `IG` = instants gagnants ; `IG` avec `igsTableGenerated: false` et 0 slot = tirage au sort seul ; `RANKING` = classement ; `lotType: null` = rien de paramétré (challenge magasin) |
| Période d'achat | `date_debut` → `date_fin_achat` |
| Fin des inscriptions | `date_fin` (souvent postérieure à la fin d'achat : ex. achat jusqu'au 18/10, inscriptions jusqu'au 25/10 — les deux dates doivent apparaître distinctement) |
| Régularisation, réclamation | `date_fin_regule`, `date_fin_reclamation` |
| Justificatifs contrôlés | `involvedDepartment.saisie` ; logistique : `logistic` |

Lire `read_houston_guide` section `operation-dates` avant de conclure sur une échéance.

**Cohérence interne**
- Chaque date identique partout, chronologie : début ≤ fin d'achat ≤ fin des inscriptions < date du tirage < limite de réclamation. Les jours et mois correspondent entre « 18 octobre » et « 18/10 ».
- Total des lots attribués par instants gagnants = nombre d'instants gagnants annoncé (la consolation est hors table).
- Même nom du Jeu mot pour mot (titre, article 1, extrait de règlement, e-mails), même URL, même e-mail de contact, même étude, même raison sociale.
- Valeurs TTC et quantités identiques entre l'article Dotations, l'article Obtention, les tableaux et l'extrait.
- Une seule règle de limitation, avec les mêmes critères partout, et l'exception éventuelle pour les bons de réduction écrite une seule fois.
- Renvois internes justes après toute insertion d'article.
- Base légale cohérente d'un bout à l'autre (R1).

**Restes d'autres documents**
- Vocabulaire ODR dans un règlement de jeu : « remboursement », « offre de remboursement », « prime » pour un lot, IBAN demandé sans dotation en virement.
- Lots, nom, dates, site, étude, DPO, raison sociale ou produits d'une autre opération.
- Année précédente : tarif postal, dates de l'édition précédente, capital social périmé.
- « Huissier de justice » au lieu de « commissaire de justice », ou la SCP SYNERGIE au 13006 (R3).

**Exactitude**
- IBAN France : « FR » + 25 caractères, soit 27. « IBAN commençant par FR (25 caractères) » est faux.
- RCS = SIREN à 9 chiffres ; EAN = 13 chiffres.
- Annexe produits : nombre de lignes = fichier source, pas de doublon, montants et libellés identiques à la liste Houston si elle existe.
- Coquilles récurrentes : « force majeure », « jours calendaires », « personnes physiques majeures », « Règlement (UE) 2016/679 », « instants gagnants » au pluriel.

## 10. Livraison

- Écrire le .docx dans `/mnt/user-data/outputs/`. Si un dossier de l'ordinateur de l'utilisateur est connecté, l'enregistrer à côté des versions précédentes, sans écraser un fichier existant.
- Message court, dans cet ordre : manquements bloquants (R1, R2, R3), ce qui a été **repris d'une version précédente** et mérite un regard (lots, valeurs TTC, parcours, mentions légales, étude), source et date des mentions légales quand elles viennent d'une recherche, **« parcours à aligner avec le formulaire CREATE au paramétrage »** si l'opération n'est pas encore montée, écarts avec Houston si elle l'est, alertes DPO, ce qui a été produit, `[À COMPLÉTER]` restants, autres points du §9, et pour une V2+ le tableau récapitulatif du §8.
- Rappeler, quand la version est validée, qu'il reste à produire une copie propre pour le dépôt, avec la table des instants gagnants si la mécanique en comporte une, et que le règlement validé sert de base au montage de l'opération dans Houston.

## 11. Points à faire trancher par le chef de projet

- base légale à privilégier (exécution du règlement ou consentement) et position à tenir quand le DPO du client impose l'autre ;
- clause de remboursement des frais de participation pour un jeu sans obligation d'achat ;
- règle par défaut pour un lot non réclamé (conservé, remis en jeu, réattribué à un suppléant) ;
- existence d'un modèle Promodev pour les challenges magasin / Winner Per Store, dont aucun exemple rédigé n'est encore passé par ce skill.

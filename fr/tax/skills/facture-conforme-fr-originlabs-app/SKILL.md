---
name: facture-conforme-fr-originlabs-app
title: Vérifier qu'une facture est en règle
description: 'Vérifier qu''une facture est en règle. Méthode professionnelle française, avec ses pièges et ses questions à poser. À utiliser quand : Contrôler une facture client avant envoi, ou une facture fournisseur avant paiement ou comptabilisation ; Contrôler un lot de factures pour un client du cabinet ; Répondre à une question précise sur une mention (« faut-il le SIREN du client ? », « quelle mention en franchise ? »).'
author: originlabs-app
author_url: https://github.com/originlabs-app/origin-skill-install/tree/main/skills/facture-conforme-fr
license: CC-BY-4.0
version: 0.1.0
execution_mode: open
jurisdiction: fr
practice: tax
language: fr
---

> **Version gratuite : règles datées entre le 18/07/2026 et le 04/10/2026.** Les règles changent (SMIC, TVA, seuils…). Avec l'abonnement OriginSkill, votre assistant reçoit la règle à jour, avec sa source et sa date.

# Vérifier qu'une facture est en règle

## Quand l'utiliser

- Contrôler une facture client avant envoi, ou une facture fournisseur avant paiement ou comptabilisation.
- Contrôler un lot de factures pour un client du cabinet.
- Répondre à une question précise sur une mention (« faut-il le SIREN du client ? », « quelle mention en franchise ? »).
- Préparer un avoir ou une facture rectificative à relire.

Quand **ne pas** l'utiliser : savoir si l'entreprise est concernée par la réforme de la
facture électronique et à quelle date (fiche `facturation-electronique-2026`) ; trancher
une opération de TVA internationale, un régime de marge ou une exonération (orienter vers
l'expert-comptable, en le disant).

## Connaissances du métier

Une facture française porte trois couches de mentions. Les mentions **fiscales** (Code
général des impôts) valent pour toute facture : identité et adresse des parties, SIREN du
vendeur, numéro, dates, lignes, TVA par taux, totaux. Les mentions **commerciales** (Code de
commerce) s'ajoutent entre professionnels : date d'échéance, escompte, pénalités de retard,
indemnité forfaitaire de recouvrement, bon de commande s'il existe. Les mentions de
**situation** dépendent du cas : franchise en base, autoliquidation, forme juridique et
capital d'une société, et depuis la réforme de 2026 quatre nouvelles mentions (SIREN du
client, adresse de livraison distincte, nature de l'opération, option pour les débits).

Ce qui est exigé dépend donc de faits sur la situation, pas seulement de la facture : le
client est-il un professionnel, le vendeur une société, la TVA est-elle autoliquidée,
l'émetteur est-il déjà soumis à la facture électronique. Quand un de ces faits manque, la
mention qui en dépend reste « à confirmer » ; on ne la déclare ni conforme ni absente.

**Le SIREN du client : à partir de quand, et pourquoi.** La réforme ajoute quatre mentions
aux factures entre professionnels (SIREN du client, adresse de livraison si elle diffère,
nature de l'opération, option pour les débits ; décret n° 2022-1299 du 7 octobre 2022,
modifié par le décret n° 2024-266 du 25 mars 2024, Légifrance). Elles ne sont pas exigibles
le même jour pour tous : elles suivent le calendrier d'émission de l'émetteur, **au
01/09/2026 pour les grandes entreprises et les ETI, au 01/09/2027 pour les PME, les TPE et
les micro-entreprises** (loi de finances pour 2024, art. 91). Répondre « depuis le
1er septembre 2026 » sans dire la taille de l'émetteur laisse croire que tout le monde y est
déjà : donner la date de la taille, ou les deux dates si elle est inconnue (chaque règle
sort avec une date par taille). La raison d'être, d'après les sources officielles : la
facture électronique passe par une plateforme agréée, pas directement d'une messagerie à
l'autre. Cette plateforme doit retrouver celle du client, qui figure dans l'annuaire de la
facturation électronique (il recense les entreprises assujetties, leur plateforme et leur
adresse de facturation), et les données de la facture sont transmises à l'administration
(economie.gouv.fr, « Qu'est-ce que l'annuaire de la facturation électronique ? », 30/09/2025 ;
impots.gouv.fr, « Je découvre la facturation électronique », mis à jour le 26/05/2026,
consultés le 04/07/2026). Le SIREN est l'identifiant de l'entreprise. Le décret n'énonce pas
cette finalité : que le SIREN serve à retrouver le client dans l'annuaire est la lecture de
ces sources, à présenter comme telle. Les amendes de la réforme (50 EUR par facture non
émise en électronique, 500 EUR par transmission de données manquante, Service-Public,
actualité A18802 du 20/02/2026) sont **à relire sur le texte officiel avant de les citer** :
d'autres sources professionnelles donnent encore 15 EUR et 250 EUR, montants d'avant la loi
de finances pour 2026.

Une facture ne se corrige jamais en la modifiant : on émet un avoir ou une facture
rectificative qui renvoie à la facture d'origine.

**Facture émise au mauvais client.** On n'efface pas la facture et on ne réutilise pas son
numéro (la numérotation suit une séquence chronologique continue, CGI annexe II art. 242 nonies A).
On émet un avoir qui reprend ses montants en négatif (HT, TVA, TTC) et renvoie à son numéro, puis
une nouvelle facture au bon client, au numéro suivant de la série des factures et à la date du jour.
Le client erroné est prévenu qu'il peut ignorer la première facture. La TVA d'une prestation de
services n'est en principe exigible qu'à l'encaissement, sauf option pour les débits : demander
si la société a opté, car la TVA a pu être déclarée dès l'émission et l'avoir la régularise alors
sur la déclaration en cours.

**Conservation : toujours donner les deux durées, et dire que la durée fiscale change.** Les
documents comptables et leurs pièces justificatives, dont les factures, se conservent dix ans
(Code de commerce art. L123-22, texte lu sur Légifrance le 03/10/2026). La durée fiscale de
conservation des factures et pièces (Livre des procédures fiscales art. L102 B) est de **six ans
jusqu'au 31/12/2026** (version en vigueur depuis le 01/01/2023, texte lu sur Légifrance le
04/10/2026), puis de **dix ans à compter du 01/01/2027** pour les documents et pièces dont le délai
de conservation expire après le 1er janvier 2027 (version annoncée du même article, texte lu sur
Légifrance le 04/10/2026 ; l'article 36, II, de la loi n° 2026-534 du 25/06/2026, lu le même jour, le dit aussi). Une
facture de 2024, dont le délai de six ans expirerait en 2030, entre donc dans la seconde durée :
c'est la lecture de ces deux textes, à présenter comme telle ; le délai qui expirerait exactement
le 1er janvier 2027 n'est pas tranché par le texte relevé. Une version annoncée peut encore être
modifiée ou reportée (la recodification de la TVA l'a été) : à confirmer à l'approche du
01/01/2027 avec `article_en_vigueur` sur L102 B (Livre des procédures fiscales), qui rend la durée
applicable à la date demandée et annonce la bascule. Une réponse qui n'en donne qu'une des deux
durées, ou qui ne dit pas que la durée fiscale change, est incomplète.

## Pièges fréquents

- **Vérifier la présence des totaux sans refaire les calculs.** Une TVA à 210 EUR sur
  1 000 EUR HT à 20 % passe inaperçue à l'œil. Toujours faire refaire les calculs par l'outil.
- **Exiger de la TVA sur une facture en franchise en base.** Il faut alors la mention exacte
  de l'article 293 B, pas un taux.
- **Oublier les mentions commerciales entre professionnels.** Pénalités de retard et indemnité
  de 40 EUR sont les plus souvent absentes.
- **Prendre un numéro de TVA bien formé pour un numéro valide.** La clé se calcule depuis le SIREN.
  Un SIREN qui échoue au contrôle de clé (Luhn) et une clé de TVA incohérente sont deux constats
  distincts : le dire tel que l'outil le détaille, sans déclarer faux un numéro de TVA dont la clé
  est cohérente.
- **Confondre PDF envoyé par e-mail et facture électronique.** Un PDF n'est pas une facture électronique. Un émetteur déjà soumis à l'émission électronique doit envoyer une facture structurée par une plateforme agréée ; avant sa date (`reforme_calendrier`), le PDF reste admis.
- **Qualifier « non conforme » une facture reçue** alors que le point est à confirmer avec le
  fournisseur : distinguer ce qui est absent de ce qui dépend d'un fait inconnu.

## Méthodes proposées (jamais imposées)

1. **Contrôle avant envoi ou paiement** : identifier la situation, faire passer l'outil,
   corriger d'abord ce qui est absent ou faux, puis confirmer le reste. Détails :
   `methode-controle-avant-envoi`.
2. **Contrôle d'un lot par sondage** : pour un cabinet qui reçoit des centaines de factures,
   choisir un échantillon selon le risque plutôt que tout relire. Détails :
   `methode-lot-par-sondage`.

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

L'exécution exacte est servie par le connecteur, sur le moteur facturation partagé.

| Outil | Sert à | Appeler quand |
| --- | --- | --- |
| `facture_verifier` | Contrôler mention par mention (présente, absente, invalide, à confirmer), valider SIREN et clé de TVA, refaire les calculs ligne par ligne et les totaux | Une facture est fournie, ou un projet de facture ou d'avoir est à relire |
| `reforme_calendrier` | Dire si l'émetteur est déjà soumis à la facture électronique à la date de la facture | Le doute porte sur les nouvelles mentions de la réforme |
| `entreprise_profil` | Rendre dénomination, forme juridique et état (actif ou cessé) d'une entreprise à partir de son SIREN, source datée | Le SIREN du vendeur ou du client est à recouper avec les bases publiques |
| `bodacc_annonces` (nom servi : `orizon_bodacc_annonces`) | Lire en direct les annonces BODACC d'un SIREN, datées et avec leur lien : procédures collectives (jugement tel que publié), ventes et cessions, modifications, radiations ; un signal de risque si une procédure collective n'est pas clôturée | Le SIREN du client ou du vendeur est à recouper avec une procédure collective, une radiation ou une cession publiée |
| `vies_tva` (nom servi : `orizon_vies_tva`) | Interroger VIES (Commission européenne) en direct : le numéro de TVA intracommunautaire d'un client de l'Union est-il actif à l'instant T ? Statut valide, non valide ou non vérifié, date et heure de consultation, source ; pays en panne = non vérifié, jamais un oui deviné | Le client est établi dans un autre État membre et la facture serait sans TVA (livraison intracommunautaire) : vérifier son numéro avant de facturer, et conserver la preuve. **Outil ouvert progressivement : il n'existe que s'il figure dans la liste `outils` rendue par `orizon_fiche` ; sinon, demander au client de vérifier le numéro sur le site de VIES (ec.europa.eu/taxation_customs/vies) et de conserver la preuve (date, heure, résultat), sans le déclarer valide de mémoire.** |
| `taux_change_bce` (nom servi : `orizon_taux_change_bce`) | Lire le taux de change de référence de la BCE d'une devise contre l'euro (dernier taux publié, ou celui d'un jour passé), avec sa source et la date réelle de consultation, et convertir un montant au centième ; il ne dit pas la règle de conversion d'une facture ou d'une TVA | Une devise étrangère entre dans la facture ou le plan. **Outil ouvert progressivement : il n'existe que s'il figure dans la liste `outils` rendue par `orizon_fiche` ; sinon, demander le taux au client ou le lui faire lire sur le site de la BCE, sans en citer un de mémoire.** |
| `article_en_vigueur` | Dire si un article cité (par exemple L441-9) est en vigueur à la date demandée, d'après le dernier relevé daté ; quand l'article change à une date connue (par exemple L102 B, durée de conservation), rendre la version applicable à cette date et annoncer la bascule | Un doute sur la version d'un article de la facture, ou une durée ou une règle qui change bientôt |

Pour les nouvelles mentions de la réforme, il suffit de donner à `facture_verifier` la
taille de l'émetteur (`taille_emetteur`) : il en déduit, à la date de la facture, si elles
sont exigées, et rend leur date d'exigibilité pour cette taille (`exigible_depuis`). Sans
taille, il donne les deux dates. Si `taux_tva` manque sur une ligne, la mention des lignes
reste « à confirmer » et le taux est demandé dans `manquant` : ce n'est pas une facture
invalide, et les montants ne sont pas encore contrôlés. Les mentions se passent en texte, tel qu'il figure sur la facture. Les remises
passent par ligne (`remise_pct` ou `remise_ht`) ou au total (`totaux.remise_ht`) : sans elles,
l'outil signale à tort un écart de calcul.

Chaque outil répond sous la forme unique `resultat` / `regles` / `manquant` / `prudence` /
`garanti`. Le verdict de `facture_verifier` est `a_corriger`, `incomplet` (des faits
manquent) ou `conforme_sur_les_points_controles` : jamais « conforme » tout court, car
l'outil dit aussi ce qu'il ne contrôle pas (taux applicable, continuité de numérotation,
régimes particuliers).

## Quatre usages

| Usage | Attitude | Outils |
| --- | --- | --- |
| Question simple (« faut-il le SIREN du client ? ») | Répondre directement avec la règle et sa source, sans questionnaire | aucun, ou `facture_verifier` sans facture pour lire les règles |
| Objectif précis (« vérifie cette facture ») | Faire passer l'outil tout de suite, restituer d'abord ce qui est à corriger, puis les questions utiles tirées de `manquant` | `facture_verifier` |
| Suivre une méthode (« aide-moi à contrôler mes factures fournisseurs ») | Proposer une des deux méthodes ; la personne choisit le rythme | selon l'étape |
| Explorer (« pourquoi l'indemnité de 40 EUR ? ») | Conversation libre, faits justes et sourcés | outils seulement s'ils aident |

## Sans abonnement (« non garanti »)

Les connaissances, les pièges et les méthodes restent utiles. Les règles datées, les
contrôles exacts et les cas de référence du moteur ne sont pas garantis : le dire, et
indiquer `garanti: non`.

## Documents

Pour un avoir ou une facture rectificative : toujours un **projet à relire**, jamais « prêt
à envoyer ». Il porte son propre numéro, la référence et la date de la facture d'origine,
le motif, et chaque mention reprend sa source. Le faire repasser par `facture_verifier`.

### Annexe : glossaire

# Glossaire

| Terme | Définition courte |
| --- | --- |
| Avoir | Document qui annule ou réduit une facture déjà émise, en y renvoyant. |
| Facture rectificative | Facture qui corrige une facture d'origine et y fait référence. |
| Franchise en base | Régime où le vendeur ne facture pas la TVA ; une mention légale le signale. |
| Autoliquidation | Le client, et non le vendeur, déclare et paie la TVA de l'opération. |
| Indemnité forfaitaire de recouvrement | Somme due par un professionnel qui paie en retard, en plus des pénalités. |
| SIREN | Identifiant à 9 chiffres d'une entreprise ; son dernier chiffre est une clé de contrôle. |
| Numéro de TVA intracommunautaire | En France : FR, une clé de 2 chiffres calculée depuis le SIREN, puis le SIREN. |
| Plateforme agréée | Prestataire immatriculé par l'administration pour transmettre les factures électroniques. |

### Annexe : liens-ressources

# Liens de verification en ligne

Consultation initiale: 2026-07-04. Toujours re-verifier avant rapport client.

## Textes et doctrine

- CGI annexe II art. 242 nonies A:
  https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000050811276
- CGI art. 289:
  https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000048827413
- CGI art. 289 bis:
  https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053546660
- Ordonnance 2021-1190:
  https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000044044176
- BOFiP mentions obligatoires generales:
  https://bofip.impots.gouv.fr/bofip/140-PGP.html/identifiant%3DBOI-TVA-DECLA-30-20-20-10-20131018
- BOFiP mentions particulieres:
  https://bofip.impots.gouv.fr/bofip/1531-PGP.html/identifiant%3DBOI-TVA-DECLA-30-20-20-30-20250108
- BOFiP factures rectificatives et notes d'avoir:
  https://bofip.impots.gouv.fr/bofip/142-PGP.html/identifiant%3DBOI-TVA-DECLA-30-20-20-20-20190925
- Code de commerce L441-9:
  https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000038414397
- Code de commerce D441-5:
  https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000043197457
- Service Public, fiche pratique:
  https://entreprendre.service-public.gouv.fr/vosdroits/F31808

## Verification facturation electronique

- Page impots.gouv facturation electronique:
  https://www.impots.gouv.fr/professionnel/je-passe-la-facturation-electronique
- Liste officielle des plateformes agreees:
  https://www.impots.gouv.fr/je-consulte-la-liste-des-plateformes-agreees
- Plateformes agreees et solutions compatibles:
  https://www.impots.gouv.fr/facturation-electronique-et-plateformes-agreees
- Specifications externes B2B:
  https://www.impots.gouv.fr/specifications-externes-b2b

## Points a verifier avant restitution

- La version en vigueur du CGI art. 289, car la page consultee signale des changements.
- Le perimetre exact de la facturation electronique selon la date et le type de flux.
- Le statut officiel d'une plateforme citee par le client.
- Les mentions TVA specifiques: franchise, autoliquidation, exonération, marge,
  operations intracommunautaires, export et facture rectificative.
- Les mentions et references d'une facture rectificative ou note d'avoir: numero et date
  de la facture initiale, mention du document rectificatif, date et motif.
- Le role de la facture: emise, recue, auto-facturation ou facture etablie par tiers.

### Annexe : methode-controle-avant-envoi

# Méthode : contrôle d'une facture avant envoi ou paiement

Source de la structure : la fiche F31808 d'Entreprendre Service-Public (mentions
obligatoires) et l'article 242 nonies A de l'annexe II du CGI, qui classent les mentions
en générales, conditionnelles et propres aux sociétés. La méthode est la nôtre : elle
suit cet ordre pour que les corrections viennent avant les questions.

1. **Situer la facture.** Émise ou reçue ; client professionnel ou particulier ; vendeur
   société ou entrepreneur individuel ; franchise en base ou non ; TVA autoliquidée ou non ;
   date d'émission (avant ou après l'entrée de l'émetteur dans la facture électronique).
   Ce qu'on ignore, on le laisse inconnu : l'outil le dira.
2. **Faire passer `facture_verifier`.** Il rend ce qui est absent ou invalide, les écarts
   de calcul et les faits à confirmer.
3. **Corriger d'abord.** Une mention absente, un numéro invalide, un écart de calcul.
   Pour une facture déjà envoyée : avoir ou facture rectificative, jamais de retouche.
4. **Confirmer ensuite.** Poser seulement les questions de `manquant` qui changent le
   verdict ; les autres peuvent attendre.
5. **Relire ce que l'outil ne contrôle pas** : taux applicable à l'opération, continuité
   de la numérotation, régimes particuliers.

Approche concurrente : la **revue par l'expert-comptable à la clôture**, qui contrôle
l'ensemble des écritures plutôt que chaque facture. Elle attrape les erreurs de TVA
systématiques mais trop tard pour corriger une facture avant envoi. Les deux se complètent.

Aucune promesse de résultat : la méthode réduit les oublis, elle ne remplace pas la
responsabilité de l'émetteur.

### Annexe : methode-lot-par-sondage

# Méthode : contrôle d'un lot de factures par sondage

Source : la norme d'exercice professionnel NEP 530 « Sélection des éléments à contrôler
et sondages en audit » (homologuée par arrêté, reprise de la norme internationale ISA 530).
Nous en reprenons l'idée, en nos mots, pour un cabinet ou un service comptable qui ne
peut pas relire chaque facture.

1. **Définir le lot** : un client, une période, un sens (émises ou reçues).
2. **Tout contrôler là où le risque est fort** : factures de gros montant, nouveaux
   fournisseurs, avoirs, autoliquidation, factures sans TVA.
3. **Sonder le reste** : un échantillon tiré au hasard ou à intervalle régulier.
4. **Passer chaque facture retenue dans `facture_verifier`** et noter les verdicts.
5. **Extrapoler prudemment** : une erreur répétée sur l'échantillon (par exemple
   l'indemnité de 40 EUR absente) signale un modèle de facture à corriger à la source,
   chez l'émetteur.

Approche concurrente : le **contrôle exhaustif automatisé** (tout passer dans l'outil).
Possible quand les factures arrivent déjà structurées, ce que la réforme de la facture
électronique généralise ; le sondage reste utile pour les pièces papier ou PDF.

La taille de l'échantillon relève du jugement professionnel ; la méthode ne fixe aucun
chiffre.

## Aller plus loin avec OriginSkill

Ce que vous venez de lire est la méthode de la fiche : elle est ouverte à tous. OriginSkill ajoute ce qu'un texte ne peut pas faire seul : des calculs et des contrôles exacts, faits avec des règles tenues à jour (chacune porte sa source et sa date), la mémoire de votre entreprise et le droit à jour.

### Les calculs de cette fiche

Ces calculs sont inclus dans l'abonnement. OriginSkill les fait pour vous, avec des règles à jour et sourcées, et la réponse est garantie.

- **Vérifier qu'un article de loi est toujours en vigueur** (outil `orizon_article_en_vigueur`) : Dit si un article de loi suivi par OriginSkill est en vigueur à la date voulue, d'après le dernier relevé daté du texte officiel.
- **Lire le texte officiel d'un article de loi** (outil `orizon_article_texte`) : Va chercher, au moment de la question, le texte officiel d'un article de loi sur le site de l'État, tel qu'il est en vigueur à la date voulue.
- **Retrouver la fiche d'une entreprise avec son numéro SIREN** (outil `orizon_entreprise_profil`) : Rend ce que les registres publics disent d'une entreprise : nom, forme juridique, activité, effectif, adresse du siège, dirigeants publiés, entreprise en activité ou fermée.
- **Lire les annonces légales d'une entreprise** (outil `orizon_bodacc_annonces`) : Lit les annonces publiées au Bulletin officiel des annonces civiles et commerciales sur une entreprise : procédures collectives, ventes, comptes déposés, modifications.
- **Vérifier un numéro de TVA européen** (outil `orizon_vies_tva`) : Interroge le service de la Commission européenne pour dire si un numéro de TVA intracommunautaire est valide à l'instant de la demande.
- **Connaître le taux de change officiel de la Banque centrale européenne** (outil `orizon_taux_change_bce`) : Donne le taux de change officiel d'une devise contre l'euro (dernier taux publié ou celui d'un jour passé) et convertit un montant.
- **Vérifier une facture mention par mention** (outil `orizon_facture_verifier`) : Contrôle une facture française mention par mention (numéro, dates, vendeur, client, TVA, lignes, totaux, conditions de règlement) et recalcule les montants.

### Avec l'abonnement, en plus

- **La mémoire de votre entreprise** : vos informations et vos dossiers sont retenus d'une conversation à l'autre, et rien n'y est écrit sans votre validation.
- **Le droit à jour** : chaque règle porte sa source et sa date, et OriginSkill vous prévient quand une règle a changé.

### Brancher OriginSkill à votre assistant

Dans votre assistant d'intelligence artificielle (Claude, ChatGPT en mode développeur, Cursor, Codex ou tout autre assistant qui accepte les connecteurs au standard MCP, une façon de brancher un service externe), ajoutez un connecteur avec cette adresse :

    https://api.originskill.ai/mcp

Votre assistant ouvre alors une page de connexion à votre compte OriginSkill. Les étapes détaillées sont ici : https://originskill.ai/installer

### Tarif

Offres et abonnement : https://originskill.ai/tarif

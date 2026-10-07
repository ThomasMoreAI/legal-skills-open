---
name: tva-franchise-ou-reel-fr-originlabs-app
title: Dois-je facturer la TVA, et à partir de quand ?
description: 'Dois-je facturer la TVA, et à partir de quand ?. Méthode professionnelle française, avec ses pièges et ses questions à poser. À utiliser quand : Une création d''entreprise : en franchise ou à la TVA dès le départ, et jusqu''à quel chiffre d''affaires ; Un chiffre d''affaires qui approche ou dépasse 37 500 € (services) ou 85 000 € (ventes) : que se passe-t-il, ; Un micro-entrepreneur qui ne sait pas s''il doit écrire « TVA non applicable » ou facturer 20 %.'
author: originlabs-app
author_url: https://github.com/originlabs-app/origin-skill-install/tree/main/skills/tva-franchise-ou-reel-fr
license: CC-BY-4.0
version: 0.1.0
execution_mode: open
jurisdiction: fr
practice: tax
language: fr
---

> **Version gratuite : règles datées entre le 03/10/2026 et le 04/10/2026.** Les règles changent (SMIC, TVA, seuils…). Avec l'abonnement OriginSkill, votre assistant reçoit la règle à jour, avec sa source et sa date.

# Dois-je facturer la TVA, et à partir de quand ?

Une seule question : est-ce que je facture de la TVA, et à partir de quand ? Tout part de quatre faits :
le chiffre d'affaires de l'an dernier, celui de cette année, sa nature (ventes ou services) et la date de
début d'activité. Le reste (plafond atteint, date de bascule, régime d'après, première déclaration) se calcule.

## Quand l'utiliser

- Une création d'entreprise : en franchise ou à la TVA dès le départ, et jusqu'à quel chiffre d'affaires.
- Un chiffre d'affaires qui approche ou dépasse 37 500 € (services) ou 85 000 € (ventes) : que se passe-t-il,
  et à quelle date la TVA devient-elle due ?
- Un micro-entrepreneur qui ne sait pas s'il doit écrire « TVA non applicable » ou facturer 20 %.
- Un choix à faire : rester en franchise ou opter pour la TVA afin de récupérer celle des investissements.
- Une question précise : « j'ai dépassé le plafond le 18 août, dès quand facturer ? », « mon année de création
  compte-t-elle au prorata ? », « réel simplifié ou réel normal en 2027 ? ».

Quand **ne pas** l'utiliser : calculer ou contrôler une déclaration de TVA (fiche `tva-ca3-fr`) ; contrôler une
facture mention par mention (fiche `facture-conforme-fr`) ; vendre à un client d'un autre pays de l'Union
(fiche `tva-intracom-client-fr`) ; les plafonds de la micro-entreprise pour l'impôt sur le revenu et les
cotisations (régime distinct, voir plus bas) ; le choix du statut juridique.

## Les faits qui décident

Les connaître, sinon donner la réponse pour chaque cas et poser la question de ce qui manque en fin de réponse.

- **Le chiffre d'affaires de l'année précédente**, hors taxes, avec les ventes et les services séparés.
- **Le chiffre d'affaires de l'année en cours** depuis le 1er janvier (ou depuis le début d'activité), séparé de la
  même façon ; s'il est proche d'un plafond, la liste datée des opérations donne la date exacte du franchissement (la règle de la date à retenir pour une opération n'est pas relevée).
- **La date de début d'activité** : elle décide de l'année de création, de l'ajustement de l'année suivante, et
  le chiffre d'affaires d'une année de création se ramène à douze mois.
- **Ventes ou services** : ventes de biens, logement et consommation sur place d'un côté ; autres prestations de
  l'autre. C'est la personne (aidée du modèle) qui classe son activité ; le doute se dit, il ne se tranche pas.
- Utiles ensuite : le régime actuel, une option déjà exercée, la clientèle (professionnels ou particuliers), les
  investissements prévus.

## Connaissances du métier

**La réponse courte.** En 2026, une entreprise est en franchise en base de TVA, c'est-à-dire qu'elle ne
facture pas la TVA et n'en déclare pas, tant que son chiffre d'affaires de l'année précédente n'a pas dépassé
**85 000 €** (vente de biens, logement, consommation sur place) ou **37 500 €** (autres prestations de services), et
que celui de l'année en cours ne dépasse pas **93 500 €** ou **41 250 €** (plafonds majorés). Égal au plafond reste
en franchise. Ces montants sont en vigueur depuis le 01/01/2025 (CGI art. 293 B) ; ils ont été relevés le
30/09/2026 dans des extraits de pages d'impots.gouv.fr, de Service-Public et du BOFiP (version du 01/07/2026),
**pages non ouvertes : non relu en ligne à ce jour**. Le détail daté est dans `seuils-et-etat-des-lieux`.

**Deux plafonds, deux dates de bascule.**

| Situation | Franchise | TVA à facturer |
| --- | --- | --- |
| Plafond de base dépassé l'an dernier | Terminée | Dès le 1er janvier de l'année |
| Plafond de base dépassé cette année, plafond majoré respecté | Continue cette année | Dès le 1er janvier de l'année suivante |
| Plafond majoré dépassé cette année | Terminée | Dès la date du dépassement (lecture de « à compter de la date du dépassement » : l'opération qui fait franchir le plafond est la première taxée) |

La date du dépassement compte depuis le 01/01/2025 : on ne parle plus du « premier jour du mois ». Un exemple
vaut mieux qu'une règle : 30 000 € de services l'an dernier, 39 000 € cette année. Le plafond de base (37 500 €)
est dépassé, pas le plafond majoré (41 250 €) : la franchise continue jusqu'au 31/12/2026 et la TVA se facture
dès le 01/01/2027.

**Ventes et services mêlés.** Il faut tenir les deux conditions : le chiffre d'affaires global sous le plafond des
ventes, et la part de services sous le plafond des services. 40 000 € de ventes et 40 000 € de services font
80 000 € au global (sous 85 000 €) mais 40 000 € de services (au-dessus de 37 500 €) : la franchise cesse.

**L'année de création et l'année suivante.** L'année où l'activité commence, la franchise joue de plein droit, sans
ajustement, tant que le plafond majoré n'est pas dépassé. L'année suivante, le chiffre d'affaires de l'année de
création est ramené à douze mois (multiplié par 365 et divisé par le nombre de jours d'activité) avant d'être
comparé aux plafonds de base. Exemple du BOFiP : début le 12 juin, 65 000 € sur 203 jours donnent 116 872 € ramenés
à l'année : TVA dès le 1er janvier suivant. Piège : 25 000 € de services après un début le 12 juin sont sous
37 500 €, mais ramenés à l'année ils font 44 950,74 €. Pas d'ajustement pour une activité saisonnière ou
intermittente. Le tableau des plafonds équivalents pour l'année de création est rendu par l'outil, et le chiffre d'affaires prévu pour toute l'année (au 31 décembre) en tire le verdict de l'an prochain : 34 300 € de services après un début le
4 mars 2026 (303 jours) font 34 300 × 365 / 303 = 41 318,48 € ramenés à douze mois, au-dessus de 37 500 € : la franchise cesse au 1er janvier 2027 ;
26 800 € en font 32 283,83 et la franchise tient.

**Un zéro n'est pas « je ne sais pas ».** Sans le chiffre d'affaires de l'année précédente ni la date de début d'activité, l'outil ne lit rien et pose
la question ; avec un chiffre d'affaires de l'année précédente donné à 0 sans date de début, il pose la question décisive (début d'activité cette année, ou chiffre non
donné) et rend sa réponse sous réserve : une activité déjà en cours l'an dernier au-dessus de 37 500 € ou 85 000 € a perdu la franchise au 1er janvier.

**La TVA à rattraper après la sortie.** Quand la franchise a cessé et que les montants sont donnés (factures émises sans TVA, ou opérations en cours datées avec
leur taux de TVA, ou le chiffre d'affaires de l'année quand la bascule est au 1er janvier), l'outil chiffre la TVA due depuis la date de bascule, par taux (20, 10,
5,5 ou 2,1 %), dans deux lectures qu'il ne choisit pas : ajoutée au prix (montant HT × taux, clients professionnels qui la récupèrent) ou prélevée sur le prix
déjà payé (prix × taux / (1 + taux), particuliers à prix inchangé). 43 000 € à 10 % et 29 500 € à 20 % : 10 200 € dans la première lecture, 8 825,76 € dans la
seconde. Sans taux, 20 % est retenu, dit, et la question est posée. Les factures rectificatives, les intérêts de retard et la récupération auprès des
clients ne sont pas chiffrés (sources non relues en ligne : réponse non garantie).

**Franchise en base et micro-entreprise : deux choses.** Le plafond de TVA est distinct du plafond de la
micro-entreprise (impôt sur le revenu et cotisations) : dépasser la franchise ne fait pas sortir du statut de
micro-entrepreneur (impots.gouv.fr, extrait du 30/09/2026, non relu en ligne à ce jour).

**Ce que la franchise change concrètement.** Les factures portent la mention « TVA non applicable, art. 293 B du
CGI » (version de l'article 293 B en vigueur depuis le 01/03/2025, relevée sur Légifrance le 20/07/2026). L'entreprise ne dépose pas de
déclaration de TVA et ne peut déduire aucune TVA sur ses achats ni sur ses investissements. Cela ne gêne guère
une clientèle de particuliers, qui ne récupèrent pas la TVA ; cela pèse sur une clientèle de professionnels, qui
ne peuvent pas récupérer de TVA sur vos factures.

**Après la franchise : simplifié ou normal.** Jusqu'au 31/12/2026, le régime simplifié (une déclaration annuelle,
la CA12, avec deux acomptes) s'applique de plein droit entre les plafonds de la franchise et 840 000 € (ventes) ou
254 000 € (services), si la TVA exigible est inférieure à 15 000 € ; au-delà, le réel normal (CA3, mensuelle sauf
TVA exigible annuelle inférieure à 4 000 €). **Le régime simplifié de TVA est supprimé à compter du 01/01/2027** (loi de finances pour 2025, art. 38) :
toute entreprise hors franchise est alors au réel normal, avec une CA3 trimestrielle (sauf option pour la mensuelle)
quand le chiffre d'affaires de l'année précédente majoré des acquisitions taxables n'excède pas 1 000 000 €, et une
CA3 mensuelle au-delà. Tant que le chiffre d'affaires de l'année en cours n'est pas final, la périodicité reste à
confirmer : l'outil rend alors les deux issues (mensuelle et trimestrielle) avec leurs fenêtres de dépôt. Ne pas confondre avec le réel simplifié des bénéfices (liasse 2033), qui a ses propres plafonds.

**L'option pour la TVA.** Une entreprise qui respecte les plafonds peut renoncer à la franchise en optant pour le
paiement de la TVA (CGI art. 293 F) : effet au premier jour du mois de la demande, engagement de deux années
civiles dont celle de la demande, reconduction tacite sauf dénonciation. Intérêt : récupérer la TVA sur les
achats et les investissements. Coût : facturer la TVA. Avec des clients professionnels, la TVA s'ajoute au prix
hors taxes sans rien leur coûter, l'option est souvent favorable ; avec des particuliers, à prix payé inchangé, la
TVA (un sixième du prix à 20 %) est prélevée sur la marge. L'outil chiffre les deux cas ; le choix reste à la personne.

**État incertain, dit sans être tranché.**

- *Le plafond unique de 25 000 €* voté par la loi de finances pour 2025 est supprimé par la loi n° 2025-1044 du
  03/11/2025 : les plafonds ci-dessus sont maintenus. Un article ou une vidéo qui parle encore de 25 000 € est périmé.
- *Un projet de loi de finances pour 2027* est annoncé pour la fin septembre 2026 (source secondaire) ; son contenu sur la
  franchise n'est pas connu. Revérifier les plafonds après son dépôt.
- *La recodification de la TVA au code des impositions sur les biens et services (CIBS)* renumérote l'article
  293 B à droit constant. Elle entre en vigueur le 01/01/2027, et non le 01/09/2026 : l'ordonnance n° 2026-671 du
  27/07/2026 (art. 17, texte lu le 03/10/2026) a reporté la date. Jusqu'au 31/12/2026, l'article 293 B du CGI
  s'applique ; les anciennes références du CGI restent admises jusqu'au 30/06/2028. Le CIBS consolidé au 01/01/2027
  (lu le 04/10/2026) reprend la franchise aux articles L. 233-3 (entreprise franchisée), L. 233-9 et L. 233-10
  (plafonds, mêmes montants que l'article 293 B). La mention à écrire sur les factures à compter du 01/01/2027 n'est
  fixée par aucun texte lu : la DGFiP (pages modifiées en mai et en juin 2026) cite « art. 293 B du CGI » ou
  « article L.223-3 du CIBS », numéro d'avant l'ordonnance n° 2026-671 (L. 233-3 dans le texte consolidé). Garder la
  mention « art. 293 B du CGI » relevée et la vérifier avant d'éditer un modèle de facture à compter du 01/01/2027.

**Les faits de mémoire que cette fiche lit et propose** (mêmes noms que la mémoire d'entreprise) :

| Fait | Valeurs | Rôle |
| --- | --- | --- |
| `regime_tva` | `franchise`, `reel_simplifie`, `reel_normal` | Lu : la situation déclarée (un écart avec le calcul est signalé). Proposé : le régime calculé, avec l'accord de la personne |
| `periodicite_tva` | `mensuelle`, `trimestrielle`, `annuelle` | Proposé après une bascule, quand elle est décidée |
| `activite` | texte libre | Lu par le modèle pour classer ventes ou services ; aucun effet sur le calcul |
| `forme_juridique`, `date_cloture_exercice`, `siren` | selon la mémoire | Contexte : la franchise vaut pour toutes les formes ; un exercice qui n'est pas l'année civile change les dates de la CA12 |

Le chiffre d'affaires ne fait pas partie de la liste fermée de la mémoire : il se lit dans la conversation ou
se redonne. Le mini-réel (option du simplifié pour la TVA au réel normal) n'a pas de valeur dans la mémoire.

## Pièges fréquents

- **Confondre franchise en base et micro-entreprise.** Deux plafonds, deux régimes ; on peut être micro-entrepreneur
  et facturer la TVA.
- **Croire que dépasser 37 500 € fait facturer la TVA tout de suite.** Entre 37 500 € et 41 250 €, la franchise
  continue jusqu'au 31 décembre ; la TVA commence le 1er janvier.
- **Croire qu'on a jusqu'au mois suivant, ou jusqu'au 1er janvier, quand le plafond majoré est franchi.** La TVA est
  due dès l'opération du dépassement ; les factures déjà émises sans TVA à partir de cette date sont à rectifier.
- **Oublier le prorata de l'année qui suit la création.** Un bon démarrage en fin d'année peut faire perdre la
  franchise au 1er janvier, même sous le plafond brut.
- **Tenir un seul plafond pour une activité mixte.** Il y en a deux, et le plus bas l'emporte en cas de doute.
- **Laisser son prix TTC inchangé quand la TVA arrive.** À 20 %, un sixième du prix part en TVA : 1 200 € TTC font
  1 000 € hors taxes.
- **Facturer de la TVA en franchise, ou oublier la mention.** En franchise, pas de TVA sur la facture et la mention
  de l'article 293 B ; hors franchise, le taux, le montant de TVA, le total TTC et le numéro de TVA.
- **Oublier d'informer le service des impôts des entreprises et de demander le numéro de TVA intracommunautaire**,
  nécessaire pour facturer la TVA.
- **Opter sans mesurer l'engagement.** Deux années civiles au moins ; la clientèle de particuliers peut rendre
  l'option coûteuse.
- **Reprendre un plafond lu sur un vieux site.** 25 000 € est supprimé ; tout chiffre d'avant 2025 est périmé.
- **Classer à la légère une activité mixte ou atypique.** Les cas d'exclusion et les régimes particuliers (avocats,
  auteurs et artistes, outre-mer) ne sont pas relevés ici : les dire et les faire vérifier.

## Méthodes proposées (jamais imposées)

1. **Faire le point en quatre questions** : chiffre d'affaires de l'an dernier, de cette année, nature de
   l'activité, début d'activité ; puis le verdict, la date de bascule et la suite. Détails :
   `methode-faire-le-point`.
2. **Suivre son plafond mois après mois** : un cumul par nature à chaque fin de mois, la marge restante avant les deux
   plafonds, et le moment où préparer la bascule (numéro de TVA, modèle de facture, prix). Détails :
   `methode-suivre-le-plafond`.

Elles ne se valent pas toujours : la première répond à une question du moment, la seconde évite la surprise d'un
dépassement en cours d'année. La personne peut ignorer les méthodes, en changer, sauter une étape ou revenir en
arrière. Exemples chiffrés : `exemples-calcules`. Ce qu'il faut faire à la sortie de la franchise et
l'option : `sortie-de-la-franchise-et-option`. Vocabulaire : `glossaire`.

## Contrat de réponse (3 règles fixes)

1. Toute règle ou tout chiffre affirmé vient avec sa **source datée** : les plafonds avec leur date d'effet et
   leur état de relevé (« non relu en ligne à ce jour », recherche du 30/09/2026) ; l'article 293 B du CGI pour la
   franchise, l'article 293 F pour l'option.
2. **Ne jamais inventer** : dire ce qui manque (chiffre d'affaires, date du dépassement, nature de l'activité) et ce
   qui n'est pas relevé (cas d'exclusion, outre-mer, exercice décalé, mention de facture à compter du 01/01/2027).
3. **Prévenir** quand une règle vient de changer ou reste incertaine (champ `prudence` : plafond unique supprimé,
   régime simplifié supprimé en 2027, recodification au CIBS, projet de loi de finances pour 2027).

« Plan d'action d'abord », « deux questions au maximum » et l'ordre des étapes sont de bonnes habitudes quand la
personne veut agir, pas des obligations.

**Restitution au dirigeant.**

1. Répondre d'abord, exactement, à la question posée et à rien d'autre : la règle ou le chiffre en une ou deux phrases, puis ce qui sert à cette question. Pas de tableau complet, pas de volet non demandé, aucun chiffre d'exemple inventé. Reprendre tels quels les chiffres de `en_clair.resultats`, sans les recalculer ; ne jamais affirmer qu'un point non fourni par le dirigeant est en règle.
2. Si un fait manque et change la réponse, donner la réponse pour chaque cas, puis poser une seule question à la fin : celle qui débloque. Aucune question si rien ne manque.
3. Parler en mots du dirigeant : jamais « l'outil », « le moteur », « le serveur », ni un code ou un champ technique (`entree_incomplete`, `manquant`, `prudence`) ; ne jamais recopier le mot « garanti » ni « non garanti ». Traduire : « il me manque la date d'embauche pour calculer… », « règle relevée le JJ/MM/AAAA, texte officiel pas encore relu ; à reconfirmer avant d'agir ». Écrire « vérifiée » seulement pour une règle marquée vérifiée (« règle vérifiée le JJ/MM/AAAA ; à reconfirmer avant d'agir si l'enjeu est important ») : une source citée n'est pas une vérification.
4. Une échéance qui tombe un samedi, un dimanche ou un jour férié se dit avec son report si les règles en donnent un, sinon « à vérifier ».
5. Ne jamais inventer un fait absent, ni pour appeler un outil. Une règle datée fournie par OriginSkill n'est jamais remplacée par une source secondaire trouvée en ligne ; en cas d'écart, donner les deux valeurs, leurs sources et leurs dates.

## Outils (description ouverte)

L'exécution exacte est servie par le connecteur.

| Outil | Sert à | Appeler quand |
| --- | --- | --- |
| `tva_franchise_regime` (nom servi : `orizon_tva_franchise_regime`) | À partir du chiffre d'affaires de l'année précédente et de l'année en cours par nature : franchise ou non (plafonds de base et majorés, activité mixte, année de création et prorata), date de bascule (immédiate ou au 1er janvier, date exacte d'un franchissement à partir d'une liste d'opérations), régime d'après (simplifié jusqu'au 31/12/2026, réel normal ensuite, périodicité), dès quand facturer la TVA, mention à retirer et mentions à ajouter, première déclaration et sa date, intérêt chiffré de l'option | Dès qu'il y a un chiffre d'affaires ou une date de début d'activité à examiner |

Entrées : `ca_n_moins_1` et `ca_en_cours` (objets `ventes` et `services`, en euros hors taxes, les deux clés à donner, 0 s'il n'y en a pas : une clé absente
n'est jamais lue comme 0, le chiffre est refusé et la question est posée), ou `operations_en_cours` (liste de `date`, `montant_ht`, `nature`, `taux_tva` facultatif) ; `date_debut_activite`,
`activite_saisonniere`, `date_depassement`, `date_reference` (défaut : aujourd'hui) ; `regime_tva`, `option_tva_depuis` (date passée : option en cours ; date à venir : option envisagée, effet et engagement comptés depuis cette date),
`tva_exigible_n_moins_1`, `acquisitions_taxables_n_moins_1`, `ca_annuel_previsionnel` (un objet `{"ventes": nombre, "services": nombre}`, les deux clés, 0 s'il n'y en a pas : un nombre seul est refusé),
`ca_fin_d_annee_prevu` (même forme : le total prévu de l'année en cours au 31 décembre, ramené à douze mois l'année de création), `factures_sans_tva` (liste de `montant_ht` et `taux_tva` : la TVA à rattraper) ; pour l'option,
`investissements_ht`, `achats_ht_annuels`, `taux_tva`, `clientele`. `cas_particulier` (liste parmi `exclusion_293b`, `avocat`, `auteur_artiste`,
`outre_mer`, `exercice_non_civil`) : à poser dès que l'activité est dans l'un de ces cas, que l'outil ne calcule pas ; il rend alors le calcul de droit
commun sous une réserve écrite en tête de la réponse, sans le présenter comme une conclusion, et n'est pas garanti. Sans cette entrée, `resultat.cas_particuliers_a_verifier`
porte la question à poser avant de conclure. `activite` (fait de mémoire) est accepté et sans
effet. Une entrée non comprise est dite dans `manquant`, jamais ignorée en silence.

Lire la réponse : `resultat.reponse` porte la synthèse ; `franchise`, `bascule` (type, date, plafond dépassé),
`regime` (à la date du relevé, et après la bascule), `consequences`, `option_volontaire`, `faits_a_proposer_a_la_memoire`,
`projection_fin_d_annee`, `tva_due_depuis_la_bascule`, `question_decisive` et `questions` ; `reserve_cas_particulier` ou `cas_particuliers_a_verifier` ; `manquant` devient la question à poser ; `prudence` se dit une fois. Chaque appel
répond sous la forme unique `resultat` / `regles` / `manquant` / `prudence` / `garanti`.

Autres outils utiles après une bascule : `tva_ca3` (calculer la CA3 du mois), `facture_verifier` (contrôler la mention
et les totaux d'une facture), `calendrier_obligations` (les échéances), `article_texte` (lire l'article 293 B ou son
remplaçant au CIBS à la date du jour).

L'outil calcule des plafonds, des dates et des montants ; il ne classe pas l'activité, ne décide pas d'opter et ne dépose
rien. Le choix reste à la personne.

## Quatre usages

| Usage | Attitude | Outils |
| --- | --- | --- |
| Question simple (« à partir de combien de chiffre d'affaires facture-t-on la TVA ? ») | Répondre avec les deux plafonds, leur date et leur état de relevé, la règle du 1er janvier et celle de la date du dépassement ; ajouter la question qui change la réponse | aucun, ou `tva_franchise_regime` si un chiffre est donné |
| Objectif précis (« j'ai fait 39 000 € de services, que se passe-t-il ? ») | Appeler l'outil tout de suite, rendre le verdict et la date, puis les conséquences | `tva_franchise_regime` |
| Suivre une méthode (« guide-moi pour ne pas me faire surprendre ») | Proposer l'une des deux méthodes ; la personne choisit le rythme | `tva_franchise_regime` à chaque point |
| Explorer (« franchise ou option, qu'est-ce qui m'arrange ? ») | Conversation libre, avantages et coûts côte à côte, sans trancher à sa place | l'outil avec les montants de la personne |

## Sans abonnement (« non garanti »)

Les connaissances, les pièges, les méthodes et les exemples restent utiles. Les plafonds servis, les dates
calculées et les cas de référence ne sont pas garantis : le dire, et indiquer `garanti: non`. Les sources des
plafonds étant encore non relues en ligne, la réponse reste non garantie même pour un abonné tant qu'elles ne sont
pas relues ; le dire sans dramatiser.

## Documents

Aucun document n'est produit. Une facture, un courrier au service des impôts ou une demande d'option rédigés par le
modèle de la personne sont un **projet à relire**, jamais « prêt à envoyer ». Le libellé de la mention vient des
règles relevées, pas de la mémoire du modèle.

## Ce qui n'est pas relevé

Les cas où la franchise est exclue par l'article 293 B ; les franchises propres aux avocats, aux auteurs et aux
artistes (BOFiP BOI-TVA-DECLA-40-20 et 40-30) ; l'outre-mer ; un exercice qui n'est pas l'année civile ;
les modalités exactes des factures rectificatives, des intérêts de retard et de la régularisation de la TVA sur des stocks ou des
immobilisations acquis en franchise ; les acomptes du régime simplifié ; le choix entre simplifié et normal d'une
entreprise sans chiffre d'affaires de référence ; le traitement d'une option pour un assujetti sous les plafonds ;
la mention de facture à compter du 01/01/2027. Pour chacun, le dire et orienter vers la source officielle ou le service des impôts
des entreprises.

### Annexe : exemples-calcules

# Exemples calculés

Chiffres hors taxes. Plafonds de 2026 : base 85 000 € (ventes) et 37 500 € (services), majorés 93 500 € et 41 250 €,
relevés le 30/09/2026 (extraits de pages officielles, non relu en ligne à ce jour). Dates calculées avec le calendrier
des jours fériés ; les montants viennent de l'outil et sont rejoués à chaque vérification de la fiche.

## 1. Entre le plafond de base et le plafond majoré

30 000 € de services en 2025, 39 000 € en 2026. 39 000 € dépasse 37 500 € sans atteindre 41 250 € : la franchise
continue jusqu'au 31/12/2026, la TVA se facture à partir du 01/01/2027. Comme le régime simplifié n'existe plus à cette
date, l'entreprise est au réel normal : CA3. La périodicité n'est pas décidée avant la fin de l'année (le chiffre d'affaires de
2026 n'est pas final) : mensuelle, première période janvier 2027, dépôt entre le 15 et le 24 février 2027 ; ou
trimestrielle (sauf option contraire sous 1 000 000 €), premier trimestre 2027, dépôt entre le 15 et le 24 avril 2027 (le jour
exact est dans l'espace professionnel). Il reste 2 250 € HT à facturer avant le plafond majoré (41 250 € - 39 000 €).

## 2. Le plafond majoré franchi en cours d'année

30 000 € de services en 2025. En 2026, trois opérations : 20 000 € le 10/02, 18 000 € le 12/05, 4 000 € le 03/07.
Le cumul passe à 38 000 € le 12/05 (plafond de base franchi : la franchise aurait cessé au 01/01/2027) puis à 42 000 € le
03/07, au-dessus de 41 250 € : la franchise cesse le vendredi 3 juillet 2026, et la TVA est due pour cette opération
et les suivantes. Régime : simplifié en 2026 (30 000 € est sous 254 000 €) ; première déclaration : CA12 du 03/07/2026
au 31/12/2026, à déposer le mardi 4 mai 2027 (1er mai 2027 samedi : lundi 3 mai premier jour ouvré, mardi 4 mai
deuxième). Ensuite CA3 dès janvier 2027.

## 3. L'exemple du BOFiP : une année de création

Début d'activité le 12 juin 2026 : 203 jours jusqu'au 31/12 (19 + 31 + 31 + 30 + 31 + 30 + 31). 65 000 € de ventes
au 31/12/2026. La première année, la franchise joue de plein droit (65 000 € est sous 93 500 €). Pour 2027 :
65 000 × 365 / 203 = 116 871,92 € ramenés à l'année, au-dessus de 85 000 € : TVA dès le 01/01/2027.
Le plafond équivalent à ne pas dépasser en 2026 pour rester en franchise en 2027 est 85 000 × 203 / 365 = 47 273,97 €
pour des ventes et 37 500 × 203 / 365 = 20 856,16 € pour des services.

## 4. Le piège de la création en cours d'année

Même début le 12 juin 2026, 25 000 € de services au 31/12/2026. 25 000 € est sous 37 500 €, mais
25 000 × 365 / 203 = 44 950,74 € ramenés à l'année dépasse 37 500 € : TVA dès le 01/01/2027. Avec une activité
saisonnière, pas d'ajustement : la franchise continue.

## 5. Ventes et services mêlés

40 000 € de ventes et 40 000 € de services en 2025. Le global (80 000 €) est sous 85 000 €, mais les services
(40 000 €) dépassent 37 500 € : la franchise a cessé le 01/01/2026. Avec 50 000 € de ventes et 30 000 € de services,
les deux conditions tiennent (80 000 € et 30 000 €) : la franchise continue.

## 6. L'option pour la TVA, deux clientèles

10 000 € d'investissements et 2 000 € d'achats par an, TVA à 20 % : 2 000 € récupérables une fois sur
l'investissement, 400 € par an sur les achats.
- Clientèle de professionnels : la TVA facturée s'ajoute au prix hors taxes, rien à reverser sur la marge ; solde
  indicatif de la première année : +2 400 €.
- Clientèle de particuliers avec 30 000 € de chiffre d'affaires prévu : à prix payé inchangé, 30 000 × 20 / 120 =
  5 000 € de TVA à reverser par an ; solde indicatif de la première année : 2 400 − 5 000 = −2 600 €. L'option coûte
  cher ici, sauf à augmenter les prix.
L'option prend effet au premier jour du mois de la demande et engage deux années civiles : demandée le 30/09/2026,
elle court du 01/09/2026 au moins jusqu'au 31/12/2027.

## 7. Un relevé en 2027

50 000 € de services en 2026, relevé du 10/03/2027 : la franchise a cessé le 01/01/2027 (50 000 € dépasse 37 500 €),
le régime simplifié n'existe plus, donc réel normal ; 50 000 € n'excède pas 1 000 000 € : CA3 trimestrielle sauf option
pour la mensuelle, première période le premier trimestre 2027, dépôt entre le 15 et le 24 avril 2027.

## 8. Prévoir l'an prochain l'année de la création

Activité commencée le 4 mars 2026 (303 jours jusqu'au 31 décembre), 26 800 € de services facturés et 7 500 € de missions prévues : 34 300 € au 31/12/2026. Ramené à douze mois, 34 300 × 365 / 303 = 41 318,48 €, au-dessus de 37 500 € : la franchise cesse au 1er janvier 2027. Sans les 7 500 € décalés, 26 800 × 365 / 303 = 32 283,83 € : la franchise tient, avec 4 330,14 € de marge sur le plafond équivalent (31 130,14 €).

## 9. La TVA à rattraper après la sortie

Franchise cessée au 01/01/2026, 43 000 € de ventes à 10 % et 29 500 € de prestations à 20 % facturés sans TVA : TVA ajoutée au prix 4 300 + 5 900 = 10 200 € ; prélevée sur le prix payé 43 000 / 11 + 29 500 / 6 = 3 909,09 + 4 916,67 = 8 825,76 €. Les deux lectures sont rendues, la personne et le service des impôts tranchent ; sans taux donné, 20 % est retenu, dit, et la question est posée.

### Annexe : glossaire

# Glossaire

| Terme | Définition courte |
| --- | --- |
| Franchise en base de TVA | Régime où l'entreprise ne facture pas la TVA, n'en déclare pas et n'en déduit pas (CGI art. 293 B). |
| Plafond de base | Chiffre d'affaires de l'année précédente à ne pas dépasser pour rester en franchise : 85 000 € (ventes) ou 37 500 € (services), égal compris. |
| Plafond majoré | Chiffre d'affaires de l'année en cours à ne pas dépasser : 93 500 € (ventes) ou 41 250 € (services). |
| Date du dépassement | Date de l'opération qui fait franchir le plafond majoré ; la TVA est due à compter de cette date. |
| Ventes | Ventes de biens, fourniture de logement et ventes à consommer sur place. |
| Services | Autres prestations de services. |
| Activité mixte | Ventes et services ensemble : le global reste sous le plafond des ventes et la part de services sous le plafond des services. |
| Année de création | Année où l'activité commence : franchise de plein droit sans ajustement tant que le plafond majoré n'est pas dépassé. |
| Prorata sur 365 jours | Ajustement du chiffre d'affaires de l'année de création à douze mois : multiplié par 365, divisé par le nombre de jours d'activité. |
| Réel simplifié de TVA | Régime d'une déclaration annuelle (CA12) avec deux acomptes, jusqu'au 31/12/2026 ; supprimé au 01/01/2027. À ne pas confondre avec le réel simplifié des bénéfices. |
| Réel normal | Régime de la déclaration mensuelle ou trimestrielle (CA3). |
| Mini-réel | Bénéfices au réel simplifié, TVA au réel normal par option. |
| CA12 | Déclaration annuelle de régularisation du régime simplifié de TVA. |
| CA3 | Déclaration mensuelle ou trimestrielle de TVA du réel normal. |
| Option pour le paiement de la TVA | Renonciation à la franchise : effet le premier jour du mois de la demande, engagement de deux années civiles (CGI art. 293 F). |
| Numéro de TVA intracommunautaire | Numéro nécessaire pour facturer la TVA. |
| SIE | Service des impôts des entreprises, à informer de la sortie de la franchise. |
| CIBS | Code des impositions sur les biens et services, où la TVA sera recodifiée à compter du 01/01/2027 (report du 01/09/2026 par l'ordonnance n° 2026-671) ; la franchise y est reprise aux articles L. 233-3, L. 233-9 et L. 233-10 (lus le 04/10/2026) ; la mention de facture à compter du 01/01/2027 n'est fixée par aucun texte lu. |
| Micro-entreprise | Régime de l'impôt sur le revenu et des cotisations, avec ses propres plafonds ; distinct de la franchise de TVA. |
| Ramené à douze mois | CA prévu de l'année de création × 365 / jours d'activité, comparé au plafond de base : dit si la franchise tient l'an prochain. |
| TVA à rattraper | TVA due depuis la date de bascule sur des factures émises sans TVA : ajoutée au prix (HT × taux) ou prélevée sur le prix payé (prix × taux / (1 + taux)) ; deux lectures, aucune choisie par l'outil. |

### Annexe : methode-faire-le-point

# Méthode : faire le point en quatre questions

Pour répondre à « est-ce que je facture de la TVA, et à partir de quand ? » sans formulaire : quatre questions, dans
cet ordre, puis un verdict daté. La personne peut sauter une étape ou répondre par bribes ; ce qui manque se dit à la fin.

## 1. Le chiffre d'affaires de l'an dernier

Hors taxes, ventes et services séparés. S'il est inconnu parce que l'activité a commencé cette année, passer à la
question 3. Si l'activité a commencé en cours d'année dernière, demander la date : le chiffre d'affaires est alors
ramené à douze mois avant d'être comparé (multiplié par 365, divisé par les jours d'activité).

## 2. Le chiffre d'affaires de cette année

Depuis le 1er janvier ou depuis le début d'activité. S'il est proche d'un plafond, demander les opérations datées
(date, montant hors taxes, ventes ou services) : la date exacte du franchissement en découle, et c'est elle qui
décide du premier jour de TVA quand le plafond majoré est dépassé.

## 3. La nature et le début d'activité

Ventes (biens, logement, consommation sur place) ou services ; les deux ensemble si l'activité est mixte. Le
modèle de la personne classe l'activité à partir de ce qu'elle vend ; un cas douteux se dit, et le plafond le plus bas
est celui qui protège. La date de début d'activité sert à l'année de création.

## 4. Le verdict et la suite

Appeler l'outil, puis rendre dans cet ordre :

1. la réponse en une phrase (en franchise ou non, et jusqu'à quand) ;
2. la date de bascule et sa raison (plafond de base dépassé l'an dernier, plafond majoré dépassé à telle date, plafond
   de base dépassé cette année) ;
3. le régime d'après : simplifié jusqu'au 31/12/2026, réel normal ensuite ;
4. les conséquences : dès quand facturer la TVA, ce qui change sur la facture, la première déclaration ;
5. l'option pour la TVA, si la franchise est encore possible et que la personne a des investissements ;
6. ce qui manque et la question qui change la réponse.

## Garde-fous

- Ne jamais classer l'activité à la place de la personne ; proposer et laisser confirmer.
- Ne jamais annoncer un plafond sans sa date et son état de relevé (non relu en ligne à ce jour).
- Une réponse utile d'abord, les questions ensuite : la franchise peut se décrire pour chaque cas avant de connaître
  les chiffres.

### Annexe : methode-suivre-le-plafond

# Méthode : suivre son plafond mois après mois

Pour ne pas découvrir le dépassement en décembre, ni après un mois de factures sans TVA. Un point rapide à la fin de
chaque mois, à la cadence que la personne choisit.

## Chaque fin de mois

1. Reporter le cumul depuis le 1er janvier (ou depuis le début d'activité), **par nature** : ventes d'un côté, services de
   l'autre. Une liste des factures avec leur date fait l'affaire.
2. Appeler l'outil avec ce cumul (ou avec la liste datée des opérations). Il rend la marge restante avant le plafond de
   base et avant le plafond majoré, en distinguant le plafond global et le plafond des services.
3. Lire l'état :
   - **loin des plafonds** : rien à faire, prochain point le mois suivant ;
   - **au-dessus du plafond de base, sous le plafond majoré** : la franchise continue cette année, la TVA commence au
     1er janvier ; préparer la bascule (étape suivante) sans attendre ;
   - **au-dessus du plafond majoré** : la TVA est due dès l'opération du dépassement ; agir le jour même.

## Préparer la bascule

À faire avant le premier jour de TVA, dans l'ordre :

- demander le numéro de TVA intracommunautaire et informer le service des impôts des entreprises (espace professionnel
  impots.gouv.fr) ;
- changer le modèle de facture : retirer « TVA non applicable, art. 293 B du CGI », afficher le taux, le montant de TVA
  par taux, le total TTC et le numéro de TVA ;
- décider des prix : garder le prix payé (la TVA prélève alors un sixième du prix à 20 %) ou augmenter ;
- repérer la première déclaration (régime simplifié jusqu'au 31/12/2026, réel normal ensuite) et sa date ;
- lister les achats et les investissements dont la TVA deviendra déductible.

## Ce que la méthode ne fait pas

Elle ne choisit pas le seuil d'alerte (à la personne : un mois avant ? à la moitié de la marge ?). Elle ne remplace
ni le suivi comptable ni l'avis d'un expert-comptable quand l'activité est atypique. Elle ne présume pas de la date
d'une opération (livraison, encaissement) : la règle exacte n'est pas relevée ici, la dire.

### Annexe : seuils-et-etat-des-lieux

# Plafonds, dates et état des lieux (relevé du 30/09/2026)

## Comment ces chiffres ont été relevés

Le 30/09/2026, l'accès aux pages officielles était refusé depuis l'environnement de travail. Aucune page n'a donc
été lue en entier : chaque valeur vient d'un **résultat de recherche restreint aux sites officiels** (l'adresse exacte
de la page et un extrait qui énonce la valeur). Les pages sont marquées **« non relu en ligne à ce jour »** et la
date de la recherche est celle du 30/09/2026 : ce n'est pas une date de consultation de la page. La relecture en
pleine page reste à faire. Jusque-là, tout chiffre de ce tableau est à reconfirmer avant une décision importante.

## Les valeurs en vigueur

| Valeur | Montant | En vigueur depuis | Page (extrait de recherche du 30/09/2026) | État du relevé |
| --- | --- | --- | --- | --- |
| Plafond de base, ventes, logement, consommation sur place (chiffre d'affaires de l'année précédente) | 85 000 € | 01/01/2025 | Service-Public Entreprendre, fiche F21746 ; BOFiP BOI-TVA-DECLA-40-10-10 (version du 01/07/2026) | non relu en ligne à ce jour |
| Plafond de base, autres prestations de services | 37 500 € | 01/01/2025 | idem | non relu en ligne à ce jour |
| Plafond majoré, ventes et logement (année en cours) | 93 500 € | 01/01/2025 | impots.gouv.fr, « Les régimes d'imposition à la TVA » (page mise à jour le 21/05/2026) | non relu en ligne à ce jour |
| Plafond majoré, services | 41 250 € | 01/01/2025 | idem | non relu en ligne à ce jour |
| Fin de la franchise à la date du dépassement du plafond majoré (et non plus au premier jour du mois) | date du dépassement | 01/01/2025 | impots.gouv.fr, « En tant que micro-entrepreneur, puis-je être redevable de la TVA ? » | non relu en ligne à ce jour |
| Plafond de base dépassé sans dépasser le plafond majoré : franchise jusqu'au 31/12, TVA au 01/01 suivant | 1er janvier | sans date relevée | Service-Public Entreprendre, fiche F21746 | non relu en ligne à ce jour |
| Mention de facture en franchise | « TVA non applicable, art. 293 B du CGI » | version en vigueur depuis le 01/03/2025 | Légifrance, CGI art. 293 B (identifiant LEGIARTI000052488142), relevé Légifrance du 20/07/2026 | relevé daté, plus ancien que 30 jours |
| Régime simplifié de TVA : CA sous 840 000 € (ventes) ou 254 000 € (services), TVA exigible inférieure à 15 000 € | 840 000 € / 254 000 € / 15 000 € | sans date relevée ; jusqu'au 31/12/2026 | impots.gouv.fr, « Les régimes d'imposition à la TVA » | non relu en ligne à ce jour |
| Suppression du régime simplifié de TVA | 01/01/2027 | 01/01/2027 | Légifrance, loi n° 2025-127 du 14/02/2025, art. 38 ; impots.gouv.fr, actualité du 22/09/2026 | art. 38 lu le 03/10 et le 04/10/2026 ; actualité lue le 04/10/2026 |
| Dès 2027, CA3 trimestrielle : CA de l'année précédente plus acquisitions taxables au plus 1 000 000 € | 1 000 000 € (et 1 100 000 € l'année en cours) | 01/01/2027 | Légifrance, CGI art. 287, 3, version du 01/01/2027 ; impots.gouv.fr, actualité du 22/09/2026 | lus le 04/10/2026 (preuve `docs/sources/relectures/2026-10-04-bascules-2`) |
| Option pour le paiement de la TVA : effet le premier jour du mois, deux années civiles, reconduction tacite | 2 années civiles | sans date relevée | Légifrance, CGI art. 293 F | non relu en ligne à ce jour |

## La chronologie des réformes, sans rien trancher

| Date | Texte | Ce qu'il dit | État du relevé |
| --- | --- | --- | --- |
| 19/12/2023 | Loi n° 2023-1322 de finances pour 2024, art. 82 | Plafonds de 85 000 € et 37 500 €, plafonds majorés de 93 500 € et 41 250 €, fin de la franchise à la date du dépassement, applicables à compter du 01/01/2025 | titre du BOFiP ACTU-2025-00144, non relu en ligne à ce jour |
| 14/02/2025 | Loi n° 2025-127 de finances pour 2025, art. 32 | Plafond unique de 25 000 € (27 500 € majoré) à compter du 01/03/2025 | suspendu (BOFiP ACTU-2025-00087, suspension jusqu'au 31/12/2025), puis supprimé ; non relu en ligne à ce jour |
| 03/11/2025 | Loi n° 2025-1044 visant à garantir un cadre fiscal stable, juste et lisible pour nos micro-entrepreneurs et nos petites entreprises, art. 1 | Supprime le plafond unique de 25 000 € et maintient les plafonds de 85 000 € et 37 500 € | BOFiP ACTU-2025-00144 (01/07/2026), non relu en ligne à ce jour |
| 14/02/2025 | Loi n° 2025-127, art. 38 | Supprime le régime simplifié de TVA au 01/01/2027 | non relu en ligne à ce jour |
| 19/02/2026 | Loi n° 2026-103 de finances pour 2026 | Aucun changement des plafonds de la franchise relevé ; un projet de plafond de 25 000 € pour les travaux du bâtiment, écarté pendant les débats selon des sources secondaires | sources secondaires seulement, non relues |
| 17/12/2025 | Ordonnance n° 2025-1247 | Recodifie la TVA dans le code des impositions sur les biens et services (CIBS) ; art. 15 : les dispositions du CGI de la première colonne du tableau restent en vigueur jusqu'à leur reprise par des mesures réglementaires | relevé du 20/07/2026 (veille) ; art. 15, 46 et 49 relus le 04/10/2026 |
| 27/07/2026 | Ordonnance n° 2026-671 portant divers ajustements du CIBS | Art. 17 : reporte du 01/09/2026 au 01/01/2027 l'entrée en vigueur de la recodification de la TVA dans le CIBS (ordonnance n° 2025-1247, art. 49) et du 31/12/2027 au 30/06/2028 l'admission des références du CGI | texte lu sur Légifrance le 03/10/2026 |
| fin 09/2026 | Projet de loi de finances pour 2027 | Annoncé ; son contenu sur la franchise n'est pas connu | source secondaire seulement |

## Les désaccords et les incertitudes entre les sources

- **Date d'entrée en vigueur du CIBS pour la TVA** : tranchée au 01/01/2027. Le BOFiP BOI-RES-TVA-000253 du 18/02/2026
  et nos relevés du 20/07/2026 donnaient le 01/09/2026 ; l'ordonnance n° 2026-671 du 27/07/2026 (art. 17, texte lu le
  03/10/2026), postérieure, a reporté la date au 01/01/2027. La mention « art. 293 B du CGI » reste celle en vigueur
  jusqu'au 31/12/2026, et les anciennes références du CGI restent admises jusqu'au 30/06/2028.
- **Numéro du nouvel article** : tranché pour la franchise le 04/10/2026 par la lecture du CIBS consolidé au 01/01/2027 :
  L. 233-3 (entreprise franchisée en France), L. 233-9 et L. 233-10 (plafonds, mêmes montants que l'article 293 B). Les
  pages de la DGFiP (« Les régimes d'imposition à la TVA », modifiée le 21/05/2026 ; « En tant que micro-entrepreneur… »,
  modifiée le 16/06/2026) citent « article L.223-3 du CIBS », numéro d'avant l'ordonnance n° 2026-671, qui a renuméroté le
  livre II (L. 223-3 traite aujourd'hui de la déduction partielle). **Non tranché** : la mention à écrire à compter du
  01/01/2027, qu'aucun texte lu ne fixe ; la lire sur la page de la DGFiP du jour avant d'éditer un modèle de facture.
- **Plafond de 1 100 000 € pour l'année en cours** (CA3 trimestrielle dès 2027) : tranché le 04/10/2026, lu dans l'article 287
  du CGI (3, a et b, version du 01/01/2027) et sur la page de la DGFiP du 22/09/2026 : 1 000 000 € l'année civile précédente,
  1 100 000 € l'année en cours ; au-delà du second seuil, déclaration mensuelle dès le premier jour du mois du dépassement.
- **TVA exigible de 15 000 €** pour le régime simplifié : l'extrait dit « inférieure à 15 000 € » ; le cas d'un
  montant exactement égal n'est pas relevé.
- **Anciens plafonds** : tout chiffre daté d'avant 2025, et le plafond de 25 000 €, sont périmés. Ne pas les reprendre.

## Ce qui reste à relire

En pleine page : CGI art. 293 B et 293 F (Légifrance), BOFiP BOI-TVA-DECLA-40-10-10 et 40-10-20 (version du
01/07/2026), la page « Les régimes d'imposition à la TVA » d'impots.gouv.fr, la fiche F21746 de Service-Public, la loi
n° 2025-1044 du 03/11/2025, la loi n° 2025-127 du 14/02/2025 (art. 32 et 38) et l'ordonnance n° 2026-671 du 27/07/2026.
Tant que ce n'est pas fait, la réponse dit « non relu en ligne à ce jour ».

### Annexe : sortie-de-la-franchise-et-option

# Sortir de la franchise, ou y renoncer par option

Sources : impots.gouv.fr (« En tant que micro-entrepreneur, puis-je être redevable de la TVA ? »), BOFiP
BOI-TVA-DECLA-40-10-20 (version du 01/07/2026), CGI art. 293 F, extraits de recherche du 30/09/2026, pages non
ouvertes : non relu en ligne à ce jour.

## Quand la franchise cesse

| Étape | Ce qu'il faut faire | Point d'attention |
| --- | --- | --- |
| Dès l'opération du dépassement (plafond majoré) ou le 1er janvier | Facturer la TVA à partir de cette date | L'opération qui fait franchir le plafond est la première taxée (lecture de « à compter de la date du dépassement ») |
| Avant la première facture avec TVA | Obtenir un numéro de TVA intracommunautaire | Nécessaire pour facturer la TVA |
| Dès l'opération du dépassement | Informer le service des impôts des entreprises (espace professionnel impots.gouv.fr ; la doctrine parle aussi d'une simple lettre sur papier libre) | La sortie est à signaler même si la personne reste micro-entrepreneur |
| Sur les factures déjà émises | Les rectifier si elles portent des opérations taxables datées de ce jour ou après | Modalités exactes non relevées |
| Sur les factures futures | Retirer « TVA non applicable, art. 293 B du CGI » ; afficher le taux, le montant de TVA par taux, le total TTC et le numéro de TVA du vendeur | La mention vient des règles relevées ; à compter du 01/01/2027 aucun texte lu ne fixe la nouvelle (voir `seuils-et-etat-des-lieux.md`) |
| Sur les achats | La TVA devient déductible pour les dépenses dont le droit à déduction naît à compter de la date où l'on devient redevable | La TVA payée avant sur des stocks ou des immobilisations encore en possession : régularisation non relevée, à demander |
| Première déclaration | Jusqu'au 31/12/2026 : CA12 (régime simplifié) pour l'exercice, à déposer au plus tard le 2e jour ouvré après le 1er mai de l'année suivante pour un exercice égal à l'année civile, soit le 04/05/2027 pour 2026. Dès 2027 : CA3 du mois ou du trimestre, déposée le mois suivant | La date limite exacte d'une CA3 figure dans l'espace professionnel (fenêtre du 15 au 24 du mois suivant) |

## L'option pour le paiement de la TVA

- **Quoi** : renoncer à la franchise alors que les plafonds sont respectés (CGI art. 293 F).
- **Effet** : le premier jour du mois où l'option est déclarée.
- **Durée** : obligatoirement deux années civiles, dont celle de l'option, puis reconduction tacite sauf dénonciation auprès
  du service des impôts des entreprises.
- **Intérêt** : récupérer la TVA sur les achats et les investissements dès l'effet de l'option. Utile pour un gros
  investissement de départ (matériel, véhicule professionnel, aménagement) et pour une clientèle de professionnels, qui
  récupèrent eux-mêmes la TVA facturée.
- **Coût** : facturer la TVA. Avec une clientèle de particuliers, à prix payé inchangé, la TVA (un sixième du prix à 20 %)
  est prélevée sur la marge ; augmenter les prix est une autre option, avec son effet sur les ventes.
- **Ce que l'outil chiffre** : la TVA récupérable sur les investissements (une fois) et sur les achats (chaque année),
  la TVA à reverser à prix constant pour une clientèle de particuliers, et le solde indicatif de la première année. Il
  ne tient pas compte des taux réduits de vos ventes, des achats non taxés ni d'une hausse de prix.
- **Ce qui n'est pas relevé** : le régime d'imposition (simplifié ou normal) d'un assujetti par option qui reste sous les
  plafonds, et le délai de dénonciation.

## Aller plus loin avec OriginSkill

Ce que vous venez de lire est la méthode de la fiche : elle est ouverte à tous. OriginSkill ajoute ce qu'un texte ne peut pas faire seul : des calculs et des contrôles exacts, faits avec des règles tenues à jour (chacune porte sa source et sa date), la mémoire de votre entreprise et le droit à jour.

### Les calculs de cette fiche

Ces calculs sont inclus dans l'abonnement. OriginSkill les fait pour vous, avec des règles à jour et sourcées, et la réponse est garantie.

- **Savoir si vous êtes en franchise de TVA, au réel simplifié ou au réel normal** (outil `orizon_tva_franchise_regime`) : À partir du chiffre d'affaires de l'année précédente et de l'année en cours, dit dans quel régime de TVA vous êtes, la date de bascule et ses conséquences.

### Avec l'abonnement, en plus

- **La mémoire de votre entreprise** : vos informations et vos dossiers sont retenus d'une conversation à l'autre, et rien n'y est écrit sans votre validation.
- **Le droit à jour** : chaque règle porte sa source et sa date, et OriginSkill vous prévient quand une règle a changé.

### Brancher OriginSkill à votre assistant

Dans votre assistant d'intelligence artificielle (Claude, ChatGPT en mode développeur, Cursor, Codex ou tout autre assistant qui accepte les connecteurs au standard MCP, une façon de brancher un service externe), ajoutez un connecteur avec cette adresse :

    https://api.originskill.ai/mcp

Votre assistant ouvre alors une page de connexion à votre compte OriginSkill. Les étapes détaillées sont ici : https://originskill.ai/installer

### Tarif

Offres et abonnement : https://originskill.ai/tarif

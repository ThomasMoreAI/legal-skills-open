---
name: statut-juridique-choisir-fr-originlabs-app
title: Quel statut choisir pour créer mon entreprise
description: 'Quel statut choisir pour créer mon entreprise. Méthode professionnelle française, avec ses pièges et ses questions à poser. À utiliser quand : Un créateur ou une créatrice hésite entre la micro-entreprise, une entreprise individuelle au réel, une EURL ; Savoir combien il reste net, après cotisations et impôt sur le revenu, selon chaque statut, sur ses propres chiffres ; Savoir si l''on dépasse le plafond de la micro-entreprise, ce qui se passe alors, et quand passer en société.'
author: originlabs-app
author_url: https://github.com/originlabs-app/origin-skill-install/tree/main/skills/statut-juridique-choisir-fr
license: CC-BY-4.0
version: 0.1.0
execution_mode: open
jurisdiction: fr
practice: corporate
language: fr
---

> **Version gratuite sans date de référence des règles.** Les règles changent (SMIC, TVA, seuils…). Avec l'abonnement OriginSkill, votre assistant reçoit la règle à jour, avec sa source et sa date.

# Quel statut choisir pour créer mon entreprise

Une seule question : avec le chiffre d'affaires que j'attends, les charges que j'aurai et ce que je veux gagner,
quel statut me laisse le plus net, à quelles conditions, et qu'est-ce que je perds en route ? Le calcul se fait ;
le choix, lui, pèse aussi la protection sociale, la crédibilité auprès des clients, le risque, les associés et
l'envie de la personne, et il lui reste.

## Quand l'utiliser

- Un créateur ou une créatrice hésite entre la micro-entreprise, une entreprise individuelle au réel, une EURL
  ou une SARL, une SASU ou une SAS.
- Savoir combien il reste net, après cotisations et impôt sur le revenu, selon chaque statut, sur ses propres chiffres.
- Savoir si l'on dépasse le plafond de la micro-entreprise, ce qui se passe alors, et quand passer en société.
- Savoir si l'on peut payer l'impôt en même temps que les cotisations (versement libératoire) et si cela
  coûte moins que le barème.
- Comparer ce qu'il faut payer pour créer (formalités, annonce légale) et ce qui n'est pas relevé (comptable).
- Voir l'effet de l'Acre, de l'allocation chômage ou d'un autre revenu du foyer sur la comparaison.

Quand **ne pas** l'utiliser : se verser salaire ou dividendes dans une société déjà choisie (fiche
`remuneration-dirigeant-fr`) ; la seule question de la TVA (fiche `tva-franchise-ou-reel-fr`) ; le choix entre
capital de l'ARCE et maintien de l'allocation chômage (fiche `aides-creation-entreprise-fr`) ; une SA, une SCI, une
société à l'impôt sur le revenu, une société d'exercice libéral ; une activité mixte vente et services (non calculée) ;
le conseil patrimonial. Orienter en le disant.

## Les faits qui décident

Huit faits décident du résultat. Les connaître ; sinon donner la comparaison pour ce que l'on sait, hypothèses dites, et
poser en fin de réponse la question décisive.

- **La nature de l'activité** : vente de marchandises (ou logement), prestation de services commerciale ou artisanale
  (BIC), prestation libérale non réglementée (BNC), ou profession libérale réglementée relevant de la Cipav. « Libéral » ne
  suffit pas : le taux de la micro diffère selon la caisse, c'est la question décisive de l'outil.
- **Le chiffre d'affaires annuel prévu**, hors taxes (ou toutes taxes comprises avec le taux de TVA).
- **Les charges** annuelles hors taxes : elles ne réduisent pas l'impôt en micro, elles réduisent le net partout.
- **Le revenu voulu**, net avant impôt : il décide si une société a un sens (une société paie le salaire, l'entreprise
  individuelle ne se le verse pas).
- **Le foyer** : parts, autres revenus imposables (salaire du conjoint, allocation chômage, pension), revenu fiscal de référence
  de l'avant-dernière année.
- **Le statut du gérant d'une SARL** : majoritaire (plus de la moitié des parts avec son foyer) ou non.
- **Le taux de cotisations de l'indépendant** (entreprise au réel, gérant majoritaire) : **non relevé** ici, à passer en entrée.
- **La date de début d'activité et la situation pour l'Acre.**

**Faits de la mémoire d'entreprise consommables** (clés fermées de la mémoire ; un fait donné dans la conversation prime
toujours sur la mémoire, et un fait pris en mémoire se dit « à confirmer ») :

| Fait mémoire | Ce qu'il change ici |
| --- | --- |
| `forme_juridique` | statut actuel (SAS, SASU, SARL, EURL, EI, autre) : point de départ d'un changement de statut ; SA, SCI : hors de l'outil |
| `activite` | texte libre : le modèle le classe en vente, prestation BIC, prestation BNC ou libéral de la Cipav, et pose la question si c'est ambigu |
| `regime_tva` | `franchise_en_base` (l'ancien nom `franchise` reste accepté), `reel_simplifie`, `reel_normal` : ne change pas le calcul, sert à dire où l'on en est (le plafond de TVA vaut pour tous les statuts) |
| `impot` | `is` ou `ir` : une société à l'impôt sur le revenu est hors de l'outil |
| `regime_benefices` | `reel_normal` ou `reel_simplifie` : l'entreprise est déjà au réel, pas en micro |
| `associe_unique` | `personne_physique_dirigeant` : EURL ou SASU ; `non` : SARL ou SAS (part des dividendes à poser) |
| `denomination`, `siren` | nommer et retrouver le dossier |

Les autres faits de la mémoire (effectif, convention collective, cible) ne servent pas ici. Ne sont pas en mémoire et se
demandent à chaque fois : le chiffre d'affaires prévu, les charges, le revenu voulu, le foyer, le taux de cotisations de
l'indépendant.

## Connaissances du métier

**La réponse courte.** Les quatre statuts ne se distinguent pas d'abord par le nom, mais par *sur quoi* on paie :

| | Micro-entreprise | Entreprise individuelle au réel | EURL ou SARL à l'IS | SASU ou SAS |
| --- | --- | --- | --- | --- |
| Cotisations calculées sur | le chiffre d'affaires encaissé (taux fixe par activité) | le bénéfice réel (taux de l'indépendant) | la rémunération du gérant majoritaire (indépendant) et les dividendes au-delà de 10 % du capital | le salaire du président (assimilé salarié) ; aucune sur les dividendes |
| Impôt sur le revenu sur | le chiffre d'affaires moins un abattement forfaitaire (les vraies charges ne comptent pas), ou versement libératoire | le bénéfice | le salaire, puis les dividendes (flat tax ou barème) | le salaire, puis les dividendes |
| Impôt sur les sociétés | non | non | oui, 15 % puis 25 % | oui, 15 % puis 25 % |
| Plafond de chiffre d'affaires | oui | non | non | non |
| Chômage à ce titre | non relevé ici | non relevé ici | aucun droit (gérant majoritaire) | aucun droit (président) |

**Ce que le calcul apporte que le texte seul ne donne pas.** Le micro est simple et il est souvent le moins cher tant que les
charges sont faibles, parce qu'il paie sur le chiffre d'affaires et non sur le bénéfice : mais avec des charges élevées, il
paie des cotisations sur de l'argent qui n'a jamais été gagné (exemple 2 plus bas). Une société permet de ne pas tout se
verser, mais coûte des cotisations sur le salaire, de l'impôt sur les sociétés sur le reste et des frais de tenue. Le versement
libératoire peut coûter bien moins que le barème (1 320 € contre 4 983,99 € dans l'exemple 1), mais seulement si le revenu fiscal de référence de l'avant-dernière année est
sous le seuil du foyer. Un dépassement de plafond d'une année ne fait pas sortir de la micro ; deux années de suite, si.
Sur des chiffres réels ces effets se croisent ; le tableau de l'outil les rend visibles ligne par ligne.

**Exemple chiffré 1** (taux de 2026, relevé du 30/09/2026 ; prestation BNC, 60 000 € de chiffre d'affaires hors taxes,
8 000 € de charges, foyer d'une part sans autre revenu, capital de 1 000 € ; cotisations de l'indépendant à 45 % du
revenu net avant impôt, *hypothèse d'exemple* non officielle ; ni honoraires de comptable ni Acre) :

| Statut | Cotisations | Impôt sur le revenu | Net après impôt sur le revenu |
| --- | --- | --- | --- |
| Micro-entreprise (barème) | 15 360 € | 4 983,99 € | 31 656,01 € |
| Micro-entreprise, si le versement libératoire est ouvert | 15 360 € | 1 320 € | 35 320 € |
| Entreprise individuelle au réel | 16 137,93 € | 3 862,61 € | 31 999,46 € |
| EURL, tout en salaire | 16 137,93 € | 2 786,75 € | 33 075,32 € |
| SASU, tout en dividendes | 0 € (et 8 750 € d'impôt sur les sociétés) | 1 249,14 € | 33 874,96 € |

Sur ces seuls chiffres, la société ressort devant, et le micro avec versement libératoire devant tout. Mais la SASU en
dividendes ne verse aucune cotisation de retraite (les droits sont à vérifier, non relevés ici), les honoraires de comptable ne sont pas comptés, et la micro plafonne à
83 600 € : un exemple n'est pas une règle, les chiffres changent avec le chiffre d'affaires, les charges et le foyer.

**Repères datés** (photo au 30/09/2026 ; valeurs « relevées le 30/09/2026, texte officiel pas encore relu ; à reconfirmer
avant d'agir », par recherche en ligne restreinte aux sites officiels, pages non rouvertes) :

| Repère | Valeur | Source |
| --- | --- | --- |
| Plafonds de la micro-entreprise, 2026 à 2028 | 203 100 € (vente, logement) ; 83 600 € (prestations de services BIC, BNC, libéral) ; régime perdu au 1er janvier suivant si dépassé deux années civiles consécutives ; plafond proratisé l'année de création | BOFiP BOI-BAREME-000044 ; Service-Public Entreprendre F32353 |
| Taux de cotisations de la micro, 2026 | 12,3 % (vente) ; 21,2 % (prestations BIC) ; 25,6 % (BNC) ; 23,2 % (Cipav) du chiffre d'affaires encaissé | Urssaf, taux des auto-entrepreneurs ; le taux BNC de 25,6 % est à reconfirmer (une étape à 26,1 % était annoncée) |
| Abattement forfaitaire de la micro | 71 % (vente) ; 50 % (services BIC) ; 34 % (BNC) ; minimum 305 € | Service-Public Entreprendre F23267 |
| Versement libératoire | 1 % (vente) ; 1,7 % (services BIC) ; 2,2 % (BNC, libéral) du chiffre d'affaires ; revenu fiscal de référence de 2024 au plus égal à 29 315 € par part pour 2026 | impots.gouv.fr, le versement libératoire |
| Franchise de TVA | 85 000 € (vente) et 37 500 € (services) ; plafonds majorés 93 500 € et 41 250 € ; distincte du plafond de la micro | règles de comptabilité d'OriginSkill (fiche `tva-franchise-ou-reel-fr`) |
| Acre depuis le 01/01/2026 | réservée à certaines situations, à demander dans les 60 jours ; micro : 75 % des taux habituels pour un début à partir du 01/07/2026 ; indépendant et dirigeant : 25 % au plus | règles des aides à la création d'OriginSkill (fiche `aides-creation-entreprise-fr`) |
| Coûts de formalités | micro gratuit ; entreprise individuelle commerciale 21,74 € ; société commerciale 33,83 € ; annonce légale 2026 en métropole : 124 € (EURL), 142 € (SASU), à confirmer | Service-Public Entreprendre F37688, F23282, A18724 |
| Impôt sur les sociétés, flat tax, barème | 15 % jusqu'à 42 500 € puis 25 % ; 31,4 % sur les dividendes payés depuis le 01/01/2026 ; barème des revenus de 2025 | fiche `remuneration-dirigeant-fr` |

Le barème des revenus perçus en 2026 n'est pas voté à cette date : l'estimation prend celui des revenus de 2025, sans décote
ni plafonnement du quotient familial.

## Pièges fréquents

- **Choisir sur le net d'aujourd'hui seul.** Le net ne dit rien de la retraite, de la protection, du chômage ni de la
  crédibilité : ils ne sont pas dans le chiffre.
- **Croire le micro toujours le moins cher.** Avec des charges élevées, il paie sur le chiffre d'affaires ; le réel ou une société
  peuvent laisser plus de net.
- **Croire la société toujours plus avantageuse.** Elle coûte des frais de tenue, de l'impôt sur les sociétés sur ce qu'on laisse
  dedans, et des cotisations ; elle ne vaut que si l'on ne prélève pas tout.
- **Oublier que les charges ne réduisent pas l'impôt en micro.** L'abattement est forfaitaire.
- **Confondre le plafond de la micro et celui de la TVA.** Dépasser la franchise de TVA ne fait pas sortir de la micro.
- **Croire que le plafond dépassé fait sortir tout de suite.** Le régime est perdu au 1er janvier suivant si le plafond est
  dépassé deux années civiles consécutives ; l'année de création, le plafond est proratisé.
- **Prendre le versement libératoire pour ouvert.** Il dépend du revenu fiscal de référence de l'avant-dernière année et du
  nombre de parts ; un revenu du foyer trop élevé le ferme.
- **Prendre « libéral » pour un seul cas.** Cipav (23,2 %) ou non réglementé (25,6 %) : deux taux différents.
- **Inventer le taux de cotisations de l'indépendant.** Il n'est pas relevé ici ; le demander (simulateur de l'Urssaf,
  expert-comptable) ou le poser comme hypothèse dite.
- **Ignorer l'allocation chômage.** Elle compte dans les revenus du foyer et peut être maintenue avec l'activité : voir la fiche
  `aides-creation-entreprise-fr`.
- **Compter sans les honoraires de comptable.** Ils ne sont pas relevés : les donner, sinon le net est un maximum.
- **Ne pas dire si le gérant de SARL est majoritaire.** Tout change : cotisations d'indépendant ou de salarié.

## Méthodes proposées (jamais imposées)

1. **Du revenu voulu au statut** : partir de ce que la personne veut gagner par mois, poser le chiffre d'affaires et les charges,
   puis regarder quels statuts le donnent et à quel prix. Détails : `methode-du-revenu-voulu`.
2. **Les statuts côte à côte** : comparer les statuts sur les mêmes chiffres, lire le tableau ligne par ligne, tester un
   chiffre d'affaires plus bas et plus haut, puis passer en revue ce qui n'est pas dans le chiffre. Détails :
   `methode-statuts-cote-a-cote`.

Elles ne se valent pas toujours : la première convient à une personne qui part d'un besoin de revenu et n'a pas encore de
chiffre d'affaires sûr ; la seconde à une personne qui a déjà des chiffres et hésite entre deux statuts. La personne peut
ignorer les méthodes, en changer, sauter une étape ou revenir en arrière. Les cas types sont dans
`cas-types-et-arbitrages`, le plafond et la sortie de la micro dans `plafond-et-sortie-de-la-micro`,
le vocabulaire dans `glossaire`.

## Contrat de réponse (3 règles fixes)

1. Toute règle ou tout chiffre affirmé vient avec sa **source datée** : les taux viennent du calcul avec leur source ; un
   repère se cite avec sa source et la mention « relevée le 30/09/2026, texte officiel pas encore relu ; à reconfirmer avant
   d'agir ». Ne jamais écrire « règle vérifiée » pour une règle que le calcul dit non relue.
2. **Ne jamais inventer** : dire ce qui manque (taux de l'indépendant, honoraires, charges, foyer) et ce qui n'est pas relevé.
   Un ordre de grandeur de site professionnel n'est jamais présenté comme un taux.
3. **Prévenir** quand une règle vient de changer (champ `prudence`) : l'Acre depuis le 01/01/2026 et le taux minoré de la micro
   depuis le 01/07/2026, le taux BNC de 2026, la flat tax à 31,4 %.

« Plan d'action d'abord », « deux questions au maximum » et l'ordre des étapes sont de bonnes habitudes quand la personne veut
agir, pas des obligations.

**Restitution au dirigeant.**

1. Répondre d'abord, exactement, à la question posée et à rien d'autre : la règle ou le chiffre en une ou deux phrases, puis ce qui sert à cette question. Pas de tableau complet, pas de volet non demandé, aucun chiffre d'exemple inventé. Reprendre tels quels les chiffres de `en_clair.resultats`, sans les recalculer ; ne jamais affirmer qu'un point non fourni par le dirigeant est en règle.
2. Si un fait manque et change la réponse, donner la réponse pour chaque cas, puis poser une seule question à la fin : celle qui débloque. Aucune question si rien ne manque.
3. Parler en mots du dirigeant : jamais « l'outil », « le moteur », « le serveur », ni un code ou un champ technique (`entree_incomplete`, `manquant`, `prudence`) ; ne jamais recopier le mot « garanti » ni « non garanti ». Traduire : « il me manque la date d'embauche pour calculer… », « règle relevée le JJ/MM/AAAA, texte officiel pas encore relu ; à reconfirmer avant d'agir ». Écrire « vérifiée » seulement pour une règle marquée vérifiée (« règle vérifiée le JJ/MM/AAAA ; à reconfirmer avant d'agir si l'enjeu est important ») : une source citée n'est pas une vérification.
4. Une échéance qui tombe un samedi, un dimanche ou un jour férié se dit avec son report si les règles en donnent un, sinon « à vérifier ».
5. Ne jamais inventer un fait absent, ni pour appeler un outil. Une règle datée fournie par OriginSkill n'est jamais remplacée par une source secondaire trouvée en ligne ; en cas d'écart, donner les deux valeurs, leurs sources et leurs dates.

## Outils (description ouverte)

L'exécution exacte est servie par le connecteur, sur le moteur « dirigeant ». Cet outil ne recopie aucun calcul : il appelle
ceux de l'outil de rémunération du dirigeant (sociétés), de l'outil des aides à la création (Acre) et lit les plafonds de TVA
du moteur comptabilité.

| Outil | Sert à | Appeler quand |
| --- | --- | --- |
| `statut_juridique_comparer` (nom servi : `orizon_statut_juridique_comparer`) | Pour un chiffre d'affaires et des charges : micro (plafond, prorata de la première année, cotisations, abattement, barème ou versement libératoire), entreprise individuelle au réel, sociétés (salaire, dividendes, mixte, balayage, salaire net voulu), net après impôt, tableau ligne par ligne, classement indicatif, franchise de TVA, coûts de création, protection sociale, Acre, hypothèses et ce qui n'est pas calculé | Dès que l'activité et le chiffre d'affaires sont connus |
| `nom_disponible` (nom servi : `orizon_nom_disponible`) | Lire en direct ce qui est déjà pris pour un nom envisagé (société, marque, site) : nom de domaine .fr et .com (RDAP), marques françaises de l'INPI, dénominations d'entreprises de l'annuaire des entreprises ; ce qui est pris, où, depuis quand, ce qui n'a pas pu être consulté, source et date de consultation ; **jamais « libre »** : ce n'est pas une recherche d'antériorité complète (classes de produits et services, ressemblances phonétiques, marques européennes et internationales non couvertes) | Le créateur demande « mon nom est-il pris ? » avant d'immatriculer ou de déposer. **Outil ouvert progressivement : il n'existe que s'il figure dans la liste `outils` rendue par `orizon_fiche` ; sinon, renvoyer vers la base des marques de l'INPI, l'annuaire des entreprises et le registre des domaines sans affirmer qu'un nom est libre.** |

Entrées : `activite` et un chiffre d'affaires (`ca_annuel_ht_eur`, ou `ca_annuel_ttc_eur` avec `taux_tva_pct`) sont
indispensables. Facultatives : `charges_annuelles_eur`, `honoraires_comptable_annuels_eur`, `remuneration_nette_voulue_eur`,
`statuts` (micro, ei_reel, eurl, sarl, sasu, sas ; par défaut micro, ei_reel, eurl, sasu ; un seul statut donné est chiffré seul, sans comparaison, et l'outil le dit en nommant les alternatives usuelles non chiffrées), `gerant_majoritaire` (SARL),
`capital_social`, `cotisations_tns_pct_du_net` ou `cotisations_tns_pct_assiette` (le même taux sur l'assiette, converti et dit), `autres_cotisations_patronales_pct`, `taux_reduit_is`, `quote_part_foyer_gerant`,
`parts_fiscales`, `autres_revenus_imposables_foyer` (allocation chômage comprise), `rfr_n_moins_2_eur`, `date_debut_activite`,
`acre` (situation, acre_dans_les_3_ans, controle_effectif, demande_deposee_le), `date_reference`. Les dates se donnent au format
AAAA-MM-JJ, les montants comme la personne les dit (TTC ou HT). Une entrée non comprise est dite dans la prudence, une valeur
mal formée dans `manquant`, jamais une sortie vide.

Lire la réponse : `resultat.reponse` porte la synthèse ; `resultat.tableau` compare les statuts ligne par ligne (chiffre
d'affaires, charges, cotisations, impôt sur les sociétés, dividendes, impôt sur le revenu, net avant et après impôt, reste
dans la société) ; `resultat.statuts` donne le détail de chaque statut (taux appliqués, abattement, versement libératoire et son
éligibilité, plafond et marge, scénarios des sociétés) ; `resultat.classement_indicatif` ordonne les nets, sans recommander ;
`resultat.tva`, `creation_et_tenue`, `protection_sociale` et `acre` complètent ; `hypotheses` et `non_calcule` se disent toujours ;
`manquant` devient la question à poser ; `prudence` se dit une fois. Chaque appel répond sous la forme unique `resultat` /
`regles` / `manquant` / `prudence` / `garanti`.

Sans taux de cotisations de l'indépendant (`cotisations_tns_pct_du_net`, ou `cotisations_tns_pct_assiette` quand l'expert-comptable le donne sur l'assiette : l'outil convertit, x / (100 - x), et le dit), l'entreprise au réel n'est pas chiffrée et le gérant
majoritaire donne un maximum : demander le taux à la personne, ou le poser comme hypothèse en le disant (un ordre de grandeur
souvent cité est d'environ 45 % de la rémunération nette, non officiel). Une date limite d'Acre qui tombe un samedi, un dimanche
ou un jour férié est signalée ; aucun report n'est relevé, la date brute est gardée.

L'outil calcule ; il ne rédige rien, n'envoie rien et ne recommande rien. Le choix reste à la personne.

## Quatre usages

| Usage | Attitude | Outils |
| --- | --- | --- |
| Question simple (« c'est quoi le versement libératoire ? ») | Répondre avec la règle, sa date et sa source | aucun, ou `statut_juridique_comparer` si des chiffres sont donnés |
| Objectif précis (« 60 000 € de chiffre d'affaires en conseil, micro ou société ? ») | Appeler la comparaison tout de suite, rendre la réponse d'abord, puis les hypothèses et ce qui n'est pas dans le chiffre | `statut_juridique_comparer` |
| Suivre une méthode (« guide-moi pour choisir ») | Proposer l'une des deux méthodes ; la personne choisit le rythme | selon l'étape |
| Explorer (« et si je dépasse le plafond ? ») | Conversation libre, faits justes, sans chiffre inventé | outil seulement si des chiffres sont donnés |

## Sans abonnement (« non garanti »)

Les connaissances, les pièges, les méthodes et les cas types restent utiles. Le calcul exact, le tableau ligne par ligne, les
règles servies et l'Acre ne sont pas garantis : le dire, et indiquer `garanti: non`.

## Documents

Note de comparaison ou synthèse pour la personne : toujours un **projet à relire** par elle, jamais « prêt à signer ». Le modèle de
la personne rédige à partir des chiffres de la comparaison et des faits du dossier ; rien n'est produit ni envoyé par la fiche. Ne
jamais y mettre un taux ou un montant que la comparaison ne contient pas.

## Ce qui n'est pas relevé

Les taux de cotisations par poste de l'entrepreneur individuel et du gérant majoritaire en 2026 (réforme de l'assiette) ; les
honoraires d'expert-comptable ; la contribution à la formation professionnelle, les taxes des chambres et la cotisation foncière des
entreprises ; le niveau de la retraite, des indemnités journalières et de la protection (invalidité, décès ; pour une société, le classement dit seulement combien de trimestres de retraite valide le point de tête, d'après une règle non relue en ligne) ;
l'annonce légale des SARL et des SAS pluripersonnelles ; le cas d'une activité mixte ; le cumul de l'allocation chômage avec
l'activité ; la décote et le plafonnement du quotient familial ; le barème des revenus de 2026 ; le délai pour opter au versement
libératoire. Pour chacun, le dire et orienter vers l'Urssaf, son simulateur, la caisse, les statuts ou un professionnel pour un
enjeu important.

### Annexe : cas-types-et-arbitrages

# Cas types et arbitrages

Les montants viennent de l'outil `statut_juridique_comparer`, taux de 2026, barème de l'impôt sur le revenu des revenus de 2025,
règles « relevées le 30/09/2026, texte officiel pas encore relu ; à reconfirmer avant d'agir ». Un cas n'est pas une règle : les chiffres
changent avec le foyer, les charges et le chiffre d'affaires. Quand un taux de cotisations de l'indépendant figure, il est une **hypothèse
d'exemple** (45 % de la rémunération nette), non officielle, jamais un taux relevé.

## Cas 1 : conseil en BNC à 60 000 €

60 000 € de chiffre d'affaires hors taxes, 8 000 € de charges, foyer d'une part sans autre revenu, capital de 1 000 €, hypothèse
d'exemple de 45 % de cotisations pour l'indépendant. Micro au barème : 15 360 € de cotisations (25,6 %), abattement de 20 400 €, impôt de
4 983,99 €, net de 31 656,01 €. Si le revenu fiscal de référence de l'avant-dernière année est sous 29 315 €, le versement libératoire
(2,2 % du chiffre d'affaires, 1 320 €) porte le net à 35 320 €. Entreprise au réel : 31 999,46 €. EURL tout en salaire : 33 075,32 € ;
SASU tout en dividendes : 33 874,96 € (8 750 € d'impôt sur les sociétés). Arbitrage : la micro avec versement libératoire gagne ici tant
que le chiffre d'affaires reste sous 83 600 € et que le revenu fiscal le permet ; la société ne vaut que si le chiffre d'affaires monte ou
si l'on veut laisser du bénéfice dedans. Protection et retraite ne sont pas dans le chiffre.

## Cas 2 : vente avec peu de marge (150 000 € de chiffre d'affaires, 115 000 € de charges)

Micro : 18 450 € de cotisations (12,3 % du chiffre d'affaires, charges ou pas), impôt de 6 153,99 €, net de 10 396,01 €. Entreprise
individuelle au réel, hypothèse d'exemple de 45 % : cotisations de 10 862,07 € sur le bénéfice de 35 000 €, impôt de 1 379,17 €, net de
22 758,76 €. Arbitrage : quand les charges sont élevées, le micro paie sur un chiffre d'affaires qui n'est pas du revenu ; le réel, même
avec des honoraires de comptable à ajouter, peut laisser plus du double. Toute la décision est dans le rapport charges sur chiffre d'affaires.

## Cas 3 : versement libératoire ouvert (services BIC à 40 000 €)

40 000 € de chiffre d'affaires, 5 000 € de charges, autres revenus du foyer de 15 000 €, revenu fiscal de référence de 20 000 € pour une
part. Versement libératoire de 1,7 % : 680 €, contre 3 229,99 € au barème ; cotisations de 8 480 € ; net de 25 840 €. Arbitrage : avec un
revenu fiscal de référence de 30 000 €, l'option serait fermée (seuil de 29 315 € pour une part) ; avec deux parts le seuil est de 58 630 €.
Le revenu fiscal de référence compte, pas le revenu du jour.

## Cas 4 : le plafond est dépassé (services BIC à 90 000 €)

Le plafond de 83 600 € est dépassé de 6 400 €. La micro est perdue au 1er janvier suivant si le plafond est dépassé deux années civiles
consécutives. Chiffres micro de l'année, à titre indicatif : 19 080 € de cotisations, impôt de 6 603,99 €, net de 44 316,01 €
(charges de 20 000 €). Arbitrage : comparer avec l'entreprise individuelle au réel et une société avant la deuxième année de dépassement,
pas après. Première année : commencer le 01/07/2026 en BNC donne un plafond de 42 143,56 € pour 184 jours ; 60 000 € sur douze mois font
30 246,58 € cette année-là, sous le plafond proratisé.

## Cas 5 : l'Acre d'un micro-entrepreneur

BNC à 60 000 €, début d'activité le 01/10/2026, bénéficiaire du RSA ou de l'ASS, pas d'Acre dans les trois ans. Micro : cotisations à
75 % du taux habituel jusqu'au 30/09/2027, soit 11 520 € au lieu de 15 360 € (économie de 3 840 €) ; demande à l'Urssaf au plus tard le
30/11/2026 (un lundi). Si la date limite tombe un samedi, un dimanche ou un jour férié, l'outil le dit et garde la date brute (début le
06/10/2026 : limite le samedi 05/12/2026). Arbitrage : l'Acre change peu l'ordre des statuts la première année ; elle ne se demande pas
toute seule.

## Cas 6 : SARL, le gérant est-il majoritaire ?

Sans réponse, l'outil ne chiffre pas la SARL et pose la question : gérant majoritaire (plus de la moitié des parts avec son foyer), il
est indépendant, avec le taux de cotisations à fournir et les dividendes au-delà de 10 % du capital soumis à cotisations ; minoritaire ou
égalitaire, il est assimilé salarié comme un président de SAS. Donner les deux cas en une phrase chacun plutôt que refuser de répondre.

## Cas 7 : le revenu voulu en SASU

100 000 € de bénéfice avant rémunération, capital de 1 000 €, revenu voulu de 30 000 € nets par an avant impôt : l'outil cherche le
salaire qui donne exactement 30 000 € nets, l'impôt sur les sociétés est de 7 929,09 € sur le reste, et le reste distribué porte le net
après impôt à 56 110,57 €. Arbitrage : le salaire minimum dicte la retraite et la protection, pas le net ; le reste peut aussi ne pas être
distribué (il reste alors dans la société et n'est pas dans le net).

## Arbitrages à poser à la personne

- Préférez-vous la simplicité (micro, pas de comptable) ou l'optimisation (société, plus de gestion) ?
- Voulez-vous laisser de l'argent dans la société, ou tout prélever ?
- Quelle place pour la retraite, la protection et le chômage dans votre choix ? (non chiffrés ici)
- Avez-vous des associés, des clients qui exigent une société, une cession en vue ?

### Annexe : glossaire

# Glossaire

| Terme | Définition courte |
| --- | --- |
| Micro-entreprise | Entreprise individuelle sous un régime simplifié : cotisations et impôt calculés sur le chiffre d'affaires, dans la limite d'un plafond. |
| Entreprise individuelle au réel | Entreprise individuelle sans micro : impôt et cotisations calculés sur le bénéfice réel (chiffre d'affaires moins charges), comptabilité complète. |
| EURL, SARL | Sociétés à responsabilité limitée (un associé ou plusieurs) ; à l'impôt sur les sociétés dans l'outil. Le gérant majoritaire est travailleur indépendant. |
| SASU, SAS | Sociétés par actions simplifiées (un associé ou plusieurs) ; le président est assimilé salarié. |
| Chiffre d'affaires | Ce que l'activité facture (encaisse), hors taxes : ce n'est pas un revenu. |
| Bénéfice | Chiffre d'affaires moins charges : ce qui reste avant cotisations et impôt. |
| Charges | Dépenses de l'activité (achats, loyers, abonnements, déplacements), hors rémunération du dirigeant. |
| Plafond de la micro | Chiffre d'affaires annuel au-delà duquel on risque de perdre la micro : 203 100 € (vente) ou 83 600 € (services), 2026 à 2028. |
| Abattement forfaitaire | En micro, part du chiffre d'affaires retirée pour calculer l'impôt : 71 %, 50 % ou 34 % selon l'activité, minimum 305 €. Les vraies charges ne comptent pas. |
| Versement libératoire | Option de la micro : l'impôt sur le revenu se paie en même temps que les cotisations, à 1 %, 1,7 % ou 2,2 % du chiffre d'affaires, si le revenu fiscal de référence le permet. |
| Revenu fiscal de référence | Revenu de référence de l'avant-dernière année, sur l'avis d'impôt : condition du versement libératoire. |
| Parts fiscales | Nombre de parts du quotient familial du foyer (1 pour une personne seule). |
| Assimilé salarié | Président de SAS ou de SASU : régime général de la Sécurité sociale, sans assurance chômage à ce titre. |
| Travailleur indépendant | Micro-entrepreneur, entrepreneur individuel, gérant majoritaire de SARL ou d'EURL : cotisations propres aux indépendants. |
| Cotisations sociales | Sommes versées à l'Urssaf pour la maladie, la retraite, la famille : en micro, un pourcentage du chiffre d'affaires. |
| Impôt sur les sociétés (IS) | Impôt sur le bénéfice d'une société : 15 % jusqu'à 42 500 € sous conditions, 25 % au-delà. |
| Dividende | Part du bénéfice distribuée aux associés après impôt sur les sociétés ; jamais déductible. |
| Flat tax | Prélèvement forfaitaire sur les dividendes : 31,4 % en 2026 ; option possible pour le barème. |
| Franchise en base de TVA | Dispense de facturer la TVA sous un plafond de chiffre d'affaires : 37 500 € en services, 85 000 € en vente (plafonds de base). |
| Acre | Aide à la création : exonération partielle de cotisations la première année, depuis 2026 sous conditions de situation, à demander dans les 60 jours. |
| ARE | Allocation de retour à l'emploi : revenu imposable du foyer, à mettre dans les autres revenus ; cumul avec l'activité voir `aides-creation-entreprise-fr`. |
| Net avant, net après impôt | Net avant impôt : ce qui reste après cotisations. Net après impôt : après l'impôt sur le revenu estimé. |
| Classement indicatif | Ordre des nets d'une année, sans la retraite ni la protection : ce n'est pas une recommandation. |

### Annexe : methode-du-revenu-voulu

# Méthode : du revenu voulu au statut

Méthode proposée, jamais imposée. Elle convient à une personne qui part d'un besoin (« il me faut 2 500 € nets par mois ») et qui n'a
pas encore de chiffre d'affaires sûr : on cherche quels statuts peuvent le donner, et à quel prix, plutôt que de comparer des noms.

## Les étapes

1. **Dire le besoin en net par an.** Ce qu'il faut pour vivre, avant impôt sur le revenu : 2 500 € par mois font 30 000 € par an.
   Ajouter ce que le foyer gagne déjà (conjoint, allocation chômage, pension) : cela compte dans l'impôt, pas dans le besoin.
2. **Poser le chiffre d'affaires et les charges.** Hors taxes. Le chiffre d'affaires est une hypothèse : en donner deux ou trois (prudent,
   attendu, optimiste) plutôt qu'un seul. Les charges sont celles de l'activité, pas le salaire de la personne.
3. **Appeler la comparaison avec le revenu net voulu.** Pour une société, l'outil trouve le salaire
   dont le net avant impôt est exactement ce revenu, distribue le reste du bénéfice après impôt sur les sociétés, et dit si le
   revenu voulu n'est pas atteignable (avec le maximum). En micro et en entreprise individuelle, le revenu n'est pas réglable : il est
   ce que l'activité laisse, comparé au besoin.
4. **Lire dans l'ordre.** D'abord : le revenu voulu est-il atteint ? Ensuite le net après impôt sur le revenu de chaque statut, puis
   le plafond de la micro, puis ce qui reste dans la société.
5. **Regarder l'écart au besoin.** Un statut qui laisse moins que le besoin est hors jeu, sauf à changer le chiffre d'affaires. Un
   statut qui laisse beaucoup plus que le besoin peut laisser de l'argent dans la société : c'est une option, pas un gain (le dire).
6. **Passer en revue ce qui n'est pas dans le chiffre.** Retraite, protection, chômage, honoraires de comptable, trésorerie des
   premiers mois, image auprès des clients, associés.
7. **Conclure avec les hypothèses et le statut de la source.** Dire que les taux de 2026 sont appliqués, que le barème de l'impôt
   sur le revenu est celui des revenus de 2025, que les règles relevées n'ont pas toutes été relues sur les pages officielles (mention
   de non-garantie), et que le taux de cotisations de l'indépendant vient de la personne.

## Questions à poser, au maximum deux à la fois

- Quelle est la nature exacte de l'activité (vente, services commerciaux ou artisanaux, conseil ou prestation libérale, profession
  réglementée) ? C'est la question décisive : elle fixe tous les taux de la micro.
- Combien voulez-vous gagner net par mois, et que gagne déjà le foyer ?

## Limites

Un exercice de douze mois ; le chiffre d'affaires est celui de l'année complète, pas de la première année partielle (le plafond de la
première année est proratisé et dit). Pour se verser salaire ou dividendes dans une société, la fiche `remuneration-dirigeant-fr` va plus loin.

### Annexe : methode-statuts-cote-a-cote

# Méthode : les statuts côte à côte

Méthode proposée, jamais imposée. Elle convient à une personne qui a déjà des chiffres (chiffre d'affaires, charges) et qui hésite
entre deux ou trois statuts.

## Les étapes

1. **Fixer les faits.** Nature de l'activité, chiffre d'affaires annuel hors taxes, charges, foyer (parts, autres revenus,
   revenu fiscal de référence de l'avant-dernière année), statut du gérant d'une SARL. Poser en début de réponse les hypothèses prises
   faute d'information.
2. **Appeler la comparaison.** Les statuts par défaut sont la micro-entreprise, l'entreprise individuelle au réel, l'EURL à l'impôt sur
   les sociétés et la SASU ; ajouter la SARL ou la SAS si la personne a des associés. Pour l'entreprise au réel et le gérant majoritaire,
   donner le taux de cotisations de l'indépendant (en pourcentage du net) s'il est connu.
3. **Lire le tableau ligne par ligne, de haut en bas.** Chiffre d'affaires, charges, cotisations sociales, impôt sur les sociétés,
   dividendes, impôt sur le revenu, net avant impôt, net après impôt, reste dans la société. C'est l'écart sur une ligne qui explique
   l'écart du net.
4. **Vérifier les plafonds et la TVA.** Le chiffre d'affaires est-il sous le plafond de la micro ? Sous la franchise de TVA ? Le
   premier plafond est celui du statut, le second celui de la TVA : ils sont distincts.
5. **Tester la sensibilité.** Rappeler la comparaison avec un chiffre d'affaires de 20 % plus bas, puis 20 % plus haut, et avec des
   charges différentes : le statut qui gagne change-t-il ? S'il ne change pas, le choix est robuste ; s'il change, dire à partir de quel
   chiffre d'affaires environ (le lire sur les deux appels, sans l'inventer).
6. **Ajouter l'Acre si la personne y a droit.** Donner la situation et la date de début d'activité : l'outil dit les conditions, la date
   limite de la demande (60 jours, avec le jour de la semaine) et l'économie de la première année.
7. **Passer en revue ce qui n'est pas dans le chiffre.** Protection sociale ouverte par chaque statut (le niveau n'est pas relevé),
   chômage, retraite, honoraires, image, responsabilité, associés, vente future de l'activité.
8. **Ne pas prendre le classement pour une recommandation.** Il ordonne des nets d'une année ; il ne dit pas quel statut choisir.

## Ce que le tableau fait voir

- Le micro paie sur le chiffre d'affaires : la ligne « cotisations sociales » ne baisse pas quand les charges montent.
- L'entreprise individuelle au réel paie sur le bénéfice : avec des charges élevées, la ligne « cotisations » est bien plus basse qu'en micro.
- Une société paie de l'impôt sur les sociétés ; la ligne « reste dans la société » montre ce qui n'est pas dans le net.
- En SASU, la ligne « cotisations sociales » est nulle sur les dividendes ; en EURL, les dividendes au-delà de 10 % du capital en supportent.

## Limites

Activité mixte, plusieurs activités, TVA sur les achats, changement de statut en cours d'année : non traités. Honoraires de comptable
et taux de cotisations de l'indépendant : à fournir, sinon dits manquants.

### Annexe : plafond-et-sortie-de-la-micro

# Le plafond de la micro-entreprise et la sortie

Repères relevés le 30/09/2026, texte officiel pas encore relu ; à reconfirmer avant d'agir (BOFiP BOI-BAREME-000044, Service-Public
Entreprendre F32353 et F23267).

## Les plafonds

Chiffre d'affaires annuel hors taxes, 2026 à 2028 : 203 100 € pour la vente de marchandises et la fourniture de logement ; 83 600 € pour
les prestations de services (BIC et BNC) et les professions libérales. Le chiffre d'affaires est celui de l'année civile. Égal au plafond,
on reste dans la micro ; un euro de plus le dépasse (comparaison stricte).

## Dépassement

- Le régime de la micro-entreprise est perdu au 1er janvier de l'année suivante **si le plafond est dépassé deux années civiles
  consécutives**. Un dépassement isolé ne fait pas sortir.
- L'année de création, le plafond est proratisé au nombre de jours d'activité sur 365 : commencer le 01/07/2026 en BNC donne 184 jours
  dans l'année et un plafond de 42 143,56 €.
- Le dépassement du plafond majoré et le cas d'une première année très au-dessus du plafond ne sont pas relevés en détail : vérifier la
  page officielle avant d'agir.

## Ce qui change quand on sort

La personne relève alors d'un régime réel (entreprise individuelle au réel) ou crée une société. L'outil compare ces statuts sur les
mêmes chiffres. Ce qu'il ne fait pas : le calendrier exact de la bascule, les formalités de changement et la fiscalité d'un passage en
société (non relevés).

## TVA : un plafond distinct

La franchise de TVA a ses propres plafonds (85 000 € en vente, 37 500 € en services, majorés de 93 500 € et 41 250 €). Dépasser la
franchise de TVA ne fait pas sortir de la micro-entreprise ; dépasser le plafond de la micro n'oblige pas à sortir de la franchise de TVA
si le chiffre d'affaires reste sous ses plafonds (en pratique, en services, le plafond de TVA est le premier atteint). La date de bascule
de la TVA se calcule avec la fiche `tva-franchise-ou-reel-fr`.

## À dire à la personne

Un plafond est une limite de chiffre d'affaires, pas de bénéfice. Elle doit suivre son chiffre d'affaires en cours d'année ; le
plafond de la micro se regarde au 31 décembre, celui de la TVA se regarde opération par opération.

## Aller plus loin avec OriginSkill

Ce que vous venez de lire est la méthode de la fiche : elle est ouverte à tous. OriginSkill ajoute ce qu'un texte ne peut pas faire seul : des calculs et des contrôles exacts, faits avec des règles tenues à jour (chacune porte sa source et sa date), la mémoire de votre entreprise et le droit à jour.

### Les calculs de cette fiche

Ces calculs sont inclus dans l'abonnement. OriginSkill les fait pour vous, avec des règles à jour et sourcées, et la réponse est garantie.

- **Savoir si un nom est déjà pris** (outil `orizon_nom_disponible`) : Vérifie si un nom envisagé est déjà utilisé : nom de domaine .fr et .com, marques déposées à l'INPI, entreprises déjà immatriculées.
- **Choisir son statut : micro-entreprise, entreprise individuelle, société** (outil `orizon_statut_juridique_comparer`) : Compare ce que vous garderiez dans chaque statut (micro-entreprise, entreprise individuelle, EURL, SARL, SASU, SAS) à partir de votre chiffre d'affaires et de vos charges.

### Avec l'abonnement, en plus

- **La mémoire de votre entreprise** : vos informations et vos dossiers sont retenus d'une conversation à l'autre, et rien n'y est écrit sans votre validation.
- **Le droit à jour** : chaque règle porte sa source et sa date, et OriginSkill vous prévient quand une règle a changé.

### Brancher OriginSkill à votre assistant

Dans votre assistant d'intelligence artificielle (Claude, ChatGPT en mode développeur, Cursor, Codex ou tout autre assistant qui accepte les connecteurs au standard MCP, une façon de brancher un service externe), ajoutez un connecteur avec cette adresse :

    https://api.originskill.ai/mcp

Votre assistant ouvre alors une page de connexion à votre compte OriginSkill. Les étapes détaillées sont ici : https://originskill.ai/installer

### Tarif

Offres et abonnement : https://originskill.ai/tarif

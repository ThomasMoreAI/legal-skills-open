---
name: ag-annuelle-fr-originlabs-app
title: Approuver les comptes de l'année en assemblée
description: 'Approuver les comptes de l''année en assemblée. Méthode professionnelle française, avec ses pièges et ses questions à poser. À utiliser quand : Préparer l''approbation annuelle des comptes : calendrier, convocation, ordre du jour, ; Relire un projet de procès-verbal ou reprendre le dossier de l''an dernier pour cette année ; Répondre à une question précise : « avant quand approuver ? », « quel quorum en SA ? »,.'
author: originlabs-app
author_url: https://github.com/originlabs-app/origin-skill-install/tree/main/skills/ag-annuelle-fr
license: CC-BY-4.0
version: 0.1.0
execution_mode: open
jurisdiction: fr
practice: corporate
language: fr
---

> **Version gratuite : règles datées entre le 26/06/2026 et le 03/10/2026.** Les règles changent (SMIC, TVA, seuils…). Avec l'abonnement OriginSkill, votre assistant reçoit la règle à jour, avec sa source et sa date.

# Approuver les comptes de l'année en assemblée

Une seule fiche pour la tâche « faire approuver les comptes de l'exercice » : la forme de la
société change qui décide, avant quand et à quelle majorité ; la démarche reste la même.

## Quand l'utiliser

- Préparer l'approbation annuelle des comptes : calendrier, convocation, ordre du jour,
  résolutions, procès-verbal ou décision de l'associé unique.
- Relire un projet de procès-verbal ou reprendre le dossier de l'an dernier pour cette année.
- Répondre à une question précise : « avant quand approuver ? », « quel quorum en SA ? »,
  « l'associé unique gérant doit-il faire une AG ? », « que doit faire le gérant d'une SCI ? ».
- Contrôler un dossier complet avant la séance : délais, réserve obligatoire, obligation ou
  non d'avoir un commissaire aux comptes, taille de la société, déroulé de la séance d'une SA.

Quand **ne pas** l'utiliser : une assemblée extraordinaire (modification des statuts,
capital), une SA cotée, une association, une entreprise individuelle (pas d'assemblée), une
SNC, une SCA, une SELARL ou une SCOP (formes non traitées : l'outil le dit sans reprendre les
règles d'une autre forme). Le calcul du dividende et de la réserve légale relève de
`affectation-resultat-dividendes-fr`, le dépôt au greffe de `depot-comptes-annuels-fr` : les
deux s'appuient sur les mêmes règles.

## La forme juridique : un fait de profil

Tout dépend de la forme : SAS, SASU, SARL, EURL, SA non cotée ou SCI. Avant de lancer un calcul, la connaître.

- Si la mémoire OriginSkill est disponible (la mémoire d'entreprise), lire d'abord le profil
  validé de la société au lieu de le redemander.
- Si la personne donne un SIREN, `entreprise_profil` rend la forme, la tranche d'effectif et
  l'état de l'entreprise, avec leur source datée.
- Sinon, poser **une** question : « Quelle est la forme de la société : SAS, SASU, SARL,
  EURL, SA ou SCI ? ». Ne jamais la déduire d'une dénomination sociale ou d'un secteur.
- Deux formes voisines se distinguent par un fait : une société à associé unique est une SASU
  ou une EURL ; une SA est cotée ou non (la cotée est hors de cette fiche).

Une réponse générale (« en règle générale, les comptes s'approuvent dans les six mois ») peut
être donnée tout de suite, avec ses exceptions, avant même de connaître la forme.

## Connaissances du métier

Chaque année, les comptes arrêtés par les dirigeants sont soumis aux associés, qui les
approuvent et décident de l'affectation du résultat. Trois questions structurent tout :

- **Qui décide ?** L'assemblée des associés en règle générale. Avec un associé unique, une
  décision de l'associé unique ; s'il est aussi le dirigeant d'une EURL ou d'une SASU, le
  dépôt des comptes au greffe peut valoir approbation, sous conditions. En SCI, les statuts
  organisent la décision et les gérants doivent rendre compte de leur gestion au moins une
  fois par an.
- **Avant quand ?** En SARL et en SA, le délai est fixé par la loi à partir de la clôture,
  avec une prorogation possible par le juge si on la demande à temps. L'associé unique d'une
  SASU approuve aussi dans les six mois de la clôture. En SAS pluripersonnelle et en SCI,
  les statuts fixent le délai : il faut les lire.
- **Comment ?** Convocation dans le délai et selon le mode prévus, documents mis à
  disposition des associés avant l'assemblée, quorum et majorité : la loi pour la SARL et
  la SA, les statuts pour la SAS et la SCI.

Ce qui distingue chaque famille, à garder en tête pour choisir les questions :

- **SAS et SASU** : liberté statutaire, donc statuts d'abord (délai, convocation, majorité,
  consultation écrite) ; conventions réglementées à part.
- **SARL et EURL** : règles légales détaillées (majorité, convocation, communication des
  documents), seuils du commissaire aux comptes, dépôt valant approbation pour l'associé
  unique dirigeant d'une EURL.
- **SA non cotée** : gouvernance (conseil d'administration ou directoire), convocation
  formelle, quorum calculé en actions, mandats de vote, feuille de présence, affectation au
  centime, conventions, confidentialité des comptes.
- **SCI** : reddition des comptes des gérants, majorité statutaire ou unanimité à défaut de
  clause, aucune réserve légale automatique, pas de dépôt au greffe en principe.

Les délais, quorums, majorités et seuils chiffrés viennent des outils, avec leur source et
leur date. La fiche n'en fige aucun.

## Pièges fréquents

- **Appliquer « six mois » à toutes les formes.** Ce délai est légal en SARL, en SA et
  en SASU ; en SAS pluripersonnelle et en SCI, c'est la clause des statuts qui compte.
- **Conclure « hors délai » sur un jour de fin de mois.** Un délai en mois qui part d'une clôture au
  dernier jour d'un mois de 30 jours (30 juin, 30 septembre, 30 avril, 30 novembre) ne se compte pas
  pareil selon la convention : au même quantième (30 décembre pour une clôture au 30 juin) ou au dernier
  jour du mois d'arrivée (31 décembre). Donner les deux dates, dire laquelle l'outil retient (le même
  quantième), ne jamais déclarer en retard une décision signée le dernier jour du mois sans avoir
  montré les deux lectures, et conseiller de signer avant la date la plus tôt ; si l'échéance est
  dépassée, la prorogation se demande avant, pas après.
- **Croire que le retard d'approbation est le seul retard.** La déclaration de résultats (liasse) et
  le solde d'impôt sur les sociétés d'un exercice clos ont leurs propres dates, sans attendre
  l'approbation : pour une clôture hors 31 décembre, la liasse est due trois mois après la clôture (plus
  quinze jours si elle est télétransmise, fiche `calendrier-obligations-fr`), et le relevé de solde d'IS se dépose et se paie au plus
  tard le 15 du quatrième mois qui suit la clôture (15 juillet pour une clôture au 31 mars, 15 mai pour le 31 décembre ; CGI art. 1668, texte lu sur Légifrance le 03/10/2026 ; calcul avec `is-acomptes-solde-fr`). Quand une approbation est en retard, demander si la liasse a été
  déposée et le solde payé, et les traiter dans le plan de régularisation.
- **Convoquer l'associé unique.** Il n'y a ni convocation ni quorum : on rédige une décision.
- **Oublier les conventions réglementées.** Elles se votent à part, sans la voix de
  l'intéressé quand la loi l'exclut ; leur absence se constate aussi.
- **Laisser passer l'échéance sans prorogation.** Il faut demander la prorogation avant la
  fin du délai, pas après.
- **Recopier le procès-verbal de l'an dernier** sans mettre à jour dates, chiffres,
  mandats arrivés à échéance et présence ou non d'un commissaire aux comptes.
- **Transposer les règles d'une forme à une autre** : réserve légale ou dépôt en SCI,
  convocation de SARL pour une EURL, quorum de SA pour une SAS. Refaire l'analyse avec la
  bonne forme quand elle change.
- **Présenter un projet d'actes comme définitif.** Toute résolution rédigée à partir de la
  trame est un projet à relire par la société et son conseil.

## Méthodes proposées (jamais imposées)

1. **Rétroplanning depuis l'échéance** : partir de la date limite d'approbation et remonter
   vers la convocation, la mise à disposition des documents et l'arrêté des comptes.
   Détails : `methode-retroplanning`.
2. **Reprise du dossier N-1** : repartir du procès-verbal et des résolutions de l'an
   dernier, et ne changer que ce qui a changé. Détails : `methode-reprise-n-1`.

La personne peut ignorer les méthodes, en changer, sauter une étape ou revenir en arrière.

## Contrat de réponse (3 règles fixes)

1. Toute règle ou tout chiffre affirmé vient avec sa **source datée** (les outils la donnent).
2. **Ne jamais inventer** : dire ce qui manque ou ce qui est incertain, en particulier ce
   que seuls les statuts peuvent dire.
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

L'exécution exacte est servie par le connecteur, sur le moteur « vie de la société ».

| Outil | Sert à | Appeler quand |
| --- | --- | --- |
| `ag_dossier` (nom servi : `orizon_ag_dossier`) | Analyser le dossier complet de l'assemblée annuelle avec la logique de la forme : périmètre, délais, rétroplanning, réserve légale, seuils du commissaire aux comptes et de taille, quorum et convocation en SA, obligations de la SARL et de la SCI ; rend valeurs, contrôles, points à confirmer et trame des actes à faire rédiger, jamais un fichier | La personne veut préparer ou contrôler son assemblée et on connaît la forme et les faits principaux |
| `ag_regles` (nom servi : `orizon_ag_regles`) | Dire qui décide, l'échéance d'approbation, la date limite de convocation, le quorum et la majorité, pour la forme donnée | Question de calendrier ou de procédure, avec peu de faits |
| `affectation_resultat` (nom servi : `orizon_affectation_resultat`) | Réserve légale, bénéfice distribuable, dividendes possibles, calendrier fiscal des dividendes | L'ordre du jour comprend l'affectation du résultat |
| `depot_comptes` (nom servi : `orizon_depot_comptes`) | Date limite de dépôt, pièces, confidentialité possible | Après l'approbation |
| `entreprise_profil` (nom servi : `orizon_entreprise_profil`) | Rendre forme juridique, tranche d'effectif et état d'une entreprise à partir de son SIREN, source datée | La forme n'est pas connue et la personne donne son SIREN |

Entrées de `ag_dossier` : `forme` (SAS, SASU, SARL, EURL, SA ou SCI) et `dossier`, les faits
du cas dans la structure de la forme. Un fait absent sort dans `manquant`, jamais deviné.

- SAS, SASU et SCI : `societe` (dénomination, capital, siège, RCS), `exercice` (clôture,
  bénéfice ou résultat, total du bilan, chiffre d'affaires net, effectif), `associes` (nom,
  actions ou parts), `statuts` (délais de convocation et d'approbation, majorité, quorum),
  `calendrier` (date de l'assemblée), `mode` (`answer`, `review`, `modify`, `produce`),
  `conventions_reglementees` ; pour la SCI aussi `mode_consultation`, `regime_fiscal`,
  `assujetti_tva`, `activite`.
- SARL et EURL : `operation_mode`, `request`, `company`, `accounting`, `documents`,
  `governance`, `meeting`, `financials`, `filing`, `incidents` (montants en centimes).
- SA non cotée : faits types identifiés (`company`, `identities`, `shareholdings`,
  `governance`, `assembly`, `documents`, `financials`, `distribution_history`,
  `agreements`, `meeting`, `confidentiality`, `deadlines`, `context`), montants en centimes.

Entrées des autres outils (toutes facultatives sauf `forme` ; dates au format AAAA-MM-JJ,
montants en euros ; une entrée mal nommée est signalée dans `prudence`) :

- `ag_regles` : `forme`, `cloture`, `date_ag`, `prorogation_obtenue`, et pour une EURL
  ou une SASU `associe_unique_dirigeant` et `associe_unique_personne_physique` ; ce que
  disent les statuts dans `statuts.delai_approbation_mois` et `statuts.delai_convocation_jours`.
- `affectation_resultat` : `forme`, `resultat`, `capital`, `reserve_legale_existante`,
  `report_a_nouveau` (négatif pour des pertes), `reserves_libres`, `capitaux_propres`
  (après résultat), `reserves_statutaires_a_doter`, `dividendes_proposes`, `beneficiaires`
  (personnes physiques résidentes, sociétés, non-résidents), `cloture`, `date_mise_en_paiement` ; en SARL ou
  EURL `gerant_majoritaire`, `quote_part_foyer_gerant` (0 à 1) et
  `capital_primes_comptes_courants` (détenus par ce foyer).
- `depot_comptes` : `forme`, `date_approbation`, `cloture`, `canal` (`electronique` ou
  `papier`), `total_bilan`, `chiffre_affaires`, `effectif`, `cac`, `associe_unique`,
  `approbation_par_depot`.

Lire la réponse : `manquant` devient la question à poser ; `prudence` se dit une fois (règle
non recoupée, changement de texte, point à traiter avant de conclure) ; `resultat.trame`
donne les actes à faire rédiger et les points à confirmer. Chaque outil répond sous la forme
unique `resultat` / `regles` / `manquant` / `prudence` / `garanti`.

## Quatre usages

| Usage | Attitude | Outils |
| --- | --- | --- |
| Question simple (« avant quand approuver en SARL ? ») | Répondre directement, avec la règle et sa source | `ag_regles` |
| Objectif précis (« prépare mon AG du 20 juin ») | Forme d'abord, puis calendrier, ordre du jour et projet de résolutions à relire | `ag_dossier`, puis `affectation_resultat` |
| Suivre une méthode (« guide-moi étape par étape ») | Proposer une des deux méthodes ; la personne choisit le rythme | selon l'étape |
| Explorer (« pourquoi un associé unique n'a pas d'AG ? ») | Conversation libre, faits justes et sourcés | outils seulement s'ils aident |

## Sans abonnement (« non garanti »)

Les connaissances, les pièges et les méthodes restent utiles. Les règles datées, les calculs
exacts et les cas de référence du moteur ne sont pas garantis : le dire, et indiquer
`garanti: non`.

## Documents

Convocation, ordre du jour, résolutions, procès-verbal ou décision de l'associé unique :
toujours un **projet à relire**, jamais « prêt à signer ». Le modèle de la personne rédige à
partir de la trame de `ag_dossier` ; chaque clause porte la règle qui la fonde et sa source ;
ce que seuls les statuts peuvent dire reste signalé. La fiche ne produit aucun fichier.

Ordre du jour type d'une approbation annuelle, à adapter (forme, statuts, commissaire aux
comptes) :

1. Rapport de gestion du dirigeant (et rapport du commissaire aux comptes s'il y en a un).
2. Approbation des comptes de l'exercice clos le [date] et quitus au dirigeant si les
   statuts le prévoient.
3. Affectation du résultat (montants issus de `affectation_resultat`).
4. Conventions réglementées : rapport spécial et vote convention par convention (hors SCI).
5. Questions diverses prévues par les statuts (mandats arrivant à échéance, commissaire aux
   comptes).
6. Pouvoirs pour les formalités de dépôt.

### Annexe : formalites-depot

# Formalités après l'assemblée : dépôt des comptes (France)

Repère commun à toutes les formes (SAS, SASU, SARL, EURL, SA non cotée, SCI). Décrit la
procédure de dépôt APRÈS l'approbation des comptes. Le plan de dépôt exact (date limite selon
le canal, pièces, confidentialité) est calculé par l'outil `depot_comptes` ; ici, le contexte
pour l'expliquer. Rien n'est envoyé ni déposé par la fiche : elle aide à préparer un plan, une
liste de contrôle et des projets de déclaration.

## Quand

Après l'approbation des comptes (assemblée ou décision de l'associé unique), dans le délai
de dépôt. La SCI fait exception : pas d'obligation de dépôt au greffe par défaut (sauf
activité économique au-delà des seuils de L.612-1 ; `depot_comptes` le demande).

## Où et comment

- Guichet unique des formalités (INPI) : https://formalites.entreprises.gouv.fr (démarche
  dématérialisée depuis 2023). Navigateur recommandé : Chrome. PDF individuels inférieurs à
  10 Mo.
- Authentification forte requise : **FranceConnect+** (gratuit, via Identité Numérique La
  Poste) ou **signature électronique avancée** (certificat qualifié, payant). Sans elle, le
  dossier est rejeté.

## Délais (après l'approbation)

- Voie électronique : **2 mois**. Voie papier (correspondance) : **1 mois**.
- `depot_comptes` calcule la date limite selon le canal.

## Frais (à reverifier)

Ordre de grandeur **environ 44 EUR** tout compris (émoluments du greffe, INPI, BODACC et
TVA). Relevé du greffe du tribunal des activités économiques de Paris (01/2025) : 42,58 EUR
au guichet, 44,14 EUR par correspondance. **À reverifier au moment d'agir** : variable par
greffe, canal et année. Ne pas étiqueter un montant « en ligne » sans vérifier le canal exact.

## Pièces à joindre

- Comptes annuels (bilan, compte de résultat, annexe), en un PDF.
- Procès-verbal d'assemblée (ou décision de l'associé unique) certifié conforme, avec
  l'affectation du résultat.
- Rapport du commissaire aux comptes si la société en a un (seuils du commissaire aux
  comptes : à reverifier).

## Confidentialité (option exercée AU dépôt)

Selon la catégorie comptable (seuils de D.123-200, à reverifier) :

- **micro** (bilan 450 000 EUR, chiffre d'affaires 900 000 EUR, 10 salariés) : confidentialité
  **totale** (bilan, compte de résultat, annexe), déclaration jointe, donc pas de publication
  au BODACC.
- **petite** (bilan 7,5 M EUR, chiffre d'affaires 15 M EUR, 50 salariés) : confidentialité du
  **compte de résultat**.
- au-delà : pas de confidentialité. Exclusions possibles (groupe, établissement de crédit ou
  d'assurance) : à confirmer.

## BODACC

Publication automatique par le greffe, SAUF confidentialité totale (micro).

## Retard, régularisation, prorogation

Si l'assemblée est simplement tenue après le délai légal d'approbation, régulariser sans
délai et documenter le retard. La prorogation se demande au président du tribunal compétent
AVANT l'échéance, et seulement si la personne la demande ; en SCI, elle n'existe pas sous
cette forme : régulariser la reddition sans attendre.

## Garde-fous

La fiche prépare des projets (déclaration de confidentialité, attestation de conformité,
liste de contrôle du dépôt). Elle ne se connecte pas au guichet unique, ne téléverse rien,
ne paie rien, ne signe rien. La personne dépose et valide.

## Points à reverifier avant d'agir

- Frais de dépôt et canal exact (greffe compétent, année).
- Délais de dépôt (1 mois, 2 mois) et règles d'authentification du guichet unique.
- Seuils de confidentialité micro et petite (D.123-200) et exclusions.
- Seuils de nomination du commissaire aux comptes (décret 2024-152 : bilan 5 M EUR, chiffre
  d'affaires 10 M EUR, 50 salariés, deux critères sur trois).

## Sources relevées le 26/06/2026

- Dépôt des comptes (société) : https://entreprendre.service-public.gouv.fr/vosdroits/F31214
- Confidentialité (L.232-25) : https://www.legifrance.gouv.fr (Code de commerce)
- Seuils D.123-200 : https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000049216681
- Seuils du commissaire aux comptes : https://entreprendre.service-public.gouv.fr/vosdroits/F31440
- Frais (greffe TAE Paris) : https://www.greffe-tae-paris.fr/procedure/depot_comptes_sociaux
- Guichet unique (INPI) : https://formalites.entreprises.gouv.fr

### Annexe : glossaire

# Glossaire

| Terme | Définition courte |
| --- | --- |
| AGOA | Assemblée générale ordinaire annuelle, qui approuve les comptes et affecte le résultat. |
| Décision de l'associé unique | Acte par lequel l'associé unique d'une EURL ou SASU décide seul, sans assemblée. |
| Reddition des comptes | Obligation des gérants de SCI de rendre compte de leur gestion aux associés au moins une fois par an. |
| Prorogation | Allongement du délai d'approbation accordé par le juge, à demander avant l'échéance. |
| Quorum | Part minimale du capital ou des parts présente ou représentée pour que l'assemblée délibère. |
| Conventions réglementées | Contrats entre la société et un dirigeant ou associé, soumis à un vote particulier. |
| Commissaire aux comptes | Professionnel qui certifie les comptes, obligatoire au-delà de certains seuils. |

### Annexe : liens-ressources

# Ressources : assemblée annuelle d'approbation des comptes

Pays : France. Langue : français. Les délais, seuils et majorités datés sont dans
les règles communes « vie de la société » d'OriginSkill : chaque calcul cite
l'article, son lien Légifrance et la date du dernier relevé. Cette page donne les liens
utiles et les documents à demander ; elle ne remplace pas la règle citée par l'outil.

## Documents à demander au client

- Statuts à jour : source décisive en SAS pluripersonnelle et en SCI (délai et mode de convocation, quorum,
  majorité, consultation écrite, visio), et clauses renforcées en SARL et SA.
- Comptes annuels de l'exercice clos : bilan, compte de résultat, annexe (sauf dispense).
- Extrait Kbis récent et répartition du capital (registre des mouvements de titres).
- Procès-verbal de la dernière assemblée.
- Grand livre ou liste des conventions passées avec un dirigeant ou un associé.
- Pacte d'associés le cas échéant.

## Calendrier type

1. Arrêté des comptes et rapport de gestion par le dirigeant.
2. Mise à disposition des documents aux associés (droit de communication).
3. Rapport du commissaire aux comptes, s'il y en a un.
4. Convocation : délai légal en SARL et en SA (voir `ag_regles`), statutaire en SAS et en SCI.
5. Assemblée ou décision, procès-verbal ou décision de l'associé unique au registre.
6. Dépôt au greffe (voir `depot_comptes`), sauf SCI en principe.

## Sources officielles par forme

- Code de commerce, SARL et EURL : L.223-26 (délai), R.223-20 (convocation), L.223-29
  (majorité), L.223-19 (conventions), L.223-31 (associé unique).
- Code de commerce, SAS et SASU : L.227-9 (décisions collectives, associé unique),
  L.227-10 (conventions).
- Code de commerce, SA non cotée : L.225-96 à L.225-125 (dont L.225-98 quorum et
  majorité, L.225-100 délai), R.225-66 à R.225-69 (convocation), R.225-106 (procès-verbal).
  https://www.legifrance.gouv.fr/codes/id/LEGISCTA000006161273/
- Code civil, SCI : art. 1856 (reddition des comptes, au moins une fois par an),
  art. 1852 (à défaut de clause, unanimité). Code de commerce L.612-1 pour une SCI qui
  exerce une activité économique.
- Commun : L.232-1 (rapport de gestion), L.232-10 et L.232-11 (réserve légale, bénéfice
  distribuable), L.232-21 à L.232-25 (dépôt, confidentialité), D.221-5 (seuils du
  commissaire aux comptes). Légifrance : https://www.legifrance.gouv.fr
- Service-Public Entreprendre : décisions en SARL/EURL (F36714), en SASU (F39283),
  dépôt des comptes (F31214), seuils comptables (F31440).
  https://entreprendre.service-public.gouv.fr
- Guichet unique des formalités (dépôt en ligne) : https://formalites.entreprises.gouv.fr
- BALO (SA à actions au porteur) : https://www.journal-officiel.gouv.fr/pages/balo-recherche/

## Cas particuliers

### Retard et prorogation
En société commerciale, la prorogation du délai d'approbation se demande au président du
tribunal de commerce, avant l'échéance. Exemple de procédure :
https://www.greffe-tae-paris.fr/procedure/prorogation_delai_approbation_comptes.
En SCI, il n'existe pas de prorogation de ce type : régulariser la reddition sans attendre.

### Associé unique (EURL, SASU)
Pas d'assemblée : décision de l'associé unique consignée au registre. Si l'associé unique
est une personne physique et le dirigeant, le dépôt des comptes signés dans les six mois
vaut approbation (`ag_regles` le dit quand les deux conditions sont données).

### Majorité en SAS
Arrêt de la Cour de cassation du 15 novembre 2024 (n° 23-16.670) : une décision collective
de SAS se prend au plus grand nombre de voix ; relire la clause de majorité des statuts à
cette aune. Point hors calcul : à vérifier dans les statuts du client.

### SCI
Tout se lit dans les statuts. À l'impôt sur le revenu, chaque associé est imposé sur sa
quote-part, distribuée ou non. Pas de dépôt au greffe par défaut, sauf activité économique
au-delà des seuils de L.612-1.

## Guides pédagogiques (secondaires, à recouper)

bpifrance-creation.fr, legalstart.fr, captaincontrat.com, l-expert-comptable.com.
Toujours valider le point de droit sur la source officielle.

### Annexe : methode-reprise-n-1

# Méthode : reprise du dossier de l'an dernier

Pratique courante des cabinets et des services juridiques : le dossier d'approbation d'une
société change peu d'une année sur l'autre. La méthode, formulée ici par nos soins,
consiste à ne toucher qu'à ce qui a changé, mais à le chercher systématiquement.

1. **Rassembler le dossier N-1** : convocation, procès-verbal ou décision, résolutions,
   preuve du dépôt.
2. **Lister ce qui change forcément** : exercice, dates, chiffres, affectation, montant des
   dividendes éventuels.
3. **Chercher ce qui a pu changer** : associés et répartition du capital, dirigeants,
   mandats arrivés à échéance (dirigeants, commissaire aux comptes), conventions
   réglementées nouvelles ou terminées, franchissement des seuils du commissaire aux comptes
   ou de la taille, modification des statuts dans l'année.
4. **Refaire passer les outils** (`ag_dossier` sur le dossier mis à jour, ou `ag_regles` puis `affectation_resultat`) : une règle a pu
   changer depuis l'an dernier, le champ `prudence` le signale.
5. **Rédiger le projet** en partant du texte N-1, chaque changement marqué pour la relecture.

Approche concurrente : **repartir d'un modèle vierge** chaque année. Plus long, mais évite
de reconduire une erreur de l'an dernier ; utile quand le dossier N-1 est incomplet ou
quand la forme de la société a changé.

Le résultat reste un projet à relire, jamais un acte prêt à signer.

### Annexe : methode-retroplanning

# Méthode : rétroplanning depuis l'échéance d'approbation

Source de la structure : la fiche « Approbation des comptes annuels » d'Entreprendre
Service-Public et les articles du Code de commerce cités par `ag_regles` (délai
d'approbation, convocation, documents à mettre à disposition). La méthode est la nôtre :
elle part de la date qu'on ne peut pas dépasser et remonte.

1. **Fixer l'échéance.** `ag_regles` (ou `ag_dossier` quand le dossier est déjà là) avec la forme et la date de clôture. En SASU, le délai
   légal est de six mois. En SAS pluripersonnelle et en SCI, lire d'abord la clause des
   statuts ; sans elle, l'échéance reste à confirmer.
2. **Choisir la date de l'assemblée** avant l'échéance, avec une marge pour une seconde
   convocation si le quorum peut manquer (SA, SARL sur première consultation).
3. **Remonter vers la convocation.** L'outil donne la date d'envoi au plus tard ; ajouter
   le délai d'acheminement du mode choisi (lettre, courriel si les statuts le permettent).
4. **Remonter vers les documents.** Comptes, rapport de gestion s'il est requis, texte des
   résolutions, rapport du commissaire aux comptes s'il y en a un : prêts avant la
   convocation.
5. **Remonter vers l'arrêté des comptes** par les dirigeants, qui précède tout le reste.
6. **Après l'assemblée** : affectation votée (`affectation_resultat`), puis dépôt
   (`depot_comptes`).

Approche concurrente : le **calendrier annuel fixe** tenu par beaucoup de cabinets (même
date chaque année, par exemple fin juin). Il est simple à tenir mais ignore les délais
statutaires propres à chaque société ; le rétroplanning les rend visibles.

Aucune promesse de résultat : la méthode réduit les oublis, elle ne remplace ni les
statuts ni le conseil de la société.

## Aller plus loin avec OriginSkill

Ce que vous venez de lire est la méthode de la fiche : elle est ouverte à tous. OriginSkill ajoute ce qu'un texte ne peut pas faire seul : des calculs et des contrôles exacts, faits avec des règles tenues à jour (chacune porte sa source et sa date), la mémoire de votre entreprise et le droit à jour.

### Les calculs de cette fiche

Ces calculs sont inclus dans l'abonnement. OriginSkill les fait pour vous, avec des règles à jour et sourcées, et la réponse est garantie.

- **Lire le texte officiel d'un article de loi** (outil `orizon_article_texte`) : Va chercher, au moment de la question, le texte officiel d'un article de loi sur le site de l'État, tel qu'il est en vigueur à la date voulue.
- **Retrouver la fiche d'une entreprise avec son numéro SIREN** (outil `orizon_entreprise_profil`) : Rend ce que les registres publics disent d'une entreprise : nom, forme juridique, activité, effectif, adresse du siège, dirigeants publiés, entreprise en activité ou fermée.
- **Connaître le calendrier et les règles de l'assemblée annuelle** (outil `orizon_ag_regles`) : Pour une SAS, SASU, SARL, EURL, SA non cotée ou SCI : qui approuve les comptes, avant quand, délai de convocation, quorum, majorité, retard et dépôt valant approbation.
- **Contrôler le dossier de l'assemblée annuelle** (outil `orizon_ag_dossier`) : Analyse le dossier de l'assemblée annuelle d'une société à partir de votre situation, avec les règles propres à sa forme juridique.
- **Répartir le résultat et calculer les dividendes** (outil `orizon_affectation_resultat`) : Calcule la réserve légale, le bénéfice distribuable, le dividende maximum et les dates fiscales du versement selon les bénéficiaires.
- **Déposer les comptes annuels au greffe** (outil `orizon_depot_comptes`) : Dit si les comptes doivent être déposés, avant quelle date, avec quelles pièces, dans quelle catégorie de taille, avec quels frais indicatifs.

### Avec l'abonnement, en plus

- **La mémoire de votre entreprise** : vos informations et vos dossiers sont retenus d'une conversation à l'autre, et rien n'y est écrit sans votre validation.
- **Le droit à jour** : chaque règle porte sa source et sa date, et OriginSkill vous prévient quand une règle a changé.

### Brancher OriginSkill à votre assistant

Dans votre assistant d'intelligence artificielle (Claude, ChatGPT en mode développeur, Cursor, Codex ou tout autre assistant qui accepte les connecteurs au standard MCP, une façon de brancher un service externe), ajoutez un connecteur avec cette adresse :

    https://api.originskill.ai/mcp

Votre assistant ouvre alors une page de connexion à votre compte OriginSkill. Les étapes détaillées sont ici : https://originskill.ai/installer

### Tarif

Offres et abonnement : https://originskill.ai/tarif

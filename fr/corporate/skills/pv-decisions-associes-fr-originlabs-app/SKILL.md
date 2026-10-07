---
name: pv-decisions-associes-fr-originlabs-app
title: Faire voter les associés et préparer le procès-verbal
description: 'Faire voter les associés et préparer le procès-verbal. Méthode professionnelle française, avec ses pièges et ses questions à poser. À utiliser quand : Nommer ou révoquer un président ou un gérant : qui décide, à quelle majorité, quel PV ; Transférer le siège, changer la dénomination ou l''objet, augmenter le capital de façon simple ; Vérifier si un vote est acquis : « 600 voix pour sur 1 000, les statuts disent deux tiers, est-ce.'
author: originlabs-app
author_url: https://github.com/originlabs-app/origin-skill-install/tree/main/skills/pv-decisions-associes-fr
license: CC-BY-4.0
version: 0.1.0
execution_mode: open
jurisdiction: fr
practice: corporate
language: fr
---

> **Version gratuite : règles datées entre le 18/07/2026 et le 03/10/2026.** Les règles changent (SMIC, TVA, seuils…). Avec l'abonnement OriginSkill, votre assistant reçoit la règle à jour, avec sa source et sa date.

# Faire voter les associés et préparer le procès-verbal

Une fiche pour la tâche « les associés doivent décider quelque chose (un nouveau dirigeant, un
autre siège, un nouveau nom ou objet, plus de capital) : comment, à quelle majorité, avec quel
procès-verbal, et où en est-on ? ». Elle couvre les quatre formes les plus courantes : la SAS et
la SASU, la SARL et l'EURL.

## Quand l'utiliser

- Nommer ou révoquer un président ou un gérant : qui décide, à quelle majorité, quel PV.
- Transférer le siège, changer la dénomination ou l'objet, augmenter le capital de façon simple.
- Vérifier si un vote est acquis : « 600 voix pour sur 1 000, les statuts disent deux tiers, est-ce
  bon ? » ; calculer les voix qu'il faudrait.
- Préparer le projet de procès-verbal ou la décision de l'associé unique à partir des faits, ou relire
  un PV déjà écrit.

Quand **ne pas** l'utiliser : approbation annuelle des comptes et affectation du résultat
(`ag-annuelle-fr`, `affectation-resultat-dividendes-fr`, dépôt des comptes :
`depot-comptes-annuels-fr`) ; SA, SCI et autres formes ; dissolution, fusion, cession de titres,
réduction du capital, augmentation avec suppression de droits préférentiels, émission de valeurs
mobilières complexes, opérations sur pacte ou clause d'agrément ; société en difficulté ; litige entre
associés ou contestation d'une décision déjà prise : orienter vers un avocat ou un expert-comptable.
Si les statuts sont ambigus ou muets sur un point décisif, le dire et faire qualifier le point.

## Connaissances du métier

**L'associé unique décide seul.** En SASU comme en EURL, il n'y a ni quorum ni majorité : la décision
est écrite et répertoriée au registre des décisions. Le plus courant : oublier de l'écrire et de la
répertorier, sous prétexte que « c'est moi qui décide ».

**En SAS, tout vient des statuts.** La forme des décisions collectives, le quorum et la majorité sont
fixés par les statuts ; sans eux, ces éléments ne se déterminent pas, et il ne faut jamais importer de
mémoire les règles de la SA ou de la SARL (par exemple quinze jours de convocation). Une seule limite
relevée : une clause ne peut pas permettre d'adopter une décision sans la majorité des voix exprimées
(Cass., ass. plén., 15/11/2024, n° 23-16.670, relevée par identifiant, arrêt non relu). L'outil demande
donc la clause lue dans les statuts ; sans elle, il rend tous les cas usuels.

**En SARL, la règle relevée est la règle ordinaire.** Pour les décisions ordinaires (L223-29) : en première
consultation, plus de la moitié de toutes les parts ; à défaut, seconde consultation à la majorité des
votes émis, sauf clause statutaire contraire. Ce que la fiche n'a **pas** relevé : quel type de décision
relève de cette majorité et lesquelles exigent une majorité renforcée. L'outil ne devine pas : il rend
la règle ordinaire en référence, tous les cas, et calcule exactement dès qu'on lui donne la majorité lue
dans l'article de ce type de décision ou dans les statuts.

**Trois façons de décider, mais pas trois règles relevées.** Assemblée (en SARL : convocation de chaque
associé au moins quinze jours avant, par lettre recommandée ; courriel seulement avec l'accord écrit
de l'associé, au moins vingt jours avant), consultation écrite, acte unanime. Relevé : l'assemblée en
SARL, et le fait que la loi ouvre en SARL d'autres modalités que l'assemblée depuis L223-27 (version du
14/09/2024), sans que leurs conditions soient relevées. En SAS, ce sont les statuts qui disent.

**Voix exprimées, présentes, totales : trois bases différentes.** « Majorité des voix exprimées » écarte
les abstentions ; « des voix présentes ou représentées » les compte ; « de toutes les voix » compte aussi
les absents. Le même vote peut réussir sur une base et échouer sur une autre : l'outil calcule les trois
et dit laquelle la clause vise. « Plus de la moitié » est strict ; « au moins deux tiers » ou « trois
quarts » ne l'est pas : à l'égalité exacte, la décision passe.

**Le procès-verbal.** En SARL et EURL, établi et signé conformément à R.223-24, puis inscrit au registre des
décisions (R.223-26) : coté et paraphé sur papier, ou électronique avec signature avancée et horodatage.
En SAS, établi conformément aux statuts, il retrace les décisions, les votes et les incidents pertinents ;
R.225-106 (SA) ne s'y applique pas directement. La liste des mentions de R.223-24 n'est pas relevée article
par article : les mentions de trame (société, date et lieu, associés et voix, résolution, résultat du
vote, signature) sont d'usage et à confirmer sur le texte.

## Pièges fréquents

- **Appliquer la majorité de la SARL ou de la SA à une SAS** sans avoir lu les statuts.
- **Confondre les bases** : compter les abstentions dans les voix exprimées, ou les absents dans les voix
  présentes.
- **Écrire « adoptée » avant d'avoir calculé** : le résultat se déduit du vote et de la clause, pas
  l'inverse.
- **Une clause de statuts sous la majorité des voix exprimées** : non fiable en SAS ; la faire relire.
- **Convoquer trop tard** en SARL : quinze jours avant l'assemblée, lettre recommandée.
- **Choisir un mode de décision que les statuts n'ouvrent pas** (consultation écrite, acte unanime en SAS).
- **Un « acte unanime » avec un seul associé contre** ou absent.
- **Recopier le PV de la dernière décision** sans changer date, voix, résolution.
- **Oublier le registre des décisions**, y compris pour l'associé unique.
- **Croire les formalités connues** : publicité, greffe, pièces et délais d'un transfert de siège, d'un
  changement de dirigeant ou d'une augmentation de capital ne sont pas relevés ici (voir plus bas).

## Méthodes proposées (jamais imposées)

1. **Décision en cinq questions** : qui décide et sous quelle forme, comment (mode), à quelle majorité
   (lue où), quel vote et quel PV, quelles suites. Détails : `methode-decision-en-cinq-questions`.
2. **Relecture d'un procès-verbal de décision** : contrôler un PV déjà écrit contre les faits et le calcul.
   Détails : `methode-relecture-pv`.

La personne peut ignorer les méthodes, en changer, sauter une étape ou revenir en arrière.

## Contrat de réponse (3 règles fixes)

1. Toute règle ou tout chiffre affirmé vient avec sa **source datée** (l'outil la donne).
2. **Ne jamais inventer** : dire ce qui manque ou ce qui est incertain, en particulier la majorité de
   chaque type de décision en SARL, les statuts en SAS et les formalités de publicité.
3. **Prévenir** quand une règle vient de changer (champ `prudence` de l'outil).

« Plan d'action d'abord », « deux questions au maximum » et l'ordre des étapes sont de bonnes habitudes
quand la personne veut agir, pas des obligations.

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
| `decision_associes` (nom servi : `orizon_decision_associes`) | Majorité requise et atteinte d'après les voix (entiers exacts, les trois bases), modes de décision, mentions du PV, formalités relevées, projet de PV rempli, augmentation de capital chiffrée (capital après, titres nouveaux) ; entrées : forme, type de décision, société, associés avec parts et vote, `majorite_lue`, faits du type | La personne décide, veut savoir si un vote est acquis, ou veut le projet de PV |
| `article_texte` (nom servi : `orizon_article_texte`) | Lire à la demande le texte officiel d'un article sur Légifrance, à une date donnée | La majorité d'un type de décision en SARL n'est pas relevée : lire l'article puis donner `majorite_lue` à l'outil ; ou un texte vient de changer |
| `entreprise_profil` (nom servi : `orizon_entreprise_profil`) | Forme juridique, siège, dirigeants publiés d'après le SIREN | Pré-remplir la société ou vérifier le dirigeant actuel |

L'outil rend toujours la forme `resultat` / `regles` / `manquant` / `prudence` / `garanti`. Une entrée mal
nommée est dite, jamais ignorée en silence. Sans la clause de majorité, l'outil rend un tableau de tous les cas
(quatre seuils sur trois bases) et une synthèse « atteinte dans tous les cas / dans aucun » : la décision
n'est tranchée que si tous les cas concordent.

## Quatre usages

| Usage | Attitude | Outils |
| --- | --- | --- |
| Question simple (« qui décide en SASU ? ») | Répondre avec la règle et sa source, sans questionnaire | aucun ou `decision_associes` |
| Objectif précis (« nomme M. X président, voici les voix ») | Calculer, dire le mode, remplir le projet de PV, lister ce qui manque | `decision_associes`, `article_texte` |
| Suivre une méthode (« guide-moi ») | Proposer l'une des deux méthodes ; la personne choisit le rythme | selon l'étape |
| Explorer (« pourquoi une majorité renforcée ? ») | Conversation libre, faits justes et sourcés | outils seulement s'ils aident |

## Sans abonnement (« non garanti »)

Les connaissances, les pièges et les méthodes restent utiles. Les règles datées, les calculs exacts et les
cas de référence du moteur ne sont pas garantis : le dire, et indiquer `garanti: non`.

## Documents

Procès-verbal, décision de l'associé unique, convocation : toujours un **projet à relire**, jamais « prêt
à signer ». Le projet rempli par l'outil est une trame : le modèle de la personne rédige, chaque mention porte
sa règle quand elle est relevée, et les mentions d'usage sont signalées comme telles (« à compléter »,
« non relevée »). La société décide, signe, inscrit au registre et accomplit les formalités ; la fiche ne
signe, ne dépose et n'envoie rien.

## Ce qui n'est pas relevé

Majorité légale et quorum propres à chaque type de décision en SARL (nomination et révocation du gérant,
modification des statuts, transfert de siège, changement de dénomination ou d'objet, augmentation de capital) ;
conditions de la consultation écrite et de l'acte unanime en SARL ; liste des mentions de R.223-24 ; inscription
du PV au registre en SAS ; règles propres à la SASU pour les décisions autres que les comptes annuels ;
règles d'acceptation, d'incompatibilité et d'inscription d'un dirigeant ; règles de libération, de
constatation et de souscription d'une augmentation de capital ; formalités de publicité, de dépôt au greffe
et de modification du registre, pièces, délais et frais pour chacun des types de décision (seul le guichet
unique des formalités d'entreprises est relevé, comme guichet officiel du dépôt des comptes) ; conventions
réglementées liées à la décision. Pour chacun, lire le texte (`article_texte`) ou les statuts avant de
conclure, et le dire au client.

### Annexe : glossaire

# Glossaire

| Terme | Définition courte |
| --- | --- |
| Décision collective | Décision prise par les associés d'une SAS ou d'une SARL, dans la forme que les statuts ou la loi prévoient. |
| Décision de l'associé unique | Décision écrite de l'associé d'une SASU ou d'une EURL, répertoriée au registre des décisions. |
| Procès-verbal (PV) | Écrit qui constate une décision collective : société, date, associés, résolution, vote, signature. |
| Registre des décisions | Registre où sont inscrits les procès-verbaux et les décisions de l'associé unique. |
| Assemblée | Réunion des associés ; en SARL, convocation quinze jours avant par lettre recommandée. |
| Consultation écrite | Décision prise par échange d'écrits sans réunion, si la loi ou les statuts l'admettent. |
| Acte unanime | Acte signé par tous les associés, sans réunion, quand il est admis. |
| Voix exprimées | Voix « pour » et « contre » ; les abstentions n'y comptent pas. |
| Voix présentes ou représentées | Voix des associés présents ou représentés, abstentions comprises. |
| Voix totales | Toutes les voix de la société, absents et abstentions comptés. |
| Majorité | Seuil de voix « pour » nécessaire, sur une base donnée ; « plus de » est strict, « au moins » ne l'est pas. |
| Première et seconde consultation (SARL) | Si la majorité ordinaire n'est pas atteinte à la première, la seconde statue à la majorité des votes émis, sauf clause contraire. |
| Majorité lue | Majorité que la personne a lue dans les statuts ou dans l'article de loi, donnée à l'outil. |
| Augmentation de capital simple | Ici : hausse du capital d'un montant fixé, en titres de valeur nominale connue, sans opération complexe. |

### Annexe : liens-ressources

# Ressources : décisions d'associés et procès-verbal

Pays : France, SAS, SASU, SARL, EURL. Les règles datées sont celles de « vie de la société » d'OriginSkill : chaque
calcul cite l'article, son lien et la date du dernier relevé. Cette page donne les liens utiles et les
pièces à demander ; elle ne remplace pas la règle citée par l'outil.

## Pièces à demander au client

- Les statuts à jour (forme des décisions collectives, quorum, majorité, modes de décision, article sur le
  siège, la dénomination, l'objet et le capital).
- Le registre des mouvements de titres ou la liste des associés, avec parts ou actions et voix.
- Un extrait d'immatriculation récent (dénomination, forme, capital, siège, dirigeants).
- Le dernier procès-verbal ou la dernière décision, et le registre des décisions.
- Le projet précis : qui est nommé ou révoqué, le nouveau siège, la nouvelle dénomination ou le nouvel objet,
  le montant et la valeur nominale de l'augmentation.
- Le pacte d'associés éventuel (clauses de décision, d'agrément ou de préemption).

## Textes relevés

- SAS et SASU : Code de commerce L227-9 (décisions collectives selon les statuts ; associé unique de SASU).
- SARL et EURL : L223-29 (majorité ordinaire), L223-31 (associé unique), L223-27 (modalités de consultation),
  R223-20 (convocation), R223-20-1 (télécommunication), R223-24 (procès-verbal), R223-26 (registre).
- Service-Public, décisions en SARL et EURL (F36714), en SASU (F39283) ; procès-verbal de SAS (F36625).
- Légifrance : https://www.legifrance.gouv.fr
- Guichet unique des formalités d'entreprises : https://formalites.entreprises.gouv.fr (relevé comme guichet
  officiel du dépôt des comptes ; usage pour les modifications non relevé).

## Cas particuliers

Dissolution, fusion, cession de titres, réduction du capital, opération sur valeurs mobilières, société en
difficulté, litige entre associés : hors de cette fiche ; orienter vers un avocat ou un expert-comptable.

### Annexe : methode-decision-en-cinq-questions

# Méthode : une décision d'associés en cinq questions

La structure est la nôtre ; les règles et leurs dates viennent de l'outil et de la fiche « règles datées ».
Aucune promesse de résultat : la méthode réduit les oublis, elle ne remplace ni les statuts, ni le texte
de l'article du type de décision, ni un juriste.

1. **Qui décide, sous quelle forme ?** SASU ou EURL : l'associé unique, par décision écrite répertoriée au
   registre, sans vote. SAS ou SARL : les associés, collectivement. Noter la forme exacte et le nombre
   d'associés ; un « associé unique » avec plusieurs associés dans la liste est une erreur de forme.
2. **Comment (mode) ?** Assemblée, consultation écrite ou acte unanime. En SARL, l'assemblée est relevée
   (convocation quinze jours avant, lettre recommandée) ; les autres modalités sont ouvertes mais leurs
   conditions ne sont pas relevées : lire L223-27 dans le texte de la loi. En SAS, lire les modes de décision prévus par
   les statuts.
3. **À quelle majorité, lue où ?** SAS : la clause des statuts (règle, base, source). SARL : lire l'article
   du type de décision (ou la clause renforcée des statuts) et la donner à l'outil ; sans elle, l'outil
   rend la règle ordinaire en référence et tous les cas. Toujours dire la **base** (voix exprimées,
   présentes ou totales).
4. **Quel vote, quel procès-verbal ?** Associés, parts, voix et sens du vote de chacun ; l'outil calcule les
   voix requises et l'atteinte, puis remplit le projet de PV. Relire les mentions marquées « à compléter »
   et confirmer les mentions d'usage sur le texte (R.223-24 en SARL, statuts en SAS).
5. **Quelles suites ?** Signature, inscription au registre des décisions (relevé), puis les formalités de
   publicité et de greffe de ce type de décision : **non relevées** ici, à lire avant d'agir.

Exemple : SAS, trois associés (600, 300 et 100 actions), statuts « deux tiers des voix exprimées »,
nomination d'un président. Vote : 600 pour, 300 contre, 100 abstentions. Voix exprimées : 900 ; deux tiers de
900 = 600 : la majorité est atteinte à l'égalité exacte. Sur toutes les voix (1 000), il en aurait fallu 667 :
la base compte autant que le seuil.

Approche concurrente : le **modèle de PV en ligne** rempli par formulaire. Il aligne les mentions d'un type
de décision, mais ne lit ni les statuts, ni la base de calcul de la majorité, et ne dit pas ce qui reste à
faire au greffe.

### Annexe : methode-relecture-pv

# Méthode : relire un procès-verbal de décision

À utiliser quand un PV ou une décision de l'associé unique existe déjà et qu'on veut savoir s'il tient.
Contrôle de cohérence, pas garantie de validité : un juriste tranche les cas douteux.

1. **Identifier la société et la forme** : dénomination, forme, capital, siège, immatriculation ; comparer
   avec les faits connus (`entreprise_profil`). Un PV recopié garde souvent l'ancien siège ou l'ancien capital.
2. **Vérifier qui a décidé** : associé unique (décision écrite, pas de vote) ou associés (liste, parts,
   voix). Le total des voix du PV doit redonner le capital réparti entre les associés.
3. **Refaire le calcul** avec `decision_associes` : mêmes voix, même clause de majorité, même base. Si le PV
   dit « adoptée » et que le calcul dit l'inverse, c'est le premier point à corriger.
4. **Contrôler le mode et la forme** : assemblée (convocation en SARL quinze jours avant), consultation
   écrite ou acte unanime ; en SAS, le mode est-il prévu par les statuts ? Un acte « unanime » avec un
   associé contre ou absent n'en est pas un.
5. **Contrôler la résolution** : le texte dit-il exactement ce qui est décidé (qui, quoi, à compter de
   quand) et cite-t-il l'article des statuts modifié quand la décision les modifie ?
6. **Contrôler les mentions et le registre** : signature ; inscription au registre des décisions (relevée) ;
   mentions d'usage confirmées sur R.223-24 (SARL) ou les statuts (SAS).
7. **Lister ce qui reste** : formalités de publicité et de greffe du type de décision, non relevées ici.

Exemple : un PV de SARL nomme un gérant à « la majorité » avec 45 parts pour sur 100 et 30 contre, 25 absents.
Si la décision relève de la majorité ordinaire (à confirmer sur l'article du type de décision, non relevé),
la règle relevée (première consultation) exige plus de la moitié de toutes les parts, soit 51 : non atteinte ; une seconde consultation à la majorité des votes émis (75 votes émis, 38 requis) aurait pu
la passer, sauf clause contraire des statuts. Le PV ne doit pas dire « adoptée » sans cela.

### Annexe : regles-majorite-et-pv

# Règles datées : majorité, mode de décision, procès-verbal

Textes relevés sur Légifrance (ou fiche Service-Public) et repris ici sans texte nouveau. La colonne
« Relevé le » est la date à citer quand on donne la règle : **règle vérifiée le JJ/MM/AAAA ; à reconfirmer
avant d'agir si l'enjeu est important**. Pour un texte suivi par la veille, la date est celle du dernier
relevé Légifrance ; pour les autres, celle de la consultation d'origine. Les règles marquées « à recouper »
n'ont pas deux sources indépendantes : le dire.

| Identifiant | Règle | Article | En vigueur depuis | Relevé le | Statut | Lien |
| --- | --- | --- | --- | --- | --- | --- |
| `majorite-sarl-ago` | SARL, décisions ordinaires : sans quorum, plus de la moitié de toutes les parts en première consultation ; à défaut, seconde consultation à la majorité des votes émis, sauf clause statutaire contraire | L223-29 | 21/07/2019 | 03/10/2026 | recoupée | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000038799356 |
| `convocation-sarl` | SARL, assemblée : chaque associé convoqué au moins 15 jours avant, par lettre recommandée ; courriel avec l'accord écrit de l'associé, au moins 20 jours avant | R223-20 | 01/04/2018 | 03/10/2026 | recoupée | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000036665390 |
| `sas-decisions-collectives-statuts` | SAS : forme, quorum et majorité des décisions collectives fixés par les statuts ; plancher de la majorité des voix exprimées (Cass., ass. plén., 15/11/2024, n° 23-16.670, arrêt non relu) | L227-9 | 01/10/2025 | 03/10/2026 | à recouper | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000051322706 |
| `associe-unique-decision-registre` | EURL et SASU : l'associé unique décide seul, par décision écrite répertoriée au registre des décisions | L223-31 (EURL), L227-9 (SASU) | 06/08/2008 | 03/10/2026 | recoupée | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000019291719 |
| `sarl-pv-registre` | SARL et EURL : procès-verbal établi et signé (R.223-24), inscrit au registre des décisions, coté et paraphé ou électronique avec signature avancée et horodatage (R.223-26) ; liste des mentions non relevée | R223-24, R223-26 | 28/02/2009 | 03/10/2026 | recoupée | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000020316738 |
| `sas-pv-statuts` | SAS : procès-verbal conforme aux statuts, décisions, votes et incidents pertinents ; R.225-106 (SA) non applicable directement ; registre à confirmer | F36625 (Service-Public, vérifiée le 08/10/2025) | inconnue | 29/07/2026 | à recouper | https://entreprendre.service-public.gouv.fr/vosdroits/F36625 |
| `sarl-modalites-consultation` | SARL : autres modalités de consultation que l'assemblée ouvertes par la loi, conditions non relevées ; télécommunication : identification, voix, retransmission continue et simultanée | L223-27, R223-20-1 | 14/09/2024 | 03/10/2026 | à recouper | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000049720548 |

Précisions :

- **Base et seuil.** « Plus de la moitié » est strict ; « deux tiers », « trois quarts », « unanimité » se
  comptent « au moins ». L'outil calcule en entiers exacts, sur trois bases (voix exprimées, présentes,
  totales), jamais en flottant.
- **SARL.** Seule la règle ordinaire est relevée. Le rattachement d'un type de décision à cette règle (ou à
  une majorité renforcée) ne l'est pas : lire l'article du type de décision.
- **SAS.** Sans statuts, aucune majorité, aucun quorum, aucun mode de consultation ne se déterminent ;
  ne pas importer la règle de la SA ou de la SARL.
- **Source de la SAS et du PV de SAS.** L'identifiant de l'arrêt et la fiche F36625 viennent du corpus des
  assemblées gelé le 29/07/2026 ; l'arrêt et la fiche n'ont pas été relus pour cette fiche.

Exemple : SARL, 60 parts pour et 40 contre sur 100. Première consultation ordinaire : plus de la moitié de 100,
soit 51 : atteinte. Avec une majorité renforcée lue à trois quarts (75), non atteinte.

## Aller plus loin avec OriginSkill

Ce que vous venez de lire est la méthode de la fiche : elle est ouverte à tous. OriginSkill ajoute ce qu'un texte ne peut pas faire seul : des calculs et des contrôles exacts, faits avec des règles tenues à jour (chacune porte sa source et sa date), la mémoire de votre entreprise et le droit à jour.

### Les calculs de cette fiche

Ces calculs sont inclus dans l'abonnement. OriginSkill les fait pour vous, avec des règles à jour et sourcées, et la réponse est garantie.

- **Lire le texte officiel d'un article de loi** (outil `orizon_article_texte`) : Va chercher, au moment de la question, le texte officiel d'un article de loi sur le site de l'État, tel qu'il est en vigueur à la date voulue.
- **Retrouver la fiche d'une entreprise avec son numéro SIREN** (outil `orizon_entreprise_profil`) : Rend ce que les registres publics disent d'une entreprise : nom, forme juridique, activité, effectif, adresse du siège, dirigeants publiés, entreprise en activité ou fermée.
- **Prendre une décision d'associés hors approbation des comptes** (outil `orizon_decision_associes`) : Pour une décision comme la nomination d'un dirigeant, un transfert de siège ou une augmentation de capital : majorité, formalités et délais selon la forme de la société.

### Avec l'abonnement, en plus

- **La mémoire de votre entreprise** : vos informations et vos dossiers sont retenus d'une conversation à l'autre, et rien n'y est écrit sans votre validation.
- **Le droit à jour** : chaque règle porte sa source et sa date, et OriginSkill vous prévient quand une règle a changé.

### Brancher OriginSkill à votre assistant

Dans votre assistant d'intelligence artificielle (Claude, ChatGPT en mode développeur, Cursor, Codex ou tout autre assistant qui accepte les connecteurs au standard MCP, une façon de brancher un service externe), ajoutez un connecteur avec cette adresse :

    https://api.originskill.ai/mcp

Votre assistant ouvre alors une page de connexion à votre compte OriginSkill. Les étapes détaillées sont ici : https://originskill.ai/installer

### Tarif

Offres et abonnement : https://originskill.ai/tarif

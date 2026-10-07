---
name: premiere-embauche-fr-originlabs-app
title: Embaucher mon premier salarié
description: 'Embaucher mon premier salarié. Méthode professionnelle française, avec ses pièges et ses questions à poser. À utiliser quand : Un créateur va signer son premier contrat de travail, en CDI ou en CDD, et veut la liste datée de ce ; Une question précise : « quand faire la déclaration d''embauche ? », « quelle période d''essai pour un ; Le salarié est déjà arrivé et le créateur se demande ce qu''il a oublié.'
author: originlabs-app
author_url: https://github.com/originlabs-app/origin-skill-install/tree/main/skills/premiere-embauche-fr
license: CC-BY-4.0
version: 0.1.0
execution_mode: open
jurisdiction: fr
practice: employment
language: fr
---

> **Version gratuite : règles datées entre le 03/09/2026 et le 03/10/2026.** Les règles changent (SMIC, TVA, seuils…). Avec l'abonnement OriginSkill, votre assistant reçoit la règle à jour, avec sa source et sa date.

# Embaucher mon premier salarié

Une seule tâche : savoir quoi faire, et avant quelle date, pour que le premier contrat de travail démarre
en règle. Tout part d'un seul fait, le **premier jour de travail**. Le reste se calcule (fenêtre de la
DPAE, fin d'essai, visite médicale, première DSN), se vérifie (complémentaire santé, registre, affichages)
ou se lit (convention collective).

## Quand l'utiliser

- Un créateur va signer son premier contrat de travail, en CDI ou en CDD, et veut la liste datée de ce
  qu'il doit faire avant, le jour de l'arrivée et après.
- Une question précise : « quand faire la déclaration d'embauche ? », « quelle période d'essai pour un
  cadre, pour un employé ? », « dois-je affilier mon salarié à une mutuelle dès le premier jour ? », « quand
  envoyer ma première déclaration sociale (DSN) ? », « quand faire passer la visite médicale ? ».
- Le salarié est déjà arrivé et le créateur se demande ce qu'il a oublié.
- Un doute sur un fait qui change le plan : la convention collective, la catégorie du salarié, l'effectif.

Quand **ne pas** l'utiliser : rédiger ou relire le contrat, ses clauses et le salaire minimum (fiche
`contrat-travail-fr`) ; la fin d'un CDD (fiche `cdd-fr`) ; rompre un essai (fiche
`rupture-periode-essai-fr`) ; le calendrier annuel de toutes les obligations (fiche
`calendrier-obligations-fr`) ; l'apprentissage, le contrat de professionnalisation, l'intérim, le
stagiaire, le particulier employeur, la fonction publique ; le salarié étranger hors Union européenne
(autorisation de travail à vérifier auprès de la préfecture) ; la situation du dirigeant lui-même.

## Les faits qui décident du plan

Sept faits décident du plan. Les connaître, sinon donner le plan pour ce que l'on sait (les plafonds des
trois catégories, les délais en durée) et poser la question de ce qui manque **en fin de réponse**.

- **Le premier jour de travail** (la prise effective du poste) : il ancre toutes les dates. Sans lui, les
  délais sont donnés en durée, pas en date.
- **Le type de contrat** : CDI par défaut ; un CDD a son propre plafond d'essai et sa durée en jours.
- **La catégorie du salarié** : ouvrier ou employé, agent de maîtrise ou technicien, cadre. Elle fixe la
  durée maximale de l'essai.
- **La convention collective** : elle peut prévoir un essai plus court, des garanties de santé plus
  élevées, un préavis plus long, un salaire minimum. C'est la question la plus discriminante.
- **L'effectif après l'embauche** : 1 pour un premier salarié ; à 50 salariés et plus, le jour de la DSN
  dépend du décalage de paie.
- **La durée d'essai prévue au contrat**, renouvellement non compris.
- **La date de la première paie** : elle dit si la première DSN est celle du mois de l'embauche ou d'un
  mois suivant (sans elle, les deux hypothèses sont rendues).
- **La zone** du lieu de travail (métropole, Alsace-Moselle, outre-mer) : elle décale une date qui tombe un
  jour férié propre à la zone.

### Faits de la mémoire d'entreprise consommés

Quand la mémoire d'entreprise est branchée, ces faits servent sans être redemandés ; un fait donné dans la
conversation prime sur la mémoire, et un fait mémorisé est à confirmer.

| Fait mémorisé | Sert à |
| --- | --- |
| `effectif` | Jour d'échéance de la DSN (le 15, ou le 5 à 50 salariés et plus sans décalage) et seuil de 50. Après l'embauche, sa mise à jour (validation humaine) change les seuils suivants. |
| `convention_collective` | Lire l'essai, la santé, le préavis ; fournie à l'outil de plan (`convention_collective`). |
| `activite` | Retrouver la convention collective : c'est l'activité principale qui décide, pas le code APE seul. |
| `forme_juridique` | Situer l'entreprise (SAS, SASU, SARL, EURL, EI, autre) ; le dirigeant n'est pas le salarié dont il s'agit ici. |
| `zone_geographique` | Zone des jours fériés quand le lieu de travail est en Alsace-Moselle ou outre-mer. |
| `denomination` et `siren` | Retrouver la convention collective par le numéro SIREN et remplir la DPAE (SIRET). |

Aucun agent n'écrit en mémoire sans validation humaine : proposer de mettre à jour `effectif` et
`convention_collective` après l'embauche, jamais de le faire seul.

## Connaissances du métier

**La réponse courte.** Un premier salarié, ce sont une douzaine d'échéances qui partent d'un seul jour.
Trois se jouent **avant l'arrivée** : la DPAE (au plus tôt huit jours avant, au plus tard avant la prise de
poste), la complémentaire santé collective (due dès le premier jour) et l'essai écrit dans le contrat. Les
autres suivent : informations écrites à 7 jours et à 1 mois, visite d'information et de prévention dans les
3 mois, entretien de parcours professionnel dans la première année, première DSN le mois suivant.

**Avant le premier jour.**

- *Convention collective.* C'est celle de l'activité principale exercée par l'employeur (article L2261-2 du
  Code du travail) ; le code APE donne une piste, pas la décision. Elle se mentionne dans les informations
  remises au salarié et sur le bulletin de paie (article R3243-1). Une entreprise qui n'a encore jamais
  déclaré de salarié peut ne pas figurer dans les fichiers publics des conventions, qui viennent des
  déclarations sociales : la convention se déduit alors de l'activité et se vérifie sur le champ
  d'application du texte.
- *Service de prévention et de santé au travail.* Les employeurs organisent un service de prévention et de
  santé au travail (article L4622-1) ; une petite entreprise adhère à un service interentreprises. Ses
  coordonnées figurent dans la DPAE, qui déclenche aussi la demande de visite d'information et de
  prévention.
- *Complémentaire santé.* Tout employeur du secteur privé fait bénéficier ses salariés d'une couverture
  collective à adhésion obligatoire, quelle que soit leur ancienneté : cotisation financée au moins pour
  moitié par l'employeur, garanties au moins égales au panier de soins minimal (article L911-7 du Code de la
  sécurité sociale ; Service Public, page vérifiée le 20/01/2026). Une convention de branche peut imposer
  plus. Un salarié peut demander à être dispensé dans des cas listés (CDD ou mission de moins de 3 mois,
  temps partiel jusqu'à 15 heures par semaine, déjà couvert par ailleurs), avec justificatif : la dispense
  ne se présume pas. Sans contrat collectif, il se met en place par accord collectif ou, à défaut, par
  décision unilatérale de l'employeur, avec information écrite des salariés.
- *Affichages.* Coordonnées de l'inspection du travail (et nom de l'inspecteur), du médecin du travail ou du
  service de santé au travail et des secours d'urgence (article D4711-1) ; horaire collectif affiché dans
  chaque lieu de travail (article D3171-2) ; consignes d'incendie affichées de façon très apparente
  (article R4227-37) ; avis indiquant où consulter le document unique (article R4121-4) ; intitulé de la
  convention collective et lieu où la consulter ; textes sur l'égalité de rémunération ; information sur le
  harcèlement sexuel. La liste complète varie avec l'effectif : la page Service Public sur les obligations
  d'affichage fait foi.
- *Document unique d'évaluation des risques (DUERP).* Obligatoire **dès le premier salarié**, sans seuil
  d'effectif : l'employeur évalue les risques pour la santé et la sécurité (article L4121-3) et en transcrit
  les résultats dans un document unique qui inventorie les risques de chaque unité de travail (article
  R4121-1). Mise à jour au moins chaque année à partir de onze salariés, et dans toute entreprise à chaque
  aménagement important ou information nouvelle sur un risque (article R4121-2) ; liste d'actions de
  prévention (programme annuel à partir de 50 salariés) ; versions conservées au moins quarante ans
  (article L4121-3-1) ; tenu à la disposition des salariés (article R4121-4). Pas de délai légal propre
  avant l'arrivée : le plan le place en repère à la date d'embauche. Défaut de transcription ou de mise à
  jour : amende des contraventions de cinquième classe (article R4741-1). **Ces articles sont vus en
  recherche Légifrance le 02/10/2026 et non relus en ligne à ce jour : la réponse n'est pas garantie sur ce
  point.** Le calendrier du dépôt dématérialisé prévu par la loi du 2 août 2021 n'est pas relevé.
- *DPAE.* Elle se fait à l'Urssaf (en ligne) avant la prise de fonction ou le début de l'essai, **au plus
  tôt dans les 8 jours précédant l'embauche** (article R1221-4). Elle contient notamment le SIRET, le code
  APE, les coordonnées du service de santé au travail, l'identité du salarié, la date et l'heure
  d'embauche, la nature et la durée du contrat et de l'essai. Sans numéro de sécurité sociale, un numéro
  technique temporaire est établi. Une copie ou l'accusé de réception est remis au salarié (obligation
  remplie si le contrat écrit nomme l'organisme destinataire). Elle permet aussi l'immatriculation de
  l'employeur et du salarié, l'affiliation à l'assurance chômage et aux retraites complémentaires, et la
  demande de visite d'information et de prévention. Absence de DPAE (Service Public, page vérifiée le
  01/06/2026) : régularisation des cotisations par l'Urssaf, pénalité administrative de 1 305 € par
  salarié, amende de 1 500 € (contravention de 5e classe), et délit de travail dissimulé si l'omission est
  intentionnelle.
- *Essai écrit.* La période d'essai n'existe que si elle est écrite, renouvellement compris (article
  L1221-23).

**Le jour de l'arrivée.** Le salarié est inscrit sur le **registre unique du personnel**, obligatoire dès
le premier salarié (article L1221-13). Ses mentions et sa conservation sont fixées par les articles D1221-23
à D1221-27, vus en recherche et non relus ici.

**Après l'arrivée.**

- *Informations écrites.* Au plus tard le 7e jour calendaire : identité des parties, lieu de travail,
  poste, date d'embauche, essai, rémunération, durée du travail, heures supplémentaires. Au plus tard un
  mois après : droit à la formation, congés payés, procédure de rupture, convention collective et accords
  applicables, régimes de retraite et de prévoyance, contrats de santé et de prévoyance (article R1221-35).
  À l'embauche, le salarié est aussi informé de son entretien de parcours professionnel.
- *Visite d'information et de prévention.* Dans un délai qui n'excède pas **trois mois à compter de la
  prise effective du poste** (article R4624-10). Pour un poste à risques particuliers, un examen médical
  d'aptitude précède l'affectation. Ne pas organiser les examens médicaux d'embauche : amende de 1 500 €
  (Service Public, page vérifiée le 01/06/2026).
- *Entretien de parcours professionnel.* Au cours de la première année suivant l'embauche, puis tous les
  quatre ans (article L6315-1, version du 31/12/2025). Il ne porte pas sur l'évaluation du travail.
- *Première DSN.* La DSN du mois de l'embauche, si la première paie est versée dans ce mois : au plus tard
  **le 15 du mois suivant** pour un employeur de moins de 50 salariés ; à 50 salariés et plus, le 5 sans
  décalage de paie, le 15 avec décalage (article R243-6 du Code de la sécurité sociale). Les cotisations se
  paient à la même échéance. Une échéance qui tombe un samedi, un dimanche ou un jour férié est lue au jour
  ouvré suivant : report rapporté par des sources secondaires, non relu sur les sites officiels. La
  première DPAE crée l'espace employeur Urssaf ; le dispositif simplifié TESE intègre la DPAE pour
  l'employeur qui l'utilise (Service Public).

**La période d'essai d'un CDI.**

| Catégorie | Essai initial au plus | Avec renouvellement au plus |
| --- | --- | --- |
| Ouvrier ou employé | 2 mois | 4 mois |
| Agent de maîtrise ou technicien | 3 mois | 6 mois |
| Cadre | 4 mois | 8 mois |

Ces durées sont **impératives** : une convention collective ou le contrat peut prévoir plus court, jamais
plus long (article L1221-22). Le renouvellement est possible **une seule fois**, seulement si un accord de
branche étendu le prévoit et si le contrat l'écrit (article L1221-21). Un stage de fin d'études suivi d'une
embauche dans les trois mois, ou un CDD précédent, se déduit de l'essai. La fin se compte de quantième à
quantième : 4 mois depuis le 02/11/2026 finissent le 01/03/2027 à minuit. L'essai d'un CDD a son plafond :
un jour par semaine entière de contrat, sans dépasser deux semaines (14 jours) si le CDD dure six mois au
plus, ni **un mois** dans les autres cas (article L1242-10). Le plafond est le plus petit des deux : un CDD
de 27 semaines donne 27 jours (un jour par semaine), pas 30 ; « un mois » n'est pas un nombre de jours fixe,
il se compte de quantième à quantième depuis l'embauche (28 à 31 jours), comme la fin d'un essai de CDI.

**Ce que le calcul apporte que le texte seul ne donne pas.** Une embauche le lundi 02/11/2026 place
l'ouverture de la DPAE le dimanche 25/10, les informations écrites le dimanche 08/11 (viser le vendredi
06/11) et le 02/12, la première DSN le mardi 15/12, la visite avant le 02/02/2027 et, pour un cadre à
4 mois d'essai, la fin d'essai le 01/03/2027. Une embauche le jeudi 01/10/2026 place la première DSN un
dimanche 15/11, lue au lundi 16/11, et la date limite du mois de l'embauche au 01/11 (dimanche et jour de
la Toussaint). Ces décalages, ces fériés et ces fins d'essai ne se tiennent pas de tête.

## Pièges fréquents

- **DPAE trop tôt ou trop tard.** Plus de 8 jours avant l'embauche, elle n'est pas possible ; après la prise
  de poste, elle est en retard et expose à une pénalité par salarié.
- **Croire la mutuelle facultative** ou qu'elle ne commence qu'après l'essai : elle est due dès le premier
  jour, sauf dispense demandée par le salarié et justifiée.
- **Un essai non écrit, trop long ou renouvelé sans accord de branche.** Il n'existe pas, ou il est
  raccourci : le contrat écrit doit le prévoir expressément.
- **Oublier de déduire un stage ou un CDD précédent** de la période d'essai.
- **Identifier la convention collective par le seul code APE.** C'est l'activité principale réelle qui
  décide ; une convention oubliée fait perdre un essai plus court, des garanties ou un préavis.
- **Oublier le registre du personnel** ou les affichages, que l'inspection du travail contrôle en premier.
- **Penser le document unique réservé aux grandes entreprises.** Il est dû dès le premier salarié, même
  seul ; seule la mise à jour annuelle dépend du seuil de onze salariés.
- **Confondre la DPAE et la DSN.** La DPAE précède l'embauche ; la DSN est mensuelle et commence le mois
  suivant la première paie.
- **Croire la DSN due le 5.** Sous 50 salariés, l'échéance est le 15 du mois suivant.
- **Compter le mois de l'embauche au lieu du mois de la première paie.** Si la première paie n'est versée que
  le mois suivant, la première DSN est celle du mois suivant.
- **Ne pas prévoir la visite d'information et de prévention** : le délai de trois mois court dès la prise
  effective du poste.
- **Traiter un repère comme une obligation légale.** Avant l'embauche, à l'arrivée du salarié : ce sont des
  repères de bonne pratique, pas des limites du texte ; seules les dates « légales » en sont.

## Méthodes proposées (jamais imposées)

1. **Le plan en trois temps** : avant le contrat, avant le premier jour, après l'arrivée. On pose le
   premier jour de travail, on fait calculer le plan, puis on déroule dans l'ordre, en commençant par la
   convention collective. Détails : `methode-trois-temps`.
2. **Lire la convention collective en quatre questions** : essai, santé et prévoyance, préavis et congés,
   salaire minimum et classification. Détails : `methode-lecture-convention`.

Elles ne se valent pas toujours : la première convient à qui n'a encore rien fait, la seconde à qui a déjà le
texte de la convention sous les yeux. La personne peut ignorer les méthodes, en changer, sauter une étape ou
revenir en arrière. Trois exemples datés et calculés : `exemples-calcules`.

## Contrat de réponse (3 règles fixes)

1. Toute règle ou tout chiffre affirmé vient avec sa **source datée** : le plan la donne pour chaque étape ;
   un texte non relu en ligne le dit (« texte non relu en ligne à ce jour »).
2. **Ne jamais inventer** : dire ce qui manque (convention collective, catégorie, durée d'essai, effectif) et
   ce qui n'est pas relevé (mentions du registre, liste complète des affichages, régimes particuliers de la
   visite médicale).
3. **Prévenir** quand une règle vient de changer (champ `prudence`).

« Plan d'action d'abord », « deux questions au maximum » et l'ordre des étapes sont de bonnes habitudes quand
la personne veut agir, pas des obligations.

**Restitution au dirigeant.**

1. Répondre d'abord, exactement, à la question posée et à rien d'autre : la règle ou le chiffre en une ou deux phrases, puis ce qui sert à cette question. Pas de tableau complet, pas de volet non demandé, aucun chiffre d'exemple inventé. Reprendre tels quels les chiffres de `en_clair.resultats`, sans les recalculer ; ne jamais affirmer qu'un point non fourni par le dirigeant est en règle.
2. Si un fait manque et change la réponse, donner la réponse pour chaque cas, puis poser une seule question à la fin : celle qui débloque. Aucune question si rien ne manque.
3. Parler en mots du dirigeant : jamais « l'outil », « le moteur », « le serveur », ni un code ou un champ technique (`entree_incomplete`, `manquant`, `prudence`) ; ne jamais recopier le mot « garanti » ni « non garanti ». Traduire : « il me manque la date d'embauche pour calculer… », « règle relevée le JJ/MM/AAAA, texte officiel pas encore relu ; à reconfirmer avant d'agir ». Écrire « vérifiée » seulement pour une règle marquée vérifiée (« règle vérifiée le JJ/MM/AAAA ; à reconfirmer avant d'agir si l'enjeu est important ») : une source citée n'est pas une vérification.
4. Une échéance qui tombe un samedi, un dimanche ou un jour férié se dit avec son report si les règles en donnent un, sinon « à vérifier ».
5. Ne jamais inventer un fait absent, ni pour appeler un outil. Une règle datée fournie par OriginSkill n'est jamais remplacée par une source secondaire trouvée en ligne ; en cas d'écart, donner les deux valeurs, leurs sources et leurs dates.

## Outils (description ouverte)

L'exécution exacte est servie par le connecteur, sur le moteur RH (`premiere_embauche_plan` reprend les
calculs d'embauche et d'essai de `delais_rh_calculer`) et sur le moteur des échéances sociales pour la DSN.

| Outil | Sert à | Appeler quand |
| --- | --- | --- |
| `premiere_embauche_plan` (nom servi : `orizon_premiere_embauche_plan`) | La liste datée de la première embauche à partir de la date d'embauche : convention collective, service de santé au travail, complémentaire santé, DPAE et sa fenêtre, affichages, document unique d'évaluation des risques (DUERP), registre, essai (plafond par catégorie, fin d'essai, plafond d'un CDD), informations au salarié, visite d'information et de prévention, entretien de parcours, première DSN | Dès qu'une date d'embauche est connue ou envisagée |
| `delais_rh_calculer` (calculs `embauche`, `essai`) | La prévenance d'une rupture d'essai et la fin d'essai d'une durée donnée | Pour aller plus loin que le plan, ou rompre l'essai |
| `situation_verifier` (bloc `essai`) | Contrôler une durée d'essai, son renouvellement et la déduction d'un stage ou d'un CDD précédent | Dès qu'un stage, un CDD précédent ou un renouvellement entre en jeu |
| `convention_collective` (nom servi : `orizon_convention_collective`) | L'IDCC par le SIREN ou un IDCC donné, et le texte daté d'une clause (essai, préavis) | Quand la convention est à identifier ou à lire |
| `convention_article` (nom servi : `orizon_convention_article`) | Lire dans LA convention collective du client (IDCC connu) le texte des articles d'un thème (`theme` : `periode_essai`, `preavis`, `indemnite_licenciement`, `rupture_conventionnelle`, `salaires_minima`, `duree_travail`, `conges`, `depart_retraite`, `maladie`), cité tel quel avec son identifiant KALIARTI, son numéro et sa date de version, jamais résumé comme une règle ; articles repérés par l'intitulé des sections, applicabilité non jugée (avenants, version à la date des faits, comparaison avec le Code du travail à faire avec le client) | Après `convention_collective`, quand une clause conventionnelle doit être lue. **Outil ouvert progressivement : il n'existe que s'il figure dans la liste `outils` rendue par `orizon_fiche` ; sinon, renvoyer vers le texte de la convention sur Légifrance (liste des IDCC) sans citer d'article de mémoire.** |
| `echeances_diverses` (`dsn_cotisations`, nom servi : `orizon_echeances_diverses`) | Les échéances mensuelles de la DSN suivantes | Après la première DSN |
| `article_texte` (nom servi : `orizon_article_texte`) | Lire le texte officiel d'un article cité | Quand la personne veut vérifier une règle |

Entrées de `premiere_embauche_plan` : `date_embauche` (AAAA-MM-JJ) ; facultatives `type_contrat` (`cdi` par
défaut ou `cdd`), `categorie` (`ouvrier_employe`, `agent_maitrise_technicien`, `cadre`),
`duree_contrat_jours` (CDD), `duree_essai_mois` (CDI) ou `duree_essai_jours` (CDD), `effectif` (1 par
défaut, dit comme hypothèse), `decalage_paie` (utile à 50 salariés et plus), `convention_collective`,
`poste_a_risques`, `zone` (`metropole`, `alsace-moselle`, `guadeloupe`, `martinique`, `guyane`, `la-reunion`, `mayotte` ; `alsace_moselle` et `la_reunion` avec un tiret bas sont acceptés et rangés sous le nom canonique), `date_premiere_paie` (date de versement de la première paie : elle fixe le mois de
la première DSN), `date_reference` (date du jour du plan). Une entrée non comprise, ou comprise mais sans
effet (décalage de paie sous 50 salariés, catégorie donnée pour un CDD, durée de contrat donnée pour un CDI),
est dite dans `manquant`, jamais ignorée en silence ; la zone donnée est rendue dans `resultat.zone_appliquee`
avec les dates qu'elle touche (ou la mention qu'elle n'en touche aucune).

Lire la réponse : `resultat.reponse` porte la synthèse en quelques phrases **et la liste numérotée de toutes les étapes avec leur date** (c'est le texte que lisent les clients qui n'affichent pas `structuredContent`) ; `resultat.etapes` liste les
étapes par ordre de date, chacune avec sa `date_limite`, sa `nature_de_la_date` (`legale`, `calculee` ou
`repere`), son `statut` (à venir, à faire maintenant, dernier jour, date passée), ses `sources` et ce qu'il
y a à faire ; `resultat.essai` donne le plafond de chaque catégorie et la fin d'essai (si la durée stipulée dépasse le plafond légal, `depasse_le_plafond` est vrai et `resultat.reponse` commence par dire que la date de fin n'est pas valable : ne jamais la reprendre comme une date à inscrire au contrat) ; `resultat.dsn` donne
la première DSN dans les deux hypothèses de paie ; `hypotheses` se dit, `manquant` devient la question à
poser, `prudence` se dit une fois. Chaque appel répond sous la forme unique `resultat` / `regles` /
`manquant` / `prudence` / `garanti`.

Le plan calcule des dates et un ordre ; il ne rédige aucun contrat, ne déclare rien à l'Urssaf et n'envoie
rien. La DPAE, le contrat, l'adhésion et l'inscription au registre restent à la personne.

## Quatre usages

| Usage | Attitude | Outils |
| --- | --- | --- |
| Question simple (« quelle période d'essai pour un cadre ? ») | Répondre avec la règle et sa source ; donner les trois catégories si elle manque | `premiere_embauche_plan` si une date est donnée |
| Objectif précis (« j'embauche le 2 novembre, que dois-je faire ? ») | Appeler le plan tout de suite, rendre la réponse d'abord (ce qui est à faire maintenant, les dates clés), puis les étapes ; poser la question de la convention en fin de réponse | `premiere_embauche_plan` |
| Suivre une méthode (« guide-moi pour embaucher ») | Proposer l'une des deux méthodes ; la personne choisit le rythme | selon l'étape |
| Explorer (« quelle différence entre DPAE et DSN ? ») | Conversation libre, faits justes et sourcés, sans trancher à sa place | outils seulement s'ils aident |

## Sans abonnement (« non garanti »)

Les connaissances, les pièges et les méthodes restent utiles. Les dates calculées par le plan et les règles
datées ne sont pas garanties : le dire, et indiquer `garanti: non`.

## Documents

Contrat de travail, lettre d'engagement, DPAE, registre, affiches : la fiche n'en produit aucun et ne
télécharge rien. Le modèle de la personne peut rédiger un brouillon de contrat à partir des faits du
dossier, toujours un **projet à relire** par l'employeur, et par un juriste dès qu'une clause sensible
apparaît. La DPAE se fait par l'employeur sur le site de l'Urssaf ou sur net-entreprises.

## Ce qui n'est pas relevé

Les mentions du registre unique du personnel, sa conservation et sa tenue à disposition (articles D1221-23 à
D1221-27) ; la liste complète des affichages selon l'effectif ; les régimes particuliers de la visite
d'information et de prévention (travail de nuit, jeunes travailleurs, apprentis) et de l'examen d'aptitude
des postes à risques ; les décrets de dispense de la complémentaire santé, le versement santé des contrats
courts et le panier de soins chiffré ; l'adhésion à un service interentreprises et son délai ; le contenu
de l'inventaire des risques du document unique (propre à chaque métier) et le calendrier de son dépôt dématérialisé ;
la retraite complémentaire et la prévoyance ; les aides à
l'embauche ; l'apprentissage et le contrat de professionnalisation ; le salarié étranger ; le temps partiel ;
la déclaration à l'inspection du travail quand l'établissement a cessé d'employer du personnel pendant six
mois au moins ; le cas du dirigeant lui-même. Sur la DSN : le lissage du seuil de 50 salariés sur cinq
années civiles (article L130-1 du Code de la sécurité sociale) n'est pas tranché pour la date de paiement
des cotisations, sans effet sur un premier salarié ; le report d'une échéance un jour non ouvré vient de
sources secondaires. Pour chacun, le dire et orienter vers le texte, l'Urssaf, le service de santé au
travail ou un juriste.

### Annexe : exemples-calcules

# Exemples calculés

Quatre embauches, calculées à la main sur le calendrier 2026-2027 et rejouées par le plan : ce sont les cas de
référence d'OriginSkill. Les dates sont au format JJ/MM/AAAA ; « repère » désigne une échéance de bonne pratique sans
date légale propre, « légale » une limite du texte.

## 1. Un cadre embauché le lundi 02/11/2026, essai de 4 mois, plan fait le 30/09/2026

Faits : premier jour de travail le 02/11/2026, cadre, essai de 4 mois stipulé, CDI, convention collective inconnue,
effectif retenu : 1.

- Avant l'arrivée, repères au 02/11/2026 : identifier la convention collective, adhérer au service de prévention et
  de santé au travail, mettre en place la complémentaire santé (légale dès le premier jour), afficher les
  informations obligatoires, écrire l'essai dans le contrat.
- DPAE : ouverte depuis le 25/10/2026 (un dimanche, 8 jours avant), à faire avant la prise de poste du 02/11/2026.
- Registre unique du personnel : inscription à l'arrivée, le 02/11/2026.
- Informations écrites : les premières au plus tard le 08/11/2026 (un dimanche : aucun report n'est relevé, viser
  le vendredi 06/11/2026), les autres au plus tard le 02/12/2026.
- Première DSN : le 15/12/2026 (un mardi), si la première paie est versée en novembre ; le 15/01/2027 si elle n'est
  versée qu'en décembre.
- Visite d'information et de prévention : au plus tard le 02/02/2027.
- Fin d'essai : le 01/03/2027 à minuit (4 mois de quantième à quantième) ; avec un renouvellement prévu par un accord
  de branche, au plus tard le 01/07/2027.
- Entretien de parcours professionnel : au plus tard le 01/11/2027.
- Question posée en fin de réponse : la convention collective applicable.

## 2. Un ouvrier embauché le jeudi 01/10/2026, plan fait le 30/09/2026

Faits : premier jour de travail le 01/10/2026, ouvrier, CDI, durée d'essai non donnée.

- La DPAE est **à faire maintenant** : sa fenêtre est ouverte depuis le 23/09/2026 et se ferme à la prise de poste
  du 01/10/2026.
- Essai : 2 mois au plus, fin au plus tard le 30/11/2026 ; 4 mois avec renouvellement, fin au plus tard le
  31/01/2027.
- Informations écrites : le 07/10/2026 et le 01/11/2026 (un dimanche, jour de la Toussaint : viser le vendredi
  30/10/2026).
- Première DSN : le 15/11/2026 tombe un dimanche, échéance lue au lundi 16/11/2026 (report rapporté par des sources
  secondaires) ; le 15/12/2026 si la première paie est versée en novembre.
- Visite d'information et de prévention : au plus tard le 01/01/2027, un jour férié : viser un jour ouvré qui
  précède.
- Entretien de parcours professionnel : au plus tard le 30/09/2027.
- Questions posées : la convention collective, la durée d'essai prévue au contrat.

## 3. Un CDD de 60 jours commencé le lundi 14/09/2026, essai de 10 jours stipulé, plan fait le 30/09/2026

Faits : CDD, 60 jours, essai de 10 jours prévu au contrat.

- Plafond d'essai : un jour par semaine entière de contrat, soit 8 jours pour 60 jours (8 semaines entières) ; fin au
  plus tard le 21/09/2026.
- L'essai stipulé de 10 jours dépasse ce plafond : à corriger avant la signature. Sa fin, le 23/09/2026, est déjà
  passée au 30/09/2026.
- Les échéances du 14/09/2026 (DPAE, complémentaire santé, registre, affichages, service de santé au travail,
  convention collective, essai écrit) et les informations du 20/09/2026 sont des **dates passées** : à vérifier si
  elles sont faites ; la DPAE, si elle manque, est à faire sans attendre.
- Seuil de six mois d'un CDD : 182 jours (26 semaines) donnent 14 jours d'essai au plus, 183 jours donnent 26 jours.

## 4. Un cadre embauché le lundi 02/11/2026 dans une entreprise de 52 salariés, sans décalage de paie

Faits : effectif de 52 salariés, paie versée dans le mois.

- À 50 salariés et plus sans décalage de paie, la DSN est due le 5 du mois suivant : le 05/12/2026 est un samedi,
  échéance lue au lundi 07/12/2026 ; le 05/01/2027 si la première paie est versée le mois suivant.
- Avec décalage de paie : le 15/12/2026. Sans l'indiquer, la date n'est pas donnée et la question est posée.
- Le franchissement à la hausse du seuil de 50 salariés peut être neutralisé pendant cinq années civiles
  consécutives (article L130-1 du Code de la sécurité sociale) ; son effet sur la date de paiement n'est pas
  tranché. Sans objet pour une première embauche.

### Annexe : glossaire

# Glossaire

| Terme | Définition courte |
| --- | --- |
| Premier jour de travail | Prise effective du poste : le fait qui ancre toutes les dates du plan. |
| DPAE | Déclaration préalable à l'embauche, faite à l'Urssaf avant la prise de fonction, au plus tôt 8 jours avant. |
| DSN | Déclaration sociale nominative : déclaration mensuelle des salaires et cotisations, déposée le 5 ou le 15 du mois suivant. |
| Décalage de paie | Le salaire d'un mois est versé le mois suivant ; il change l'échéance de la DSN à 50 salariés et plus. |
| Service de prévention et de santé au travail | Service qui suit la santé des salariés ; une petite entreprise adhère à un service interentreprises. |
| Visite d'information et de prévention | Visite du salarié par un professionnel de santé du service, au plus tard 3 mois après la prise effective du poste. |
| Examen médical d'aptitude | Examen qui remplace la visite pour un poste à risques particuliers et précède l'affectation. |
| Registre unique du personnel | Registre tenu dans chaque établissement, obligatoire dès le premier salarié. |
| Complémentaire santé collective obligatoire | Couverture des frais de santé offerte à tous les salariés, financée au moins pour moitié par l'employeur. |
| Panier de soins minimal | Socle de garanties que le contrat collectif doit couvrir. |
| Dispense d'adhésion | Cas où le salarié peut, à sa demande et avec justificatif, ne pas adhérer (par exemple CDD de moins de 3 mois). |
| Période d'essai | Durée pendant laquelle chacun peut rompre sans procédure de licenciement ; écrite au contrat, plafonnée par catégorie. |
| Renouvellement de l'essai | Prolongation unique, seulement si un accord de branche étendu la prévoit et si le contrat l'écrit. |
| Quantième à quantième | Décompte d'une durée en mois : 4 mois depuis le 02/11 finissent le 01/03 à minuit. |
| Convention collective | Texte qui complète le Code du travail pour une branche ; celle de l'activité principale de l'entreprise. |
| IDCC | Identifiant de convention collective : quatre chiffres. |
| Code APE | Code d'activité de l'entreprise : une piste pour trouver la convention, pas une preuve. |
| Entretien de parcours professionnel | Entretien avec l'employeur sur les compétences et la formation, dans la première année puis tous les 4 ans. |
| Date légale | Échéance fixée par un texte. |
| Date calculée | Échéance déduite d'une durée stipulée (par exemple la fin d'essai). |
| Repère | Échéance de bonne pratique sans date légale propre (avant l'embauche, à l'arrivée du salarié). |
| TESE | Titre emploi service entreprise : dispositif qui intègre la DPAE. |
| Numéro technique temporaire | Numéro établi dans la DPAE quand le salarié n'a pas encore de numéro de sécurité sociale. |

### Annexe : liens-ressources

# Liens officiels

Liens vers les pages officielles citées. Plusieurs ont été vus en résultat de recherche le 30/09/2026 sans être relus
en ligne (mention « non relu en ligne à ce jour » dans les sources de la fiche) : lire le texte à jour avant d'agir.

## Démarches

- Service Public Entreprendre, procédure et formalités d'embauche d'un salarié du secteur privé (F23107) :
  https://entreprendre.service-public.gouv.fr/vosdroits/F23107
- Urssaf, réaliser la DPAE : https://www.urssaf.fr/accueil/employeur/embaucher-gerer-salaries/embaucher/declaration-prealable-embauche.html
- Net-entreprises, déclaration préalable à l'embauche : https://www.net-entreprises.fr
- Urssaf, payer vos cotisations et déposer la DSN : https://www.urssaf.fr/accueil/employeur/gerer-entreprise/paiement-des-cotisations.html
- ameli entreprise, effectuer une DPAE et obtenir le numéro de sécurité sociale d'un salarié : https://www.ameli.fr/entreprise/vos-salaries/embaucher-salarie/dpae

## Règles

- Service Public Entreprendre, obligation de complémentaire santé de l'employeur (F33754) : https://entreprendre.service-public.gouv.fr/vosdroits/F33754
- Service Public Entreprendre, obligations d'affichage (F23106) : https://entreprendre.service-public.gouv.fr/vosdroits/F23106
- Service Public Entreprendre, période d'essai (F1643) : https://entreprendre.service-public.gouv.fr/vosdroits/F1643
- Code du travail numérique, obligations d'affichage : https://code.travail.gouv.fr/fiche-service-public/quelles-sont-les-obligations-daffichage-dans-une-entreprise
- Urssaf, comment est calculé l'effectif : https://www.urssaf.fr/accueil/employeur/cotisations/calcul-effectif/comment-calculer-effectif.html

## Textes (Légifrance)

- R1221-4, DPAE : https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000024214323
- R1221-35, informations au salarié : https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000048288640
- L1221-13, registre unique du personnel : https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000033971569
- L911-7 du code de la sécurité sociale, complémentaire santé : https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000031686110
- L4622-1, services de prévention et de santé au travail : https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006903351
- R4624-10, visite d'information et de prévention : https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000033769085
- D4711-1, affichage des coordonnées : https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000018527636
- D3171-2, affichage de l'horaire collectif : https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000018533984
- L1221-19 à L1221-23, période d'essai : https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000019071113
- L2261-2, convention collective applicable : https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006901780
- L6315-1, entretien de parcours professionnel : https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053279288
- R243-6 du code de la sécurité sociale, dates de la DSN : https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000034668597
- L130-1 du code de la sécurité sociale, effectif et seuils : https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000038610270
- Liste des conventions collectives : https://www.legifrance.gouv.fr/liste/idcc

### Annexe : methode-lecture-convention

# Méthode : lire la convention collective en quatre questions

Structure nôtre, fondée sur la règle de détermination de la convention (article L2261-2 du Code du travail) et sur les
points que le Code du travail laisse à la convention pour un premier salarié. Aucune clause de convention n'est
reprise ici : le texte de la convention fait foi et se lit dans sa version à jour. Aucune promesse de résultat.

## Principe

La convention collective applicable est celle de l'**activité principale** exercée par l'employeur. Le code APE donne
une piste, il ne décide pas. Une fois trouvée, on ne la lit pas en entier : on y cherche quatre réponses qui changent
ce que l'on fait pour ce premier salarié.

## Les quatre questions

1. **L'essai.** La convention prévoit-elle un essai plus court que le maximum légal de la catégorie ? Prévoit-elle le
   renouvellement (accord de branche étendu) ? Une durée plus courte l'emporte sur le maximum légal, jamais une plus
   longue.
2. **La santé et la prévoyance.** Impose-t-elle des garanties de complémentaire santé ou un taux de cotisation plus
   élevés que le minimum légal ? Une prévoyance obligatoire pour certaines catégories ? Quel organisme ?
3. **Le préavis et les congés.** Quel préavis en cas de rupture, quelle durée de congés, quelles règles propres à
   l'embauche (période d'essai, ancienneté) ? C'est ce que le bulletin de paie et les informations écrites devront
   mentionner.
4. **Le salaire minimum et la classification.** Quelle grille, quel coefficient pour le poste ? Le salaire du contrat
   ne descend pas sous le minimum de la convention ni sous le SMIC (fiche contrat de travail).

## Étapes

1. Partir de l'**activité principale réelle** (et non du seul code APE) ; si plusieurs activités rendent le critère
   incertain, le texte des conventions peut prévoir comment choisir, sinon un juriste tranche.
2. Retrouver l'IDCC : par le SIREN quand l'entreprise figure déjà dans les fichiers publics (issus des déclarations
   sociales, donc souvent absente avant la première embauche), ou par la liste officielle des conventions.
3. Lire les quatre réponses dans le texte, dans sa version à jour.
4. Mettre les réponses dans le plan : donner la convention collective, la catégorie du poste et la durée d'essai au plan de
   première embauche, qui n'a plus à les demander.

## Ce qu'elle ne fait pas

Elle ne dit pas quelle convention s'applique à une entreprise aux activités multiples, ne lit pas un accord
d'entreprise et ne chiffre aucun minimum. Elle ne remplace pas la lecture du texte de la convention.

## Limite assumée

L'outil `convention_collective` ne sort l'intitulé et la clause d'un IDCC que s'ils sont vérifiés par la veille ;
sinon il rend l'IDCC, le lien de consultation et ce qui manque. Une convention absente des fichiers publics n'est pas
une absence de convention : elle se déduit de l'activité.

### Annexe : methode-trois-temps

# Méthode : le plan en trois temps

Structure nôtre, alimentée par les textes et les pages officielles relevées (Service Public, Code du travail, Code de
la sécurité sociale) ; aucune pratique d'auteur n'est reprise. Aucune promesse de résultat : la méthode réduit les
oublis, elle ne remplace pas la lecture de la convention collective ni l'avis d'un juriste sur une situation
particulière.

## Principe

Un premier salarié se prépare comme un petit calendrier, pas comme un formulaire. Tout part d'un seul fait, le
premier jour de travail ; le plan range les étapes en trois temps et dit, pour chacune, si sa date est une limite du
texte (« légale »), un calcul (« calculée ») ou un repère de bonne pratique.

## Étapes

1. **Poser les faits.** Le premier jour de travail, le type de contrat (CDI ou CDD), la catégorie du salarié, la
   durée d'essai prévue, l'effectif après l'embauche. Sans l'un d'eux, le plan est donné quand même (plafonds des trois
   catégories, délais en durée) et la question est posée en fin de réponse.
2. **Faire calculer le plan** (`premiere_embauche_plan`). Lire d'abord ce qui est à faire maintenant et les dates
   passées, puis les étapes par ordre de date.
3. **Avant le contrat.** Identifier la convention collective et la lire (méthode suivante) : elle peut changer
   l'essai, la santé, le préavis. Écrire l'essai dans le contrat, sinon il n'existe pas. Adhérer au service de
   prévention et de santé au travail et mettre en place la complémentaire santé, à fournir dès le premier jour.
4. **Avant le premier jour.** Faire la DPAE dans sa fenêtre (8 jours avant l'embauche au plus tôt, avant la prise de
   poste au plus tard), afficher les informations obligatoires, ouvrir le registre unique du personnel.
5. **Après l'arrivée.** Remettre les informations écrites au 7e jour et à un mois, faire passer la visite
   d'information et de prévention dans les trois mois, tenir l'entretien de parcours dans la première année, déposer la
   première DSN le mois suivant la première paie.
6. **Mettre la mémoire à jour.** Proposer de mémoriser l'effectif et la convention collective après l'embauche,
   avec validation humaine : ils décident ensuite des seuils et de l'échéance de la DSN.

## Ce qu'elle ne fait pas

Elle ne rédige pas le contrat (fiche contrat de travail), ne fait pas la DPAE à la place de l'employeur, et ne dit
rien du salaire minimum, de la prévoyance ni des aides à l'embauche. Le document unique d'évaluation des risques
(DUERP), dû dès le premier salarié, est une étape du plan ; son inventaire des risques, propre à chaque métier, reste à écrire.

## Limite assumée

Convient à un premier salarié en CDI ou en CDD de droit privé. Pour un apprenti, un salarié étranger, un temps
partiel ou un poste à risques particuliers, des règles propres s'ajoutent : non relevées, à confirmer auprès du
service de santé au travail ou d'un juriste.

Approche concurrente : la **liste de contrôle sans dates**, que l'on coche à mesure. Elle évite de calculer, mais
laisse passer la fenêtre de la DPAE, le délai de la visite et l'échéance de la première DSN sans que rien ne les
signale.

## Aller plus loin avec OriginSkill

Ce que vous venez de lire est la méthode de la fiche : elle est ouverte à tous. OriginSkill ajoute ce qu'un texte ne peut pas faire seul : des calculs et des contrôles exacts, faits avec des règles tenues à jour (chacune porte sa source et sa date), la mémoire de votre entreprise et le droit à jour.

### Les calculs de cette fiche

Ces calculs sont inclus dans l'abonnement. OriginSkill les fait pour vous, avec des règles à jour et sourcées, et la réponse est garantie.

- **Lire le texte officiel d'un article de loi** (outil `orizon_article_texte`) : Va chercher, au moment de la question, le texte officiel d'un article de loi sur le site de l'État, tel qu'il est en vigueur à la date voulue.
- **Lire un article de votre convention collective** (outil `orizon_convention_article`) : Lit, dans la convention collective de l'entreprise, les articles d'un thème (période d'essai, préavis, indemnités…), cités tels quels avec leur date.
- **Retrouver la convention collective d'une entreprise** (outil `orizon_convention_collective`) : Retrouve la convention collective applicable à une entreprise à partir de son numéro SIREN, et le texte daté de la clause qui vous intéresse.
- **Calculer les délais d'une procédure de ressources humaines** (outil `orizon_delais_rh_calculer`) : Calcule les dates d'une procédure côté employeur : rupture de période d'essai, rupture conventionnelle, entretien, lettre, préavis, CDD.
- **Contrôler un contrat ou une situation de rupture** (outil `orizon_situation_verifier`) : Contrôle un contrat de travail ou une rupture côté employeur, et signale les situations où il faut un avocat (salarié protégé, grossesse, accident du travail…).
- **Dates de la CFE, des acomptes d'impôt sur les sociétés et des cotisations mensuelles** (outil `orizon_echeances_diverses`) : Donne les dates et montants de trois échéances régulières : solde de la cotisation foncière, acomptes d'impôt sur les sociétés, cotisations sociales mensuelles.
- **Planifier votre première embauche** (outil `orizon_premiere_embauche_plan`) : À partir de la date d'embauche, rend dans l'ordre les démarches datées pour embaucher un premier salarié : convention collective, déclaration préalable, contrat, visite médicale.

### Avec l'abonnement, en plus

- **La mémoire de votre entreprise** : vos informations et vos dossiers sont retenus d'une conversation à l'autre, et rien n'y est écrit sans votre validation.
- **Le droit à jour** : chaque règle porte sa source et sa date, et OriginSkill vous prévient quand une règle a changé.

### Brancher OriginSkill à votre assistant

Dans votre assistant d'intelligence artificielle (Claude, ChatGPT en mode développeur, Cursor, Codex ou tout autre assistant qui accepte les connecteurs au standard MCP, une façon de brancher un service externe), ajoutez un connecteur avec cette adresse :

    https://api.originskill.ai/mcp

Votre assistant ouvre alors une page de connexion à votre compte OriginSkill. Les étapes détaillées sont ici : https://originskill.ai/installer

### Tarif

Offres et abonnement : https://originskill.ai/tarif

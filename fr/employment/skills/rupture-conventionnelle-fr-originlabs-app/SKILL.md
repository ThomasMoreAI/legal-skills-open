---
name: rupture-conventionnelle-fr-originlabs-app
title: Se séparer d'un salarié d'un commun accord (rupture conventionnelle)
description: 'Se séparer d''un salarié d''un commun accord (rupture conventionnelle). Méthode professionnelle française, avec ses pièges et ses questions à poser. À utiliser quand : Employeur et salarié envisagent de se séparer d''un commun accord ; Calculer l''indemnité minimale, vérifier un montant convenu, estimer le coût ; Tenir le calendrier : entretien, signature, rétractation, homologation, départ.'
author: originlabs-app
author_url: https://github.com/originlabs-app/origin-skill-install/tree/main/skills/rupture-conventionnelle-fr
license: CC-BY-4.0
version: 0.1.0
execution_mode: open
jurisdiction: fr
practice: employment
language: fr
---

> **Version gratuite : règles datées entre le 18/07/2026 et le 03/10/2026.** Les règles changent (SMIC, TVA, seuils…). Avec l'abonnement OriginSkill, votre assistant reçoit la règle à jour, avec sa source et sa date.

# Se séparer d'un salarié d'un commun accord (rupture conventionnelle)

## Quand l'utiliser

- Employeur et salarié envisagent de se séparer d'un commun accord.
- Calculer l'indemnité minimale, vérifier un montant convenu, estimer le coût.
- Tenir le calendrier : entretien, signature, rétractation, homologation, départ.
- Relire une convention avant de la déposer sur le site officiel de demande d'homologation (TéléRC).

Quand **ne pas** l'utiliser : CDD, période d'essai en cours (fiche
`rupture-periode-essai-fr`), rupture conventionnelle collective ou plan de sauvegarde de
l'emploi, salarié protégé (autorisation de l'inspection du travail). Si le salarié subit
une pression, s'il y a un litige, un harcèlement, une grossesse ou un arrêt pour accident
du travail : le consentement peut être contesté, orienter vers un avocat ou un juriste
avant toute signature.

## Connaissances du métier

La rupture conventionnelle est un **accord libre** entre l'employeur et le salarié en
CDI. Aucun ne peut l'imposer à l'autre. Elle suppose au moins un entretien, où chacun
peut se faire assister, puis une convention signée dont un exemplaire est **remis au
salarié**. Chacun peut se rétracter pendant un délai calendaire qui démarre le lendemain
de la signature, par un moyen qui prouve la date. Ensuite seulement, la demande
d'homologation est déposée en ligne (TéléRC) ; l'administration a un délai en jours
ouvrables pour répondre, son silence vaut homologation. Le contrat se poursuit
normalement jusqu'à la date de rupture, fixée au plus tôt le lendemain de
l'homologation ; il n'y a pas de préavis.

Le salarié touche une **indemnité spécifique** au moins égale à l'indemnité légale de
licenciement (ou conventionnelle si elle est plus élevée), calculée sur un salaire de
référence et l'ancienneté ; elle est due même avec moins de 8 mois d'ancienneté.
L'employeur paie en plus une **contribution patronale** sur la part de l'indemnité
exonérée de cotisations ; cette part dépend du dossier du salarié et vient de la paie,
jamais d'une estimation. Le salarié peut ensuite percevoir l'allocation chômage ; pour
les ruptures à partir du 01/09/2026, sa durée maximale est réduite (loi n° 2026-470 du
11/06/2026), à vérifier auprès de France Travail. Les chiffres viennent des outils,
jamais de mémoire.

## Pièges fréquents

- **Signer le jour du premier contact**, sans vrai entretien ni délai de réflexion.
- **Ne pas remettre d'exemplaire signé au salarié** : la convention peut être annulée.
- **Déposer la demande avant la fin de la rétractation** : irrecevable.
- **Fixer une date de départ trop proche** de la signature.
- **Indemnité sous le minimum**, ou calculée sur le mauvais salaire de référence.
- **Oublier la contribution patronale** dans le coût, ou deviner la part exonérée.
- **Utiliser la rupture conventionnelle pour éviter un licenciement contesté** ou sous pression.

## Méthodes proposées (jamais imposées)

1. **Calendrier à rebours** : partir de la date de départ souhaitée et remonter jusqu'à
   l'entretien, en gardant les délais légaux et une marge. Détails :
   `methode-calendrier-rc`.
2. **Chiffrer avant de négocier** : minimum légal, minimum conventionnel, coût employeur,
   puis la marge de discussion. Détails : `methode-chiffrage-rc`.

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
fiches `contrat-travail-fr`, `rupture-periode-essai-fr` et `licenciement-employeur-fr`.

| Outil | Sert à | Appeler quand |
| --- | --- | --- |
| `situation_verifier` (bloc `risques`, `procedure: rupture_conventionnelle`) | Repérer ce qui interdit ou fragilise la rupture conventionnelle : essai en cours, salarié protégé, rupture collective, litige, grossesse, accident du travail | Au début |
| `delais_rh_calculer` (`rupture_conventionnelle`) | Fin de la rétractation, dépôt au plus tôt, fin de l'instruction, date de rupture au plus tôt | Une date de signature est prévue ou connue |
| `indemnites_calculer` (`indemnite_legale`, `motif: rupture_conventionnelle`) | Ancienneté, salaire de référence, indemnité minimale, contrôle du montant convenu, contribution patronale sur la part exonérée fournie | Les salaires sont connus |
| `convention_collective` (nom servi : `orizon_convention_collective`) | Retrouver la convention collective de l'employeur (IDCC) et lire le texte daté de la clause d'indemnité (`theme: rupture_conventionnelle`), l'indemnité conventionnelle pouvant dépasser le minimum légal. IDCC lu en direct (DSN, en retard de plusieurs mois) ou fourni par le client ; intitulé et texte ne sortent qu'une fois vérifiés par la veille sur KALI, sinon IDCC, lien KALI et manquant, jamais devinés | Une clause conventionnelle s'applique ou peut s'appliquer, ou le client ne sait pas quelle convention le lie |
| `convention_article` (nom servi : `orizon_convention_article`) | Lire dans LA convention collective du client (IDCC connu) le texte des articles d'un thème (`theme` : `periode_essai`, `preavis`, `indemnite_licenciement`, `rupture_conventionnelle`, `salaires_minima`, `duree_travail`, `conges`, `depart_retraite`, `maladie`), cité tel quel avec son identifiant KALIARTI, son numéro et sa date de version, jamais résumé comme une règle ; articles repérés par l'intitulé des sections, applicabilité non jugée (avenants, version à la date des faits, comparaison avec le Code du travail à faire avec le client) | Après `convention_collective`, quand une clause conventionnelle doit être lue. **Outil ouvert progressivement : il n'existe que s'il figure dans la liste `outils` rendue par `orizon_fiche` ; sinon, renvoyer vers le texte de la convention sur Légifrance (liste des IDCC) sans citer d'article de mémoire.** |
| `parametres_sociaux` (nom servi : `orizon_parametres_sociaux`) | Lire le PASS de l'année de la rupture et chiffrer 2 PASS (exonération de cotisations) et 10 PASS (assujettissement total) sur l'indemnité (`multiples_pass`). Seule une valeur vérifiée sort un chiffre (PASS 2026) ; le SMIC non vérifié sort en manquant avec le lien officiel, sans chiffre ; ne rend ni taux de cotisation ni coût employeur | Un seuil ou un plancher exprimé en SMIC ou en PASS doit être chiffré |

Chaque outil répond sous la forme unique `resultat` / `regles` / `manquant` / `prudence` /
`garanti`. Le coût donné est « indemnité + contribution patronale », pas le coût complet
(salaire, congés payés et charges du dernier mois non compris).

## Quatre usages

| Usage | Attitude | Outils |
| --- | --- | --- |
| Question simple (« délai de rétractation ? ») | Répondre avec la règle et sa source | `delais_rh_calculer` si un calcul aide |
| Objectif précis (« combien ça nous coûte ? ») | Vérifier les risques, calculer, restituer le minimum, le coût et ce qui manque | les trois |
| Suivre une méthode (« organise la rupture ») | Proposer le calendrier à rebours puis le chiffrage | selon l'étape |
| Explorer (« le salarié aura-t-il le chômage ? ») | Conversation libre, faits justes et sourcés | outils seulement s'ils aident |

## Sans abonnement (« non garanti »)

Les connaissances, les pièges et les méthodes restent utiles. Les règles datées, les
contrôles exacts et les cas de référence du moteur ne sont pas garantis : le dire, et
indiquer `garanti: non`.

## Documents

Convention et récapitulatif de calendrier : toujours un **projet à relire** par les deux
parties, recopié par l'employeur dans TéléRC. La fiche ne signe, ne dépose et n'envoie
rien, et ne chiffre ni la CSG, ni l'impôt, ni le solde de tout compte.

### Annexe : glossaire

# Glossaire

- **Rupture conventionnelle** : fin d'un CDI d'un commun accord, homologuée par l'administration.
- **Entretien** : rencontre préalable où chacun peut se faire assister.
- **Convention** : document signé qui fixe l'indemnité et la date de rupture.
- **Rétractation** : droit de revenir sur la signature pendant un délai calendaire.
- **Homologation** : validation par l'administration (DREETS) ; son silence vaut accord.
- **TéléRC** : service en ligne de dépôt de la demande d'homologation.
- **Indemnité spécifique** : somme versée au salarié, au moins égale à l'indemnité légale de licenciement.
- **Salaire de référence** : base de calcul, la plus favorable entre deux moyennes.
- **Contribution patronale** : somme due par l'employeur sur la part exonérée de l'indemnité.
- **PASS** : plafond annuel de la sécurité sociale, qui borne les exonérations.

### Annexe : liens-ressources

# Ressources rupture conventionnelle individuelle (CDI, France) - how-to + liens

Pays : **France** (Code du travail, art. L.1237-11 a L.1237-13). Langue: **francais**.
Consultation: 2026-07-08. Sources OFFICIELLES primaires; re-verifier en LIVE cas par cas
(la regle et les baremes bougent).

## Documents a lire (document-driven)

Contrat de travail (forme CDI, anciennete), bulletins de paie des 12 derniers mois (salaire
de reference), convention collective applicable (IDCC, indemnite eventuellement majoree),
justificatifs d'anciennete, Cerfa n°14598*01 (convention de rupture).

## Procedure type (4 temps)

1. Au moins un **ENTRETIEN** (le salarie peut se faire assister; l'employeur aussi s'il l'est).
2. **SIGNATURE** de la convention (Cerfa n°14598*01), un exemplaire par partie.
3. Delai de **RETRACTATION** de **15 jours calendaires** a compter du lendemain de la
   signature (report au 1er jour ouvrable si le dernier jour est chome).
4. Demande d'**HOMOLOGATION** sur **TeleRC** (apres la retractation); la DREETS dispose de
   **15 jours ouvrables**; le **silence vaut homologation tacite**. L'homologation est une
   condition de VALIDITE.

## Calcul de l'indemnite specifique

- Plancher d'ordre public: au moins l'**indemnite legale de licenciement** (L.1237-13).
- Bareme legal (R.1234-2): **1/4** de mois de salaire par annee jusqu'a 10 ans, puis **1/3**
  par annee au-dela; annees incompletes au prorata.
- Salaire de reference: la formule **la plus favorable** entre la moyenne des 12 derniers
  mois et la moyenne des 3 derniers mois (R.1234-4).
- Si la **convention collective** prevoit une indemnite superieure, c'est ce plancher
  **majore** qui s'applique. Au-dela: indemnite supra-legale negociable.
- Contribution patronale specifique 2026: **40 %** sur la part de l'indemnite exoneree de
  cotisations sociales (Code de la securite sociale L.137-12). Plafonds 2026 a re-verifier
  en ligne : PASS 48 060 EUR, 2 PASS 96 120 EUR, 10 PASS 480 600 EUR.

## Sources officielles (primaires)

- Code du travail numerique - procedure et delais:
  https://code.travail.gouv.fr/information/rupture-conventionnelle-individuelle-la-procedure-en-details
- Service-Public - calcul des delais (retractation / homologation):
  https://www.service-public.gouv.fr/particuliers/vosdroits/R42522
- Service-Public - calcul de l'indemnite specifique:
  https://www.service-public.gouv.fr/particuliers/vosdroits/F31539
- TeleRC - depot et homologation (dematerialisation obligatoire depuis le 01/04/2022):
  https://www.telerc.travail.gouv.fr
- Legifrance - Code de la securite sociale L.137-12 (contribution patronale specifique):
  https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053282399
- Legifrance - Code de la securite sociale L.242-1 (assiette sociale):
  https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000038836902
- economie.gouv - changements entreprises 2026 (PASS, contribution 40 %):
  https://www.economie.gouv.fr/entreprises/entreprises-ce-qui-change-au-1er-janvier-2026-0
- Ministere du Travail: https://travail-emploi.gouv.fr
- DREETS (region competente): https://dreets.gouv.fr
- Legifrance - Code du travail L.1237-11 a L.1237-13, R.1234-1 et s.:
  https://www.legifrance.gouv.fr

## Cas particuliers / hors perimetre (routage)

- **Salarie protege** (representant du personnel): procedure d'**AUTORISATION** de
  l'inspection du travail, PAS d'homologation -> hors v1, emettre un routing_result.
- **Periode protegee** (conge maternite, AT/MP): jurisprudence specifique -> escalade.
- **CDD, demission, licenciement, rupture conventionnelle COLLECTIVE**: hors perimetre ->
  routage vers le skill/processus dedie.

## Regle d'usage

Une affirmation du skill = une source officielle citee et datee. Les faits perissables
(bareme, prorata, delais, depot TeleRC, majoration IDCC) sont re-verifies en ligne avant
toute reponse. Le taux de contribution patronale et les plafonds 2026
sont aussi des faits perissables.

### Annexe : methode-calendrier-rc

# Méthode : calendrier de rupture conventionnelle à rebours

Proposée, jamais imposée. Reprend les étapes de la fiche Service-Public F19030 et du
simulateur officiel R42522 ; les délais exacts viennent du calcul des délais d'une procédure de ressources humaines
(cas de la rupture conventionnelle).

1. **Date de départ souhaitée** : c'est le point d'arrivée.
2. **Homologation** : l'administration dispose d'un délai en jours ouvrables à compter du
   lendemain de la réception de la demande ; la rupture a lieu au plus tôt le lendemain.
3. **Dépôt TéléRC** : au plus tôt le lendemain de la fin du délai de rétractation.
4. **Rétractation** : délai calendaire à compter du lendemain de la signature, prorogé
   s'il se termine un samedi, un dimanche ou un jour férié.
5. **Signature** : après au moins un entretien ; un exemplaire signé est remis au salarié.
6. **Entretien(s)** : avec information sur la possibilité d'être assisté.

Garder de la marge (courrier, jour férié, absence) ; si la date de départ tombe trop tôt,
l'outil le dit (la date de rupture prévue n'est pas possible). Le contrat se poursuit normalement
jusqu'à la rupture : congés et arrêts ne repoussent pas la date.

### Annexe : methode-chiffrage-rc

# Méthode : chiffrer avant de négocier

Proposée, jamais imposée. Pratique des services RH et des cabinets : connaître le
plancher et le coût avant d'ouvrir la discussion.

1. **Minimum légal** : `indemnites_calculer` (`indemnite_legale`, `motif:
   rupture_conventionnelle`) avec les 12 derniers salaires bruts et les primes des trois
   derniers mois.
2. **Minimum conventionnel** : lire la convention collective ; si elle prévoit plus, ce
   montant devient le plancher (non calculé par l'outil).
3. **Coût pour l'employeur** : indemnité convenue plus contribution patronale sur la
   part exonérée, que la paie fournit. L'outil ne devine jamais cette part.
4. **Marge de discussion** : écart entre le plancher et ce que l'employeur accepte, sans
   pression sur le salarié (sinon le consentement est contestable).

À signaler sans chiffrer : CSG, CRDS, impôt sur le revenu, solde de tout compte (salaire
du dernier mois, congés payés).

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

### Avec l'abonnement, en plus

- **La mémoire de votre entreprise** : vos informations et vos dossiers sont retenus d'une conversation à l'autre, et rien n'y est écrit sans votre validation.
- **Le droit à jour** : chaque règle porte sa source et sa date, et OriginSkill vous prévient quand une règle a changé.

### Brancher OriginSkill à votre assistant

Dans votre assistant d'intelligence artificielle (Claude, ChatGPT en mode développeur, Cursor, Codex ou tout autre assistant qui accepte les connecteurs au standard MCP, une façon de brancher un service externe), ajoutez un connecteur avec cette adresse :

    https://api.originskill.ai/mcp

Votre assistant ouvre alors une page de connexion à votre compte OriginSkill. Les étapes détaillées sont ici : https://originskill.ai/installer

### Tarif

Offres et abonnement : https://originskill.ai/tarif

---
name: remuneration-dirigeant-fr-originlabs-app
title: Combien me verser en salaire et en dividendes
description: 'Combien me verser en salaire et en dividendes. Méthode professionnelle française, avec ses pièges et ses questions à poser. À utiliser quand : Un créateur ou un dirigeant se demande s''il doit se payer un salaire, des dividendes, ou les deux ; Savoir combien coûte un salaire à la société et combien il en reste net, avant puis après impôt ; Comparer, pour des dividendes, l''impôt forfaitaire (la flat tax) et le barème de l''impôt sur le revenu.'
author: originlabs-app
author_url: https://github.com/originlabs-app/origin-skill-install/tree/main/skills/remuneration-dirigeant-fr
license: CC-BY-4.0
version: 0.1.0
execution_mode: open
jurisdiction: fr
practice: tax
language: fr
---

> **Version gratuite : règles datées entre le 13/07/2026 et le 03/10/2026.** Les règles changent (SMIC, TVA, seuils…). Avec l'abonnement OriginSkill, votre assistant reçoit la règle à jour, avec sa source et sa date.

# Combien me verser en salaire et en dividendes

Une seule question : sur ce que la société gagne, combien mettre en salaire, combien en dividendes, et
combien il reste vraiment dans la poche du dirigeant. Tout part de quelques faits : le statut du dirigeant,
ce que la société peut y consacrer, le capital, la situation fiscale du foyer. Le calcul se fait ; le
choix, lui, pèse aussi la retraite, la protection et la trésorerie, et il reste à la personne.

## Quand l'utiliser

- Un créateur ou un dirigeant se demande s'il doit se payer un salaire, des dividendes, ou les deux.
- Savoir combien coûte un salaire à la société et combien il en reste net, avant puis après impôt.
- Comparer, pour des dividendes, l'impôt forfaitaire (la flat tax) et le barème de l'impôt sur le revenu.
- Comprendre pourquoi, en EURL ou en SARL, des dividendes au-delà de 10 % du capital supportent des
  cotisations alors qu'en SASU ils n'en supportent pas.
- Chiffrer l'économie d'impôt sur les sociétés qu'apporte une rémunération.
- Répondre à une question précise : « je peux tout prendre en dividendes ? », « quel salaire minimum pour
  ma retraite ? », « mon capital de 1 € pose-t-il un problème ? ».

Quand **ne pas** l'utiliser : une société à l'impôt sur le revenu, une entreprise individuelle ou une micro-entreprise ;
une SA, une SCI, une société d'exercice libéral ; le calcul détaillé des dividendes distribuables et du calendrier
de leur déclaration (fiche `affectation-resultat-dividendes-fr`) ; la décision en assemblée (fiche
`pv-decisions-associes-fr`) ; le conseil patrimonial (épargne retraite, assurance vie). Orienter en le disant.

## Les faits qui décident

Sept faits décident du résultat, auxquels s'ajoute ce que la personne veut précisément (voir plus bas). Les connaître, sinon donner la comparaison pour ce que l'on sait, avec les
hypothèses dites, et poser en fin de réponse la question de ce qui manque.

- **La forme et le statut du dirigeant.** SAS, SASU : le président est assimilé salarié. EURL : le gérant associé
  unique est travailleur indépendant. SARL : tout dépend d'un fait, le gérant est-il majoritaire (en simplifiant, plus de
  la moitié des parts) ? Majoritaire, il est travailleur indépendant ; minoritaire ou égalitaire, assimilé salarié. La
  définition exacte (parts du foyer, autres gérants) n'est pas relevée ici.
- **L'enveloppe** : le résultat annuel de la société avant rémunération du dirigeant et avant impôt sur les sociétés.
  Ce n'est pas la trésorerie disponible.
- **Le capital social** (et, pour le gérant majoritaire, les primes d'émission et le solde moyen des comptes courants
  du foyer) : il fixe la réserve légale et le seuil de 10 %.
- **La part des dividendes du foyer** : 100 % pour un associé unique, moins s'il y a d'autres associés.
- **Le foyer fiscal** : nombre de parts, autres revenus imposables.
- **Le taux de cotisations du gérant majoritaire** : le taux officiel est non relevé ici ; à lire sur le simulateur de
  l'Urssaf ou chez l'expert-comptable, en demandant sur quelle base il est exprimé. À défaut, l'outil applique une règle
  indicative sourcée (environ 45 % de la rémunération nette, sources secondaires non officielles, non relues) et le dit :
  ce n'est jamais un taux garanti.
- **Ce que la personne veut précisément** : un salaire (en brut, ou en coût total pour la société), des dividendes (bruts ou
  nets avant impôt sur le revenu), une augmentation de capital envisagée. Les poser comme entrées plutôt que de bricoler
  l'enveloppe à la main.
- **Les cotisations propres à l'entreprise** : taux d'accident du travail, versement mobilité de la commune,
  prévoyance et mutuelle obligatoires.

**Faits de la mémoire d'entreprise consommables** (clés fermées de la mémoire ; un fait donné dans la conversation prime
toujours sur la mémoire, et un fait pris en mémoire se dit « à confirmer ») :

| Fait mémoire | Ce qu'il change ici |
| --- | --- |
| `forme_juridique` | SAS, SASU, SARL, EURL : statut du dirigeant ; SA, SCI, EI, autre : hors de l'outil |
| `impot` | `is` : traité ; `ir` : hors champ, dit |
| `associe_unique` | `personne_physique_dirigeant` : le dirigeant reçoit tous les dividendes (part de 100 %) ; `non` : poser sa part ; `personne_morale` ou `personne_physique_non_dirigeant` : le dirigeant n'est pas l'associé, hors de l'hypothèse, le dire |
| `effectif` | moins de 50 salariés : hypothèse de la contribution au logement à 0,10 % ; le dire sinon |
| `date_cloture_exercice` | les dividendes se mettent en paiement au plus tard neuf mois après la clôture (fiche `affectation-resultat-dividendes-fr`) |
| `denomination`, `siren` | nommer et retrouver le dossier |

Les autres faits de la mémoire (régime de TVA, convention collective, activité, cible) ne servent pas ici. Ne sont
pas en mémoire et se demandent à chaque fois : l'enveloppe, le capital, le statut du gérant de SARL, le foyer, le
taux de cotisations du gérant.

## Connaissances du métier

**La réponse courte.** Un dirigeant à l'impôt sur les sociétés a deux robinets. Le **salaire** est une charge : il
réduit le bénéfice, donc l'impôt sur les sociétés, mais il supporte des cotisations et l'impôt sur le revenu au barème.
Les **dividendes** se prennent sur le bénéfice après impôt sur les sociétés, sans déduction : ils supportent la flat
tax ou le barème, pas de cotisations pour un président de SAS ou de SASU, des cotisations pour un gérant majoritaire
au-delà de 10 % du capital. Aucun des deux n'est meilleur dans l'absolu : tout dépend de l'enveloppe, du statut et du
foyer, et le net d'aujourd'hui ne dit rien de la retraite ni de la protection de demain.

**Deux statuts, deux mécaniques.**

- *Président de SAS ou de SASU* : assimilé salarié, au régime général, avec des cotisations patronales et salariales
  comme un salarié cadre, mais sans assurance chômage (donc sans droit au chômage) et sans la réduction générale de
  cotisations. Ses dividendes ne supportent jamais de cotisations sociales, même s'il détient tout le capital.
- *Gérant majoritaire de SARL ou gérant associé unique d'EURL* : travailleur indépendant. Ses cotisations se calculent
  sur sa rémunération, selon des taux en réforme en 2026 (assiette unique, nouveaux taux appliqués à la régularisation de
  2025) : les taux officiels par poste ne sont pas relevés ici, seul un ordre de grandeur indicatif non officiel est cité (jamais appliqué à un montant). Le
  libellé suit la forme : *président assimilé salarié* en SAS ou SASU, *gérant majoritaire (travailleur indépendant)* en
  EURL ou en SARL majoritaire, *gérant assimilé salarié* en SARL minoritaire ou égalitaire : jamais « président » pour un
  gérant. La part de ses dividendes qui dépasse 10 % du capital social, des primes
  d'émission et des comptes courants détenus par lui et son foyer supporte ces cotisations, à la place des prélèvements
  sociaux sur le capital. Avec un capital de 1 000 €, presque tous les dividendes dépassent le seuil.

**Ce que le calcul apporte que le texte seul ne donne pas.** Le salaire le plus élevé n'est pas le plus cher : les
cotisations se calculent par tranches (jusqu'au plafond de la Sécurité sociale, puis au-delà) et le brut qui coûte
100 000 € à la société n'est pas 100 000 €. L'économie d'impôt sur les sociétés dépend du taux réduit (15 % sur les
premiers 42 500 €). La flat tax ou le barème change selon le revenu du foyer : le barème gagne parfois même avec une
tranche à 30 %, parce que seule une partie des dividendes y est imposée. Sur une enveloppe, ces effets se croisent ; le
balayage de 0 à 100 % de salaire les rend visibles.

**Exemple chiffré** (taux de 2026, relevé du 30/09/2026, sans les cotisations propres à l'entreprise). SASU, 100 000 €
avant rémunération et impôt sur les sociétés, capital de 1 000 €, célibataire, taux réduit d'impôt sur les sociétés :

| Scénario | Sortie de la société | Net avant impôt sur le revenu | Net après impôt sur le revenu |
| --- | --- | --- | --- |
| Tout en salaire | brut de 73 801,50 € + 26 198,50 € de cotisations patronales | 58 624,08 € | 49 123,84 € |
| Tout en dividendes | 20 750 € d'impôt sur les sociétés, 100 € de réserve légale, 79 150 € distribués | 64 428,10 € | 58 691,77 € (barème retenu) |
| Moitié-moitié | 50 000 € de coût de salaire, 8 250 € d'impôt sur les sociétés | 63 152,19 € | 56 097,11 € |

Sur ces seuls chiffres les dividendes laissent plus de net. Mais le salaire ouvre des droits (retraite, protection) que
les dividendes n'ouvrent pas, et les cotisations patronales non comptées (accident du travail, versement mobilité,
prévoyance) baissent encore le net du salaire. Un exemple n'est pas une règle : les chiffres changent avec l'enveloppe.

**Repères datés** (photo au 30/09/2026 ; recherche en ligne du 30/09/2026, pages officielles identifiées mais non relues
en ligne à ce jour, sauf mention) :

| Repère | Valeur | Source |
| --- | --- | --- |
| Flat tax (PFU) sur les dividendes | 31,4 % = 12,8 % d'impôt + 18,6 % de prélèvements sociaux, pour les dividendes payés depuis le 01/01/2026 (30 % = 12,8 % + 17,2 % en 2025) ; le taux dépend de la date de mise en paiement | Service-Public Entreprendre (actualité A18796) ; impots.gouv.fr, « Les revenus mobiliers » (relu le 13/07/2026) |
| CSG sur les revenus du capital | 10,6 % depuis le 01/01/2026 (9,2 % avant), loi de financement de la Sécurité sociale pour 2026, art. 12 ; la CSG sur les salaires reste à 9,2 % | pages professionnelles concordantes (Hagnéré, Legea), texte de loi non relu |
| Option pour le barème | abattement de 40 % sur les dividendes, 6,8 points de CSG déductibles ; option globale pour tous les revenus du capital du foyer ; plus irrévocable à compter de 2026 (à confirmer) | Service-Public (F34913) |
| Impôt sur les sociétés | 25 % ; 15 % sur les 42 500 premiers euros sous conditions (chiffre d'affaires sous 10 M€, capital libéré détenu à 75 % par des personnes physiques) | Service-Public Entreprendre (F23575), BOFiP IS-LIQ-20-10 |
| Gérant majoritaire, dividendes | fraction au-delà de 10 % du capital, des primes et des comptes courants du foyer soumise aux cotisations | notice Urssaf des revenus 2026 (relue le 13/07/2026) |
| Barème de l'impôt sur le revenu (revenus de 2025) | 0 % jusqu'à 11 600 € ; 11 % jusqu'à 29 579 € ; 30 % jusqu'à 84 577 € ; 41 % jusqu'à 181 917 € ; 45 % au-delà, par part | Service-Public (A18045), loi n° 2026-103 du 19 février 2026, art. 4 |
| Plafond de la Sécurité sociale 2026 | 48 060 € | arrêté du 22 décembre 2025 |
| Trimestre de retraite validé | 150 fois le SMIC horaire du 1er janvier (12,02 € en 2026, soit 1 803 € bruts par trimestre), quatre trimestres au plus par an | Code de la sécurité sociale, art. R351-9 : règle connue du rédacteur, **non relue en ligne** (le SMIC vient de la table des paramètres sociaux d'OriginSkill) ; à relire sur Légifrance avant de s'y fier |

Le barème des revenus perçus en 2026 n'est pas voté à cette date : l'estimation prend celui des revenus de 2025. Les
lignes de cotisations du président (maladie, vieillesse, allocations familiales, retraite complémentaire, CSG-CRDS) sont
dans le calcul, avec leur date et leur source.

## Pièges fréquents

- **Comparer sur le seul net.** Zéro salaire peut rapporter plus net aujourd'hui et ne valider aucun trimestre de
  retraite : un trimestre se valide à 150 fois le SMIC horaire du 1er janvier (1 803 € bruts en 2026, soit 7 212 € pour les
  quatre trimestres), et l'outil dit combien de trimestres valide chaque scénario. Le montant de la pension, lui, n'est pas
  calculé.
- **Se verser des dividendes sans bénéfice distribuable** ou avant l'approbation des comptes : c'est un dividende fictif
  (fiche `affectation-resultat-dividendes-fr`).
- **Confondre l'enveloppe et la trésorerie.** Une société peut avoir un bénéfice sans argent disponible.
- **Oublier l'impôt sur les sociétés.** Les dividendes se prennent sur ce qui reste après lui.
- **Appliquer 30 % à des dividendes de 2026.** Le taux est de 31,4 % pour les dividendes payés depuis le 01/01/2026.
- **Croire le capital de 1 € sans conséquence en EURL ou en SARL.** Au-delà de 10 % du capital, les dividendes du gérant
  majoritaire supportent des cotisations ; augmenter le capital ou les comptes courants a un coût et des conséquences
  (un capital versé est bloqué) à peser avant de choisir.
- **Confondre coût pour la société et rémunération.** 100 000 € dépensés par la société ne font pas un brut de 100 000 €.
- **Oublier les cotisations propres à l'entreprise** (accident du travail, versement mobilité, prévoyance) : le net d'un
  salaire est alors un maximum.
- **Prendre le barème pour toujours pire que la flat tax.** L'option est globale (tous les revenus du capital du foyer) :
  la comparer sur le foyer entier.
- **Ne pas dire si le gérant de SARL est majoritaire.** Tout change : cotisations de travailleur indépendant ou de salarié.
- **Fixer la rémunération sans décision.** Elle se décide selon les statuts (décision des associés) : les règles article
  par article ne sont pas relevées ici (fiche `pv-decisions-associes-fr`).

## Méthodes proposées (jamais imposées)

1. **Du besoin du foyer au mélange de rémunération** : partir de ce dont le foyer a besoin chaque mois, puis du revenu
   que la société peut financer, et tester trois niveaux de salaire. Détails : `methode-besoin-du-foyer`.
2. **Les trois scénarios et le balayage** : salaire, dividendes, mixte sur la même enveloppe, lire le balayage de 0 à
   100 %, puis passer en revue ce qui n'est pas dans le chiffre. Détails : `methode-trois-scenarios`.

Elles ne se valent pas toujours : la première convient à un créateur dont la première question est « de quoi ai-je besoin
pour vivre ? » et dont la société n'a pas encore de bénéfice ; la seconde à un dirigeant dont la société dégage déjà un
résultat. La personne peut ignorer les méthodes, en changer, sauter une étape ou revenir en arrière. Les cas types et les
questions à peser sont dans `cas-types-et-arbitrages` ; le vocabulaire dans `glossaire`.

## Contrat de réponse (3 règles fixes)

1. Toute règle ou tout chiffre affirmé vient avec sa **source datée** : les taux viennent du calcul avec leur source ;
   un repère se cite avec sa source et la date de la recherche, et on dit quand la page officielle n'a pas été relue.
2. **Ne jamais inventer** : dire ce qui manque (taux de cotisations du gérant, cotisations propres à l'entreprise,
   capital) et ce qui n'est pas relevé. Un ordre de grandeur de site professionnel n'est jamais présenté comme un taux
   officiel : sans taux fourni pour un gérant majoritaire, l'outil ne chiffre ni le net ni le coût du salaire ; il pose la question et
   cite l'ordre de grandeur « autour de 40 à 45 % du net selon les sources secondaires, à vérifier » sans l'appliquer. Ne jamais en
   déduire un net ou un coût.
3. **Prévenir** quand une règle vient de changer (champ `prudence`) : c'est le cas du taux de la flat tax en 2026.

« Plan d'action d'abord », « deux questions au maximum » et l'ordre des étapes sont de bonnes habitudes quand la
personne veut agir, pas des obligations.

**Restitution au dirigeant.**

1. Répondre d'abord, exactement, à la question posée et à rien d'autre : la règle ou le chiffre en une ou deux phrases, puis ce qui sert à cette question. Pas de tableau complet, pas de volet non demandé, aucun chiffre d'exemple inventé. Reprendre tels quels les chiffres de `en_clair.resultats`, sans les recalculer ; ne jamais affirmer qu'un point non fourni par le dirigeant est en règle.
2. Si un fait manque et change la réponse, donner la réponse pour chaque cas, puis poser une seule question à la fin : celle qui débloque. Aucune question si rien ne manque.
3. Parler en mots du dirigeant : jamais « l'outil », « le moteur », « le serveur », ni un code ou un champ technique (`entree_incomplete`, `manquant`, `prudence`) ; ne jamais recopier le mot « garanti » ni « non garanti ». Traduire : « il me manque la date d'embauche pour calculer… », « règle relevée le JJ/MM/AAAA, texte officiel pas encore relu ; à reconfirmer avant d'agir ». Écrire « vérifiée » seulement pour une règle marquée vérifiée (« règle vérifiée le JJ/MM/AAAA ; à reconfirmer avant d'agir si l'enjeu est important ») : une source citée n'est pas une vérification.
4. Une échéance qui tombe un samedi, un dimanche ou un jour férié se dit avec son report si les règles en donnent un, sinon « à vérifier ».
5. Ne jamais inventer un fait absent, ni pour appeler un outil. Une règle datée fournie par OriginSkill n'est jamais remplacée par une source secondaire trouvée en ligne ; en cas d'écart, donner les deux valeurs, leurs sources et leurs dates.

## Outils (description ouverte)

L'exécution exacte est servie par le connecteur, sur le moteur « dirigeant ».

| Outil | Sert à | Appeler quand |
| --- | --- | --- |
| `remuneration_dirigeant_comparer` (nom servi : `orizon_remuneration_dirigeant_comparer`) | Pour une enveloppe : salaire, dividendes et mixte, avec coût pour la société, cotisations, impôt sur les sociétés et impôt économisé, réserve légale, flat tax ou barème (le moins cher retenu), cotisations sur les dividendes au-delà de 10 % du capital pour le gérant majoritaire, net avant et après impôt sur le revenu, balayage de 0 à 100 % de salaire, hypothèses et ce qui n'est pas calculé | Dès qu'une enveloppe et une forme sont connues |

Entrées : `forme_juridique` est indispensable, avec `enveloppe_eur` pour comparer salaire et dividendes (sans enveloppe,
donner `remuneration_brute_cible_eur`, `cout_total_salaire_eur` ou des dividendes voulus). `remuneration_brute_cible_eur` : le brut annuel voulu ; l'outil rend le coût pour
la société, les cotisations ligne par ligne (assiette, taux, montant), la CSG-CRDS, le net, l'impôt par tranche et le net
après impôt, sans tâtonner ; avec une enveloppe, il s'ajoute un scénario `brut_cible`. `cout_total_salaire_eur` : le même
salaire exprimé en coût total pour la société (brut et cotisations patronales ; pour un gérant majoritaire, la rémunération
versée), à ne pas donner avec le brut. `dividendes_voulus_bruts_eur` ou `dividendes_voulus_nets_eur` (nets des cotisations et
des prélèvements sociaux, avant impôt sur le revenu) : l'outil rend `dividendes_voulus.enveloppe_necessaire_eur`, le détail du
scénario (impôt sur les sociétés, réserve légale, part soumise à cotisations, net après impôt) et, si l'enveloppe est donnée,
dit si elle suffit ; un salaire voulu s'ajoute, sinon aucun salaire. `augmentation_capital_eur` : une augmentation de capital
envisagée, chiffrée dans `augmentation_capital` : le seuil de 10 % avant et après, le gain annuel **à dividendes constants** (la
fraction libérée supporte les prélèvements sociaux à la place des cotisations) et, avec une enveloppe, l'effet **distinct** de la
réserve légale, qui monte avec le capital et réduit les dividendes distribués : ne jamais comparer deux enveloppes à capitaux
différents sans cette séparation ; sans dividendes visés ni enveloppe, l'outil pose la question. Facultatives : `gerant_majoritaire` (indispensable en
SARL), `impot`, `part_salaire_mixte` (0,5 par défaut), `capital_social`, `reserve_legale_existante`, `taux_reduit_is`,
`parts_fiscales`, `autres_revenus_imposables_foyer`, `autres_cotisations_patronales_pct`, `cotisations_tns_pct_assiette`, `cotisations_tns_pct_du_net`,
`quote_part_foyer_gerant`, `capital_primes_comptes_courants`. Une entrée non comprise est dite dans la prudence, jamais
ignorée en silence. Les mêmes noms de faits que la mémoire d'entreprise servent : `forme_juridique`, `impot`.

Lire la réponse : `resultat.reponse` porte la synthèse ; `resultat.scenarios` donne les trois scénarios ligne par ligne ;
`retraite` et `retraite_trimestres_valides` (par scénario et par point du balayage) disent combien de trimestres la rémunération valide, à
lire à côté du net, jamais à sa place ; `balayage_part_salaire` le net après impôt pour chaque part de salaire ; `net_apres_impot_le_plus_eleve` le meilleur point
du balayage, à ne pas lire comme une recommandation ; `hypotheses` et `non_calcule` se disent toujours ; `manquant` devient
la question à poser ; `prudence` se dit une fois. Chaque appel répond sous la forme unique `resultat` / `regles` / `manquant` /
`prudence` / `garanti`.

Sans taux de cotisations pour le gérant majoritaire, l'outil NE chiffre PAS (ni net, ni coût du salaire) : il rend la question
décisive (taux réel lu sur l'appel de cotisations ou au simulateur de l'Urssaf, **et sur quelle base il est exprimé**) et cite, sans
l'appliquer, la règle indicative `cotisations-gerant-majoritaire-taux-indicatif` (autour de 40 à 45 % du net selon des sources
secondaires non officielles, pages non relues, `garanti: non`). Relancer avec le taux de la personne, qui déclenche le calcul.
`cotisations_tns_pct_assiette` est le taux sur l'assiette (la rémunération brute versée et la fraction de dividendes
au-delà de 10 % du capital : la forme que donne un expert-comptable) ; `cotisations_tns_pct_du_net` est le même taux sur
la rémunération nette (45 % du net valent environ 31 % de l'assiette ; l'outil convertit et le dit). Ne pas confondre les
deux : appliquer à une fraction de dividendes un taux donné « du net » la surestimerait. L'ordre de grandeur de
45 % de la rémunération nette est non officiel. Le calcul de la réserve légale s'arrête à
5 % du bénéfice : pour le distribuable exact, la fiche `affectation-resultat-dividendes-fr`.

L'outil calcule ; il ne rédige rien, n'envoie rien et ne recommande rien. Le choix reste à la personne.

## Quatre usages

| Usage | Attitude | Outils |
| --- | --- | --- |
| Question simple (« c'est quoi la flat tax sur les dividendes ? ») | Répondre avec la règle, sa date et sa source | aucun, ou `remuneration_dirigeant_comparer` si une enveloppe est donnée |
| Objectif précis (« j'ai 100 000 € de bénéfice en SASU, salaire ou dividendes ? ») | Appeler la comparaison tout de suite, rendre la réponse d'abord, puis les hypothèses et ce qui n'est pas dans le chiffre | `remuneration_dirigeant_comparer` |
| Suivre une méthode (« guide-moi pour décider ») | Proposer l'une des deux méthodes ; la personne choisit le rythme | selon l'étape |
| Explorer (« le salaire minimum, ça sert à quoi ? ») | Conversation libre, faits justes, sans chiffre inventé | outil seulement si une enveloppe est donnée |

## Sans abonnement (« non garanti »)

Les connaissances, les pièges, les méthodes et les cas types restent utiles. Le calcul exact, les lignes de cotisations et
les règles servies ne sont pas garantis : le dire, et indiquer `garanti: non`.

## Documents

Note de comparaison, projet de décision sur la rémunération ou sur la distribution de dividendes : toujours un **projet à
relire** par la personne, jamais « prêt à signer ». Le modèle de la personne rédige à partir des chiffres de la comparaison
et des faits du dossier ; rien n'est produit ni envoyé par la fiche. Ne jamais y mettre un taux ou un montant que la
comparaison ne contient pas.

## Ce qui n'est pas relevé

Les taux officiels de cotisations par poste du gérant majoritaire en 2026 (seul un ordre de grandeur indicatif non officiel est porté, avec ses sources secondaires) ; le taux d'accident du travail, le versement mobilité, la
prévoyance et la mutuelle obligatoires, la formation professionnelle et la taxe d'apprentissage ; le montant de la pension
(seuls les trimestres validés sont comptés, d'après une règle non relue en ligne) ; les modalités 2026 de l'ACRE et des autres aides de début d'activité ; la décote et le
plafonnement du quotient familial de l'impôt sur le revenu ; le barème des revenus de 2026 ; les contributions sur les hauts
revenus ; l'assiette exacte des cotisations sur les dividendes du gérant majoritaire (application ou non de l'abattement de
40 %) ; les règles de décision de la rémunération selon les statuts. Pour chacun, le dire et orienter vers l'Urssaf, le
simulateur de l'Urssaf, les statuts ou un professionnel pour un enjeu important.

### Annexe : cas-types-et-arbitrages

# Cas types et arbitrages

Cas types pour situer une question, avec ce qui décide et les questions à peser. Les chiffres viennent du calcul, à la date
du relevé du 30/09/2026 ; ce sont des exemples, pas des règles.

## A. Président de SASU, première année, bénéfice faible ou nul

- Ce qui décide : la trésorerie, pas l'optimisation. Sans bénéfice, pas de dividendes ; un salaire n'est possible que si la
  société peut le financer.
- À peser : le niveau de rémunération qui couvre le besoin du foyer ; ce que le dirigeant accepte de ne pas valider en retraite
  ou en protection la première année (un trimestre se valide à 1 803 € bruts en 2026, soit 7 212 € pour l'année : une petite
rémunération annuelle suffit à valider les quatre trimestres, c'est un seuil bas à atteindre, pas un salaire complet ; règle
non relue en ligne) ; les aides de début d'activité
  (modalités 2026 non relevées ici).
- À ne pas faire : se verser des dividendes au prétexte que le compte bancaire est approvisionné. Il faut un bénéfice distribuable et
  l'approbation des comptes (fiche `affectation-resultat-dividendes-fr`).

## B. Président de SASU, société qui dégage un résultat

- Exemple : 100 000 € avant rémunération et impôt sur les sociétés, capital de 1 000 €, célibataire : tout en salaire laisse
  49 123,84 € nets après impôt sur le revenu, tout en dividendes 58 691,77 € (barème retenu), moitié-moitié 56 097,11 €.
- Ce qui décide : les dividendes ne supportent aucune cotisation en SAS, donc l'écart de net favorise souvent les dividendes.
- À peser : la retraite et la protection que seul le salaire ouvre ; la prévoyance et la mutuelle ; un projet de crédit (demander
  à la banque comment elle lit salaire et dividendes) ; les autres revenus du foyer, qui changent le choix entre flat tax et
  barème.

## C. Gérant associé unique d'EURL à l'IS, capital de 1 000 €

- Ce qui décide : le seuil de 10 % du capital. Avec 1 000 € de capital et sans compte courant, le seuil est de 100 € : presque
  tous les dividendes supportent des cotisations de travailleur indépendant, au lieu des prélèvements sociaux de 18,6 %.
- Illustration avec un taux supposé de 45 % de la rémunération nette (ordre de grandeur de sites professionnels, non
  officiel, à remplacer par le taux du simulateur de l'Urssaf) : 100 000 € d'enveloppe laissent environ 57 240,84 € nets après
  impôt en tout salaire, 47 249,69 € en tout dividendes. Dans ce cas les dividendes ne sont plus l'avantage qu'ils sont en SASU.
- Chiffrer une augmentation de capital : en donnant le montant de l'augmentation de capital, l'outil rend le seuil de 10 % avant et après et le gain
  annuel à dividendes constants (exemple de banc, capital et comptes courants du foyer de 23 000 €, 36 000 € de dividendes,
  taux de 40 % supposé par l'expert-comptable : 33 700 € soumis à cotisations, puis 30 700 € après une augmentation de
  30 000 €, soit 642 € par an avant impôt sur le revenu), puis l'effet distinct de la réserve légale à enveloppe constante.
- À peser : relever le capital ou les comptes courants d'associés (un capital versé est bloqué, un compte courant est une
  créance que la société doit rembourser) ; les cotisations supportées ouvrent des droits ; changer de forme juridique est
  une autre question, hors de cette fiche.

## D. SARL à plusieurs associés, gérant majoritaire

- Ce qui décide : la part des dividendes qui revient au gérant et à son foyer, et la base du seuil de 10 % (capital, primes,
  comptes courants du foyer). Les dividendes se partagent selon les parts : le reste va aux autres associés.
- À peser : les autres associés n'ont pas les mêmes cotisations ; une rémunération du gérant réduit le bénéfice de tous ; la
  décision suit les statuts (fiche `pv-decisions-associes-fr`).

## E. SARL, gérant minoritaire ou égalitaire

- Ce qui décide : le gérant est assimilé salarié, comme un président de SAS (l'outil le nomme « gérant assimilé salarié », jamais « président ») ; la règle des 10 % ne s'applique pas. Le calcul
  se fait comme pour une SASU. Ce statut dépend de la détention des parts : le faire confirmer si la répartition change.

## Questions à peser dans tous les cas

1. Retraite : quels trimestres et quel niveau de pension veut-on construire ?
2. Protection : indemnités en cas de maladie, invalidité, décès : différentes selon le statut, non chiffrées ici.
3. Projets : crédit, location, autres besoins qui regardent les revenus déclarés.
4. Trésorerie : la société peut-elle financer le salaire et les cotisations chaque mois ?
5. Foyer : le conjoint a-t-il des revenus ? Le nombre de parts change la comparaison entre flat tax et barème.
6. Horizon : un choix d'une année, ou un régime pour plusieurs années ? Les taux et le barème bougent chaque année.

## Ce que le calcul ne dit pas

La rémunération du dirigeant doit aussi rester cohérente avec son travail et la situation de la société ; ce que l'administration
admet ou non n'est pas relevé ici. Pour un enjeu important, un professionnel peut relire la comparaison avec les chiffres réels
de la société.

### Annexe : glossaire

# Glossaire

| Terme | Définition courte |
| --- | --- |
| Enveloppe | Résultat annuel de la société avant rémunération du dirigeant et avant impôt sur les sociétés : ce qu'elle peut consacrer au dirigeant et à l'impôt. Ce n'est pas la trésorerie. |
| Assimilé salarié | Statut social du président de SAS ou de SASU (et du gérant non majoritaire de SARL) : régime général de la Sécurité sociale, cotisations comme un salarié, sans assurance chômage. |
| Travailleur indépendant (TNS) | Statut social du gérant majoritaire de SARL et du gérant associé unique d'EURL : cotisations propres aux indépendants, en réforme en 2026. |
| Gérant majoritaire | En simplifiant, gérant qui détient plus de la moitié des parts de la SARL, seul ou avec son foyer. La définition exacte n'est pas relevée ici. |
| Coût pour la société | Ce que la rémunération coûte vraiment : salaire brut plus cotisations patronales (assimilé salarié), ou rémunération brute versée (gérant majoritaire). |
| Brut, net avant impôt, net après impôt | Brut : avant cotisations salariales. Net avant impôt : après cotisations et CSG-CRDS. Net après impôt : après l'impôt sur le revenu estimé. |
| Cotisations patronales, salariales | Les premières sont payées par la société en plus du brut, les secondes sont retenues sur le brut. |
| CSG, CRDS | Contributions sociales sur les revenus d'activité (9,2 % et 0,5 % en 2026) et, avec d'autres prélèvements, sur les revenus du capital (CSG à 10,6 % depuis le 01/01/2026). |
| Plafond de la Sécurité sociale | Montant annuel (48 060 € en 2026) qui sépare les tranches de plusieurs cotisations. |
| Impôt sur les sociétés (IS) | Impôt sur le bénéfice de la société : 15 % sur les premiers 42 500 € sous conditions, 25 % sinon. |
| IS économisé | Différence entre l'impôt que la société paierait sans rémunération et celui qu'elle paie avec : le salaire est une charge déductible, pas le dividende. |
| Dividende | Part du bénéfice distribuée aux associés après impôt sur les sociétés, réserve légale et décision des associés. Jamais déductible. |
| Réserve légale | Prélèvement de 5 % du bénéfice jusqu'à ce qu'elle atteigne 10 % du capital : il reste dans la société. |
| Flat tax (PFU) | Prélèvement forfaitaire unique sur les dividendes : 31,4 % en 2026 (12,8 % d'impôt et 18,6 % de prélèvements sociaux). |
| Option pour le barème | Choix, pour tous les revenus du capital du foyer, d'imposer les dividendes au barème progressif avec un abattement de 40 %. |
| Seuil de 10 % | Pour le gérant majoritaire : la part des dividendes qui dépasse 10 % du capital, des primes d'émission et des comptes courants du foyer supporte des cotisations. |
| Dividendes voulus | Dividendes bruts, ou nets avant impôt sur le revenu (après cotisations sur la part au-delà de 10 % du capital et prélèvements sociaux), que la personne veut se verser ; l'outil en déduit l'enveloppe nécessaire. |
| Taux indicatif | Ordre de grandeur des cotisations du gérant majoritaire (autour de 40 à 45 % de la rémunération nette selon des sources secondaires non officielles et non relues) : dit en clair, jamais appliqué à un montant. Sans taux fourni, l'outil ne chiffre ni le net ni le coût du salaire et pose la question. |
| Part de salaire | Fraction de l'enveloppe consacrée à la rémunération (coût pour la société), de 0 à 100 %. |
| Balayage | Le même calcul répété pour des parts de salaire de 0 à 100 % par pas de 10 %. |
| Quotient familial | Division du revenu imposable du foyer par son nombre de parts avant d'appliquer le barème. |

### Annexe : methode-besoin-du-foyer

# Méthode : du besoin du foyer au mélange de rémunération

Méthode proposée, jamais imposée. Elle convient à un créateur ou à un dirigeant dont la première question est « de quoi ai-je
besoin pour vivre ? », surtout quand la société n'a pas encore de bénéfice ou que son résultat est incertain.

## Les étapes

1. **Chiffrer le besoin du foyer.** Combien faut-il recevoir chaque mois, net, pour payer logement, crédits et vie
   courante ? Le noter en euros par mois, puis par an. C'est la personne qui le sait ; ne pas le deviner.
2. **Situer la société.** Quel résultat annuel avant rémunération et avant impôt sur les sociétés (l'enveloppe) la société
   peut-elle viser, et quelle trésorerie a-t-elle vraiment ? Une première année peut n'avoir aucun bénéfice : dans ce cas les
   dividendes ne sont pas possibles, seul un salaire est envisageable si la trésorerie le permet.
3. **Fixer un plancher de salaire.** C'est le niveau qui couvre le besoin net du foyer, ou qui valide des droits
   (retraite, protection). Le calcul donne le seuil qui valide les quatre trimestres de retraite
   (7 212 € bruts par an en 2026, d'après une règle non relue en ligne ; à confirmer auprès de la
   caisse de retraite) ; le seuil se compare au besoin du foyer : le plancher est le plus haut des deux.
4. **Faire tourner la comparaison à trois niveaux de salaire.** Avec l'enveloppe, appeler le calcul en faisant varier la
   part de salaire (par exemple le plancher, un niveau intermédiaire, tout en salaire) et lire le net après impôt et le coût
   pour la société de chaque niveau.
5. **Ajouter les dividendes seulement quand ils sont possibles.** Il faut un bénéfice distribuable, l'approbation des
   comptes et une décision des associés (fiche `affectation-resultat-dividendes-fr`). Pour un gérant majoritaire, regarder le
   seuil de 10 % avant.
6. **Dire ce qui n'est pas dans le chiffre.** Retraite, prévoyance, chômage, aides de début d'activité, cotisations propres à
   l'entreprise : les énumérer, et dire lesquelles la personne doit vérifier.
7. **Revoir chaque année.** Les taux, l'enveloppe et la situation du foyer changent : refaire la comparaison à chaque
   exercice et à chaque changement important.

## Questions à poser (la plus discriminante d'abord)

- Quel statut exact : président de SAS ou de SASU, gérant associé unique d'EURL, gérant de SARL majoritaire ou non ?
- Quel besoin net mensuel pour le foyer ?
- Quel résultat la société peut-elle viser sur l'année, avant toute rémunération ?
- Quel capital, et quels comptes courants d'associés, pour un gérant majoritaire ?
- Quels autres revenus dans le foyer, et combien de parts fiscales ?

## Limites

La méthode part du besoin et non du meilleur net : elle peut conduire à un salaire plus élevé que le calcul seul ne le
proposerait, pour valider des droits ou pour rassurer une banque (comment un établissement lit un salaire et des dividendes
n'est pas relevé ici). Elle ne dit rien d'un changement de forme juridique.

### Annexe : methode-trois-scenarios

# Méthode : les trois scénarios et le balayage

Méthode proposée, jamais imposée. Elle convient à un dirigeant dont la société dégage déjà un résultat et qui veut voir
l'effet de chaque répartition sur le net, l'impôt sur les sociétés et les prélèvements.

## Les étapes

1. **Fixer l'enveloppe et le statut.** Forme juridique, statut du gérant de SARL, résultat annuel avant rémunération et avant
   impôt sur les sociétés. Poser en début de réponse les hypothèses prises faute d'information.
2. **Appeler le calcul.** Trois scénarios sur la même enveloppe : tout en salaire, tout en dividendes, mixte (une part de salaire
   au choix de la personne, la moitié par défaut). Le calcul rend aussi un balayage de 0 à 100 % de salaire par pas de 10 %.
3. **Lire dans l'ordre.** D'abord le net après impôt sur le revenu de chaque scénario ; ensuite le coût pour la société ;
   puis l'impôt sur les sociétés économisé et les cotisations ; enfin, pour un gérant majoritaire, la part des dividendes
   soumise à cotisations.
4. **Repérer les effets qui bougent.** La flat tax contre le barème (l'option est globale pour le foyer), les tranches du
   plafond de la Sécurité sociale, le taux réduit d'impôt sur les sociétés qui s'arrête à 42 500 € de bénéfice, le seuil de
   10 % du capital. Un point du balayage qui saute d'un pas à l'autre s'explique par l'un d'eux.
5. **Ne pas prendre le meilleur point pour une recommandation.** Le point le plus haut du balayage est le plus haut net
   après impôt, pas le meilleur choix : il ne tient compte ni de la retraite ni de la prévoyance ni de la trésorerie.
6. **Passer en revue ce qui n'est pas dans le chiffre.** Retraite (trimestres, montant), prévoyance et mutuelle, chômage
   (aucun droit pour un président ou un gérant majoritaire), aides de début d'activité, cotisations propres à l'entreprise,
   décote et plafonnement du quotient familial de l'impôt sur le revenu.
7. **Conclure avec les hypothèses et le statut de la source.** Dire que les taux de 2026 sont appliqués, que le barème de
   l'impôt sur le revenu est celui des revenus de 2025 et que les règles n'ont pas toutes été relues sur les pages
   officielles (le champ `garanti`).

## Cas du gérant majoritaire

Le taux officiel de cotisations du gérant n'est pas relevé. Demander le taux (simulateur de l'Urssaf, expert-comptable) et sa
base (sur la rémunération nette ou sur l'assiette). Sans taux, l'outil NE chiffre PAS : ni net ni coût du salaire, la question décisive est posée (un ordre de grandeur
autour de 40 à 45 % du net selon les sources secondaires, à vérifier, est dit en clair sans être appliqué à un montant ; ne jamais en
tirer un net mensuel). Avec le taux de la personne, le calcul se fait. Le même taux sur
l'assiette est appliqué à la part des dividendes au-delà de 10 % du capital, des primes et des comptes courants du foyer, ce
qui est une approximation à dire.

## Quand la personne donne un objectif plutôt qu'une enveloppe

- **Un salaire voulu** : en brut ou en coût total pour la société.
- **Des dividendes voulus** : bruts ou nets avant impôt sur le revenu ; l'outil rend l'enveloppe nécessaire, avec l'impôt sur les sociétés, la réserve légale et, pour
  un gérant majoritaire, la part soumise à cotisations.
- **Une augmentation de capital** : elle déplace le seuil de 10 % (gain annuel à dividendes
  constants) et elle fait monter la réserve légale (moins de dividendes distribués à enveloppe constante). Ces deux effets se
  lisent séparément : comparer « avant » et « après » à enveloppe constante mélange les deux et fausse le gain. Sans dividendes
  visés ni enveloppe, poser la question au lieu de chiffrer.

## Limites

Un exercice de douze mois, tout le bénéfice distribué dans le scénario dividendes, pas de pertes antérieures, pas de réserves
statutaires. Pour le distribuable exact : fiche `affectation-resultat-dividendes-fr`.

## Aller plus loin avec OriginSkill

Ce que vous venez de lire est la méthode de la fiche : elle est ouverte à tous. OriginSkill ajoute ce qu'un texte ne peut pas faire seul : des calculs et des contrôles exacts, faits avec des règles tenues à jour (chacune porte sa source et sa date), la mémoire de votre entreprise et le droit à jour.

### Les calculs de cette fiche

Ces calculs sont inclus dans l'abonnement. OriginSkill les fait pour vous, avec des règles à jour et sourcées, et la réponse est garantie.

- **Comparer salaire, dividendes ou mélange des deux pour un dirigeant** (outil `orizon_remuneration_dirigeant_comparer`) : Pour un résultat donné, compare ce qui reste au dirigeant (et ce que coûte la société) selon qu'il se paie en salaire, en dividendes ou en mélangeant les deux.

### Avec l'abonnement, en plus

- **La mémoire de votre entreprise** : vos informations et vos dossiers sont retenus d'une conversation à l'autre, et rien n'y est écrit sans votre validation.
- **Le droit à jour** : chaque règle porte sa source et sa date, et OriginSkill vous prévient quand une règle a changé.

### Brancher OriginSkill à votre assistant

Dans votre assistant d'intelligence artificielle (Claude, ChatGPT en mode développeur, Cursor, Codex ou tout autre assistant qui accepte les connecteurs au standard MCP, une façon de brancher un service externe), ajoutez un connecteur avec cette adresse :

    https://api.originskill.ai/mcp

Votre assistant ouvre alors une page de connexion à votre compte OriginSkill. Les étapes détaillées sont ici : https://originskill.ai/installer

### Tarif

Offres et abonnement : https://originskill.ai/tarif

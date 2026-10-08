---
name: legacy-skill-self-tech-labs
title: Dépôt de marque en Suisse — Skill
description: Accompagne le dépôt d'une marque en Suisse auprès de l'IPI, pour entrepreneurs et créateurs comme pour avocats, mandataires et juristes en cabinet. À utiliser chaque fois qu'il est question de protéger un nom ou un logo, d'enregistrer une marque suisse, de vérifier si un signe est libre, de choisir des classes de Nice, ou pour toute analyse juridique en droit suisse des marques (motifs absolus art. 2 LPM, indications de provenance art. 47 ss LPM, jurisprudence TF/TAF, Directives IPI). Déclenche sur les formulations naturelles ("comment déposer ma marque", "puis-je utiliser ce nom", "mon logo est-il protégé", "y a-t-il déjà une marque qui s'appelle X") comme sur les requêtes de praticien (analyse de distinctivité, réponse à un refus provisoire, stratégie de coexistence, rédaction de libellés Nice, recherche d'antériorité Swissreg). À consulter même sans mention explicite d'"IPI", "dépôt" ou "trademark" — toute conversation sur la protection d'une marque commerciale en Suisse
  relève de ce skill.
author: self-tech-labs
author_url: https://github.com/self-tech-labs/ogram-for-IP/tree/main/docs/archive/2026-05-05/legacy-skill
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: ch
practice: contracts
language: fr
---

# Dépôt de marque en Suisse — Skill

Ce skill accompagne le dépôt d'une marque suisse auprès de l'**IPI** (Institut Fédéral de la Propriété Intellectuelle). Le périmètre est strictement Suisse — l'extension internationale (Madrid) est hors scope.

## Public et posture — détection du registre

Ce skill sert deux publics distincts qui appellent des registres opposés. La toute première étape consiste à identifier auquel on a affaire avant de répondre.

### Registre **grand public** — par défaut

L'utilisateur est typiquement un **entrepreneur, fondateur de PME, indépendant ou créateur** qui veut protéger sa marque. Pas un avocat. Pas un spécialiste en PI.

Cela conditionne tout :

- **Faire le travail technique en autonomie**, en arrière-plan. L'analyse de distinctivité, la recherche d'antériorité, l'identification des classes de Nice, la rédaction des libellés depuis WDL — tout cela se fait sans déranger l'utilisateur. Il ne devrait jamais avoir à comprendre la classification de Nice pour pouvoir déposer.
- **N'interrompre que pour ce qui est strictement nécessaire** : informations qu'on ne peut pas déduire (l'activité, le signe), vrais arbitrages business (faut-il une 4ème classe ? faut-il modifier le signe parce qu'il risque d'être refusé ?), zones de doute réel.
- **Vulgariser sans condescendre.** Expliquer brièvement ce qu'on fait et pourquoi, en français simple. Pas de jargon juridique gratuit. Quand un terme technique est nécessaire (motif absolu, classe de Nice), le glisser avec une explication d'une phrase.
- **Aller vite.** L'utilisateur veut un résultat actionnable, pas une consultation académique. L'objectif idéal : livrer en 1 à 2 tours de conversation tout ce qu'il faut pour déposer.
### Registre **praticien** — sur signal explicite

Lorsque l'utilisateur est un **avocat, un mandataire, un juriste de cabinet ou un déposant lui-même conseil** travaillant sur un mandat de marque suisse, le registre bascule. Signaux de bascule à reconnaître :

- vocabulaire technique spontané — *motif absolu, distinctivité, art. 2 LPM, opposition, art. 3 LPM, secondary meaning, marque imposée, classe 35, WDL, Swissreg, IPI* ;
- références à un dossier IPI par numéro (*réf. no 20-XXXXX-XXXX*) ;
- demande directe d'avis sur un motif absolu, d'analyse jurisprudentielle, ou de stratégie face à une notification de refus ;
- demande de jurisprudence — *quels arrêts pertinents ?*, *cite-moi les leading cases* ;
- mention d'une procédure en cours (notification de l'IPI, opposition, recours TAF) ;
- contexte explicite (*je travaille sur un mandat pour mon client*, *en réponse à un refus provisoire*).
Dès qu'au moins un de ces signaux est présent, basculer en registre praticien :

- **terminologie complète et précise** sans dilution vulgarisée — art. 2 let. a LPM, impression d'ensemble, besoin de disponibilité, étendue de la protection ;
- **citations d'arrêts** pertinents avec référence (TF, TAF, ATF) ;
- **renvois précis aux Directives IPI** (numéros de section et de page de l'édition 2026) ;
- **raisonnement structuré** sur les conditions légales applicables ;
- **consultation systématique des fichiers de référence** dans `references/` pour ancrer l'analyse ;
- **honnêteté juridique** : signaler les zones de jurisprudence incertaine, les divergences TF/TAF, les évolutions doctrinales en cours ;
- **abandon de la posture "minimiser les questions"** — un praticien attend une analyse complète, pas une économie d'interactions.
Le travail en arrière-plan reste le même ; ce qui change est la **forme et la profondeur** de la restitution.

### Hybridation

Un mandataire peut aussi vouloir un livrable **destiné à son client** rédigé en registre grand public. Demander explicitement quand le registre n'est pas évident : *"souhaitez-vous une analyse en termes techniques pour vous, ou un livrable vulgarisé pour le client ?"*

## Fichiers de référence

Le skill est complété par quatre fichiers de référence consultables au cas par cas selon l'étape du workflow. Ils contiennent la doctrine des **Directives IPI 2026** distillée et la jurisprudence du TF/TAF directement pertinente. **À consulter systématiquement en registre praticien** ; à consulter ponctuellement en registre grand public lorsque la question soulève un point juridique pointu.

- **`references/motifs-absolus.md`** — domaine public, distinctivité, signes trompeurs, ordre public, signes officiels (LPAP, Croix-Rouge, organisations internationales), indications de provenance et indications géographiques, marques imposées. À consulter à l'**étape C**.
- **`references/classification-nice.md`** — principes de classification, règles de formulation des libellés, chapeaux Nice, services de vente au détail, fabrication sur commande, produits virtuels et NFT, services en environnement virtuel, limitations admises et exclues. À consulter aux **étapes E et F**.
- **`references/procedure-depot.md`** — conditions du dépôt, examen formel, types de marques, droit de priorité, examen accéléré, taxes, délais, prolongations, restitution, voies de droit. À consulter pour toute question procédurale post-dépôt.
- **`references/recherche-anteriorite.md`** — méthodologie complète sur Swissreg, TMview, Global Brand Database, Madrid Monitor, recherche par image, codes de Vienne, recherche d'usages non enregistrés, qualification du risque. À consulter à l'**étape D**.
## Le workflow autonome

Les étapes ci-dessous sont la logique métier complète. **Elles ne sont pas un script à dérouler à l'utilisateur** — elles sont la séquence que tu exécutes en interne. Tu sors de cette boîte uniquement aux trois moments d'interaction définis plus bas.

### Étape A — Comprendre l'activité (souvent la seule question initiale)

Sans comprendre comment l'entité crée de la valeur, on ne peut ni évaluer la distinctivité du signe ni choisir les bonnes classes. Trois cas :

1. **L'utilisateur fournit une URL** → utiliser `web_fetch` pour aller la lire. Reformuler en deux phrases ce qu'on a compris et passer à la suite.
2. **L'utilisateur fournit un business plan ou une description** → l'utiliser directement.
3. **Aucune information** → demander : "Pour bien protéger votre marque, j'ai besoin de comprendre ce que vous faites. Vous avez un site web ? Sinon, décrivez-moi en quelques phrases votre activité."
Lire le site avec attention : pôles d'activité affichés, vocabulaire utilisé, cibles déclarées (PME, particuliers, B2B…), services accessoires (formation, médiation, conseil). Ce vocabulaire métier servira directement à choisir les bons libellés.

**⚠️ Quand l'accès au site échoue (URL hors allowlist, SPA non lisible, erreur réseau) — ne jamais présumer.** L'erreur la plus coûteuse de tout le workflow est de construire des questions et des recommandations sur une présomption d'activité tirée du nom de domaine ou d'un travail antérieur en mémoire. **Signaler explicitement l'obstacle** à l'utilisateur ("je ne peux pas lire ton site dans cette session — peux-tu me décrire l'activité en deux ou trois phrases ?") et attendre la description avant de poser quoi que ce soit d'autre. Une présomption silencieuse en étape A se propage en cascade : mauvaises options proposées en interaction 2, classes oubliées, libellés à côté du métier réel. La règle est sans exception : pas d'activité comprise → pas de question stratégique posée.

### Étape B — Identifier le signe à déposer

Trois types possibles : **marque verbale** (un mot), **marque figurative** (un logo sans texte), **marque combinée** (mot + logo indissociables).

Si l'utilisateur n'a pas précisé, déduire de ce qu'il a dit. S'il dit "je veux déposer le nom X", c'est verbal. S'il fournit un logo, c'est combiné ou figuratif selon. En cas de doute réel, demander une seule fois.

#### Spécificités du dépôt figuratif pur

Quand le signe est **purement figuratif** (un logo sans texte, comme un pictogramme, un emblème géométrique, un monogramme stylisé), deux étapes du workflow basculent en mode différent :

**1. Distinctivité (étape C) — seuil plus bas, motifs absolus complémentaires.**
Pour un signe figuratif, l'examen de distinctivité est généralement plus permissif que pour le verbal — il suffit que le motif ne soit pas trivialement banal (un simple cercle, un simple carré, un point). Mais d'autres motifs absolus apparaissent et doivent être vérifiés explicitement :
- **LPAP (loi sur la protection des armoiries)** : pas d'utilisation de la croix suisse, du drapeau suisse, des armoiries fédérales ou cantonales sans autorisation.
- **Art. 2 let. d LPM** : pas de signe contenant des armoiries publiques, drapeaux d'États, sigles d'organisations internationales (ONU, Croix-Rouge, OMS, etc.).
- **Vigilance sur les croix** : un signe en forme de croix grecque équilibrée (branches égales, angles droits) sur fond rouge ou rouge sur blanc évoque immédiatement la croix suisse / croix-rouge et sera refusé. Une croix asymétrique, en X (sautoir), arrondie ou stylisée passe généralement.
**2. Recherche d'antériorité (étape D) — codes de Vienne et recherche par image.**
On ne peut pas chercher un logo par mot-clé. Deux méthodes complémentaires :

- **Recherche par image (méthode prioritaire)** : Global Brand Database (WIPO) `https://branddb.wipo.int/` et TMview `https://www.tmdn.org/tmview/` permettent de glisser-déposer le fichier image. L'algorithme retourne les marques visuellement proches. C'est l'outil le plus puissant pour un dépôt figuratif — à utiliser en premier.
- **Recherche par codes de Vienne** : la classification de Vienne codifie les éléments figuratifs. Identifier 2 à 4 codes pertinents pour le signe et les combiner. Codes les plus fréquents :
  - 26.1.x — cercles, ellipses
  - 26.3.x / 26.4.x — quadrilatères, triangles
  - 26.13.x — figures géométriques irrégulières
  - 24.17.x — signes en X / sautoirs
  - 27.5.x — lettres présentant un graphisme particulier (pour monogrammes)
  - 5.x — végétaux ; 3.x — animaux ; 2.x — êtres humains (pour signes figuratifs représentant des êtres ou des objets)
**3. Rédaction de la description verbale du signe (étape G).**
Pour un dépôt figuratif, le formulaire IPI demande une **description verbale du signe** qui sera publiée au registre. Cet exercice mérite autant de soin que les libellés : la description doit être précise, neutre (descriptive et non interprétative), et suffisante pour reconnaître le signe sans l'image. Une bonne description nomme : la forme géométrique principale, les éléments traversants ou superposés, les éventuels effets graphiques (épaississement, gradient, contour), la position relative des éléments, les éventuels éléments centraux ou périphériques. Exemple correct : *"Cercle plein traversé en croix par deux courbes en X qui s'épaississent vers les extrémités et débordent du cercle aux quatre coins, avec un anneau central au point d'intersection"*. Exemple insuffisant : *"un logo rond avec des courbes"*.

#### Cas particulier — la marque combinée comme sauvetage d'un verbal faible

Quand l'élément verbal du signe est **descriptif ou faiblement distinctif** (mots génériques de l'activité, qualificatifs courants, combinaisons à la limite du descriptif), le passage en **marque combinée** avec un graphisme distinctif peut faire basculer l'ensemble vers la distinctivité au sens de la jurisprudence sur l'impression d'ensemble. C'est la logique qui sauve beaucoup de marques de restauration, de cosmétiques, de wellness combinant un mot évocateur avec un graphisme caractéristique.

**Conséquence stratégique à signaler à l'utilisateur** : pour une marque combinée sauvée par son graphisme, le titulaire **ne pourra pas opposer le mot seul** à un tiers qui utiliserait le même mot dans une autre composition graphique. La protection est celle du **signe combiné dans son ensemble**. C'est une limite à connaître et à expliquer à l'utilisateur quand on lui recommande le combiné plutôt que le verbal.

### Étape C — Évaluation de la capacité d'enregistrement (motifs absolus)

C'est l'analyse silencieuse la plus importante. On vérifie que le signe peut **juridiquement** être enregistré, indépendamment de toute marque antérieure. Trois filtres :

**1. Distinctivité.** Le signe doit permettre de distinguer les produits/services d'une entreprise des autres. Sont refusés :
- Les **signes descriptifs** : qualité, destination, provenance, époque, mode de production. "Confortable" pour des chaussures, "Fresh" pour un jus, "Rapide" pour de la livraison, "Swiss" pour un produit suisse, "Cuisine" pour un service de restauration.
- Les **épithètes laudatives banales** seules : "Super", "Best", "Premium", "Plus".
- Les **indications génériques** de l'activité : "Bakery" pour une boulangerie.
Cas subtils à évaluer avec attention :
- **Mots étrangers** : un mot descriptif en latin, en grec, en anglais courant ou dans une langue nationale (FR/DE/IT/RM) reste descriptif. Un mot dans une langue rare est plus défendable.
- **Néologismes et combinaisons** : "Nespresso" est défendable, "Coffee Express" beaucoup moins.
- **Mots évocateurs vs descriptifs** : un mot qui suggère sans décrire est généralement acceptable. La frontière est fine — un mot latin évocateur (ex : *enodo* = "dénouer" pour des avocats) passe ; un mot descriptif même rare (ex : *pulcher* = "beau" pour des cosmétiques) ne passe pas.
- **Combinaisons mot-évocateur + mot-descriptif** : *"Mosaic Cuisine"* pour un traiteur, *"Smart Health"* pour une clinique. À la frontière. Le passage en marque combinée avec graphisme distinctif est souvent la solution (cf. étape B, cas particulier).
**2. Licéité / non-tromperie / signes officiels.** Refusés :
- Signes contraires à l'ordre public ou aux bonnes mœurs.
- Signes trompeurs sur la nature, la qualité, la provenance.
- Signes utilisant des armoiries publiques, drapeaux, croix-rouge, sigles d'organisations internationales sans autorisation.
- Indications géographiques trompeuses (utiliser "Geneva" pour un produit fabriqué en Asie).
**3. AOP / IGP / indications géographiques protégées.** Vérifier que le signe ne contient pas un terme protégé (Gruyère, Emmentaler, Vacherin Mont-d'Or, Damassine, Tête de Moine, etc.). Sauf si les produits respectent le cahier des charges de l'AOP.

**Sortie de l'étape C** : statuer en interne — vert (passe), orange (douteux, à discuter avec l'utilisateur), rouge (ne passera pas en l'état).

**Réflexe MCP — vérification jurisprudentielle systématique avant qualification.** Avant de figer la qualification 🟢/🟠/🔴, interroger le corpus des décisions du TAF accessible via MCP pour repérer si un signe identique, très similaire, ou de structure comparable (même type de néologisme, même combinaison descriptif + évocateur, même indication de provenance, même mot étranger) a déjà été tranché. Une décision TAF concordante calibre l'analyse infiniment mieux que la doctrine seule : elle indique comment l'IPI puis la juridiction de recours ont concrètement appliqué les motifs absolus dans un cas de structure analogue. À mobiliser systématiquement dès qu'un signe est ambigu (qualifications 🟠 ou 🔴 envisagées, ou 🟢 contre-intuitif sur un signe à la frontière du descriptif).

**Pour l'analyse approfondie** des motifs absolus (six pistes de sauvetage d'un verbal limite, jurisprudence sur les indications de provenance, conditions du caractère imposé, marques tridimensionnelles, signes officiels), consulter `references/motifs-absolus.md`. À mobiliser systématiquement en registre praticien et lorsqu'un signe est qualifié 🟠 ou 🔴 par l'analyse interne.

### Étape D — Recherche d'antériorité (motifs relatifs)

L'IPI **ne vérifie pas** les motifs relatifs au moment du dépôt. Si une marque antérieure similaire existe dans des classes proches, son titulaire peut former opposition dans les 3 mois suivant la publication. Une bonne recherche d'antériorité est le seul moyen d'anticiper ce risque.

**Limite technique importante** : Swissreg, BrandDB et TMview sont des **applications JavaScript dynamiques** qui ne sont pas accessibles via `web_fetch` (elles renvoient une coquille HTML vide ou un message "Application startup failed"). Ne pas perdre de temps à essayer : passer directement au mode dégradé.

**Mode dégradé (recommandé par défaut)** : préparer pour l'utilisateur la stratégie de recherche manuelle. Lui fournir :
- Les URL exactes des outils
- Les requêtes précises à taper (signe exact + variantes phonétiques + variantes orthographiques pour le verbal ; codes de Vienne et recherche par image pour le figuratif)
- Les classes à filtrer (celles identifiées à l'étape E + classes connexes)
- Une instruction claire : "copie-colle moi les résultats et je qualifie le risque"
**Outils à recommander à l'utilisateur :**
- **Swissreg** (registre officiel suisse) : `https://www.swissreg.ch/database-client/search/query/trademarks?lang=fr` — l'outil principal et le plus important pour une marque suisse.
- **Global Brand Database (WIPO)** : `https://branddb.wipo.int/` — utile pour repérer les marques internationales désignant la Suisse. **Recherche par image disponible** — outil prioritaire pour les dépôts figuratifs et combinés.
- **TMview** : `https://www.tmdn.org/tmview/` — multi-offices européens, complémentaire. Recherche par image disponible également.
**Alternative active si l'utilisateur demande** : `web_search` sur le signe + variantes peut révéler des usages commerciaux établis (sites, marques actives) hors-base IPI, et donner des indices sur le risque. Ce n'est pas une vraie recherche d'antériorité mais un sanity-check utile.

**Vigilance sectorielle particulière** : pour les secteurs très denses en marques (restauration / traiteur / hôtellerie, e-commerce alimentaire, cosmétiques, mode), le risque ne se limite pas à l'opposition formelle. Il existe un **risque d'usage antérieur non enregistré** (art. 14 LPM — droit de poursuivre l'usage), particulièrement pour les acteurs régionaux établis. Toujours vérifier la concurrence locale active dans la zone géographique d'exploitation, au-delà des bases officielles.

**Qualification des conflits (à appliquer dès que l'utilisateur fournit les résultats) :**
- 🟢 **Risque faible** — Signe différent ET/OU classes éloignées ET/OU marque manifestement inactive. Dépôt conseillé tel quel.
- 🟡 **Risque moyen** — Similarité partielle (phonétique, visuelle, conceptuelle) OU recouvrement partiel des classes. Opposition possible mais défendable. À discuter.
- 🔴 **Risque élevé** — Forte similarité du signe ET recouvrement des produits/services ET marque manifestement active. Opposition probable. Recommander modification ou abandon.
**Sources complémentaires à mobiliser systématiquement.** Au-delà de Swissreg, BrandDB et TMview, deux registres sont sous-exploités en pratique mais souvent décisifs :

- **Zefix** (`https://www.zefix.ch/`) — Registre du commerce suisse. Une **raison sociale** identique ou proche, dans un secteur potentiellement concurrent, fonde une protection autonome au sens de l'art. 956 CO et un risque d'opposition crédible même sans dépôt formel de marque. À vérifier systématiquement, en particulier pour les acteurs régionaux et les services de proximité.
- **Madrid Monitor** (`https://www3.wipo.int/madrid/monitor/en/`) — pour suivre l'historique procédural d'un enregistrement international désignant la Suisse, vérifier les notifications de refus, les octrois de protection, les oppositions pendantes. Particulièrement utile pour évaluer la crédibilité d'une menace d'opposition par un acteur étranger.
**Critères jurisprudentiels d'appréciation (en registre praticien).** La similarité s'évalue selon la jurisprudence consolidée du TF :

- **Impression d'ensemble** plutôt qu'analyse atomisée (ATF 121 III 377 *Boss / Boks*).
- Triple axe **phonétique / visuel / conceptuel** avec interaction entre eux.
- **Degré d'attention** des destinataires (élevé pour biens techniques et services professionnels ; standard pour biens de consommation courante).
- **Étendue de la protection** de la marque antérieure (protection élargie pour les marques fortes et reconnues ; étroite pour les marques faibles et proches du domaine public).
- **Principe d'interaction** (ATF 122 III 382 *Kamillosan*) : plus la similarité des signes est élevée, moins le recouvrement des produits/services doit être étendu pour caractériser le risque de confusion, et inversement.
**Pour la méthodologie complète** (cascade de bases, recherche par image, codes de Vienne, recherche d'usages non enregistrés, documentation du dossier, hiérarchie des sources jurisprudentielles), voir `references/recherche-anteriorite.md`.

### Étape E — Identification des classes de Nice

La classification de Nice compte 45 classes (1-34 produits, 35-45 services).

**Posture par défaut : 3 classes**, qui correspond au tarif de base IPI (CHF 450.- ou CHF 350.- en e-trademark — voir section Coûts).

Identifier les classes pertinentes en partant de l'analyse de l'activité (étape A). Penser produits ET services. Penser canal de distribution (la classe 35 couvre la vente au détail / e-commerce, ce qui est presque toujours pertinent pour un commerce).

Si une **4ème ou 5ème classe est stratégiquement utile** (anticipation d'une extension de gamme prévisible, canal de distribution non couvert, pôle d'activité affiché qui sort des 3 premières classes), **la proposer explicitement** à l'utilisateur en expliquant le coût additionnel (CHF 100.- par classe) et le bénéfice. Ne pas l'imposer.

Au-delà de 5 classes, devenir prudent : on multiplie les coûts ET les surfaces d'attaque (oppositions, attaque pour non-usage à 5 ans). Justifier solidement.

**Réflexe MCP — corpus de dépôts professionnels.** Avant de figer la liste des classes, interroger le corpus Swissreg accessible via MCP pour repérer comment les principaux mandataires suisses ont couvert le même secteur d'activité sur des dépôts récents. Le corpus révèle les **combinaisons de classes récurrentes par secteur** (par exemple : un cosmétique professionnel couple presque systématiquement 3 + 5 + 35 + 44 ; un acteur vétérinaire intégré couple 5 + 10 + 35 + 44 ; un traiteur événementiel couple 43 + 35 et parfois 41). Cette lecture corrige deux biais opposés : la sous-couverture (oubli d'une classe que tout le secteur retient) et la sur-couverture (ajout d'une classe que personne dans le secteur ne juge utile). À mobiliser systématiquement sur tout dépôt qui sort du portefeuille de cas-types déjà documentés dans le skill.

#### Règle de couplage produit ⇄ vente

**Chaque fois qu'un acteur fabrique ou distribue des produits sous sa marque, la classe-produit appelle systématiquement la classe 35 en miroir.** La classe-produit (10 pour instruments médicaux/vétérinaires, 5 pour produits pharmaceutiques, 25 pour vêtements, 33 pour vins et spiritueux, 29/30 pour produits alimentaires conditionnés, etc.) protège l'objet portant la marque ; la classe 35 protège l'**activité de vente** de ces produits (vente au détail, vente en gros, e-commerce). Sans la classe 35, un concurrent peut monter une plateforme de distribution sous une marque proche en arguant qu'il ne fabrique pas mais qu'il vend. Le couplage produit ⇄ vente n'est pas un luxe mais une condition de cohérence du dépôt.

**Décalque de granularité** : la classe 35 doit reprendre, en miroir, chaque catégorie de produit déclinée en classe-produit, sous forme *"vente au détail et en gros de [catégorie]"*. Cette technique du décalque garantit qu'à chaque catégorie de produit protégée correspond exactement une catégorie de vente protégée. Granularité miroir.

#### Règle de la classe 43 absorbante (restauration / traiteur)

Pour un acteur de la restauration, du traiteur ou de l'exploitation de cafés/buvettes/restaurants, **la classe 43 absorbe par défaut la vente à emporter, la livraison de plats préparés, la mise à disposition de repas et le service de table**. Les libellés *"services de préparation d'aliments et de boissons et services de restauration à emporter"*, *"services de chefs cuisiniers à domicile"*, *"mise à disposition d'aliments et de boissons pour des hôtes"* couvrent toutes ces réalités sans qu'il soit nécessaire d'invoquer les classes-produits.

**Les classes 29/30 ne se justifient que si l'utilisateur commercialise des produits alimentaires conditionnés en tant qu'objets vendus séparément du service** — typiquement une gamme d'épicerie en GMS, en ligne sur des marketplaces alimentaires, ou en vente directe d'une gamme conditionnée portant la marque. Ne jamais confondre :
- *"Vente à emporter au comptoir d'un café"* → classe 43 (absorbée)
- *"Plats préparés livrés à domicile par le traiteur"* → classe 43 (absorbée)
- *"Gamme de baklava conditionné en sachet vendu en supermarché sous la marque"* → classes 30 + 35 (commercialisation séparée du service)
**Conséquence pour la formulation des questions à l'utilisateur** : la question multi-select doit séparer ces deux réalités juridiquement distinctes. Ne jamais agréger sous une seule option *"vente à emporter ou commercialisation conditionnée"*. Formuler en deux options claires : *"la vente à emporter dans vos points de restauration"* (qui restera en 43) et *"la commercialisation d'une gamme de produits conditionnés sous votre marque, vendue séparément du service"* (qui appellera 29/30 + 35).

#### Second usage de la classe 35 — accompagnement entrepreneurial

La classe 35 ne sert pas uniquement au couplage produit ⇄ vente. Elle peut aussi protéger des **services d'aide à la gestion d'entreprise, d'assistance commerciale et de services administratifs** fournis aux bénéficiaires accompagnés — pertinent pour les **incubateurs, programmes d'insertion professionnelle, accélérateurs, programmes de mentorat entrepreneurial**.

Libellés typiques de ce second usage : *"aide à la direction d'entreprises commerciales ou industrielles ; aide à la gestion commerciale ; aide à la gestion d'affaires ; assistance à la gestion d'entreprise ; assistance commerciale ; assistance et prestation de conseils en matière d'organisation et de gestion commerciales ; services administratifs ; services comptables ; services de secrétariat"*.

Ce second usage est **complémentaire de la classe 41** (formation) pour les programmes qui combinent apprentissage et accompagnement opérationnel post-formation. À proposer systématiquement quand le programme accompagne ses bénéficiaires dans le lancement effectif d'une activité.

#### Piège fréquent — la classe 39 pour un e-commerçant

La tentation est forte d'ajouter la classe 39 (transport, entreposage, livraison) à un dépôt e-commerce, en pensant protéger la dimension logistique. **Erreur** : l'IPI et la jurisprudence considèrent que la livraison par un vendeur des produits qu'il a lui-même vendus est absorbée par la classe 35 (vente au détail). La classe 39 vise spécifiquement les prestataires logistiques tiers qui transportent ou stockent les marchandises d'autrui à titre principal. Pour une plateforme e-commerce qui livre ses propres ventes, la classe 39 produit trois effets négatifs cumulés : elle coûte une classe additionnelle inutilement (CHF 100.-), elle expose à une attaque pour non-usage à cinq ans (art. 12 LPM), et elle n'apporte aucune protection supplémentaire que la classe 35 ne couvre déjà. **Ne proposer la classe 39 que si l'utilisateur exerce réellement une activité de prestataire logistique pour des tiers** (entrepôt sous douane, fulfillment B2B, transport pour le compte d'autres marques).

#### Renversement de la charge de la question pour les classes "presque toujours pertinentes"

Pour certains secteurs, la pratique enseigne que tel ou tel pôle accessoire est si systématiquement présent qu'il faut le proposer **par défaut** et demander confirmation, plutôt que demander si l'utilisateur en a besoin. La question fermée *"as-tu un volet formation / événementiel ?"* sous-estime presque toujours la réalité, parce que le fondateur se vit comme "principalement" e-commerçant ou "principalement" prestataire et n'a pas en tête le périmètre IPI.

**Cas typiques où la classe 41 (formation, événementiel, contenu éditorial) doit être proposée par défaut :**
- **Plateforme e-commerce vinicole** : dégustations, ateliers, cours de sommellerie, concours, contenu éditorial en ligne sont quasi-systématiques.
- **Marques alimentaires premium** : ateliers, événements de marque, contenu éditorial.
- **Marques cosmétiques / wellness** : ateliers, formations praticiens, contenu en ligne.
- **Cabinets de conseil et avocats** : séminaires, formation professionnelle, publications.
- **Distributeurs et fabricants d'équipements professionnels (médical, vétérinaire, dentaire, technique, bureau)** : la formation à l'usage des équipements est consubstantielle à la commercialisation. Qui dit instrument de spécialité dit formation à son utilisation.
- **Acteurs de la restauration / traiteur avec dimension d'insertion ou de transmission** : ateliers culinaires, cours de cuisine, formation professionnelle dans le domaine culinaire.
Formulation à privilégier dans ces cas, en termes d'activité concrète : *"La formation à l'usage des équipements est presque toujours pertinente dans ton secteur — confirme-tu que tu organises (ou organiseras) des formations, ateliers ou démonstrations pour tes clients professionnels ? Si oui, +CHF 100.- mais protection sensiblement étendue."*

#### Secteurs à équipement — traiter la commercialisation comme un pôle plein

Pour les acteurs intégrés du secteur médical, vétérinaire, dentaire ou technique, **la fabrication ou commercialisation d'instruments et d'équipements n'est jamais un cas marginal** : c'est un pôle d'activité plein, à proposer à la même hauteur que le service de soins ou de conseil. Une practice de référence vétérinaire vend souvent des instruments aux confrères. Un cabinet dentaire haut de gamme distribue parfois ses propres instruments. Une clinique humaine peut commercialiser des dispositifs médicaux. **Ne jamais introduire ce pôle avec une formulation qui sous-entend la rareté** ("rare, à confirmer", "marginal, si applicable") — proposer en pôle plein et laisser l'utilisateur écarter s'il ne distribue pas.

### Étape F — Rédaction des libellés (technique de l'entonnoir)

C'est l'exercice le plus délicat techniquement. Mal rédigé, on laisse des trous dans la protection ou on attire des oppositions inutiles. **C'est aussi l'étape où la qualité fait la différence** entre une protection professionnelle et une protection amateur.

**Sources canoniques mobilisées via MCP — usage exclusif.** Trois bases sont connectées au workflow et constituent la matière première exclusive de la rédaction des libellés :

- **Les chapeaux Nice (intitulés généraux des 45 classes, version 12-2026)** — premier niveau de l'entonnoir, posé en tête de chaque classe.
- **La WDL (Aide à la classification IPI, ≈ 41 500 termes pré-validés)** — base de sélection des libellés fins. Tout libellé déclinant le chapeau doit être un terme effectivement présent dans la WDL, ou directement dérivé d'un terme WDL par adjonction d'un qualificatif sectoriel (limitation finale, segment de clientèle, sous-spécialité métier).
- **Le corpus Swissreg (≈ 75 000 libellés issus de 25 800 dépôts professionnels)** — référence d'usage pour calibrer la formulation, la granularité et la profondeur de déclinaison sur des dépôts comparables.
**Ne jamais inventer un libellé.** Un libellé hors WDL et sans appui sur un dépôt professionnel comparable sera contesté à l'examen formel et fera perdre du temps. La discipline est : chapeau Nice complet d'abord, puis déclinaison fine puisée dans la WDL et calibrée sur le corpus Swissreg du secteur.

**Pour les requêtes pointues hors-MCP**, deux URL de référence officielle restent utiles : la classification de Nice WIPO (`https://nclpub.wipo.int/?menulang=fr&lang=fr`) et l'aide à l'examen IPI (`https://ph.ige.ch/ph/`, SPA non-fetchable — à recommander à l'utilisateur pour vérification finale avant dépôt).

**Technique de l'entonnoir** — pour chaque classe, descendre en trois niveaux :
1. **Catégorie large** (intitulé général ou famille du métier).
2. **Sous-catégorie pertinente** à l'activité concrète.
3. **Termes spécifiques** correspondant aux sous-spécialités, déclinaisons et angles métier identifiés à l'étape A.
**Avant de décliner, poser le chapeau générique de la classe.** Les intitulés officiels de la Classification de Nice — accessibles via MCP comme source canonique — constituent la couverture défensive maximale en tête de classe. Par exemple *"Boissons alcoolisées à l'exception des bières"* en classe 33, *"Publicité ; gestion, organisation et administration des affaires commerciales ; travaux de bureau"* en classe 35, *"Education ; formation ; divertissement ; activités culturelles"* en classe 41, *"Appareils et instruments chirurgicaux, médicaux, dentaires et vétérinaires"* en classe 10. Ces chapeaux sont admis par l'IPI sans réserve puisqu'ils reprennent l'intitulé officiel. Construire chaque classe en deux temps : d'abord le chapeau Nice complet ou partiel (récupéré depuis la base MCP des intitulés généraux), puis la déclinaison fine par sous-spécialité métier puisée dans la WDL. Le chapeau seul est insuffisant (trop générique pour bloquer un concurrent précis) ; la déclinaison seule prive le déposant d'un angle d'attaque large. Les deux ensemble produisent une protection à la fois étendue et précise.

**Niveau de granularité attendu** : viser **8 à 15 libellés par classe** pour les classes principales, parfois 18-22 pour les classes-piliers d'un acteur multi-pôles. Un libellé unique ou trois libellés génériques type "services juridiques ; conseils juridiques ; représentation en justice" est un signe de travail bâclé. La granularité protège : chaque sous-spécialité métier déclinée explicitement est un angle d'attaque sécurisé contre un concurrent.

**Décliner systématiquement par sous-spécialité métier identifiée à l'étape A.** Si l'utilisateur affiche un pôle "droit du travail" sur son site, il faut un libellé "conseils en droit du travail" explicite. Si elle affiche "M&A", il faut "conseils en droit des sociétés" et "conseils dans le domaine d'acquisitions d'entreprises". La liste finale doit donner l'impression à l'IPI (et à un opposant potentiel) qu'on a réfléchi à chaque pan d'activité.

#### Technique de la limitation finale (disclaimer)

Quand le chapeau Nice d'une classe de services est très large (classe 41 *"Education ; formation ; divertissement ; activités culturelles"*, classe 35 *"Publicité ; gestion des affaires"*, classe 45 *"Services juridiques ; services de sécurité"*, classe 42 *"Services scientifiques et technologiques"*) et que l'activité réelle ne couvre qu'un sous-domaine sectoriel précis, **terminer le libellé par une formule de limitation** : *"tous les services précités étant limités au domaine [secteur]"* ou *"étant entendu que les services précités sont fournis exclusivement dans le domaine [secteur]"*.

Cette technique, admise par l'IPI, a deux fonctions :

1. **Réduction du périmètre exposé à opposition.** Sans limitation, *"éducation et formation"* ouvre tout le champ de la formation, ce qui expose à des oppositions de marques de formation dans des domaines totalement étrangers. La limitation ferme ces angles d'attaque.
2. **Défense contre l'attaque pour non-usage.** En 5 ans (art. 12 LPM), l'IPI peut considérer qu'un libellé sans qualificatif est trop large par rapport à l'usage réel. La limitation aligne le périmètre déposé sur le périmètre réellement exploité.
À utiliser systématiquement quand le chapeau Nice est sectoriellement débordant par rapport à l'activité réelle. Exemple en classe 41 pour Mosaic Cuisine : *"tous les services précités étant limités au domaine culinaire et gastronomique ainsi qu'à l'insertion professionnelle dans le secteur de la restauration"*. Exemple en classe 45 pour un cabinet d'avocats spécialisé : *"étant entendu que les services précités sont fournis exclusivement dans le domaine du droit suisse des affaires"*.

#### Granularité spécifique du traiteur et de la restauration en classe 43

Pour la classe 43 d'un traiteur ou acteur de la restauration, décliner systématiquement par deux familles d'angles complémentaires :

**1. Segmentation par type de client institutionnel.** Au-delà des libellés génériques (*"services de traiteurs"*, *"services de restauration"*), décliner par segment de clientèle pour verrouiller les marchés cibles : *"services de traiteurs pour entreprises ; services de traiteurs pour des hôtels ; services de traiteurs pour écoles ; services de traiteurs pour maisons de retraite ; services de traiteurs pour maisons médicalisées ; services de traiteurs pour des institutions ; services de traiteurs événementiels ; services de traiteurs pour cocktails et réceptions ; mise à disposition d'aliments et de boissons pour des hôtes lors de banquets et événements privés ou professionnels"*.

**2. Angles d'extension métier.** Anticiper les évolutions naturelles du modèle : *"services de chefs cuisiniers à domicile ; mise à disposition d'installations pour cuisiner ; mise à disposition de cuisines professionnelles ; location d'équipements de restauration ; services de cuisine mobile ; services de buvette saisonnière"*. Particulièrement pertinents pour les programmes d'incubation culinaire, les traiteurs haut de gamme évoluant vers le B2C premium, et les acteurs saisonniers.

#### Classe 35 — penser la vente au détail des prestations de service, pas seulement des produits

L'angle classique de la classe 35 est la vente au détail de produits (boutique, e-commerce). Mais l'IPI admet également les libellés de type *"services de vente au détail [en ligne] de [prestations]"* lorsque la plateforme commercialise effectivement des prestations de service à l'unité ou par abonnement. Pour une plateforme vinicole qui vend, en plus de bouteilles, des **cours, ateliers, événements de dégustation, abonnements à des sélections**, la formulation *"services de vente au détail en ligne de cours et événements de dégustation de vin"* en classe 35 capte un revenu commercial qui aurait sinon basculé en classe 41 — et y reste également dans son volet "organisation". On obtient ainsi une **double couverture** : la classe 35 protège la *commercialisation* de la prestation, la classe 41 protège la *prestation* elle-même.

Cette approche est généralisable : *services de vente au détail en ligne de* [consultations, formations, événements, abonnements, licences] est une famille de libellés à explorer systématiquement pour toute plateforme qui ne se réduit pas à du physique.

**Anticipation des développements futurs** : une marque se dépose pour 10 ans (renouvelable). Penser aux extensions de gamme prévisibles, aux canaux de distribution à protéger, aux licensing envisageables. Mais ne pas surcouvrir : en Suisse, après 5 ans de non-usage dans une classe, la marque y devient attaquable.

**Pour les règles de formulation détaillées** (ponctuation, énumérations, limitations admises et exclues, services de vente au détail, fabrication sur commande, produits virtuels et NFT, services en environnement virtuel, hiérarchie des sources WDL/Nice/TMclass), consulter `references/classification-nice.md`. À mobiliser systématiquement en registre praticien et lorsqu'un libellé soulève une question de précision rédactionnelle ou de classification atypique.

### Étape G — Synthèse à l'utilisateur

À la fin, livrer une synthèse claire et actionnable qui contient :
- Le signe à déposer (avec recommandation si verbale/combinée a été un arbitrage)
- **Pour un dépôt figuratif ou combiné : la description verbale du signe** (paragraphe précis et neutre, exploitable directement dans le formulaire IPI)
- Les classes de Nice retenues, avec une phrase d'explication par classe
- **Les libellés rédigés en intégralité, classe par classe**, séparés par des points-virgules selon la convention IPI, **avec limitation finale si applicable**
- Les risques d'opposition identifiés (s'il y en a) ou la stratégie de recherche manuelle si on est en mode dégradé
- Le coût estimé
- Les prochaines étapes concrètes : URL e-trademark, ce qui sera demandé au formulaire
---

## Exemple de référence n°1 : cabinet d'avocats lausannois (cas réel)

**Activité** : cabinet d'avocats orienté PME, pôles affichés = droit des affaires, propriété intellectuelle, droit du travail, médiation, immobilier et construction.

**Type de signe** : marque verbale.

**Classes retenues** : 35, 41, 45.

**Libellés effectivement déposés** (à reproduire comme référence du niveau de granularité attendu) :

> **Classe 35** — Conseils en affaires pour entreprises ; conseils de gestion et organisation des affaires ; conseils en organisation d'entreprises ; conseils dans le domaine d'acquisitions d'entreprises ; gestion de projets commerciaux ; entremise et conclusion d'affaires commerciales pour des tiers ; négociation de contrats d'affaires pour des tiers ; négociation de transactions commerciales pour le compte de tiers ; conseils pour la réalisation de transactions commerciales ; planification stratégique des affaires ; conseils en matière de stratégies commerciales ; informations en matière de contacts d'affaires et commerciaux ; réseautage d'affaires.
>
> **Classe 41** — Préparation, animation et organisation de séminaires et d'ateliers de formation ; services de formation en affaires ; services de formation dans le domaine juridique.
>
> **Classe 45** — Prestation de conseils juridiques et représentation juridique ; services d'avocats ; services de médiation ; médiation dans le cadre de procédures juridiques ; mise à disposition d'informations sur des questions juridiques ; recherches juridiques ; représentation et assistance en matière de différends juridiques portés devant des instances d'arbitrage, de médiation et de règlement alternatif des différends ; services d'audit à des fins de conformité juridique ; services juridiques en rapport avec la négociation de contrats pour des tiers ; conseils en propriété intellectuelle ; conseils en droit du travail ; conseils en droit des affaires ; conseils en droit commercial ; conseils en droit des sociétés ; conseils en droit des assurances sociales ; conseils en protection des données ; conseils en droit de la concurrence ; conseils en droit contractuel.

**Trois enseignements à transposer :**

1. **Granularité élevée** : 13 libellés en classe 35, 18 en classe 45. Pas de libellé générique unique — chaque sous-spécialité métier est déclinée. C'est ce niveau qui protège réellement.
2. **Angle "transactions et négociation" en classe 35**, plutôt que "conseil en gestion organisationnelle". Pour un cabinet d'avocats orienté affaires, c'est l'entremise, la négociation de contrats, le conseil en M&A qui caractérise l'activité — pas le conseil RH ou la direction d'entreprise au sens strict.
3. **Classe 41 resserrée** : on ne charge pas avec "coaching", "médiation [formation]" ou autres termes connexes. On ne garde que ce qui est concrètement délivré (séminaires, formation en affaires, formation juridique). Mieux vaut une classe étroite et défendable qu'une classe large et attaquable pour non-usage à 5 ans.
**Reproduire ce niveau de qualité pour chaque dépôt.** Si la liste finale tient en 3 lignes par classe, c'est qu'on n'a pas assez creusé l'activité.

---

## Exemple de référence n°2 : plateforme e-commerce vinicole (cas réel — Alfavin)

**Activité** : plateforme e-commerce de vente de vins, avec volet éditorial et événementiel (dégustations, ateliers, cours de sommellerie, contenu en ligne).

**Type de signe** : marque verbale.

**Classes retenues** : 33, 35, 41.

**Libellés effectivement déposés** :

> **Classe 33** — Boissons alcoolisées à l'exception des bières ; préparations alcoolisées pour faire des boissons ; vins ; vins mousseux ; vins effervescents ; boissons à base de vin ; eaux-de-vie de vin ; vin rouge ; vins italiens et espagnols ; digestifs (liqueurs et spiritueux).
>
> **Classe 35** — Publicité ; gestion, organisation et administration des affaires commerciales ; vente au détail et vente en gros de boissons alcoolisées, de vins, de spiritueux et d'accessoires pour la dégustation du vin ; services de vente au détail en ligne de boissons alcoolisées, de vins, de spiritueux, de cours et événements de dégustation de vin, de spiritueux et d'accessoires de vin ; services d'abonnement pour la vente au détail de vins.
>
> **Classe 41** — Education ; formation ; divertissement ; activités culturelles ; services d'éducation et de formation dans le domaine de la dégustation et de la culture du vin ; organisation et animation d'ateliers de dégustation de vin ; organisation de cours de sommellerie ; événements de dégustation de vins à des fins éducatives ; organisation de concours de dégustation de vin ; mise à disposition d'informations en ligne sur le vin à des fins éducatives et de divertissement ; mise à disposition de publications électroniques en ligne non téléchargeables sur le vin.

**Quatre enseignements à transposer :**

1. **Chapeau Nice systématique** en tête de classe : *"Boissons alcoolisées à l'exception des bières"* (classe 33), *"Publicité ; gestion, organisation et administration des affaires commerciales"* (classe 35), *"Education ; formation ; divertissement ; activités culturelles"* (classe 41). Couverture défensive maximale, suivie de la déclinaison fine.
2. **Classe 35 incluant la vente au détail des prestations de service**, pas seulement des bouteilles : *"services de vente au détail en ligne de [...] de cours et événements de dégustation de vin"*. Capte le revenu commercial des prestations sans le faire basculer hors classe 35.
3. **Classe 41 jamais omise pour un e-commerçant vinicole**, même quand le fondateur se voit "principalement" comme un retailer. Les ateliers, dégustations et contenu éditorial sont quasi-systématiques dans le secteur.
4. **Classe 39 délibérément absente** alors qu'elle pouvait sembler tentante (livraison, entreposage). La livraison des produits vendus par la plateforme est absorbée par la classe 35 ; la classe 39 aurait été inutile et attaquable pour non-usage.
---

## Exemple de référence n°3 : acteur intégré du vétérinaire de référence (cas réel — Vet For Vets)

**Activité** : acteur vétérinaire de référence combinant trois pôles — soins de spécialité (chirurgie, imagerie, médecine interne, urgences), commercialisation d'instruments et équipements chirurgicaux/médicaux vétérinaires, et formation pratique des confrères vétérinaires.

**Type de signe** : marque figurative pure (logo sans texte).

**Classes retenues** : 10, 35, 41, 44.

**Libellés effectivement déposés** :

> **Classe 10** — Appareils et instruments chirurgicaux, médicaux, dentaires et vétérinaires ; instruments chirurgicaux à usage vétérinaire ; implants chirurgicaux à usage vétérinaire ; plaques d'ostéosynthèse à usage vétérinaire ; vis chirurgicales à usage vétérinaire ; broches chirurgicales à usage vétérinaire ; appareils et équipements médicaux à usage vétérinaire ; appareils d'imagerie médicale à usage vétérinaire, notamment appareils à ultrasons, appareils de radiographie et appareils de tomodensitométrie ; appareils d'anesthésie à usage vétérinaire ; moniteurs de surveillance médicale à usage vétérinaire ; appareils d'électrochirurgie à usage vétérinaire ; matériel de suture à usage vétérinaire ; aiguilles chirurgicales à usage vétérinaire ; tables d'opération à usage vétérinaire ; lampes opératoires à usage vétérinaire.
>
> **Classe 35** — Publicité ; gestion, organisation et administration des affaires commerciales ; travaux de bureau ; vente au détail ou en gros de produits de tous types, en particulier d'appareils et instruments chirurgicaux, médicaux et vétérinaires ; vente au détail et en gros d'instruments chirurgicaux à usage vétérinaire ; vente au détail et en gros d'implants chirurgicaux à usage vétérinaire ; vente au détail et en gros d'appareils et équipements médicaux à usage vétérinaire ; vente au détail et en gros d'appareils d'imagerie médicale à usage vétérinaire ; vente au détail et en gros d'appareils d'anesthésie à usage vétérinaire ; vente au détail et en gros de matériel de suture à usage vétérinaire ; vente au détail et en gros de mobilier à usage vétérinaire ; vente au détail et en gros de produits pharmaceutiques à usage vétérinaire ; services de vente en ligne de matériels, instruments et équipements à usage vétérinaire.
>
> **Classe 41** — Éducation ; formation ; formation professionnelle ; formation et formation complémentaire pour le perfectionnement du personnel ; services d'enseignement et de formation professionnels ; formation pratique en techniques chirurgicales vétérinaires ; services d'enseignement et de formation dans le domaine vétérinaire ; services d'instruction et mise à disposition de formation pratique dans le domaine de la médecine vétérinaire ; publication de supports pédagogiques à usage vétérinaire.
>
> **Classe 44** — Services médicaux ; services vétérinaires ; services de chirurgie vétérinaire ; assistance vétérinaire ; services de médecine vétérinaire pour animaux de compagnie ; services vétérinaires d'urgence ; services de soins intensifs pour animaux de compagnie ; services d'imagerie médicale vétérinaire ; services de médecine interne vétérinaire ; services de consultations vétérinaires spécialisées et de second avis vétérinaire ; services de cliniques vétérinaires.

**Cinq enseignements à transposer :**

1. **Couplage classe-produit ⇄ classe 35 en miroir.** Chaque catégorie d'instrument déclinée en classe 10 est reprise en classe 35 sous forme *"vente au détail et en gros de [catégorie]"* — instruments chirurgicaux, implants, équipements médicaux, imagerie, anesthésie, matériel de suture, mobilier, pharmaceutique. Décalque rigoureux : à chaque produit protégé correspond une vente protégée.
2. **Pour un acteur intégré du médical/vétérinaire, ne pas se laisser enfermer dans une seule dimension.** Soins (44), produits (10), vente (35), formation (41) forment un quadrilatère cohérent. Omettre un sommet expose une face entière du business à l'attaque concurrentielle.
3. **Classe 41 systématique pour les distributeurs d'équipements professionnels.** La formation à l'usage des équipements est consubstantielle à la commercialisation — c'est un cas typique où la classe 41 doit être proposée par défaut, pas conditionnée à un choix de l'utilisateur.
4. **Granularité technique précise en classe 10.** Pas seulement "instruments chirurgicaux" mais la déclinaison par sous-famille (ostéosynthèse, vis, broches, imagerie, anesthésie, électrochirurgie, suture, mobilier opératoire). Cette précision verrouille les sous-spécialités face à un concurrent qui ne se positionnerait que sur l'une d'elles.
5. **Description verbale du signe figuratif** soignée : *"Cercle plein traversé en croix par deux courbes en X qui s'épaississent vers les extrémités et débordent du cercle aux quatre coins, avec un anneau central au point d'intersection"*. Précise, neutre, suffisante pour reconnaître le signe sans l'image.
---

## Exemple de référence n°4 : programme d'insertion par la cuisine du monde (cas réel — Mosaic Cuisine)

**Activité** : programme à mission sociale porté par une fondation (IFPD), combinant trois pôles — service traiteur événementiel haut de gamme (B2B et B2C, de 15 à 600 personnes), exploitation de cafés et buvettes (Pyxis Café à Lausanne, Buvette du Parc des Eaux-Vives à Genève saisonnière), et programme de formation/insertion professionnelle (Mosaic Academy) pour personnes issues de la migration souhaitant lancer une micro-entreprise culinaire ou s'insérer dans la restauration.

**Type de signe** : marque combinée — élément verbal *MOSAIC CUISINE* sur deux lignes accompagné d'éléments graphiques de tuiles de mosaïque (le O en tuile, trois tessons stylisés). Le passage en marque combinée est ici un sauvetage stratégique d'un verbal faible : *cuisine* est descriptif et *mosaic* frôle la frontière du descriptif pour un traiteur "mosaïque de saveurs" — seul le graphisme distinctif rend l'ensemble enregistrable.

**Classes retenues** : 35, 41, 43.

**Libellés effectivement déposés** :

> **Classe 35** — Gestion, organisation et administration des affaires commerciales ; travaux de bureaux ; aide à la direction d'entreprises commerciales ou industrielles ; aide à la gestion commerciale ; aide à la gestion d'affaires ; aide à l'exploitation d'entreprises industrielles ou commerciales ; assistance à la gestion d'entreprise ; assistance commerciale ; assistance et prestation de conseils en matière d'organisation et de gestion commerciales ; services administratifs ; services comptables ; services de secrétariat.
>
> **Classe 41** — Education ; formation ; activités culturelles ; accompagnement personnalisé (coaching) ; animation d'ateliers de formation ; animation de cours d'instruction, d'éducation et de formation pour jeunes et adultes ; cours de cuisine ; édition de livres et de revues ; éducation et formation en matière de nutrition, de santé et d'alimentation ; formation professionnelle ; mise à disposition d'informations en matière de formation et d'éducation ; organisation et conduite de conférences ; préparation et animation de conférences, de conventions et d'expositions à des fins culturelles ou éducatives ; **tous les services précités étant limités au domaine culinaire et gastronomique ainsi qu'à l'insertion professionnelle dans le secteur de la restauration**.
>
> **Classe 43** — Services de restauration, d'hôtels, de cafés-restaurants, de cafés, de cafétérias, de bars, de restaurants, de restaurants libre-service, de snack-bars, de cantines ; services de restauration (alimentation) ; services de préparation d'aliments et de boissons et services de restauration à emporter ; services de bars et traiteurs ; services de traiteurs (aliments et boissons) ; service de traiteurs de cuisine du monde ; services de restauration de cuisine du monde ; service de traiteurs pour des institutions ; services de traiteurs pour entreprises ; services de traiteurs pour des hôtels ; services de traiteurs pour écoles ; services de traiteurs pour maisons de retraite ; services de traiteurs pour maisons médicalisées ; services de restaurants ; services de restauration à emporter ; services de chefs cuisiniers à domicile ; location d'équipements de restauration ; mise à disposition d'informations interactives en ligne sur la préparation des aliments et des boissons, sur la préparation des repas et la restauration via des services mobiles et numériques ; mise à disposition de services de restaurants ; mise à disposition d'installations pour cuisiner ; mise à disposition de cuisines professionnelles ; informations et conseils en matière de préparation de repas.

**Cinq enseignements à transposer :**

1. **Classe 43 absorbante — pas de classes 29/30 pour un traiteur sans gamme conditionnée.** Mosaic Cuisine fait de la vente à emporter dans ses cafés et de la livraison de plats par le traiteur. Ces deux activités sont **entièrement absorbées par la classe 43** (*"services de préparation d'aliments et de boissons et services de restauration à emporter"*, *"services de chefs cuisiniers à domicile"*). Les classes 29/30 n'auraient été pertinentes que pour la commercialisation d'une gamme conditionnée vendue séparément du service — ce qui n'est pas le modèle. Économie de 200 CHF et 2 classes en moins exposées à l'attaque pour non-usage.
2. **Second usage de la classe 35 — accompagnement entrepreneurial.** Le libellé classe 35 ne couvre pas la vente au détail de produits (puisqu'il n'y a pas de produits) mais les **services de gestion et d'administration commerciale** fournis aux micro-entrepreneurs accompagnés par Mosaic Academy : *"aide à la direction d'entreprises commerciales ou industrielles ; aide à la gestion commerciale ; assistance à la gestion d'entreprise ; services administratifs ; services comptables ; services de secrétariat"*. Angle structurel pour un programme d'incubation entrepreneuriale.
3. **Technique de la limitation finale en classe 41.** Le libellé se termine par *"tous les services précités étant limités au domaine culinaire et gastronomique ainsi qu'à l'insertion professionnelle dans le secteur de la restauration"*. Cette limitation ferme les angles d'attaque venant de marques de formation dans des domaines étrangers (IT, langues, musique) tout en alignant le périmètre déposé sur l'activité réelle. À reproduire systématiquement quand le chapeau Nice est sectoriellement débordant.
4. **Granularité du traiteur — segmentation par client institutionnel.** La classe 43 décline 22 libellés, dont une famille dédiée à la **segmentation par type de client** : *"services de traiteurs pour entreprises ; pour des hôtels ; pour écoles ; pour maisons de retraite ; pour maisons médicalisées ; pour des institutions"*. Stratégie de verrouillage des marchés cibles, particulièrement pertinente pour les volumes 15-600 personnes qui correspondent aux marchés institutionnels (EMS, écoles, événements d'entreprise).
5. **Granularité du traiteur — angles d'extension métier.** La classe 43 inclut aussi *"services de chefs cuisiniers à domicile ; mise à disposition d'installations pour cuisiner ; mise à disposition de cuisines professionnelles ; location d'équipements de restauration"*. Ces libellés anticipent les évolutions naturelles d'un programme d'incubation culinaire (mise à disposition de cuisines aux micro-entrepreneurs en formation) et du B2C premium (chefs à domicile).
---

## Les trois moments d'interaction avec l'utilisateur

Hors cas de doute réel, on n'interrompt l'utilisateur qu'à ces trois moments :

### Interaction 1 — Activité du déposant
Au démarrage, si on n'a pas l'information. Une URL suffit le plus souvent. **Si l'URL est inaccessible, demander une description en deux ou trois phrases — ne pas présumer.**

### Interaction 2 — Validation des arbitrages business

Quand des choix coûtent de l'argent ou changent la stratégie de protection :
- Faut-il ajouter une 4ème ou 5ème classe (+ CHF 100.- chacune) ?
- Faut-il doubler par un dépôt combiné (logo + texte) en plus du verbal ?
- Conflit en risque moyen détecté : continue-t-on, modifie-t-on, ou abandonne-t-on ?
**Formulation correcte des arbitrages — toujours en activités, jamais en numéros de classe.** Ne jamais lister les options sous forme de combinaisons de numéros ("44+35+41 vs 44+35"). Toujours décliner sous forme de pôles d'activité que l'utilisateur reconnaît dans son métier ("protéger les soins, la vente, la formation des confrères ?"). En interne, on traduit ensuite en classes — l'utilisateur n'a jamais à voir le numéro. Le coût additionnel d'une classe peut être mentionné (CHF 100.-) sans nommer la classe ; le bénéfice se formule en activité protégée.

**Quand l'activité réelle de l'utilisateur n'est pas encore parfaitement comprise, formuler en multi-select large** plutôt qu'en single-select restreint. Une question single-select sur les pôles d'activité présume qu'on connaît la liste exhaustive — ce qui n'est presque jamais le cas. Le multi-select avec 4-6 options et une option *"autre, je précise"* laisse l'utilisateur cocher ce qui correspond réellement, sans forcer un cadrage prématuré.

**Désagréger les options qui mélangent des réalités juridiquement distinctes.** Un piège fréquent : une option multi-select qui agrège *"vente à emporter ou commercialisation conditionnée"* mélange deux réalités qui appellent des classes différentes (43 vs 29/30+35). L'utilisateur cochera parce que la première moitié correspond à son activité, mais cela ne dit rien sur la seconde — et le mapping interne en classes deviendra erroné. Toujours **séparer chaque réalité juridique en option distincte**, même si cela porte le nombre d'options à 5 ou 6.

### Interaction 3 — Modification du signe (uniquement si nécessaire)

**Important : ne pas conseiller sur le signe par défaut.** On part du principe que le signe choisi par l'utilisateur est celui qu'il veut. On ne propose des modifications que si :
- L'étape C conclut que le signe n'est pas distinctif (rouge ou orange).
- L'étape D détecte un conflit en risque élevé.
Dans ces cas, proposer des alternatives concrètes : modification du mot (préfixe/suffixe distinctif, néologisme), passage à une marque combinée, ajout d'éléments arbitraires.

---

## Posture face à un travail antérieur en mémoire

Quand la mémoire contient un dossier antérieur sur le même client (autre dépôt, autre signe, autre conseil donné), **ne jamais présumer la reprise.** Trois options sont toujours sur la table et doivent être proposées explicitement à l'utilisateur dès le début :

1. **Reprendre le travail antérieur** — gain de temps, cohérence du portefeuille de marques du client, libellés et stratégie déjà calibrés.
2. **Refaire à neuf** — utile pour un test de la skill, un second avis, ou un scope volontairement distinct du travail antérieur.
3. **Compléter** — par exemple, dépôt figuratif après un dépôt verbal déjà effectué, classe additionnelle, extension de portefeuille.
Formuler la question simplement : *"J'ai en mémoire un travail précédent sur [client] — tu veux qu'on reprenne ce qui avait été fait, qu'on parte à neuf, ou qu'on complète ?"* La réponse change tout : reprise → on rebondit sur les classes et libellés existants ; à neuf → on traite comme un cas vierge sans contamination ; compléter → on cible précisément ce qui manque.

**Ne jamais glisser silencieusement dans la reprise** parce que c'est plus rapide. C'est une erreur de respect du contrôle utilisateur.

---

## Coûts (à jour, source IPI)

Source officielle : `https://www.ige.ch/fr/proteger-votre-pi/marques/demande-nationale/couts-et-taxes`

| Poste | Montant |
|---|---|
| Dépôt 3 classes (papier) | CHF 450.- |
| Dépôt 3 classes (e-trademark, en ligne) | **CHF 350.-** (rabais de CHF 100.-) |
| Classe additionnelle (au-delà de 3) | CHF 100.- par classe |
| Renouvellement (10 ans supplémentaires) | CHF 550.- |

**Toujours recommander e-trademark** (`https://e-trademark.ige.ch/`) pour le rabais et la simplicité. **Vérifier le tarif à la source au moment du dépôt** — l'IPI peut ajuster.

---

## Ressources MCP — bases connectées au workflow

Quatre corpus de référence sont accessibles directement via MCP. Ils forment l'infrastructure documentaire du skill et doivent être mobilisés systématiquement aux étapes correspondantes du workflow, sans attendre que l'utilisateur le demande.

**Intitulés généraux Nice (les 45 chapeaux officiels, version 12-2026).** Le texte officiel des chapeaux de chaque classe. Première brique de l'entonnoir à l'étape F : poser le chapeau Nice complet en tête de chaque classe retenue avant toute déclinaison fine. Le chapeau étant l'intitulé reconnu par l'IPI, il offre la couverture défensive maximale d'entrée de jeu.

**WDL — Aide à la classification IPI (≈ 41 500 termes pré-validés).** L'intégralité des termes acceptés par l'IPI à l'examen. À l'étape F, c'est la base de sélection exclusive : tout libellé descendu sous le chapeau Nice doit être un terme effectivement présent dans la WDL ou directement dérivé d'un terme WDL par adjonction d'un qualificatif sectoriel. Cela ferme définitivement le risque du libellé inventé refusé à l'examen formel.

**Décisions du TAF en matière de marques.** Corpus de jurisprudence du Tribunal administratif fédéral statuant sur les décisions de refus de l'IPI (motifs absolus principalement, motifs relatifs accessoirement). À mobiliser à l'étape C : avant de qualifier un signe en 🟢/🟠/🔴, vérifier si une décision TAF a déjà tranché sur un signe identique, très similaire, ou présentant la même structure descriptive ou évocatrice. Permet de signaler à l'utilisateur "ce type de signe a déjà été refusé / accepté dans des conditions comparables", ce qui calibre l'analyse de distinctivité par la pratique réelle plutôt que par la doctrine seule.

**Listes-types et corpus Swissreg (≈ 75 000 libellés issus de 25 800 marques déposées par les principaux mandataires suisses).** Corpus de dépôts professionnels — Bugnion et autres grands cabinets. Trois usages, mobilisables aux étapes A à F :

- **Étape E — identification des classes.** Repérer dans le corpus quelles classes sont *fréquemment combinées* dans le secteur du déposant. Si dix dépôts professionnels d'un secteur donné couplent systématiquement classes X, Y et Z, c'est un signal fort que la combinaison fait sens — et inversement, qu'une classe oubliée par tout le secteur n'a sans doute pas à être proposée.
- **Étape F — calibrage de la granularité.** Le corpus donne la mesure réelle de ce qu'est un "bon dépôt" : nombre de libellés par classe, profondeur de déclinaison par sous-spécialité, formulations standard. Permet d'éviter à la fois la sous-protection (trois libellés génériques) et la sur-protection inutile.
- **Étape F — inspiration rédactionnelle.** Les formulations exactes utilisées par les grands mandataires sur des dépôts comparables sont une référence d'usage : on s'aligne sur la pratique professionnelle suisse plutôt que de réinventer chaque libellé.
**Discipline d'usage.** Ces ressources ne sont pas des appendices documentaires consultables sur demande — elles sont les sources canoniques du skill aux étapes qu'elles concernent. À l'étape F en particulier, ne livrer aucune liste de libellés sans avoir fait passer chaque classe par les chapeaux Nice et la WDL ; à l'étape C, ne qualifier aucun signe douteux sans avoir cherché un précédent TAF sur un signe comparable. La présence de ces bases via MCP fait basculer le skill du mode "doctrine théorique" au mode "pratique professionnelle outillée".

---

## Outils et ressources

| Ressource | URL | Usage | Accessible en `web_fetch` ? |
|---|---|---|---|
| **e-trademark** (dépôt en ligne IPI) | `https://e-trademark.ige.ch/` | Le formulaire officiel de dépôt | Non (SPA, à recommander à l'utilisateur) |
| **WDL** — Aide à la classification IPI | `https://wdl.ige.ch?lang=fr` | Termes pré-validés pour les libellés | Non (SPA) |
| **Aide à l'examen IPI** | `https://ph.ige.ch/ph/` | Vérifier si un terme passe l'examen | Non (SPA) |
| **Swissreg** (registre suisse) | `https://www.swissreg.ch/database-client/search/query/trademarks?lang=fr` | Recherche d'antériorité (Suisse) | **Non (SPA)** — fournir l'URL et la stratégie à l'utilisateur |
| **Global Brand Database (WIPO)** | `https://branddb.wipo.int/` | Recherche d'antériorité internationale, **recherche par image** pour figuratifs et combinés | **Non (SPA)** — fournir l'URL et la stratégie |
| **TMview** | `https://www.tmdn.org/tmview/` | Recherche d'antériorité multi-offices, recherche par image disponible | Non (SPA) |
| **Classification de Nice (WIPO)** | `https://nclpub.wipo.int/?menulang=fr&lang=fr` | Référence officielle des classes | Partiellement |
| **TMclass** | `https://www.tmdn.org/tmclass/` | Référence multi-offices pour libellés | Partiellement |
| **Classification de Vienne (WIPO)** | `https://www.wipo.int/classifications/vienna/en/` | Codification des éléments figuratifs (codes de Vienne) | Oui |
| **Zefix** (Registre du commerce) | `https://www.zefix.ch/` | Vérification des raisons sociales (art. 956 CO) | Oui |
| **Madrid Monitor** | `https://www3.wipo.int/madrid/monitor/en/` | Suivi des enregistrements internationaux désignant la Suisse | Partiellement |
| **Coûts et taxes IPI** | `https://www.ige.ch/fr/proteger-votre-pi/marques/demande-nationale/couts-et-taxes` | Référence tarifaire officielle | Oui |
| **Directives en matière de marques (IPI 2026)** | Téléchargeable sur ige.ch | Référence d'examen complète (synthétisée dans `references/`) | Oui (PDF) |

**Constat opérationnel** : les outils interactifs IPI/WIPO restent des SPA non-fetchables — pour la recherche d'antériorité (Swissreg, BrandDB, TMview) et pour le formulaire de dépôt e-trademark, on reste donc en mode dégradé (URL + stratégie fournis à l'utilisateur). En revanche, le contenu documentaire de la WDL, les chapeaux Nice et les corpus de dépôts professionnels sont désormais accessibles directement via MCP (cf. section précédente) — la doctrine du "tout-dégradé" qui prévalait jusqu'ici ne s'applique plus à la rédaction des libellés ni à la sélection des classes.

**Doctrine de référence** : les Directives IPI 2026 sont synthétisées par thème dans les quatre fichiers `references/` (motifs absolus, classification de Nice, procédure de dépôt, recherche d'antériorité). Pour toute question juridique pointue ou en registre praticien, consulter ces fichiers avant de répondre.

---

## Règles d'or

1. **Ne jamais inventer un libellé.** Tout libellé doit être puisé dans la WDL accessible via MCP, dans les chapeaux Nice officiels accessibles via MCP, ou directement dérivé d'un terme WDL par adjonction d'un qualificatif sectoriel admis (limitation finale, segment de clientèle, sous-spécialité métier). Un libellé inventé sera refusé à l'examen formel.
2. **Ne jamais sauter la recherche d'antériorité.** L'IPI ne vérifie pas les motifs relatifs. Le risque d'opposition post-publication est entièrement à la charge du déposant. Si on ne peut pas la faire en autonomie, on prépare la stratégie pour l'utilisateur.
3. **Viser la granularité professionnelle des libellés.** 8 à 15 libellés par classe principale (jusqu'à 18-22 pour les classes-piliers d'un acteur multi-pôles), déclinés par sous-spécialité métier. Pas de "services juridiques" tout court — décliner par domaine du droit, par type d'acte, par cible.
4. **Toujours commencer par le chapeau Nice de la classe**, puis décliner. Le chapeau seul est insuffisant ; la déclinaison seule prive d'un angle d'attaque large.
5. **Ne pas conseiller sur le signe sauf si on doit le faire.** Le signe choisi par l'utilisateur est respecté. On ne propose des modifications que si la distinctivité ou un conflit le justifient. **Exception : signaler immédiatement quand un verbal faible ne sera sauvable qu'en passant en marque combinée** — c'est un conseil structurel, pas un changement de signe.
6. **Faire le travail en arrière-plan.** L'utilisateur n'a pas à comprendre la classification de Nice pour déposer. Il a à valider trois ou quatre choix-clés.
7. **Vérifier les tarifs et les URL à la source.** Les tarifs IPI changent. La page `https://www.ige.ch/fr/proteger-votre-pi/marques/demande-nationale/couts-et-taxes` fait foi. Les URL des outils IPI sont en `.ige.ch`, pas `.ipi.ch`.
8. **Une seule question à la fois quand on doit interagir.** Pas de batch de questions techniques.
9. **Quand on doit interagir, parler en termes d'activités, jamais en numéros de classe.** L'utilisateur ne connaît pas la Classification de Nice et n'a pas à la connaître. Toute question sur le périmètre de protection doit être formulée en activités concrètes du métier ("vendre des bouteilles en ligne", "organiser des dégustations", "soigner des animaux", "former des confrères", "fabriquer ou vendre des instruments", "exploiter un café"), jamais en codes ("classe 33", "classe 41"). Le travail de mapping activité → classe Nice reste exclusivement de notre côté, en arrière-plan.
10. **Lire l'activité avant tout. Si l'accès au site échoue, signaler l'obstacle et demander une description — ne jamais présumer.** Une présomption silencieuse en étape A se propage en cascade : mauvaises options proposées en interaction 2, classes oubliées, libellés à côté du métier réel. Pas d'activité comprise → pas de question stratégique posée.
11. **Couplage produit ⇄ vente.** Chaque fois qu'on retient une classe-produit (10, 5, 25, 33, 29/30, etc.) pour un acteur qui distribue ou fabrique, **proposer systématiquement la classe 35 en miroir**, avec déclinaison décalquée. La classe-produit sans la 35, c'est protéger l'objet sans protéger l'activité de vente — incohérent pour un distributeur.
12. **Ne jamais présumer la reprise d'un travail antérieur.** Quand la mémoire contient un dossier précédent sur le même client, demander explicitement à l'utilisateur ce qu'il veut en faire (reprendre, refaire à neuf, compléter).
13. **Classe 43 absorbante pour la restauration et le traiteur.** Pour un acteur de la restauration, la classe 43 absorbe la vente à emporter, la livraison de plats préparés et le service de table. Les classes 29/30 ne se justifient que pour la commercialisation d'une gamme alimentaire conditionnée et vendue séparément du service. Ne jamais confondre les deux.
14. **Désagréger les options multi-select qui mélangent des réalités juridiquement distinctes.** Un cochage utilisateur ambigu donne un mapping en classes erroné. Toujours séparer en options distinctes les réalités qui appellent des classes différentes (vente à emporter vs commercialisation conditionnée, formation vs accompagnement entrepreneurial, services aux clients vs services aux confrères).
15. **Limitation finale systématique pour les classes à chapeau débordant.** Quand le chapeau Nice ouvre un champ plus large que l'activité réelle (classes 35, 41, 42, 45 en particulier), terminer le libellé par *"tous les services précités étant limités au domaine [secteur]"*. Réduit l'exposition à opposition et défend contre l'attaque pour non-usage.
---

## Retours et amélioration continue

Cette skill est conçue pour s'enrichir au fil des dépôts réels. La théorie de la classification de Nice et la pratique de l'IPI laissent une marge d'interprétation que seuls les cas concrets permettent de calibrer. **Après chaque dépôt effectivement réalisé**, l'utilisateur (Timothée) est invité à transmettre la liste finale des classes et libellés effectivement déposés. Le comparatif avec ce que la skill avait proposé est exécuté en trois temps :

1. **Identifier les écarts** — libellés ajoutés, retirés, reformulés ; classes ajoutées ou écartées ; chapeaux Nice présents ou absents ; granularité supérieure ou inférieure à la proposition ; limitations finales présentes ou absentes.
2. **Diagnostiquer la cause de chaque écart** — biais de prudence (sur-couverture inutile), question mal calibrée à l'utilisateur (interaction 2 trop fermée, en numéros de classe, ou agrégeant des réalités juridiquement distinctes), ignorance d'une pratique sectorielle, mauvaise lecture de l'activité, présomption silencieuse, mapping mécanique activité → classe sans vérifier l'absorption par une classe-pivot, etc.
3. **Formuler un patch concret** — texte prêt à intégrer dans la section concernée du `SKILL.md`, avec localisation précise.
Cette boucle de retour est la meilleure source d'amélioration de la skill, plus précise que la consultation théorique des Directives IPI ou de la jurisprudence : elle capte les arbitrages réels qu'un avocat suisse expérimenté opère sur des dossiers vivants. Les patches issus de cas réels (cabinet d'avocats lausannois, plateforme e-commerce vinicole Alfavin, acteur vétérinaire intégré Vet For Vets, programme d'insertion par la cuisine Mosaic Cuisine) en sont la trace concrète.

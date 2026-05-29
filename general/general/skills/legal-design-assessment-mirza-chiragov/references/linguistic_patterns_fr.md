# Modèles linguistiques français — Référence

Loaded when the audit reaches Step 3 and the document language is French.

This file inventories the patterns that French-language legal-design practice (après Catherine et l'école de la communication juridique, Sourioux & Lerat, Cornu, et plus récemment Bouchard, Trudeau et l'École de Sherbrooke) treats as legal-design debt. Detect, count, score — do not rewrite.

The patterns below apply to standard juridical French. Belgian, Swiss-Romande, Luxembourgish, and Québécois legal French use the same baseline with marginal vocabulary differences (noted where relevant).

## Patterns à détecter

### 1. Archaïsmes juridiques

Mots et locutions qui survivent dans la rédaction juridique française sans fournir de travail juridique additionnel. Compter chaque occurrence.

- **Démonstratifs et anaphoriques archaïques.** *ledit, ladite, lesdits, lesdites, dudit, audit, susdit, susmentionné, susvisé, précité.* Chacun substituable par "ce/cet/cette/ces" ou par la reprise nominale.
- **Locutions adverbiales archaïsantes.** *nonobstant, par devers, ci-dessus, ci-après, ci-dessous, ci-joint, ci-inclus, ci-annexé, ci-présent, par les présentes, aux présentes, ès qualités, à l'effet de, à toutes fins utiles, en tant que de besoin.*
- **Formules anciennes.** *icelui, icelle* (extrêmement archaïque — rare mais à signaler chaque fois), *iceux, icelles.*
- **Locutions verbales lourdes.** *aux fins de, en vue de* (préférer "pour"), *aux termes de* (préférer "selon" ou "d'après"), *en raison de, à raison de* (préférer "à cause de" ou la reformulation), *eu égard à* (préférer "vu" ou "compte tenu de"), *afférent à* (préférer "relatif à" ou "concernant"), *consécutif à* (préférer "à la suite de").
- **Formules notariales hors contexte notarial.** *par devant Maître…, comparant…, déclarant savoir et pouvoir signer…, l'an deux mille…* — pertinentes dans les actes authentiques, déplacées dans les CGU/CGV ou un contrat commercial standard.

**Comptage.** Densité d'archaïsmes = (occurrences signalées) / (mots totaux) × 1 000.

| Densité (pour 1 000 mots) | Niveau |
| --- | --- |
| 0–2 | Vert |
| 3–6 | Jaune |
| 7–11 | Ambre |
| 12+ | Rouge |

### 2. Substantivation (nominalisation)

Le français juridique a une affinité naturelle pour le nom au détriment du verbe. La transformation d'une action en groupe nominal force le lecteur à reconstruire le verbe sous-jacent.

Signaux à détecter :

- Suffixes nominaux après verbes vides ("procéder à", "effectuer", "réaliser", "opérer", "faire") : *procéder à la résiliation, effectuer le paiement, réaliser une notification, opérer la cession, faire mention de.*
- Constructions en "la X de Y" où X est un nom déverbal : *la résolution du litige, l'exécution du contrat, la fixation du prix, la mise en œuvre des présentes.*
- "Mise en …" lourde : *mise en œuvre, mise en demeure* (terme technique, à conserver lorsqu'il vise la procédure de mise en demeure de l'article 1344 du Code civil), *mise en place, mise à disposition, mise en demeure préalable.*

Densité de nominalisation = (constructions signalées) / (mots totaux) × 1 000.

| Densité (pour 1 000 mots) | Niveau |
| --- | --- |
| 0–5 | Vert |
| 6–10 | Jaune |
| 11–16 | Ambre |
| 17+ | Rouge |

### 3. Voix passive et tournures impersonnelles

Le français juridique abuse de :
- La voix passive proprement dite : *est réputé, est considéré comme, est notifié.*
- Les tournures impersonnelles : *il est convenu que, il est entendu que, il sera procédé à, il y a lieu de.*
- Le passif pronominal (pseudo-passif) : *le contrat se résout, l'obligation s'éteint.*

Compter chaque tournure. Densité = (tournures) / (verbes finis totaux) × 100.

| Densité passive / impersonnelle | Niveau |
| --- | --- |
| 0–12% | Vert |
| 13–22% | Jaune |
| 23–32% | Ambre |
| 33%+ | Rouge |

Pour les contrats B2B entre professionnels avertis, ajouter 5 points à chaque seuil.

### 4. Longueur des phrases

Le français juridique tolère traditionnellement des phrases plus longues que l'anglais ou l'allemand contemporain, mais la longueur excessive reste un défaut de conception.

Calculer :
- Longueur moyenne de phrase (mots).
- Longueur médiane.
- Phrases > 45 mots ("longues").
- Phrases > 70 mots ("très longues").
- Phrase la plus longue, avec son emplacement.

| Longueur moyenne | Niveau |
| --- | --- |
| 0–20 | Vert |
| 21–28 | Jaune |
| 29–38 | Ambre |
| 39+ | Rouge |

Toujours rapporter moyenne **et** médiane. Une médiane de 22 mais une moyenne de 40 signale quelques phrases monstrueuses tirant la moyenne — à signaler comme problème structurel.

### 5. Subordination en cascade

Spécificité du français juridique : enchaînement de subordonnées relatives ("qui … laquelle … dont … duquel …") sur plusieurs lignes. Détecter :
- Phrases comportant plus de trois subordonnées relatives.
- Chaînes de "lequel/laquelle/lesquels/lesquelles" en cascade (signaleur quasi infaillible de prose lourde).
- Antécédents éloignés de plus de 30 mots de leur relatif.

Une phrase de ce type vaut systématiquement Ambre ou Rouge selon la longueur totale.

### 6. Doubles négations et tournures négatives complexes

*"Aucune Partie ne saurait être réputée n'avoir pas, sauf en cas où il ne lui serait pas déraisonnable de procéder à…"* — chaque couche de négation alourdit le décodage.

Détecter :
- "ne … pas … sans que … ne …"
- "à moins que … ne …"
- "nul ne peut … sauf à …"

Une chaîne par 1 000 mots = Jaune. Deux ou plus = Ambre. Triple négation imbriquée = Rouge.

### 7. Vocabulaire technique pléonastique

Préférer le mot court à équivalence sémantique :

- *préalablement* → avant.
- *postérieurement* → après.
- *concomitamment* → en même temps.
- *nonobstant* → malgré.
- *aux fins de / à l'effet de* → pour.
- *à raison de / en raison de* → à cause de / en raison de (selon le sens).
- *par dérogation à* → contrairement à (selon le contexte).
- *dans la mesure où* → si / quand (selon le contexte).
- *eu égard à* → vu / compte tenu de.
- *aux termes de / au sens de* → selon.
- *réputé* → considéré comme.
- *icelle / icelui* → ce / cette.
- *de convention expresse* → expressément.

Compter les occurrences ; alimenter à la fois le score linguistique et la liste prioritaire de la fin du rapport.

### 8. Densité des renvois internes

Compter "tel que défini à l'article X", "conformément à l'annexe Y", "sous réserve des stipulations des articles X à Y", "ainsi qu'il est dit à l'article Z".

| Renvois pour 1 000 mots | Niveau |
| --- | --- |
| 0–5 | Vert |
| 6–11 | Jaune |
| 12–20 | Ambre |
| 21+ | Rouge |

Signaler en particulier :
- Les chaînes de renvois (article qui renvoie à un article qui renvoie ailleurs).
- Les renvois à des annexes non jointes.

## Score du pilier "Modèles linguistiques" (français)

Combiner les huit sous-scores à poids égal sur 0–100 :

1. Densité d'archaïsmes
2. Densité de nominalisation
3. Densité passive / impersonnelle
4. Longueur moyenne de phrase
5. Subordination en cascade
6. Doubles négations
7. Vocabulaire pléonastique
8. Densité des renvois

Conversion par sous-score :
- Vert → 90.
- Jaune → 70.
- Ambre → 45.
- Rouge → 20.

Score du pilier = moyenne arrondie.

## Spécificités régionales à noter

- **Droit belge.** Vocabulaire administratif plus formel ; "septante"/"nonante" si présents indiquent l'origine belge ou suisse (signal pour Step 2).
- **Droit suisse romand.** "Code des obligations" (CO), "convention de prévoyance", terminologie spécifique au droit des assurances sociales. Le passage "en bonne foi" est traditionnel et conserve sa valeur de terme technique.
- **Droit québécois.** Influence du common law (vocabulaire mixte) ; anglicismes plus tolérés. "Bail" garde son sens technique du Code civil du Québec.
- **Droit français.** Modernisation depuis la réforme du droit des contrats (Ordonnance 2016-131 et Loi 2018-287) : la rédaction post-2016 du Code civil est plus accessible ; signaler comme positif lorsque le contrat suit ce style.

## Sources de référence

- Cornu, Gérard. *Linguistique juridique* (3e éd.).
- Sourioux, J.-L. & Lerat, P. *Le langage du droit*.
- Bouchard, M., Trudeau, H. *La rédaction juridique* (École de Sherbrooke).
- Catherine, Robert. *Le style administratif* (classique du Conseil d'État).
- Gémar, J.-C. *Traduire ou l'art d'interpréter* (utile pour la rédaction multilingue).

Ces sources soutiennent la norme appliquée ; ne pas les citer dans le rapport sauf à la demande de l'utilisateur.

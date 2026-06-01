---
name: recherche-legislation
title: Recherche dans la legislation francaise
description: Rechercher dans les textes legislatifs et reglementaires francais (lois, codes, decrets, ordonnances, arretes, Journal Officiel, conventions collectives). A utiliser quand l'utilisateur cherche "que dit la loi", cite un article de code (Code civil, du travail, de commerce, penal, monetaire et financier, de la sante publique, de la consommation, de l'environnement, general des impots, des assurances, etc.), demande "trouve la loi sur X", "le decret de", "l'ordonnance de", "l'arrete du", evoque le JO ou le Journal Officiel, ou cherche une convention collective par numero IDCC ou par secteur. Mobilise Legifrance (fonds LODA, CODE, JORF, KALI). Lit le profil de pratique pour respecter le format de citation choisi et le perimetre prioritaire.
author: legalmcp
author_url: https://github.com/legalmcp/openlegi-plugin/tree/main/skills/recherche-legislation
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: fr
practice: general
language: en
---

# Recherche dans la legislation francaise

Cette competence permet de rechercher et consulter les textes legislatifs et reglementaires francais via les bases de donnees publiques Legifrance.

**Pre-requis** : lire `~/.claude/plugins/config/recherche-juridique-fr/CLAUDE.md`
au demarrage pour appliquer le format de citation, la verbosite et le perimetre
configures dans le profil de pratique. Si le fichier n'existe pas, suggerer
`/recherche-juridique-fr:cold-start-interview`.

## Quand utiliser cette competence

- L'utilisateur cherche une loi, un decret, une ordonnance ou un arrete
- L'utilisateur veut connaitre le contenu d'un article de code (Code civil, Code du travail, etc.)
- L'utilisateur demande ce que dit la loi sur un sujet precis
- L'utilisateur cherche un texte paru au Journal Officiel
- L'utilisateur cherche une convention collective

## Sources de donnees

| Source | Fond | Outil | Contenu |
|--------|------|-------|---------|
| Legifrance | LODA | `rechercher_dans_texte_legal` | Lois, ordonnances, decrets, arretes |
| Legifrance | CODE | `rechercher_code` | 75+ codes juridiques (civil, penal, travail, commerce, etc.) |
| Legifrance | JORF | `recherche_journal_officiel` | Journal Officiel de la Republique Francaise |
| Legifrance | JORF | `dernier_journal_officiel` | Dernier JO publie |
| Legifrance | KALI | `rechercher_conventions_collectives` | Conventions collectives nationales |

## Workflow de recherche

### Etape 1 : Identifier le type de recherche

Determiner quel fond interroger selon la demande :

| La demande porte sur... | Outil a utiliser |
|------------------------|------------------|
| Un article d'un code precis (ex: "article 1240 du Code civil") | `rechercher_code` |
| Une loi par son numero (ex: "loi 2024-364") | `rechercher_dans_texte_legal` |
| Un decret, une ordonnance, un arrete | `rechercher_dans_texte_legal` |
| Un sujet general (ex: "teletravail") | `rechercher_code` + `rechercher_dans_texte_legal` |
| Un texte recent paru au JO | `recherche_journal_officiel` ou `dernier_journal_officiel` |
| Une convention collective | `rechercher_conventions_collectives` |

### Etape 2 : Construire la requete

**Pour `rechercher_code`** :
- Specifier le nom du code (ex: `CODE_CIVIL`, `CODE_DU_TRAVAIL`, `CODE_DE_COMMERCE`)
- Utiliser des mots-cles precis extraits de la question
- Filtrer par numero d'article si connu

**Pour `rechercher_dans_texte_legal`** :
- Utiliser des termes juridiques precis
- Filtrer par nature de texte (LOI, DECRET, ORDONNANCE, ARRETE) si connu
- Filtrer par date si pertinent

**Pour `recherche_journal_officiel`** :
- Filtrer par emetteur si connu (MINISTERE_JUSTICE, PREMIER_MINISTRE, etc.)
- Filtrer par nature et par date

### Etape 3 : Analyser et presenter les resultats

Pour chaque texte trouve :

1. **Identification** : numero NOR, titre complet, date de publication
2. **Statut** : en vigueur, abroge, modifie — toujours verifier la date de vigueur
3. **Contenu pertinent** : extraire les articles ou dispositions qui repondent a la question
4. **Contexte** : mentionner les modifications recentes ou textes d'application

### Etape 4 : Enrichir si necessaire

Si la reponse legislative est incomplete :
- Croiser avec la jurisprudence (`~~jurisprudence`) pour l'interpretation des textes
- Consulter la doctrine fiscale (`~~doctrine-fiscale`) pour les aspects fiscaux
- Verifier le droit europeen (`~~droit-europeen`) si le sujet a une dimension UE

## Format de reponse

```
## [Sujet de la recherche]

### Textes applicables

**[Titre du texte]**
- Reference : [NOR / numero]
- Date : [date de publication]
- Statut : [en vigueur / modifie le...]

> [Citation des articles pertinents]

### Analyse

[Synthese de ce que disent les textes sur le sujet, en langage clair]

### Points d'attention

- [Modifications recentes a surveiller]
- [Textes d'application en attente]
- [Jurisprudence notable sur l'interpretation]
```

## Bonnes pratiques

- **Toujours verifier la vigueur** : un texte peut avoir ete abroge ou modifie
- **Croiser les sources** : une loi seule ne suffit pas, verifier les decrets d'application
- **Citer les articles** : donner les references exactes pour permettre la verification
- **Dater la recherche** : les bases sont mises a jour quotidiennement, preciser la date de consultation
- **Ne pas interpreter** : presenter le droit positif tel qu'il est, signaler les ambiguites sans trancher

## Limitations

Cette competence donne acces au droit positif francais tel que publie sur Legifrance. Elle ne constitue pas un conseil juridique. Les resultats doivent etre verifies par un professionnel du droit qualifie avant toute prise de decision.

---

**Sortie : brouillon de recherche destine a la relecture d'un professionnel du
droit qualifie. Ce n'est pas un conseil juridique, ce n'est pas une conclusion
juridique, et cela ne remplace pas l'analyse d'un avocat.**

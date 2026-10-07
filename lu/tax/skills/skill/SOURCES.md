# Sources officielles — Paperasse Luxembourg

Toutes les données chiffrées, références juridiques et procédures de ce dépôt s'appuient exclusivement sur les sources officielles luxembourgeoises listées ci-dessous. En cas de divergence entre ce dépôt et la source officielle, **la source officielle fait foi**.

## 1. Plan comptable — Plan Comptable Normalisé (PCN)

| Élément | Détail |
|---|---|
| Texte de référence | Règlement grand-ducal du 12 septembre 2019 fixant le Plan Comptable Normalisé |
| Publication | Mémorial A n° 642 du 23 septembre 2019 |
| Autorité | Commission des Normes Comptables (CNC) |
| Site officiel | https://www.cnc.lu |
| Texte consolidé | https://legilux.public.lu (recherche "Plan Comptable Normalisé") |
| Fichier dans ce dépôt | `comptable/data/pcn-comptes.json` |

## 2. Fiscalité — équivalent du Code Général des Impôts français

Le Luxembourg n'a pas de code unique ; la fiscalité est répartie entre plusieurs lois publiées sur **Legilux** (https://legilux.public.lu), équivalent luxembourgeois de Légifrance.

| Domaine | Texte de référence | Autorité |
|---|---|---|
| Impôt sur le revenu (personnes physiques et collectivités, IRC) | Loi modifiée du 4 décembre 1967 concernant l'impôt sur le revenu (**L.I.R.**) | ACD |
| Impôt commercial communal (ICC) | Loi modifiée du 1er décembre 1936 sur l'impôt commercial communal | ACD + communes |
| Impôt sur la fortune (IF) | Loi modifiée du 16 octobre 1934 sur l'évaluation des biens et valeurs (**L.É.F.**) | ACD |
| TVA | Loi modifiée du 12 février 1979 concernant la TVA | AED |
| Droits d'enregistrement et de transcription | Loi modifiée du 7 août 1920 ; Loi du 30 juillet 2002 (Bëllegen Akt) | AED |
| Taxe d'abonnement (OPC, sociétés holding) | Loi modifiée du 17 décembre 2010 | AED |

**Autorités fiscales :**

- **ACD** — Administration des Contributions Directes : https://impotsdirects.public.lu (impôts directs : LIR, ICC, IF)
- **AED** — Administration de l'Enregistrement, des Domaines et de la TVA : https://pfi.public.lu (TVA, enregistrement, succession)
- **ADA** — Administration des Douanes et Accises : https://douanes.public.lu (accises, droits d'importation)

**Fichiers dans ce dépôt :** `comptable/data/irc-icc-if.json`, `comptable/data/tva-taux.json`, `notaire/data/droits-enregistrement.json`, `fiscaliste/data/*.json`.

## 3. Audit légal — équivalent de la CNCC française

Au Luxembourg, deux entités encadrent l'audit, contre une seule en France :

| Entité | Rôle | Site officiel |
|---|---|---|
| **IRE** — Institut des Réviseurs d'Entreprises | Ordre professionnel des réviseurs d'entreprises agréés (équivalent CNCC pour l'aspect ordre) | https://www.ire.lu |
| **CSSF** — Commission de Surveillance du Secteur Financier | Autorité publique de supervision des audits d'Entités d'Intérêt Public (EIP) (équivalent H3C/H2A) | https://www.cssf.lu |

| Élément | Détail |
|---|---|
| Cadre légal | Loi modifiée du 23 juillet 2016 relative à la profession de l'audit |
| Normes d'audit applicables | **ISA** (International Standards on Auditing) adoptées telles quelles, contrairement aux NEP françaises |
| Liste publique des réviseurs agréés | Tableau IRE consultable sur https://www.ire.lu |
| Fichiers dans ce dépôt | `commissaire-aux-comptes/references/normes-isa.md`, `commissaire-aux-comptes/data/seuils-audit.json` |

## 4. Données ouvertes — équivalent de data.gouv.fr

| Portail / source | Contenu utile | URL |
|---|---|---|
| **data.public.lu** | Portail open data officiel (CTIE), équivalent direct de data.gouv.fr — API CKAN standard disponible sur `/api/3/action/` | https://data.public.lu |
| **STATEC** | Statistiques officielles (économie, fiscalité, démographie) | https://statistiques.public.lu |
| **LBR — Registre de Commerce et des Sociétés** | Comptes annuels déposés en XBRL, formes juridiques, dirigeants | https://www.lbr.lu |
| **eCDF** | Plateforme officielle de dépôt des formulaires comptables et fiscaux (XBRL, schémas XML) | https://ecdf.b2g.etat.lu |
| **Guichet.lu** | Source faisant foi pour toutes les démarches administratives | https://guichet.public.lu |
| **Legilux** | Texte intégral et consolidé de toutes les lois et règlements (Mémorial A et B) | https://legilux.public.lu |

**Script d'aide** : `scripts/fetch-open-data.js` permet d'interroger l'API CKAN de data.public.lu pour découvrir et télécharger des jeux de données pertinents (taux ICC par commune, statistiques TVA, etc.). Voir l'usage dans le script même.

## Mise à jour

Les chiffres (taux d'imposition, seuils, barèmes) évoluent chaque année, généralement par la loi budgétaire votée en décembre pour l'année suivante. Une revue annuelle de tous les fichiers `data/*.json` est recommandée à chaque parution du Mémorial A budgétaire (généralement entre le 20 et le 31 décembre).

## Disclaimer

Ce dépôt est un outil d'aide. Il ne remplace ni l'avis d'un professionnel (expert-comptable, réviseur agréé, fiscaliste, notaire) ni la consultation directe des sources officielles ci-dessus. Les auteurs déclinent toute responsabilité en cas d'usage du contenu sans validation par un professionnel qualifié.

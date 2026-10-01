# Dépôt eCDF et publication RCS

## eCDF — Plateforme commune de dépôt

### Définition
**eCDF** = Espace Commun de Dépôt des Données Financières — plateforme officielle pour :
- Comptes annuels (bilan, CPP, annexe)
- Déclarations TVA (TVA-100, TVA-101, TVA-CSI)
- Déclarations fiscales (IRC/ICC/IF — formulaire 500)
- Rapport de gestion
- Rapport du réviseur

### Accès
- URL : **https://ecdf.public.lu**
- Authentification : **LuxTrust** (Token, Smartcard, Signing Stick, ou Mobile)
- ID Beneficial Owner : matricule national + matricule personne morale

## Modèles de comptes annuels

### MIRA / SIRA
- **MIRA** : Modèle Intégré de Reporting Annuel — version standard / abrégée
- **SIRA** : Modèle Standard de Reporting Annuel — version complète
- Format **XML** structuré selon schémas XSD eCDF
- **Outil de saisie** : disponible sur eCDF.public.lu (interface web) ou export depuis logiciel comptable certifié

### Selon catégorie d'entreprise

| Catégorie | Modèle |
|---|---|
| Micro | Bilan + CPP très abrégés |
| Petite | Modèle abrégé |
| Moyenne | Modèle complet, audit obligatoire |
| Grande | Modèle complet + rapport gestion détaillé + rapport audit |

### Annexe — informations obligatoires
- Méthodes comptables et changements
- Détail des immobilisations (mouvements)
- Détail des participations
- Effectif moyen par catégorie
- Rémunérations des organes d'administration
- Honoraires du réviseur (si applicable)
- Engagements hors bilan
- Événements postérieurs significatifs

## Workflow de dépôt comptes annuels

### Étape 1 — Saisie
- Logiciel comptable (export XML eCDF)
- Ou saisie manuelle sur portail eCDF

### Étape 2 — Validation
- Le portail vérifie la conformité au schéma XSD
- Cohérence : actif = passif, totaux corrects
- En cas d'erreur : correction obligatoire avant signature

### Étape 3 — Signature électronique
- Signature LuxTrust de l'**administrateur** ou **gérant** habilité
- Si réviseur d'entreprises : signature additionnelle de son rapport

### Étape 4 — Transmission
- Validation finale → transmission simultanée :
  - **ACD** (pour la déclaration fiscale)
  - **AED** (pour la TVA si applicable)
  - **RCS** (pour publication RESA)
  - **Statec** (statistiques)

### Étape 5 — Confirmation
- Accusé de réception PDF avec n° de dépôt
- Délai de publication RESA : généralement 1 à 5 jours ouvrés

## RCS — Registre de Commerce et des Sociétés

### Plateforme
- **LBR.lu** (Luxembourg Business Registers)
- Géré par le LBR (entité publique sous tutelle MJ)

### Documents à déposer (annuels)
1. **Comptes annuels** (eCDF — déjà transmis automatiquement)
2. **PV de l'AGO** mentionnant l'approbation des comptes
3. **Liste des participations** (sociétés liées détenues)
4. **Rapport de gestion** (si moyenne/grande)
5. **Rapport du réviseur** (si audit)
6. **Décisions de répartition du résultat**

### Délais
- **7 mois** après clôture (loi 19 décembre 2002, art. 79)
- Pour exercice clos 31/12 → **dépôt avant le 31 juillet N+1**

### Frais (2025)
- Petite entreprise : ~30 €
- Moyenne : ~50 €
- Grande : ~75 €
- Pénalité retard : majoration progressive

### Publication RESA
- **RESA** = Recueil Électronique des Sociétés et Associations
- Publication automatique des dépôts
- Consultable gratuitement sur **lbr.lu**
- Permet aux tiers d'accéder aux comptes

## Sanctions retard / défaut

### RCS
- Amende administrative **25 à 1 250 €** (loi 27 mai 2016)
- Inscription d'office d'une mention « comptes non déposés » au RCS
- Risque de **dissolution judiciaire** après 3 années consécutives de défaut (art. 1200-1 loi sociétés)
- Refus d'extraits RCS officiels

### ACD / AED
- Majoration jusqu'à **10 %** de l'impôt en cas de retard de déclaration (LIR + AO)
- **Taxation d'office** en cas d'absence prolongée

## Cas particulier : sociétés non actives / dormantes

- Toutes les sociétés inscrites au RCS doivent déposer des comptes, même si inactives
- Comptes peuvent être à 0 € (« comptes nuls ») mais doivent être déposés
- Coût : forfait minimum de dépôt

## Cas particulier : SCSp et sociétés sans personnalité morale

- **SCSp** : pas de personnalité morale → pas d'obligation comptable LRC stricto sensu, mais obligations contractuelles + fiscales
- Inscription RCS obligatoire mais comptes non publiés (sauf statuts contraires)

## Liens

- eCDF : https://ecdf.public.lu
- LBR : https://www.lbr.lu
- RESA (consultation) : https://www.lbr.lu/resa
- Loi 19 décembre 2002 : https://eli.legilux.public.lu/eli/etat/leg/loi/2002/12/19
- Loi 27 mai 2016 RCS : https://eli.legilux.public.lu/eli/etat/leg/loi/2016/05/27

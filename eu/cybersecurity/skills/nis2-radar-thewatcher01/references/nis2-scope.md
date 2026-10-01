# Périmètre NIS2 — Table de référence

## Seuils de classification

| Catégorie | Effectif | Chiffre d'affaires | Bilan annuel |
|-----------|----------|--------------------:|-------------:|
| **Entité essentielle** | >= 250 salariés | >= 50 M EUR | >= 43 M EUR |
| **Entité importante** | >= 50 salariés | >= 10 M EUR | >= 10 M EUR |
| **Hors périmètre** | < 50 salariés | < 10 M EUR | < 10 M EUR |

**Note** : Il suffit de dépasser UN des seuils (effectif OU CA OU bilan) pour être concerné, à condition d'opérer dans un secteur couvert.

## Exceptions — Entités essentielles quelle que soit la taille

- Fournisseurs de services DNS
- Registres de noms de domaine de premier niveau (TLD)
- Prestataires de services de confiance qualifiés
- Fournisseurs de réseaux publics de communications électroniques
- Entités de l'administration publique centrale
- Entités identifiées comme critiques au titre de la directive CER

## Secteurs hautement critiques (Annexe I)

| Secteur NIS2 | Codes NAF correspondants | Exemples |
|--------------|--------------------------|----------|
| **Énergie** | 3511Z, 3512Z, 3513Z, 3514Z, 3521Z, 3522Z, 3523Z, 3530Z, 0610Z, 0620Z, 4950Z | Électricité, gaz, pétrole, hydrogène, chauffage/refroidissement urbain |
| **Transports** | 4910Z, 4920Z, 5010Z, 5020Z, 5110Z, 5121Z, 5210A, 5210B | Aérien, ferroviaire, maritime, routier (uniquement opérateurs d'importance) |
| **Banque** | 6419Z, 6492Z | Établissements de crédit |
| **Infrastructures des marchés financiers** | 6611Z | Opérateurs de plateformes de négociation, contreparties centrales |
| **Santé** | 8610Z, 8621Z, 8622Z, 8623Z, 2110Z, 2120Z, 3250A | Hôpitaux, laboratoires, fabricants de dispositifs médicaux, fabricants pharma |
| **Eau potable** | 3600Z | Distribution d'eau potable |
| **Eaux usées** | 3700Z | Collecte et traitement des eaux usées |
| **Infrastructures numériques** | 6110Z, 6120Z, 6130Z, 6190Z, 6311Z, 6312Z | Fournisseurs IXP, DNS, TLD, cloud, datacenters, CDN, services de confiance, télécom |
| **Gestion des services TIC (B2B)** | 6201Z, 6202A, 6202B, 6203Z, 6209Z | Fournisseurs de services managés (MSP), fournisseurs de services de sécurité managés (MSSP) |
| **Espace** | 5122Z, 7219Z | Opérateurs d'infrastructures terrestres de soutien aux services spatiaux |
| **Administration publique** | 8411Z, 8412Z, 8413Z | Entités de l'administration publique centrale (hors défense/sécurité nationale) |

## Secteurs critiques (Annexe II)

| Secteur NIS2 | Codes NAF correspondants | Exemples |
|--------------|--------------------------|----------|
| **Services postaux et d'expédition** | 5310Z, 5320Z | Prestataires de services postaux, messagerie et colis |
| **Gestion des déchets** | 3811Z, 3812Z, 3821Z, 3822Z, 3831Z, 3832Z | Collecte, traitement, recyclage |
| **Fabrication, production et distribution de produits chimiques** | 2011Z, 2012Z, 2013A, 2013B, 2014Z, 2015Z, 2016Z, 2017Z, 2020Z, 2030Z, 2041Z, 2042Z, 2051Z, 2052Z, 2053Z, 2059Z, 2060Z | Chimie de base, pesticides, peintures, etc. |
| **Production, transformation et distribution de denrées alimentaires** | 1011Z-1089Z, 1091Z-1092Z, 4631Z, 4632Z, 4633Z, 4634Z, 4636Z, 4637Z, 4638A, 4638B, 4639A, 4639B | Industrie alimentaire, commerce de gros alimentaire |
| **Fabrication** | 2611Z-2612Z, 2620Z, 2630Z, 2640Z, 2651A, 2651B, 2660Z, 2670Z, 2680Z, 2711Z, 2712Z, 2720Z, 2731Z, 2732Z, 2733Z, 2740Z, 2751Z, 2752Z, 2790Z, 2811Z-2899Z, 2910Z, 2920Z, 2932Z, 3011Z, 3012Z, 3020Z, 3030Z, 3040Z, 3091Z, 3092Z, 3099Z, 3250A, 3250B | Dispositifs médicaux, informatique/électronique, machines, véhicules |
| **Fournisseurs numériques** | 6311Z, 6312Z, 6399Z, 5813Z, 5821Z, 5829A, 5829B, 5829C | Places de marché en ligne, moteurs de recherche, réseaux sociaux |
| **Recherche** | 7211Z, 7219Z | Organismes de recherche (hors établissements d'enseignement) |

## Mapping rapide — Secteurs cibles Teddy Deberdt

Les secteurs les plus fréquents dans l'activité de conseil :

| Cible | NAF fréquents | Statut NIS2 probable |
|-------|---------------|----------------------|
| ESN / SSII | 6201Z, 6202A, 6202B | **Importante** si >= 50 salariés (Gestion services TIC) |
| Hébergeurs / Cloud | 6311Z, 6312Z | **Essentielle** ou **Importante** (Infrastructures numériques) |
| Associations santé | 8610Z, 8621Z, 8622Z | **Importante** si >= 50 salariés (Santé) |
| Industrie manufacturing | 2811Z-2899Z | **Importante** si >= 50 salariés (Fabrication) |
| Éditeurs logiciel | 5829A, 5829B, 5829C | **Importante** si >= 50 salariés (Fournisseurs numériques) |
| Collectivités | 8411Z | **Essentielle** (Administration publique) |

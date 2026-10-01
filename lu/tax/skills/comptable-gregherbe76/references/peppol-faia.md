# Peppol et FAIA — facturation électronique et SAF-T au Luxembourg

## 1. Peppol — facturation électronique

### Cadre légal
- **Loi du 16 mai 2019** sur la facturation électronique dans les marchés publics (transposition directive 2014/55/UE)
- Standard imposé : **Peppol BIS Billing 3.0** au format UBL 2.1 ou UN/CEFACT CII

### Obligation B2G (Business-to-Government)

**OBLIGATOIRE** depuis le 18 mars 2023 pour toute facture émise vers un organisme public lux :
- État (administrations centrales)
- Communes et syndicats de communes
- Établissements publics
- Toutes entités relevant des marchés publics

Phasage :
| Date | Catégorie obligée |
|---|---|
| 18 mai 2022 | Grandes entreprises |
| 18 octobre 2022 | Moyennes entreprises |
| **18 mars 2023** | Petites + micro-entreprises |

### Statut B2B
**Pas encore obligatoire au Luxembourg en 2025**, mais :
- La directive UE **ViDA** (VAT in the Digital Age) prévoit la facturation électronique B2B intra-UE obligatoire à horizon **2030-2032**
- Adoption volontaire encouragée (le format simplifie la comptabilité)

### Comment émettre une facture Peppol

#### Option 1 — MyGuichet.lu (gratuit)
- Pour PME envoyant à des organismes publics
- Saisie en ligne ou import d'un fichier UBL
- Transmission Peppol intégrée

#### Option 2 — Access Point certifié
- Solutions tierces : **Basware, Pagero, Tradeshift, Cegedim, Yooz, Mercurius (Belgique-Lux)**
- Connexion API depuis ERP / logiciel facturation
- Coût mensuel ~10 à 100 € selon volume

#### Option 3 — ERP avec connecteur Peppol intégré
- SAP, Microsoft Dynamics, Sage, **BOB-50 (Lux)**, Cegid…

### Identifiant Peppol
- Format Lux : `0208:<matricule national 13 chiffres>`
- Exemple : `0208:20121234567`
- Annuaire public : https://directory.peppol.eu/

### Réception de factures Peppol
- Tout assujetti TVA peut configurer son **endpoint Peppol** pour recevoir des factures
- Inscription via Access Point ou MyGuichet

## 2. FAIA — SAF-T luxembourgeois

### Définition
**FAIA** = **F**ichier d'**A**udit **I**nformatisé de l'**A**ED — équivalent luxembourgeois du SAF-T (Standard Audit File for Tax) imposé par l'OCDE.

### Cadre
- **Circulaire AED n° 780** (mise à jour régulière)
- Format **XML** normé (schéma XSD publié par l'AED)
- Obligation de **transmission sur demande** lors d'un contrôle fiscal

### Quand est-il demandé ?
- Lors d'un **contrôle fiscal** AED ou ACD sur place
- Obligatoirement disponible pour la **période contrôlée** (jusqu'à 10 ans en cas de fraude)
- Délai habituel pour le fournir après demande : **15 à 30 jours**

### Contenu du fichier FAIA

Sections principales :

1. **Header** : identification entreprise, période, devise, numéro TVA, exercice
2. **MasterFiles** :
   - Plan comptable (PCN intégral utilisé)
   - Clients (avec coordonnées, matricules)
   - Fournisseurs
   - Produits (codes articles, taux TVA, comptes)
   - Comptes bancaires
3. **GeneralLedgerEntries** : toutes les écritures comptables de la période
   - Numéro pièce, date, libellé, compte, débit/crédit, contre-partie, journal
4. **SourceDocuments** :
   - **Factures de vente émises** (lignes détaillées)
   - **Factures d'achat reçues**
   - Mouvements de stock
   - Encaissements/décaissements

### Logiciels conformes FAIA

Les principaux logiciels comptables luxembourgeois génèrent le FAIA nativement :
- **BOB-50** (Sage)
- **Wincarat** (Quadient)
- **Ettlinger** (Ettlinger Lux)
- **Microsoft Dynamics 365 Business Central** (avec extension Lux)
- **Sage Cloud** Lux
- **Cegid Quadra Lux**

Outil open-source : `scripts/generate-faia.js` du présent skill (basique, pour audit ponctuel).

### Vérification FAIA avant envoi
1. Validation contre le schéma XSD AED
2. Cohérence : total débits = total crédits par journal et par exercice
3. Cohérence comptes / PCN
4. Toutes les pièces sources rattachables aux écritures

### Sanctions absence/non-conformité FAIA
- L'AED peut exiger le fichier **dans les 10 jours** ; en cas de non-fourniture :
  - Taxation d'office
  - Amende administrative jusqu'à **10 000 €**
  - En cas de fraude établie : sanctions pénales

### Lien avec Peppol
- Les factures émises via Peppol au format UBL contiennent toutes les données nécessaires au FAIA
- Bonne pratique : un système ERP unique gère Peppol et génère le FAIA

## 3. Bonnes pratiques

- Mettre en place dès le début **un logiciel comptable certifié FAIA**
- Utiliser des **codes articles, comptes et matricules tiers normalisés**
- Conserver les **PDF des factures originales** liées aux écritures
- Faire un **test de génération FAIA** chaque trimestre (détection précoce des anomalies)
- Tenir un **registre des opérations intra-UE** avec matricules TVA validés VIES

## 4. Liens

- Documentation FAIA AED : https://pfi.public.lu/fr/professionnels/AED.html
- Schéma XSD FAIA : sur demande auprès de l'AED
- Peppol Authority Lux : https://digital.public.lu
- Loi facturation 2019 : https://eli.legilux.public.lu/eli/etat/leg/loi/2019/05/16/a338/jo

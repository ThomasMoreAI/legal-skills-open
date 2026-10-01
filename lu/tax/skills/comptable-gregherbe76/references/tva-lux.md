# TVA luxembourgeoise — référence détaillée

## Cadre légal

- **Loi modifiée du 12 février 1979** concernant la taxe sur la valeur ajoutée
- **Directive 2006/112/CE** (directive TVA UE) — transposée en droit luxembourgeois
- Autorité : **Administration de l'Enregistrement, des Domaines et de la TVA (AED)** — https://pfi.public.lu

## Taux applicables (2025)

| Taux | Pourcentage | Exemples principaux |
|---|---|---|
| Normal | **17 %** | Conseil, vente matériel, logiciels, restauration de luxe |
| Intermédiaire | **14 %** | Vins (<13°), publicité, brochures imprimées |
| Réduit | **8 %** | Coiffure, plantes, gaz/électricité (sous conditions) |
| Super-réduit | **3 %** | Alimentation, médicaments, livres, hôtellerie, restauration courante, transport personnes, vêtements enfants |

### TVA-logement 3 %

Travaux de **création ou rénovation** d'un logement affecté à la résidence principale → taux super-réduit 3 % au lieu de 17 %, plafonné à **50 000 € d'avantage fiscal par logement**.

**Procédure** : demande d'agrément TVA-logement à l'AED **AVANT** les travaux (formulaire 750-F).

## Régimes déclaratifs

| CA annuel HT | Périodicité |
|---|---|
| ≤ 112 000 € | **Annuelle** uniquement (TVA-100) |
| 112 000 – 620 000 € | **Trimestrielle** + TVA-100 annuelle |
| > 620 000 € | **Mensuelle** + TVA-100 annuelle |

### Échéances

- Déclarations périodiques : **15 du 2e mois suivant** la période (ex. T1 → 15 mai)
- TVA-100 annuelle : **1er mars** de l'année N+1
- État récapitulatif intracommunautaire (ESL/CSI) : **15 du mois suivant**

## Franchise PME

Depuis le **1er janvier 2025** : seuil de franchise relevé à **50 000 € de CA HT annuel** (auparavant 35 000 €).

L'entreprise sous franchise :
- Ne facture pas de TVA
- Ne déduit pas la TVA sur ses achats
- Mention obligatoire sur facture : « Régime particulier — Franchise des petites entreprises »
- Doit toujours s'identifier auprès de l'AED si activité économique régulière

## Opérations intracommunautaires

### Livraisons B2B intra-UE
- **Exonérées** si :
  - Numéro TVA acheteur valide (vérification VIES)
  - Preuve de transport hors Lux (CMR, ordres expédition)
- Reportées en case 17 de la TVA-100
- Mention sur facture : « Livraison intracommunautaire exonérée — art. 138 dir. TVA / art. 43 loi TVA »

### Acquisitions intra-UE
- **Auto-liquidation** : TVA collectée + déductible simultanément (cases 35-37)
- Ne génère pas de décaissement si entreprise pleinement déductible

### Services B2B intra-UE
- Lieu de taxation = pays du **preneur** (art. 17 directive)
- Auto-liquidation par le client
- Mention : « Auto-liquidation par le preneur — art. 196 dir. TVA »

### OSS / IOSS (B2C intra-UE)
- Au-delà de **10 000 €** de CA B2C intra-UE annuel → enregistrement OSS obligatoire
- Déclaration unique trimestrielle via MyGuichet → reversement aux États membres

## Format eCDF — déclaration électronique

- Plateforme : **eCDF.public.lu** (Économie commune des données financières)
- Format **XML** normalisé
- Connexion via certificat **LuxTrust** (Token, Smartcard, Signing Stick)
- Signature électronique obligatoire

## Mentions facture obligatoires (rappel)

Cf. `peppol-formats.json` pour la liste exhaustive. Les principales :

1. Numéro séquentiel unique
2. Date d'émission
3. Identité fournisseur (raison sociale, adresse, RCS, matricule TVA)
4. Identité client (matricule TVA si B2B intra-UE > 10 000 €)
5. Description précise des biens/services
6. Quantité, prix unitaire HT, total HT
7. Taux TVA et montant TVA par taux
8. Total HT et TTC
9. Mentions spéciales (auto-liquidation, franchise, etc.)

## Pénalités

- Retard paiement : intérêts **0,6 % / mois** (= 7,2 % / an)
- Défaut de déclaration : amende **250 à 10 000 €**
- TVA éludée : majoration **10 à 25 %** de la taxe
- Fraude > 200 000 € : qualification pénale

## Conservation

- **10 ans** pour pièces comptables (Code de commerce art. 11)
- Numérique accepté avec garantie d'intégrité

## Liens utiles

- Portail TVA AED : https://pfi.public.lu/fr/professionnels/tva.html
- eCDF : https://ecdf.public.lu
- Vérification VIES : https://ec.europa.eu/taxation_customs/vies/
- Demande matricule TVA : MyGuichet → AED

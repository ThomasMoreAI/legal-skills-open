# TVA, régimes et déclarations

## Seuils 2026 (indicatifs, à vérifier)

### Franchise en base (dispense de TVA)

| Activité | Seuil HT | Tolérance |
|----------|----------|-----------|
| Services | 36 800 € | 39 100 € |
| Ventes et hébergement | 91 900 € | 101 000 € |

### Réel simplifié

| Activité | Seuil max HT |
|----------|--------------|
| Services | 254 000 € |
| Ventes | 840 000 € |

### Réel normal (au-delà)

Obligatoire si la TVA annuelle exigible > 15 000 €.

## Déclarations

### CA3 (réel normal mensuel)

- Périodicité : mensuelle
- Échéance : entre le 16 et le 24 du mois suivant selon 1er digit SIREN
  - Digit 0, 1, 2 : 16-17
  - Digit 3, 4, 5, 6, 7 : 19-20
  - Digit 8, 9 : 21-24

### CA3 trimestrielle

Possible si TVA annuelle due < 4 000 €.
Échéance : trimestre suivant, date selon SIREN.

### CA12 (réel simplifié)

- 1 déclaration annuelle
- Acompte juillet : 55% de la TVA de référence N-1
- Acompte décembre : 40% de la TVA N-1
- Solde : au dépôt de la CA12 (3-5 mois après clôture)

## Opérations intra-UE

### DEB (Déclaration d'Échanges de Biens)

- Ventes intra-UE : obligatoire si CA intra-UE > 460 000 € (modification 2022)
- Achats intra-UE : obligatoire dès le 1er euro
- Échéance : 10e jour ouvré du mois suivant

### DES (Déclaration Européenne de Services)

- Obligatoire pour toutes les prestations intra-UE
- Échéance : 10e jour ouvré du mois suivant

## Taux de TVA 2026

| Taux | Usage |
|------|-------|
| 20% | Normal (la plupart des biens/services) |
| 10% | Restauration, travaux immobiliers rénovation, transport |
| 5.5% | Produits alimentaires, livres, spectacles, énergie |
| 2.1% | Médicaments remboursés, presse |
| 0% | Export hors UE, livraisons intra-UE (à un assujetti) |

### DOM-TOM

- Taux normal Martinique/Guadeloupe : **8.5%**
- Taux réduit DOM : **2.1%**
- Régime TVA NPR (Non Perçue Récupérable) applicable

## Contrôle de cohérence CA3

Balance comptable au 31/M :
- Compte 44571 TVA collectée : doit correspondre à la TVA sur les ventes du mois
- Compte 44566 TVA déductible : doit correspondre à la TVA sur les achats du mois
- Solde net = 44571 - 44566 - 44567 (TVA sur immos)

Si solde > 0 (plus de collectée que déductible) → TVA à payer.
Si solde < 0 (plus de déductible) → Crédit de TVA (reporter ou demander remboursement).

## Script `tva_checker.py`

Vérifie la cohérence entre :
- Compte 44571 (TVA collectée) dans la balance
- CA HT × taux de TVA appliqués (ventilé par taux)
- CA3 déclarée auprès de la DGFiP

Alerte si discordance > 1% ou 1 000 €.

## Pénalités en cas de retard

- **Retard de dépôt** : 10% (pas d'infraction antérieure) → 40% (infractions antérieures) + intérêts de retard 0,4%/mois
- **Défaut de dépôt** : taxation d'office avec coefficient aggravant

## Remboursement de crédit TVA

Si crédit > 760 € (seuil simplifié) : demande de remboursement via CA3 / 3519-SD.
Traitement DGFiP : 4-12 semaines.

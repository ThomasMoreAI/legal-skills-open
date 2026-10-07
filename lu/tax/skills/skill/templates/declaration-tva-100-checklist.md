# Checklist — Déclaration TVA annuelle 100 (Luxembourg)

Plateforme : **eCDF** (https://ecdf.b2g.etat.lu) — authentification LuxTrust ou eIDAS.

À déposer **au 1er mai N+1** (récapitulative annuelle) ou **1er mars N+1** (régime annuel simplifié).

---

## Avant de remplir

- [ ] Matricule TVA actif et à jour (LU + 8 chiffres)
- [ ] FAIA généré et archivé
- [ ] Toutes les déclarations périodiques (mensuelles ou trimestrielles) déposées
- [ ] Rapprochement entre les déclarations périodiques et le compte 70x du grand livre
- [ ] Listing récapitulatif intracommunautaire (état 270) à jour

---

## Cases principales (déclaration 100)

### Opérations imposables (Chiffre d'affaires)

| Case | Libellé | Source comptable |
|------|---------|------------------|
| 011 | CA taxé à 17 % | Compte 70x (taux standard) |
| 012 | CA taxé à 14 % | Compte 70x (taux intermédiaire) |
| 013 | CA taxé à 8 % | Compte 70x (taux réduit) |
| 014 | CA taxé à 3 % | Compte 70x (taux super-réduit) |
| 019 | CA taxé à autre taux (transitoire) | – |

### Opérations non imposables / exonérées

| Case | Libellé | Justificatif |
|------|---------|--------------|
| 021 | Livraisons intracom (art. 43) | Listing 270 + matricule TVA client |
| 022 | Exports hors UE | Documents douaniers (DAU export) |
| 023 | Opérations exonérées avec droit à déduction (banque, assurance art. 44) | Contrats |
| 024 | Opérations exonérées sans droit à déduction (médical, enseignement) | Justification d'exonération |
| 025 | Locations immobilières exonérées | Bail |

### TVA collectée

- [ ] TVA collectée à 17 % = case 011 × 17 %
- [ ] TVA collectée à 14 % = case 012 × 14 %
- [ ] TVA collectée à 8 % = case 013 × 8 %
- [ ] TVA collectée à 3 % = case 014 × 3 %
- [ ] **Total TVA collectée** (case 030)

### TVA déductible

| Case | Libellé | Vérification |
|------|---------|--------------|
| 041 | TVA sur achats de biens (factures fournisseurs) | Compte 442 |
| 042 | TVA sur services reçus | Compte 442 |
| 043 | TVA sur immobilisations | Compte 442 (sous-compte immo) |
| 044 | TVA autoliquidée (intracom + service hors UE) | Égalité collectée = déductible |
| 050 | **Total TVA déductible** | |

### Régularisations

- [ ] Régularisations bonnes/mauvaises créances (art. 13)
- [ ] Régularisations sur immobilisations (durée 5 ou 20 ans selon nature)
- [ ] Prorata si activité mixte (assujetti + exonéré)

### Solde

- [ ] **TVA à payer** (case 030 − 050) **ou** **TVA à récupérer**

---

## Cohérence à vérifier avant validation

| Contrôle | Source |
|----------|--------|
| Σ CA des 12 mois (déclarations périodiques) = CA récapitulatif | Déclarations 100 mensuelles vs récap |
| Total TVA collectée = ∑ comptes 441x | Grand livre |
| Total TVA déductible = ∑ comptes 442x | Grand livre |
| CA intracom = listing 270 cumulé annuel | État 270 vs déclarations |

---

## Erreurs fréquentes

- Oubli d'un mois (régime mensuel) ou trimestre (régime trimestriel)
- TVA récupérée sur frais de réception (non récupérable au-delà de 30 %)
- TVA récupérée sur cadeaux > 40 € HT/bénéficiaire/an (non récupérable)
- Listing 270 désaccordé avec la case 021
- Auto-liquidation oubliée pour services reçus de prestataires hors Lux

---

## Pénalités en cas de retard

- **Déclaration tardive** : 10 % du montant dû
- **Intérêts de retard** : 0,75 % par mois (art. 84 loi TVA)
- **Défaut de déclaration** : amende jusqu'à 25 000 € (art. 77)

---

> Source : loi modifiée du 12 février 1979 concernant la TVA + circulaires AED.

---
name: legal-docs-fr-kernel8901
title: Legal Docs FR
description: Générateur de documents juridiques français pour freelances/micro-entrepreneurs. Génère des CGV, mentions légales, contrats de prestation et devis en HTML.
author: Kernel8901
author_url: https://github.com/Kernel8901/ai-agent-skills-classification/tree/main/%E7%BD%91%E9%A1%B5%E4%B8%8E%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91/legal-docs-fr
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: fr
practice: general
language: fr
sources:
- title: French Legal Ref
  path: references/french-legal-ref.md
---

# Legal Docs FR

Générateur de documents juridiques français pour freelances/micro-entrepreneurs.
Génère des CGV, mentions légales, contrats de prestation et devis en HTML.

## Scripts

Tout dans `scripts/`. Python 3 stdlib uniquement. Documents dans `~/.freelance/legal/`.

### legal.py — Génération de documents juridiques

```bash
# CGV — Conditions Générales de Vente
python3 legal.py generate cgv [--no-open]
python3 legal.py generate cgv --tribunal "Paris" --mediateur "CMAP, Paris"

# Mentions légales pour un site web
python3 legal.py generate mentions --hebergeur "Vercel Inc, San Francisco" [--site "monsite.fr"] [--dpo "dpo@email.com"]

# Contrat de prestation de services
python3 legal.py generate contrat --client "Acme Corp" --mission "Développement application web" \
  --montant 5000 --duree "3 mois" [--client-address "10 rue Example, Paris"] \
  [--client-siret "12345678900010"] [--date-debut "01/03/2026"] [--non-sollicitation]

# Devis
python3 legal.py generate devis --client "Acme Corp" --items "Dev frontend:10:400" "Design UX:3:500" \
  [--number DEV-2026-001] [--date 2026-02-15]

# Lister tous les documents générés
python3 legal.py list [--json]

# Voir la configuration prestataire
python3 legal.py config [--json]
```

Tous les documents supportent `--no-open` pour ne pas ouvrir dans le navigateur.

### Overrides prestataire (sur toutes les commandes generate)
```bash
--nom "Hugo Dupont" --siret "12345" --adresse "42 rue X" --email "x@y.com" --phone "06..."
```
Si `~/.freelance/config.json` existe (du freelance-toolkit), les infos sont pré-remplies.

## Documents générés

| Type | Fichier | Contenu |
|------|---------|---------|
| CGV | `cgv.html` | 10 articles : objet, commandes, paiement (30j, 3×taux légal, 40€), délais, PI, responsabilité, résiliation, force majeure, juridiction, médiation |
| Mentions | `mentions.html` | Identité, hébergeur, directeur publication, RGPD (droits, finalités, DPO), cookies, PI |
| Contrat | `contrat-{client}-{ts}.html` | Parties, mission, durée, prix (30/70), obligations, confidentialité, PI, résiliation, non-sollicitation optionnelle |
| Devis | `DEV-YYYY-NNN.html` | Numéro auto, validité 30j, lignes de prestation, conditions de paiement, signature "Bon pour accord" |

## Configuration

Utilise `~/.freelance/config.json` (partagé avec freelance-toolkit) :
```json
{
  "provider": { "name": "...", "address": "...", "siret": "...", "email": "...", "phone": "..." },
  "micro_entreprise": true,
  "tva_rate": 0
}
```

Si `micro_entreprise: true` → mention art. 293B du CGI sur tous les documents.

## Données

```
~/.freelance/legal/
├── cgv.html / cgv.json
├── mentions.html / mentions.json
├── contrat-acme-20260215-143022.html / .json
├── DEV-2026-001.html / .json
└── ...
```

## Contenu juridique

Les documents incluent les clauses obligatoires du droit français :
- **Paiement** : 30 jours, pénalités 3× taux légal, indemnité 40€ (art. D441-5 Code de commerce)
- **PI** : Cession subordonnée au paiement intégral
- **Médiation** : Obligatoire depuis 2016 (art. L611-1 Code de la consommation)
- **RGPD** : Droits des personnes, finalités, durée conservation, contact DPO
- **Force majeure** : Art. 1218 du Code civil

Voir `references/french-legal-ref.md` pour le détail des obligations légales.

## Notes
- HTML avec CSS inline, optimisé pour impression / export PDF
- Montants au format français (2 900,00 €)
- Initiales du prestataire comme logo (même style que les factures)
- `--json` disponible sur `list` et `config`

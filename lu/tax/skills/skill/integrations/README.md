# Intégrations Paperasse Lux

Connecteurs pour récupérer automatiquement vos données bancaires, paiements et facturation.

## Connecteurs disponibles

| Connecteur | Usage | Statut |
|---|---|---|
| [`psd2-tink/`](./psd2-tink/) | Récupérer transactions des banques LU (BCEE, BIL, BGL, ING, Raiffeisen) via PSD2 / Open Banking | v0.1 — squelette |
| [`stripe/`](./stripe/) | Récupérer paiements Stripe (multi-comptes, Stripe Connect) | v0.1 — squelette |
| [`peppol/`](./peppol/) | Émettre / recevoir des factures électroniques B2G via Peppol BIS 3.0 | v0.1 — documentation |

## Configuration

1. Copiez `.env.example` en `.env` à la racine du repo et remplissez les clés.
2. Créez `company.json` (à partir de `company.example.json`) avec vos comptes bancaires.
3. Lancez `npm install` puis `npm run fetch` pour tout récupérer en une fois.

## Pourquoi PSD2 et pas une banque-spécifique ?

Au Luxembourg il n'y a pas d'équivalent direct à Qonto avec une API publique simple. Les banques LU (BCEE, BIL, BGL BNP Paribas, Banque Raiffeisen, ING Luxembourg, Banque de Luxembourg) exposent toutes leurs comptes via l'**API PSD2** standardisée (Berlin Group NextGenPSD2). On passe donc par un agrégateur agréé qui parle PSD2 avec toutes ces banques en une seule API :

- **[Tink](https://tink.com)** (recommandé, racheté par Visa)
- **[Salt Edge](https://www.saltedge.com)**
- **[Bridge by Bud](https://bud.financial)**
- **[Klarna Kosma](https://www.kosma.com)**

Le squelette ci-joint cible Tink, mais le pattern est interchangeable.

# Stripe — paiements en ligne

Récupère les charges Stripe pour les inclure dans la comptabilité.

## Configuration

```bash
STRIPE_SECRET=sk_live_...
```

Pour plusieurs comptes Stripe séparés :

```bash
STRIPE_SECRET_SHOP=sk_live_...
STRIPE_SECRET_SAAS=sk_live_...
```

Pour Stripe Connect (clé plateforme + sous-comptes) :

```bash
STRIPE_PLATFORM_SECRET=sk_live_...
```

Et dans `company.json` :

```json
{
  "stripe": {
    "accounts": [
      { "name": "shop", "type": "standalone", "envVar": "STRIPE_SECRET_SHOP" },
      { "name": "marketplace", "type": "connect", "stripeAccountId": "acct_xxx" }
    ]
  }
}
```

## Usage

```bash
npm run fetch:stripe
```

Écrit les charges dans `data/transactions/stripe-<account>-<YYYY-MM>.json`.

## Spécificité Luxembourg

Stripe LU émet des factures au nom de **Stripe Payments Europe Ltd** (Dublin, Irlande). Les commissions Stripe arrivent donc en facture B2B intra-UE — autoliquidation TVA si vous êtes assujetti LU (article 196 directive 2006/112/CE).

# Tink — Open Banking PSD2 (banques LU)

Connecteur générique pour récupérer les transactions des banques luxembourgeoises via [Tink](https://tink.com) (Visa). Tink parle PSD2 avec toutes les banques LU agréées.

## Banques LU couvertes

BCEE, BIL, BGL BNP Paribas, Banque Raiffeisen, ING Luxembourg, Banque de Luxembourg, Post Finance, Quintet Private Bank, Banque Internationale à Luxembourg.

## Configuration

1. Créer un compte développeur sur https://console.tink.com
2. Récupérer `client_id` + `client_secret`
3. Renseigner dans `.env` :

```bash
TINK_CLIENT_ID=...
TINK_CLIENT_SECRET=...
```

4. Renseigner dans `company.json` :

```json
{
  "tink": {
    "userId": "votre-user-id-tink",
    "marketCode": "LU"
  }
}
```

## Usage

```bash
npm run fetch:tink
```

Récupère les transactions de tous les comptes liés et les écrit dans `data/transactions/<bank>-<account>-<YYYY-MM>.json` au format normalisé (date, libellé, montant, devise, contrepartie, IBAN).

## Format de sortie

```json
[
  {
    "id": "tink-tx-123",
    "date": "2025-04-15",
    "libelle": "Virement client TechSolutions Sàrl",
    "montant": 1170.00,
    "devise": "EUR",
    "iban_contrepartie": "LU280019400644750000",
    "categorie": "encaissement_client"
  }
]
```

## Limites v0.1

- Authentification 3DS interactive nécessaire la première fois (consentement PSD2 valable 90 jours puis renouvellement).
- Pas de catégorisation auto LU-spécifique : à brancher dans `comptable/scripts/`.
- Pas de gestion des comptes multi-devises (USD, GBP, CHF) — à ajouter si besoin.

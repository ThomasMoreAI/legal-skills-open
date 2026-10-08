---
name: fintech-compliance-checker-khalilbenaz
title: Vérificateur de Conformité Fintech
description: Vérification de conformité pour applications fintech — PCI-DSS, KYC/AML, PSD2, RGPD appliqué aux données financières. À utiliser quand l'utilisateur développe une application de paiement, un wallet ou un service financier et doit vérifier la conformité réglementaire. Se déclenche aussi avec "PCI-DSS", "KYC", "AML", "PSD2", "conformité paiement", "compliance fintech", "données bancaires", "carte de crédit sécurité". Also triggers on "PCI-DSS compliance", "KYC and AML requirements", "PSD2 compliance".
author: khalilbenaz
author_url: https://github.com/khalilbenaz/claude-skills-collection/tree/main/finance-skills/fintech-compliance-checker
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: ma
practice: regulatory
language: fr
---

# Vérificateur de Conformité Fintech

## Workflow en 5 étapes

1. **Cartographier le périmètre** : identifier les flux de données financières (carte, virement, wallet, crypto) et les marchés cibles (UE, US, MENA…).
2. **Sélectionner les référentiels** : croiser type de service × géographie → liste des normes applicables (tableau ci-dessous).
3. **Auditer point par point** : pour chaque norme, dérouler la checklist correspondante ; noter les gaps avec niveau de risque (critique / élevé / moyen).
4. **Corriger et prioriser** : implémenter les contrôles manquants critiques en premier ; documenter chaque décision (ADR ou ticket).
5. **Maintenir la preuve** : logs d'audit, scans périodiques, enregistrement des consentements — tout doit être traçable et exportable.

---

## 1. Sélection des référentiels applicables

| Service | Réglementations applicables |
|---------|---------------------------|
| Paiement par carte | PCI-DSS v4, PSD2, RGPD |
| Wallet / compte de paiement | KYC/AML (DLTF/5AMLD), PSD2, RGPD |
| Transfert d'argent (remittance) | Règlement UE 2015/847, KYC/AML, RGPD |
| Prêt / crédit consommation | Directive 2023/2225, RGPD |
| Crypto-actifs | MiCA (applicable depuis déc. 2024), KYC/AML, RGPD |
| Open Banking / AISP-PISP | PSD2, Berlin Group API, RGPD |

---

## 2. PCI-DSS v4 — Checklist développeur

### Données de carte : ce qui est interdit

```
INTERDIT (même chiffré) :
  - Stocker le CVV/CVC après autorisation
  - Stocker le contenu de la piste magnétique
  - Logger le PAN complet dans les fichiers de log

INTERDIT :
  - Envoyer des données de carte par email, chat, SMS
  - Recevoir le numéro de carte sur vos propres serveurs si scope SAQ A possible
```

### Tokenisation — flux recommandé

```
# Stripe / Adyen / Braintree
Client (browser/app)
  └─► Stripe.js / Hosted Fields
        └─► PSP (hors scope PCI)
              └─► token  tok_live_xxxxx  → votre backend
                          ↓
              api.stripe.com/v1/charges { source: tok_live_xxxxx }
```

Votre backend ne voit jamais le PAN. Scope réduit à SAQ A ou SAQ A-EP.

### Niveaux PCI-DSS et obligations

| Niveau | Volume annuel | Exigence minimale |
|--------|--------------|-------------------|
| 1 | > 6 M transactions | Audit QSA sur site + ASV scan trimestriel |
| 2 | 1–6 M | SAQ + ASV scan trimestriel |
| 3 | 20 K–1 M (e-commerce) | SAQ A-EP ou SAQ D |
| 4 | < 20 K (e-commerce) | SAQ A (si full-redirect PSP) |

### Exigences techniques PCI-DSS v4 nouvelles (2025+)

- Exigence 6.4.3 : gestion d'inventaire et intégrité de tous les scripts de page de paiement (CSP + SRI).
- Exigence 11.6.1 : détection des modifications non autorisées des pages de paiement (script tamper detection).
- TLS 1.0 et 1.1 définitivement interdits ; TLS 1.2 minimum, TLS 1.3 recommandé.

```bash
# Vérifier TLS d'un endpoint
openssl s_client -connect api.monservice.com:443 -tls1_2 </dev/null 2>&1 | grep "Protocol"
# Ou avec testssl.sh (outil open source)
./testssl.sh --protocols api.monservice.com
```

---

## 3. KYC/AML — Approche basée sur le risque

### Niveaux de due diligence (5AMLD / DLTF)

| Niveau | Seuil indicatif UE | Vérifications requises |
|--------|-------------------|----------------------|
| Simplifié (SDD) | < 150 €/mois, produit à faible risque listé | Email + téléphone (profil limité) |
| Standard (CDD) | Usage courant | Pièce d'identité + preuve d'adresse + screening sanctions |
| Renforcé (EDD) | > 2 500 €/mois, PEP, pays à haut risque FATF | Identité + source des fonds + justificatif patrimoine + revue périodique |

### Screening sanctions — intégration code

```python
# Exemple avec l'API Comply Advantage / ComplyLaunch
import requests

def screen_customer(name: str, dob: str) -> dict:
    resp = requests.post(
        "https://api.complyadvantage.com/searches",
        headers={"Authorization": f"Token {API_KEY}"},
        json={
            "search_term": name,
            "filters": {"birth_year": dob[:4]},
            "share_url": False,
            "types": ["sanction", "pep", "warning", "adverse-media"],
        },
        timeout=10,
    )
    resp.raise_for_status()
    hits = resp.json()["content"]["data"]["hits"]
    return {"clear": len(hits) == 0, "hits": hits}
```

Alternatives : Refinitiv World-Check, Dow Jones Risk & Compliance, listes publiques OFAC/EU/ONU (CSV téléchargeables).

### Checklist AML

- [ ] Screening initial à l'onboarding + re-screening périodique (min. annuel)
- [ ] Détection PEP (Personne Politiquement Exposée) et membres de famille
- [ ] Monitoring transactionnel : règles de seuil + modèle comportemental
- [ ] Déclaration de soupçon automatisée vers Tracfin (FR) / CRF (TN) / FinCEN (US)
- [ ] Conservation des données KYC : 5 ans après fin de relation (obligation légale)
- [ ] Gel des avoirs : blocage immédiat si match sanctions confirmé

### Red flags à coder comme règles de détection

```
STRUCTURING : montant < seuil déclaration sur N transactions proches dans le temps
VELOCITY    : > X transactions en 24 h sur un même compte
GEOGRAPHY   : destination dans pays FATF liste grise/noire
ROUND_TRIP  : dépôt → retrait immédiat sans utilisation intermédiaire
NEW_ACCOUNT : volume élevé les 48 h suivant la création du compte
```

---

## 4. PSD2 / SCA — Authentification Forte

### Règle SCA

```
Transaction > 30 € → 2 facteurs obligatoires parmi :
  - Connaissance  : mot de passe, PIN
  - Possession    : téléphone (OTP SMS/TOTP), carte physique
  - Inhérence     : biométrie (empreinte, face ID)
```

### Exemptions applicables (à documenter)

| Exemption | Condition | Responsabilité du risque |
|-----------|-----------|--------------------------|
| Low-value | < 30 € (cumul < 100 € ou < 5 tx) | Émetteur |
| Trusted beneficiary | Bénéficiaire whitelisté par le payeur | Émetteur |
| Recurring | Même montant + même bénéficiaire | Émetteur |
| TRA (Transaction Risk Analysis) | Taux fraude < seuil EBA + scoring bas | Acquéreur ou émetteur |
| Corporate / B2B | Comptes d'entreprise dédiés | Émetteur |

### Implémentation 3DS2 (Stripe exemple)

```javascript
// Côté client — gérer le défi SCA
const { error, paymentIntent } = await stripe.confirmCardPayment(clientSecret, {
  payment_method: { card: cardElement },
});
if (error?.code === "authentication_required") {
  // Redemander la SCA via stripe.handleNextAction(clientSecret)
}
```

---

## 5. RGPD — Données financières

### Durées de conservation légales

| Donnée | Durée | Base légale |
|--------|-------|-------------|
| Transactions / pièces comptables | 10 ans | Obligation légale (Code commerce) |
| Dossiers KYC | 5 ans après fin de relation | LCB-FT / 5AMLD |
| Données de carte tokenisées | Durée mandat + 13 mois | Contrat / Consentement |
| Logs d'accès et connexion | 12 mois | Intérêt légitime / LCEN |
| Consentements marketing | Jusqu'au retrait + 3 ans | Consentement |

### Droits des utilisateurs — implémentation minimale

- **Portabilité** : endpoint `/api/user/export` → JSON/CSV des transactions (format Account Statement ISO 20022 recommandé).
- **Effacement** : pseudonymiser (ne pas supprimer) les données soumises à conservation légale ; effacer les données hors obligations.
- **Accès** : réponse sous 30 jours ; authentification forte avant divulgation.
- **Rectification** : formulaire avec audit trail de la modification.

```python
# Pseudonymisation irréversible pour données hors conservation légale
import hashlib, os

def pseudonymize(value: str, salt: bytes = None) -> str:
    salt = salt or os.urandom(16)
    return hashlib.blake2b(value.encode(), key=salt, digest_size=32).hexdigest()
```

---

## 6. Garde-fous et anti-patterns fréquents

| Anti-pattern | Risque | Correction |
|---|---|---|
| Logger `request.body` sur un endpoint de paiement | PCI-DSS violation, amende + perte certification | Filtrer les champs sensibles avant log (`pan`, `cvv`, `card_number`) |
| KYC "one-shot" sans re-screening | Passer à côté d'une sanction ajoutée après onboarding | Cron de re-screening hebdomadaire sur la base clients active |
| SCA contournée côté backend pour "améliorer l'UX" | Fraude, responsabilité acquéreur, amende ABE | Utiliser les exemptions officielles PSD2, documenter le choix |
| Conservation infinie des données "au cas où" | RGPD — amende CNIL jusqu'à 4 % du CA mondial | Mettre en place une politique de purge automatique par type de donnée |
| Secrets d'API PSP dans le code source | Compromission PSP, fraude directe | Vault (HashiCorp / AWS Secrets Manager) + rotation automatique |
| Validation KYC uniquement côté client | Contournement trivial | Toujours re-valider côté serveur, renvoyer le statut KYC depuis le backend |

---

## 7. Commandes d'audit utiles

```bash
# Scanner les secrets dans le code (clés API, PANs…)
trufflehog git file://. --only-verified

# Vérifier les headers de sécurité d'un endpoint
curl -I https://api.monservice.com/v1/payments | grep -E "Strict-Transport|Content-Security|X-Frame"

# Tester les ciphers TLS (rejeter TLS < 1.2)
nmap --script ssl-enum-ciphers -p 443 api.monservice.com

# Vérifier l'inventaire des scripts de paiement (PCI v4 req. 6.4.3)
# Générer les SRI hashes pour les scripts tiers
curl -s https://cdn.js.stripe.com/v3/ | openssl dgst -sha384 -binary | openssl base64 -A
```

---

> Ce skill fournit des orientations techniques et opérationnelles. Pour des décisions de conformité engageant la responsabilité légale de l'entreprise, consulter un juriste spécialisé en droit financier et/ou un QSA PCI certifié.

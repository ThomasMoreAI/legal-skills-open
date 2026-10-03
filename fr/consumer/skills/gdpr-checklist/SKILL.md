---
name: gdpr-checklist
title: GDPR / RGPD — Checklist de conformité
description: Aide à vérifier la conformité RGPD/GDPR d'un site, d'une app ou d'un traitement de données. Se déclenche aussi avec "RGPD", "GDPR", "données personnelles", "politique de confidentialité", "cookies", "conformité", ou toute question de protection des données. Also triggers on "GDPR compliance", "privacy policy check", "data protection checklist".
author: khalilbenaz
author_url: https://github.com/khalilbenaz/claude-skills-collection/tree/main/legal-skills/gdpr-checklist
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: fr
practice: consumer
language: en
---

# GDPR / RGPD — Checklist de conformité

> Cette checklist est un outil d'auto-évaluation structuré. Pour toute situation à enjeu réel (amende, plainte, audit CNIL), consultez un DPO certifié ou un avocat spécialisé en droit des données.

---

## Étape 1 — Cadrer le périmètre

Avant de cocher quoi que ce soit, répondez à ces questions :

1. **Quels types de données** sont collectées ? (email, IP, localisation, données de santé, paiement…)
2. **Quelles finalités** ? (marketing, analytics, exécution du contrat, sécurité…)
3. **Qui est concerné** ? (utilisateurs EU, mineurs, salariés, prospects B2B…)
4. **Qui traite** ? (vous seul, sous-traitants : Stripe, Mailchimp, Datadog, Sentry…)
5. **Volume** : moins de 250 salariés ? Traitement à grande échelle ? Données sensibles (art. 9) ?

> Si données de santé, biométriques, origine raciale, opinions politiques/syndicales, orientation sexuelle → règles renforcées, DPIA obligatoire.

---

## Étape 2 — Registre des traitements (art. 30)

Obligation dès que vous traitez des données pour compte propre ou en tant que sous-traitant.

| Traitement | Finalité | Base légale | Données | Durée conservation | Destinataires | Transfert hors EU |
|---|---|---|---|---|---|---|
| Analytics | Mesure d'audience | Intérêt légitime / Consentement | IP anonymisée, pages vues | 13 mois | Plausible / Matomo | Non |
| Newsletter | Marketing | Consentement | Email, prénom | Jusqu'au désabonnement | Mailchimp (USA) | Oui — SCCs |

**Conseil pratique :** utilisez un tableur ou un outil DPO (Axeptio, Didomi, Witik) pour maintenir ce registre vivant.

---

## Étape 3 — Bases légales (art. 6)

Chaque traitement doit reposer sur **une seule** base légale clairement documentée :

- **Consentement** : libre, éclairé, spécifique, univoque. Cases pré-cochées = non valide.
- **Contrat** : données strictement nécessaires à l'exécution (ex. adresse de livraison).
- **Obligation légale** : factures, déclarations fiscales.
- **Intérêts vitaux** : cas d'urgence médicale uniquement.
- **Mission d'intérêt public** : réservé aux organismes publics.
- **Intérêt légitime** : possible si l'intérêt ne prévaut pas sur les droits de la personne (test LIA requis). **Non applicable** au marketing direct vers des particuliers sans consentement.

---

## Étape 4 — Consentement & cookies (ePrivacy + RGPD)

### Bandeau cookies conforme CNIL 2026

```
✅ Bouton "Accepter tout" visible
✅ Bouton "Refuser tout" aussi visible (même niveau, même couleur)
✅ Lien "Personnaliser" fonctionnel
✅ Cookies analytics/pub bloqués AVANT clic
✅ Choix mémorisé 6 mois max (CNIL) puis redemande
✅ Retrait du consentement aussi simple que le don
```

**Cookies strictement nécessaires** (pas de consentement requis) : session de connexion, panier, CSRF token, équilibrage de charge.

**Exemple de vérification rapide en console :**
```js
// Vérifie si Google Analytics se charge avant consentement
// Dans l'onglet Network, filtrer "analytics" ou "gtag"
// Si présent au chargement initial → non conforme
```

### Consentement formulaire

```html
<!-- NON CONFORME : case pré-cochée -->
<input type="checkbox" checked> J'accepte de recevoir des emails

<!-- CONFORME -->
<input type="checkbox"> J'accepte de recevoir la newsletter (vous pouvez vous désabonner à tout moment)
```

---

## Étape 5 — Transparence & politique de confidentialité

La politique doit inclure (art. 13/14) :

- [ ] Identité et coordonnées du responsable de traitement
- [ ] Coordonnées du DPO si désigné
- [ ] Finalités et base légale de chaque traitement
- [ ] Durées de conservation par catégorie
- [ ] Destinataires (sous-traitants nommés ou catégories)
- [ ] Transferts hors EU : pays, mécanisme (SCCs, décision d'adéquation)
- [ ] Liste des droits et comment les exercer
- [ ] Droit de réclamation auprès de la CNIL (cnil.fr)
- [ ] Si intérêt légitime : droit d'opposition

---

## Étape 6 — Droits des personnes (art. 15-22)

| Droit | Délai réponse | Ce qu'il faut implémenter |
|---|---|---|
| Accès (art. 15) | 1 mois | Export de toutes les données de l'utilisateur |
| Rectification (art. 16) | 1 mois | Modification via profil ou support |
| Effacement (art. 17) | 1 mois | Suppression compte + backups (délai raisonnable) |
| Portabilité (art. 20) | 1 mois | Export JSON/CSV machine-readable |
| Opposition (art. 21) | Sans délai | Opt-out marketing, désactivation intérêt légitime |
| Limitation (art. 18) | 1 mois | Gel du traitement sans suppression |

**Endpoint d'export — exemple Node.js :**
```js
app.get('/api/me/export', requireAuth, async (req, res) => {
  const data = await collectUserData(req.user.id); // profil, commandes, logs
  res.setHeader('Content-Disposition', 'attachment; filename="mes-donnees.json"');
  res.json(data);
});
```

---

## Étape 7 — Sécurité & sous-traitants (art. 25, 28, 32)

### Sécurité technique
- [ ] HTTPS partout (HSTS activé)
- [ ] Chiffrement des données sensibles au repos (bcrypt pour mots de passe, AES-256 pour données médicales/bancaires)
- [ ] Accès aux données de production limité et loggé
- [ ] MFA sur les comptes admin
- [ ] Politique de rétention : purge automatique après expiration

### Sous-traitants
- [ ] DPA (Data Processing Agreement) signé avec chaque sous-traitant
- [ ] Sous-traitants listés dans la politique (ou page dédiée)
- [ ] Vérification que les sous-traitants US bénéficient du Data Privacy Framework ou de SCCs

### Violation de données (art. 33-34)
- [ ] Procédure documentée de gestion d'incident
- [ ] Notification CNIL sous **72 heures** si risque pour les personnes
- [ ] Notification des personnes concernées si risque élevé

---

## Étape 8 — DPIA (art. 35) — Quand est-elle obligatoire ?

Obligatoire si au moins deux critères parmi :
- Profilage ou décision automatisée
- Données sensibles (santé, biométrie, etc.)
- Surveillance systématique à grande échelle
- Personnes vulnérables (mineurs, patients)
- Croisement de données issues de sources multiples

→ Si obligatoire : réalisez-la avant le démarrage du traitement, documentez-la, consultez la CNIL si risque résiduel élevé.

---

## Étape 9 — Tableau des manquements identifiés

| Point de contrôle | Statut | Action corrective | Priorité | Responsable |
|---|---|---|---|---|
| Bandeau cookies | ❌ Bouton refus absent | Ajouter bouton refus niveau 1 | 🔴 Critique | Dev front |
| DPA Stripe | ✅ Signé | — | — | — |
| Export données | ⚠️ Manuel seulement | Automatiser endpoint /export | 🟡 Moyen | Backend |

---

## Anti-patterns fréquents (pièges à éviter)

- **Dark patterns** : bouton "Refuser" caché, couleur grisée, 12 clics pour refuser → sanction CNIL.
- **Consentement groupé** : une case pour tout accepter (analytics + pub + partage tiers) → invalide.
- **"Anonymisation" partielle** : IP tronquée mais user_id conservé → toujours une donnée personnelle.
- **Durée de conservation infinie** : "nous conservons vos données aussi longtemps que nécessaire" sans durée chiffrée → non conforme.
- **Sous-traitant sans DPA** : utiliser Sentry, Datadog, Intercom sans DPA signé → violation directe.
- **Mineurs** : si votre service peut toucher des moins de 15 ans (France), consentement parental requis.
- **Logs de prod accessibles à tous** : logs contenant emails/IPs sans restriction d'accès → risque art. 32.

---

## Ressources de référence

- CNIL — guides sectoriels : [cnil.fr/fr/les-guides-de-la-cnil](https://www.cnil.fr/fr/les-guides-de-la-cnil)
- Liste des traitements nécessitant une DPIA : [cnil.fr/fr/DPIA](https://www.cnil.fr/fr/les-traitements-qui-requirent-une-aipd)
- Data Privacy Framework (transferts US) : [dataprivacyframework.gov](https://www.dataprivacyframework.gov)
- Texte consolidé RGPD : [eur-lex.europa.eu — Règlement 2016/679](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX%3A32016R0679)

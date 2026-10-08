---
name: rgpdix-dduquenne
title: Rgpdix — Conformité RGPD & Protection des Données Personnelles
description: 'Expert en conformité RGPD et protection des données personnelles pour applications métier TypeScript. Utilise ce skill dès qu''une question touche au Règlement Général sur la Protection des Données : registre des traitements, bases légales, durées de conservation, droits des personnes (accès, portabilité, effacement, rectification), consentement, anonymisation, pseudonymisation, Privacy Impact Assessment (PIA/AIPD), mentions légales, politique de confidentialité, cookies, ou toute implémentation technique de conformité RGPD. Déclenche également pour : "données personnelles", "RGPD", "GDPR", "droit à l''oubli", "droit d''accès", "portabilité", "consentement", "DPO", "registre des traitements", "durée de conservation", "anonymisation", "pseudonymisation", "PIA", "AIPD", "CNIL", "base légale", "finalité", "sous-traitant", "transfert de données", "données sensibles", "catégorie spéciale", "cookie banner", "mentions légales", "politique de confidentialité". Ce skill est CRITIQUE
  pour les données médico-sociales (CREAI) et les données RH (Link''s).'
author: dduquenne
author_url: https://github.com/dduquenne/unanima-platform/tree/main/.claude/skills/rgpdix
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: fr
practice: data-protection
language: fr
---

# Rgpdix — Conformité RGPD & Protection des Données Personnelles

Tu es **Rgpdix**, expert en conformité RGPD pour les applications métier TypeScript
du monorepo Unanima. Tu garantis que chaque traitement de données personnelles respecte
le cadre réglementaire européen et les recommandations de la CNIL.

> **Règle d'or : la conformité RGPD n'est pas un document — c'est une pratique continue
> intégrée au cycle de développement.**

---

## 1. Cartographie des risques RGPD du monorepo

| Application | Données traitées | Catégorie RGPD | Niveau de risque |
|---|---|---|---|
| **Link's Accompagnement** | Bilans de compétences, parcours professionnels, CV | Données personnelles RH | 🟠 Élevé |
| **CREAI Île-de-France** | Données médico-sociales, situations de handicap | **Catégorie spéciale** (art. 9) | 🔴 Très élevé |
| **Omega Automotive** | Contacts clients, historique SAV, données Salesforce | Données commerciales | 🟡 Moyen |

> ⚠️ **CREAI traite des données de santé** (catégorie spéciale RGPD, art. 9). Cela impose
> des obligations renforcées : base légale spécifique, PIA obligatoire, mesures de sécurité
> renforcées, et DPO désigné.

---

## 2. Les 6 bases légales (art. 6 RGPD)

Pour chaque traitement de données, identifier la base légale applicable :

| Base légale | Usage dans Unanima | Exemple |
|---|---|---|
| **Consentement** | Cookies, newsletter, prospection | Cookie banner, inscription newsletter |
| **Contrat** | Exécution du service acheté | Suivi des bilans (Link's), gestion SAV (Omega) |
| **Obligation légale** | Comptabilité, archivage | Conservation des factures 10 ans |
| **Intérêt légitime** | Analytics, amélioration service | Logs d'audit, statistiques anonymes |
| **Mission d'intérêt public** | CREAI (accompagnement médico-social) | Transformation de l'offre |
| **Intérêts vitaux** | Rarement applicable | — |

### Pour les données de santé (CREAI) — art. 9
Base légale supplémentaire nécessaire parmi :
- Consentement **explicite** de la personne
- Nécessité pour des raisons d'intérêt public dans le domaine de la santé publique
- Nécessité aux fins de la médecine préventive ou du travail

---

## 3. Droits des personnes — Implémentation technique

### Package `@unanima/rgpd`

Le monorepo fournit `packages/rgpd/` avec les briques suivantes :

```
packages/rgpd/src/
├── components/
│   ├── LegalNotice.tsx         ← Mentions légales configurables
│   ├── PrivacyPolicy.tsx       ← Politique de confidentialité
│   └── CookieBanner.tsx        ← Bandeau cookies (consentement)
├── api/
│   ├── export.ts               ← Droit d'accès / portabilité (JSON/CSV)
│   ├── delete.ts               ← Droit à l'effacement
│   └── audit.ts                ← Journal des demandes d'exercice de droits
└── config.ts                   ← RGPDConfig (raison sociale, DPO, finalités)
```

### Droit d'accès (art. 15) — Export des données

```typescript
// Endpoint : GET /api/rgpd/export
// Retourne toutes les données personnelles de l'utilisateur en JSON
export async function exportUserData(userId: string): Promise<UserDataExport> {
  const supabase = createServerClient()

  const [profile, auditLogs, documents] = await Promise.all([
    supabase.from('profiles').select('*').eq('id', userId).single(),
    supabase.from('audit_logs').select('*').eq('user_id', userId),
    // ... toutes les tables contenant des données de l'utilisateur
  ])

  return {
    exportedAt: new Date().toISOString(),
    profile: profile.data,
    activityLog: auditLogs.data,
    documents: documents.data,
    // ...
  }
}
```

### Droit à l'effacement (art. 17) — Suppression / anonymisation

```typescript
// ⚠️ Stratégie selon le contexte :
// - Données avec obligation légale de conservation → anonymisation
// - Données sans obligation → suppression complète

export async function deleteUserData(userId: string): Promise<DeletionReport> {
  const supabase = createServerClient()

  // ① Anonymiser les données avec obligation de conservation
  await supabase.from('audit_logs')
    .update({ user_id: null, ip_address: null })
    .eq('user_id', userId)

  // ② Supprimer les données sans obligation
  await supabase.from('documents').delete().eq('owner_id', userId)

  // ③ Supprimer le profil (CASCADE supprime les FK)
  await supabase.auth.admin.deleteUser(userId)

  // ④ Logger la demande d'exercice de droit
  await logRGPDRequest(userId, 'erasure', 'completed')

  return { deletedAt: new Date().toISOString(), status: 'completed' }
}
```

### Droit de portabilité (art. 20)

```typescript
// Export dans un format structuré, couramment utilisé et lisible par machine
// Format : JSON ou CSV
export async function exportPortable(userId: string, format: 'json' | 'csv') {
  const data = await exportUserData(userId)

  if (format === 'csv') {
    return convertToCSV(data)
  }
  return JSON.stringify(data, null, 2)
}
```

---

## 4. Durées de conservation

| Donnée | Durée | Base | Action à expiration |
|---|---|---|---|
| Compte utilisateur inactif | 3 ans après dernière connexion | CNIL | Suppression ou anonymisation |
| Bilan de compétences | 1 an après fin de prestation | Code du travail | Anonymisation |
| Données médico-sociales | Défini par le cadre réglementaire | Réglementation santé | Archivage sécurisé |
| Logs d'audit | 1 an | Intérêt légitime | Anonymisation |
| Données SAV | 5 ans après fin de relation | Prescription civile | Suppression |
| Cookies analytics | 13 mois max | CNIL | Suppression automatique |

### Implémentation technique des durées

```sql
-- Fonction de purge automatique (à planifier via cron Supabase)
CREATE OR REPLACE FUNCTION rgpd_purge_expired_data()
RETURNS void LANGUAGE plpgsql SECURITY DEFINER AS $$
BEGIN
  -- Anonymiser les comptes inactifs depuis 3 ans
  UPDATE public.profiles
  SET email = 'anonymized-' || id || '@deleted.local',
      full_name = 'Utilisateur supprimé',
      metadata = '{}',
      is_active = false
  WHERE updated_at < now() - interval '3 years'
    AND is_active = true;

  -- Anonymiser les logs d'audit de plus d'1 an
  UPDATE public.audit_logs
  SET user_id = NULL, ip_address = NULL
  WHERE created_at < now() - interval '1 year'
    AND user_id IS NOT NULL;
END;
$$;
```

---

## 5. Registre des traitements (art. 30)

Chaque application doit maintenir un registre des traitements dans sa documentation :

```markdown
## Registre des traitements — [Nom de l'app]

### Traitement 1 : Gestion des comptes utilisateurs
- **Finalité** : Authentification et gestion des accès
- **Base légale** : Exécution du contrat (art. 6.1.b)
- **Catégories de personnes** : Utilisateurs de la plateforme
- **Catégories de données** : Email, nom, rôle, date de connexion
- **Destinataires** : Supabase (hébergeur BDD), Vercel (hébergeur app)
- **Durée de conservation** : 3 ans après dernière connexion
- **Transferts hors UE** : Oui (Vercel US — clauses contractuelles types)
- **Mesures de sécurité** : Chiffrement TLS, RLS, audit trail

### Traitement 2 : ...
```

---

## 6. Privacy Impact Assessment (PIA/AIPD)

### Quand est-ce obligatoire ?
- Traitement de données de santé (CREAI) → **obligatoire**
- Profilage ou scoring → **obligatoire**
- Traitement à grande échelle → **obligatoire**
- Nouveau traitement avec risque élevé → **obligatoire**

### Structure d'un PIA

```
1. Description du traitement
   - Finalité, base légale, catégories de données
   - Flux de données (qui collecte, qui traite, qui accède)

2. Évaluation de la nécessité et de la proportionnalité
   - Minimisation des données
   - Durées de conservation justifiées
   - Information des personnes

3. Évaluation des risques pour les droits et libertés
   - Accès illégitime aux données
   - Modification non désirée
   - Disparition des données

4. Mesures de mitigation
   - Chiffrement, pseudonymisation, RLS
   - Sauvegarde, PCA/PRA
   - Formation, sensibilisation
```

---

## 7. Cookie banner et consentement

### Configuration du bandeau cookies

```typescript
// packages/rgpd/src/config.ts
export interface RGPDConfig {
  organisationName: string
  dpoEmail: string
  privacyPolicyUrl: string
  cookies: {
    necessary: CookieCategory    // Toujours actifs (pas de consentement)
    analytics?: CookieCategory   // Consentement requis
    marketing?: CookieCategory   // Consentement requis
  }
  dataRetention: {
    accounts: string             // ex: "3 years"
    auditLogs: string            // ex: "1 year"
  }
}
```

### Règles CNIL pour les cookies
- Consentement **libre, spécifique, éclairé et univoque**
- Refus aussi simple que l'acceptation (pas de dark pattern)
- Conservation du consentement : 13 mois max
- Pas de mur de cookies (cookie wall) sauf cas justifié

---

## 8. Checklist RGPD par sprint

### Pour chaque nouvelle fonctionnalité
- [ ] Quelles données personnelles sont collectées ?
- [ ] Quelle est la base légale ?
- [ ] La finalité est-elle clairement définie ?
- [ ] La minimisation des données est-elle respectée ?
- [ ] La durée de conservation est-elle définie ?
- [ ] Les droits des personnes sont-ils implémentés ?
- [ ] Le registre des traitements est-il mis à jour ?
- [ ] Un PIA est-il nécessaire ?

---

## Références complémentaires

- **`references/registre-traitements-template.md`** — Template de registre des traitements par application
- **`references/pia-guide.md`** — Guide de réalisation d'un PIA avec la méthode CNIL
- **`references/cnil-recommandations.md`** — Recommandations CNIL applicables (cookies, durées, droits)

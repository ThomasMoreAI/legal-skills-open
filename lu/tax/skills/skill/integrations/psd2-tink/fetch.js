#!/usr/bin/env node
/**
 * fetch.js — Récupère les transactions PSD2 via Tink pour les banques LU.
 *
 * v0.1 — STUB NON OPÉRATIONNEL en mode headless.
 *
 * Le flux PSD2 / Open Banking de Tink nécessite une étape interactive
 * obligatoire (consentement utilisateur via Tink Link, redirect callback,
 * échange du code contre user_access_token). Ce flux ne peut PAS être
 * automatisé en pure ligne de commande.
 *
 * Pour une v1 réelle, il faut :
 *   1. Créer une mini app Express qui héberge le redirect Tink Link
 *   2. Exposer un endpoint /callback qui échange le code contre user_access_token
 *   3. Stocker le user_access_token (durée 24h, refresh nécessaire)
 *   4. Renouveler le consentement PSD2 tous les 90 jours (obligation DSP2)
 *
 * Documentation : https://docs.tink.com/resources/transactions
 *                 https://docs.tink.com/resources/account-aggregation/quickstart
 *
 * En attendant, ce script affiche les instructions de configuration et sort
 * proprement avec un code 0 (pour ne pas casser `npm run fetch` agrégé).
 */

const CLIENT_ID = process.env.TINK_CLIENT_ID;
const CLIENT_SECRET = process.env.TINK_CLIENT_SECRET;

console.log("=".repeat(70));
console.log("  TINK / PSD2 — Récupération bancaire luxembourgeoise");
console.log("=".repeat(70));

if (!CLIENT_ID || !CLIENT_SECRET) {
  console.log("");
  console.log("[STUB] Variables d'environnement manquantes.");
  console.log("       Renseignez TINK_CLIENT_ID et TINK_CLIENT_SECRET dans .env");
  console.log("       Voir : integrations/psd2-tink/README.md");
  console.log("");
  process.exit(0);
}

console.log("");
console.log("[STUB] Le flux PSD2 nécessite un consentement interactif (Tink Link)");
console.log("       qui ne peut pas être automatisé en headless.");
console.log("");
console.log("Pour brancher Tink en production :");
console.log("  1. Créer une mini app Express avec un endpoint /tink-callback");
console.log("  2. Lancer le flux Tink Link depuis votre navigateur");
console.log("  3. Échanger le code reçu contre un user_access_token");
console.log("  4. Stocker le token et appeler GET /data/v2/transactions");
console.log("");
console.log("Documentation complète : integrations/psd2-tink/README.md");
console.log("");
console.log("[OK] Stub terminé sans erreur.");
process.exit(0);

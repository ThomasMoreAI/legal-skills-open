#!/usr/bin/env node
/**
 * validate-facture.js — Vérifie qu'une facture (JSON) contient toutes
 * les mentions obligatoires luxembourgeoises (loi TVA modifiée du 12 fév. 1979,
 * art. 61 ; règlement grand-ducal du 21 décembre 1979).
 *
 * Usage : node scripts/validate-facture.js facture.json
 */

import fs from "node:fs";

const REQUIRED = [
  ["numero", "numéro séquentiel"],
  ["dateEmission", "date d'émission"],
  ["dateLivraison", "date de livraison/prestation"],
  ["vendeur.raisonSociale", "raison sociale du vendeur"],
  ["vendeur.adresse", "adresse du vendeur"],
  ["vendeur.matriculeTva", "n° TVA luxembourgeois du vendeur (LU + 8 chiffres)"],
  ["vendeur.rcs", "n° RCS Luxembourg (B + chiffres)"],
  ["client.raisonSociale", "raison sociale du client"],
  ["client.adresse", "adresse du client"],
  ["lignes", "lignes de facture (libellé, quantité, PU HT)"],
  ["totalHT", "total hors TVA"],
  ["tauxTva", "taux de TVA appliqué (17 / 14 / 8 / 3 / exonéré)"],
  ["montantTva", "montant TVA"],
  ["totalTtc", "total TTC en euros"],
  ["modalitesPaiement", "modalités de paiement (échéance, IBAN, BIC)"],
];

const TAUX_VALIDES = [17, 14, 8, 3, 0];

function get(obj, p) {
  return p.split(".").reduce((a, k) => (a == null ? undefined : a[k]), obj);
}

function main() {
  const file = process.argv[2];
  if (!file || !fs.existsSync(file)) {
    console.error("Usage : node scripts/validate-facture.js <facture.json>");
    process.exit(1);
  }
  const f = JSON.parse(fs.readFileSync(file, "utf8"));
  const errors = [];

  for (const [path, label] of REQUIRED) {
    const v = get(f, path);
    if (v === undefined || v === null || v === "" || (Array.isArray(v) && v.length === 0)) {
      errors.push(`Champ manquant : ${path} (${label})`);
    }
  }

  if (f.vendeur?.matriculeTva && !/^LU\d{8}$/.test(f.vendeur.matriculeTva)) {
    errors.push(`Matricule TVA vendeur invalide (attendu : LU + 8 chiffres) — reçu : ${f.vendeur.matriculeTva}`);
  }
  if (f.vendeur?.rcs && !/^B\d+$/.test(f.vendeur.rcs)) {
    errors.push(`N° RCS vendeur invalide (attendu : B + chiffres) — reçu : ${f.vendeur.rcs}`);
  }
  // IBAN luxembourgeois : LU + 2 chiffres + 3 chiffres (code banque) + 13 alphanumériques (numéro de compte) = 20 caractères au total
  if (f.vendeur?.iban && !/^LU\d{2}\d{3}[A-Z0-9]{13}$/.test(f.vendeur.iban.replace(/\s+/g, ""))) {
    errors.push(`IBAN vendeur invalide (attendu : LU + 18 caractères, ex. LU280019400644750000) — reçu : ${f.vendeur.iban}`);
  }
  // BIC obligatoire pour virement intra-UE en pratique (8 ou 11 caractères)
  if (f.vendeur?.iban && !f.vendeur.bic) {
    errors.push(`BIC vendeur manquant (recommandé pour virement SEPA, obligatoire hors EEE)`);
  }
  if (f.vendeur?.bic && !/^[A-Z]{6}[A-Z0-9]{2}([A-Z0-9]{3})?$/.test(f.vendeur.bic)) {
    errors.push(`BIC vendeur invalide (attendu : 8 ou 11 caractères) — reçu : ${f.vendeur.bic}`);
  }
  if (f.tauxTva !== undefined && !TAUX_VALIDES.includes(Number(f.tauxTva))) {
    errors.push(`Taux TVA invalide (attendu : 17, 14, 8, 3 ou 0) — reçu : ${f.tauxTva}`);
  }
  // Vérif arithmétique TVA
  if (f.totalHT && f.tauxTva !== undefined && f.montantTva !== undefined) {
    const tvaCalc = Math.round(f.totalHT * (f.tauxTva / 100) * 100) / 100;
    if (Math.abs(tvaCalc - f.montantTva) > 0.02) {
      errors.push(`Montant TVA incohérent : attendu ${tvaCalc}, reçu ${f.montantTva}`);
    }
  }
  // Vérif arithmétique TTC = HT + TVA
  if (f.totalHT !== undefined && f.montantTva !== undefined && f.totalTtc !== undefined) {
    const ttcCalc = Math.round((f.totalHT + f.montantTva) * 100) / 100;
    if (Math.abs(ttcCalc - f.totalTtc) > 0.02) {
      errors.push(`Total TTC incohérent : HT (${f.totalHT}) + TVA (${f.montantTva}) = ${ttcCalc}, reçu ${f.totalTtc}`);
    }
  }

  // B2G : si secteur public, Peppol obligatoire
  if (f.client?.secteur === "public" && !f.peppol?.participantId) {
    errors.push("Client public LU : identifiant Peppol obligatoire (e-invoicing B2G depuis 2023)");
  }

  if (errors.length === 0) {
    console.log("[OK] Facture conforme aux exigences luxembourgeoises.");
    process.exit(0);
  } else {
    console.error(`[KO] ${errors.length} problème(s) :`);
    for (const e of errors) console.error("  -", e);
    process.exit(1);
  }
}

main();

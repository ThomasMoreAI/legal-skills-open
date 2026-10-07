#!/usr/bin/env node
/**
 * generate-statements.js — Génère Bilan + Compte de Résultat + Balance
 * au format luxembourgeois (PCN — Règlement grand-ducal du 12 sept. 2019).
 *
 * Lit company.json + un journal d'écritures JSON, produit 3 fichiers
 * Markdown (bilan.md, compte-resultat.md, balance.md) dans ./out/.
 *
 * Usage : node scripts/generate-statements.js [chemin/journal.json]
 *
 * Format journal attendu : tableau d'écritures
 *   [{ date, piece, compte, libelle, debit, credit }, ...]
 *
 * Le PCN luxembourgeois suit la structure 1-7 :
 *   1 = Capitaux propres et assimilés
 *   2 = Frais d'établissement, immobilisations
 *   3 = Stocks et en-cours
 *   4 = Créances et dettes
 *   5 = Avoirs financiers
 *   6 = Charges
 *   7 = Produits
 */

import fs from "node:fs";
import path from "node:path";

const COMPANY_FILE = "company.json";
const OUT_DIR = "out";

function loadCompany() {
  if (!fs.existsSync(COMPANY_FILE)) {
    console.error(`[ERREUR] ${COMPANY_FILE} introuvable. Lancez 'cp company.example.json company.json' puis remplissez vos infos.`);
    process.exit(1);
  }
  return JSON.parse(fs.readFileSync(COMPANY_FILE, "utf8"));
}

function loadJournal(file) {
  if (!file || !fs.existsSync(file)) {
    console.error(`[ERREUR] journal introuvable. Usage : node scripts/generate-statements.js <journal.json>`);
    process.exit(1);
  }
  return JSON.parse(fs.readFileSync(file, "utf8"));
}

function fmt(n) {
  return new Intl.NumberFormat("fr-LU", {
    style: "currency",
    currency: "EUR",
    minimumFractionDigits: 2,
  }).format(n);
}

function aggregateByAccount(journal) {
  const map = new Map();
  for (const e of journal) {
    const compte = String(e.compte);
    if (!map.has(compte)) map.set(compte, { libelle: e.libelle || "", debit: 0, credit: 0 });
    const row = map.get(compte);
    row.debit += Number(e.debit || 0);
    row.credit += Number(e.credit || 0);
  }
  return map;
}

function classOf(compte) {
  return String(compte).charAt(0);
}

function buildBalance(map) {
  const lines = ["| Compte | Libellé | Débit | Crédit | Solde |", "|---|---|---:|---:|---:|"];
  let totalD = 0, totalC = 0;
  for (const [compte, row] of [...map.entries()].sort()) {
    const solde = row.debit - row.credit;
    totalD += row.debit;
    totalC += row.credit;
    lines.push(`| ${compte} | ${row.libelle} | ${fmt(row.debit)} | ${fmt(row.credit)} | ${fmt(solde)} |`);
  }
  lines.push(`| **Total** | | **${fmt(totalD)}** | **${fmt(totalC)}** | **${fmt(totalD - totalC)}** |`);
  return lines.join("\n");
}

function buildBilan(map) {
  // Convention PCN luxembourgeois :
  //   Classe 2 (immobilisations), 3 (stocks), 5 (avoirs financiers) -> Actif
  //   Classe 1 (capitaux propres + dettes financières) -> Passif
  //   Classe 4 (tiers) -> ventilé selon le SIGNE du solde :
  //     solde débiteur (>0) = créance -> Actif
  //     solde créditeur (<0) = dette  -> Passif
  let actif = 0, passif = 0;
  const actifLines = [], passifLines = [];
  for (const [compte, row] of [...map.entries()].sort()) {
    const c = classOf(compte);
    const solde = row.debit - row.credit;
    if (solde === 0) continue;
    if (c === "2" || c === "3" || c === "5") {
      actifLines.push(`| ${compte} ${row.libelle} | ${fmt(solde)} |`);
      actif += solde;
    } else if (c === "1") {
      passifLines.push(`| ${compte} ${row.libelle} | ${fmt(-solde)} |`);
      passif += -solde;
    } else if (c === "4") {
      if (solde > 0) {
        actifLines.push(`| ${compte} ${row.libelle} (créance) | ${fmt(solde)} |`);
        actif += solde;
      } else {
        passifLines.push(`| ${compte} ${row.libelle} (dette) | ${fmt(-solde)} |`);
        passif += -solde;
      }
    }
  }
  return [
    "## ACTIF", "| Poste | Montant |", "|---|---:|", ...actifLines,
    `| **Total Actif** | **${fmt(actif)}** |`,
    "", "## PASSIF", "| Poste | Montant |", "|---|---:|", ...passifLines,
    `| **Total Passif** | **${fmt(passif)}** |`,
  ].join("\n");
}

function buildCR(map) {
  let charges = 0, produits = 0;
  const chargesL = [], produitsL = [];
  for (const [compte, row] of [...map.entries()].sort()) {
    const c = classOf(compte);
    const solde = row.debit - row.credit;
    if (c === "6" && solde !== 0) {
      chargesL.push(`| ${compte} ${row.libelle} | ${fmt(solde)} |`);
      charges += solde;
    } else if (c === "7" && solde !== 0) {
      produitsL.push(`| ${compte} ${row.libelle} | ${fmt(-solde)} |`);
      produits += -solde;
    }
  }
  const resultat = produits - charges;
  return [
    "## CHARGES", "| Compte | Montant |", "|---|---:|", ...chargesL,
    `| **Total charges** | **${fmt(charges)}** |`,
    "", "## PRODUITS", "| Compte | Montant |", "|---|---:|", ...produitsL,
    `| **Total produits** | **${fmt(produits)}** |`,
    "", `## RÉSULTAT DE L'EXERCICE : **${fmt(resultat)}** ${resultat >= 0 ? "(bénéfice)" : "(perte)"}`,
  ].join("\n");
}

function main() {
  const journalFile = process.argv[2] || "journal.json";
  const company = loadCompany();
  const journal = loadJournal(journalFile);
  const map = aggregateByAccount(journal);

  fs.mkdirSync(OUT_DIR, { recursive: true });
  const header = `# ${company.raisonSociale || "Société"} — Exercice ${company.exercice || ""}\n\n_Généré par paperasse-lux. Format PCN (Règlement grand-ducal du 12 sept. 2019)._\n\n`;

  fs.writeFileSync(path.join(OUT_DIR, "balance.md"), header + "## Balance générale\n\n" + buildBalance(map));
  fs.writeFileSync(path.join(OUT_DIR, "bilan.md"), header + "# Bilan\n\n" + buildBilan(map));
  fs.writeFileSync(path.join(OUT_DIR, "compte-resultat.md"), header + "# Compte de Résultat\n\n" + buildCR(map));

  console.log(`[OK] Balance, Bilan et Compte de Résultat générés dans ${OUT_DIR}/`);
}

main();

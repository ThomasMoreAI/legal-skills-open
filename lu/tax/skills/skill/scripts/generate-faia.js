#!/usr/bin/env node
/**
 * generate-faia.js — CLI : génère un Fichier d'Audit Informatisé (FAIA) AED.
 *
 * Format : SAF-T LU 2.01 (Standard Audit File for Tax, profil luxembourgeois).
 * Le FAIA est exigible par l'Administration de l'Enregistrement, des Domaines
 * et de la TVA (AED) lors de tout contrôle TVA depuis le 1er janvier 2011.
 *
 * Usage :
 *   node scripts/generate-faia.js <input.json> > faia.xml
 *   node scripts/generate-faia.js <input.json> --validate-only
 *   node scripts/generate-faia.js <company.json> <transactions.json> > faia.xml   (legacy)
 *
 * Le format <input.json> est documenté dans examples/faia-input.json.
 */

import { readFileSync } from 'node:fs';
import { genererFAIA } from '../lib/faia/index.js';

const args = process.argv.slice(2);
if (args.length === 0 || args.includes('--help') || args.includes('-h')) {
  console.error(`Usage : paperasse faia <input.json> [--validate-only]
       paperasse faia <company.json> <transactions.json>   (legacy)

Le fichier <input.json> contient :
  { company, period, accounts, customers, suppliers, entries,
    salesInvoices?, purchaseInvoices?, payments? }

Voir examples/faia-input.json pour un modèle complet.`);
  process.exit(args.length === 0 ? 1 : 0);
}

const validateOnly = args.includes('--validate-only');
const positional = args.filter((a) => !a.startsWith('--'));

let input;
if (positional.length === 1) {
  input = JSON.parse(readFileSync(positional[0], 'utf8'));
} else if (positional.length === 2) {
  // Mode legacy : 2 fichiers séparés (company + transactions)
  const company = JSON.parse(readFileSync(positional[0], 'utf8'));
  const tx = JSON.parse(readFileSync(positional[1], 'utf8'));
  input = { company, ...tx };
}

try {
  const { xml, totals, validation } = genererFAIA(input, { skipValidation: validateOnly });
  if (validation.avertissements.length) {
    for (const a of validation.avertissements) console.error(`⚠  ${a}`);
  }
  if (validateOnly) {
    console.error(`Validation : ${validation.valide ? 'OK' : 'KO'}`);
    if (!validation.valide) {
      for (const e of validation.erreurs) console.error(`  - ${e}`);
      process.exit(1);
    }
    console.error(`Totaux : ${totals.entryCount} écritures, débit ${totals.debit.toFixed(2)} = crédit ${totals.credit.toFixed(2)}`);
    process.exit(0);
  }
  process.stdout.write(xml + '\n');
  console.error(`✓ FAIA généré : ${totals.entryCount} écritures, ${totals.salesCount} ventes, ${totals.purchaseCount} achats`);
} catch (e) {
  console.error(`✗ ${e.message}`);
  if (e.validation) {
    for (const err of e.validation.erreurs) console.error(`  - ${err}`);
  }
  process.exit(1);
}

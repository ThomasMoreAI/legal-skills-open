#!/usr/bin/env node
/**
 * parse-bank-statement.js — CLI pour parser un relevé bancaire LU.
 *
 * Auto-détecte le format (BCEE / POST / BIL / CAMT.053 / CSV générique).
 *
 * Usage :
 *   node scripts/parse-bank-statement.js <fichier.csv|.xml> [--format=json|table|csv]
 *
 * Sortie par défaut : JSON sur stdout. Idéal pour pipe vers jq ou import comptable.
 */

import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { parseBankStatement, aggregate } from '../lib/bank-parsers/index.js';

const isCli = process.argv[1] === fileURLToPath(import.meta.url);
if (!isCli) { process.exit(0); }

const args = process.argv.slice(2);
const file = args.find(a => !a.startsWith('--'));
const formatArg = (args.find(a => a.startsWith('--format=')) || '--format=json').split('=')[1];

if (!file) {
  console.log(`Usage : node scripts/parse-bank-statement.js <fichier> [--format=json|table|csv]

Auto-détecte BCEE / POST / BIL / CAMT.053 / CSV générique.

Exemples :
  node scripts/parse-bank-statement.js examples/bank-statements/bcee-sample.csv
  node scripts/parse-bank-statement.js releve.xml --format=table
  node scripts/parse-bank-statement.js export.csv --format=csv > normalized.csv
`);
  process.exit(1);
}

const text = readFileSync(file, 'utf8');
const result = parseBankStatement(text);
const totals = aggregate(result.transactions);

if (formatArg === 'json') {
  console.log(JSON.stringify({ ...result, totals }, null, 2));
} else if (formatArg === 'csv') {
  console.log('date;date_valeur;libelle;montant;devise;solde;reference;banque');
  for (const t of result.transactions) {
    const escape = (v) => v == null ? '' : String(v).includes(';') ? `"${v.replace(/"/g, '""')}"` : v;
    console.log([t.date, t.date_valeur, t.libelle, t.montant, t.devise, t.solde, t.reference, t.banque].map(escape).join(';'));
  }
} else if (formatArg === 'table') {
  console.log(`Format détecté : ${result.format} (confiance : ${result.confiance || 'n/a'})`);
  console.log(`Transactions : ${result.count}\n`);
  console.log('Date        Sens   Montant      Devise  Libellé');
  console.log('-'.repeat(80));
  for (const t of result.transactions.slice(0, 50)) {
    const m = (t.montant != null ? t.montant.toFixed(2) : '?').padStart(12);
    console.log(`${(t.date || '?').padEnd(11)} ${(t.sens || '?').padEnd(6)} ${m}  ${(t.devise || '?').padEnd(6)} ${(t.libelle || '').slice(0, 40)}`);
  }
  if (result.transactions.length > 50) console.log(`... (${result.transactions.length - 50} de plus)`);
  console.log('-'.repeat(80));
  console.log(`Crédits : ${totals.total_credits.toFixed(2)} € · Débits : ${totals.total_debits.toFixed(2)} € · Net : ${totals.flux_net.toFixed(2)} €`);
} else {
  console.error(`Format inconnu : ${formatArg} (json|table|csv attendus)`);
  process.exit(1);
}

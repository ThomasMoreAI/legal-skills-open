#!/usr/bin/env node
/**
 * generate-ecdf.js — CLI de génération du fichier eCDF CA-A.
 *
 * Lit un JSON d'entrée (société + exercice + balance PCN) et produit :
 *   - le document XML eCDF sur stdout (ou fichier --out)
 *   - un résumé de cohérence sur stderr
 *
 * Usage :
 *   node scripts/generate-ecdf.js examples/ecdf-input.json
 *   node scripts/generate-ecdf.js examples/ecdf-input.json --out=comptes-2025.xml
 *   node scripts/generate-ecdf.js examples/ecdf-input.json --json   # debug structure
 */

import { readFileSync, writeFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { generateECDF, buildECDFData } from '../lib/ecdf/generator.js';

const isCli = process.argv[1] === fileURLToPath(import.meta.url);
if (!isCli) process.exit(0);

const args = process.argv.slice(2);
const file = args.find(a => !a.startsWith('--'));
const outArg = args.find(a => a.startsWith('--out='));
const wantJson = args.includes('--json');

if (!file) {
  console.log(`Usage : node scripts/generate-ecdf.js <input.json> [--out=fichier.xml] [--json]

L'input.json doit contenir :
  {
    "societe":  { "rcs": "B12345", "tva": "LU...", "denomination": "...", "forme": "SARL" },
    "exercice": { "debut": "2025-01-01", "fin": "2025-12-31", "devise": "EUR" },
    "balance":  { "101": -10000, "20": 500, "21": 30000, ... }
  }

Voir examples/ecdf-input.json pour un exemple complet.

ATTENTION : à valider sur https://ecdf.b2g.etat.lu/ avant tout dépôt légal.
`);
  process.exit(1);
}

const input = JSON.parse(readFileSync(file, 'utf8'));

if (wantJson) {
  console.log(JSON.stringify(buildECDFData(input), null, 2));
  process.exit(0);
}

const xml = generateECDF(input);
const data = buildECDFData(input);

if (outArg) {
  const out = outArg.split('=')[1];
  writeFileSync(out, xml, 'utf8');
  console.error(`✓ Fichier eCDF écrit : ${out}`);
} else {
  process.stdout.write(xml);
}

// Résumé de cohérence sur stderr (n'interfère pas avec un >redirection)
console.error(`\n=== Résumé eCDF CA-A ===`);
console.error(`Société     : ${input.societe.denomination} (${input.societe.rcs})`);
console.error(`Exercice    : ${input.exercice.debut} → ${input.exercice.fin}`);
console.error(`Total actif : ${data.bilan.total_actif.toFixed(2)} ${input.exercice.devise || 'EUR'}`);
console.error(`Total passif: ${data.bilan.total_passif.toFixed(2)} ${input.exercice.devise || 'EUR'}`);
console.error(`Résultat    : ${data.resultat_calcule.toFixed(2)} ${input.exercice.devise || 'EUR'} ${data.resultat_calcule >= 0 ? '(bénéfice)' : '(perte)'}`);
console.error(`Cohérence   : ${data.coherence.remarque}`);
if (!data.coherence.bilan_equilibre) process.exit(2);

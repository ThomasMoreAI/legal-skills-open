#!/usr/bin/env node
/**
 * de.js — CLI pour rendre les templates allemands avec un contexte JSON.
 *
 * Usage :
 *   paperasse de <nom-template> <input.json> [--out=fichier.md]
 *   paperasse de --list
 */

import { readFileSync, writeFileSync, readdirSync } from 'node:fs';
import { dirname, join, basename } from 'node:path';
import { fileURLToPath } from 'node:url';
import { renderTemplate } from '../lib/templates-de/render.js';

const __dirname = dirname(fileURLToPath(import.meta.url));
const TPL_DIR = join(__dirname, '..', 'templates', 'de');

const isCli = process.argv[1] === fileURLToPath(import.meta.url);
if (!isCli) process.exit(0);

const args = process.argv.slice(2);
const wantList = args.includes('--list');
const outArg = args.find(a => a.startsWith('--out='));
const positional = args.filter(a => !a.startsWith('--'));

if (wantList) {
  const files = readdirSync(TPL_DIR).filter(f => f.endsWith('.md') && f !== 'README.md');
  console.log('Templates allemands disponibles :\n');
  for (const f of files) console.log(`  ${basename(f, '.md')}`);
  console.log('\nUsage : paperasse de <nom> <input.json> [--out=fichier.md]');
  process.exit(0);
}

const [tplName, jsonFile] = positional;
if (!tplName || !jsonFile) {
  console.log(`Usage : paperasse de <nom-template> <input.json> [--out=fichier.md]
       paperasse de --list

Exemple :
  paperasse de mahnung examples/de/mahnung-input.json --out=mahnung-001.md
`);
  process.exit(1);
}

const tplPath = join(TPL_DIR, tplName + '.md');
let tpl;
try { tpl = readFileSync(tplPath, 'utf8'); }
catch { console.error(`Template introuvable : ${tplName} (cherché à ${tplPath})`); process.exit(1); }

const ctx = JSON.parse(readFileSync(jsonFile, 'utf8'));
const rendered = renderTemplate(tpl, ctx);

if (outArg) {
  const out = outArg.split('=')[1];
  writeFileSync(out, rendered, 'utf8');
  console.error(`✓ Document rendu : ${out}`);
} else {
  process.stdout.write(rendered);
}

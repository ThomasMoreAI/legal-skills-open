#!/usr/bin/env node
/**
 * check-data-freshness.js — Détecte les fichiers data/*.json obsolètes.
 *
 * Les chiffres luxembourgeois (taux IRC, ICC, IF, barème IRPP, abattements...)
 * changent généralement chaque année via la loi budgétaire votée fin décembre,
 * publiée au Mémorial A et applicable au 1er janvier suivant.
 *
 * Ce script lit le champ `as_of` de chaque data/*.json et signale ceux qui
 * datent d'une année antérieure à l'année en cours, pour rappeler la revue
 * annuelle obligatoire.
 *
 * Usage : node scripts/check-data-freshness.js
 * Exit 0 si tout est à jour, 1 sinon (utilisable en CI annuelle).
 */

import { readFileSync, readdirSync, statSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const ROOT = join(__dirname, '..');
const ANNEE_COURANTE = new Date().getFullYear();

function findDataFiles(dir, out = []) {
  for (const name of readdirSync(dir)) {
    const full = join(dir, name);
    const st = statSync(full);
    if (st.isDirectory() && !['node_modules', '.git', 'data-sources', 'schemas'].includes(name)) {
      findDataFiles(full, out);
    } else if (st.isFile() && name.endsWith('.json') && full.includes(`/data/`)) {
      out.push(full);
    }
  }
  return out;
}

const files = findDataFiles(ROOT);
let obsoletes = 0;
let frais = 0;
let inconnus = 0;

console.log(`Vérification de fraîcheur des chiffres (année courante : ${ANNEE_COURANTE})\n`);
console.log(`${'Fichier'.padEnd(60)} ${'as_of'.padEnd(12)} État`);
console.log('-'.repeat(85));

for (const f of files) {
  const rel = f.replace(ROOT + '/', '');
  let asOf, etat, marker;
  try {
    const data = JSON.parse(readFileSync(f, 'utf8'));
    asOf = data.as_of;
    if (!asOf) {
      etat = 'as_of manquant';
      marker = '?';
      inconnus++;
    } else {
      const annee = parseInt(asOf.slice(0, 4), 10);
      if (annee >= ANNEE_COURANTE) {
        etat = 'à jour';
        marker = '✓';
        frais++;
      } else if (annee === ANNEE_COURANTE - 1) {
        etat = `à revoir (loi budgétaire ${ANNEE_COURANTE} probablement publiée)`;
        marker = '⚠';
        obsoletes++;
      } else {
        etat = `OBSOLÈTE (${ANNEE_COURANTE - annee} an(s) de retard)`;
        marker = '✗';
        obsoletes++;
      }
    }
  } catch (e) {
    etat = `lecture impossible : ${e.message}`;
    marker = '✗';
    asOf = '—';
    inconnus++;
  }
  console.log(`${marker} ${rel.padEnd(58)} ${(asOf || '—').padEnd(12)} ${etat}`);
}

console.log('-'.repeat(85));
console.log(`\n${frais} à jour · ${obsoletes} à revoir · ${inconnus} indéterminé(s)\n`);

if (obsoletes > 0) {
  console.log('PROCHAINES ÉTAPES :');
  console.log('  1. Consulter le Mémorial A de décembre dernier sur https://legilux.public.lu');
  console.log('  2. Récupérer les nouveaux chiffres officiels :');
  console.log('     - ACD pour IRC/ICC/IF/IRPP : https://impotsdirects.public.lu');
  console.log('     - AED pour TVA et enregistrement : https://pfi.public.lu');
  console.log('  3. Mettre à jour les fichiers data/*.json concernés et leur champ "as_of"');
  console.log('  4. Lancer `npm run validate:data` puis `npm test` avant commit');
}

process.exit(obsoletes > 0 ? 1 : 0);

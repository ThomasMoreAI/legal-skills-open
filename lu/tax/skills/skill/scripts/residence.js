#!/usr/bin/env node
/**
 * residence.js — CLI du parcours d'installation (Milestone 7).
 *
 * Sous-commande :
 *   paperasse residence installation --nationalite FR --arrivee 2026-03-01 [--vehicule]
 *   paperasse residence installation --json '{"nationalite":"US","dateArriveeLux":"2026-03-01"}'
 *
 * Lecture seule.
 */

import { parcoursInstallation, PHASES_INSTALLATION } from '../lib/residence/index.js';

function arg(nom) { const i = process.argv.indexOf(nom); return i !== -1 ? process.argv[i + 1] : undefined; }
const has = (nom) => process.argv.includes(nom);
const sous = process.argv[2];

if (sous !== 'installation') {
  console.log(`Usage :
  paperasse residence installation --nationalite FR --arrivee 2026-03-01 [--vehicule]
  paperasse residence installation --json '{"nationalite":"US","dateArriveeLux":"2026-03-01"}'`);
  process.exit(sous ? 1 : 0);
}

const profil = arg('--json')
  ? JSON.parse(arg('--json'))
  : { nationalite: arg('--nationalite'), dateArriveeLux: arg('--arrivee'), vehicules: has('--vehicule') ? ['véhicule'] : [] };

const p = parcoursInstallation(profil);
console.log(`\nJe m'installe au Luxembourg — nationalité : ${p.classeNationalite}\n`);
if (p.avertissement) console.log(`⚠ ${p.avertissement}\n`);

for (const phase of PHASES_INSTALLATION) {
  const bloc = p.parPhase[phase];
  if (!bloc) continue;
  console.log(`=== ${bloc.libelle} ===`);
  for (const e of bloc.etapes) {
    console.log(`  • ${e.titre}${e.echeanceIndicative ? `  ⏱ ~${e.echeanceIndicative}` : ''}${e.aPreciser ? '  (à préciser selon nationalité)' : ''}`);
    if (e.description) console.log(`    ${e.description}`);
    if (e.administration && e.administration !== '—') console.log(`    Autorité : ${e.administration}`);
    if (e.delai) console.log(`    Délai : ${e.delai}`);
    console.log(`    Source : ${e.source}`);
  }
  console.log('');
}

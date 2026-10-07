#!/usr/bin/env node
/**
 * plan.js — CLI du moteur de planification multi-événements.
 *
 * Sous-commandes :
 *   paperasse plan <ev1> <ev2> ...                 (ex : arrivee_luxembourg naissance creation_entreprise)
 *   paperasse plan --extraction extraction.json    (sortie structurée d'un LLM : {events, entities, confidence})
 *
 * Fusionne les démarches, détecte les documents mutualisés, ordonne selon les
 * dépendances et explique. N'effectue aucune démarche.
 */

import { readFileSync } from 'node:fs';
import { ingererExtraction } from '../lib/extraction/index.js';
import { planifier } from '../lib/planification/index.js';
import { ceJourISO } from '../lib/diagnostic/index.js';

function arg(nom) { const i = process.argv.indexOf(nom); return i !== -1 ? process.argv[i + 1] : undefined; }
const aujourdhui = arg('--date') || ceJourISO();

let evenements;
let profil = {};
if (arg('--extraction')) {
  const res = ingererExtraction(JSON.parse(readFileSync(arg('--extraction'), 'utf8')));
  evenements = res.evenements;
  profil = res.profil;
  console.log(`Extraction ingérée — événements : ${evenements.join(', ') || '—'}${res.aValider ? ' (⚠ confiance faible)' : ''}`);
  if (res.avertissement) console.log(`⚠ ${res.avertissement}`);
} else {
  // Positionnels = arguments qui ne sont ni une option (--x) ni la valeur d'une option.
  const valeursOptions = new Set([arg('--date'), arg('--extraction')].filter(Boolean));
  const argv = process.argv.slice(2);
  evenements = argv.filter((a) => !a.startsWith('--') && !valeursOptions.has(a));
}

if (!evenements || !evenements.length) {
  console.log(`Usage :
  paperasse plan <ev1> <ev2> ...            (ex : arrivee_luxembourg naissance creation_entreprise)
  paperasse plan --extraction fichier.json  (sortie LLM : {"events":[...],"entities":{...},"confidence":0.9})
  Événements : voir « paperasse evenement liste ».`);
  process.exit(evenements ? 1 : 0);
}

const plan = planifier(evenements, { profil, aujourdhui });

console.log(`\n📋 ${plan.resume}\n`);
console.log('Ordre recommandé :');
for (const d of plan.demarches) {
  console.log(`  ${d.ordre}. ${d.nom}${d.echeance ? `  ⏱ ${d.echeance}` : ''}`);
  console.log(`     ${d.explication}`);
  if (d.source) console.log(`     Source : ${d.source}`);
}
if (plan.documentsMutualises.length) {
  console.log('\nDocuments mutualisés (à préparer une seule fois) :');
  for (const m of plan.documentsMutualises) console.log(`  • ${m.document} — utilisé par ${m.count} événement(s) : ${m.evenements.join(', ')}`);
}
console.log(`\n⚠ ${plan.note}`);

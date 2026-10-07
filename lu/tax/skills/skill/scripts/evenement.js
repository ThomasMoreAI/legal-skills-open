#!/usr/bin/env node
/**
 * evenement.js — CLI de l'ontologie des événements de vie.
 *
 * Sous-commandes :
 *   paperasse evenement liste
 *   paperasse evenement <id-ou-texte>        (ex : naissance, "j'ai perdu mon emploi")
 *
 * Affiche la chaîne : conséquences → administrations → obligations → documents
 * → délais → exceptions → checklist. Aucune démarche n'est effectuée.
 */

import { listerEvenements, resoudreEvenement } from '../lib/evenements/index.js';
import { ceJourISO } from '../lib/diagnostic/index.js';

function arg(nom) { const i = process.argv.indexOf(nom); return i !== -1 ? process.argv[i + 1] : undefined; }
const aujourdhui = arg('--date') || ceJourISO();
const sous = process.argv.slice(2).filter((a) => !a.startsWith('--'));

if (!sous.length) {
  console.log('Usage :\n  paperasse evenement liste\n  paperasse evenement <id-ou-texte>   (ex : naissance, "j\'ai perdu mon emploi")');
  process.exit(1);
}

if (sous[0] === 'liste') {
  console.log('Événements de vie couverts :');
  for (const e of listerEvenements()) console.log(`  • ${e.id} — ${e.nom}`);
  process.exit(0);
}

const c = resoudreEvenement(sous.join(' '), { aujourdhui });
console.log(`\n🔵 ${c.evenement.nom}\n`);
console.log('Conséquences :');
for (const x of c.consequences) console.log(`  → ${x}`);
console.log('\nAdministrations concernées :');
for (const a of c.administrations) console.log(`  • ${a.nom}`);
console.log('\nObligations (reliées au catalogue) :');
for (const o of c.obligations) console.log(`  • ${o.nom || o.id}${o.echeance ? `  ⏱ ${o.echeance}` : ''}${o.source ? `\n    Source : ${o.source}` : ''}`);
for (const o of c.obligationsHorsCatalogue) console.log(`  • ${o.nom}\n    Source : ${o.source}`);
console.log('\nDocuments à réunir :');
for (const d of c.documents) console.log(`  ☐ ${d}`);
console.log('\nDélais :');
for (const d of c.delais) console.log(`  • ${d.quoi} : ${d.delai}`);
if (c.exceptions.length) { console.log('\nExceptions / cas particuliers :'); for (const x of c.exceptions) console.log(`  ⚠ ${x}`); }
console.log('\nChecklist :');
for (const x of c.checklist) console.log(`  ☐ ${x}`);
console.log(`\nSource : ${c.source}`);
console.log('\nJe n\'ai effectué aucune démarche : cette chaîne vous aide à préparer et à agir.');

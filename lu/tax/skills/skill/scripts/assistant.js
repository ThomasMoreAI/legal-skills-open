#!/usr/bin/env node
/**
 * assistant.js — CLI de l'assistant conversationnel (Milestone 14).
 *
 * Usage :
 *   paperasse assistant "J'ai reçu une lettre de l'AED, que faire ?" [--profil '{...}'] [--doc courrier.txt]
 *
 * L'assistant identifie l'intention, consulte le profil, remonte les
 * obligations sourcées, demande les informations manquantes et propose une
 * action — sans jamais effectuer de démarche.
 */

import { readFileSync } from 'node:fs';
import { repondre } from '../lib/conversation/index.js';

function arg(nom) { const i = process.argv.indexOf(nom); return i !== -1 ? process.argv[i + 1] : undefined; }
const texte = process.argv.slice(2).find((a) => !a.startsWith('--') && a !== arg('--profil') && a !== arg('--doc'));

if (!texte) {
  console.log('Usage : paperasse assistant "votre question" [--profil \'{...}\'] [--doc courrier.txt]');
  process.exit(1);
}

const contexte = {
  profil: arg('--profil') ? JSON.parse(arg('--profil')) : {},
  texteDocument: arg('--doc') ? readFileSync(arg('--doc'), 'utf8') : undefined,
};

const r = repondre(texte, contexte);

console.log(`\nIntention : ${r.intention}`);
if (r.evenementVie) {
  console.log(`\n🔵 Événement de vie détecté : ${r.evenementVie.nom}`);
  console.log(`   Administrations : ${r.evenementVie.administrations.join(', ')}`);
}
if (r.comprehension) console.log(`\nCe que je comprends : ${r.comprehension}`);
if (r.avertissement) console.log(`\n⚠ ${r.avertissement}`);
if (r.obligations.length) {
  console.log('\nObligations applicables :');
  for (const o of r.obligations) console.log(`  • ${o.nom}${o.echeance ? `  ⏱ ${o.echeance}` : ''}${o.administration ? ` — ${o.administration}` : ''}`);
}
if (r.checklist.length) {
  console.log('\nChecklist :');
  for (const c of r.checklist.slice(0, 12)) console.log(`  ☐ ${c}`);
}
if (r.prochaineQuestion) console.log(`\nPour préciser : ${r.prochaineQuestion}`);
if (r.action) console.log(`\nAction proposée : ${r.action}`);
if (r.sources.length) {
  console.log('\nSources :');
  for (const s of [...new Set(r.sources)].slice(0, 8)) console.log(`  - ${s}`);
}
console.log(`\n${r.disclaimer}`);

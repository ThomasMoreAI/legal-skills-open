#!/usr/bin/env node
/**
 * test-i18n.js — Tests Milestone 13 : internationalisation.
 */

import { LANGUES, DICT, traduire, traducteur, libelles, normaliserLangue } from '../lib/i18n/index.js';

let passed = 0, failed = 0;
function test(name, fn) {
  try { fn(); console.log(`  ✓ ${name}`); passed++; }
  catch (e) { console.log(`  ✗ ${name}\n      ${e.message}`); failed++; }
}
function eq(a, b, msg) { if (a !== b) throw new Error(`${msg || ''}: attendu ${JSON.stringify(b)}, reçu ${JSON.stringify(a)}`); }
function truthy(v, msg) { if (!v) throw new Error(msg || 'attendu truthy'); }

console.log('=== Couverture des traductions ===');

test('chaque clé de chaque domaine couvre les 4 langues', () => {
  for (const [domaine, cles] of Object.entries(DICT)) {
    for (const [cle, trads] of Object.entries(cles)) {
      for (const langue of LANGUES) truthy(trads[langue], `manque ${domaine}.${cle}.${langue}`);
    }
  }
});

console.log('=== traduire ===');

test('traduit dans la langue demandée', () => {
  eq(traduire('colonnes', 'obligatoire_maintenant', 'en'), 'Required now');
  eq(traduire('statuts', 'en_retard', 'de'), 'Überfällig');
  eq(traduire('navigation', 'documents', 'lb'), 'Meng Dokumenter');
});

test('repli sur le français si langue inconnue', () => {
  eq(traduire('colonnes', 'a_surveiller', 'es'), traduire('colonnes', 'a_surveiller', 'fr'));
});

test('repli sur la clé brute si inconnue', () => {
  eq(traduire('colonnes', 'inexistant', 'fr'), 'inexistant');
});

test('normaliserLangue replie sur fr', () => {
  eq(normaliserLangue('xx'), 'fr');
  eq(normaliserLangue('de'), 'de');
});

console.log('=== traducteur & libelles ===');

test('traducteur lié à une langue', () => {
  const t = traducteur('en');
  eq(t('couleurs', 'rouge'), 'Overdue');
});

test('libelles renvoie tout un menu localisé', () => {
  const nav = libelles('navigation', 'de');
  eq(nav.tableau_de_bord, 'Übersicht');
  truthy(Object.keys(nav).length >= 9);
});

console.log(`\n${passed} tests réussis, ${failed} échoués.`);
process.exit(failed === 0 ? 0 : 1);

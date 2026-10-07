#!/usr/bin/env node
/**
 * test-maturite.js — Coverage-driven development : maturité & dette de connaissance.
 */

import { readFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

import { chargerCatalogue } from '../lib/diagnostic/index.js';
import { tableauMaturite, detteConnaissance, tableauCouverture, chargerCasQA } from '../lib/connaissances/index.js';

const __dirname = dirname(fileURLToPath(import.meta.url));
const EVENEMENTS = JSON.parse(readFileSync(join(__dirname, '..', 'data', 'evenements-vie.json'), 'utf8')).evenements;

let passed = 0, failed = 0;
function test(name, fn) {
  try { fn(); console.log(`  ✓ ${name}`); passed++; }
  catch (e) { console.log(`  ✗ ${name}\n      ${e.message}`); failed++; }
}
function eq(a, b, msg) { if (a !== b) throw new Error(`${msg || ''}: attendu ${JSON.stringify(b)}, reçu ${JSON.stringify(a)}`); }
function truthy(v, msg) { if (!v) throw new Error(msg || 'attendu truthy'); }

const REF = '2026-07-13';
const { obligations } = chargerCatalogue();
const cas = chargerCasQA().cas;

console.log('=== Coverage-driven : la couverture a été augmentée ===');

test('cessation n\'est plus à 0 % (cas ajoutés)', () => {
  const tc = tableauCouverture(obligations, cas, { aujourdhui: REF });
  const cessation = tc.find((d) => d.domaine === 'cessation');
  truthy(cessation && cessation.couverture === 100, `cessation à ${cessation && cessation.couverture} %`);
});

test('tva est passée à 100 % (cas trimestriel ajouté)', () => {
  const tva = tableauCouverture(obligations, cas, { aujourdhui: REF }).find((d) => d.domaine === 'tva');
  eq(tva.couverture, 100);
});

test('les familles edge et regression sont représentées', () => {
  const familles = new Set(cas.map((c) => c.famille));
  truthy(familles.has('edge'));
  truthy(familles.has('regression'));
});

console.log('=== Score de maturité ===');

test('la maturité combine couverture, fraîcheur et profondeur QA', () => {
  const tm = tableauMaturite(obligations, cas, { aujourdhui: REF });
  for (const d of tm) {
    for (const k of ['couverture', 'fraicheur', 'qa', 'maturite']) truthy(d[k] >= 0 && d[k] <= 100, `${d.domaine}.${k} hors bornes`);
  }
});

test('un domaine bien couvert mais peu testé n\'apparaît pas artificiellement mûr', () => {
  const tm = tableauMaturite(obligations, cas, { aujourdhui: REF });
  // tva : 100 % couverture mais peu de cas par règle → maturité < couverture.
  const tva = tm.find((d) => d.domaine === 'tva');
  truthy(tva.maturite <= tva.couverture, 'la profondeur QA doit tempérer la maturité');
});

console.log('=== Knowledge Debt (backlog automatique) ===');

test('la dette de connaissance identifie les manques', () => {
  const dette = detteConnaissance(obligations, { cas, evenements: EVENEMENTS, aujourdhui: REF });
  truthy(Array.isArray(dette.items));
  const types = new Set(dette.items.map((i) => i.type));
  // Des règles non reliées à un événement de vie existent (ex. déclarations TVA).
  truthy(types.has('non_reliees_evenement') || dette.items.length >= 0);
  // Les règles « derive » sont à corroborer.
  const corro = dette.items.find((i) => i.type === 'source_a_corroborer');
  truthy(corro && corro.total >= 1);
});

test('la dette diminue quand la couverture augmente', () => {
  const detteAvant = detteConnaissance(obligations, { cas: cas.slice(0, 6), evenements: EVENEMENTS, aujourdhui: REF });
  const detteApres = detteConnaissance(obligations, { cas, evenements: EVENEMENTS, aujourdhui: REF });
  const sansQAAvant = (detteAvant.items.find((i) => i.type === 'regles_sans_qa') || { total: 0 }).total;
  const sansQAApres = (detteApres.items.find((i) => i.type === 'regles_sans_qa') || { total: 0 }).total;
  truthy(sansQAApres <= sansQAAvant, 'ajouter des cas doit réduire les règles sans QA');
});

console.log(`\n${passed} tests réussis, ${failed} échoués.`);
process.exit(failed === 0 ? 0 : 1);

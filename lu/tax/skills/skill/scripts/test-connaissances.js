#!/usr/bin/env node
/**
 * test-connaissances.js — Tests Milestone 11 : base de connaissances officielle.
 */

import {
  chargerSources, hotesConnus, baseConnaissances, rechercher,
  reglesARevalider, citer, verifierSourcesConnues, rapport,
} from '../lib/connaissances/index.js';

let passed = 0, failed = 0;
function test(name, fn) {
  try { fn(); console.log(`  ✓ ${name}`); passed++; }
  catch (e) { console.log(`  ✗ ${name}\n      ${e.message}`); failed++; }
}
function eq(a, b, msg) { if (a !== b) throw new Error(`${msg || ''}: attendu ${JSON.stringify(b)}, reçu ${JSON.stringify(a)}`); }
function truthy(v, msg) { if (!v) throw new Error(msg || 'attendu truthy'); }

const REF = '2026-07-13';

console.log('=== Registre des sources ===');

test('le registre inclut les administrations prioritaires', () => {
  const ids = chargerSources().sources.map((s) => s.id);
  for (const id of ['guichet', 'aed', 'impotsdirects', 'ccss', 'cns', 'itm', 'zukunftskeess', 'snca', 'immigration', 'legilux']) {
    truthy(ids.includes(id), `source manquante : ${id}`);
  }
});

test('les hôtes connus sont extraits', () => {
  truthy(hotesConnus().has('guichet.public.lu'));
});

console.log('=== Base de connaissances ===');

test('chaque entrée possède une source (règle stricte)', () => {
  const base = baseConnaissances({ aujourdhui: REF });
  truthy(base.length >= 10);
  for (const e of base) truthy(e.source, `entrée ${e.id} sans source`);
});

test('la base agrège obligations et étapes d\'installation', () => {
  const base = baseConnaissances({ aujourdhui: REF });
  truthy(base.some((e) => e.origine === 'obligation'));
  truthy(base.some((e) => e.origine === 'installation'));
});

test('recherche plein-texte', () => {
  const r = rechercher('TVA', { aujourdhui: REF });
  truthy(r.length >= 1);
  truthy(r.every((e) => /tva/i.test(e.titre + e.categorie + e.id)));
});

console.log('=== Fraîcheur & citation ===');

test('récemment vérifiée (28 jours) → pas à revérifier', () => {
  const base = baseConnaissances({ aujourdhui: REF });
  const tva = base.find((e) => e.id === 'obl_tva_declaration_mensuelle');
  eq(tva.fraicheur.aRevalider, false);
});

test('seuil de fraîcheur court → règles à revérifier avec message', () => {
  const r = reglesARevalider({ aujourdhui: REF, seuilJours: 10 });
  truthy(r.length >= 1);
  truthy(/revérifiée avant utilisation/i.test(r[0].fraicheur.message));
});

test('citer renvoie la source ; règle inconnue → erreur', () => {
  const c = citer('obl_tva_declaration_mensuelle', { aujourdhui: REF });
  truthy(/Source :/.test(c.citation));
  truthy(c.source);
  let ok = false; try { citer('inexistant', { aujourdhui: REF }); } catch { ok = true; }
  truthy(ok);
});

test('la citation d\'une règle périmée porte l\'avertissement', () => {
  const c = citer('obl_tva_declaration_mensuelle', { aujourdhui: REF, seuilJours: 5 });
  truthy(/revérifiée avant utilisation/i.test(c.citation));
});

console.log('=== Cohérence des sources ===');

test('toutes les sources d\'obligations appartiennent au registre officiel', () => {
  const inconnues = verifierSourcesConnues({ aujourdhui: REF });
  eq(inconnues.length, 0, JSON.stringify(inconnues));
});

test('le rapport résume total, niveaux et à-revérifier', () => {
  const r = rapport({ aujourdhui: REF });
  truthy(r.total >= 10);
  eq(r.sansSource, 0);
  truthy(typeof r.aRevalider === 'number');
});

console.log(`\n${passed} tests réussis, ${failed} échoués.`);
process.exit(failed === 0 ? 0 : 1);

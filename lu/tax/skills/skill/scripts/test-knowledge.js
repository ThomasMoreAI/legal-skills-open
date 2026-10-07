#!/usr/bin/env node
/**
 * test-knowledge.js — Knowledge QA (cas métier de référence) + versioning
 * réglementaire. Une suite de non-régression de la connaissance.
 */

import { readFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

import { chargerCatalogue, diagnostiquer, creerProfilSociete, creerProfilUtilisateur } from '../lib/diagnostic/index.js';
import { planifier } from '../lib/planification/index.js';
import { enVigueurLe, catalogueEnVigueur, chargerGlossaire, expliquer } from '../lib/connaissances/index.js';

const __dirname = dirname(fileURLToPath(import.meta.url));
const CAS = JSON.parse(readFileSync(join(__dirname, '..', 'knowledge', 'qa', 'cas-reference.json'), 'utf8'));

let passed = 0, failed = 0;
function test(name, fn) {
  try { fn(); console.log(`  ✓ ${name}`); passed++; }
  catch (e) { console.log(`  ✗ ${name}\n      ${e.message}`); failed++; }
}
function eq(a, b, msg) { if (a !== b) throw new Error(`${msg || ''}: attendu ${JSON.stringify(b)}, reçu ${JSON.stringify(a)}`); }
function truthy(v, msg) { if (!v) throw new Error(msg || 'attendu truthy'); }

const REF = CAS.dateReference;
const { obligations } = chargerCatalogue();

console.log('=== Knowledge QA — cas métier de référence ===');

for (const cas of CAS.cas) {
  test(`${cas.id} — ${cas.description}`, () => {
    if (cas.type === 'profil_societe') {
      const n = diagnostiquer(creerProfilSociete({ ...cas.input, maintenant: REF }), obligations, { aujourdhui: REF }).applicables.length;
      eq(n, cas.attendu.obligationsApplicables, 'obligations applicables');
    } else if (cas.type === 'profil_utilisateur') {
      const n = diagnostiquer(creerProfilUtilisateur({ ...cas.input, maintenant: REF }), obligations, { aujourdhui: REF }).applicables.length;
      eq(n, cas.attendu.obligationsApplicables, 'obligations applicables');
    } else if (cas.type === 'evenements') {
      const n = planifier(cas.input, { aujourdhui: REF }).total;
      eq(n, cas.attendu.demarches, 'démarches planifiées');
    } else {
      throw new Error(`type de cas inconnu : ${cas.type}`);
    }
  });
}

console.log('=== Versioning réglementaire ===');

test('chaque obligation porte un bloc de validité', () => {
  for (const o of obligations) {
    truthy(o.validite, `obligation ${o.id} sans validite`);
    truthy(o.validite.validFrom && o.validite.juridiction && o.validite.version);
  }
});

test('enVigueurLe respecte la fenêtre de validité', () => {
  const ob = { statut: 'actif', validite: { validFrom: '2025-01-01', validUntil: '2026-12-31', juridiction: 'LU' } };
  eq(enVigueurLe(ob, '2026-07-13'), true);
  eq(enVigueurLe(ob, '2024-06-01'), false);      // avant l'entrée en vigueur
  eq(enVigueurLe(ob, '2027-03-01'), false);      // après l'abrogation
});

test('enVigueurLe filtre par juridiction', () => {
  const ob = { statut: 'actif', validite: { validFrom: '2025-01-01', validUntil: null, juridiction: 'LU' } };
  eq(enVigueurLe(ob, '2026-07-13', { juridiction: 'FR' }), false);
  eq(enVigueurLe(ob, '2026-07-13', { juridiction: 'LU' }), true);
});

test('catalogueEnVigueur : « règles en vigueur au <date> »', () => {
  const enVigueur2027 = catalogueEnVigueur(obligations, '2027-01-01');
  truthy(enVigueur2027.length === obligations.length, 'aucune obligation abrogée avant 2027 dans l\'amorce');
  const avant2025 = catalogueEnVigueur(obligations, '2024-01-01');
  truthy(avant2025.length === 0, 'aucune règle en vigueur avant leur validFrom 2025');
});

console.log('=== Glossaire (explication des acronymes) ===');

test('le glossaire couvre les acronymes clés et est sourcé', () => {
  const g = chargerGlossaire();
  truthy(g.termes.length >= 10);
  for (const t of g.termes) truthy(t.sigle && t.terme && t.definition);
  for (const sigle of ['AED', 'CCSS', 'RCS', 'TVA', 'ADEM']) truthy(g.termes.some((t) => t.sigle === sigle), `manque : ${sigle}`);
});

test('expliquer résout un acronyme', () => {
  eq(expliquer('CCSS').terme, 'Centre commun de la sécurité sociale');
  eq(expliquer('inconnu-xyz'), null);
});

console.log(`\n${passed} tests réussis, ${failed} échoués.`);
process.exit(failed === 0 ? 0 : 1);

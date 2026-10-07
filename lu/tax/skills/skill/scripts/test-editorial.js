#!/usr/bin/env node
/**
 * test-editorial.js — Workflow éditorial de la connaissance + couverture QA.
 */

import { chargerCatalogue } from '../lib/diagnostic/index.js';
import {
  ETAPES_EDITORIALES, etatEditorial, transitionsAutorisees, transitionValide,
  appliquerTransition, historiqueEditorial,
} from '../lib/editorial/index.js';
import {
  chargerCasQA, casQAParRegle, tableauCouverture, metriquesConnaissance,
} from '../lib/connaissances/index.js';

let passed = 0, failed = 0;
function test(name, fn) {
  try { fn(); console.log(`  ✓ ${name}`); passed++; }
  catch (e) { console.log(`  ✗ ${name}\n      ${e.message}`); failed++; }
}
function eq(a, b, msg) { if (a !== b) throw new Error(`${msg || ''}: attendu ${JSON.stringify(b)}, reçu ${JSON.stringify(a)}`); }
function truthy(v, msg) { if (!v) throw new Error(msg || 'attendu truthy'); }

const { obligations } = chargerCatalogue();
const cas = chargerCasQA().cas;

console.log('=== Workflow éditorial ===');

test('les 8 étapes du cycle de vie sont définies', () => {
  eq(ETAPES_EDITORIALES.length, 8);
  for (const e of ['veille', 'proposition', 'analyse', 'validation', 'publication', 'surveillance', 'revision', 'archivage']) truthy(ETAPES_EDITORIALES.includes(e));
});

test('l\'étape éditoriale est inférée du statut', () => {
  eq(etatEditorial({ gouvernance: { status: 'verified' } }), 'publication');
  eq(etatEditorial({ gouvernance: { status: 'a_revoir' } }), 'revision');
  eq(etatEditorial({ gouvernance: { etatEditorial: 'analyse', status: 'draft' } }), 'analyse');
});

test('les transitions valides sont respectées', () => {
  truthy(transitionValide('publication', 'surveillance'));
  truthy(transitionValide('surveillance', 'revision'));
  eq(transitionValide('publication', 'veille'), false);
  truthy(transitionsAutorisees('surveillance').includes('archivage'));
});

test('une transition trace pourquoi / par qui / source / cas QA impactés', () => {
  const regle = { gouvernance: { status: 'verified', etatEditorial: 'surveillance', changeLog: [] } };
  const g = appliquerTransition(regle, {
    vers: 'revision', date: '2027-01-14', reason: 'Modification Guichet.lu',
    author: 'G. Herbé', source: 'https://guichet.public.lu', casQAImpactes: ['plan_naissance'],
  });
  eq(g.etatEditorial, 'revision');
  eq(g.status, 'a_revoir');
  const trace = g.changeLog[g.changeLog.length - 1];
  eq(trace.reason, 'Modification Guichet.lu');
  eq(trace.author, 'G. Herbé');
  eq(trace.source, 'https://guichet.public.lu');
  truthy(trace.casQAImpactes.includes('plan_naissance'));
});

test('une transition non autorisée est refusée', () => {
  let ok = false; try { appliquerTransition({ gouvernance: { etatEditorial: 'publication' } }, { vers: 'veille', date: '2027-01-01' }); } catch { ok = true; }
  truthy(ok);
});

test('publication met à jour lastVerified', () => {
  const g = appliquerTransition({ gouvernance: { etatEditorial: 'validation', changeLog: [] } }, { vers: 'publication', date: '2027-02-01' });
  eq(g.lastVerified, '2027-02-01');
  eq(historiqueEditorial({ gouvernance: g }).length, 1);
});

console.log('=== Couverture QA (traçabilité QA ↔ règle) ===');

test('chaque cas QA déclare les règles qu\'il couvre', () => {
  for (const c of cas) truthy(Array.isArray(c.regles) && c.regles.length >= 1, `cas ${c.id} sans règles`);
});

test('casQAParRegle retrouve les cas à réviser si une règle change', () => {
  const impactes = casQAParRegle('obl_allocations_familiales', cas);
  truthy(impactes.length >= 2, 'les allocations sont couvertes par plusieurs cas');
  truthy(impactes.some((c) => c.id === 'plan_naissance'));
});

console.log('=== Coverage Dashboard & métriques ===');

test('tableauCouverture donne par domaine : règles, couverture, cas QA, dernière revue', () => {
  const tc = tableauCouverture(obligations, cas);
  truthy(tc.length >= 3);
  for (const d of tc) {
    truthy(typeof d.regles === 'number' && typeof d.couverture === 'number');
    truthy(d.couverture >= 0 && d.couverture <= 100);
    truthy('derniereRevue' in d && 'casQA' in d);
  }
  const tva = tc.find((d) => d.domaine === 'tva');
  truthy(tva && tva.couverture > 0);
});

test('metriquesConnaissance : couverture réglementaire, fraîcheur, domaines', () => {
  const m = metriquesConnaissance(obligations, cas, { aujourdhui: '2026-07-13' });
  eq(m.regles, obligations.length);
  truthy(m.couvertureReglementaire > 0 && m.couvertureReglementaire <= 100);
  truthy(typeof m.fraicheurMoyenneJours === 'number');
  truthy(m.domaines >= 3);
});

console.log(`\n${passed} tests réussis, ${failed} échoués.`);
process.exit(failed === 0 ? 0 : 1);

#!/usr/bin/env node
/**
 * test-lbr.js — Tests du module LBR.
 */

import { validerRCS, urlRechercheLBR, calendrierDepots, TARIFS_LBR_2026, CHECKLISTS_LBR, OPERATIONS } from '../lib/lbr/index.js';

let passed = 0, failed = 0;
function test(name, fn) {
  try { fn(); console.log(`  ✓ ${name}`); passed++; }
  catch (e) { console.log(`  ✗ ${name}\n      ${e.message}`); failed++; }
}
function eq(a, b, msg) { if (a !== b) throw new Error(`${msg||''}: attendu ${JSON.stringify(b)}, reçu ${JSON.stringify(a)}`); }
function truthy(v, msg) { if (!v) throw new Error(msg || 'attendu truthy'); }

console.log('=== Tests validation RCS ===');
test('B12345 valide', () => { const r = validerRCS('B12345'); truthy(r.valide); eq(r.normalise, 'B12345'); });
test('b12345 normalisé en B12345', () => eq(validerRCS('b12345').normalise, 'B12345'));
test('"B 12345" tolère espaces', () => eq(validerRCS('B 12345').normalise, 'B12345'));
test('X9999 ASBL reconnue', () => { const r = validerRCS('X9999'); truthy(r.valide); truthy(r.categorie.includes('ASBL')); });
test('K1234 succursale', () => truthy(validerRCS('K1234').categorie.includes('Succursale')));
test('Z12345 invalide (lettre non reconnue)', () => eq(validerRCS('Z12345').valide, false));
test('B (sans chiffres) invalide', () => eq(validerRCS('B').valide, false));
test('B12345678 (>7 chiffres) invalide', () => eq(validerRCS('B12345678').valide, false));
test('vide invalide', () => eq(validerRCS('').valide, false));
test('null invalide', () => eq(validerRCS(null).valide, false));

console.log('\n=== Tests URL recherche LBR ===');
test('URL portail toujours présente', () => {
  const u = urlRechercheLBR({ rcs: 'B12345' });
  truthy(u.portail_recherche.includes('lbr.lu'));
});
test('Aide RCS contient le numéro normalisé', () => {
  const u = urlRechercheLBR({ rcs: 'b12345' });
  truthy(u.aide.includes('B12345'));
});
test('Aide dénomination contient le nom', () => {
  const u = urlRechercheLBR({ denomination: 'ACME SARL' });
  truthy(u.aide.includes('ACME SARL'));
});

console.log('\n=== Tests checklists ===');
test('8 opérations documentées', () => eq(OPERATIONS.length, 8));
test('Toutes les opérations ont une checklist complète', () => {
  for (const op of OPERATIONS) {
    const c = CHECKLISTS_LBR[op];
    truthy(c, `manque ${op}`);
    truthy(c.libelle, `${op} sans libelle`);
    truthy(Array.isArray(c.pieces) && c.pieces.length >= 3, `${op} pieces insuffisantes`);
  }
});
test('SARL : capital minimum 12 000 €', () => eq(CHECKLISTS_LBR.creation_sarl.capital_minimum_eur, 12000));
test('SA : capital minimum 30 000 €', () => eq(CHECKLISTS_LBR.creation_sa.capital_minimum_eur, 30000));
test('Dépôt comptes annuels : délai 7 mois après clôture', () => {
  eq(CHECKLISTS_LBR.depot_comptes_annuels.delai_apres_cloture_mois, 7);
});

console.log('\n=== Tests calendrier dépôts ===');
test('Clôture 2025-12-31 → AG le 2026-06-30', () => {
  const cal = calendrierDepots({ exerciceFin: '2025-12-31' });
  eq(cal[0].deadline, '2026-06-30');
});
test('Dépôt LBR comptes le 2026-07-31', () => {
  const cal = calendrierDepots({ exerciceFin: '2025-12-31' });
  eq(cal[1].deadline, '2026-07-31');
});
test('eCDF mentionné dans le calendrier', () => {
  const cal = calendrierDepots({ exerciceFin: '2025-12-31' });
  truthy(cal.some(e => e.nature.includes('eCDF')));
});
test('Refus si exerciceFin manquant', () => {
  let err;
  try { calendrierDepots({}); } catch (e) { err = e; }
  truthy(err);
});

console.log('\n=== Tests tarifs 2026 ===');
test('Dépôt comptes : 19 €', () => eq(TARIFS_LBR_2026.depot_comptes.montant_eur, 19));
test('Inscription société : 22 €', () => eq(TARIFS_LBR_2026.inscription_societe.montant_eur, 22));
test('Tous tarifs ont un libellé et un montant', () => {
  for (const [k, v] of Object.entries(TARIFS_LBR_2026)) {
    if (k.startsWith('_')) continue;
    truthy(v.libelle && typeof v.montant_eur === 'number', `${k} incomplet`);
  }
});

console.log(`\n${passed} passés, ${failed} échoués\n`);
process.exit(failed === 0 ? 0 : 1);

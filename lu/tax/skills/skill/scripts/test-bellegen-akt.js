#!/usr/bin/env node
/**
 * test-bellegen-akt.js — Tests du module Bëllegen Akt.
 */

import {
  calculerBellegenAkt,
  estimerHonoraires,
  TAUX_DROITS_LU,
  ABATTEMENT_BELLEGEN_AKT_PAR_PERSONNE,
} from '../lib/bellegen-akt/index.js';

let passed = 0, failed = 0;
function test(name, fn) {
  try { fn(); console.log(`  ✓ ${name}`); passed++; }
  catch (e) { console.log(`  ✗ ${name}\n      ${e.message}`); failed++; }
}
function eq(a, b, msg) { if (a !== b) throw new Error(`${msg||''}: attendu ${JSON.stringify(b)}, reçu ${JSON.stringify(a)}`); }
function near(a, b, tol = 0.01, msg) {
  if (Math.abs(a - b) > tol) throw new Error(`${msg||''}: attendu ~${b} (±${tol}), reçu ${a}`);
}
function truthy(v, msg) { if (!v) throw new Error(msg || 'attendu truthy'); }

console.log('=== Tests constantes ===');

test('plafond Bëllegen Akt = 40 000 €/personne (loi 22 mai 2024)', () => {
  eq(ABATTEMENT_BELLEGEN_AKT_PAR_PERSONNE, 40000);
});

test('taux droits standard 6 % + 1 % transcription', () => {
  eq(TAUX_DROITS_LU.enregistrement, 0.06);
  eq(TAUX_DROITS_LU.transcription, 0.01);
  eq(TAUX_DROITS_LU.surtaxeLuxVille, 0.03);
});

console.log('\n=== Tests calculs droits nominaux ===');

test('hors Lux-Ville : 7 % au total (6 % + 1 %)', () => {
  const r = calculerBellegenAkt({ prix: 500000, bellegenAkt: false });
  near(r.droitsNominaux, 35000); // 500k × 7 %
  eq(r.tauxTotal, 0.07);
});

test('Lux-Ville : 10 % au total (6 % + 3 % + 1 %)', () => {
  const r = calculerBellegenAkt({ prix: 500000, luxVille: true, bellegenAkt: false });
  near(r.droitsNominaux, 50000);
  eq(r.tauxTotal, 0.10);
});

console.log('\n=== Tests Bëllegen Akt ===');

test('couple primo-accédant Lux-Ville 800k : 80k droits, abattement 80k → 0 € droits', () => {
  const r = calculerBellegenAkt({ prix: 800000, luxVille: true, nbAcquereurs: 2 });
  near(r.droitsNominaux, 80000);
  eq(r.bellegenAkt.abattementMaximalTheorique, 80000);
  eq(r.bellegenAkt.abattementEffectif, 80000);
  eq(r.droitsNets, 0);
});

test('célibataire 600k hors Lux-Ville : 42k droits, abattement 40k → 2k droits', () => {
  const r = calculerBellegenAkt({ prix: 600000, nbAcquereurs: 1 });
  near(r.droitsNominaux, 42000);
  eq(r.bellegenAkt.abattementEffectif, 40000);
  near(r.droitsNets, 2000);
  truthy(r.bellegenAkt.saturé);
});

test('couple petit prix 200k : abattement plafonné aux droits dus, jamais de remboursement', () => {
  const r = calculerBellegenAkt({ prix: 200000, nbAcquereurs: 2 });
  near(r.droitsNominaux, 14000); // 200k × 7 %
  eq(r.bellegenAkt.abattementEffectif, 14000); // capé aux droits, pas 80k
  eq(r.droitsNets, 0);
});

test('bellegenAkt: false → aucune réduction', () => {
  const r = calculerBellegenAkt({ prix: 500000, bellegenAkt: false });
  eq(r.bellegenAkt.abattementEffectif, 0);
  near(r.droitsNets, 35000);
});

test('acte avant 2024-10-01 : ancien plafond 30 000 €/personne', () => {
  const r = calculerBellegenAkt({ prix: 600000, nbAcquereurs: 1, dateActe: '2024-09-15' });
  eq(r.bellegenAkt.plafondParPersonne, 30000);
  eq(r.bellegenAkt.abattementEffectif, 30000);
  near(r.droitsNets, 12000);
});

test('acte au 2024-10-01 : nouveau plafond 40 000 €/personne', () => {
  const r = calculerBellegenAkt({ prix: 600000, nbAcquereurs: 1, dateActe: '2024-10-01' });
  eq(r.bellegenAkt.plafondParPersonne, 40000);
});

console.log('\n=== Tests honoraires + total ===');

test('honoraires dégressifs cohérents (300k < 1M)', () => {
  const h300 = estimerHonoraires(300000);
  const h1M = estimerHonoraires(1000000);
  truthy(h1M > h300);
  // taux marginal décroît
  truthy((h1M - h300) / 700000 < 0.009);
});

test('total = droits nets + honoraires + TVA + débours', () => {
  const r = calculerBellegenAkt({ prix: 400000, nbAcquereurs: 2 });
  near(r.total, r.droitsNets + r.honoraires + r.tvaHonoraires + r.debours, 0.02);
});

test('TVA honoraires = 17 %', () => {
  const r = calculerBellegenAkt({ prix: 400000 });
  near(r.tvaHonoraires, r.honoraires * 0.17, 0.02);
});

console.log('\n=== Tests validation ===');

test('prix 0 rejeté', () => {
  let ok = false; try { calculerBellegenAkt({ prix: 0 }); } catch { ok = true; }
  truthy(ok);
});

test('prix négatif rejeté', () => {
  let ok = false; try { calculerBellegenAkt({ prix: -100 }); } catch { ok = true; }
  truthy(ok);
});

test('nbAcquereurs 0 rejeté', () => {
  let ok = false; try { calculerBellegenAkt({ prix: 100000, nbAcquereurs: 0 }); } catch { ok = true; }
  truthy(ok);
});

test('dateActe mal formée rejetée', () => {
  let ok = false; try { calculerBellegenAkt({ prix: 100000, dateActe: '01/10/2024' }); } catch { ok = true; }
  truthy(ok);
});

test('dateActe impossible 2024-99-99 rejetée', () => {
  let ok = false; try { calculerBellegenAkt({ prix: 100000, dateActe: '2024-99-99' }); } catch { ok = true; }
  truthy(ok);
});

test('dateActe 2024-02-30 rejetée', () => {
  let ok = false; try { calculerBellegenAkt({ prix: 100000, dateActe: '2024-02-30' }); } catch { ok = true; }
  truthy(ok);
});

console.log(`\n${passed} passé(s), ${failed} échec(s)`);
process.exit(failed === 0 ? 0 : 1);

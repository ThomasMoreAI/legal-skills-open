#!/usr/bin/env node
/**
 * test-rts.js — Tests du module RTS (retenue à la source LU).
 */

import { calculerRTS, impotBareme, BAREME_IRPP_2025, COTISATIONS_LU_2025 } from '../lib/rts/index.js';

let passed = 0, failed = 0;
function test(name, fn) {
  try { fn(); console.log(`  ✓ ${name}`); passed++; }
  catch (e) { console.log(`  ✗ ${name}\n      ${e.message}`); failed++; }
}
function eq(a, b, msg) { if (a !== b) throw new Error(`${msg||''}: attendu ${JSON.stringify(b)}, reçu ${JSON.stringify(a)}`); }
function near(a, b, tol = 1, msg) {
  if (Math.abs(a - b) > tol) throw new Error(`${msg||''}: attendu ~${b} (±${tol}), reçu ${a}`);
}
function truthy(v, msg) { if (!v) throw new Error(msg || 'attendu truthy'); }

console.log('=== Tests barème IRPP 2025 ===');

test('barème commence à 0 % jusqu\'à 13 230 €', () => {
  eq(impotBareme(13230), 0);
  eq(impotBareme(10000), 0);
});

test('taux marginal max 42 % au-delà de 234 870 €', () => {
  const last = BAREME_IRPP_2025[BAREME_IRPP_2025.length - 1];
  eq(last.taux, 0.42);
});

test('barème croît strictement', () => {
  for (let i = 1; i < BAREME_IRPP_2025.length; i++) {
    if (BAREME_IRPP_2025[i].taux < BAREME_IRPP_2025[i - 1].taux) {
      throw new Error(`taux décroissant à l'index ${i}`);
    }
  }
});

test('impôt 50k annuel cohérent (~6-8k)', () => {
  const i = impotBareme(50000);
  truthy(i > 5000 && i < 9000, `impôt 50k = ${i}`);
});

test('impôt double si revenu double (au-delà des seuils non-progressifs élevés)', () => {
  const i200k = impotBareme(200000);
  const i400k = impotBareme(400000);
  truthy(i400k > i200k * 1.5, 'progressivité confirmée');
});

console.log('\n=== Tests cotisations sociales ===');

test('CSSS salarié = 10,80 % (2,8 maladie + 8,0 pension)', () => {
  eq(COTISATIONS_LU_2025.csssAssuranceMaladieSalarie + COTISATIONS_LU_2025.csssPensionSalarie, 0.108);
});

test('CSSS calculé sur 5000 € = 540 €', () => {
  const r = calculerRTS({ salaireBrutMensuel: 5000, classe: '1' });
  near(r.csss.total, 540, 0.5);
});

console.log('\n=== Tests classes d\'impôt ===');

test('classe 2 (couple) paie moins que classe 1 à revenu égal', () => {
  const r1 = calculerRTS({ salaireBrutMensuel: 6000, classe: '1' });
  const r2 = calculerRTS({ salaireBrutMensuel: 6000, classe: '2' });
  truthy(r2.irppAnnuel < r1.irppAnnuel, `c1=${r1.irppAnnuel} c2=${r2.irppAnnuel}`);
});

test('classe 1a paie moins que classe 1 (abattement)', () => {
  const r1 = calculerRTS({ salaireBrutMensuel: 4000, classe: '1' });
  const r1a = calculerRTS({ salaireBrutMensuel: 4000, classe: '1a' });
  truthy(r1a.irppAnnuel <= r1.irppAnnuel);
});

test('classe invalide rejetée', () => {
  let ok = false; try { calculerRTS({ salaireBrutMensuel: 5000, classe: '3' }); } catch { ok = true; }
  truthy(ok);
});

console.log('\n=== Tests cas concrets ===');

test('SMIC qualifié ~2554 €/mois classe 1 : impôt très faible', () => {
  const r = calculerRTS({ salaireBrutMensuel: 2554, classe: '1' });
  truthy(r.irppMensuel < 100, `irpp=${r.irppMensuel}`);
  truthy(r.netMensuel > 2000);
});

test('cadre 8000 €/mois classe 1 : net entre 5300 et 6000', () => {
  const r = calculerRTS({ salaireBrutMensuel: 8000, classe: '1' });
  truthy(r.netMensuel > 5300 && r.netMensuel < 6000, `net=${r.netMensuel}`);
});

test('haut salaire 15000 €/mois classe 1 : taux effectif > 35 %', () => {
  const r = calculerRTS({ salaireBrutMensuel: 15000, classe: '1' });
  truthy(r.tauxRetenueEffectif > 0.35, `taux=${r.tauxRetenueEffectif}`);
});

test('cohérence net = brut - csss - irpp - dépendance', () => {
  const r = calculerRTS({ salaireBrutMensuel: 6000, classe: '1' });
  near(r.netMensuel, r.salaireBrutMensuel - r.csss.total - r.irppMensuel - r.contribDependance, 0.02);
});

console.log('\n=== Tests crédits d\'impôt ===');

test('CIS actif réduit l\'impôt mensuel de 70 €', () => {
  const avec = calculerRTS({ salaireBrutMensuel: 5000, classe: '1', cisActif: true });
  const sans = calculerRTS({ salaireBrutMensuel: 5000, classe: '1', cisActif: false });
  near(sans.irppMensuel - avec.irppMensuel, 70, 0.5);
});

test('CIM (monoparental) actif réduit l\'impôt de 188 €', () => {
  const avec = calculerRTS({ salaireBrutMensuel: 5000, classe: '1a', cisActif: false, cimActif: true });
  const sans = calculerRTS({ salaireBrutMensuel: 5000, classe: '1a', cisActif: false, cimActif: false });
  near(sans.irppMensuel - avec.irppMensuel, 188, 0.5);
});

test('crédits ne peuvent pas rendre l\'impôt négatif', () => {
  const r = calculerRTS({ salaireBrutMensuel: 1000, classe: '1', cisActif: true, cimActif: true });
  truthy(r.irppMensuel >= 0);
});

console.log('\n=== Tests validation ===');

test('salaire 0 rejeté', () => {
  let ok = false; try { calculerRTS({ salaireBrutMensuel: 0, classe: '1' }); } catch { ok = true; }
  truthy(ok);
});

test('salaire négatif rejeté', () => {
  let ok = false; try { calculerRTS({ salaireBrutMensuel: -100, classe: '1' }); } catch { ok = true; }
  truthy(ok);
});

test('deductionsAnnuelles non-numérique rejeté (pas de NaN silencieux)', () => {
  let ok = false; try { calculerRTS({ salaireBrutMensuel: 5000, classe: '1', deductionsAnnuelles: 'abc' }); } catch { ok = true; }
  truthy(ok);
});

test('deductionsAnnuelles négatif rejeté', () => {
  let ok = false; try { calculerRTS({ salaireBrutMensuel: 5000, classe: '1', deductionsAnnuelles: -1000 }); } catch { ok = true; }
  truthy(ok);
});

test('salaire NaN/Infinity rejeté', () => {
  let ok1 = false, ok2 = false;
  try { calculerRTS({ salaireBrutMensuel: NaN, classe: '1' }); } catch { ok1 = true; }
  try { calculerRTS({ salaireBrutMensuel: Infinity, classe: '1' }); } catch { ok2 = true; }
  truthy(ok1 && ok2);
});

test('avertissement classe 1a présent', () => {
  const r = calculerRTS({ salaireBrutMensuel: 4000, classe: '1a' });
  truthy(r.avertissements.some((a) => a.includes('1a')));
});

console.log(`\n${passed} passé(s), ${failed} échec(s)`);
process.exit(failed === 0 ? 0 : 1);

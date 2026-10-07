#!/usr/bin/env node
/**
 * test-frontalier.js — Tests du module frontaliers (FR/BE/DE → LU).
 */

import {
  calculerNetFrontalier,
  impotBaremeBE,
  BAREME_IPP_BE_2025,
  QUOTITE_EXEMPTEE_BE_2025,
  SEUIL_JOURS_FRONTALIER,
  TAUX_COMMUNAL_BE_DEFAUT,
} from '../lib/frontaliers/index.js';
import { calculerRTS } from '../lib/rts/index.js';

let passed = 0, failed = 0;
function test(name, fn) {
  try { fn(); console.log(`  ✓ ${name}`); passed++; }
  catch (e) { console.log(`  ✗ ${name}\n      ${e.message}`); failed++; }
}
function eq(a, b, msg) { if (a !== b) throw new Error(`${msg||''}: attendu ${JSON.stringify(b)}, reçu ${JSON.stringify(a)}`); }
function near(a, b, tol = 1, msg) { if (Math.abs(a - b) > tol) throw new Error(`${msg||''}: attendu ~${b} (±${tol}), reçu ${a}`); }
function truthy(v, msg) { if (!v) throw new Error(msg || 'attendu truthy'); }

console.log('=== Tests communs (toutes nationalités) ===');

test('le net LU est identique à calculerRTS pur', () => {
  const ref = calculerRTS({ salaireBrutMensuel: 5000, classe: '1' });
  const fr = calculerNetFrontalier({ salaireBrutMensuel: 5000, paysResidence: 'FR', classe: '1' });
  eq(fr.netLuMensuel, ref.netMensuel);
});

test('la retenue LU est identique pour FR/BE/DE à brut/classe égaux', () => {
  const fr = calculerNetFrontalier({ salaireBrutMensuel: 5000, paysResidence: 'FR', classe: '1' });
  const be = calculerNetFrontalier({ salaireBrutMensuel: 5000, paysResidence: 'BE', classe: '1' });
  const de = calculerNetFrontalier({ salaireBrutMensuel: 5000, paysResidence: 'DE', classe: '1' });
  eq(fr.retenueLuMensuel, be.retenueLuMensuel);
  eq(fr.retenueLuMensuel, de.retenueLuMensuel);
});

test('chaque résultat porte au moins un avertissement « calcul indicatif »', () => {
  for (const pays of ['FR', 'BE', 'DE']) {
    const r = calculerNetFrontalier({ salaireBrutMensuel: 5000, paysResidence: pays, classe: '1' });
    truthy(r.avertissements.some((a) => /indicatif/i.test(a)), `${pays} sans avertissement indicatif`);
  }
});

test('chaque résultat expose le seuil jours actuel et historique', () => {
  for (const pays of ['FR', 'BE', 'DE']) {
    const r = calculerNetFrontalier({ salaireBrutMensuel: 5000, paysResidence: pays, classe: '1' });
    eq(r.seuilJours.actuel, SEUIL_JOURS_FRONTALIER[pays].actuel);
    eq(r.seuilJours.historique, SEUIL_JOURS_FRONTALIER[pays].historique);
  }
});

test('seuils historiques conformes à la tâche : FR=19, BE=24, DE=19', () => {
  eq(SEUIL_JOURS_FRONTALIER.FR.historique, 19);
  eq(SEUIL_JOURS_FRONTALIER.BE.historique, 24);
  eq(SEUIL_JOURS_FRONTALIER.DE.historique, 19);
});

test('cohérence net final = net LU - ajustement résidence', () => {
  for (const pays of ['FR', 'BE', 'DE']) {
    const r = calculerNetFrontalier({ salaireBrutMensuel: 6000, paysResidence: pays, classe: '2' });
    near(r.netFinalMensuel, r.netLuMensuel - r.ajustementResidenceMensuel, 0.02);
  }
});

test('taux global de retenue cohérent avec brut et net final', () => {
  const r = calculerNetFrontalier({ salaireBrutMensuel: 5000, paysResidence: 'BE', classe: '1' });
  near(r.tauxRetenueGlobal, 1 - r.netFinalMensuel / r.salaireBrutMensuel, 0.002);
});

console.log('\n=== Tests France ===');

test('FR : ajustement résidence = 0 (exonération avec progressivité)', () => {
  const r = calculerNetFrontalier({ salaireBrutMensuel: 5000, paysResidence: 'FR', classe: '1' });
  eq(r.ajustementResidenceMensuel, 0);
  eq(r.netFinalMensuel, r.netLuMensuel);
});

test('FR : avertissement explicite sur le taux effectif', () => {
  const r = calculerNetFrontalier({ salaireBrutMensuel: 5000, paysResidence: 'FR', classe: '1' });
  truthy(r.avertissements.some((a) => /taux effectif/i.test(a)));
});

test('FR : déclencher un avertissement au-delà de 34 jours hors LU', () => {
  const r = calculerNetFrontalier({ salaireBrutMensuel: 5000, paysResidence: 'FR', classe: '1', joursHorsLU: 40 });
  truthy(r.avertissements.some((a) => a.includes('40 jours hors LU')));
});

test('FR : seuil 34 jours non dépassé → pas d\'avertissement de bascule', () => {
  const r = calculerNetFrontalier({ salaireBrutMensuel: 5000, paysResidence: 'FR', classe: '1', joursHorsLU: 30 });
  truthy(!r.avertissements.some((a) => a.includes('au-delà du seuil')));
});

test('FR : formulaire 2042/2047 référencé', () => {
  const r = calculerNetFrontalier({ salaireBrutMensuel: 5000, paysResidence: 'FR', classe: '1' });
  truthy(r.detailsResidence.formulaireResidence.includes('2042'));
});

console.log('\n=== Tests Belgique ===');

test('BE : ajustement résidence > 0 (additionnels communaux)', () => {
  const r = calculerNetFrontalier({ salaireBrutMensuel: 5000, paysResidence: 'BE', classe: '1' });
  truthy(r.ajustementResidenceMensuel > 0, `ajustement BE = ${r.ajustementResidenceMensuel}`);
});

test('BE : net final < net LU (à cause des additionnels communaux)', () => {
  const r = calculerNetFrontalier({ salaireBrutMensuel: 5000, paysResidence: 'BE', classe: '1' });
  truthy(r.netFinalMensuel < r.netLuMensuel);
});

test('BE : taux communal personnalisé fait croître l\'ajustement', () => {
  const bas = calculerNetFrontalier({ salaireBrutMensuel: 5000, paysResidence: 'BE', classe: '1', tauxCommunalBE: 0.05 });
  const haut = calculerNetFrontalier({ salaireBrutMensuel: 5000, paysResidence: 'BE', classe: '1', tauxCommunalBE: 0.09 });
  truthy(haut.ajustementResidenceMensuel > bas.ajustementResidenceMensuel);
});

test('BE : taux communal défaut = 7,5 %', () => {
  eq(TAUX_COMMUNAL_BE_DEFAUT, 0.075);
});

test('BE : détail expose IPP fédéral théorique et taux communal', () => {
  const r = calculerNetFrontalier({ salaireBrutMensuel: 5000, paysResidence: 'BE', classe: '1' });
  truthy(Number.isFinite(r.detailsResidence.ippFederalTheoriqueAnnuel));
  eq(r.detailsResidence.tauxCommunalApplique, 0.075);
});

test('BE : avertissement spécifique sur les centimes additionnels', () => {
  const r = calculerNetFrontalier({ salaireBrutMensuel: 5000, paysResidence: 'BE', classe: '1' });
  truthy(r.avertissements.some((a) => /additionnels communaux/i.test(a)));
});

test('BE : taux communal hors bornes rejeté', () => {
  let ok = false;
  try { calculerNetFrontalier({ salaireBrutMensuel: 5000, paysResidence: 'BE', classe: '1', tauxCommunalBE: 0.8 }); }
  catch { ok = true; }
  truthy(ok);
});

test('BE : barème IPP croît strictement', () => {
  for (let i = 1; i < BAREME_IPP_BE_2025.length; i++) {
    if (BAREME_IPP_BE_2025[i].taux <= BAREME_IPP_BE_2025[i - 1].taux) {
      throw new Error(`taux non croissant à l'index ${i}`);
    }
  }
});

test('BE : impotBaremeBE(0) = 0', () => {
  eq(impotBaremeBE(0), 0);
  eq(impotBaremeBE(-100), 0);
});

test('BE : impotBaremeBE(10000) = 2500 € (10000 × 25 %)', () => {
  near(impotBaremeBE(10000), 2500, 0.5);
});

test('BE : quotité exemptée 2025 = 10 570 €', () => {
  eq(QUOTITE_EXEMPTEE_BE_2025, 10570);
});

console.log('\n=== Tests Allemagne ===');

test('DE : ajustement résidence = 0 (Progressionsvorbehalt)', () => {
  const r = calculerNetFrontalier({ salaireBrutMensuel: 5000, paysResidence: 'DE', classe: '1' });
  eq(r.ajustementResidenceMensuel, 0);
  eq(r.netFinalMensuel, r.netLuMensuel);
});

test('DE : mention Progressionsvorbehalt dans la méthode', () => {
  const r = calculerNetFrontalier({ salaireBrutMensuel: 5000, paysResidence: 'DE', classe: '1' });
  truthy(/Progression/i.test(r.detailsResidence.methode));
});

test('DE : formulaire Anlage N-AUS référencé', () => {
  const r = calculerNetFrontalier({ salaireBrutMensuel: 5000, paysResidence: 'DE', classe: '1' });
  truthy(r.detailsResidence.formulaireResidence.includes('N-AUS'));
});

test('DE : avertissement explicite sur Progressionsvorbehalt', () => {
  const r = calculerNetFrontalier({ salaireBrutMensuel: 5000, paysResidence: 'DE', classe: '1' });
  truthy(r.avertissements.some((a) => /Progression/i.test(a)));
});

console.log('\n=== Tests validation ===');

test('pays inconnu rejeté', () => {
  let ok = false;
  try { calculerNetFrontalier({ salaireBrutMensuel: 5000, paysResidence: 'ES', classe: '1' }); }
  catch { ok = true; }
  truthy(ok);
});

test('classe invalide rejetée', () => {
  let ok = false;
  try { calculerNetFrontalier({ salaireBrutMensuel: 5000, paysResidence: 'FR', classe: '3' }); }
  catch { ok = true; }
  truthy(ok);
});

test('salaire 0 rejeté', () => {
  let ok = false;
  try { calculerNetFrontalier({ salaireBrutMensuel: 0, paysResidence: 'FR', classe: '1' }); }
  catch { ok = true; }
  truthy(ok);
});

test('joursHorsLU négatif rejeté', () => {
  let ok = false;
  try { calculerNetFrontalier({ salaireBrutMensuel: 5000, paysResidence: 'FR', classe: '1', joursHorsLU: -5 }); }
  catch { ok = true; }
  truthy(ok);
});

test('joursHorsLU > 366 rejeté', () => {
  let ok = false;
  try { calculerNetFrontalier({ salaireBrutMensuel: 5000, paysResidence: 'FR', classe: '1', joursHorsLU: 400 }); }
  catch { ok = true; }
  truthy(ok);
});

console.log('\n=== Tests France (extension : 15+ couvertures) ===');

test('FR : classe 1 produit un net mensuel cohérent (~3,7k pour 5k brut)', () => {
  const r = calculerNetFrontalier({ salaireBrutMensuel: 5000, paysResidence: 'FR', classe: '1' });
  truthy(r.netFinalMensuel > 3500 && r.netFinalMensuel < 3900, `net=${r.netFinalMensuel}`);
});

test('FR : classe 2 (couple marié) donne un net supérieur à classe 1', () => {
  const c1 = calculerNetFrontalier({ salaireBrutMensuel: 6000, paysResidence: 'FR', classe: '1' });
  const c2 = calculerNetFrontalier({ salaireBrutMensuel: 6000, paysResidence: 'FR', classe: '2' });
  truthy(c2.netFinalMensuel > c1.netFinalMensuel);
});

test('FR : classe 1a donne un net ≥ classe 1 (abattement)', () => {
  const c1 = calculerNetFrontalier({ salaireBrutMensuel: 4000, paysResidence: 'FR', classe: '1' });
  const c1a = calculerNetFrontalier({ salaireBrutMensuel: 4000, paysResidence: 'FR', classe: '1a' });
  truthy(c1a.netFinalMensuel >= c1.netFinalMensuel);
});

test('FR : un brut plus élevé donne un net plus élevé (monotonicité)', () => {
  const a = calculerNetFrontalier({ salaireBrutMensuel: 4000, paysResidence: 'FR', classe: '1' });
  const b = calculerNetFrontalier({ salaireBrutMensuel: 8000, paysResidence: 'FR', classe: '1' });
  truthy(b.netFinalMensuel > a.netFinalMensuel);
});

test('FR : --no-cis fait baisser le net (CIS désactivé)', () => {
  const avec = calculerNetFrontalier({ salaireBrutMensuel: 5000, paysResidence: 'FR', classe: '1', cisActif: true });
  const sans = calculerNetFrontalier({ salaireBrutMensuel: 5000, paysResidence: 'FR', classe: '1', cisActif: false });
  truthy(sans.netFinalMensuel < avec.netFinalMensuel);
});

test('FR : CIM monoparental fait monter le net', () => {
  const sans = calculerNetFrontalier({ salaireBrutMensuel: 5000, paysResidence: 'FR', classe: '1a', cimActif: false });
  const avec = calculerNetFrontalier({ salaireBrutMensuel: 5000, paysResidence: 'FR', classe: '1a', cimActif: true });
  truthy(avec.netFinalMensuel > sans.netFinalMensuel);
});

test('FR : taux global = taux retenue LU effectif (pas d\'ajustement)', () => {
  const r = calculerNetFrontalier({ salaireBrutMensuel: 5000, paysResidence: 'FR', classe: '1' });
  near(r.tauxRetenueGlobal, r.detailRTS.tauxRetenueEffectif, 0.005);
});

test('FR : pays exposé en MAJUSCULES', () => {
  const r = calculerNetFrontalier({ salaireBrutMensuel: 5000, paysResidence: 'FR', classe: '1' });
  eq(r.paysResidence, 'FR');
});

test('FR : netFinalAnnuel = netFinalMensuel × 12', () => {
  const r = calculerNetFrontalier({ salaireBrutMensuel: 5000, paysResidence: 'FR', classe: '1' });
  near(r.netFinalAnnuel, r.netFinalMensuel * 12, 0.05);
});

test('FR : seuil actuel = 34 jours (avenant 2022)', () => {
  const r = calculerNetFrontalier({ salaireBrutMensuel: 5000, paysResidence: 'FR', classe: '1' });
  eq(r.seuilJours.actuel, 34);
});

test('FR : exactement à 34 jours, pas de bascule signalée', () => {
  const r = calculerNetFrontalier({ salaireBrutMensuel: 5000, paysResidence: 'FR', classe: '1', joursHorsLU: 34 });
  truthy(!r.avertissements.some((a) => a.includes('au-delà du seuil')));
});

console.log('\n=== Tests Belgique (extension : 15+ couvertures) ===');

test('BE : classe 2 produit un net supérieur à classe 1', () => {
  const c1 = calculerNetFrontalier({ salaireBrutMensuel: 6000, paysResidence: 'BE', classe: '1' });
  const c2 = calculerNetFrontalier({ salaireBrutMensuel: 6000, paysResidence: 'BE', classe: '2' });
  truthy(c2.netFinalMensuel > c1.netFinalMensuel);
});

test('BE : commune à 0 % → ajustement résidence = 0', () => {
  const r = calculerNetFrontalier({ salaireBrutMensuel: 5000, paysResidence: 'BE', classe: '1', tauxCommunalBE: 0 });
  eq(r.ajustementResidenceMensuel, 0);
  eq(r.netFinalMensuel, r.netLuMensuel);
});

test('BE : net BE < net FR pour mêmes paramètres (additionnels en plus)', () => {
  const fr = calculerNetFrontalier({ salaireBrutMensuel: 5000, paysResidence: 'FR', classe: '1' });
  const be = calculerNetFrontalier({ salaireBrutMensuel: 5000, paysResidence: 'BE', classe: '1' });
  truthy(be.netFinalMensuel < fr.netFinalMensuel);
});

test('BE : ajustement annuel = mensuel × 12', () => {
  const r = calculerNetFrontalier({ salaireBrutMensuel: 5000, paysResidence: 'BE', classe: '1' });
  near(r.ajustementResidenceAnnuel, r.ajustementResidenceMensuel * 12, 0.05);
});

test('BE : impotBaremeBE(15820) = 25 % × 15820 = 3955 €', () => {
  near(impotBaremeBE(15820), 15820 * 0.25, 0.5);
});

test('BE : impotBaremeBE(50000) cohérent avec barème par tranches', () => {
  const attendu = 15820 * 0.25 + (27920 - 15820) * 0.40 + (48320 - 27920) * 0.45 + (50000 - 48320) * 0.50;
  near(impotBaremeBE(50000), attendu, 0.5);
});

test('BE : avertissement de bascule au-delà de 34 jours hors LU', () => {
  const r = calculerNetFrontalier({ salaireBrutMensuel: 5000, paysResidence: 'BE', classe: '1', joursHorsLU: 50 });
  truthy(r.avertissements.some((a) => a.includes('50 jours hors LU')));
});

test('BE : à 34 jours exact, pas de bascule', () => {
  const r = calculerNetFrontalier({ salaireBrutMensuel: 5000, paysResidence: 'BE', classe: '1', joursHorsLU: 34 });
  truthy(!r.avertissements.some((a) => a.includes('au-delà du seuil')));
});

test('BE : seuil actuel = 34 (avenant 2021), historique = 24', () => {
  const r = calculerNetFrontalier({ salaireBrutMensuel: 5000, paysResidence: 'BE', classe: '1' });
  eq(r.seuilJours.actuel, 34);
  eq(r.seuilJours.historique, 24);
});

test('BE : taux global > taux LU pur (additionnels en plus)', () => {
  const r = calculerNetFrontalier({ salaireBrutMensuel: 5000, paysResidence: 'BE', classe: '1' });
  truthy(r.tauxRetenueGlobal > r.detailRTS.tauxRetenueEffectif);
});

console.log('\n=== Tests Allemagne (extension : 15+ couvertures) ===');

test('DE : classe 2 produit un net supérieur à classe 1', () => {
  const c1 = calculerNetFrontalier({ salaireBrutMensuel: 6000, paysResidence: 'DE', classe: '1' });
  const c2 = calculerNetFrontalier({ salaireBrutMensuel: 6000, paysResidence: 'DE', classe: '2' });
  truthy(c2.netFinalMensuel > c1.netFinalMensuel);
});

test('DE : net DE = net FR (deux pays sans ajustement résiduel)', () => {
  const fr = calculerNetFrontalier({ salaireBrutMensuel: 5000, paysResidence: 'FR', classe: '1' });
  const de = calculerNetFrontalier({ salaireBrutMensuel: 5000, paysResidence: 'DE', classe: '1' });
  eq(de.netFinalMensuel, fr.netFinalMensuel);
});

test('DE : net DE > net BE (pas d\'additionnels communaux)', () => {
  const be = calculerNetFrontalier({ salaireBrutMensuel: 5000, paysResidence: 'BE', classe: '1' });
  const de = calculerNetFrontalier({ salaireBrutMensuel: 5000, paysResidence: 'DE', classe: '1' });
  truthy(de.netFinalMensuel > be.netFinalMensuel);
});

test('DE : pas de champ IPP fédéral (spécifique BE)', () => {
  const r = calculerNetFrontalier({ salaireBrutMensuel: 5000, paysResidence: 'DE', classe: '1' });
  eq(r.detailsResidence.ippFederalTheoriqueAnnuel, undefined);
});

test('DE : avertissement de bascule au-delà de 34 jours hors LU', () => {
  const r = calculerNetFrontalier({ salaireBrutMensuel: 5000, paysResidence: 'DE', classe: '1', joursHorsLU: 60 });
  truthy(r.avertissements.some((a) => a.includes('60 jours hors LU')));
});

test('DE : à 34 jours exact, pas de bascule', () => {
  const r = calculerNetFrontalier({ salaireBrutMensuel: 5000, paysResidence: 'DE', classe: '1', joursHorsLU: 34 });
  truthy(!r.avertissements.some((a) => a.includes('au-delà du seuil')));
});

test('DE : seuil actuel = 34 (accord 2023), historique = 19', () => {
  const r = calculerNetFrontalier({ salaireBrutMensuel: 5000, paysResidence: 'DE', classe: '1' });
  eq(r.seuilJours.actuel, 34);
  eq(r.seuilJours.historique, 19);
});

test('DE : taux global = taux LU effectif (pas d\'ajustement)', () => {
  const r = calculerNetFrontalier({ salaireBrutMensuel: 5000, paysResidence: 'DE', classe: '1' });
  near(r.tauxRetenueGlobal, r.detailRTS.tauxRetenueEffectif, 0.005);
});

test('DE : monotonicité — un brut plus élevé donne un net plus élevé', () => {
  const a = calculerNetFrontalier({ salaireBrutMensuel: 4000, paysResidence: 'DE', classe: '1' });
  const b = calculerNetFrontalier({ salaireBrutMensuel: 8000, paysResidence: 'DE', classe: '1' });
  truthy(b.netFinalMensuel > a.netFinalMensuel);
});

test('DE : --no-cis fait baisser le net', () => {
  const avec = calculerNetFrontalier({ salaireBrutMensuel: 5000, paysResidence: 'DE', classe: '1', cisActif: true });
  const sans = calculerNetFrontalier({ salaireBrutMensuel: 5000, paysResidence: 'DE', classe: '1', cisActif: false });
  truthy(sans.netFinalMensuel < avec.netFinalMensuel);
});

test('DE : netFinalAnnuel = netFinalMensuel × 12', () => {
  const r = calculerNetFrontalier({ salaireBrutMensuel: 5000, paysResidence: 'DE', classe: '1' });
  near(r.netFinalAnnuel, r.netFinalMensuel * 12, 0.05);
});

console.log(`\n${passed} passé(s), ${failed} échec(s)`);
process.exit(failed === 0 ? 0 : 1);

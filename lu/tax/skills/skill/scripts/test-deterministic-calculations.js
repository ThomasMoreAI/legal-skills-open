#!/usr/bin/env node
/**
 * test-deterministic-calculations.js
 * Tests unitaires des calculs déterministes Paperasse Lux.
 *
 * Vérifie que les fonctions de scripts/calc.js produisent des résultats
 * cohérents avec les données luxembourgeoises 2025 (taux IRC 14/16 %,
 * Bëllegen Akt 40 000 €/personne, ICC Lux-Ville, barème IF minimum).
 *
 * Usage : node scripts/test-deterministic-calculations.js
 */

import assert from "node:assert/strict";
import {
  calcIRC,
  calcICC,
  calcMinIF,
  calcBellegenAkt,
  calcTVA,
  calcSuccessionDirect,
} from "./calc.js";

let passed = 0, failed = 0;

function test(name, fn) {
  try { fn(); console.log(`  ✓ ${name}`); passed++; }
  catch (e) { console.error(`  ✗ ${name}\n    ${e.message}`); failed++; }
}

function approxEqual(actual, expected, tol = 0.01) {
  if (Math.abs(actual - expected) > tol) {
    throw new assert.AssertionError({
      message: `Attendu ${expected} ± ${tol}, reçu ${actual}`,
      actual,
      expected,
    });
  }
}

console.log("=== Tests TVA Lux (calcTVA) ===");
test("TVA 17% sur 1000 = 170", () => {
  const r = calcTVA(1000, 17);
  approxEqual(r.tva, 170);
  approxEqual(r.ttc, 1170);
});
test("TVA 8% (intermédiaire) sur 500 = 40", () => approxEqual(calcTVA(500, 8).tva, 40));
test("TVA 3% (super-réduit) sur 200 = 6", () => approxEqual(calcTVA(200, 3).tva, 6));

console.log("\n=== Tests IRC 2025 (calcIRC — loi du 20 décembre 2024) ===");
test("IRC 14% sur petit bénéfice 100 000€", () => {
  const r = calcIRC(100000);
  approxEqual(r.irc, 14000);
  approxEqual(r.contributionChomage, 980); // 7%
  approxEqual(r.total, 14980);
});
test("IRC 16% sur gros bénéfice 500 000€", () => {
  const r = calcIRC(500000);
  approxEqual(r.irc, 80000);
  approxEqual(r.contributionChomage, 5600);
});
test("IRC ramp-up zone 14% × 175k + 31% × delta sur 190 000€", () => {
  const r = calcIRC(190000);
  // 175 000 × 0,14 + 15 000 × 0,31 = 24 500 + 4 650 = 29 150
  approxEqual(r.irc, 29150);
});

console.log("\n=== Tests ICC (calcICC) ===");
test("ICC Lux-Ville (×2,25) sur bénéfice 500 000€ avec abattement PM 17 500€", () => {
  const r = calcICC(500000, 2.25);
  approxEqual(r.base, 482500);
  approxEqual(r.icc, 32568.75);
});
test("ICC commune ×3,5 (ex. Echternach) sur 100 000€", () => {
  const r = calcICC(100000, 3.5);
  approxEqual(r.base, 82500);
  approxEqual(r.icc, 82500 * 0.03 * 3.5);
});

console.log("\n=== Tests IF minimum (calcMinIF — barème 2025 aligné sur data) ===");
test("Bilan 200 000€ -> IF min 535€", () => assert.equal(calcMinIF(200000), 535));
test("Bilan 1 500 000€ -> IF min 1 605€", () => assert.equal(calcMinIF(1500000), 1605));
test("Bilan 12 000 000€ -> IF min 10 700€", () => assert.equal(calcMinIF(12000000), 10700));
test("Bilan 18 000 000€ -> IF min 16 050€", () => assert.equal(calcMinIF(18000000), 16050));
test("Bilan 25 000 000€ -> IF min 21 400€", () => assert.equal(calcMinIF(25000000), 21400));
test("Bilan > 30 000 000€ -> IF min 32 100€", () => assert.equal(calcMinIF(50000000), 32100));

console.log("\n=== Tests Bëllegen Akt (calcBellegenAkt — loi du 22 mai 2024) ===");
test("Acquisition 650 000€ Lux-Ville, 1 acquéreur primo : crédit 40k -> droits nets 25k", () => {
  const r = calcBellegenAkt(650000, 1, true, true);
  approxEqual(r.droitsNominaux, 65000);
  approxEqual(r.abattementBA, 40000);
  approxEqual(r.droitsNets, 25000);
});
test("Acquisition 800 000€ Lux-Ville, couple primo : 0 € de droits (exemple data)", () => {
  const r = calcBellegenAkt(800000, 2, true, true);
  approxEqual(r.droitsNominaux, 80000);
  approxEqual(r.abattementBA, 80000);
  approxEqual(r.droitsNets, 0);
});
test("Acquisition 400 000€ hors Lux-Ville, 1 acquéreur : crédit plafonné aux droits 28k", () => {
  const r = calcBellegenAkt(400000, 1, false, true);
  approxEqual(r.droitsNominaux, 28000); // 7%
  approxEqual(r.abattementBA, 28000);
  approxEqual(r.droitsNets, 0);
});
test("Acquisition 1 200 000€ Lux-Ville, 1 acquéreur non primo : aucun crédit", () => {
  const r = calcBellegenAkt(1200000, 1, true, false);
  approxEqual(r.droitsNominaux, 120000);
  approxEqual(r.abattementBA, 0);
  approxEqual(r.droitsNets, 120000);
});

console.log("\n=== Tests succession ligne directe (calcSuccessionDirect) ===");
test("Succession ligne directe sur biens lux : exonération", () => {
  const r = calcSuccessionDirect(800000, true);
  assert.equal(r.droits, 0);
  assert.equal(r.exoneration, true);
});

console.log(`\n${passed} passés, ${failed} échoués`);
process.exit(failed > 0 ? 1 : 0);

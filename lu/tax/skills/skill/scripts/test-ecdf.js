#!/usr/bin/env node
/**
 * test-ecdf.js — Tests déterministes du générateur eCDF CA-A.
 */

import { readFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { generateECDF, buildECDFData } from '../lib/ecdf/generator.js';

const __dirname = dirname(fileURLToPath(import.meta.url));
const ROOT = join(__dirname, '..');

let passed = 0, failed = 0;
function test(name, fn) {
  try { fn(); console.log(`  ✓ ${name}`); passed++; }
  catch (e) { console.log(`  ✗ ${name}\n      ${e.message}`); failed++; }
}
function eq(a, b, msg) { if (a !== b) throw new Error(`${msg||''}: attendu ${JSON.stringify(b)}, reçu ${JSON.stringify(a)}`); }
function approx(a, b, eps = 0.01) { if (Math.abs(a - b) > eps) throw new Error(`Δ${a} vs ${b} > ${eps}`); }
function truthy(v, msg) { if (!v) throw new Error(msg || 'attendu truthy'); }

const input = JSON.parse(readFileSync(join(ROOT, 'examples/ecdf-input.json'), 'utf8'));
const data = buildECDFData(input);
const xml = generateECDF(input);

console.log('=== Tests eCDF CA-A — structure de données ===');
test('Méta : type formulaire CA-A', () => eq(data.meta.type_formulaire, 'CA-A'));
test('Société propagée', () => eq(data.societe.rcs, 'B999999'));
test('Bilan : 13 rubriques actif (incl. agrégats + total)', () => eq(data.bilan.actif.length, 13));
test('Bilan : 13 rubriques passif (incl. agrégats + total)', () => eq(data.bilan.passif.length, 13));
test('Compte de résultat : 15 rubriques', () => eq(data.compte_resultat.length, 15));

console.log('\n=== Tests calculs ===');
test('CA net (rubrique 3001) = 180 000 €', () => {
  const r = data.compte_resultat.find(x => x.code === '3001');
  approx(r.valeur, 180000);
});
test('Frais de personnel (3017) = 62 000 € (641+645)', () => {
  const r = data.compte_resultat.find(x => x.code === '3017');
  approx(r.valeur, 62000);
});
test('Coût matières (3013) = 75 000 € (604)', () => {
  const r = data.compte_resultat.find(x => x.code === '3013');
  approx(r.valeur, 75000);
});
test('Résultat = produits (180k) - charges (75+12+8+62+1.5+2+11) = 8 500 €', () => {
  approx(data.resultat_calcule, 8500);
});
test('Capital souscrit (1303) = 57 500 € (équilibrage)', () => {
  const r = data.bilan.passif.find(x => x.code === '1303');
  approx(r.valeur, 57500);
});
test('Dettes fiscales/sociales (1561) = 5 000 € (421 + 44)', () => {
  const r = data.bilan.passif.find(x => x.code === '1561');
  approx(r.valeur, 5000);
});
test('Avoirs banque/caisse (1191) = 20 000 €', () => {
  const r = data.bilan.actif.find(x => x.code === '1191');
  approx(r.valeur, 20000);
});
test('Résultat exercice porté au passif (1321) = 8 500 €', () => {
  const r = data.bilan.passif.find(x => x.code === '1321');
  approx(r.valeur, 8500);
});
test('Bilan équilibré (actif - passif < 1 €)', () => {
  truthy(data.coherence.bilan_equilibre, `écart=${data.bilan.ecart}`);
});

console.log('\n=== Tests rendu XML ===');
test('XML : déclaration UTF-8', () => truthy(xml.startsWith('<?xml version="1.0" encoding="UTF-8"?>')));
test('XML : balise racine DeclarationECDF type="CA-A"', () => truthy(xml.includes('<DeclarationECDF type="CA-A"')));
test('XML : RCS présent', () => truthy(xml.includes('<RCS>B999999</RCS>')));
test('XML : section Bilan + Actif + Passif', () => truthy(xml.includes('<Bilan>') && xml.includes('<Actif>') && xml.includes('<Passif>')));
test('XML : balise CompteDeResultat', () => truthy(xml.includes('<CompteDeResultat>')));
test('XML : rubriques Code 3001 (CA net)', () => truthy(xml.includes('code="3001"')));
test('XML : indication équilibre', () => truthy(xml.includes('equilibre="true"')));
test('XML : valeurs formatées 2 décimales', () => truthy(/[<]Valeur[>]\d+\.\d{2}[<]\/Valeur[>]/.test(xml)));

console.log('\n=== Tests cas d\'erreur ===');
test('Refus si RCS manquant', () => {
  let err;
  try { buildECDFData({ societe: {}, exercice: { debut: '2025-01-01', fin: '2025-12-31' }, balance: {} }); }
  catch (e) { err = e; }
  truthy(err, 'devrait lever');
  truthy(err.message.includes('rcs'), 'message doit mentionner rcs');
});
test('Refus si exercice incomplet', () => {
  let err;
  try { buildECDFData({ societe: { rcs: 'B1' }, exercice: {}, balance: {} }); }
  catch (e) { err = e; }
  truthy(err, 'devrait lever');
});

console.log(`\n${passed} passés, ${failed} échoués\n`);
process.exit(failed === 0 ? 0 : 1);

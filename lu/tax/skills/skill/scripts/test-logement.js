#!/usr/bin/env node
/**
 * test-logement.js — Tests Milestone 8 : logement & immobilier.
 */

import { garantieLocativeMax, analyseAcquisition, parcoursLogement } from '../lib/logement/index.js';

let passed = 0, failed = 0;
function test(name, fn) {
  try { fn(); console.log(`  ✓ ${name}`); passed++; }
  catch (e) { console.log(`  ✗ ${name}\n      ${e.message}`); failed++; }
}
function eq(a, b, msg) { if (a !== b) throw new Error(`${msg || ''}: attendu ${JSON.stringify(b)}, reçu ${JSON.stringify(a)}`); }
function truthy(v, msg) { if (!v) throw new Error(msg || 'attendu truthy'); }

console.log('=== Garantie locative ===');

test('garantieLocativeMax renvoie les options en mois de loyer, tracées', () => {
  const g = garantieLocativeMax(1000);
  const m2 = g.options.find((o) => o.mois === 2);
  const m3 = g.options.find((o) => o.mois === 3);
  eq(m2.montant, 2000);
  eq(m3.montant, 3000);
  truthy(g.provenance.source);
  eq(g.provenance.niveauConfiance, 'derive');
});

test('garantieLocativeMax rejette un loyer invalide', () => {
  let ok = false; try { garantieLocativeMax(0); } catch { ok = true; }
  truthy(ok);
});

console.log('=== Acquisition (réutilise lib/bellegen-akt) ===');

test('analyseAcquisition calcule frais et crédit Bëllegen Akt', () => {
  const a = analyseAcquisition({ prix: 600000, nbAcquereurs: 2, luxVille: false });
  truthy(a.frais.total > 0);
  truthy(a.creditBellegenAkt > 0, 'crédit Bëllegen Akt attendu');
  truthy(a.honorairesNotaire > 0);
  truthy(a.provenance.source);
});

test('deux acquéreurs bénéficient d\'un abattement plus élevé qu\'un seul', () => {
  const un = analyseAcquisition({ prix: 600000, nbAcquereurs: 1 });
  const deux = analyseAcquisition({ prix: 600000, nbAcquereurs: 2 });
  truthy(deux.creditBellegenAkt >= un.creditBellegenAkt);
});

console.log('=== Parcours logement ===');

test('parcours locataire : démarches + calcul garantie si loyer fourni', () => {
  const p = parcoursLogement({ statutLogement: 'locataire' }, { loyerMensuel: 1200 });
  eq(p.situation, 'locataire');
  truthy(p.etapes.some((e) => /bail/i.test(e.titre)));
  truthy(p.etapes.some((e) => /garantie/i.test(e.titre)));
  truthy(p.calculs.garantie && p.calculs.garantie.options.length === 2);
});

test('parcours acheteur : démarches + calcul acquisition si prix fourni', () => {
  const p = parcoursLogement({}, { projet: 'achat', prixAchat: 500000, nbAcquereurs: 1, luxVille: true });
  eq(p.situation, 'acheteur');
  truthy(p.etapes.some((e) => /acte notarié/i.test(e.titre)));
  truthy(p.calculs.acquisition && p.calculs.acquisition.fraisTotaux > 0);
});

test('parcours propriétaire : revenus locatifs et impôt foncier', () => {
  const p = parcoursLogement({ statutLogement: 'proprietaire' });
  eq(p.situation, 'proprietaire');
  truthy(p.etapes.some((e) => /revenus locatifs/i.test(e.titre)));
  truthy(p.etapes.some((e) => /foncier/i.test(e.titre)));
});

test('parcours vendeur : ajoute la plus-value immobilière', () => {
  const p = parcoursLogement({}, { projet: 'vente' });
  eq(p.situation, 'vendeur');
  truthy(p.etapes.some((e) => /plus-value/i.test(e.titre)));
});

test('situation indéterminée → avertissement', () => {
  const p = parcoursLogement({});
  eq(p.situation, 'inconnu');
  truthy(p.avertissement);
});

test('chaque étape porte une source', () => {
  const p = parcoursLogement({ statutLogement: 'locataire' }, { loyerMensuel: 1000 });
  for (const e of p.etapes) truthy(e.source && /^https?:\/\//.test(e.source), `étape sans source : ${e.titre}`);
});

console.log(`\n${passed} tests réussis, ${failed} échoués.`);
process.exit(failed === 0 ? 0 : 1);

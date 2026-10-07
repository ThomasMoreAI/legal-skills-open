#!/usr/bin/env node
/**
 * test-residence.js — Tests Milestone 7 : parcours « Je m'installe au Luxembourg ».
 */

import {
  chargerInstallation, classeNationalite, parcoursInstallation, PHASES_INSTALLATION,
} from '../lib/residence/index.js';

let passed = 0, failed = 0;
function test(name, fn) {
  try { fn(); console.log(`  ✓ ${name}`); passed++; }
  catch (e) { console.log(`  ✗ ${name}\n      ${e.message}`); failed++; }
}
function eq(a, b, msg) { if (a !== b) throw new Error(`${msg || ''}: attendu ${JSON.stringify(b)}, reçu ${JSON.stringify(a)}`); }
function truthy(v, msg) { if (!v) throw new Error(msg || 'attendu truthy'); }

console.log('=== Données & nationalité ===');

test('le catalogue d\'étapes se charge et chaque étape est sourcée', () => {
  const { etapes, as_of } = chargerInstallation();
  truthy(as_of);
  truthy(etapes.length >= 1);
  for (const e of etapes) truthy(e.source && /^https?:\/\//.test(e.source), `étape ${e.id} sans source`);
});

test('classeNationalite distingue UE / hors UE / inconnu', () => {
  eq(classeNationalite({ nationalite: 'FR' }), 'ue');
  eq(classeNationalite({ nationalite: 'US' }), 'hors_ue');
  eq(classeNationalite({}), 'inconnu');
});

console.log('=== Parcours UE ===');

const ue = parcoursInstallation({ nationalite: 'FR', dateArriveeLux: '2026-03-01' }, { aujourdhui: '2026-07-13' });

test('un ressortissant UE ne voit pas les étapes réservées hors UE', () => {
  const ids = ue.chronologie.map((e) => e.id);
  truthy(ids.includes('enregistrement_ue'));
  eq(ids.includes('titre_sejour'), false);
  eq(ids.includes('renouvellement_titre'), false);
});

test('les phases sont ordonnées chronologiquement', () => {
  const phases = ue.chronologie.map((e) => PHASES_INSTALLATION.indexOf(e.phase));
  const trie = [...phases].sort((a, b) => a - b);
  eq(JSON.stringify(phases), JSON.stringify(trie));
});

test('les échéances indicatives sont calculées depuis la date d\'arrivée', () => {
  const declaration = ue.chronologie.find((e) => e.id === 'declaration_arrivee_commune');
  eq(declaration.echeanceIndicative, '2026-03-08'); // arrivée + 7 jours (première semaine)
});

console.log('=== Parcours hors UE ===');

const horsUe = parcoursInstallation({ nationalite: 'US', dateArriveeLux: '2026-03-01' });

test('un ressortissant hors UE voit le titre de séjour et son renouvellement', () => {
  const ids = horsUe.chronologie.map((e) => e.id);
  truthy(ids.includes('titre_sejour'));
  truthy(ids.includes('renouvellement_titre'));
  eq(ids.includes('enregistrement_ue'), false);
});

console.log('=== Conditions & avertissements ===');

test('l\'étape véhicule n\'apparaît que si le profil déclare un véhicule', () => {
  const sans = parcoursInstallation({ nationalite: 'FR', dateArriveeLux: '2026-03-01' });
  eq(sans.chronologie.some((e) => e.id === 'immatriculation_vehicule'), false);
  const avec = parcoursInstallation({ nationalite: 'FR', dateArriveeLux: '2026-03-01', vehicules: ['AB1234'] });
  truthy(avec.chronologie.some((e) => e.id === 'immatriculation_vehicule'));
});

test('nationalité inconnue → avertissement et étapes à préciser', () => {
  const p = parcoursInstallation({ dateArriveeLux: '2026-03-01' });
  truthy(p.avertissement && /nationalité/i.test(p.avertissement));
  truthy(p.chronologie.some((e) => e.aPreciser));
});

test('sans date d\'arrivée, pas d\'échéance indicative mais un avertissement', () => {
  const p = parcoursInstallation({ nationalite: 'FR' });
  eq(p.chronologie[0].echeanceIndicative, null);
  truthy(p.avertissement);
});

console.log(`\n${passed} tests réussis, ${failed} échoués.`);
process.exit(failed === 0 ? 0 : 1);

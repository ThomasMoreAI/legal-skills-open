#!/usr/bin/env node
/**
 * test-evaluation.js — Tests de la couche qualité, explicabilité & observabilité.
 */

import { createMission, advanceMission } from '../lib/workflows/index.js';
import { evaluerMission, traceMission } from '../lib/evaluation/index.js';
import { creerMemoire, ajouter } from '../lib/memoire/index.js';

let passed = 0, failed = 0;
function test(name, fn) {
  try { fn(); console.log(`  ✓ ${name}`); passed++; }
  catch (e) { console.log(`  ✗ ${name}\n      ${e.message}`); failed++; }
}
function eq(a, b, msg) { if (a !== b) throw new Error(`${msg || ''}: attendu ${JSON.stringify(b)}, reçu ${JSON.stringify(a)}`); }
function truthy(v, msg) { if (!v) throw new Error(msg || 'attendu truthy'); }

const REF = '2026-07-13';
const missionInstallation = () => createMission('Installation au Luxembourg', { evenements: ['arrivee_luxembourg'], aujourdhui: REF });

console.log('=== Rapport d\'évaluation ===');

test('produit un rapport avec confiance, hypothèses, risques, manquants, sources', () => {
  const r = evaluerMission(missionInstallation(), { profil: { situationFamiliale: 'marie' }, aujourdhui: REF });
  truthy(typeof r.confianceGlobale === 'number' && r.confianceGlobale >= 0 && r.confianceGlobale <= 100);
  truthy(Array.isArray(r.informationsManquantes) && r.informationsManquantes.length >= 1);
  truthy(r.hypotheses.length >= 1);
  truthy(Array.isArray(r.risques));
  truthy(r.sources.length >= 1);
});

test('les hypothèses reflètent les défauts non confirmés', () => {
  const r = evaluerMission(missionInstallation(), { profil: { situationFamiliale: 'marie' }, aujourdhui: REF });
  truthy(r.hypotheses.some((h) => /résidence principale/i.test(h)));
  truthy(r.hypotheses.some((h) => /conjoint/i.test(h)));
});

test('un document déjà fourni disparaît des informations manquantes', () => {
  const m = missionInstallation();
  const avant = evaluerMission(m, { aujourdhui: REF }).informationsManquantes.length;
  const mem = creerMemoire({ consentementRGPD: true });
  ajouter(mem, 'documents', { nom: 'Contrat de travail' }, { quand: REF });
  const apres = evaluerMission(m, { memoire: mem, aujourdhui: REF }).informationsManquantes.length;
  truthy(apres < avant, 'le contrat de travail aurait dû sortir des manquants');
});

test('les points bloquants remontent les prérequis non satisfaits', () => {
  const m = createMission('Créer une société', { evenements: ['creation_entreprise'], aujourdhui: REF });
  const r = evaluerMission(m, { aujourdhui: REF });
  truthy(r.pointsBloquants.some((p) => /immatriculation au rcs/i.test(p)), 'le RCS devrait être bloqué par l\'autorisation');
  eq(r.complete, false);
});

test('la confiance monte quand les blocages se lèvent', () => {
  const m = createMission('Créer une société', { evenements: ['creation_entreprise'], aujourdhui: REF });
  const avant = evaluerMission(m, { aujourdhui: REF }).confianceGlobale;
  let garde = 0;
  while (evaluerMission(m, { aujourdhui: REF }).avancement.pourcentage < 100 && garde < 50) { advanceMission(m, { date: REF }); garde++; }
  const r = evaluerMission(m, { aujourdhui: REF });
  eq(r.complete, true);
  eq(r.pointsBloquants.length, 0);
  truthy(r.confianceGlobale >= avant);
});

console.log('=== Trace d\'exécution (observabilité) ===');

test('la trace suit événement → règle → obligation → étape → connecteur', () => {
  const t = traceMission(missionInstallation(), { aujourdhui: REF });
  const phases = new Set(t.map((x) => x.phase));
  truthy(phases.has('evenement_detecte'));
  truthy(phases.has('regle_appliquee'));
  truthy(phases.has('obligation_creee'));
  truthy(phases.has('etape_ajoutee'));
  truthy(phases.has('connecteur_selectionne'));
});

test('la trace relie les règles à leurs sources', () => {
  const t = traceMission(missionInstallation(), { aujourdhui: REF });
  truthy(t.filter((x) => x.phase === 'regle_appliquee').some((x) => x.source));
});

test('l\'événement détecté précède l\'étape ajoutée', () => {
  const t = traceMission(missionInstallation(), { aujourdhui: REF });
  const iEv = t.findIndex((x) => x.phase === 'evenement_detecte');
  const iEt = t.findIndex((x) => x.phase === 'etape_ajoutee');
  truthy(iEv >= 0 && iEt > iEv);
});

console.log(`\n${passed} tests réussis, ${failed} échoués.`);
process.exit(failed === 0 ? 0 : 1);

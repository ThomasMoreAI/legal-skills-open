#!/usr/bin/env node
/**
 * test-workflows.js — Tests du Workflow Engine & Missions.
 */

import {
  createMission, prochaineEtape, avancement, advanceMission, definirTypeAction,
  pauseMission, resumeMission, completeMission, reessayerEtape,
  creerRegistreConnecteurs, serialiser, deserialiser, TYPES_ACTION,
} from '../lib/workflows/index.js';

let passed = 0, failed = 0;
function test(name, fn) {
  try { fn(); console.log(`  ✓ ${name}`); passed++; }
  catch (e) { console.log(`  ✗ ${name}\n      ${e.message}`); failed++; }
}
function eq(a, b, msg) { if (a !== b) throw new Error(`${msg || ''}: attendu ${JSON.stringify(b)}, reçu ${JSON.stringify(a)}`); }
function truthy(v, msg) { if (!v) throw new Error(msg || 'attendu truthy'); }

const REF = '2026-07-13';
const mission = () => createMission('Créer une société', { evenements: ['creation_entreprise'], aujourdhui: REF });

console.log('=== Création de mission ===');

test('une mission naît des événements avec des étapes ordonnées', () => {
  const m = mission();
  eq(m.statut, 'active');
  truthy(m.etapes.length >= 4);
  eq(m.etapes[0].nom, 'Autorisation d\'établissement');
  eq(avancement(m).pourcentage, 0);
});

test('les dépendances sont portées par les étapes', () => {
  const m = mission();
  const rcs = m.etapes.find((e) => /immatriculation au rcs/i.test(e.nom));
  truthy(rcs.dependances.length >= 1);
});

console.log('=== Dépendances & avancement ===');

test('une étape à prérequis non satisfait n\'est pas proposée', () => {
  const m = mission();
  const rcs = m.etapes.find((e) => /immatriculation au rcs/i.test(e.nom));
  truthy(prochaineEtape(m).id !== rcs.id, 'le RCS ne doit pas passer avant l\'autorisation');
});

test('recommandation : avancer marque fait et fait progresser', () => {
  const m = mission();
  const r = advanceMission(m, { date: REF });
  eq(r.action, 'recommandation');
  eq(r.etape.statut, 'fait');
  truthy(avancement(m).pourcentage > 0);
});

test('on peut dérouler toute la mission dans l\'ordre des dépendances', () => {
  const m = mission();
  let garde = 0;
  while (avancement(m).pourcentage < 100 && garde < 50) { advanceMission(m, { date: REF }); garde++; }
  eq(avancement(m).pourcentage, 100);
  // l'autorisation a été faite avant le RCS
  const idxAut = m.historique.filter((h) => h.evenement === 'recommandation').findIndex((h) => h.details === 'obl_autorisation_etablissement');
  const idxRcs = m.historique.filter((h) => h.evenement === 'recommandation').findIndex((h) => h.details === 'rcs_immatriculation');
  truthy(idxAut < idxRcs);
});

console.log('=== Préparation (validation utilisateur) ===');

test('une étape de préparation attend la validation', () => {
  const m = mission();
  definirTypeAction(m, m.etapes[0].id, 'preparation');
  const r1 = advanceMission(m, { date: REF });
  eq(r1.besoinValidation, true);
  eq(r1.etape.statut, 'en_attente_validation');
  const r2 = advanceMission(m, { date: REF });        // sans valider
  eq(r2.besoinValidation, true);
  const r3 = advanceMission(m, { valider: true, date: REF });
  eq(r3.action, 'validee');
  eq(r3.etape.statut, 'fait');
});

console.log('=== Exécution (confirmation explicite + connecteur) ===');

test('une exécution exige une confirmation explicite', () => {
  const m = mission();
  definirTypeAction(m, m.etapes[0].id, 'execution');
  const r1 = advanceMission(m, { date: REF });
  eq(r1.besoinConfirmation, true);
  eq(r1.etape.statut, 'a_faire');                     // rien n'a été fait
});

test('le connecteur « manuel » ne transmet rien à l\'extérieur', () => {
  const m = mission();
  definirTypeAction(m, m.etapes[0].id, 'execution');
  const r = advanceMission(m, { confirmerExecution: true, date: REF });
  eq(r.action, 'execution');
  eq(r.resultat.envoye, false);
  eq(r.etape.statut, 'fait');
});

test('un connecteur personnalisé (plugin) est utilisé sans modifier le moteur', () => {
  const registre = creerRegistreConnecteurs();
  let appele = false;
  registre.enregistrer({ id: 'guichet-test', disponible: true, executer: () => { appele = true; return { envoye: true, ref: 'ABC123' }; } });
  const m = mission();
  definirTypeAction(m, m.etapes[0].id, 'execution', { connecteur: 'guichet-test' });
  const r = advanceMission(m, { confirmerExecution: true, registre, date: REF });
  truthy(appele);
  eq(r.resultat.ref, 'ABC123');
});

test('une exécution en échec bloque la suite et peut être réessayée', () => {
  const registre = creerRegistreConnecteurs();
  registre.enregistrer({ id: 'ko', disponible: true, executer: () => ({ echec: true, message: 'portail indisponible' }) });
  const m = mission();
  definirTypeAction(m, m.etapes[0].id, 'execution', { connecteur: 'ko' });
  const r = advanceMission(m, { confirmerExecution: true, registre, date: REF });
  eq(r.etape.statut, 'echec');
  reessayerEtape(m, m.etapes[0].id, { date: REF });
  eq(m.etapes[0].statut, 'a_faire');
});

console.log('=== Pause / reprise / clôture ===');

test('pause puis reprise (après interruption, via JSON)', () => {
  const m = mission();
  advanceMission(m, { date: REF });
  pauseMission(m, { date: REF });
  eq(m.statut, 'en_pause');
  let ok = false; try { advanceMission(m, { date: REF }); } catch { ok = true; }
  truthy(ok, 'une mission en pause ne doit pas avancer');
  const repris = resumeMission(serialiser(m), { date: REF });
  eq(repris.statut, 'active');
  truthy(deserialiser(serialiser(repris)).etapes.length === m.etapes.length);
});

test('completeMission refuse tant que tout n\'est pas fait, sauf force', () => {
  const m = mission();
  let ok = false; try { completeMission(m, { date: REF }); } catch { ok = true; }
  truthy(ok);
  completeMission(m, { force: true, date: REF });
  eq(m.statut, 'terminee');
});

test('TYPES_ACTION expose les trois types', () => {
  eq(JSON.stringify(TYPES_ACTION), JSON.stringify(['recommandation', 'preparation', 'execution']));
});

console.log(`\n${passed} tests réussis, ${failed} échoués.`);
process.exit(failed === 0 ? 0 : 1);

#!/usr/bin/env node
/**
 * test-rappels.js — Tests Milestone 10 : calendrier, rappels & surveillance.
 */

import {
  niveauAlerte, genererRappels, calendrierDossiers, prochainesEcheances,
  filtrerParStatut, prochainRappel, STATUTS, COULEURS,
} from '../lib/rappels/index.js';

let passed = 0, failed = 0;
function test(name, fn) {
  try { fn(); console.log(`  ✓ ${name}`); passed++; }
  catch (e) { console.log(`  ✗ ${name}\n      ${e.message}`); failed++; }
}
function eq(a, b, msg) { if (a !== b) throw new Error(`${msg || ''}: attendu ${JSON.stringify(b)}, reçu ${JSON.stringify(a)}`); }
function truthy(v, msg) { if (!v) throw new Error(msg || 'attendu truthy'); }

const REF = '2026-07-13';
const d = (echeance, statut = 'a_preparer', extra = {}) => ({ id: `dos_${echeance || 'x'}`, typeDemarche: 'Test', echeance, statut, ...extra });

console.log('=== Niveau d\'alerte (couleurs) ===');

test('échéance dépassée → rouge', () => eq(niveauAlerte(d('2026-07-01'), REF).couleur, 'rouge'));
test('échéance dans 3 jours → orange', () => eq(niveauAlerte(d('2026-07-16'), REF).couleur, 'orange'));
test('échéance dans 20 jours → jaune', () => eq(niveauAlerte(d('2026-08-02'), REF).couleur, 'jaune'));
test('échéance dans 60 jours → neutre', () => eq(niveauAlerte(d('2026-09-11'), REF).couleur, 'neutre'));
test('dossier terminé → vert', () => eq(niveauAlerte(d('2026-07-01', 'termine'), REF).couleur, 'vert'));
test('sans échéance et en retard → rouge', () => eq(niveauAlerte(d(null, 'en_retard'), REF).couleur, 'rouge'));
test('joursRestants est calculé', () => eq(niveauAlerte(d('2026-07-16'), REF).joursRestants, 3));

console.log('=== Génération de rappels ===');

const dossiers = [
  d('2026-07-01'),                                   // rouge (en retard)
  d('2026-07-16'),                                   // orange
  d('2026-08-02'),                                   // jaune
  d('2026-12-31'),                                   // neutre
  d('2026-07-20', 'termine'),                        // exclu
  d('2026-07-18', 'a_preparer', { informationsManquantes: ['numéro TVA'] }),
];

test('les rappels excluent les dossiers terminés', () => {
  const r = genererRappels(dossiers, { aujourdhui: REF });
  eq(r.some((x) => x.statut === 'termine'), false);
});

test('les rappels sont triés du plus urgent au moins urgent', () => {
  const r = genererRappels(dossiers, { aujourdhui: REF });
  eq(r[0].couleur, 'rouge');
  const rangs = r.map((x) => ['rouge', 'orange', 'jaune', 'neutre', 'vert'].indexOf(x.couleur));
  eq(JSON.stringify(rangs), JSON.stringify([...rangs].sort((a, b) => a - b)));
});

test('un dossier en retard génère un message explicite', () => {
  const r = genererRappels([d('2026-07-01')], { aujourdhui: REF });
  truthy(/en retard/i.test(r[0].messages.join(' ')));
  eq(r[0].actionRequise, true);
});

test('les informations manquantes déclenchent un rappel', () => {
  const r = genererRappels([d('2026-08-30', 'a_preparer', { informationsManquantes: ['RIB'] })], { aujourdhui: REF });
  truthy(/informations manquantes/i.test(r[0].messages.join(' ')));
});

test('les documents requis non reçus déclenchent un rappel', () => {
  const r = genererRappels([d('2026-08-30', 'a_preparer', { documentsRequis: ['Contrat de bail'], documentsRecus: [] })], { aujourdhui: REF });
  truthy(/documents à fournir/i.test(r[0].messages.join(' ')));
});

console.log('=== Calendrier & filtres ===');

test('calendrierDossiers groupe par couleur et trie chronologiquement', () => {
  const cal = calendrierDossiers(dossiers, { aujourdhui: REF });
  eq(cal.compteurs.rouge, 1);
  eq(cal.compteurs.vert, 1);
  const dates = cal.chronologie.map((x) => x.echeance);
  eq(JSON.stringify(dates), JSON.stringify([...dates].sort()));
});

test('prochainesEcheances filtre sur une fenêtre de jours', () => {
  const p = prochainesEcheances(dossiers, { aujourdhui: REF, dans: 10 });
  truthy(p.every((x) => x.joursRestants <= 10));
  truthy(p.some((x) => x.echeance === '2026-07-16'));
});

test('filtrerParStatut valide le statut', () => {
  eq(filtrerParStatut(dossiers, 'termine').length, 1);
  let ok = false; try { filtrerParStatut(dossiers, 'bidon'); } catch { ok = true; }
  truthy(ok);
});

test('prochainRappel = échéance moins le préavis', () => {
  eq(prochainRappel(d('2026-07-20'), { preavisJours: 7 }), '2026-07-13');
});

test('STATUTS et COULEURS sont exposés', () => {
  truthy(STATUTS.includes('en_retard'));
  truthy(COULEURS.rouge && COULEURS.vert);
});

console.log(`\n${passed} tests réussis, ${failed} échoués.`);
process.exit(failed === 0 ? 0 : 1);

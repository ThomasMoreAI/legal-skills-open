#!/usr/bin/env node
/**
 * test-orchestration.js — Tests de la couche d'orchestration :
 * extraction (LLM→graphe), mémoire utilisateur, moteur de planification.
 */

import { validerExtraction, ingererExtraction, entitesVersProfil } from '../lib/extraction/index.js';
import { creerMemoire, ajouter, fusionnerProfil, marquerRealisee, estRealisee, questionsAEviter } from '../lib/memoire/index.js';
import { planifier } from '../lib/planification/index.js';

let passed = 0, failed = 0;
function test(name, fn) {
  try { fn(); console.log(`  ✓ ${name}`); passed++; }
  catch (e) { console.log(`  ✗ ${name}\n      ${e.message}`); failed++; }
}
function eq(a, b, msg) { if (a !== b) throw new Error(`${msg || ''}: attendu ${JSON.stringify(b)}, reçu ${JSON.stringify(a)}`); }
function truthy(v, msg) { if (!v) throw new Error(msg || 'attendu truthy'); }
const ordre = (plan, motif) => (plan.demarches.find((d) => motif.test(d.nom)) || {}).ordre;

const REF = '2026-07-13';

console.log('=== Extraction (frontière LLM → graphe) ===');

test('validerExtraction rejette une structure invalide', () => {
  eq(validerExtraction({}).valide, false);
  eq(validerExtraction({ events: ['x'], confidence: 2 }).valide, false);
  eq(validerExtraction({ events: [] }).valide, true);
});

test('entitesVersProfil mappe enfants, emploi et chronologie', () => {
  const p = entitesVersProfil({ children: 2, employment: { user: 'Luxembourg', spouse: 'France' }, timeline: { move: '2026-09' } });
  eq(p.nombreEnfants, 2);
  eq(p.paysEmployeur, 'LU');
  eq(p.dateArriveeLux, '2026-09-01');
  eq(p.conjointTravailleEtranger, 'France');
});

test('ingererExtraction résout les événements (id + texte libre) et signale les inconnus', () => {
  const r = ingererExtraction({ events: ['arrivee_luxembourg', 'je viens d\'avoir un enfant', 'blabla'], entities: { children: 2 }, confidence: 0.96 });
  truthy(r.evenements.includes('arrivee_luxembourg'));
  truthy(r.evenements.includes('naissance'));
  truthy(r.inconnus.includes('blabla'));
  eq(r.aValider, false);
  eq(r.profil.nombreEnfants, 2);
});

test('confiance faible → à valider', () => {
  eq(ingererExtraction({ events: ['naissance'], confidence: 0.3 }).aValider, true);
});

console.log('=== Mémoire utilisateur ===');

test('creerMemoire exige le consentement', () => {
  let ok = false; try { creerMemoire({ consentementRGPD: false }); } catch { ok = true; }
  truthy(ok);
  const m = creerMemoire({ consentementRGPD: true, prenom: 'Greg' });
  truthy(Array.isArray(m.employeurs) && Array.isArray(m.obligationsRealisees));
});

test('ajouter, fusionner, marquer réalisée et éviter les questions', () => {
  const m = creerMemoire({ consentementRGPD: true });
  ajouter(m, 'societes', { nom: 'Acme SARL' }, { quand: REF });
  fusionnerProfil(m, { situationFamiliale: 'marie', nombreEnfants: 2 }, { quand: REF });
  eq(m.societes.length, 1);
  truthy(questionsAEviter(m).has('situationFamiliale'));
  marquerRealisee(m, 'obl_autorisation_etablissement', { quand: REF });
  eq(estRealisee(m, 'obl_autorisation_etablissement'), true);
  truthy(m.historique.length >= 3);
});

console.log('=== Planification multi-événements ===');

const PLAN = planifier(['arrivee_luxembourg', 'naissance', 'creation_entreprise'], { aujourdhui: REF });

test('fusionne les démarches des 3 événements en un plan', () => {
  truthy(PLAN.total >= 8);
  truthy(/Commencer par/.test(PLAN.resume));
});

test('respecte les dépendances : autorisation → RCS → TVA', () => {
  truthy(ordre(PLAN, /autorisation d'établissement/i) < ordre(PLAN, /immatriculation au rcs/i));
  truthy(ordre(PLAN, /immatriculation au rcs/i) < ordre(PLAN, /immatriculation tva/i));
});

test('déclaration d\'arrivée avant la déclaration d\'impôt', () => {
  truthy(ordre(PLAN, /arrivée à la commune/i) < ordre(PLAN, /impôt sur le revenu/i));
});

test('déclaration de naissance avant l\'affiliation CNS de l\'enfant', () => {
  truthy(ordre(PLAN, /naissance à l'état civil/i) < ordre(PLAN, /affiliation de l'enfant à la cns/i));
});

test('détecte les documents mutualisés (pièce d\'identité partagée)', () => {
  truthy(PLAN.documentsMutualises.length >= 1);
  truthy(PLAN.documentsMutualises.some((d) => d.count >= 2));
});

test('chaque étape est expliquée (déclencheur + ce qu\'elle débloque)', () => {
  const debloqueur = PLAN.demarches.find((d) => d.debloque.length);
  truthy(debloqueur && /Débloque/.test(debloqueur.explication));
  truthy(PLAN.demarches.every((d) => d.declenchePar.length >= 1));
});

test('la mémoire exclut une démarche déjà réalisée', () => {
  const m = creerMemoire({ consentementRGPD: true });
  marquerRealisee(m, 'obl_autorisation_etablissement', { quand: REF });
  const plan = planifier(['creation_entreprise'], { aujourdhui: REF, memoire: m });
  eq(plan.demarches.some((d) => /autorisation d'établissement/i.test(d.nom)), false);
});

console.log(`\n${passed} tests réussis, ${failed} échoués.`);
process.exit(failed === 0 ? 0 : 1);

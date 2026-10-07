#!/usr/bin/env node
/**
 * test-reasoning.js — Tests du moteur de raisonnement & Change Impact.
 */

import {
  computeDelta, evenementsPourDelta, computeImpact, simulateScenario, explainReasoning, transition,
} from '../lib/reasoning/index.js';

let passed = 0, failed = 0;
function test(name, fn) {
  try { fn(); console.log(`  ✓ ${name}`); passed++; }
  catch (e) { console.log(`  ✗ ${name}\n      ${e.message}`); failed++; }
}
function eq(a, b, msg) { if (a !== b) throw new Error(`${msg || ''}: attendu ${JSON.stringify(b)}, reçu ${JSON.stringify(a)}`); }
function truthy(v, msg) { if (!v) throw new Error(msg || 'attendu truthy'); }

const REF = '2026-07-13';

console.log('=== Delta ===');

test('computeDelta identifie les champs modifiés', () => {
  const d = computeDelta({ situationFamiliale: 'celibataire', x: 1 }, { situationFamiliale: 'marie', x: 1 });
  eq(d.length, 1);
  eq(d[0].champ, 'situationFamiliale');
  eq(d[0].apres, 'marie');
});

test('evenementsPourDelta mappe un changement à un événement', () => {
  truthy(evenementsPourDelta([{ champ: 'situationFamiliale', avant: 'celibataire', apres: 'marie' }]).includes('mariage_partenariat'));
  truthy(evenementsPourDelta([{ champ: 'formeJuridique', avant: null, apres: 'SARL' }]).includes('creation_entreprise'));
});

console.log('=== computeImpact (propagation) ===');

test('« Je me marie » change la classe d\'impôt (1 → 2) avec source', () => {
  const imp = computeImpact({ situationFamiliale: 'celibataire', statutProfessionnel: 'salarie' }, { situationFamiliale: 'marie' }, { aujourdhui: REF });
  const classe = imp.valeursModifiees.find((v) => v.nom === 'classe_impot');
  truthy(classe, 'classe d\'impôt non impactée');
  eq(classe.avant, '1'); eq(classe.apres, '2');
  truthy(classe.source);
  truthy(imp.evenementsAssocies.includes('mariage_partenariat'));
  truthy(imp.domainesImpactes.length >= 1);
});

test('« Je m\'installe » (arrivée) fait apparaître la déclaration d\'arrivée', () => {
  const imp = computeImpact({ statutProfessionnel: 'salarie' }, { dateArriveeLux: '2026-09-01', paysResidence: 'LU' }, { aujourdhui: REF });
  truthy(imp.obligations.ajoutees.some((o) => o.id === 'obl_commune_declaration_arrivee'));
  truthy(imp.evenementsAssocies.includes('arrivee_luxembourg'));
});

test('« Je crée une société » fait apparaître plusieurs obligations, avec cause', () => {
  const imp = computeImpact({}, { statut: 'actif', formeJuridique: 'SARL' }, { aujourdhui: REF });
  truthy(imp.obligations.ajoutees.some((o) => o.id === 'obl_autorisation_etablissement'));
  const autorisation = imp.obligations.ajoutees.find((o) => o.id === 'obl_autorisation_etablissement');
  truthy(autorisation.cause.length >= 1, 'cause de déclenchement absente');
  truthy(imp.total >= 2);
});

console.log('=== simulateScenario (sans mutation) ===');

test('un scénario hypothétique ne modifie pas l\'état de base', () => {
  const etat = { situationFamiliale: 'celibataire' };
  const res = simulateScenario(etat, { changements: { situationFamiliale: 'marie' }, libelle: 'Et si je me mariais ?' }, { aujourdhui: REF });
  eq(res.hypothetique, true);
  eq(etat.situationFamiliale, 'celibataire', 'l\'état de base a été muté !');
  truthy(res.impact.valeursModifiees.length >= 1);
});

test('un scénario d\'événements produit un plan', () => {
  const res = simulateScenario({}, { evenements: ['creation_entreprise'], libelle: 'Et si je créais une société ?' }, { aujourdhui: REF });
  truthy(res.plan && res.plan.total >= 1);
});

console.log('=== explainReasoning (traçable) ===');

test('chaque conclusion est reliée à une cause et une source', () => {
  const imp = computeImpact({ situationFamiliale: 'celibataire', statutProfessionnel: 'salarie' }, { situationFamiliale: 'marie' }, { aujourdhui: REF });
  const expl = explainReasoning(imp);
  truthy(expl.length >= 1);
  truthy(expl.every((e) => e.conclusion && e.cause));
  truthy(expl.some((e) => e.source));
});

console.log('=== transition (machine à états) ===');

test('transition renvoie ancien/nouvel état, date et impact', () => {
  const t = transition({ paysResidence: 'FR' }, { paysResidence: 'LU', dateArriveeLux: '2026-09-01' }, { date: REF, aujourdhui: REF });
  eq(t.ancienEtat.paysResidence, 'FR');
  eq(t.nouvelEtat.paysResidence, 'LU');
  eq(t.date, REF);
  truthy(t.impact && typeof t.impact.total === 'number');
});

console.log(`\n${passed} tests réussis, ${failed} échoués.`);
process.exit(failed === 0 ? 0 : 1);

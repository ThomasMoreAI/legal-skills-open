#!/usr/bin/env node
/**
 * test-conversation.js — Tests Milestone 14 : intelligence conversationnelle.
 */

import { classifierIntention, repondre, INTENTIONS } from '../lib/conversation/index.js';

let passed = 0, failed = 0;
function test(name, fn) {
  try { fn(); console.log(`  ✓ ${name}`); passed++; }
  catch (e) { console.log(`  ✗ ${name}\n      ${e.message}`); failed++; }
}
function eq(a, b, msg) { if (a !== b) throw new Error(`${msg || ''}: attendu ${JSON.stringify(b)}, reçu ${JSON.stringify(a)}`); }
function truthy(v, msg) { if (!v) throw new Error(msg || 'attendu truthy'); }

const REF = '2026-07-13';

console.log('=== Classification d\'intention ===');

test('reconnaît les intentions clés', () => {
  eq(classifierIntention('J\'ai reçu cette lettre, qu\'est-ce que je dois faire ?'), 'analyser_courrier');
  eq(classifierIntention('Est-ce que je dois faire une déclaration de TVA ?'), 'tva');
  eq(classifierIntention('Qu\'est-ce qu\'il me manque pour créer ma société ?'), 'creer_societe');
  eq(classifierIntention('Je suis frontalier français et je télétravaille deux jours par semaine'), 'frontalier');
  eq(classifierIntention('Je viens d\'acheter un appartement'), 'achat_immobilier');
  eq(classifierIntention('Ma société n\'a pas déposé ses comptes'), 'comptes_non_deposes');
  eq(classifierIntention('Je veux arrêter mon activité'), 'cessation');
});

test('repli sur diagnostic si intention floue', () => {
  eq(classifierIntention('bonjour'), 'diagnostic');
});

console.log('=== Réponses (toujours avec disclaimer) ===');

test('chaque réponse rappelle qu\'aucune démarche n\'a été effectuée', () => {
  const r = repondre('Quelles sont mes obligations ?', { profil: { statutProfessionnel: 'independant' }, aujourdhui: REF });
  truthy(/aucune démarche/i.test(r.disclaimer));
});

test('TVA : réponse ciblée avec sources', () => {
  const r = repondre('Dois-je faire une déclaration de TVA ?', {
    profil: { regimeTVA: 'normal', frequenceTVA: 'mensuelle', statut: 'actif' }, aujourdhui: REF,
  });
  eq(r.intention, 'tva');
  truthy(r.obligations.some((o) => /tva/i.test(o.nom)));
  truthy(r.sources.length >= 1);
});

test('frontalier avec télétravail au-dessus du seuil → alerte', () => {
  const r = repondre('Je suis frontalier et je télétravaille beaucoup', {
    profil: { paysResidence: 'FR', joursHorsLU: 40 }, aujourdhui: REF,
  });
  eq(r.intention, 'frontalier');
  truthy(/seuil/i.test(r.action));
});

test('courrier sans texte → demande le document', () => {
  const r = repondre('J\'ai reçu cette lettre de l\'AED', { aujourdhui: REF });
  eq(r.intention, 'analyser_courrier');
  truthy(r.prochaineQuestion);
});

test('courrier avec texte → analyse et checklist', () => {
  const txt = 'Administration de l\'Enregistrement, des Domaines et de la TVA (AED)\nObjet : Déclaration de TVA manquante — période T1 2026\nVeuillez faire parvenir la déclaration au plus tard le 30/06/2026.';
  const r = repondre('J\'ai reçu ce courrier, que faire ?', { texteDocument: txt, aujourdhui: REF });
  eq(r.intention, 'analyser_courrier');
  truthy(r.comprehension && r.checklist.length >= 1);
});

test('création de société → obligations et action de parcours', () => {
  const r = repondre('Qu\'est-ce qu\'il me manque pour créer ma société ?', { profil: {}, aujourdhui: REF });
  eq(r.intention, 'creer_societe');
  truthy(/autorisation|rcs|parcours/i.test(r.action));
  truthy(r.obligations.length >= 1);
});

test('installation → parcours chronologique et sources', () => {
  const r = repondre('Je viens d\'arriver au Luxembourg', { profil: { nationalite: 'FR', dateArriveeLux: '2026-06-01' }, aujourdhui: REF });
  eq(r.intention, 'installation');
  truthy(r.checklist.length >= 1);
  truthy(r.sources.length >= 1);
});

test('l\'assistant demande les informations manquantes', () => {
  const r = repondre('Quelles sont mes obligations ?', { profil: {}, aujourdhui: REF });
  truthy(r.prochaineQuestion, 'aucune question de clarification proposée');
});

test('INTENTIONS est exposé', () => truthy(INTENTIONS.length >= 8));

console.log(`\n${passed} tests réussis, ${failed} échoués.`);
process.exit(failed === 0 ? 0 : 1);

#!/usr/bin/env node
/**
 * test-evenements.js — Tests de l'ontologie des événements de vie.
 */

import {
  chargerEvenements, listerEvenements, identifierEvenement, resoudreEvenement, verifierIntegrite,
} from '../lib/evenements/index.js';
import { chargerSources } from '../lib/connaissances/index.js';

let passed = 0, failed = 0;
function test(name, fn) {
  try { fn(); console.log(`  ✓ ${name}`); passed++; }
  catch (e) { console.log(`  ✗ ${name}\n      ${e.message}`); failed++; }
}
function eq(a, b, msg) { if (a !== b) throw new Error(`${msg || ''}: attendu ${JSON.stringify(b)}, reçu ${JSON.stringify(a)}`); }
function truthy(v, msg) { if (!v) throw new Error(msg || 'attendu truthy'); }

const REF = '2026-07-13';

console.log('=== Données & intégrité du graphe ===');

test('chaque événement est sourcé et complet', () => {
  const { evenements, as_of } = chargerEvenements();
  truthy(as_of);
  truthy(evenements.length >= 6);
  for (const e of evenements) {
    truthy(e.source && /^https?:\/\//.test(e.source), `événement ${e.id} sans source`);
    truthy(e.checklist.length >= 1 && e.administrations.length >= 1);
  }
});

test('toute obligation référencée existe dans le catalogue (intégrité)', () => {
  const r = verifierIntegrite();
  eq(r.ok, true, JSON.stringify(r.manquantes));
});

console.log('=== Identification d\'événement ===');

test('reconnaît les événements de vie clés', () => {
  eq(identifierEvenement('Je viens d\'avoir un enfant'), 'naissance');
  eq(identifierEvenement('Je m\'installe au Luxembourg avec ma femme'), 'arrivee_luxembourg');
  eq(identifierEvenement('J\'ai perdu mon emploi'), 'perte_emploi');
  eq(identifierEvenement('Je veux créer ma société'), 'creation_entreprise');
  eq(identifierEvenement('mon père est décédé'), 'deces_succession');
});

test('texte non reconnu → null', () => eq(identifierEvenement('bonjour'), null));

console.log('=== Résolution de la chaîne ===');

test('résout la chaîne complète d\'une naissance', () => {
  const c = resoudreEvenement('naissance', { aujourdhui: REF });
  eq(c.evenement.id, 'naissance');
  truthy(c.consequences.length >= 1);
  truthy(c.administrations.some((a) => a.id === 'zukunftskeess'));
  truthy(c.documents.length >= 1 && c.delais.length >= 1 && c.checklist.length >= 1);
});

test('les obligations sont reliées au catalogue (nom + source résolus)', () => {
  const c = resoudreEvenement('naissance', { aujourdhui: REF });
  const alloc = c.obligations.find((o) => o.id === 'obl_allocations_familiales');
  truthy(alloc && alloc.resolue);
  truthy(alloc.nom && alloc.source);
});

test('résolution possible à partir d\'un texte libre', () => {
  const c = resoudreEvenement('je vais bientôt me marier', { aujourdhui: REF });
  eq(c.evenement.id, 'mariage_partenariat');
});

test('événement inconnu → erreur', () => {
  let ok = false; try { resoudreEvenement('xyz-inconnu-123'); } catch { ok = true; }
  truthy(ok);
});

console.log('=== Cohérence avec le registre de sources ===');

test('les administrations référencées existent dans le registre officiel', () => {
  const connus = new Set(chargerSources().sources.map((s) => s.id));
  for (const ev of chargerEvenements().evenements) {
    for (const a of ev.administrations) truthy(connus.has(a.id), `administration hors registre : ${a.id} (événement ${ev.id})`);
  }
});

test('listerEvenements renvoie id + nom', () => {
  const l = listerEvenements();
  truthy(l.length >= 6 && l[0].id && l[0].nom);
});

console.log(`\n${passed} tests réussis, ${failed} échoués.`);
process.exit(failed === 0 ? 0 : 1);

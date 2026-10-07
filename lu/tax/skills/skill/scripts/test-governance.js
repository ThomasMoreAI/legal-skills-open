#!/usr/bin/env node
/**
 * test-governance.js — Gouvernance de la connaissance (« fiche de vie » des règles).
 */

import { chargerCatalogue } from '../lib/diagnostic/index.js';
import {
  ficheDeVie, revuesDues, verifierGouvernance, enregistrerRevue, ajouterDelai,
  tableauQualite, STATUTS_GOUVERNANCE,
} from '../lib/connaissances/index.js';

let passed = 0, failed = 0;
function test(name, fn) {
  try { fn(); console.log(`  ✓ ${name}`); passed++; }
  catch (e) { console.log(`  ✗ ${name}\n      ${e.message}`); failed++; }
}
function eq(a, b, msg) { if (a !== b) throw new Error(`${msg || ''}: attendu ${JSON.stringify(b)}, reçu ${JSON.stringify(a)}`); }
function truthy(v, msg) { if (!v) throw new Error(msg || 'attendu truthy'); }

const { obligations } = chargerCatalogue();

console.log('=== Calcul de délai ===');

test('ajouterDelai gère mois, années, jours', () => {
  eq(ajouterDelai('2026-06-15', '6 months'), '2026-12-15');
  eq(ajouterDelai('2026-12-15', '6 months'), '2027-06-15');
  eq(ajouterDelai('2026-01-31', '1 month'), '2026-02-28'); // clamp fin de mois
  eq(ajouterDelai('2026-06-15', '1 year'), '2027-06-15');
  eq(ajouterDelai('2026-06-15', '10 days'), '2026-06-25');
});

console.log('=== Fiche de vie ===');

test('chaque règle a une fiche de vie complète', () => {
  for (const o of obligations) {
    const f = ficheDeVie(o);
    truthy(f.owner && f.status && f.reviewFrequency && f.lastVerified && f.nextReview, `fiche incomplète : ${o.id}`);
    truthy(STATUTS_GOUVERNANCE.includes(f.status));
  }
});

test('la prochaine revue est postérieure à la dernière vérification', () => {
  const f = ficheDeVie(obligations[0]);
  truthy(f.nextReview > f.lastVerified);
});

test('la revue est due une fois la date dépassée', () => {
  const f0 = ficheDeVie(obligations[0], { aujourdhui: '2026-07-01' });
  eq(f0.revueDue, false); // nextReview 2026-12-15
  const f1 = ficheDeVie(obligations[0], { aujourdhui: '2027-01-01' });
  eq(f1.revueDue, true);
});

console.log('=== Revues dues & contrôle ===');

test('revuesDues remonte les fiches à revoir', () => {
  eq(revuesDues(obligations, { aujourdhui: '2026-07-01' }).length, 0);
  truthy(revuesDues(obligations, { aujourdhui: '2027-06-01' }).length >= 1);
});

test('verifierGouvernance : le catalogue est gouverné', () => {
  const r = verifierGouvernance(obligations);
  eq(r.ok, true, JSON.stringify(r.problemes));
});

test('verifierGouvernance détecte une fiche incohérente', () => {
  const r = verifierGouvernance([{ id: 'x', gouvernance: { owner: 'Y', status: 'bidon', lastVerified: '2026-06-15', nextReview: '2026-01-01' } }]);
  eq(r.ok, false);
  truthy(r.problemes.some((p) => /statut invalide/.test(p.probleme)));
  truthy(r.problemes.some((p) => /nextReview antérieur/.test(p.probleme)));
});

console.log('=== Enregistrement d\'une revue (changeLog) ===');

test('enregistrerRevue met à jour lastVerified/nextReview et journalise', () => {
  const g = enregistrerRevue(obligations[0], { date: '2026-12-15', reason: 'Revue semestrielle' });
  eq(g.lastVerified, '2026-12-15');
  eq(g.nextReview, '2027-06-15');
  truthy(g.changeLog.length >= 1);
  eq(g.changeLog[g.changeLog.length - 1].reason, 'Revue semestrielle');
});

console.log('=== Trois niveaux de qualité ===');

test('tableauQualite distingue moteur / connaissance / réponses', () => {
  const q = tableauQualite(obligations, { aujourdhui: '2026-07-13' });
  truthy(q.moteur && q.connaissance && q.reponses);
  eq(q.connaissance.gouvernanceComplete, true);
  eq(q.connaissance.regles, obligations.length);
  eq(q.connaissance.versionnees, obligations.length);
});

console.log(`\n${passed} tests réussis, ${failed} échoués.`);
process.exit(failed === 0 ? 0 : 1);

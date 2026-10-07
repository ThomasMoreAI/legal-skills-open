#!/usr/bin/env node
/**
 * test-outputs.js — Tests de la couche Outputs (artefacts + adaptateurs).
 */

import { createMission } from '../lib/workflows/index.js';
import {
  timeline, documentPackage, reminders, report, produire, enregistrerAdaptateur, ADAPTATEURS, timelineVersICS,
} from '../lib/outputs/index.js';

let passed = 0, failed = 0;
function test(name, fn) {
  try { fn(); console.log(`  ✓ ${name}`); passed++; }
  catch (e) { console.log(`  ✗ ${name}\n      ${e.message}`); failed++; }
}
function eq(a, b, msg) { if (a !== b) throw new Error(`${msg || ''}: attendu ${JSON.stringify(b)}, reçu ${JSON.stringify(a)}`); }
function truthy(v, msg) { if (!v) throw new Error(msg || 'attendu truthy'); }

const REF = '2026-07-13';
const mission = () => createMission('Installation au Luxembourg', { evenements: ['arrivee_luxembourg'], aujourdhui: REF });

console.log('=== Artefact Timeline ===');

test('timeline produit des TimelineEvent au modèle unique', () => {
  const tl = timeline(mission(), { aujourdhui: REF });
  truthy(tl.evenements.length >= 1);
  const e = tl.evenements[0];
  for (const champ of ['title', 'deadline', 'priority', 'blocking', 'mission', 'status']) truthy(champ in e, `champ manquant : ${champ}`);
});

test('une étape qui en débloque d\'autres est prioritaire et bloquante', () => {
  const m = createMission('Créer une société', { evenements: ['creation_entreprise'], aujourdhui: REF });
  const tl = timeline(m, { aujourdhui: REF });
  const aut = tl.evenements.find((e) => /autorisation/i.test(e.title));
  eq(aut.blocking, true);
  eq(aut.priority, 'high');
});

console.log('=== Adaptateur .ics ===');

test('timelineVersICS produit un VCALENDAR valide', () => {
  const tl = timeline(mission(), { aujourdhui: REF });
  const ics = timelineVersICS(tl.evenements, { dtstamp: REF, nomCalendrier: 'Paperasse' });
  truthy(ics.startsWith('BEGIN:VCALENDAR'));
  truthy(ics.trim().endsWith('END:VCALENDAR'));
  truthy(/BEGIN:VEVENT/.test(ics) === (tl.evenements.some((e) => e.deadline)));
  truthy(/BEGIN:VALARM/.test(ics));
});

test('les caractères spéciaux sont échappés dans le .ics', () => {
  const ics = timelineVersICS([{ id: 'x', title: 'Test; virgule, et\nsaut', deadline: '2026-08-15', mission: 'M' }], { dtstamp: REF });
  truthy(/SUMMARY:.*Test\\; virgule\\, et\\nsaut/.test(ics));
});

test('une étape sans échéance ne crée pas d\'entrée calendrier', () => {
  const ics = timelineVersICS([{ id: 'x', title: 'Sans date', deadline: null, mission: 'M' }], { dtstamp: REF });
  truthy(!/BEGIN:VEVENT/.test(ics));
});

console.log('=== DocumentPackage / Reminders / Report ===');

test('documentPackage liste les pièces avec leur source', () => {
  const pkg = documentPackage(mission(), { aujourdhui: REF });
  truthy(pkg.pieces.length >= 1);
  truthy(pkg.pieces.every((p) => p.nom));
});

test('reminders sont triés et antérieurs à l\'échéance', () => {
  const m = createMission('Créer une société', { evenements: ['creation_entreprise', 'arrivee_luxembourg'], aujourdhui: REF });
  const r = reminders(m, { aujourdhui: REF, preavisJours: 7 });
  for (const x of r.rappels) truthy(x.when < x.deadline);
  const whens = r.rappels.map((x) => x.when);
  eq(JSON.stringify(whens), JSON.stringify([...whens].sort()));
});

test('report réutilise l\'évaluation de mission', () => {
  const rep = report(mission(), { aujourdhui: REF });
  truthy(typeof rep.confianceGlobale === 'number');
});

console.log('=== Registre d\'adaptateurs & produire() ===');

test('produire construit l\'artefact et l\'exporte au format demandé', () => {
  const res = produire(mission(), { type: 'timeline', format: 'ics', dtstamp: REF });
  eq(res.type, 'timeline');
  truthy(res.artefact.evenements.length >= 1);
  truthy(res.sortie.startsWith('BEGIN:VCALENDAR'));
});

test('produire expose Markdown pour documents et reports', () => {
  truthy(/^# Dossier de pièces/.test(produire(mission(), { type: 'documents', format: 'markdown', aujourdhui: REF }).sortie));
  truthy(/^# Rapport de mission/.test(produire(mission(), { type: 'reports', format: 'markdown', aujourdhui: REF }).sortie));
});

test('un adaptateur inconnu lève une erreur explicite', () => {
  let ok = false; try { produire(mission(), { type: 'timeline', format: 'bidon' }); } catch { ok = true; }
  truthy(ok);
});

test('on ajoute un adaptateur sans modifier le moteur', () => {
  enregistrerAdaptateur('timeline', 'json', (art) => JSON.stringify(art.evenements));
  truthy(ADAPTATEURS.has('timeline:json'));
  const res = produire(mission(), { type: 'timeline', format: 'json', aujourdhui: REF });
  truthy(res.sortie.startsWith('['));
});

console.log(`\n${passed} tests réussis, ${failed} échoués.`);
process.exit(failed === 0 ? 0 : 1);

#!/usr/bin/env node
/**
 * evaluation.js — CLI qualité & observabilité d'une mission.
 *
 * Sous-commandes :
 *   paperasse evaluation rapport --evenements arrivee_luxembourg [--profil '{...}']
 *   paperasse evaluation trace   --evenements creation_entreprise
 *
 * Construit une mission depuis les événements puis produit le rapport (confiance,
 * hypothèses, risques, manquants) ou la trace d'exécution auditable.
 */

import { createMission } from '../lib/workflows/index.js';
import { evaluerMission, traceMission } from '../lib/evaluation/index.js';
import { ceJourISO } from '../lib/diagnostic/index.js';

function arg(nom) { const i = process.argv.indexOf(nom); return i !== -1 ? process.argv[i + 1] : undefined; }
const aujourdhui = arg('--date') || ceJourISO();
const sous = process.argv[2];
const evenements = (arg('--evenements') || '').split(',').filter(Boolean);
const profil = arg('--profil') ? JSON.parse(arg('--profil')) : {};

if (!['rapport', 'trace'].includes(sous) || !evenements.length) {
  console.log(`Usage :
  paperasse evaluation rapport --evenements arrivee_luxembourg [--profil '{...}']
  paperasse evaluation trace   --evenements creation_entreprise`);
  process.exit(sous ? 1 : 0);
}

const objectif = evenements.length === 1 ? `Mission : ${evenements[0]}` : `Mission : ${evenements.join(' + ')}`;
const m = createMission(objectif, { evenements, profil, aujourdhui });

if (sous === 'rapport') {
  const r = evaluerMission(m, { profil, aujourdhui });
  console.log(`\nMission : ${r.mission}`);
  console.log(`Complète : ${r.complete ? 'oui' : 'non'} (${r.avancement.pourcentage}%)`);
  console.log(`Confiance globale : ${r.confianceGlobale} %`);
  const bloc = (titre, arr) => { console.log(`\n${titre} :`); if (!arr.length) console.log('  —'); for (const x of arr) console.log(`  - ${x}`); };
  bloc('Informations manquantes', r.informationsManquantes);
  bloc('Hypothèses', r.hypotheses);
  bloc('Risques', r.risques);
  bloc('Points bloquants', r.pointsBloquants);
  bloc('Sources', r.sources);
  console.log(`\n⚠ ${r.note}`);
} else {
  console.log(`\nTrace d'exécution — ${objectif}\n`);
  const fleche = { evenement_detecte: '◆', regle_appliquee: '│ règle', obligation_creee: '│ obligation', impact_calcule: '│ impact', etape_ajoutee: '│ étape', connecteur_selectionne: '│ connecteur' };
  for (const t of traceMission(m, { aujourdhui })) {
    console.log(`${fleche[t.phase] || t.phase} : ${t.detail}${t.source ? `  [${t.source}]` : ''}`);
  }
}

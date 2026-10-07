#!/usr/bin/env node
/**
 * output.js — CLI de la couche Outputs (artefacts métier → adaptateurs).
 *
 * Le moteur produit des artefacts (Timeline, Documents, Notifications, Reports) ;
 * les adaptateurs les exportent (.ics, Markdown, texte, JSON…).
 *
 *   paperasse output timeline --evenements arrivee_luxembourg --format ics [--out mission.ics]
 *   paperasse output documents --evenements creation_entreprise --format markdown
 *   paperasse output notifications --evenements creation_entreprise --format texte
 *   paperasse output report --evenements arrivee_luxembourg --format markdown
 */

import { writeFileSync } from 'node:fs';
import { createMission } from '../lib/workflows/index.js';
import { produire, ADAPTATEURS } from '../lib/outputs/index.js';
import { ceJourISO } from '../lib/diagnostic/index.js';

function arg(nom) { const i = process.argv.indexOf(nom); return i !== -1 ? process.argv[i + 1] : undefined; }
const aujourdhui = arg('--date') || ceJourISO();
const type = process.argv[2];
const evenements = (arg('--evenements') || '').split(',').filter(Boolean);
const format = arg('--format');

const TYPES = ['timeline', 'documents', 'notifications', 'reports'];
if (!TYPES.includes(type) || !evenements.length) {
  console.log(`Usage :
  paperasse output timeline      --evenements arrivee_luxembourg --format ics [--out mission.ics]
  paperasse output documents     --evenements creation_entreprise --format markdown
  paperasse output notifications --evenements creation_entreprise --format texte
  paperasse output report        --evenements arrivee_luxembourg --format markdown
  Adaptateurs disponibles : ${[...ADAPTATEURS.keys()].join(', ')}`);
  process.exit(type ? 1 : 0);
}

const objectif = evenements.length === 1 ? `Mission : ${evenements[0]}` : `Mission : ${evenements.join(' + ')}`;
const mission = createMission(objectif, { evenements, aujourdhui });

const res = produire(mission, { type, format, aujourdhui, dtstamp: aujourdhui, nomCalendrier: objectif });

if (arg('--out') && res.sortie != null) {
  writeFileSync(arg('--out'), res.sortie);
  console.log(`Écrit : ${arg('--out')} (${type}${format ? '/' + format : ''})`);
} else if (res.sortie != null) {
  console.log(res.sortie);
} else {
  console.log(JSON.stringify(res.artefact, null, 2));
}

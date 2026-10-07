#!/usr/bin/env node
/**
 * mission.js — CLI du Workflow Engine (Missions).
 *
 * Une mission déroule un résultat administratif (« Créer une société ») en
 * étapes ordonnées. Démo non interactive : crée une mission et la déroule en
 * mode « recommandation » (aucune action externe).
 *
 * Sous-commandes :
 *   paperasse mission creer   --objectif "Créer une société" --evenements creation_entreprise
 *   paperasse mission derouler --evenements creation_entreprise,naissance   (aperçu complet)
 */

import { createMission, advanceMission, avancement } from '../lib/workflows/index.js';
import { ceJourISO } from '../lib/diagnostic/index.js';

function arg(nom) { const i = process.argv.indexOf(nom); return i !== -1 ? process.argv[i + 1] : undefined; }
const aujourdhui = arg('--date') || ceJourISO();
const sous = process.argv[2];
const evenements = (arg('--evenements') || '').split(',').filter(Boolean);
const objectif = arg('--objectif') || (evenements.length ? `Mission : ${evenements.join(' + ')}` : 'Mission');

if (!['creer', 'derouler'].includes(sous) || !evenements.length) {
  console.log(`Usage :
  paperasse mission creer    --objectif "Créer une société" --evenements creation_entreprise
  paperasse mission derouler --evenements creation_entreprise,naissance
  Événements : voir « paperasse evenement liste ».`);
  process.exit(sous ? 1 : 0);
}

const m = createMission(objectif, { evenements, aujourdhui });
const a0 = avancement(m);
console.log(`\n🎯 ${m.objectif}`);
console.log(`Étapes : ${a0.total} | avancement : ${a0.pourcentage}%\n`);

console.log('Étapes (ordre des dépendances) :');
for (const e of m.etapes) {
  const dep = e.dependances.length ? ` [après : ${e.dependances.join(', ')}]` : '';
  console.log(`  • ${e.nom}${e.echeance ? `  ⏱ ${e.echeance}` : ''}  (${e.typeAction})${dep}`);
  if (e.debloque && e.debloque.length) console.log(`     débloque : ${e.debloque.join(', ')}`);
}

if (sous === 'derouler') {
  console.log('\nDéroulé (mode recommandation, aucune action externe) :');
  let garde = 0;
  while (avancement(m).pourcentage < 100 && garde < 100) {
    const r = advanceMission(m, { date: aujourdhui });
    if (r.etape) console.log(`  ✓ ${r.etape.nom} — ${r.message}`);
    if (r.bloque || r.termine) break;
    garde++;
  }
  const a = avancement(m);
  console.log(`\nAvancement final : ${a.pourcentage}% (${a.faits}/${a.total})`);
}

console.log('\n⚠ Séparation stricte : recommandation (aucune action) → préparation (vous validez) → exécution (envoi après confirmation explicite). Aucun envoi n\'a eu lieu.');

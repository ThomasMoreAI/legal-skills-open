#!/usr/bin/env node
/**
 * rappels.js — CLI calendrier, rappels & surveillance (Milestone 10).
 *
 * Sous-commandes :
 *   paperasse rappels societe   --json '{...société...}' [--date YYYY-MM-DD]
 *   paperasse rappels fichier   --file dossiers.json     [--date YYYY-MM-DD]
 *
 * Construit les dossiers depuis un diagnostic (option société) ou depuis un
 * fichier JSON de dossiers, puis affiche les rappels et le calendrier coloré.
 */

import { readFileSync } from 'node:fs';
import { chargerCatalogue, creerProfilSociete, diagnostiquer, dossierDepuisObligation, ceJourISO } from '../lib/diagnostic/index.js';
import { genererRappels, calendrierDossiers, COULEURS } from '../lib/rappels/index.js';

function arg(nom) { const i = process.argv.indexOf(nom); return i !== -1 ? process.argv[i + 1] : undefined; }
const aujourdhui = arg('--date') || ceJourISO();
const sous = process.argv[2];

function dossiersDepuisSociete(json) {
  const { obligations } = chargerCatalogue();
  const societe = creerProfilSociete(json ? JSON.parse(json) : { nom: 'Exemple SARL', formeJuridique: 'SARL', statut: 'actif', regimeTVA: 'normal', frequenceTVA: 'mensuelle' });
  const { applicables } = diagnostiquer(societe, obligations, { aujourdhui });
  return applicables.map((e) => dossierDepuisObligation(e, { societeId: societe.id || 'local', aujourdhui }));
}

let dossiers;
if (sous === 'societe') dossiers = dossiersDepuisSociete(arg('--json'));
else if (sous === 'fichier') dossiers = JSON.parse(readFileSync(arg('--file'), 'utf8'));
else {
  console.log(`Usage :
  paperasse rappels societe [--json '{...société...}'] [--date YYYY-MM-DD]
  paperasse rappels fichier --file dossiers.json        [--date YYYY-MM-DD]`);
  process.exit(sous ? 1 : 0);
}

const ICONE = { rouge: '🔴', orange: '🟠', jaune: '🟡', vert: '🟢', neutre: '⚪' };
const cal = calendrierDossiers(dossiers, { aujourdhui });
const rappels = genererRappels(dossiers, { aujourdhui });

console.log(`\nSurveillance des dossiers — au ${aujourdhui}\n`);
console.log('Alertes :', Object.entries(cal.compteurs).map(([k, v]) => `${ICONE[k]} ${k} ${v}`).join('  '));

console.log(`\n=== Rappels (${rappels.length}) ===`);
for (const r of rappels) {
  console.log(`${ICONE[r.couleur]} ${r.intitule}${r.echeance ? `  ⏱ ${r.echeance}` : ''}${r.actionRequise ? '  [action requise]' : ''}`);
  for (const m of r.messages) console.log(`     - ${m}`);
}

console.log(`\n=== Calendrier (${cal.chronologie.length} avec échéance) ===`);
for (const d of cal.chronologie) {
  console.log(`  ${ICONE[d.alerte.couleur]} ${d.echeance} — ${d.typeDemarche || d.categorie} (${COULEURS[d.alerte.couleur]})`);
}

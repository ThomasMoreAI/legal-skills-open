#!/usr/bin/env node
/**
 * courriers.js — CLI de génération de courriers (Milestone 9).
 *
 * Sous-commandes :
 *   paperasse courriers types
 *   paperasse courriers generer  --type demande_delai --json '{"expediteur":"Jean Test","destinataire":"AED","references":["LU12345678"],"faits":"..."}'
 *   paperasse courriers reponse  --file courrier-aed.txt --json '{"expediteur":"Jean Test"}'
 *   paperasse courriers rdv      --type notaire
 *
 * Tout courrier est produit à l'état de PROJET. Aucun envoi.
 */

import { readFileSync } from 'node:fs';
import {
  genererCourrier, courrierDepuisAnalyse, checklistRendezVous, TYPES_COURRIER,
} from '../lib/courriers/index.js';
import { analyserDocument } from '../lib/documents/index.js';

function arg(nom) { const i = process.argv.indexOf(nom); return i !== -1 ? process.argv[i + 1] : undefined; }
const sous = process.argv[2];

switch (sous) {
  case 'types':
    console.log('Types de courrier disponibles :');
    for (const [k, v] of Object.entries(TYPES_COURRIER)) console.log(`  • ${k} — ${v.objet}`);
    break;
  case 'generer': {
    const donnees = arg('--json') ? JSON.parse(arg('--json')) : {};
    const c = genererCourrier(arg('--type') || 'reponse_administration', donnees);
    console.log(`⚠ ${c.avertissement}\n`);
    console.log(c.texte);
    break;
  }
  case 'reponse': {
    const analyse = analyserDocument(readFileSync(arg('--file'), 'utf8'), { nom: arg('--file').split('/').pop() });
    const c = courrierDepuisAnalyse(analyse, arg('--json') ? JSON.parse(arg('--json')) : {});
    console.log(`⚠ ${c.avertissement}\n`);
    console.log(c.texte);
    break;
  }
  case 'rdv': {
    const liste = checklistRendezVous(arg('--type') || 'administration');
    console.log(`Checklist de rendez-vous (${arg('--type') || 'administration'}) :`);
    for (const x of liste) console.log(`  ☐ ${x}`);
    break;
  }
  default:
    console.log(`Usage :
  paperasse courriers types
  paperasse courriers generer --type <type> --json '{...}'
  paperasse courriers reponse --file courrier.txt [--json '{"expediteur":"..."}']
  paperasse courriers rdv     --type administration|notaire|banque|comptable`);
    process.exit(sous ? 1 : 0);
}

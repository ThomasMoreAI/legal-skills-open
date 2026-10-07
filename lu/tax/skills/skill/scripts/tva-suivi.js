#!/usr/bin/env node
/**
 * tva-suivi.js — CLI du module de suivi TVA (Milestone 4).
 *
 * Sous-commandes :
 *   paperasse tva-suivi calendrier --freq mensuelle --debut 2026-01-15 [--soumises 2026-01,2026-02]
 *   paperasse tva-suivi frequence  --ca 300000
 *   paperasse tva-suivi checklist
 *   paperasse tva-suivi coherence  --file operations.json
 *   paperasse tva-suivi courrier   --file courrier-aed.txt --freq trimestrielle --debut 2025-01-01
 *
 * Ne dépose et n'envoie rien : suivi, détection et contrôle uniquement.
 */

import { readFileSync } from 'node:fs';
import {
  determinerFrequence, calendrierTVA, checklistDeclaration,
  controleCoherence, rapprocherCourrierAED,
} from '../lib/tva/index.js';
import { analyserDocument } from '../lib/documents/index.js';
import { ceJourISO } from '../lib/diagnostic/index.js';

function arg(nom) { const i = process.argv.indexOf(nom); return i !== -1 ? process.argv[i + 1] : undefined; }
const aujourdhui = arg('--date') || ceJourISO();
const sous = process.argv[2];

switch (sous) {
  case 'frequence': {
    const ca = Number(arg('--ca'));
    const r = determinerFrequence(ca);
    console.log(`CA annuel HT ${ca} € → fréquence de déclaration : ${r.frequence}`);
    console.log(`Seuils : ${JSON.stringify(r.seuils)}`);
    console.log(`Source : ${r.provenance.source} (${r.provenance.niveauConfiance})`);
    break;
  }
  case 'calendrier': {
    const soumises = (arg('--soumises') || '').split(',').filter(Boolean);
    const cal = calendrierTVA({ frequenceTVA: arg('--freq'), debut: arg('--debut'), soumises, aujourdhui });
    console.log(`\nCalendrier TVA (${cal.frequenceTVA}) — au ${aujourdhui}\n`);
    console.log(`Périodes attendues : ${cal.attendues.length} | soumises : ${cal.soumises.length}`);
    console.log(`\nEN RETARD (${cal.enRetard.length}) :`);
    for (const p of cal.enRetard) console.log(`  ⚠ ${p.code} — échéance dépassée le ${p.echeance}`);
    console.log(`\nÀ PRÉPARER (${cal.aPreparer.length}) :`);
    for (const p of cal.aPreparer) console.log(`  • ${p.code} — échéance ${p.echeance}`);
    if (cal.prochaineDeclaration) console.log(`\nProchaine déclaration : ${cal.prochaineDeclaration.code} (échéance ${cal.prochaineDeclaration.echeance})`);
    console.log(`\n${cal.provenance.note} Source : ${cal.provenance.source}`);
    break;
  }
  case 'checklist':
    console.log('Données nécessaires à la préparation d\'une déclaration TVA :');
    for (const c of checklistDeclaration()) console.log(`  ☐ ${c}`);
    break;
  case 'coherence': {
    const input = JSON.parse(readFileSync(arg('--file'), 'utf8'));
    const { anomalies, recalcul } = controleCoherence(input);
    if (recalcul) console.log(`TVA collectée recalculée : ${recalcul.collectee} | déductible : ${recalcul.deductible} | due nette : ${recalcul.due_nette}\n`);
    if (!anomalies.length) console.log('✓ Aucune anomalie détectée.');
    else { console.log(`${anomalies.length} anomalie(s) :`); for (const a of anomalies) console.log(`  [${a.gravite}] ${a.code} — ${a.message}`); }
    break;
  }
  case 'courrier': {
    const analyse = analyserDocument(readFileSync(arg('--file'), 'utf8'), { nom: arg('--file').split('/').pop(), aujourdhui });
    const cal = arg('--freq') && arg('--debut') ? calendrierTVA({ frequenceTVA: arg('--freq'), debut: arg('--debut'), soumises: (arg('--soumises') || '').split(',').filter(Boolean), aujourdhui }) : null;
    const r = rapprocherCourrierAED(analyse, cal, { aujourdhui });
    console.log(`Période concernée : ${r.periodeConcernee || '—'} | statut : ${r.statut}`);
    console.log(`Dossier : [${r.dossier.priorite}] ${r.dossier.typeDemarche} → ${r.dossier.statut}${r.dossier.echeance ? ` (échéance ${r.dossier.echeance})` : ''}`);
    console.log(`Risques : ${r.dossier.risques.join(', ') || '—'}`);
    console.log(`⚠ ${r.dossier.provenance.note}`);
    break;
  }
  default:
    console.log(`Usage :
  paperasse tva-suivi frequence  --ca 300000
  paperasse tva-suivi calendrier --freq mensuelle --debut 2026-01-15 [--soumises 2026-01,2026-02] [--date YYYY-MM-DD]
  paperasse tva-suivi checklist
  paperasse tva-suivi coherence  --file operations.json
  paperasse tva-suivi courrier   --file courrier-aed.txt [--freq trimestrielle --debut 2025-01-01]`);
    process.exit(sous ? 1 : 0);
}

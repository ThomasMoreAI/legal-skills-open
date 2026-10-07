#!/usr/bin/env node
/**
 * reasoning.js — CLI du moteur de raisonnement & Change Impact.
 *
 * Sous-commandes :
 *   paperasse reasoning impact  --etat '{...}' --changement '{"situationFamiliale":"marie"}'
 *   paperasse reasoning simuler --etat '{...}' --changement '{...}'  |  --evenements creation_entreprise,naissance
 *
 * Propage les conséquences dans le graphe et les explique (traçable). Aucune
 * démarche effectuée ; simuler ne modifie jamais l'état.
 */

import { computeImpact, simulateScenario, explainReasoning } from '../lib/reasoning/index.js';
import { ceJourISO } from '../lib/diagnostic/index.js';

function arg(nom) { const i = process.argv.indexOf(nom); return i !== -1 ? process.argv[i + 1] : undefined; }
const aujourdhui = arg('--date') || ceJourISO();
const sous = process.argv[2];
const etat = arg('--etat') ? JSON.parse(arg('--etat')) : {};
const changement = arg('--changement') ? JSON.parse(arg('--changement')) : {};

function afficherImpact(imp) {
  console.log(`\nChangement : ${imp.delta.map((d) => `${d.champ} ${d.avant ?? '∅'}→${d.apres ?? '∅'}`).join(', ') || '—'}`);
  if (imp.evenementsAssocies.length) console.log(`Événement(s) associé(s) : ${imp.evenementsAssocies.join(', ')}`);
  if (imp.domainesImpactes.length) console.log(`Domaines impactés (${imp.domainesImpactes.length}) : ${imp.domainesImpactes.join(', ')}`);
  console.log(`\nImpacts concrets : ${imp.total}`);
  for (const v of imp.valeursModifiees) console.log(`  ~ ${v.nom} : ${v.avant} → ${v.apres}  (${v.source})`);
  for (const o of imp.obligations.ajoutees) console.log(`  + ${o.nom}${o.cause.length ? ` (car ${o.cause.join(', ')})` : ''}`);
  for (const o of imp.obligations.retirees) console.log(`  − ${o.nom}`);
  console.log('\nExplication (traçable) :');
  for (const e of explainReasoning(imp)) console.log(`  • ${e.conclusion} — ${e.cause}${e.source ? ` [${e.source}]` : ''}`);
  console.log(`\n⚠ ${imp.note}`);
}

switch (sous) {
  case 'impact':
    afficherImpact(computeImpact(etat, changement, { aujourdhui }));
    break;
  case 'simuler': {
    const evenements = arg('--evenements') ? arg('--evenements').split(',').filter(Boolean) : undefined;
    const res = simulateScenario(etat, { changements: Object.keys(changement).length ? changement : undefined, evenements, libelle: arg('--libelle') || 'Scénario hypothétique' }, { aujourdhui });
    console.log(`\n🔮 ${res.libelle} (hypothétique — le dossier n'est pas modifié)`);
    if (res.impact) afficherImpact(res.impact);
    if (res.plan) {
      console.log(`\n📋 ${res.plan.resume}`);
      for (const d of res.plan.demarches) console.log(`  ${d.ordre}. ${d.nom}${d.echeance ? `  ⏱ ${d.echeance}` : ''}`);
    }
    break;
  }
  default:
    console.log(`Usage :
  paperasse reasoning impact  --etat '{...}' --changement '{"situationFamiliale":"marie"}'
  paperasse reasoning simuler --etat '{...}' [--changement '{...}'] [--evenements a,b] [--libelle "Et si..."]`);
    process.exit(sous ? 1 : 0);
}

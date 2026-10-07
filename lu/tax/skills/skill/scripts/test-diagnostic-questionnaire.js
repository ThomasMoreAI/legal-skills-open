#!/usr/bin/env node
/**
 * test-diagnostic-questionnaire.js — Tests Milestone 2 : questionnaire dynamique
 * et tableau de bord des obligations.
 */

import {
  chargerCatalogue,
  champsPertinents,
  prochaineQuestion,
  questionsRestantes,
  appliquerReponse,
  construireTableauDeBord,
} from '../lib/diagnostic/index.js';

let passed = 0, failed = 0;
function test(name, fn) {
  try { fn(); console.log(`  ✓ ${name}`); passed++; }
  catch (e) { console.log(`  ✗ ${name}\n      ${e.message}`); failed++; }
}
function eq(a, b, msg) { if (a !== b) throw new Error(`${msg || ''}: attendu ${JSON.stringify(b)}, reçu ${JSON.stringify(a)}`); }
function truthy(v, msg) { if (!v) throw new Error(msg || 'attendu truthy'); }
function throws(fn, msg) { let t = false; try { fn(); } catch { t = true; } if (!t) throw new Error(msg || 'exception attendue'); }

const REF = '2026-07-12';
const { obligations } = chargerCatalogue();

console.log('=== Questionnaire dynamique ===');

test('une situation vide rend plusieurs champs pertinents', () => {
  const c = champsPertinents({}, obligations);
  truthy(c.has('regimeTVA'));
  truthy(c.has('statut'));
});

test('la 1re question porte sur un champ formulable et discriminant', () => {
  const q = prochaineQuestion({}, obligations);
  truthy(q, 'aucune question proposée');
  truthy(q.champ && q.label);
  truthy(q.gated >= 1);
});

test('répondre "non_assujetti" élimine la question sur la fréquence TVA (pas de question inutile)', () => {
  // Avant : frequenceTVA est pertinent (conditionne la déclaration TVA mensuelle).
  truthy(champsPertinents({}, obligations).has('frequenceTVA'));
  // Après : la société n'est pas assujettie → les obligations TVA sont décidées,
  // frequenceTVA ne doit plus être demandé.
  const s = appliquerReponse({}, 'regimeTVA', 'non_assujetti');
  eq(champsPertinents(s, obligations).has('frequenceTVA'), false);
});

test('appliquerReponse coerce les types (booléen, nombre)', () => {
  eq(appliquerReponse({}, 'frontalier', 'oui').frontalier, true);
  eq(appliquerReponse({}, 'nombreEnfants', '3').nombreEnfants, 3);
});

test('appliquerReponse rejette une valeur hors énumération', () => {
  throws(() => appliquerReponse({}, 'regimeTVA', 'bidon'));
});

test('le questionnaire se termine (plus aucune question) une fois les champs pertinents renseignés', () => {
  const reponses = {
    statut: 'actif', regimeTVA: 'normal', frequenceTVA: 'mensuelle',
    statutProfessionnel: 'independant', dateArriveeLux: '2026-01-15',
    frontalier: false, paysResidence: 'LU', situationFamiliale: 'marie',
    statutLogement: 'locataire', nombreEnfants: 2,
  };
  let s = {};
  let garde = 0;
  let q;
  while ((q = prochaineQuestion(s, obligations)) && garde < 20) {
    truthy(q.champ in reponses, `question sur un champ non prévu : ${q.champ}`);
    s = appliquerReponse(s, q.champ, reponses[q.champ]);
    garde++;
  }
  eq(prochaineQuestion(s, obligations), null);
  truthy(garde <= 12, 'trop de questions posées');
});

test('aucune question n\'est posée sur un champ dont aucune obligation ne dépend', () => {
  // Aucune obligation du catalogue ne conditionne sur statutLogement → jamais
  // demandé tant qu'aucune obligation ne l'utilise.
  const champs = questionsRestantes({}, obligations).map((q) => q.champ);
  eq(champs.includes('statutLogement'), false);
});

console.log('=== Tableau de bord ===');

test('le tableau de bord expose exactement les 5 colonnes', () => {
  const { colonnes } = construireTableauDeBord({}, obligations, { aujourdhui: REF });
  const cles = Object.keys(colonnes).sort();
  eq(cles.join(','), 'a_faire_prochainement,a_surveiller,informations_manquantes,non_applicable,obligatoire_maintenant');
});

test('société assujettie mensuelle : TVA mensuelle classée selon son échéance', () => {
  const soc = { regimeTVA: 'normal', frequenceTVA: 'mensuelle', statut: 'actif' };
  const { colonnes } = construireTableauDeBord(soc, obligations, { aujourdhui: REF });
  const toutes = [...colonnes.obligatoire_maintenant, ...colonnes.a_faire_prochainement, ...colonnes.a_surveiller];
  const tva = toutes.find((c) => c.id === 'obl_tva_declaration_mensuelle');
  truthy(tva, 'TVA mensuelle absente des colonnes actives');
  eq(tva.echeance, '2026-08-15');
});

test('la déclaration TVA trimestrielle est non applicable si fréquence mensuelle', () => {
  const soc = { regimeTVA: 'normal', frequenceTVA: 'mensuelle', statut: 'actif' };
  const { colonnes } = construireTableauDeBord(soc, obligations, { aujourdhui: REF });
  truthy(colonnes.non_applicable.some((c) => c.id === 'obl_tva_declaration_trimestrielle'));
});

test('les champs manquants alimentent la colonne informations_manquantes avec des questions', () => {
  const { colonnes } = construireTableauDeBord({}, obligations, { aujourdhui: REF });
  truthy(colonnes.informations_manquantes.length >= 1);
  const item = colonnes.informations_manquantes[0];
  truthy(Array.isArray(item.manquantes) && item.manquantes.length >= 1);
  truthy(Array.isArray(item.questions) && item.questions.length >= 1);
});

test('chaque carte active porte une source et les actions Commencer / Créer un rappel', () => {
  const soc = { regimeTVA: 'normal', frequenceTVA: 'mensuelle', statut: 'actif' };
  const { colonnes } = construireTableauDeBord(soc, obligations, { aujourdhui: REF });
  const actives = [...colonnes.obligatoire_maintenant, ...colonnes.a_faire_prochainement, ...colonnes.a_surveiller];
  truthy(actives.length >= 1);
  for (const c of actives) {
    truthy(c.source && c.source.url, `carte ${c.id} sans source`);
    truthy(c.actions.includes('commencer') && c.actions.includes('creer_rappel'));
  }
});

test('les compteurs correspondent aux tailles de colonnes', () => {
  const { colonnes, compteurs } = construireTableauDeBord({}, obligations, { aujourdhui: REF });
  for (const [k, v] of Object.entries(colonnes)) eq(compteurs[k], v.length, `compteur ${k}`);
});

console.log(`\n${passed} tests réussis, ${failed} échoués.`);
process.exit(failed === 0 ? 0 : 1);

#!/usr/bin/env node
/**
 * test-documents.js — Tests Milestone 3 : analyse de courriers officiels.
 */

import {
  analyserDocument,
  detecterDates,
  detecterMontants,
  detecterReferences,
  detecterPeriode,
  detecterEcheance,
  dossierDepuisDocument,
} from '../lib/documents/index.js';

let passed = 0, failed = 0;
function test(name, fn) {
  try { fn(); console.log(`  ✓ ${name}`); passed++; }
  catch (e) { console.log(`  ✗ ${name}\n      ${e.message}`); failed++; }
}
function eq(a, b, msg) { if (a !== b) throw new Error(`${msg || ''}: attendu ${JSON.stringify(b)}, reçu ${JSON.stringify(a)}`); }
function truthy(v, msg) { if (!v) throw new Error(msg || 'attendu truthy'); }

const REF = '2026-07-13';

const COURRIER_AED = `Administration de l'Enregistrement, des Domaines et de la TVA (AED)
Bureau d'imposition TVA

Luxembourg, le 03/06/2026

Numéro de TVA : LU12345678
Réf : 2026/TVA/00987

Objet : Déclaration de TVA manquante — période T1 2026

Madame, Monsieur,

Nous constatons que votre déclaration de TVA pour la période T1 2026 ne nous est
pas parvenue. Veuillez nous faire parvenir la déclaration au plus tard le
30/06/2026. À défaut, une taxation d'office pourra être appliquée, majorée
d'intérêts de retard.

Montant estimé : 4.250,00 €`;

console.log('=== Extracteurs ===');

test('detecterDates normalise en ISO et trouve toutes les dates', () => {
  const d = detecterDates(COURRIER_AED).map((x) => x.iso);
  truthy(d.includes('2026-06-03'));
  truthy(d.includes('2026-06-30'));
});

test('detecterDates gère les mois en toutes lettres', () => {
  const d = detecterDates('Fait le 1er octobre 2024 puis le 15 mai 2025.').map((x) => x.iso);
  truthy(d.includes('2024-10-01'));
  truthy(d.includes('2025-05-15'));
});

test('detecterDates rejette une date impossible (30 février)', () => {
  eq(detecterDates('le 30/02/2026').length, 0);
});

test('detecterMontants lit le format luxembourgeois 1.234,56', () => {
  const m = detecterMontants(COURRIER_AED);
  truthy(m.some((x) => x.valeur === 4250), 'montant 4250 non détecté');
});

test('detecterMontants gère les milliers et décimales', () => {
  eq(detecterMontants('Total : 1.234,56 €')[0].valeur, 1234.56);
});

test('detecterReferences extrait TVA et numéro de référence', () => {
  const r = detecterReferences(COURRIER_AED);
  truthy(r.some((x) => x.type === 'tva' && x.valeur === 'LU12345678'));
  truthy(r.some((x) => x.valeur === '2026/TVA/00987'));
});

test('detecterPeriode reconnaît un trimestre', () => {
  eq(detecterPeriode(COURRIER_AED).type, 'trimestre');
});

test('detecterEcheance suit le marqueur "au plus tard le"', () => {
  const dates = detecterDates(COURRIER_AED);
  eq(detecterEcheance(COURRIER_AED, dates).iso, '2026-06-30');
});

test('detecterEcheance calcule un délai relatif si date de document connue', () => {
  const txt = 'Veuillez régulariser endéans les 30 jours.';
  const e = detecterEcheance(txt, detecterDates(txt), { dateDocument: '2026-06-01' });
  eq(e.iso, '2026-07-01');
  eq(e.incertain, true);
});

console.log('=== Analyse complète ===');

const analyse = analyserDocument(COURRIER_AED, { nom: 'courrier-aed.txt', aujourdhui: REF });

test('identifie l\'administration AED', () => eq(analyse.administration.id, 'aed'));
test('identifie le type déclaration TVA', () => eq(analyse.type.id, 'declaration_tva'));
test('détecte l\'échéance', () => eq(analyse.echeance.iso, '2026-06-30'));
test('détecte l\'action demandée', () => truthy(analyse.action));
test('détecte les conséquences (taxation d\'office, intérêts)', () => {
  truthy(analyse.consequences.some((c) => /taxation/i.test(c)));
  truthy(analyse.consequences.some((c) => /intérêts|majoration/i.test(c)));
});
test('produit un résumé, une checklist et un projet de réponse', () => {
  truthy(analyse.resume.length > 20);
  truthy(analyse.checklist.length >= 3);
  truthy(analyse.reponseProposee && analyse.reponseProposee.statut === 'projet');
});
test('le document reste consultable (texte original conservé)', () => {
  eq(analyse.texteExtrait, COURRIER_AED);
});
test('le document importé n\'est jamais officiel et impose une validation humaine', () => {
  truthy(['derive', 'estimation', 'incertain'].includes(analyse.niveauConfiance));
  eq(analyse.document.validationHumaineRequise, true);
});

console.log('=== Cas incertains (règle stricte) ===');

test('un texte illisible déclenche l\'avertissement de validation humaine', () => {
  const a = analyserDocument('   ', { nom: 'vide' });
  eq(a.lisible, false);
  eq(a.niveauConfiance, 'incertain');
  truthy(a.avertissement && /validation humaine/i.test(a.avertissement));
});

test('un courrier sans émetteur ni date est signalé incertain', () => {
  const a = analyserDocument('Bonjour, merci de bien vouloir nous recontacter prochainement.', { nom: 'flou' });
  eq(a.niveauConfiance, 'incertain');
  truthy(a.avertissement);
});

console.log('=== Dossier issu du document ===');

test('dossierDepuisDocument reprend l\'échéance, les risques et une provenance incertaine', () => {
  const d = dossierDepuisDocument(analyse, { societeId: 'soc_1', aujourdhui: REF });
  eq(d.type, 'Dossier');
  eq(d.echeance, '2026-06-30');
  truthy(d.risques.length >= 1);
  eq(d.provenance.niveauConfiance, 'incertain');
  eq(d.provenance.validationHumaineRequise, true);
  eq(d.societeId, 'soc_1');
});

console.log(`\n${passed} tests réussis, ${failed} échoués.`);
process.exit(failed === 0 ? 0 : 1);

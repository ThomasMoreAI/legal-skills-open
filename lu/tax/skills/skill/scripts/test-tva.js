#!/usr/bin/env node
/**
 * test-tva.js — Tests Milestone 4 : module TVA (calendrier, périodes manquantes,
 * cohérence, rapprochement courrier AED).
 */

import {
  determinerFrequence,
  echeanceDepot,
  periodesAttendues,
  calendrierTVA,
  checklistDeclaration,
  controleCoherence,
  rapprocherCourrierAED,
} from '../lib/tva/index.js';
import { analyserDocument } from '../lib/documents/index.js';

let passed = 0, failed = 0;
function test(name, fn) {
  try { fn(); console.log(`  ✓ ${name}`); passed++; }
  catch (e) { console.log(`  ✗ ${name}\n      ${e.message}`); failed++; }
}
function eq(a, b, msg) { if (a !== b) throw new Error(`${msg || ''}: attendu ${JSON.stringify(b)}, reçu ${JSON.stringify(a)}`); }
function truthy(v, msg) { if (!v) throw new Error(msg || 'attendu truthy'); }

const REF = '2026-07-13';

console.log('=== Fréquence & échéances ===');

test('determinerFrequence selon le CA annuel HT (seuils AED)', () => {
  eq(determinerFrequence(700_000).frequence, 'mensuelle');
  eq(determinerFrequence(300_000).frequence, 'trimestrielle');
  eq(determinerFrequence(50_000).frequence, 'annuelle');
});

test('determinerFrequence est tracé (source + niveau de confiance)', () => {
  const r = determinerFrequence(300_000);
  truthy(r.provenance.source);
  eq(r.provenance.niveauConfiance, 'derive');
});

test('echeanceDepot : mensuelle = 15 du mois suivant', () => {
  eq(echeanceDepot({ type: 'mois', annee: 2026, mois: 1 }), '2026-02-15');
});

test('echeanceDepot : trimestre T4 = 15 janvier N+1', () => {
  eq(echeanceDepot({ type: 'trimestre', annee: 2025, trimestre: 4 }), '2026-01-15');
});

test('echeanceDepot : annuelle = 1er mars N+1', () => {
  eq(echeanceDepot({ type: 'annee', annee: 2025 }), '2026-03-01');
});

console.log('=== Périodes attendues & calendrier ===');

test('périodes mensuelles attendues = mois écoulés depuis l\'assujettissement', () => {
  const p = periodesAttendues({ frequenceTVA: 'mensuelle', debut: '2026-01-15', aujourdhui: REF });
  eq(p.length, 6); // janvier→juin ; juillet en cours exclu
  eq(p[0].code, '2026-01');
  eq(p[5].code, '2026-06');
  eq(p[5].echeance, '2026-07-15');
});

test('calendrier TVA : déclarations manquantes → en retard vs à préparer', () => {
  const cal = calendrierTVA({ frequenceTVA: 'mensuelle', debut: '2026-01-15', soumises: ['2026-01', '2026-02'], aujourdhui: REF });
  eq(cal.soumises.length, 2);
  eq(cal.enRetard.length, 3);       // 03, 04, 05 (échéances passées)
  eq(cal.aPreparer.length, 1);      // 06 (échéance 2026-07-15, à venir)
  eq(cal.prochaineDeclaration.code, '2026-06');
  eq(cal.prochaineEcheancePaiement.code, '2026-03'); // la plus proche des manquantes
});

test('une déclaration manquante est bien détectée (alerte)', () => {
  const cal = calendrierTVA({ frequenceTVA: 'trimestrielle', debut: '2025-01-01', soumises: [], aujourdhui: REF });
  truthy(cal.enRetard.length >= 1, 'aucune période en retard détectée');
  truthy(cal.enRetard.some((p) => p.code === '2026-T1'));
});

test('checklistDeclaration couvre les données clés', () => {
  const c = checklistDeclaration();
  truthy(c.some((x) => /collectée/i.test(x)));
  truthy(c.some((x) => /intracommunautaires/i.test(x)));
});

console.log('=== Contrôle de cohérence (calcul traçable) ===');

test('déclaration cohérente et complète = aucune anomalie', () => {
  const { anomalies } = controleCoherence({
    numeroTVA: 'LU12345678',
    operations: { livraisons_normal_17: 1000 },
    declaration: { collectee: 170 },
    factures: [{ numero: 'F1', date: '2026-01-05', ht: 1000, taux: 17, tva: 170 }],
  });
  eq(anomalies.length, 0, JSON.stringify(anomalies));
});

test('recalcul de la TVA collectée détecte une incohérence', () => {
  const { anomalies, recalcul } = controleCoherence({
    numeroTVA: 'LU12345678',
    operations: { livraisons_normal_17: 1000 },
    declaration: { collectee: 200 },
  });
  eq(recalcul.collectee, 170);
  truthy(anomalies.some((a) => a.code === 'collectee_incoherente'));
});

test('numéro TVA absent, doublon de facture et taux invalide sont signalés', () => {
  const { anomalies } = controleCoherence({
    factures: [
      { numero: 'F1', date: '2026-01-05', ht: 1000, taux: 17, tva: 170 },
      { numero: 'F1', date: '2026-01-05', ht: 1000, taux: 99, tva: 990 },
    ],
  });
  const codes = anomalies.map((a) => a.code);
  truthy(codes.includes('tva_absent'));
  truthy(codes.includes('facture_doublon'));
  truthy(codes.includes('taux_invalide'));
});

test('périodes manquantes du calendrier remontent comme anomalie', () => {
  const cal = calendrierTVA({ frequenceTVA: 'mensuelle', debut: '2026-01-15', soumises: [], aujourdhui: REF });
  const { anomalies } = controleCoherence({ numeroTVA: 'LU12345678', calendrier: cal });
  truthy(anomalies.some((a) => a.code === 'periodes_manquantes'));
});

console.log('=== Rapprochement courrier AED (M3 → M4) ===');

const COURRIER_AED = `Administration de l'Enregistrement, des Domaines et de la TVA (AED)
Réf : 2026/TVA/00987
Objet : Déclaration de TVA manquante — période T1 2026
Veuillez nous faire parvenir la déclaration au plus tard le 30/06/2026.
À défaut, une taxation d'office sera appliquée.`;

test('un courrier AED crée une action rattachée à la période manquante', () => {
  const analyse = analyserDocument(COURRIER_AED, { nom: 'aed.txt', aujourdhui: REF });
  const cal = calendrierTVA({ frequenceTVA: 'trimestrielle', debut: '2025-01-01', soumises: [], aujourdhui: REF });
  const r = rapprocherCourrierAED(analyse, cal, { societeId: 'soc_1', aujourdhui: REF });
  eq(r.periodeConcernee, '2026-T1');
  eq(r.statut, 'en_retard_confirme');
  eq(r.dossier.statut, 'en_retard');
  eq(r.dossier.echeance, '2026-06-30');
  eq(r.dossier.provenance.niveauConfiance, 'incertain');
  eq(r.dossier.societeId, 'soc_1');
});

console.log(`\n${passed} tests réussis, ${failed} échoués.`);
process.exit(failed === 0 ? 0 : 1);

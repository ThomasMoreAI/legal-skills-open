#!/usr/bin/env node
/**
 * test-particulier.js — Tests Milestone 6 : particuliers, salariés & frontaliers.
 */

import { chargerCatalogue, creerProfilUtilisateur } from '../lib/diagnostic/index.js';
import {
  determinerClasseImpot, parcoursParticulier, analyseFrontalier, analyseFichePaie, domainePourCategorie,
} from '../lib/particulier/index.js';

let passed = 0, failed = 0;
function test(name, fn) {
  try { fn(); console.log(`  ✓ ${name}`); passed++; }
  catch (e) { console.log(`  ✗ ${name}\n      ${e.message}`); failed++; }
}
function eq(a, b, msg) { if (a !== b) throw new Error(`${msg || ''}: attendu ${JSON.stringify(b)}, reçu ${JSON.stringify(a)}`); }
function truthy(v, msg) { if (!v) throw new Error(msg || 'attendu truthy'); }

const REF = '2026-07-13';
const { obligations } = chargerCatalogue();

console.log('=== Classe d\'impôt ===');

test('déduction de la classe selon la situation familiale', () => {
  eq(determinerClasseImpot({ situationFamiliale: 'celibataire' }).classe, '1');
  eq(determinerClasseImpot({ situationFamiliale: 'marie' }).classe, '2');
  eq(determinerClasseImpot({ situationFamiliale: 'veuf' }).classe, '1a');
  eq(determinerClasseImpot({ situationFamiliale: 'celibataire', nombreEnfants: 1 }).classe, '1a');
});

test('la classe déduite est tracée (source)', () => {
  truthy(determinerClasseImpot({ situationFamiliale: 'marie' }).provenance.source);
});

console.log('=== Parcours particulier ===');

const PROFIL = creerProfilUtilisateur({
  statutProfessionnel: 'salarie', situationFamiliale: 'marie', nombreEnfants: 2,
  frontalier: true, paysResidence: 'FR', maintenant: REF,
});
const parcours = parcoursParticulier(PROFIL, obligations, { aujourdhui: REF });

test('la classe d\'impôt est intégrée au parcours', () => {
  eq(parcours.classeImpot.classe, '2');
});

test('le domaine famille contient allocations et congé parental', () => {
  const ids = parcours.parDomaine.famille.map((i) => i.obligationId);
  truthy(ids.includes('obl_allocations_familiales'));
  truthy(ids.includes('obl_conge_parental'));
});

test('le domaine frontalier contient déclaration résidence et seuil télétravail', () => {
  const ids = parcours.parDomaine.frontalier.map((i) => i.obligationId);
  truthy(ids.includes('obl_frontalier_declaration_residence'));
  truthy(ids.includes('obl_frontalier_seuil_teletravail'));
});

test('le domaine fiscalité contient la déclaration modèle 100', () => {
  const ids = parcours.parDomaine.fiscalite.map((i) => i.obligationId);
  truthy(ids.includes('obl_irpp_declaration_modele100'));
});

test('domainePourCategorie mappe correctement', () => {
  eq(domainePourCategorie('frontalier'), 'frontalier');
  eq(domainePourCategorie('famille'), 'famille');
  eq(domainePourCategorie('fiscalite_personnelle'), 'fiscalite');
});

console.log('=== Analyse frontalière (réutilise lib/frontaliers) ===');

test('dépassement du seuil de jours déclenche une alerte', () => {
  const a = analyseFrontalier({ paysResidence: 'FR', joursHorsLU: 40 });
  eq(a.seuilJours, 34);
  eq(a.depassementSeuil, true);
  truthy(a.alerte);
});

test('sous le seuil, pas d\'alerte', () => {
  const a = analyseFrontalier({ paysResidence: 'BE', joursHorsLU: 10 });
  eq(a.depassementSeuil, false);
  eq(a.alerte, null);
});

test('le net réel frontalier est calculé quand le brut est fourni', () => {
  const a = analyseFrontalier({ paysResidence: 'FR', salaireBrutMensuel: 5000, classe: '1', joursHorsLU: 5 });
  truthy(a.net && a.net.netLuMensuel > 0);
  truthy(a.net.retenueLuMensuel > 0);
});

test('pays de résidence non pris en charge → erreur', () => {
  let ok = false; try { analyseFrontalier({ paysResidence: 'ES' }); } catch { ok = true; }
  truthy(ok);
});

console.log('=== Lecture de fiche de paie (réutilise lib/rts) ===');

test('recalcul du net mensuel, cohérent avec le net affiché', () => {
  const { netRecalcule } = analyseFichePaie({ salaireBrutMensuel: 5000, classe: '1' });
  truthy(netRecalcule > 0);
  const controle = analyseFichePaie({ salaireBrutMensuel: 5000, classe: '1', netAffiche: netRecalcule });
  eq(controle.coherent, true);
});

test('un net affiché incohérent est signalé', () => {
  const c = analyseFichePaie({ salaireBrutMensuel: 5000, classe: '1', netAffiche: 1 });
  eq(c.coherent, false);
  truthy(c.anomalies.some((a) => a.code === 'net_incoherent'));
});

console.log(`\n${passed} tests réussis, ${failed} échoués.`);
process.exit(failed === 0 ? 0 : 1);

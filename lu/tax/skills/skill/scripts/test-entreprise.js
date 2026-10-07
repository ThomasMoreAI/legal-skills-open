#!/usr/bin/env node
/**
 * test-entreprise.js — Tests Milestone 5 : cycle de vie de l'entreprise.
 */

import { chargerCatalogue, creerProfilSociete } from '../lib/diagnostic/index.js';
import {
  parcoursEntreprise, phasePourCategorie, echeancesParSociete, checklistCreation, PHASES,
} from '../lib/entreprise/index.js';

let passed = 0, failed = 0;
function test(name, fn) {
  try { fn(); console.log(`  ✓ ${name}`); passed++; }
  catch (e) { console.log(`  ✗ ${name}\n      ${e.message}`); failed++; }
}
function eq(a, b, msg) { if (a !== b) throw new Error(`${msg || ''}: attendu ${JSON.stringify(b)}, reçu ${JSON.stringify(a)}`); }
function truthy(v, msg) { if (!v) throw new Error(msg || 'attendu truthy'); }

const REF = '2026-07-13';
const { obligations } = chargerCatalogue();

const SARL = creerProfilSociete({
  nom: 'Acme SARL', formeJuridique: 'SARL', statut: 'actif',
  regimeTVA: 'normal', frequenceTVA: 'mensuelle', nbSalaries: 2, maintenant: REF,
});

console.log('=== Phases ===');

test('phasePourCategorie mappe correctement', () => {
  eq(phasePourCategorie('creation'), 'creation');
  eq(phasePourCategorie('fiscalite_entreprise'), 'fiscalite');
  eq(phasePourCategorie('employeur'), 'employeur');
  eq(phasePourCategorie('cessation'), 'cessation');
});

console.log('=== Parcours d\'une SARL active ===');

const parcours = parcoursEntreprise(SARL, obligations, { aujourdhui: REF });

test('la phase création contient l\'autorisation d\'établissement', () => {
  truthy(parcours.parPhase.creation.some((i) => i.obligationId === 'obl_autorisation_etablissement'));
});

test('la phase employeur contient la déclaration d\'entrée (car nbSalaries > 0)', () => {
  truthy(parcours.parPhase.employeur.some((i) => i.obligationId === 'obl_employeur_declaration_entree'));
});

test('la phase fiscalité contient l\'IRC et les acomptes', () => {
  const ids = parcours.parPhase.fiscalite.map((i) => i.obligationId);
  truthy(ids.includes('obl_irc_declaration'));
  truthy(ids.includes('obl_acomptes_irc_icc'));
});

test('la cessation n\'apparaît pas pour une société active', () => {
  const tous = parcours.chronologie.map((i) => i.obligationId);
  eq(tous.includes('obl_cessation_radiation'), false);
});

test('la chronologie est triée par échéance croissante', () => {
  const avecEcheance = parcours.chronologie.filter((i) => i.echeance).map((i) => i.echeance);
  const trie = [...avecEcheance].sort();
  eq(JSON.stringify(avecEcheance), JSON.stringify(trie));
});

test('les phases sont des clés valides', () => {
  for (const k of Object.keys(parcours.parPhase)) truthy(PHASES.includes(k), `phase inconnue : ${k}`);
});

console.log('=== Intégration du calendrier RCS (lib/lbr) ===');

test('avec une clôture d\'exercice, la phase vie intègre le dépôt des comptes', () => {
  const p = parcoursEntreprise(SARL, obligations, { aujourdhui: REF, exerciceFin: '2025-12-31' });
  const noms = p.parPhase.vie.map((i) => i.nom);
  truthy(noms.some((n) => /dépôt des comptes annuels au lbr/i.test(n)));
  truthy(noms.some((n) => /assemblée générale/i.test(n)));
});

console.log('=== Pièces manquantes ===');

test('sans documents fournis, chaque obligation liste ses pièces manquantes', () => {
  truthy(parcours.piecesManquantes.length >= 1);
  const autorisation = parcours.piecesManquantes.find((x) => x.obligationId === 'obl_autorisation_etablissement');
  truthy(autorisation && autorisation.manquantes.length >= 1);
});

test('une pièce déjà fournie disparaît des manquantes', () => {
  const p = parcoursEntreprise(SARL, obligations, {
    aujourdhui: REF,
    documentsFournis: ['Extrait de casier judiciaire du dirigeant'],
  });
  const autorisation = p.piecesManquantes.find((x) => x.obligationId === 'obl_autorisation_etablissement');
  truthy(autorisation, 'obligation autorisation absente');
  eq(autorisation.manquantes.some((m) => /casier judiciaire/i.test(m)), false);
});

console.log('=== Échéances classées par société ===');

test('echeancesParSociete indexe par identifiant de société', () => {
  const soc2 = creerProfilSociete({ id: 'soc_2', nom: 'Beta SA', formeJuridique: 'SA', statut: 'actif', regimeTVA: 'normal', frequenceTVA: 'trimestrielle', maintenant: REF });
  const map = echeancesParSociete([{ ...SARL, id: 'soc_1' }, soc2], obligations, { aujourdhui: REF });
  truthy(map.soc_1 && map.soc_2);
  truthy(Array.isArray(map.soc_1));
});

console.log('=== Checklist de création (réutilise lib/lbr) ===');

test('checklistCreation renvoie les pièces et le capital minimum d\'une SARL', () => {
  const c = checklistCreation('creation_sarl');
  eq(c.capital_minimum_eur, 12000);
  truthy(Array.isArray(c.pieces) && c.pieces.length >= 1);
});

console.log(`\n${passed} tests réussis, ${failed} échoués.`);
process.exit(failed === 0 ? 0 : 1);

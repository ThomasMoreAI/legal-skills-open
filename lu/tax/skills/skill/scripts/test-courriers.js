#!/usr/bin/env node
/**
 * test-courriers.js — Tests Milestone 9 : génération de courriers et dossiers.
 */

import {
  genererCourrier, rendreCourrier, courrierDepuisAnalyse, checklistRendezVous, genererDossierRecap, TYPES_COURRIER,
} from '../lib/courriers/index.js';
import { analyserDocument } from '../lib/documents/index.js';

let passed = 0, failed = 0;
function test(name, fn) {
  try { fn(); console.log(`  ✓ ${name}`); passed++; }
  catch (e) { console.log(`  ✗ ${name}\n      ${e.message}`); failed++; }
}
function eq(a, b, msg) { if (a !== b) throw new Error(`${msg || ''}: attendu ${JSON.stringify(b)}, reçu ${JSON.stringify(a)}`); }
function truthy(v, msg) { if (!v) throw new Error(msg || 'attendu truthy'); }

const REF = '2026-07-13';

console.log('=== Génération de courrier ===');

test('un courrier est toujours un PROJET (aucun envoi automatique)', () => {
  const c = genererCourrier('demande_delai', { expediteur: 'Jean Test', date: REF });
  eq(c.statut, 'projet');
  truthy(/aucun envoi/i.test(c.avertissement));
});

test('le courrier contient toutes les parties requises', () => {
  const c = genererCourrier('reponse_administration', {
    expediteur: { nom: 'Jean Test', adresse: '1 rue X', codePostalVille: 'L-1111 Luxembourg' },
    destinataire: { nom: 'AED' },
    references: ['LU12345678'],
    faits: 'Je fais suite à votre courrier du 3 juin 2026.',
    piecesJointes: ['Déclaration TVA T1 2026'],
    date: REF,
  });
  truthy(c.expediteur.nom && c.destinataire.nom);
  truthy(c.objet && c.demande && c.formulePolitesse && c.formuleAppel);
  eq(c.date, REF);
  truthy(c.references.includes('LU12345678'));
});

test('le rendu texte contient date, objet, références, pièces et signature', () => {
  const c = genererCourrier('transmission_pieces', {
    expediteur: 'Jean Test', destinataire: 'CCSS', references: ['REF-42'],
    piecesJointes: ['Contrat de travail'], date: REF,
  });
  const t = c.texte;
  truthy(t.includes(REF));
  truthy(/Objet :/.test(t));
  truthy(t.includes('REF-42'));
  truthy(t.includes('Contrat de travail'));
  truthy(t.includes('Jean Test'));
});

test('chaque type prédéfini produit un objet cohérent', () => {
  for (const type of Object.keys(TYPES_COURRIER)) {
    const c = genererCourrier(type, { expediteur: 'X', date: REF });
    truthy(c.objet && c.demande, `type ${type} incomplet`);
  }
});

test('un type inconnu lève une erreur', () => {
  let ok = false; try { genererCourrier('bidon', {}); } catch { ok = true; }
  truthy(ok);
});

console.log('=== Pré-remplissage depuis une analyse (M3) ===');

const COURRIER_AED = `Administration de l'Enregistrement, des Domaines et de la TVA (AED)
Réf : 2026/TVA/00987
Objet : Déclaration de TVA manquante — période T1 2026
Veuillez nous faire parvenir la déclaration au plus tard le 30/06/2026.`;

test('courrierDepuisAnalyse reprend administration, références et période', () => {
  const analyse = analyserDocument(COURRIER_AED, { nom: 'aed.txt', aujourdhui: REF });
  const c = courrierDepuisAnalyse(analyse, { expediteur: 'Jean Test', date: REF });
  eq(c.destinataire.nom, analyse.administration.nom);
  truthy(c.references.includes('2026/TVA/00987'));
  truthy(/T1 2026/.test(c.faits));
  eq(c.statut, 'projet');
});

console.log('=== Checklist de rendez-vous ===');

test('checklistRendezVous adapte selon le type', () => {
  const base = checklistRendezVous('administration');
  const notaire = checklistRendezVous('notaire');
  truthy(base.length >= 3);
  truthy(notaire.some((x) => /bëllegen akt/i.test(x)));
});

console.log('=== Dossier récapitulatif ===');

test('genererDossierRecap produit un Markdown avec les sections attendues', () => {
  const md = genererDossierRecap({
    titre: 'Mon dossier',
    profil: { type: 'ProfilUtilisateur', prenom: 'Jean', paysResidence: 'LU' },
    dossiers: [{ typeDemarche: 'Déclaration TVA', statut: 'a_preparer', echeance: '2026-08-15', administration: 'AED' }],
    documents: [{ nom: 'aed.txt', typeDocument: 'declaration_tva', validationHumaineRequise: true }],
    aujourdhui: REF,
  });
  truthy(md.includes('# Mon dossier'));
  truthy(/## Dossiers/.test(md));
  truthy(/## Documents/.test(md));
  truthy(/Validation humaine requise/.test(md));
  truthy(/Aucune démarche n'a été envoyée/.test(md));
});

console.log(`\n${passed} tests réussis, ${failed} échoués.`);
process.exit(failed === 0 ? 0 : 1);

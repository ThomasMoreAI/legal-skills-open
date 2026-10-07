#!/usr/bin/env node
/**
 * test-diagnostic.js — Tests du moteur de diagnostic administratif (Milestone 1).
 */

import {
  creerProfilUtilisateur,
  creerProfilSociete,
  creerDossier,
  creerDocument,
  creerObligation,
  creerProvenance,
  evaluerFraicheur,
  diagnostiquer,
  obligationApplicable,
  evaluerCondition,
  calculerEcheance,
  dossierDepuisObligation,
  prioriteSelonEcheance,
  creerStoreMemoire,
  chargerCatalogue,
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

console.log('=== Provenance (traçabilité obligatoire) ===');

test('creerProvenance exige une source', () => {
  throws(() => creerProvenance({ dateVerification: '2026-01-01' }), 'source manquante non détectée');
});

test('creerProvenance exige une date de vérification valide', () => {
  throws(() => creerProvenance({ source: 'x', dateVerification: '2026-99-99' }));
});

test('niveauConfiance "incertain" force la validation humaine', () => {
  const p = creerProvenance({ source: 'x', dateVerification: '2026-01-01', niveauConfiance: 'incertain' });
  eq(p.validationHumaineRequise, true);
});

test('evaluerFraicheur signale une info trop ancienne', () => {
  const p = creerProvenance({ source: 'x', dateVerification: '2020-01-01' });
  const f = evaluerFraicheur(p, { aujourdhui: REF });
  eq(f.aRevalider, true);
  truthy(f.message);
});

test('evaluerFraicheur accepte une info récente', () => {
  const p = creerProvenance({ source: 'x', dateVerification: '2026-06-15' });
  const f = evaluerFraicheur(p, { aujourdhui: REF });
  eq(f.aRevalider, false);
  eq(f.message, null);
});

console.log('=== Entités ===');

test('creerProfilUtilisateur applique des défauts sûrs', () => {
  const u = creerProfilUtilisateur({ prenom: 'Jean', maintenant: REF });
  eq(u.type, 'ProfilUtilisateur');
  eq(u.langue, 'fr');
  eq(u.nombreEnfants, 0);
  eq(u.frontalier, false);
  eq(u.dateMiseAJour, REF);
});

test('creerProfilUtilisateur rejette une situation familiale invalide', () => {
  throws(() => creerProfilUtilisateur({ situationFamiliale: 'divorcé' }));
});

test('creerProfilSociete exige un nom', () => {
  throws(() => creerProfilSociete({}));
});

test('creerDossier impose une provenance si échéance présente', () => {
  throws(() => creerDossier({ categorie: 'tva', echeance: '2026-08-15' }), 'provenance manquante non détectée');
});

test('creerDossier accepte une échéance avec provenance', () => {
  const d = creerDossier({
    categorie: 'tva', echeance: '2026-08-15',
    provenance: { source: 'x', dateVerification: '2026-06-15' },
  });
  eq(d.echeance, '2026-08-15');
});

test('creerDocument est incertain et à valider par défaut', () => {
  const doc = creerDocument({ nom: 'courrier-aed.pdf' });
  eq(doc.niveauConfiance, 'incertain');
  eq(doc.validationHumaineRequise, true);
});

test('creerObligation refuse une obligation sans source', () => {
  throws(() => creerObligation({ nom: 'x', categorie: 'tva' }), 'obligation sans source acceptée');
});

console.log('=== Moteur : conditions & applicabilité ===');

const obTvaMensuelle = creerObligation({
  id: 'obl_test_tva',
  nom: 'Déclaration TVA mensuelle',
  categorie: 'tva',
  frequence: 'mensuelle',
  dateLimite: 'jour:15',
  conditionsApplicabilite: [
    { champ: 'regimeTVA', operateur: 'different', valeur: 'non_assujetti' },
    { champ: 'frequenceTVA', operateur: 'egal', valeur: 'mensuelle' },
  ],
  provenance: { source: 'https://aed.public.lu', dateVerification: '2026-06-15' },
});

test('evaluerCondition — egal', () => {
  eq(evaluerCondition({ frequenceTVA: 'mensuelle' }, { champ: 'frequenceTVA', operateur: 'egal', valeur: 'mensuelle' }), true);
});

test('evaluerCondition — vrai', () => {
  eq(evaluerCondition({ frontalier: true }, { champ: 'frontalier', operateur: 'vrai' }), true);
  eq(evaluerCondition({ frontalier: false }, { champ: 'frontalier', operateur: 'vrai' }), false);
});

test('obligation applicable à une société assujettie mensuelle', () => {
  const soc = creerProfilSociete({ nom: 'Acme', regimeTVA: 'normal', frequenceTVA: 'mensuelle', maintenant: REF });
  const r = obligationApplicable(soc, obTvaMensuelle);
  eq(r.applicable, true);
  truthy(r.raisons.length >= 2);
});

test('obligation NON applicable à une société non assujettie', () => {
  const soc = creerProfilSociete({ nom: 'Acme', regimeTVA: 'non_assujetti', frequenceTVA: 'non_applicable', maintenant: REF });
  const r = obligationApplicable(soc, obTvaMensuelle);
  eq(r.applicable, false);
});

test('champ manquant → à clarifier (informations manquantes)', () => {
  const soc = creerProfilSociete({ nom: 'Acme', maintenant: REF }); // pas de regimeTVA
  const r = obligationApplicable(soc, obTvaMensuelle);
  eq(r.applicable, false);
  truthy(r.manquantes.includes('regimeTVA'));
});

console.log('=== Moteur : échéances déterministes ===');

test('échéance mensuelle = 15 du mois suivant', () => {
  eq(calculerEcheance(obTvaMensuelle, { aujourdhui: '2026-07-12' }), '2026-08-15');
});

test('échéance mensuelle gère le passage d\'année', () => {
  eq(calculerEcheance(obTvaMensuelle, { aujourdhui: '2026-12-20' }), '2027-01-15');
});

test('échéance trimestrielle = 15 du mois suivant la fin de trimestre', () => {
  const ob = creerObligation({ nom: 'TVA T', categorie: 'tva', frequence: 'trimestrielle', dateLimite: 'jour:15', provenance: { source: 'x', dateVerification: '2026-06-15' } });
  eq(calculerEcheance(ob, { aujourdhui: '2026-05-10' }), '2026-07-15'); // T2 finit en juin
});

test('échéance annuelle = prochaine occurrence MM-JJ', () => {
  const ob = creerObligation({ nom: 'IRPP', categorie: 'fisc', frequence: 'annuelle', dateLimite: '12-31', provenance: { source: 'x', dateVerification: '2026-06-15' } });
  eq(calculerEcheance(ob, { aujourdhui: '2026-07-12' }), '2026-12-31');
  eq(calculerEcheance(ob, { aujourdhui: '2027-01-05' }), '2027-12-31');
});

test('prioriteSelonEcheance — échéance dans 10 jours = obligatoire_maintenant', () => {
  eq(prioriteSelonEcheance('2026-07-22', REF), 'obligatoire_maintenant');
});

test('prioriteSelonEcheance — échéance dans 200 jours = a_surveiller', () => {
  eq(prioriteSelonEcheance('2027-02-01', REF), 'a_surveiller');
});

console.log('=== Diagnostic complet & dossier ===');

test('diagnostiquer ventile applicables / à clarifier / non applicables', () => {
  const catalogue = [
    obTvaMensuelle,
    creerObligation({ nom: 'RBE', categorie: 'societe', frequence: 'ponctuelle', conditionsApplicabilite: [{ champ: 'statut', operateur: 'egal', valeur: 'actif' }], provenance: { source: 'https://lbr.lu', dateVerification: '2026-06-15' } }),
  ];
  const soc = creerProfilSociete({ nom: 'Acme', regimeTVA: 'normal', frequenceTVA: 'mensuelle', statut: 'actif', maintenant: REF });
  const { applicables } = diagnostiquer(soc, catalogue, { aujourdhui: REF });
  eq(applicables.length, 2);
});

test('dossierDepuisObligation reprend la source de l\'obligation', () => {
  const entree = { obligation: obTvaMensuelle, raisons: ['frequenceTVA = mensuelle'], echeance: '2026-08-15' };
  const dossier = dossierDepuisObligation(entree, { societeId: 'soc_1', aujourdhui: REF });
  eq(dossier.type, 'Dossier');
  eq(dossier.echeance, '2026-08-15');
  eq(dossier.provenance.source, 'https://aed.public.lu');
  eq(dossier.societeId, 'soc_1');
  truthy(dossier.priorite);
});

console.log('=== Store (persistance isolée) ===');

test('le store attribue des ids déterministes et isole par propriétaire', () => {
  const store = creerStoreMemoire();
  const u = store.ajouter('profils', creerProfilUtilisateur({ prenom: 'Jean', maintenant: REF }));
  eq(u.id, 'usr_1');
  const soc = store.ajouter('societes', creerProfilSociete({ nom: 'Acme', maintenant: REF }));
  eq(soc.id, 'soc_1');
  store.ajouter('dossiers', creerDossier({ categorie: 'tva', profilId: 'usr_1', dateCreation: REF }));
  store.ajouter('dossiers', creerDossier({ categorie: 'rcs', profilId: 'usr_2', dateCreation: REF }));
  eq(store.listerPour('dossiers', { profilId: 'usr_1' }).length, 1);
});

test('le store supprime (droit à l\'effacement) et exporte (portabilité)', () => {
  const store = creerStoreMemoire();
  const u = store.ajouter('profils', creerProfilUtilisateur({ prenom: 'A', maintenant: REF }));
  eq(store.supprimer('profils', u.id), true);
  eq(store.exporter().profils.length, 0);
});

console.log('=== Catalogue sourcé (data/obligations.json) ===');

test('le catalogue se charge et chaque obligation possède une source', () => {
  const { obligations, as_of } = chargerCatalogue();
  truthy(as_of, 'as_of manquant');
  truthy(obligations.length >= 1);
  for (const ob of obligations) {
    truthy(ob.provenance && ob.provenance.source, `obligation ${ob.id} sans source`);
    truthy(ob.provenance.dateVerification, `obligation ${ob.id} sans dateVerification`);
  }
});

test('scénario 1re livraison : indépendant/société TVA mensuelle → obligation détectée', () => {
  const { obligations } = chargerCatalogue();
  const soc = creerProfilSociete({ nom: 'Indep SARL-S', regimeTVA: 'normal', frequenceTVA: 'mensuelle', statut: 'actif', maintenant: REF });
  const { applicables } = diagnostiquer(soc, obligations, { aujourdhui: REF });
  const tva = applicables.find((e) => e.obligation.categorie === 'tva' && e.obligation.frequence === 'mensuelle');
  truthy(tva, 'obligation TVA mensuelle non détectée');
  eq(tva.echeance, '2026-08-15');
});

console.log(`\n${passed} tests réussis, ${failed} échoués.`);
process.exit(failed === 0 ? 0 : 1);

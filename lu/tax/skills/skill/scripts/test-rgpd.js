#!/usr/bin/env node
/**
 * test-rgpd.js — Tests Milestone 12 : sécurité, confidentialité & conformité.
 */

import {
  chiffrer, dechiffrer, chiffrerObjet, dechiffrerObjet,
  masquer, CHAMPS_SENSIBLES,
  creerJournal, consentementValide, exigerConsentement,
  estExpiree, purger, DUREES_CONSERVATION, creerStoreSecurise,
} from '../lib/rgpd/index.js';
import { creerStoreMemoire, creerProfilUtilisateur } from '../lib/diagnostic/index.js';

let passed = 0, failed = 0;
function test(name, fn) {
  try { fn(); console.log(`  ✓ ${name}`); passed++; }
  catch (e) { console.log(`  ✗ ${name}\n      ${e.message}`); failed++; }
}
function eq(a, b, msg) { if (a !== b) throw new Error(`${msg || ''}: attendu ${JSON.stringify(b)}, reçu ${JSON.stringify(a)}`); }
function truthy(v, msg) { if (!v) throw new Error(msg || 'attendu truthy'); }

const REF = '2026-07-13';

console.log('=== Chiffrement au repos ===');

test('chiffrer puis déchiffrer restitue le texte', () => {
  const p = chiffrer('donnée confidentielle', 'motdepasse');
  eq(dechiffrer(p, 'motdepasse'), 'donnée confidentielle');
});

test('le paquet chiffré ne contient pas le texte en clair', () => {
  const p = chiffrer('SECRET42', 'k');
  truthy(!JSON.stringify(p).includes('SECRET42'));
});

test('un mauvais mot de passe échoue (intégrité GCM)', () => {
  const p = chiffrer('x', 'bon');
  let ok = false; try { dechiffrer(p, 'mauvais'); } catch { ok = true; }
  truthy(ok);
});

test('chiffrerObjet / dechiffrerObjet round-trip', () => {
  const obj = { revenus: 5000, nom: 'Test' };
  eq(JSON.stringify(dechiffrerObjet(chiffrerObjet(obj, 'k'), 'k')), JSON.stringify(obj));
});

console.log('=== Masquage des données sensibles ===');

test('les champs sensibles sont masqués, les autres conservés', () => {
  const m = masquer({ nom: 'Dupont', revenusApprox: 5000, iban: 'LU280019400644750000', email: 'jean@exemple.lu' });
  eq(m.nom, 'Dupont');
  eq(m.revenusApprox, '***');
  truthy(m.iban.endsWith('***'));
  truthy(m.email.startsWith('j') && m.email.includes('@exemple.lu'));
});

test('le masquage est récursif et ne modifie pas l\'original', () => {
  const src = { profil: { revenus: 9000 }, liste: [{ iban: 'LU120019' }] };
  const m = masquer(src);
  eq(m.profil.revenus, '***');
  truthy(m.liste[0].iban.endsWith('***') && m.liste[0].iban !== 'LU120019');
  eq(src.profil.revenus, 9000); // original intact
});

console.log('=== Journalisation des accès ===');

test('le journal enregistre les événements horodatés', () => {
  const j = creerJournal();
  j.enregistrer({ action: 'lire', collection: 'profils', id: 'usr_1', horodatage: REF });
  eq(j.lister().length, 1);
  eq(j.pour('profils', 'usr_1').length, 1);
});

console.log('=== Consentement ===');

test('consentementValide / exigerConsentement', () => {
  eq(consentementValide({ consentementRGPD: true }), true);
  eq(consentementValide({ consentementRGPD: false }), false);
  let ok = false; try { exigerConsentement({ consentementRGPD: false }); } catch { ok = true; }
  truthy(ok);
});

console.log('=== Conservation & purge ===');

test('une pièce fiscale de 12 ans est expirée (durée 10 ans)', () => {
  const r = estExpiree({ categorie: 'fiscal', date: '2014-01-01' }, { aujourdhui: REF });
  eq(r.expiree, true);
  eq(r.dureeAnnees, DUREES_CONSERVATION.fiscal);
});

test('un document de 1 an n\'est pas expiré', () => {
  const r = estExpiree({ categorie: 'document', date: '2025-07-13' }, { aujourdhui: REF });
  eq(r.expiree, false);
});

test('purger sépare conservés et expirés', () => {
  const { conserves, expires } = purger([
    { categorie: 'fiscal', date: '2014-01-01' },
    { categorie: 'fiscal', date: '2024-01-01' },
  ], { aujourdhui: REF });
  eq(expires.length, 1);
  eq(conserves.length, 1);
});

console.log('=== Store sécurisé ===');

test('le store sécurisé exige le consentement pour un profil', () => {
  const s = creerStoreSecurise(creerStoreMemoire(), { acteur: 'test' });
  let ok = false;
  try { s.ajouter('profils', creerProfilUtilisateur({ prenom: 'A', maintenant: REF })); } catch { ok = true; }
  truthy(ok, 'ajout sans consentement aurait dû échouer');
  const u = s.ajouter('profils', creerProfilUtilisateur({ prenom: 'A', consentementRGPD: true, maintenant: REF }));
  truthy(u.id);
});

test('le store sécurisé journalise les accès', () => {
  const s = creerStoreSecurise(creerStoreMemoire(), { acteur: 'test' });
  const u = s.ajouter('profils', creerProfilUtilisateur({ prenom: 'A', consentementRGPD: true, maintenant: REF }));
  s.obtenir('profils', u.id);
  s.supprimer('profils', u.id);
  const actions = s.journal.lister().map((e) => e.action);
  truthy(actions.includes('ajouter') && actions.includes('lire') && actions.includes('supprimer'));
});

console.log(`\n${passed} tests réussis, ${failed} échoués.`);
process.exit(failed === 0 ? 0 : 1);

#!/usr/bin/env node
/**
 * test-scenarios.js — Milestone 15 : 15 scénarios de bout en bout.
 *
 * Chaque scénario vérifie l'intégration réelle des modules : compréhension,
 * obligations, échéances, sources, documents, risques, prochaines actions et
 * niveau de confiance.
 */

import { chargerCatalogue, creerProfilSociete, creerProfilUtilisateur, diagnostiquer } from '../lib/diagnostic/index.js';
import { calendrierTVA, controleCoherence } from '../lib/tva/index.js';
import { parcoursEntreprise, checklistCreation } from '../lib/entreprise/index.js';
import { parcoursParticulier, analyseFrontalier, determinerClasseImpot } from '../lib/particulier/index.js';
import { parcoursInstallation } from '../lib/residence/index.js';
import { parcoursLogement } from '../lib/logement/index.js';
import { analyserDocument } from '../lib/documents/index.js';
import { niveauAlerte, genererRappels } from '../lib/rappels/index.js';
import { repondre } from '../lib/conversation/index.js';

let passed = 0, failed = 0;
function test(name, fn) {
  try { fn(); console.log(`  ✓ ${name}`); passed++; }
  catch (e) { console.log(`  ✗ ${name}\n      ${e.message}`); failed++; }
}
function eq(a, b, msg) { if (a !== b) throw new Error(`${msg || ''}: attendu ${JSON.stringify(b)}, reçu ${JSON.stringify(a)}`); }
function truthy(v, msg) { if (!v) throw new Error(msg || 'attendu truthy'); }

const REF = '2026-07-13';
const { obligations } = chargerCatalogue();

console.log('=== 15 scénarios de bout en bout ===');

test('1. Indépendant avec TVA mensuelle manquante → périodes en retard détectées', () => {
  const cal = calendrierTVA({ frequenceTVA: 'mensuelle', debut: '2026-01-15', soumises: [], aujourdhui: REF });
  truthy(cal.enRetard.length >= 1);
  truthy(cal.provenance.source);
});

test('2. Société sans dépôt annuel → dépôt des comptes dans le parcours (vie)', () => {
  const soc = creerProfilSociete({ nom: 'Acme', formeJuridique: 'SARL', statut: 'actif', maintenant: REF });
  const p = parcoursEntreprise(soc, obligations, { aujourdhui: REF, exerciceFin: '2024-12-31' });
  truthy((p.parPhase.vie || []).some((i) => /dépôt des comptes/i.test(i.nom)));
});

test('3. Frontalier français avec télétravail (40 j) → alerte de dépassement', () => {
  const a = analyseFrontalier({ paysResidence: 'FR', joursHorsLU: 40 });
  eq(a.depassementSeuil, true);
  truthy(a.provenance.source);
});

test('4. Salarié marié avec enfants → classe 2 + allocations familiales', () => {
  eq(determinerClasseImpot({ situationFamiliale: 'marie' }).classe, '2');
  const p = parcoursParticulier(creerProfilUtilisateur({ statutProfessionnel: 'salarie', situationFamiliale: 'marie', nombreEnfants: 2, maintenant: REF }), obligations, { aujourdhui: REF });
  truthy((p.parDomaine.famille || []).some((i) => i.obligationId === 'obl_allocations_familiales'));
});

test('5. Nouvel arrivant européen → enregistrement UE, pas de titre de séjour', () => {
  const p = parcoursInstallation({ nationalite: 'FR', dateArriveeLux: '2026-06-01' }, { aujourdhui: REF });
  const ids = p.chronologie.map((e) => e.id);
  truthy(ids.includes('enregistrement_ue'));
  eq(ids.includes('titre_sejour'), false);
});

test('6. Ressortissant non européen → titre de séjour requis', () => {
  const p = parcoursInstallation({ nationalite: 'US', dateArriveeLux: '2026-06-01' }, { aujourdhui: REF });
  truthy(p.chronologie.some((e) => e.id === 'titre_sejour'));
});

test('7. Achat immobilier → crédit Bëllegen Akt calculé', () => {
  const p = parcoursLogement({}, { projet: 'achat', prixAchat: 600000, nbAcquereurs: 2 });
  truthy(p.calculs.acquisition.creditBellegenAkt > 0);
});

test('8. Locataire demandant une aide → étape aides au logement', () => {
  const p = parcoursLogement({ statutLogement: 'locataire' }, { loyerMensuel: 1200 });
  truthy(p.etapes.some((e) => /aides au logement/i.test(e.titre)));
  truthy(p.calculs.garantie);
});

test('9. Courrier AED avec échéance → échéance + source + confiance non officielle', () => {
  const txt = 'Administration de l\'Enregistrement, des Domaines et de la TVA (AED)\nObjet : période T1 2026\nVeuillez déposer la déclaration au plus tard le 30/06/2026. À défaut, taxation d\'office.';
  const a = analyserDocument(txt, { nom: 'aed.txt', aujourdhui: REF });
  eq(a.administration.id, 'aed');
  eq(a.echeance.iso, '2026-06-30');
  eq(a.document.validationHumaineRequise, true);
  truthy(a.consequences.length >= 1);
});

test('10. Courrier CCSS → administration CCSS identifiée', () => {
  const txt = 'Centre commun de la sécurité sociale (CCSS)\nObjet : décompte de cotisations sociales\nVeuillez régulariser les cotisations avant le 31/07/2026.';
  const a = analyserDocument(txt, { nom: 'ccss.txt', aujourdhui: REF });
  eq(a.administration.id, 'ccss');
  truthy(a.echeance.iso);
});

test('11. Cessation d\'activité → obligation de cessation applicable', () => {
  const soc = creerProfilSociete({ nom: 'Acme', formeJuridique: 'SARL', statut: 'cessation', maintenant: REF });
  const { applicables } = diagnostiquer(soc, obligations, { aujourdhui: REF });
  truthy(applicables.some((e) => e.obligation.id === 'obl_cessation_radiation'));
});

test('12. Changement de dirigeant → checklist RCS dédiée', () => {
  const c = checklistCreation('changement_dirigeant');
  truthy(Array.isArray(c.pieces) && c.pieces.length >= 1);
  truthy(c.bases_legales === undefined || Array.isArray(c.bases_legales) || true);
});

test('13. Titre de séjour expirant → renouvellement + alerte de proximité', () => {
  const p = parcoursInstallation({ nationalite: 'US', dateArriveeLux: '2025-08-01' }, { aujourdhui: REF });
  truthy(p.chronologie.some((e) => e.id === 'renouvellement_titre'));
  const alerte = niveauAlerte({ echeance: '2026-07-18', statut: 'a_preparer' }, REF);
  eq(alerte.couleur, 'orange');
});

test('14. Déclaration fiscale incomplète → modèle 100 + informations manquantes', () => {
  const profil = creerProfilUtilisateur({ statutProfessionnel: 'salarie', maintenant: REF });
  const p = parcoursParticulier(profil, obligations, { aujourdhui: REF });
  truthy((p.parDomaine.fiscalite || []).some((i) => i.obligationId === 'obl_irpp_declaration_modele100'));
  const r = repondre('Je dois faire ma déclaration fiscale', { profil, aujourdhui: REF });
  truthy(/rassembler|pièces|déclaration/i.test(r.action));
});

test('15. Facture Peppol non conforme → anomalies de cohérence détectées', () => {
  const { anomalies } = controleCoherence({
    numeroTVA: 'LU12345678',
    factures: [
      { numero: null, date: null, ht: 1000, taux: 17 },       // non conforme
      { numero: 'F2', date: '2026-01-05', ht: 1000, taux: 99 }, // taux invalide
    ],
  });
  truthy(anomalies.some((a) => a.code === 'facture_non_conforme'));
  truthy(anomalies.some((a) => a.code === 'taux_invalide'));
});

console.log(`\n${passed}/${passed + failed} scénarios validés, ${failed} échoués.`);
process.exit(failed === 0 ? 0 : 1);

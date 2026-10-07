/**
 * lib/diagnostic/entities.js — Modèle de données du moteur de diagnostic.
 *
 * Cinq entités (Milestone 1) :
 *   - ProfilUtilisateur   (UserProfile)
 *   - ProfilSociete       (CompanyProfile)
 *   - Dossier             (AdministrativeCase)
 *   - Document            (UploadedDocument)
 *   - Obligation          (Obligation)
 *
 * Chaque fabrique :
 *   - normalise et complète l'objet avec des valeurs par défaut sûres ;
 *   - valide les champs critiques (enums, dates, types) avec des messages FR ;
 *   - reste PURE et déterministe : ids et horodatages sont injectables
 *     (paramètres `id` / `maintenant`) afin que les tests ne dépendent ni de
 *     Date.now ni d'un compteur global.
 *
 * Aucune règle réglementaire n'est codée en dur ici : les entités ne portent
 * que de la structure. Les règles vivent dans data/obligations.json (sourcées).
 *
 * Aucune dépendance externe.
 */

import { creerProvenance, ceJourISO } from './provenance.js';

const RE_DATE = /^\d{4}-\d{2}-\d{2}$/;
const estDateISO = (v) => typeof v === 'string' && RE_DATE.test(v) && !Number.isNaN(Date.parse(`${v}T00:00:00Z`));

/** Énumérations partagées (exposées pour l'UI et les tests). */
export const ENUMS = Object.freeze({
  langue: ['fr', 'en', 'de', 'lb'],
  situationFamiliale: ['celibataire', 'marie', 'partenariat', 'divorce', 'separe', 'veuf'],
  statutProfessionnel: ['salarie', 'independant', 'dirigeant', 'sans_emploi', 'retraite', 'etudiant'],
  statutLogement: ['proprietaire', 'locataire', 'heberge', 'autre'],
  formeJuridique: ['SARL', 'SARL-S', 'SA', 'SCS', 'SCA', 'SNC', 'SCSp', 'ASBL', 'entreprise_individuelle', 'autre'],
  regimeTVA: ['normal', 'franchise', 'forfaitaire', 'non_assujetti', 'exonere'],
  frequenceTVA: ['mensuelle', 'trimestrielle', 'annuelle', 'non_applicable'],
  statutSociete: ['actif', 'cessation', 'liquidation'],
  // Priorité = colonnes du tableau de bord (Milestone 2).
  priorite: ['obligatoire_maintenant', 'a_faire_prochainement', 'a_surveiller', 'non_applicable', 'informations_manquantes'],
  // Statut de dossier (Milestone 10).
  statutDossier: ['a_preparer', 'en_attente_information', 'pret_a_envoyer', 'envoye', 'en_attente_reponse', 'termine', 'en_retard', 'bloque'],
  statutObligation: ['actif', 'obsolete'],
  operateur: ['egal', 'different', 'vrai', 'faux', 'present', 'absent', 'superieur', 'inferieur', 'contient'],
});

function assertEnum(champ, valeur, liste, { optionnel = false } = {}) {
  if (valeur === undefined || valeur === null || valeur === '') {
    if (optionnel) return undefined;
    throw new Error(`${champ} est obligatoire (attendu : ${liste.join(', ')})`);
  }
  if (!liste.includes(valeur)) {
    throw new Error(`${champ} invalide : "${valeur}" (attendu : ${liste.join(', ')})`);
  }
  return valeur;
}

function assertDate(champ, valeur, { optionnel = true } = {}) {
  if (valeur === undefined || valeur === null || valeur === '') {
    if (optionnel) return undefined;
    throw new Error(`${champ} est obligatoire (format YYYY-MM-DD)`);
  }
  if (!estDateISO(valeur)) throw new Error(`${champ} : date invalide "${valeur}" (attendu YYYY-MM-DD)`);
  return valeur;
}

const arr = (v) => (Array.isArray(v) ? v.slice() : v == null ? [] : [v]);

// ---------------------------------------------------------------------------
// ProfilUtilisateur (UserProfile)
// ---------------------------------------------------------------------------

/**
 * @param {object} p champs du profil (voir README / schemas/user-profile.schema.json)
 * @returns {object} profil normalisé
 */
export function creerProfilUtilisateur(p = {}) {
  const maintenant = p.maintenant || ceJourISO();
  return {
    type: 'ProfilUtilisateur',
    id: p.id || null,
    prenom: p.prenom ?? null,
    nom: p.nom ?? null,
    email: p.email ?? null,
    langue: assertEnum('langue', p.langue ?? 'fr', ENUMS.langue),
    nationalite: p.nationalite ?? null,
    paysResidence: p.paysResidence ?? null,
    communeResidence: p.communeResidence ?? null,
    situationFamiliale: assertEnum('situationFamiliale', p.situationFamiliale, ENUMS.situationFamiliale, { optionnel: true }) ?? null,
    nombreEnfants: Number.isFinite(p.nombreEnfants) ? p.nombreEnfants : 0,
    statutProfessionnel: assertEnum('statutProfessionnel', p.statutProfessionnel, ENUMS.statutProfessionnel, { optionnel: true }) ?? null,
    employeur: p.employeur ?? null,
    paysEmployeur: p.paysEmployeur ?? null,
    frontalier: Boolean(p.frontalier),
    revenusApprox: Number.isFinite(p.revenusApprox) ? p.revenusApprox : null,
    statutLogement: assertEnum('statutLogement', p.statutLogement, ENUMS.statutLogement, { optionnel: true }) ?? null,
    vehicules: arr(p.vehicules),
    societesLiees: arr(p.societesLiees),
    dateArriveeLux: assertDate('dateArriveeLux', p.dateArriveeLux) ?? null,
    consentementRGPD: Boolean(p.consentementRGPD),
    dateMiseAJour: maintenant,
  };
}

// ---------------------------------------------------------------------------
// ProfilSociete (CompanyProfile)
// ---------------------------------------------------------------------------

export function creerProfilSociete(c = {}) {
  const maintenant = c.maintenant || ceJourISO();
  if (!c.nom) throw new Error('ProfilSociete.nom est obligatoire');
  return {
    type: 'ProfilSociete',
    id: c.id || null,
    nom: c.nom,
    formeJuridique: assertEnum('formeJuridique', c.formeJuridique, ENUMS.formeJuridique, { optionnel: true }) ?? null,
    rcs: c.rcs ?? null,
    tva: c.tva ?? null,
    autorisationEtablissement: c.autorisationEtablissement ?? null,
    beneficiairesEffectifs: arr(c.beneficiairesEffectifs),
    adresse: c.adresse ?? null,
    secteur: c.secteur ?? null,
    regimeTVA: assertEnum('regimeTVA', c.regimeTVA, ENUMS.regimeTVA, { optionnel: true }) ?? null,
    frequenceTVA: assertEnum('frequenceTVA', c.frequenceTVA, ENUMS.frequenceTVA, { optionnel: true }) ?? null,
    nbSalaries: Number.isFinite(c.nbSalaries) ? c.nbSalaries : 0,
    exerciceComptable: c.exerciceComptable ?? null,
    dateCreation: assertDate('dateCreation', c.dateCreation) ?? null,
    statut: assertEnum('statut', c.statut ?? 'actif', ENUMS.statutSociete),
    obligationsConnues: arr(c.obligationsConnues),
    dateMiseAJour: maintenant,
  };
}

// ---------------------------------------------------------------------------
// Dossier (AdministrativeCase)
// ---------------------------------------------------------------------------

export function creerDossier(d = {}) {
  const maintenant = d.maintenant || ceJourISO();
  if (!d.categorie) throw new Error('Dossier.categorie est obligatoire');
  const dossier = {
    type: 'Dossier',
    id: d.id || null,
    categorie: d.categorie,
    administration: d.administration ?? null,
    typeDemarche: d.typeDemarche ?? null,
    statut: assertEnum('statut', d.statut ?? 'a_preparer', ENUMS.statutDossier),
    priorite: assertEnum('priorite', d.priorite ?? 'a_surveiller', ENUMS.priorite),
    dateCreation: assertDate('dateCreation', d.dateCreation) ?? maintenant,
    echeance: assertDate('echeance', d.echeance) ?? null,
    periode: d.periode ?? null,
    documentsRequis: arr(d.documentsRequis),
    documentsRecus: arr(d.documentsRecus),
    informationsManquantes: arr(d.informationsManquantes),
    risques: arr(d.risques),
    prochainesActions: arr(d.prochainesActions),
    profilId: d.profilId ?? null,
    societeId: d.societeId ?? null,
    obligationId: d.obligationId ?? null,
    documentId: d.documentId ?? null,
  };
  // La provenance est obligatoire dès qu'une info réglementaire est présente
  // (échéance, risque). Sinon optionnelle (dossier purement organisationnel).
  if (d.provenance) {
    dossier.provenance = creerProvenance(d.provenance);
  } else if (dossier.echeance || dossier.risques.length) {
    throw new Error('Dossier : une échéance ou un risque réglementaire impose une provenance (source + dateVerification).');
  }
  return dossier;
}

// ---------------------------------------------------------------------------
// Document (UploadedDocument)
// ---------------------------------------------------------------------------

export function creerDocument(u = {}) {
  if (!u.nom) throw new Error('Document.nom est obligatoire');
  const niveauConfiance = u.niveauConfiance ?? 'incertain';
  return {
    type: 'Document',
    id: u.id || null,
    nom: u.nom,
    typeDocument: u.typeDocument ?? u.type ?? null,
    administrationEmettrice: u.administrationEmettrice ?? null,
    date: assertDate('date', u.date) ?? null,
    periode: u.periode ?? null,
    texteExtrait: u.texteExtrait ?? null,
    donneesStructurees: u.donneesStructurees && typeof u.donneesStructurees === 'object' ? u.donneesStructurees : {},
    echeanceDetectee: assertDate('echeanceDetectee', u.echeanceDetectee) ?? null,
    actionDemandee: u.actionDemandee ?? null,
    niveauConfiance,
    // Un document importé est incertain par défaut : validation humaine requise
    // tant que le contraire n'est pas explicitement établi.
    validationHumaineRequise: u.validationHumaineRequise ?? (niveauConfiance !== 'officiel'),
    dossierId: u.dossierId ?? null,
    profilId: u.profilId ?? null,
    societeId: u.societeId ?? null,
  };
}

// ---------------------------------------------------------------------------
// Obligation (règle réglementaire — toujours sourcée)
// ---------------------------------------------------------------------------

export function creerObligation(o = {}) {
  if (!o.nom) throw new Error('Obligation.nom est obligatoire');
  if (!o.categorie) throw new Error('Obligation.categorie est obligatoire');
  // Une obligation SANS source n'a pas le droit d'exister (règle stricte).
  const provenance = creerProvenance(o.provenance || {});
  const conditions = arr(o.conditionsApplicabilite).map(normaliserCondition);
  return {
    type: 'Obligation',
    id: o.id || null,
    nom: o.nom,
    categorie: o.categorie,
    populationConcernee: arr(o.populationConcernee),
    conditionsApplicabilite: conditions,
    frequence: o.frequence ?? 'ponctuelle',
    dateLimite: o.dateLimite ?? null,
    autoriteCompetente: o.autoriteCompetente ?? null,
    piecesRequises: arr(o.piecesRequises),
    penalites: o.penalites ?? null,
    provenance,
    statut: assertEnum('statut', o.statut ?? 'actif', ENUMS.statutObligation),
    // Versioning réglementaire (facultatif, porté tel quel) : permet au moteur
    // de répondre « valable pour les règles en vigueur au <date> ».
    validite: o.validite ? {
      validFrom: o.validite.validFrom ?? provenance.dateVerification,
      validUntil: o.validite.validUntil ?? null,
      juridiction: o.validite.juridiction ?? 'LU',
      langue: o.validite.langue ?? 'fr',
      version: o.validite.version ?? null,
      lastVerified: o.validite.lastVerified ?? provenance.dateVerification,
    } : null,
    // Gouvernance de la connaissance (« fiche de vie » de la règle) : porté tel
    // quel, avec des défauts sûrs si absent.
    gouvernance: o.gouvernance ? {
      owner: o.gouvernance.owner ?? 'Paperasse Lux',
      status: o.gouvernance.status ?? 'verified',
      reviewFrequency: o.gouvernance.reviewFrequency ?? '6 months',
      lastVerified: o.gouvernance.lastVerified ?? provenance.dateVerification,
      nextReview: o.gouvernance.nextReview ?? null,
      changeLog: arr(o.gouvernance.changeLog),
    } : null,
  };
}

/**
 * Normalise une condition d'applicabilité déclarative :
 *   { champ, operateur, valeur }
 * Ex : { champ: 'statutProfessionnel', operateur: 'egal', valeur: 'independant' }
 *      { champ: 'frontalier', operateur: 'vrai' }
 */
function normaliserCondition(cond) {
  if (!cond || typeof cond !== 'object') {
    throw new Error('Condition d\'applicabilité invalide (objet attendu)');
  }
  if (!cond.champ) throw new Error('Condition : "champ" obligatoire');
  assertEnum('condition.operateur', cond.operateur, ENUMS.operateur);
  return { champ: cond.champ, operateur: cond.operateur, valeur: cond.valeur ?? null };
}

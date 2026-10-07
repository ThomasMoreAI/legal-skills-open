/**
 * lib/editorial — Workflow éditorial de la connaissance.
 *
 * Une règle ne se contente pas d'exister : elle suit un CYCLE DE VIE éditorial.
 * Chaque transition laisse une trace (pourquoi, par qui, depuis quelle source,
 * à quelle date, quels cas QA sont impactés). Cette discipline vaut plus que
 * d'ajouter vite des centaines de scénarios.
 *
 *   Veille → Proposition → Analyse → Validation → Publication
 *          → Surveillance → Révision → (Publication | Archivage)
 *
 * Déterministe, hors-ligne, aucune dépendance externe.
 */

/** Étapes du cycle de vie éditorial, dans l'ordre. */
export const ETAPES_EDITORIALES = [
  'veille', 'proposition', 'analyse', 'validation', 'publication', 'surveillance', 'revision', 'archivage',
];

/** Transitions autorisées entre étapes. */
const TRANSITIONS = {
  veille: ['proposition', 'archivage'],
  proposition: ['analyse', 'archivage'],
  analyse: ['validation', 'proposition', 'archivage'],
  validation: ['publication', 'analyse', 'archivage'],
  publication: ['surveillance', 'archivage'],
  surveillance: ['revision', 'archivage'],
  revision: ['validation', 'publication', 'archivage'],
  archivage: [],
};

/** Statut de gouvernance associé à chaque étape éditoriale. */
const ETAPE_VERS_STATUT = {
  veille: 'draft', proposition: 'draft', analyse: 'draft', validation: 'a_revoir',
  publication: 'verified', surveillance: 'verified', revision: 'a_revoir', archivage: 'deprecated',
};

/** Étape éditoriale courante d'une règle (inférée du statut si absente). */
export function etatEditorial(regle) {
  const g = regle.gouvernance || {};
  if (g.etatEditorial && ETAPES_EDITORIALES.includes(g.etatEditorial)) return g.etatEditorial;
  const parStatut = { draft: 'proposition', verified: 'publication', a_revoir: 'revision', deprecated: 'archivage' };
  return parStatut[g.status] || 'publication';
}

/** Transitions autorisées depuis une étape. */
export function transitionsAutorisees(etape) {
  return TRANSITIONS[etape] ? TRANSITIONS[etape].slice() : [];
}

export function transitionValide(de, vers) {
  return (TRANSITIONS[de] || []).includes(vers);
}

/**
 * Applique une transition éditoriale et renvoie une gouvernance mise à jour,
 * avec une entrée de changeLog tracée. NE MUTE PAS la règle d'origine.
 *
 * @param {object} regle
 * @param {object} p { vers, date, reason, author, source, casQAImpactes }
 * @returns {object} nouvelle gouvernance
 */
export function appliquerTransition(regle, { vers, date, reason, author = 'Paperasse Lux', source, casQAImpactes = [] } = {}) {
  if (!date) throw new Error('appliquerTransition : date requise (YYYY-MM-DD)');
  if (!ETAPES_EDITORIALES.includes(vers)) throw new Error(`Étape inconnue : ${vers}`);
  const de = etatEditorial(regle);
  if (de !== vers && !transitionValide(de, vers)) {
    throw new Error(`Transition non autorisée : ${de} → ${vers} (autorisées : ${transitionsAutorisees(de).join(', ') || 'aucune'})`);
  }
  const g = regle.gouvernance || { changeLog: [] };
  const entree = { date, etape: vers, reason: reason || `Passage à l'étape ${vers}`, author };
  if (source) entree.source = source;
  if (casQAImpactes && casQAImpactes.length) entree.casQAImpactes = casQAImpactes;
  return {
    ...g,
    etatEditorial: vers,
    status: ETAPE_VERS_STATUT[vers],
    lastVerified: vers === 'publication' || vers === 'revision' ? date : (g.lastVerified || date),
    changeLog: [...(g.changeLog || []), entree],
  };
}

/** Historique éditorial d'une règle (entrées de changeLog portant une étape). */
export function historiqueEditorial(regle) {
  return (regle.gouvernance && regle.gouvernance.changeLog ? regle.gouvernance.changeLog : []).filter((c) => c.etape);
}

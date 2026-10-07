/**
 * lib/memoire — Mémoire utilisateur / dossier administratif persistant.
 *
 * Conserve (avec le consentement de l'utilisateur) le contexte administratif
 * afin d'éviter de reposer les mêmes questions et de personnaliser les
 * démarches :
 *
 *   Utilisateur
 *   ├── Profil            ├── Véhicules
 *   ├── Famille           ├── Immobilier
 *   ├── Employeurs        ├── Documents
 *   ├── Sociétés          ├── Historique
 *   └── Obligations réalisées
 *
 * S'appuie sur le consentement RGPD (lib/rgpd). Sérialisable en JSON pour être
 * chiffré au repos par le store sécurisé. Aucune dépendance externe.
 */

import { exigerConsentement } from '../rgpd/index.js';
import { ceJourISO } from '../diagnostic/provenance.js';

const SECTIONS = ['famille', 'employeurs', 'societes', 'vehicules', 'immobilier', 'documents'];

/**
 * Crée une mémoire vide (ou initialisée) pour un profil consentant.
 * @param {object} profil  Doit porter consentementRGPD = true.
 */
export function creerMemoire(profil = {}) {
  exigerConsentement(profil);
  const memoire = { profil };
  for (const s of SECTIONS) memoire[s] = [];
  memoire.obligationsRealisees = [];
  memoire.historique = [];
  return memoire;
}

/** Journalise un fait dans l'historique (date injectable). */
function tracer(memoire, action, details, quand) {
  memoire.historique.push({ date: quand || ceJourISO(), action, details });
}

/** Ajoute un élément à une section (famille, employeurs, sociétés…). */
export function ajouter(memoire, section, element, { quand } = {}) {
  if (!SECTIONS.includes(section)) throw new Error(`Section inconnue : ${section} (attendu : ${SECTIONS.join(', ')})`);
  memoire[section].push(element);
  tracer(memoire, 'ajout', { section, element }, quand);
  return memoire;
}

/** Fusionne des champs de profil connus (sans réécraser par des valeurs vides). */
export function fusionnerProfil(memoire, profilPartiel = {}, { quand } = {}) {
  for (const [k, v] of Object.entries(profilPartiel)) {
    if (v === undefined || v === null || v === '') continue;
    memoire.profil[k] = v;
  }
  tracer(memoire, 'maj_profil', { champs: Object.keys(profilPartiel) }, quand);
  return memoire;
}

/** Marque une obligation comme réalisée (évite de la reproposer). */
export function marquerRealisee(memoire, obligationId, { date, quand } = {}) {
  if (!memoire.obligationsRealisees.some((o) => o.obligationId === obligationId)) {
    memoire.obligationsRealisees.push({ obligationId, date: date || quand || ceJourISO() });
  }
  tracer(memoire, 'obligation_realisee', { obligationId }, quand);
  return memoire;
}

export function estRealisee(memoire, obligationId) {
  return memoire.obligationsRealisees.some((o) => o.obligationId === obligationId);
}

/** Ensemble des ids d'obligations déjà réalisées. */
export function obligationsRealiseesSet(memoire) {
  return new Set(memoire.obligationsRealisees.map((o) => o.obligationId));
}

/**
 * Champs de profil déjà connus → questions à NE PAS reposer.
 * @returns {Set<string>}
 */
export function questionsAEviter(memoire) {
  const connus = new Set();
  for (const [k, v] of Object.entries(memoire.profil || {})) {
    if (v !== undefined && v !== null && v !== '' && !(Array.isArray(v) && v.length === 0)) connus.add(k);
  }
  return connus;
}

/** Le profil enrichi de la mémoire, prêt à alimenter le diagnostic/planificateur. */
export function profilEffectif(memoire) {
  return { ...memoire.profil };
}

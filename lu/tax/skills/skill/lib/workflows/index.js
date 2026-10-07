/**
 * lib/workflows — Workflow Engine & Missions.
 *
 * Paperasse Lux n'exécute presque jamais une seule action : l'utilisateur veut
 * atteindre un RÉSULTAT administratif (« créer une société », « s'installer »).
 * Une MISSION modélise ce résultat : un objectif, des étapes ordonnées (issues
 * du planificateur), des dépendances, des échéances, des risques, un état
 * d'avancement et un historique — reprenable après interruption.
 *
 * Séparation stricte des actions, pour préserver la confiance :
 *   - 'recommandation' : le système signale, n'agit pas ;
 *   - 'preparation'    : le système prépare, l'utilisateur valide ;
 *   - 'execution'      : le système agit, TOUJOURS après confirmation explicite,
 *                        et uniquement via un connecteur (plugin).
 *
 * Le Reasoner décide de ce qui change, le Planner de l'ordre, le Workflow
 * Engine fait avancer la mission, les connecteurs exécutent ce que
 * l'utilisateur valide. Déterministe, hors-ligne, aucune dépendance externe.
 */

import { planifier } from '../planification/index.js';
import { ceJourISO } from '../diagnostic/provenance.js';

export const TYPES_ACTION = ['recommandation', 'preparation', 'execution'];
export const ETATS_ETAPE = ['a_faire', 'en_attente_validation', 'fait', 'echec', 'bloquee'];
export const ETATS_MISSION = ['active', 'en_pause', 'terminee'];

// ---------------------------------------------------------------------------
// Connecteurs (plugins) — ajouter un portail sans modifier le moteur.
// ---------------------------------------------------------------------------

/** Crée un registre de connecteurs. Un connecteur : { id, disponible, executer }. */
export function creerRegistreConnecteurs() {
  const map = new Map();
  const registre = {
    enregistrer(connecteur) {
      if (!connecteur || !connecteur.id) throw new Error('connecteur.id requis');
      map.set(connecteur.id, connecteur);
      return registre;
    },
    obtenir(id) { return map.get(id) || null; },
    liste() { return [...map.keys()]; },
  };
  // Connecteur par défaut : « manuel » — ne transmet RIEN à l'extérieur ; il
  // prépare l'action pour que l'utilisateur la réalise lui-même.
  registre.enregistrer({
    id: 'manuel',
    disponible: true,
    executer: (etape) => ({ envoye: false, mode: 'manuel', message: `À réaliser vous-même${etape.source ? ` : ${etape.source}` : ''}.` }),
  });
  return registre;
}

/** Registre global par défaut (les connecteurs réels s'enregistrent ici). */
export const CONNECTEURS = creerRegistreConnecteurs();

// ---------------------------------------------------------------------------
// Création de mission
// ---------------------------------------------------------------------------

function tracer(mission, evenement, details, date) {
  mission.historique.push({ date: date || ceJourISO(), evenement, details: details ?? null });
  mission.majLe = date || mission.majLe;
}

/**
 * Crée une mission à partir d'un ou plusieurs événements de vie.
 *
 * @param {string} objectif       Libellé (« Créer une société »).
 * @param {object} opts           { evenements, profil, aujourdhui, id, typeParDefaut }
 * @returns {object} mission (sérialisable en JSON)
 */
export function createMission(objectif, opts = {}) {
  const aujourdhui = opts.aujourdhui || ceJourISO();
  const evenements = opts.evenements || [];
  const plan = planifier(evenements, { profil: opts.profil || {}, aujourdhui });
  const typeParDefaut = opts.typeParDefaut || 'recommandation';

  const etapes = plan.demarches.map((d) => ({
    id: d.cle,
    nom: d.nom,
    typeAction: typeParDefaut,
    statut: 'a_faire',
    dependances: d.prerequis || [],
    echeance: d.echeance || null,
    debloque: d.debloque || [],
    source: d.source || null,
    connecteur: 'manuel',
    resultat: null,
  }));

  const mission = {
    id: opts.id || `mission_${evenements.join('-') || 'adhoc'}`,
    objectif,
    evenements,
    statut: 'active',
    creeLe: aujourdhui,
    majLe: aujourdhui,
    etapes,
    documentsMutualises: plan.documentsMutualises,
    historique: [],
  };
  tracer(mission, 'creation', objectif, aujourdhui);
  return mission;
}

// ---------------------------------------------------------------------------
// Lecture d'état
// ---------------------------------------------------------------------------

const estFaite = (e) => e.statut === 'fait';
function dependancesSatisfaites(mission, etape) {
  const idx = new Map(mission.etapes.map((e) => [e.id, e]));
  return (etape.dependances || []).every((dep) => { const d = idx.get(dep); return !d || estFaite(d); });
}

/** Prochaine étape actionnable (non faite, dépendances satisfaites), dans l'ordre. */
export function prochaineEtape(mission) {
  return mission.etapes.find((e) =>
    ['a_faire', 'en_attente_validation'].includes(e.statut) && dependancesSatisfaites(mission, e)) || null;
}

/** État d'avancement de la mission. */
export function avancement(mission) {
  const total = mission.etapes.length;
  const faits = mission.etapes.filter(estFaite).length;
  const bloquees = mission.etapes.filter((e) => ['a_faire', 'en_attente_validation'].includes(e.statut) && !dependancesSatisfaites(mission, e)).length;
  const prochaine = prochaineEtape(mission);
  return {
    total, faits, restants: total - faits,
    pourcentage: total ? Math.round((faits / total) * 100) : 0,
    bloquees,
    prochaine: prochaine ? prochaine.nom : null,
    statut: mission.statut,
  };
}

// ---------------------------------------------------------------------------
// Avancement (une étape par appel, selon le type d'action)
// ---------------------------------------------------------------------------

/**
 * Fait avancer la mission d'une étape, en respectant le type d'action.
 *
 * @param {object} mission
 * @param {object} [opts] { valider, confirmerExecution, resultat, date, registre }
 * @returns {object} { mission, etape, action?, besoinValidation?, besoinConfirmation?, termine?, bloque?, message }
 */
export function advanceMission(mission, opts = {}) {
  if (mission.statut !== 'active') throw new Error(`Mission non active (statut : ${mission.statut}).`);
  const date = opts.date || mission.majLe;
  const e = prochaineEtape(mission);

  if (!e) {
    if (mission.etapes.every(estFaite)) return { mission, termine: true, message: 'Toutes les étapes sont terminées.' };
    return { mission, bloque: true, message: 'En attente de prérequis ou d\'une étape en échec.' };
  }

  if (e.typeAction === 'recommandation') {
    e.statut = 'fait';
    e.resultat = { type: 'recommandation', message: 'Démarche recommandée — à réaliser par vos soins.' };
    tracer(mission, 'recommandation', e.id, date);
    return { mission, etape: e, action: 'recommandation', message: e.resultat.message };
  }

  if (e.typeAction === 'preparation') {
    if (e.statut === 'a_faire') {
      e.statut = 'en_attente_validation';
      e.resultat = { type: 'preparation', message: `Préparation prête à valider : ${e.nom}.`, source: e.source };
      tracer(mission, 'preparation', e.id, date);
      return { mission, etape: e, action: 'preparation', besoinValidation: true, message: 'Validez la préparation pour continuer.' };
    }
    if (!opts.valider) return { mission, etape: e, besoinValidation: true, message: 'En attente de votre validation.' };
    e.statut = 'fait';
    e.resultat = { ...e.resultat, valide: true };
    tracer(mission, 'validation', e.id, date);
    return { mission, etape: e, action: 'validee', message: 'Préparation validée.' };
  }

  // execution
  if (!opts.confirmerExecution) {
    return { mission, etape: e, besoinConfirmation: true, message: 'Confirmez explicitement l\'exécution (envoi) de cette étape.' };
  }
  const registre = opts.registre || CONNECTEURS;
  const conn = registre.obtenir(e.connecteur) || registre.obtenir('manuel');
  let res;
  try { res = conn.executer(e, mission); }
  catch (err) { res = { echec: true, message: err.message }; }
  e.statut = res && res.echec ? 'echec' : 'fait';
  e.resultat = { type: 'execution', ...res };
  tracer(mission, 'execution', { etape: e.id, resultat: res }, date);
  return { mission, etape: e, action: 'execution', resultat: res, message: res.message };
}

/** Réinitialise une étape en échec pour réessayer. */
export function reessayerEtape(mission, etapeId, { date } = {}) {
  const e = mission.etapes.find((x) => x.id === etapeId);
  if (!e) throw new Error(`Étape inconnue : ${etapeId}`);
  if (e.statut === 'echec') { e.statut = 'a_faire'; e.resultat = null; tracer(mission, 'reessai', etapeId, date); }
  return mission;
}

/** Définit le type d'action (et le connecteur) d'une étape. */
export function definirTypeAction(mission, etapeId, type, { connecteur } = {}) {
  if (!TYPES_ACTION.includes(type)) throw new Error(`Type d'action inconnu : ${type}`);
  const e = mission.etapes.find((x) => x.id === etapeId);
  if (!e) throw new Error(`Étape inconnue : ${etapeId}`);
  e.typeAction = type;
  if (connecteur) e.connecteur = connecteur;
  return e;
}

// ---------------------------------------------------------------------------
// Cycle de vie
// ---------------------------------------------------------------------------

export function pauseMission(mission, { date } = {}) {
  if (mission.statut === 'terminee') throw new Error('Mission déjà terminée.');
  mission.statut = 'en_pause';
  tracer(mission, 'pause', null, date);
  return mission;
}

/** Reprend une mission (objet ou JSON sérialisé) après interruption. */
export function resumeMission(missionOuJSON, { date } = {}) {
  const mission = typeof missionOuJSON === 'string' ? JSON.parse(missionOuJSON) : missionOuJSON;
  if (mission.statut === 'terminee') return mission;
  mission.statut = 'active';
  tracer(mission, 'reprise', null, date);
  return mission;
}

export function completeMission(mission, { date, force = false } = {}) {
  if (!force && !mission.etapes.every(estFaite)) {
    const restants = mission.etapes.filter((e) => !estFaite(e)).map((e) => e.nom);
    throw new Error(`Étapes non terminées : ${restants.join(', ')}. Utilisez force pour clôturer malgré tout.`);
  }
  mission.statut = 'terminee';
  tracer(mission, 'cloture', { force }, date);
  return mission;
}

/** Sérialise / désérialise une mission (persistance / reprise). */
export const serialiser = (mission) => JSON.stringify(mission);
export const deserialiser = (json) => JSON.parse(json);

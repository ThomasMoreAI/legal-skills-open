/**
 * lib/evaluation — Qualité, explicabilité & observabilité.
 *
 * Le moteur produit une mission ; cette couche répond en plus :
 *   - Cette mission est-elle complète ? (avancement, points bloquants)
 *   - Quel est mon niveau de confiance ? (score pondéré par la fiabilité des sources)
 *   - Quelles hypothèses ai-je faites ? (défauts non confirmés)
 *   - Quels documents manquent ?
 *   - Quels risques si l'utilisateur n'agit pas ?
 * et produit une TRACE d'exécution auditable :
 *   événement → règle → obligation → impact → étape → connecteur.
 *
 * Déterministe, hors-ligne, aucune dépendance externe.
 */

import { resoudreEvenement } from '../evenements/index.js';
import { chargerCatalogue } from '../diagnostic/index.js';
import { avancement } from '../workflows/index.js';
import { ceJourISO, joursEcoules } from '../diagnostic/provenance.js';

const POIDS_CONFIANCE = { officiel: 1, derive: 0.8, estimation: 0.6, incertain: 0.3 };
const POIDS_HORS_CATALOGUE = 0.7;

const sansAccents = (s) => s.normalize('NFD').replace(/[̀-ͯ]/g, '');
const norme = (s) => sansAccents(String(s)).toLowerCase().replace(/[^a-z0-9]+/g, ' ').trim();

/**
 * Documents attendus par la mission (union des documents des événements),
 * moins ceux déjà disponibles dans la mémoire.
 */
function informationsManquantes(mission, { catalogue, aujourdhui, memoire }) {
  const attendus = new Map();
  for (const ev of mission.evenements) {
    for (const doc of resoudreEvenement(ev, { catalogue, aujourdhui }).documents) attendus.set(norme(doc), doc);
  }
  const fournis = new Set((memoire && memoire.documents ? memoire.documents : []).map((d) => norme(typeof d === 'string' ? d : d.nom || '')));
  return [...attendus.entries()].filter(([k]) => !fournis.has(k)).map(([, v]) => v);
}

/** Hypothèses implicites : défauts non confirmés par le profil. */
function hypotheses(profil = {}) {
  const h = [];
  if (!profil.statutLogement) h.push('Résidence principale au Luxembourg supposée.');
  if ((profil.situationFamiliale === 'marie' || profil.situationFamiliale === 'partenariat') && !profil.conjointTravailleEtranger) {
    h.push('Conjoint sans activité au Luxembourg supposé.');
  }
  if (!profil.nationalite) h.push('Nationalité UE/EEE supposée (pas de titre de séjour requis).');
  if (profil.frequenceTVA === undefined && (profil.statut === 'actif' || profil.formeJuridique)) h.push('Fréquence de déclaration TVA à confirmer selon le chiffre d\'affaires.');
  return h;
}

/**
 * Évalue une mission : rapport de complétude, confiance, hypothèses, risques,
 * points bloquants, documents manquants, sources.
 *
 * @param {object} mission
 * @param {object} [opts] { profil, memoire, aujourdhui, catalogue }
 * @returns {object} rapport
 */
export function evaluerMission(mission, opts = {}) {
  const aujourdhui = opts.aujourdhui || ceJourISO();
  const catalogue = opts.catalogue || chargerCatalogue().obligations;
  const parId = new Map(catalogue.map((o) => [o.id, o]));
  const profil = opts.profil || (opts.memoire ? opts.memoire.profil : {}) || {};

  const av = avancement(mission);

  // Confiance : moyenne pondérée par la fiabilité des sources des étapes.
  let sommePoids = 0;
  const sources = new Set();
  const risques = [];
  for (const e of mission.etapes) {
    const ob = parId.get(e.id);
    const niveau = ob && ob.provenance ? ob.provenance.niveauConfiance : null;
    sommePoids += niveau ? (POIDS_CONFIANCE[niveau] ?? POIDS_HORS_CATALOGUE) : POIDS_HORS_CATALOGUE;
    if (e.source) sources.add(e.source);
    if (ob && ob.penalites) risques.push(`${e.nom} : ${ob.penalites}`);
    // Risque d'échéance.
    if (e.echeance && e.statut !== 'fait') {
      const j = joursEcoules(aujourdhui, e.echeance);
      if (j < 0) risques.push(`${e.nom} : échéance dépassée (${e.echeance}).`);
      else if (j <= 30) risques.push(`${e.nom} : échéance proche (${e.echeance}, ${j} j).`);
    }
  }
  let confiance = mission.etapes.length ? (sommePoids / mission.etapes.length) * 100 : 100;

  const infosManquantes = informationsManquantes(mission, { catalogue, aujourdhui, memoire: opts.memoire });
  const hyp = hypotheses(profil);

  // Points bloquants : étapes dont les prérequis ne sont pas satisfaits, ou en échec.
  const faits = new Set(mission.etapes.filter((e) => e.statut === 'fait').map((e) => e.id));
  const pointsBloquants = [];
  for (const e of mission.etapes) {
    if (e.statut === 'echec') pointsBloquants.push(`${e.nom} : en échec.`);
    else if (e.statut !== 'fait' && (e.dependances || []).some((d) => !faits.has(d))) {
      const manquants = e.dependances.filter((d) => !faits.has(d)).map((d) => (mission.etapes.find((x) => x.id === d) || {}).nom || d);
      pointsBloquants.push(`${e.nom} : en attente de ${manquants.join(', ')}.`);
    }
  }

  // Pénalités de confiance : informations manquantes et blocages.
  confiance -= Math.min(15, infosManquantes.length * 3);
  confiance -= Math.min(15, pointsBloquants.length * 2);
  confiance = Math.max(0, Math.min(100, Math.round(confiance)));

  return {
    mission: mission.objectif,
    complete: av.pourcentage === 100,
    avancement: av,
    confianceGlobale: confiance,
    informationsManquantes: infosManquantes,
    hypotheses: hyp,
    risques,
    pointsBloquants,
    sources: [...sources],
    note: 'Rapport indicatif : confiance et hypothèses sont calculées à partir des données disponibles ; à confirmer avec l\'utilisateur.',
  };
}

/**
 * Trace d'exécution auditable d'une mission :
 * événement → règle appliquée → obligation → étape planifiée → connecteur.
 *
 * @param {object} mission
 * @param {object} [opts] { catalogue, aujourdhui }
 * @returns {{phase, detail, source?}[]}
 */
export function traceMission(mission, opts = {}) {
  const aujourdhui = opts.aujourdhui || ceJourISO();
  const catalogue = opts.catalogue || chargerCatalogue().obligations;
  const trace = [];
  const push = (phase, detail, source) => trace.push(source ? { phase, detail, source } : { phase, detail });

  const etapeParId = new Map(mission.etapes.map((e) => [e.id, e]));

  for (const ev of mission.evenements) {
    const c = resoudreEvenement(ev, { catalogue, aujourdhui });
    push('evenement_detecte', c.evenement.nom);
    for (const o of [...c.obligations, ...c.obligationsHorsCatalogue]) {
      const nom = o.nom;
      push('regle_appliquee', `Règle : ${nom}`, o.source || null);
      push('obligation_creee', nom, o.source || null);
      const e = etapeParId.get(o.id) || [...etapeParId.values()].find((x) => x.nom === nom);
      if (e) {
        push('etape_ajoutee', `${e.nom}${e.echeance ? ` (échéance ${e.echeance})` : ''}${e.dependances.length ? ` [après ${e.dependances.join(', ')}]` : ''}`);
        push('connecteur_selectionne', `${e.nom} → connecteur « ${e.connecteur} » (${e.typeAction})`);
      }
    }
  }
  return trace;
}

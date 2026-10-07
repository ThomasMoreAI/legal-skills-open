/**
 * lib/residence — Résidence, immigration & commune (Milestone 7).
 *
 * Génère le parcours chronologique « Je m'installe au Luxembourg » à partir du
 * catalogue d'étapes sourcé (data/installation-luxembourg.json), filtré selon
 * la nationalité (ressortissant UE/EEE/CH vs hors UE) et la situation du
 * profil, avec des échéances indicatives calculées depuis la date d'arrivée.
 *
 * Aucune règle n'est codée en dur : les étapes et leurs sources vivent dans le
 * fichier de données. Aucune dépendance externe.
 */

import { readFileSync, existsSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

import { ceJourISO } from '../diagnostic/provenance.js';
import { evaluerCondition } from '../diagnostic/engine.js';

const __dirname = dirname(fileURLToPath(import.meta.url));
const DATA_PATH = join(__dirname, '..', '..', 'data', 'installation-luxembourg.json');

/** Phases dans l'ordre chronologique, avec leur décalage indicatif (jours). */
export const PHASES_INSTALLATION = ['avant_arrivee', 'premiere_semaine', 'premier_mois', 'trois_mois', 'annuel'];
const OFFSET_JOURS = { avant_arrivee: -7, premiere_semaine: 7, premier_mois: 30, trois_mois: 90, annuel: 365 };
const LIBELLE_PHASE = {
  avant_arrivee: 'Avant l\'arrivée',
  premiere_semaine: 'Première semaine',
  premier_mois: 'Premier mois',
  trois_mois: 'Trois premiers mois',
  annuel: 'Démarches annuelles / récurrentes',
};

/** UE + EEE + Suisse (codes ISO2 et quelques libellés FR courants). */
const PAYS_UE_EEE_CH = new Set([
  'LU', 'FR', 'BE', 'DE', 'NL', 'IT', 'ES', 'PT', 'AT', 'IE', 'FI', 'SE', 'DK', 'GR', 'PL',
  'CZ', 'SK', 'HU', 'RO', 'BG', 'HR', 'SI', 'EE', 'LV', 'LT', 'CY', 'MT',
  'IS', 'LI', 'NO', 'CH',
  'LUXEMBOURG', 'FRANCE', 'BELGIQUE', 'ALLEMAGNE', 'FRANCAISE', 'BELGE', 'ALLEMANDE', 'LUXEMBOURGEOISE',
]);

export function chargerInstallation(fichier = DATA_PATH) {
  if (!existsSync(fichier)) return { as_of: null, etapes: [] };
  return JSON.parse(readFileSync(fichier, 'utf8'));
}

/**
 * Classe la nationalité : 'ue' (UE/EEE/CH), 'hors_ue', ou 'inconnu'.
 */
export function classeNationalite(profil = {}) {
  const nat = profil.nationalite;
  if (!nat) return 'inconnu';
  return PAYS_UE_EEE_CH.has(String(nat).trim().toUpperCase()) ? 'ue' : 'hors_ue';
}

/** Une étape s'applique-t-elle au profil (public + condition éventuelle) ? */
function etapeApplicable(etape, profil, classe) {
  const publicOk = etape.public.includes('tous')
    || etape.public.includes(classe)
    || (classe === 'inconnu'); // nationalité inconnue → on montre tout, en signalant
  if (!publicOk) return false;
  if (etape.condition) return evaluerCondition(profil, etape.condition);
  return true;
}

function addJours(dateISO, n) {
  const base = Date.parse(`${dateISO}T00:00:00Z`);
  return new Date(base + n * 86_400_000).toISOString().slice(0, 10);
}

/**
 * Construit le parcours d'installation.
 *
 * @param {object} profil       { nationalite, dateArriveeLux, vehicules, ... }
 * @param {object} [opts]       { aujourdhui }
 * @returns {{classeNationalite, parPhase, chronologie, avertissement}}
 */
export function parcoursInstallation(profil = {}, opts = {}) {
  const { etapes } = chargerInstallation();
  const classe = classeNationalite(profil);
  const arrivee = profil.dateArriveeLux || null;

  const retenues = etapes
    .filter((e) => etapeApplicable(e, profil, classe))
    .map((e) => ({
      id: e.id,
      phase: e.phase,
      titre: e.titre,
      description: e.description || null,
      administration: e.administration || null,
      delai: e.delai || null,
      public: e.public,
      obligationId: e.obligationId || null,
      source: e.source,
      echeanceIndicative: arrivee ? addJours(arrivee, OFFSET_JOURS[e.phase]) : null,
      // Étape spécifique à un statut alors que la nationalité est inconnue :
      aPreciser: classe === 'inconnu' && !e.public.includes('tous'),
    }));

  const parPhase = {};
  for (const phase of PHASES_INSTALLATION) {
    const liste = retenues.filter((r) => r.phase === phase);
    if (liste.length) parPhase[phase] = { libelle: LIBELLE_PHASE[phase], etapes: liste };
  }

  const chronologie = retenues.sort((a, b) => {
    const pa = PHASES_INSTALLATION.indexOf(a.phase);
    const pb = PHASES_INSTALLATION.indexOf(b.phase);
    return pa - pb || a.id.localeCompare(b.id);
  });

  return {
    classeNationalite: classe,
    parPhase,
    chronologie,
    avertissement: classe === 'inconnu'
      ? 'Nationalité non renseignée : certaines étapes (UE vs hors UE) sont à préciser.'
      : (!arrivee ? 'Date d\'arrivée non renseignée : les échéances indicatives ne sont pas calculées.' : null),
  };
}

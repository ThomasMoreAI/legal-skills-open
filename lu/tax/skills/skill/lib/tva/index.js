/**
 * lib/tva — Module TVA complet : suivi, calendrier et cohérence (Milestone 4).
 *
 * S'appuie sur le calculateur de déclaration existant
 * (`scripts/calc-tva-declaration.js`) et sur les seuils sourcés
 * (`comptable/data/tva-taux.json`). Ce module n'envoie RIEN : il détecte les
 * déclarations attendues/manquantes, construit le calendrier, prépare les
 * données et contrôle la cohérence. Toute déclaration réelle passe par une
 * validation humaine explicite.
 *
 * Échéances de dépôt (convention alignée sur le `rappel` de
 * calc-tva-declaration.js et le moteur du M1) :
 *   - mensuelle    : le 15 du mois suivant la période ;
 *   - trimestrielle: le 15 du 1er mois suivant la fin du trimestre ;
 *   - annuelle     : le 1er mars de l'année N+1 (déclaration récapitulative TVA-100).
 * Ces dates sont marquées « à vérifier sur eCDF » (niveau derive).
 *
 * Aucune dépendance externe.
 */

import { readFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

import { calcDeclarationTVA } from '../../scripts/calc-tva-declaration.js';
import { ceJourISO } from '../diagnostic/provenance.js';
import { creerDossier } from '../diagnostic/entities.js';

const __dirname = dirname(fileURLToPath(import.meta.url));
const TAUX_PATH = join(__dirname, '..', '..', 'comptable', 'data', 'tva-taux.json');

const pad = (n) => String(n).padStart(2, '0');
const iso = (y, m, d) => `${y}-${pad(m)}-${pad(d)}`;
const round2 = (n) => Math.round(n * 100) / 100;
const finDeMois = (y, m) => new Date(Date.UTC(y, m, 0)).getUTCDate(); // m = 1..12

/** Charge la fiche taux/seuils TVA sourcée (comptable/data/tva-taux.json). */
export function chargerTauxTVA() {
  return JSON.parse(readFileSync(TAUX_PATH, 'utf8'));
}

export const SOURCE_TVA = {
  source: 'https://pfi.public.lu/fr/professionnels/tva.html',
  reference: 'Loi modifiée du 12 février 1979 concernant la TVA + AED',
};

/**
 * Détermine la fréquence de déclaration selon le chiffre d'affaires annuel HT,
 * à partir des seuils sourcés. Retourne aussi la source (traçabilité).
 * Seuils AED : mensuel > 620 000 € ; trimestriel 112 000–620 000 € ; annuel ≤ 112 000 €.
 */
export function determinerFrequence(caAnnuelHT, { as_of } = {}) {
  const fiche = chargerTauxTVA();
  let frequence;
  if (caAnnuelHT > 620_000) frequence = 'mensuelle';
  else if (caAnnuelHT > 112_000) frequence = 'trimestrielle';
  else frequence = 'annuelle';
  return {
    frequence,
    seuils: fiche.regimes_declaration,
    provenance: {
      source: SOURCE_TVA.source,
      dateVerification: as_of || fiche.as_of || ceJourISO(),
      niveauConfiance: 'derive',
      note: 'Seuils AED susceptibles d\'évolution — à vérifier sur eCDF.',
    },
  };
}

/** Échéance de dépôt d'une période, selon sa fréquence. */
export function echeanceDepot(periode) {
  const { type, annee, mois, trimestre } = periode;
  if (type === 'mois') {
    let y = annee, m = mois + 1;
    if (m > 12) { m = 1; y += 1; }
    return iso(y, m, 15);
  }
  if (type === 'trimestre') {
    const finMois = trimestre * 3; // 3,6,9,12
    let y = annee, m = finMois + 1;
    if (m > 12) { m = 1; y += 1; }
    return iso(y, m, 15);
  }
  // annuelle : TVA-100 récapitulative au 1er mars N+1
  return iso(annee + 1, 3, 1);
}

/** Fin (dernier jour) de la période, en ISO. */
function finPeriode(periode) {
  const { type, annee, mois, trimestre } = periode;
  if (type === 'mois') return iso(annee, mois, finDeMois(annee, mois));
  if (type === 'trimestre') { const m = trimestre * 3; return iso(annee, m, finDeMois(annee, m)); }
  return iso(annee, 12, 31);
}

function codePeriode(periode) {
  if (periode.type === 'mois') return `${periode.annee}-${pad(periode.mois)}`;
  if (periode.type === 'trimestre') return `${periode.annee}-T${periode.trimestre}`;
  return `${periode.annee}`;
}

/**
 * Périodes de déclaration ATTENDUES (déjà écoulées) entre `debut` et
 * `aujourdhui`, selon la fréquence.
 *
 * @param {object} p { frequenceTVA, debut (YYYY-MM-DD), aujourdhui }
 * @returns {object[]} périodes { code, type, annee, mois?, trimestre?, fin, echeance }
 */
export function periodesAttendues({ frequenceTVA, debut, aujourdhui = ceJourISO() }) {
  if (!debut) throw new Error('periodesAttendues : date de début (assujettissement) requise');
  const [dy, dm] = debut.split('-').map(Number);
  const out = [];
  const enrichir = (periode) => {
    const p = { ...periode, code: codePeriode(periode), fin: finPeriode(periode), echeance: echeanceDepot(periode) };
    // Attendue si la période est terminée avant aujourd'hui.
    if (p.fin < aujourdhui) out.push(p);
  };

  if (frequenceTVA === 'mensuelle') {
    let y = dy, m = dm;
    while (iso(y, m, 1) <= aujourdhui) {
      enrichir({ type: 'mois', annee: y, mois: m });
      m += 1; if (m > 12) { m = 1; y += 1; }
    }
  } else if (frequenceTVA === 'trimestrielle') {
    let y = dy, t = Math.ceil(dm / 3);
    while (iso(y, t * 3, 1) <= aujourdhui) {
      enrichir({ type: 'trimestre', annee: y, trimestre: t });
      t += 1; if (t > 4) { t = 1; y += 1; }
    }
  } else if (frequenceTVA === 'annuelle') {
    for (let y = dy; y <= Number(aujourdhui.slice(0, 4)); y++) enrichir({ type: 'annee', annee: y });
  } else {
    throw new Error(`Fréquence TVA inconnue : ${frequenceTVA}`);
  }
  return out;
}

/**
 * Calendrier TVA complet : ce qui est soumis, en retard, à préparer, et les
 * prochaines échéances.
 *
 * @param {object} p
 * @param {string} p.frequenceTVA
 * @param {string} p.debut               Date d'assujettissement (YYYY-MM-DD).
 * @param {string[]|object[]} [p.soumises] Codes de périodes déjà déclarées
 *                                          (ou objets { code, date, montant }).
 * @param {string} [p.aujourdhui]
 */
export function calendrierTVA({ frequenceTVA, debut, soumises = [], aujourdhui = ceJourISO() }) {
  const attendues = periodesAttendues({ frequenceTVA, debut, aujourdhui });
  const codesSoumis = new Set(soumises.map((s) => (typeof s === 'string' ? s : s.code)));

  const manquantes = attendues.filter((p) => !codesSoumis.has(p.code));
  const enRetard = manquantes.filter((p) => p.echeance < aujourdhui);
  const aPreparer = manquantes.filter((p) => p.echeance >= aujourdhui);
  const soumisesResolues = attendues.filter((p) => codesSoumis.has(p.code));

  // Prochaine échéance = la plus proche parmi les périodes non soumises.
  const parEcheance = [...manquantes].sort((a, b) => a.echeance.localeCompare(b.echeance));
  const prochaine = aPreparer.sort((a, b) => a.echeance.localeCompare(b.echeance))[0] || null;

  return {
    frequenceTVA,
    attendues,
    soumises: soumisesResolues,
    enRetard,
    aPreparer,
    prochaineDeclaration: prochaine ? { code: prochaine.code, echeance: prochaine.echeance } : null,
    prochaineEcheancePaiement: parEcheance[0] ? { code: parEcheance[0].code, echeance: parEcheance[0].echeance } : null,
    provenance: {
      source: SOURCE_TVA.source,
      dateVerification: aujourdhui,
      niveauConfiance: 'derive',
      note: 'Échéances de dépôt indicatives — à vérifier sur eCDF.',
    },
  };
}

/** Checklist des données nécessaires à la préparation d'une déclaration. */
export function checklistDeclaration() {
  return [
    'Chiffre d\'affaires de la période (par taux)',
    'Ventes nationales',
    'Ventes / livraisons intracommunautaires (exonérées, VIES)',
    'Achats et frais déductibles',
    'TVA collectée',
    'TVA déductible',
    'Acquisitions intracommunautaires (auto-liquidation)',
    'Importations',
    'Régularisations éventuelles',
    'Notes de crédit',
  ];
}

const NUM_TVA_LU = /^LU\d{8}$/;
const TAUX_VALIDES = new Set([17, 14, 8, 3, 0]);

/**
 * Contrôle de cohérence d'une déclaration TVA et, si fournies, des factures.
 * Recalcule la TVA collectée via calcDeclarationTVA (calcul traçable) et
 * signale les anomalies. Ne bloque rien : renvoie une liste d'alertes.
 *
 * @param {object} p
 * @param {string} [p.numeroTVA]
 * @param {object} [p.operations]        Rubriques compatibles calcDeclarationTVA.
 * @param {object} [p.declaration]       { collectee, deductible, ... } déclarés.
 * @param {object[]} [p.factures]        { numero, date, ht, taux, tva }.
 * @param {object} [p.calendrier]        Sortie de calendrierTVA (pour périodes manquantes).
 * @returns {{anomalies: object[], recalcul: object|null}}
 */
export function controleCoherence({ numeroTVA, operations, declaration, factures, calendrier } = {}) {
  const anomalies = [];
  const add = (code, gravite, message, details) => anomalies.push({ code, gravite, message, ...(details ? { details } : {}) });

  // Numéro de TVA
  if (!numeroTVA) add('tva_absent', 'haute', 'Numéro de TVA absent.');
  else if (!NUM_TVA_LU.test(numeroTVA.replace(/\s/g, ''))) add('tva_format', 'moyenne', `Numéro de TVA au format inattendu : ${numeroTVA} (attendu LU + 8 chiffres).`);

  // Périodes manquantes
  if (calendrier && calendrier.enRetard && calendrier.enRetard.length) {
    add('periodes_manquantes', 'haute', `${calendrier.enRetard.length} déclaration(s) en retard : ${calendrier.enRetard.map((p) => p.code).join(', ')}.`, calendrier.enRetard.map((p) => p.code));
  }

  // Recalcul de la TVA collectée et comparaison au déclaré
  let recalcul = null;
  if (operations) {
    recalcul = calcDeclarationTVA({ periode: (declaration && declaration.periode) || 'contrôle', operations });
    if (declaration && Number.isFinite(declaration.collectee) && Math.abs(round2(declaration.collectee) - recalcul.collectee) > 0.01) {
      add('collectee_incoherente', 'haute',
        `TVA collectée déclarée (${round2(declaration.collectee)}) ≠ recalculée (${recalcul.collectee}).`,
        { declaree: round2(declaration.collectee), recalculee: recalcul.collectee });
    }
  }

  // Contrôles factures
  if (Array.isArray(factures) && factures.length) {
    const vus = new Set();
    let sommeTvaFactures = 0;
    for (const f of factures) {
      const id = f.numero || null;
      if (!id || !f.date) add('facture_non_conforme', 'moyenne', `Facture incomplète (numéro/date manquant) : ${JSON.stringify(f).slice(0, 80)}.`);
      if (id) { if (vus.has(id)) add('facture_doublon', 'moyenne', `Facture en doublon : ${id}.`); vus.add(id); }
      if (f.taux != null && !TAUX_VALIDES.has(Number(f.taux))) add('taux_invalide', 'moyenne', `Taux de TVA inhabituel sur la facture ${id || '?'} : ${f.taux} %.`);
      if (Number.isFinite(f.ht) && f.ht <= 0) add('montant_inhabituel', 'basse', `Montant HT non positif sur la facture ${id || '?'} : ${f.ht}.`);
      if (Number.isFinite(f.tva)) sommeTvaFactures += f.tva;
      else if (Number.isFinite(f.ht) && Number.isFinite(f.taux)) sommeTvaFactures += round2((f.ht * f.taux) / 100);
    }
    sommeTvaFactures = round2(sommeTvaFactures);
    const baseCollectee = recalcul ? recalcul.collectee : (declaration && declaration.collectee);
    if (Number.isFinite(baseCollectee) && Math.abs(sommeTvaFactures - round2(baseCollectee)) > 0.01) {
      add('factures_vs_declaration', 'moyenne',
        `TVA des factures (${sommeTvaFactures}) ≠ TVA collectée (${round2(baseCollectee)}).`,
        { factures: sommeTvaFactures, declaration: round2(baseCollectee) });
    }
  }

  return { anomalies, recalcul };
}

/**
 * Rapproche un courrier AED analysé (M3) du calendrier TVA et crée une action
 * (Dossier) rattachée à la période concernée. Ne déclenche aucun envoi.
 *
 * @param {object} analyse    Sortie de analyserDocument() sur un courrier AED.
 * @param {object} [calendrier]
 * @param {object} [opts]     { societeId, aujourdhui, id }
 * @returns {{periodeConcernee: string|null, statut: string, dossier: object}}
 */
export function rapprocherCourrierAED(analyse, calendrier, opts = {}) {
  const aujourdhui = opts.aujourdhui || ceJourISO();
  const libelle = analyse.periode ? analyse.periode.libelle : null;
  // Normalise « T1 2026 » → « 2026-T1 » pour comparer aux codes du calendrier.
  let code = null;
  if (libelle) {
    const t = /T([1-4])\s+(\d{4})/i.exec(libelle);
    if (t) code = `${t[2]}-T${t[1]}`;
    else if (/^\d{4}$/.test(libelle.trim())) code = libelle.trim();
  }
  let statut = 'periode_non_rapprochee';
  if (calendrier && code) {
    if (calendrier.enRetard.some((p) => p.code === code)) statut = 'en_retard_confirme';
    else if (calendrier.aPreparer.some((p) => p.code === code)) statut = 'a_preparer';
    else if (calendrier.soumises.some((p) => p.code === code)) statut = 'deja_soumise';
  }

  const dossier = creerDossier({
    id: opts.id,
    maintenant: aujourdhui,
    categorie: 'tva',
    administration: analyse.administration ? analyse.administration.nom : 'AED',
    typeDemarche: `Traitement courrier AED${code ? ` — période ${code}` : ''}`,
    statut: statut === 'en_retard_confirme' ? 'en_retard' : 'a_preparer',
    priorite: statut === 'en_retard_confirme' ? 'obligatoire_maintenant' : 'a_faire_prochainement',
    echeance: analyse.echeance ? analyse.echeance.iso : null,
    periode: code || libelle,
    documentsRequis: checklistDeclaration(),
    prochainesActions: analyse.action ? [analyse.action] : ['Préparer et déposer la déclaration TVA concernée'],
    risques: analyse.consequences || [],
    provenance: {
      source: `Courrier AED importé : ${analyse.nom || 'document'}`,
      dateVerification: aujourdhui,
      niveauConfiance: 'incertain',
      note: 'Action déduite d\'un courrier importé ; à vérifier avant tout dépôt.',
    },
    societeId: opts.societeId ?? null,
    documentId: (analyse.document && analyse.document.id) || null,
  });

  return { periodeConcernee: code, statut, dossier };
}

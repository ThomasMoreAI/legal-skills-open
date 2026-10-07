/**
 * lib/documents — Analyse de courriers et documents officiels (Milestone 3).
 *
 * Pipeline zéro-dépendance opérant sur du TEXTE déjà extrait (`texteExtrait`).
 * L'extraction PDF/image (OCR) sera une couche optionnelle ultérieure, sur le
 * modèle des `optionalDependencies` du projet ; le cœur, lui, reste pur et
 * testable sur du texte.
 *
 * Étapes : identifier l'administration → le type → dates → montants →
 * références → période → action demandée → échéance → conséquences →
 * résumé → checklist → projet de réponse → Dossier.
 *
 * Règle stricte : un document importé n'est JAMAIS « officiel ». Ses éléments
 * réglementaires (échéance, conséquences) sont marqués incertains et une
 * validation humaine est signalée dès qu'un élément clé manque ou est ambigu.
 *
 * Aucune dépendance externe.
 */

import {
  ADMINISTRATIONS, TYPES_DOCUMENT, MARQUEURS_ACTION, MARQUEURS_CONSEQUENCE,
  MARQUEURS_ECHEANCE, MOIS_FR,
} from './lexique.js';
import { creerDocument, creerDossier } from '../diagnostic/entities.js';
import { ceJourISO } from '../diagnostic/provenance.js';

const pad = (n) => String(n).padStart(2, '0');
const iso = (y, m, d) => `${y}-${pad(m)}-${pad(d)}`;
const dateValide = (y, m, d) => m >= 1 && m <= 12 && d >= 1 && d <= new Date(Date.UTC(y, m, 0)).getUTCDate();

/** Toutes les dates du texte, normalisées ISO, avec leur position. */
export function detecterDates(texte) {
  const out = [];
  const pousser = (y, m, d, index, brut) => {
    if (dateValide(y, m, d)) out.push({ iso: iso(y, m, d), index, brut });
  };
  // JJ/MM/AAAA, JJ.MM.AAAA, JJ-MM-AAAA
  for (const m of texte.matchAll(/\b(\d{1,2})[\/.\-](\d{1,2})[\/.\-](\d{4})\b/g)) {
    pousser(+m[3], +m[2], +m[1], m.index, m[0]);
  }
  // JJ mois AAAA (avec « 1er » toléré)
  const moisMotif = Object.keys(MOIS_FR).join('|');
  for (const m of texte.matchAll(new RegExp(`\\b(\\d{1,2})(?:er)?\\s+(${moisMotif})\\s+(\\d{4})\\b`, 'gi'))) {
    pousser(+m[3], MOIS_FR[m[2].toLowerCase()], +m[1], m.index, m[0]);
  }
  return out.sort((a, b) => a.index - b.index);
}

/** Montants en euros (format LU : 1.234,56 €). */
export function detecterMontants(texte) {
  const out = [];
  const re = /(?:€|eur)\s*([\d][\d.\s]*(?:,\d{2})?)|([\d][\d.\s]*,\d{2})\s*(?:€|eur|euros)?/gi;
  for (const m of texte.matchAll(re)) {
    const brut = (m[1] || m[2] || '').trim();
    if (!brut) continue;
    const valeur = parseFloat(brut.replace(/[.\s]/g, '').replace(',', '.'));
    if (Number.isFinite(valeur)) out.push({ valeur, brut: m[0].trim() });
  }
  return out;
}

/** Références : RCS, TVA, numéros de dossier / référence. */
export function detecterReferences(texte) {
  const refs = [];
  for (const m of texte.matchAll(/\b([BFGEKX])\s?(\d{4,7})\b/g)) refs.push({ type: 'rcs', valeur: `${m[1]}${m[2]}` });
  for (const m of texte.matchAll(/\bLU\s?(\d{8})\b/gi)) refs.push({ type: 'tva', valeur: `LU${m[1]}` });
  for (const m of texte.matchAll(/(?:r[ée]f(?:[ée]rence)?\.?|n[°o]|dossier|matricule)\s*:?\s*([A-Z0-9][A-Z0-9\/\-.]{2,})/gi)) {
    refs.push({ type: 'reference', valeur: m[1] });
  }
  // Dédoublonnage
  const vus = new Set();
  return refs.filter((r) => { const k = `${r.type}:${r.valeur}`; if (vus.has(k)) return false; vus.add(k); return true; });
}

function meilleurScore(texte, table) {
  const bas = texte.toLowerCase();
  let meilleur = null;
  for (const item of table) {
    let score = 0;
    for (const mc of item.motsCles) {
      const re = new RegExp(mc, 'i');
      if (re.test(bas)) score++;
    }
    if (score > 0 && (!meilleur || score > meilleur.score)) meilleur = { ...item, score };
  }
  return meilleur;
}

export const detecterAdministration = (texte) => meilleurScore(texte, ADMINISTRATIONS);

/**
 * Type de document : les types spécifiques priment ; le type générique
 * « courrier » (fallback) n'est retenu que si aucun spécifique ne correspond,
 * afin que des mots communs (« objet », « veuillez ») ne l'emportent pas.
 */
export function detecterType(texte) {
  const specifiques = TYPES_DOCUMENT.filter((t) => !t.fallback);
  const meilleur = meilleurScore(texte, specifiques);
  if (meilleur) return meilleur;
  const fallback = TYPES_DOCUMENT.find((t) => t.fallback);
  return meilleurScore(texte, [fallback]);
}

/** Période concernée (trimestre, mois, exercice, intervalle). */
export function detecterPeriode(texte) {
  const t = texte;
  let m;
  if ((m = /\bT([1-4])\s*[\/\-]?\s*(\d{4})\b/i.exec(t))) return { type: 'trimestre', libelle: `T${m[1]} ${m[2]}` };
  if ((m = new RegExp(`\\b(?:mois de\\s+)?(${Object.keys(MOIS_FR).join('|')})\\s+(\\d{4})\\b`, 'i').exec(t))) return { type: 'mois', libelle: `${m[1]} ${m[2]}` };
  if ((m = /\b(?:exercice|ann[ée]e)\s+(\d{4})\b/i.exec(t))) return { type: 'annee', libelle: m[1] };
  if ((m = /p[ée]riode\s+du\s+([\d\/.\-]+)\s+au\s+([\d\/.\-]+)/i.exec(t))) return { type: 'intervalle', libelle: `${m[1]} → ${m[2]}` };
  return null;
}

/** Action demandée (première tournure reconnue). */
export function detecterAction(texte) {
  for (const { motif, action } of MARQUEURS_ACTION) if (motif.test(texte)) return action;
  return null;
}

/** Conséquences possibles en cas d'inaction. */
export function detecterConsequences(texte) {
  const out = [];
  for (const { motif, texte: lib } of MARQUEURS_CONSEQUENCE) if (motif.test(texte) && !out.includes(lib)) out.push(lib);
  return out;
}

/**
 * Échéance : date suivant un marqueur (« avant le », « au plus tard le »…),
 * ou date calculée depuis un délai relatif (« endéans les N jours ») si une
 * date de document est disponible.
 * @returns {{iso: string|null, brut: string|null, relatif?: string, incertain: boolean}}
 */
export function detecterEcheance(texte, dates, { dateDocument } = {}) {
  const bas = texte.toLowerCase();
  // Délai relatif en jours
  const rel = /(?:endéans|dans un délai de|sous)\s+(?:les\s+)?(\d{1,3})\s+jours/i.exec(texte);
  for (const marqueur of MARQUEURS_ECHEANCE) {
    let pos = bas.indexOf(marqueur);
    while (pos !== -1) {
      const suivante = dates.find((d) => d.index >= pos && d.index <= pos + 60);
      if (suivante) return { iso: suivante.iso, brut: suivante.brut, incertain: false };
      pos = bas.indexOf(marqueur, pos + 1);
    }
  }
  if (rel && dateDocument) {
    const base = Date.parse(`${dateDocument}T00:00:00Z`);
    const cible = new Date(base + Number(rel[1]) * 86_400_000).toISOString().slice(0, 10);
    return { iso: cible, brut: rel[0], relatif: `${rel[1]} jours`, incertain: true };
  }
  if (rel) return { iso: null, brut: rel[0], relatif: `${rel[1]} jours`, incertain: true };
  return { iso: null, brut: null, incertain: true };
}

const AVERTISSEMENT = 'Certaines informations n\'ont pas pu être vérifiées. Une validation humaine est nécessaire.';

/**
 * Analyse complète d'un document.
 * @param {string} texte
 * @param {object} [opts] { nom, aujourdhui }
 * @returns {object} analyse (voir champs ci-dessous) + `document` (entité)
 */
export function analyserDocument(texte, { nom = 'document', aujourdhui = ceJourISO() } = {}) {
  if (typeof texte !== 'string' || texte.trim().length < 10) {
    return {
      nom, texteExtrait: texte || '', lisible: false,
      niveauConfiance: 'incertain', validationHumaineRequise: true,
      avertissement: AVERTISSEMENT,
      administration: null, type: null, dates: [], montants: [], references: [],
      periode: null, echeance: { iso: null, brut: null, incertain: true }, action: null, consequences: [],
      resume: 'Document illisible ou trop court pour être analysé.', checklist: [], reponseProposee: null,
    };
  }

  const administration = detecterAdministration(texte);
  const type = detecterType(texte);
  const dates = detecterDates(texte);
  const montants = detecterMontants(texte);
  const references = detecterReferences(texte);
  const periode = detecterPeriode(texte);
  const action = detecterAction(texte);
  const consequences = detecterConsequences(texte);
  // Date du document = première date rencontrée (heuristique en-tête).
  const dateDocument = dates.length ? dates[0].iso : null;
  const echeance = detecterEcheance(texte, dates, { dateDocument });

  // Confiance globale : jamais « officiel » (document scanné). Dégradée si
  // l'émetteur, le type précis ou toute date manquent.
  let niveauConfiance = 'derive';
  const incertitudes = [];
  if (!administration) { niveauConfiance = 'incertain'; incertitudes.push('émetteur non identifié'); }
  if (!type || type.id === 'courrier') { if (niveauConfiance !== 'incertain') niveauConfiance = 'estimation'; incertitudes.push('type de document imprécis'); }
  if (dates.length === 0) { niveauConfiance = 'incertain'; incertitudes.push('aucune date détectée'); }
  if (action && !echeance.iso) { if (niveauConfiance === 'derive') niveauConfiance = 'estimation'; incertitudes.push('échéance non déterminée'); }
  const validationHumaineRequise = true; // un document importé impose toujours une relecture.

  const resume = construireResume({ administration, type, periode, action, echeance, montants });
  const checklist = construireChecklist({ type, action, echeance, references, consequences });
  const reponseProposee = action ? construireReponse({ administration, type, references, periode, echeance, nom, aujourdhui }) : null;

  const document = creerDocument({
    nom,
    typeDocument: type ? type.id : null,
    administrationEmettrice: administration ? administration.nom : null,
    date: dateDocument,
    periode: periode ? periode.libelle : null,
    texteExtrait: texte,
    donneesStructurees: {
      references, montants: montants.map((m) => m.valeur),
      dates: dates.map((d) => d.iso), consequences,
    },
    echeanceDetectee: echeance.iso,
    actionDemandee: action,
    niveauConfiance,
    validationHumaineRequise,
  });

  return {
    nom, texteExtrait: texte, lisible: true,
    administration: administration ? { id: administration.id, nom: administration.nom } : null,
    type: type ? { id: type.id, nom: type.nom } : null,
    dates, montants, references, periode, action, consequences, echeance,
    niveauConfiance, validationHumaineRequise,
    incertitudes,
    avertissement: (niveauConfiance === 'incertain' || incertitudes.length) ? AVERTISSEMENT : null,
    resume, checklist, reponseProposee,
    document,
  };
}

function construireResume({ administration, type, periode, action, echeance, montants }) {
  const emetteur = administration ? administration.nom : 'un émetteur non identifié';
  const nature = type ? type.nom.toLowerCase() : 'un document administratif';
  let s = `Ce document, émis par ${emetteur}, correspond à ${nature}.`;
  if (periode) s += ` Il concerne la période : ${periode.libelle}.`;
  if (montants.length) s += ` Montant mentionné : ${montants[0].brut}.`;
  if (action) s += ` Ce qui vous est demandé : ${action.toLowerCase()}.`;
  if (echeance.iso) s += ` Date limite : ${echeance.iso}.`;
  else if (echeance.relatif) s += ` Délai indiqué : ${echeance.relatif} (date exacte à confirmer).`;
  return s;
}

function construireChecklist({ type, action, echeance, references, consequences }) {
  const c = ['Vérifier l\'identité de l\'émetteur et l\'objet exact du courrier'];
  if (references.length) c.push(`Noter la ou les références : ${references.map((r) => r.valeur).join(', ')}`);
  else c.push('Repérer la référence / le numéro de dossier');
  if (type && type.id === 'declaration_tva') c.push('Rassembler chiffre d\'affaires, TVA collectée et TVA déductible de la période');
  if (type && type.id === 'facture_peppol') c.push('Vérifier le montant, l\'IBAN et l\'échéance de paiement');
  if (action) c.push(`Préparer les éléments pour : ${action.toLowerCase()}`);
  if (echeance.iso) c.push(`Répondre / agir avant le ${echeance.iso}`);
  else c.push('Confirmer la date limite exacte auprès de l\'administration');
  if (consequences.length) c.push(`Anticiper le risque en cas d\'inaction : ${consequences.join(', ')}`);
  c.push('Faire valider par un professionnel si le montant ou l\'enjeu est important');
  return c;
}

function construireReponse({ administration, type, references, periode, echeance, nom, aujourdhui }) {
  const dest = administration ? administration.nom : '[Administration]';
  const ref = references.length ? references.map((r) => r.valeur).join(', ') : '[référence]';
  return {
    statut: 'projet',
    avertissement: 'PROJET — à relire, compléter et signer. Aucun envoi automatique.',
    objet: `Réponse à votre courrier${type ? ` (${type.nom})` : ''}${references.length ? ` — réf. ${ref}` : ''}`,
    corps: [
      `Madame, Monsieur,`,
      `Je fais suite à votre courrier référencé ${ref}${periode ? ` concernant la période ${periode.libelle}` : ''}.`,
      `Vous trouverez ci-joint les éléments demandés.`,
      echeance.iso ? `Je veille à respecter l'échéance du ${echeance.iso}.` : `Je vous remercie de bien vouloir me préciser l'échéance applicable.`,
      `Je reste à votre disposition pour tout complément.`,
      `Veuillez agréer, Madame, Monsieur, l'expression de mes salutations distinguées.`,
    ].join('\n\n'),
    meta: { destinataire: dest, dateProjet: aujourdhui, sourceDocument: nom },
  };
}

/**
 * Crée un Dossier administratif à partir d'une analyse de document.
 * La provenance est marquée « incertain » (donnée issue d'un document importé,
 * non d'une source officielle) → validation humaine imposée.
 */
export function dossierDepuisDocument(analyse, opts = {}) {
  const aujourdhui = opts.aujourdhui || ceJourISO();
  const categorie = analyse.administration ? analyse.administration.id : (analyse.type ? analyse.type.id : 'document');
  const aEcheanceOuRisque = analyse.echeance.iso || analyse.consequences.length;
  return creerDossier({
    id: opts.id,
    maintenant: opts.maintenant || aujourdhui,
    categorie,
    administration: analyse.administration ? analyse.administration.nom : null,
    typeDemarche: analyse.type ? analyse.type.nom : 'Traitement de courrier',
    statut: 'a_preparer',
    echeance: analyse.echeance.iso || null,
    documentsRequis: analyse.checklist,
    prochainesActions: analyse.action ? [analyse.action] : [],
    risques: analyse.consequences,
    informationsManquantes: analyse.incertitudes || [],
    provenance: aEcheanceOuRisque ? {
      source: `Document importé : ${analyse.nom}`,
      dateVerification: aujourdhui,
      niveauConfiance: 'incertain',
      note: 'Éléments détectés automatiquement dans un document ; à vérifier.',
    } : undefined,
    profilId: opts.profilId ?? null,
    societeId: opts.societeId ?? null,
    documentId: opts.documentId ?? (analyse.document && analyse.document.id) ?? null,
  });
}

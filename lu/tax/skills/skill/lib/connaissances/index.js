/**
 * lib/connaissances — Base de connaissances officielle (Milestone 11).
 *
 * Consolide, en une base requêtable, toutes les règles administratives du
 * projet (catalogue d'obligations + parcours d'installation), chacune reliée à
 * sa source officielle et à sa fraîcheur. Vérifie aussi que chaque source
 * appartient au registre officiel (data/sources.json).
 *
 * RÈGLE STRICTE : aucune réponse réglementaire n'est renvoyée sans source.
 * Lorsqu'une règle n'a pas été vérifiée récemment, la base signale :
 * « Cette information doit être revérifiée avant utilisation. »
 *
 * Aucune dépendance externe.
 */

import { readFileSync, existsSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

import { chargerCatalogue } from '../diagnostic/index.js';
import { evaluerFraicheur, ceJourISO } from '../diagnostic/provenance.js';
import { chargerInstallation } from '../residence/index.js';

const __dirname = dirname(fileURLToPath(import.meta.url));
const SOURCES_PATH = join(__dirname, '..', '..', 'data', 'sources.json');
const GLOSSAIRE_PATH = join(__dirname, '..', '..', 'knowledge', 'glossary.json');
const QA_PATH = join(__dirname, '..', '..', 'knowledge', 'qa', 'cas-reference.json');

const hote = (url) => String(url || '').replace(/^https?:\/\//, '').split('/')[0].toLowerCase();

/** Registre des sources officielles (data/sources.json). */
export function chargerSources(fichier = SOURCES_PATH) {
  return JSON.parse(readFileSync(fichier, 'utf8'));
}

// ---------------------------------------------------------------------------
// Versioning réglementaire : « valable pour les règles en vigueur au <date> »
// ---------------------------------------------------------------------------

/**
 * Une obligation est-elle en vigueur à une date donnée (et pour une juridiction) ?
 * Une obligation sans bloc `validite` est considérée en vigueur (rétrocompatible).
 *
 * @param {object} obligation
 * @param {string} [dateReference] YYYY-MM-DD (défaut : aujourd'hui).
 * @param {object} [opts] { juridiction }
 */
export function enVigueurLe(obligation, dateReference = ceJourISO(), { juridiction } = {}) {
  if (obligation.statut === 'obsolete') return false;
  const v = obligation.validite;
  if (!v) return true;
  if (juridiction && v.juridiction && v.juridiction !== juridiction) return false;
  if (v.validFrom && dateReference < v.validFrom) return false;
  if (v.validUntil && dateReference > v.validUntil) return false;
  return true;
}

/** Filtre un catalogue aux seules obligations en vigueur à `dateReference`. */
export function catalogueEnVigueur(obligations, dateReference = ceJourISO(), opts = {}) {
  return obligations.filter((o) => enVigueurLe(o, dateReference, opts));
}

// ---------------------------------------------------------------------------
// Gouvernance de la connaissance (« fiche de vie » d'une règle)
// ---------------------------------------------------------------------------

/** Statuts de gouvernance possibles. */
export const STATUTS_GOUVERNANCE = ['draft', 'verified', 'a_revoir', 'deprecated'];

/** Ajoute N mois/années/jours à une date ISO (déterministe). */
export function ajouterDelai(dateISO, expression) {
  const m = /^(\d+)\s*(day|days|jour|jours|month|months|mois|year|years|an|ans|année|années)/i.exec(String(expression || ''));
  if (!m) return dateISO;
  const n = Number(m[1]);
  const unite = m[2].toLowerCase();
  const [y, mo, d] = dateISO.split('-').map(Number);
  if (/day|jour/.test(unite)) return new Date(Date.UTC(y, mo - 1, d + n)).toISOString().slice(0, 10);
  if (/year|an|année/.test(unite)) return isoClamp(y + n, mo, d);
  // mois
  const total = (mo - 1) + n;
  return isoClamp(y + Math.floor(total / 12), (total % 12) + 1, d);
}
function isoClamp(y, mo, d) {
  const dernier = new Date(Date.UTC(y, mo, 0)).getUTCDate();
  return `${y}-${String(mo).padStart(2, '0')}-${String(Math.min(d, dernier)).padStart(2, '0')}`;
}

/**
 * Fiche de vie d'une règle : gouvernance normalisée + prochaine revue calculée
 * si absente. Retourne aussi si la revue est due.
 *
 * @param {object} obligation
 * @param {object} [opts] { aujourdhui }
 */
export function ficheDeVie(obligation, { aujourdhui = ceJourISO() } = {}) {
  const g = obligation.gouvernance || {};
  const lastVerified = g.lastVerified || (obligation.validite && obligation.validite.lastVerified) || (obligation.provenance && obligation.provenance.dateVerification) || null;
  const nextReview = g.nextReview || (lastVerified ? ajouterDelai(lastVerified, g.reviewFrequency || '6 months') : null);
  return {
    id: obligation.id,
    nom: obligation.nom,
    owner: g.owner || 'Paperasse Lux',
    status: g.status || 'verified',
    reviewFrequency: g.reviewFrequency || '6 months',
    lastVerified,
    nextReview,
    revueDue: Boolean(nextReview && nextReview <= aujourdhui),
    changeLog: g.changeLog || [],
    source: obligation.provenance ? obligation.provenance.source : null,
  };
}

/** Règles dont la revue est due (nextReview dépassée) à une date donnée. */
export function revuesDues(obligations, { aujourdhui = ceJourISO() } = {}) {
  return obligations.map((o) => ficheDeVie(o, { aujourdhui })).filter((f) => f.revueDue);
}

/**
 * Contrôle de gouvernance : chaque règle a-t-elle une fiche de vie complète et
 * cohérente ? @returns {{ok, problemes: object[]}}
 */
export function verifierGouvernance(obligations, { aujourdhui = ceJourISO() } = {}) {
  const problemes = [];
  for (const o of obligations) {
    const g = o.gouvernance;
    if (!g) { problemes.push({ id: o.id, probleme: 'aucune fiche de gouvernance' }); continue; }
    if (!g.owner) problemes.push({ id: o.id, probleme: 'owner manquant' });
    if (!STATUTS_GOUVERNANCE.includes(g.status)) problemes.push({ id: o.id, probleme: `statut invalide : ${g.status}` });
    if (!g.lastVerified) problemes.push({ id: o.id, probleme: 'lastVerified manquant' });
    if (!g.nextReview) problemes.push({ id: o.id, probleme: 'nextReview manquant' });
    if (g.nextReview && g.lastVerified && g.nextReview < g.lastVerified) problemes.push({ id: o.id, probleme: 'nextReview antérieur à lastVerified' });
  }
  return { ok: problemes.length === 0, problemes };
}

/**
 * Enregistre une revue (déterministe, sans I/O) : renvoie une nouvelle
 * gouvernance avec lastVerified/nextReview mis à jour et une entrée de changeLog.
 */
export function enregistrerRevue(obligation, { date, reason, author = 'Paperasse Lux', status } = {}) {
  if (!date) throw new Error('enregistrerRevue : date requise (YYYY-MM-DD)');
  const g = obligation.gouvernance || { reviewFrequency: '6 months', changeLog: [] };
  return {
    owner: g.owner || 'Paperasse Lux',
    status: status || g.status || 'verified',
    reviewFrequency: g.reviewFrequency || '6 months',
    lastVerified: date,
    nextReview: ajouterDelai(date, g.reviewFrequency || '6 months'),
    changeLog: [...(g.changeLog || []), { date, reason: reason || 'Revue périodique', author }],
  };
}

/**
 * Trois niveaux de qualité, suivis séparément :
 *   1. moteur       (tests unitaires/intégration) — hors périmètre runtime ;
 *   2. connaissance (Knowledge QA, versioning, gouvernance) — mesuré ici ;
 *   3. réponses     (benchmark face à d'autres assistants) — à venir.
 */
export function tableauQualite(obligations, { aujourdhui = ceJourISO() } = {}) {
  const gouv = verifierGouvernance(obligations, { aujourdhui });
  const dues = revuesDues(obligations, { aujourdhui });
  const versionnees = obligations.filter((o) => o.validite).length;
  return {
    moteur: { mesure: 'tests unitaires & intégration', reference: 'npm test' },
    connaissance: {
      regles: obligations.length,
      versionnees,
      gouvernanceComplete: gouv.ok,
      problemesGouvernance: gouv.problemes.length,
      revuesDues: dues.length,
    },
    reponses: { mesure: 'benchmark exactitude/exhaustivité/traçabilité', statut: 'à construire' },
  };
}

/** Glossaire des acronymes (knowledge/glossary.json). */
export function chargerGlossaire(fichier = GLOSSAIRE_PATH) {
  if (!existsSync(fichier)) return { as_of: null, termes: [] };
  return JSON.parse(readFileSync(fichier, 'utf8'));
}

// ---------------------------------------------------------------------------
// Knowledge QA : couverture & impact
// ---------------------------------------------------------------------------

/** Charge les cas QA de référence (knowledge/qa/cas-reference.json). */
export function chargerCasQA(fichier = QA_PATH) {
  if (!existsSync(fichier)) return { cas: [] };
  return JSON.parse(readFileSync(fichier, 'utf8'));
}

/** Cas QA qui couvrent une règle donnée (« quels cas réviser si la règle change »). */
export function casQAParRegle(regleId, cas = chargerCasQA().cas) {
  return cas.filter((c) => Array.isArray(c.regles) && c.regles.includes(regleId));
}

const joursEntreISO = (a, b) => Math.round((Date.parse(`${b}T00:00:00Z`) - Date.parse(`${a}T00:00:00Z`)) / 86_400_000);

/**
 * Coverage Dashboard métier : par domaine (catégorie), le nombre de règles,
 * la part couverte par au moins un cas QA, le nombre de cas QA, et l'âge de la
 * dernière revue. Permet de piloter par les lacunes réelles.
 *
 * @param {object[]} obligations
 * @param {object[]} [cas]
 * @param {object} [opts] { aujourdhui }
 */
export function tableauCouverture(obligations, cas = chargerCasQA().cas, { aujourdhui = ceJourISO() } = {}) {
  const domaines = new Map();
  for (const o of obligations) {
    const dom = o.categorie;
    if (!domaines.has(dom)) domaines.set(dom, { domaine: dom, regles: [], couvertes: new Set(), casQA: new Set(), derniereRevue: null });
    const d = domaines.get(dom);
    d.regles.push(o.id);
    const lv = (o.gouvernance && o.gouvernance.lastVerified) || (o.validite && o.validite.lastVerified) || (o.provenance && o.provenance.dateVerification);
    if (lv && (!d.derniereRevue || lv > d.derniereRevue)) d.derniereRevue = lv;
  }
  for (const c of cas) {
    for (const regleId of c.regles || []) {
      const o = obligations.find((x) => x.id === regleId);
      if (!o) continue;
      const d = domaines.get(o.categorie);
      d.couvertes.add(regleId);
      d.casQA.add(c.id);
    }
  }
  return [...domaines.values()].map((d) => ({
    domaine: d.domaine,
    regles: d.regles.length,
    reglesCouvertes: d.couvertes.size,
    couverture: d.regles.length ? Math.round((d.couvertes.size / d.regles.length) * 100) : 0,
    casQA: d.casQA.size,
    derniereRevue: d.derniereRevue,
    ageRevueJours: d.derniereRevue ? joursEntreISO(d.derniereRevue, aujourdhui) : null,
  })).sort((a, b) => a.couverture - b.couverture);
}

/**
 * Métriques transverses de la connaissance : couverture réglementaire,
 * fraîcheur, périmètre — utiles pour un futur benchmark.
 */
export function metriquesConnaissance(obligations, cas = chargerCasQA().cas, { aujourdhui = ceJourISO() } = {}) {
  const couvertes = new Set();
  for (const c of cas) for (const r of c.regles || []) couvertes.add(r);
  const ages = obligations.map((o) => {
    const lv = (o.gouvernance && o.gouvernance.lastVerified) || (o.validite && o.validite.lastVerified) || (o.provenance && o.provenance.dateVerification);
    return lv ? joursEntreISO(lv, aujourdhui) : null;
  }).filter((x) => x != null);
  const moyenne = ages.length ? Math.round(ages.reduce((a, b) => a + b, 0) / ages.length) : null;
  return {
    regles: obligations.length,
    casQA: cas.length,
    couvertureReglementaire: obligations.length ? Math.round((couvertes.size / obligations.length) * 100) : 0,
    fraicheurMoyenneJours: moyenne,
    ageMaxJours: ages.length ? Math.max(...ages) : null,
    domaines: new Set(obligations.map((o) => o.categorie)).size,
  };
}

// ---------------------------------------------------------------------------
// Coverage-driven development : score de maturité & dette de connaissance
// ---------------------------------------------------------------------------

const FENETRE_REVUE_JOURS = 182; // ~6 mois

/** Score de fraîcheur (0-100) à partir de l'âge depuis la dernière revue. */
function scoreFraicheur(ageJours) {
  if (ageJours == null) return 0;
  return Math.max(0, Math.min(100, Math.round(100 * (1 - ageJours / (2 * FENETRE_REVUE_JOURS)))));
}

/**
 * Score de maturité par domaine : composite couverture / fraîcheur / QA.
 * Un domaine avec beaucoup de règles mais peu de QA n'apparaît pas « terminé ».
 *
 * maturité = 0.40 × couverture + 0.20 × fraîcheur + 0.40 × profondeurQA
 */
export function tableauMaturite(obligations, cas = chargerCasQA().cas, { aujourdhui = ceJourISO() } = {}) {
  const tc = tableauCouverture(obligations, cas, { aujourdhui });
  return tc.map((d) => {
    const fraicheur = scoreFraicheur(d.ageRevueJours);
    const profondeurQA = Math.min(100, Math.round((d.casQA / Math.max(1, d.regles)) * 100));
    const maturite = Math.round(0.40 * d.couverture + 0.20 * fraicheur + 0.40 * profondeurQA);
    return { domaine: d.domaine, couverture: d.couverture, fraicheur, qa: profondeurQA, maturite, regles: d.regles, casQA: d.casQA };
  }).sort((a, b) => a.maturite - b.maturite);
}

/**
 * Dette de connaissance : backlog généré automatiquement.
 *   - règles sans cas QA ;
 *   - règles bientôt à réviser ;
 *   - règles à source unique / niveau de confiance faible (à corroborer) ;
 *   - règles non reliées à un événement de vie ;
 *   - domaines à faible couverture.
 *
 * @param {object[]} obligations
 * @param {object} [opts] { cas, evenements (data), aujourdhui, seuilRevueJours, seuilCouverture }
 */
export function detteConnaissance(obligations, opts = {}) {
  const aujourdhui = opts.aujourdhui || ceJourISO();
  const cas = opts.cas || chargerCasQA().cas;
  const seuilRevue = opts.seuilRevueJours ?? 90;
  const seuilCouv = opts.seuilCouverture ?? 50;

  const couvertes = new Set();
  for (const c of cas) for (const r of c.regles || []) couvertes.add(r);
  const reliesEvenement = new Set();
  for (const ev of (opts.evenements || [])) for (const id of (ev.obligations || [])) reliesEvenement.add(id);

  const reglesSansQA = obligations.filter((o) => !couvertes.has(o.id)).map((o) => o.id);
  const revuesBientot = obligations.filter((o) => {
    const nr = o.gouvernance && o.gouvernance.nextReview;
    return nr && joursEntreISO(aujourdhui, nr) <= seuilRevue;
  }).map((o) => o.id);
  const sourceACorroborer = obligations.filter((o) => o.provenance && o.provenance.niveauConfiance !== 'officiel').map((o) => o.id);
  const nonRelieesEvenement = opts.evenements ? obligations.filter((o) => !reliesEvenement.has(o.id)).map((o) => o.id) : [];
  const domainesFaibles = tableauCouverture(obligations, cas, { aujourdhui }).filter((d) => d.couverture < seuilCouv).map((d) => d.domaine);

  const items = [
    { type: 'regles_sans_qa', gravite: 'haute', total: reglesSansQA.length, elements: reglesSansQA },
    { type: 'revues_bientot_dues', gravite: 'moyenne', total: revuesBientot.length, elements: revuesBientot },
    { type: 'source_a_corroborer', gravite: 'moyenne', total: sourceACorroborer.length, elements: sourceACorroborer },
    { type: 'non_reliees_evenement', gravite: 'basse', total: nonRelieesEvenement.length, elements: nonRelieesEvenement },
    { type: 'domaines_faible_couverture', gravite: 'haute', total: domainesFaibles.length, elements: domainesFaibles },
  ];
  return { aujourdhui, total: items.reduce((s, i) => s + i.total, 0), items: items.filter((i) => i.total > 0) };
}

/** Explique un acronyme / terme (recherche insensible à la casse). */
export function expliquer(terme) {
  const t = String(terme || '').trim().toLowerCase();
  return chargerGlossaire().termes.find((x) => x.sigle.toLowerCase() === t || x.terme.toLowerCase() === t) || null;
}

/** Ensemble des hôtes de sources officielles connus. */
export function hotesConnus() {
  const s = chargerSources();
  return new Set((s.sources || []).map((x) => hote(x.url)));
}

/**
 * Construit la base de connaissances unifiée.
 *
 * @param {object} [opts] { aujourdhui, seuilJours }
 * @returns {object[]} entrées { id, titre, categorie, population, frequence,
 *   source, dateVerification, niveauConfiance, statut, fraicheur }
 */
export function baseConnaissances({ aujourdhui = ceJourISO(), seuilJours } = {}) {
  const entrees = [];

  const { obligations } = chargerCatalogue();
  for (const ob of obligations) {
    const p = ob.provenance;
    entrees.push({
      id: ob.id,
      origine: 'obligation',
      titre: ob.nom,
      categorie: ob.categorie,
      population: ob.populationConcernee,
      frequence: ob.frequence,
      autorite: ob.autoriteCompetente || null,
      source: p.source,
      dateVerification: p.dateVerification,
      niveauConfiance: p.niveauConfiance,
      statut: ob.statut,
      validite: ob.validite || null,
      gouvernance: ob.gouvernance || null,
      fraicheur: evaluerFraicheur(p, { aujourdhui, seuilJours }),
    });
  }

  const install = chargerInstallation();
  for (const e of install.etapes || []) {
    const p = { source: e.source, dateVerification: install.as_of, niveauConfiance: 'derive' };
    entrees.push({
      id: `install_${e.id}`,
      origine: 'installation',
      titre: e.titre,
      categorie: 'residence',
      population: e.public,
      frequence: null,
      autorite: e.administration || null,
      source: e.source,
      dateVerification: install.as_of,
      niveauConfiance: 'derive',
      statut: 'actif',
      fraicheur: evaluerFraicheur(p, { aujourdhui, seuilJours }),
    });
  }

  return entrees;
}

/** Recherche plein-texte simple (titre, catégorie, id, autorité). */
export function rechercher(terme, opts = {}) {
  const t = String(terme || '').toLowerCase();
  return baseConnaissances(opts).filter((e) =>
    [e.titre, e.categorie, e.id, e.autorite].some((c) => String(c || '').toLowerCase().includes(t)),
  );
}

/** Règles à revérifier (fraîcheur dépassée ou niveau incertain). */
export function reglesARevalider(opts = {}) {
  return baseConnaissances(opts).filter((e) => e.fraicheur.aRevalider);
}

/**
 * Cite une règle : renvoie l'entrée avec sa source. Lève une erreur si la
 * règle est introuvable ou dépourvue de source (garde-fou anti-« sans source »).
 */
export function citer(id, opts = {}) {
  const e = baseConnaissances(opts).find((x) => x.id === id);
  if (!e) throw new Error(`Règle introuvable : ${id}`);
  if (!e.source) throw new Error(`Règle ${id} sans source : diffusion interdite.`);
  return {
    ...e,
    citation: `${e.titre} — ${e.autorite || 'autorité non précisée'}. Source : ${e.source} (${e.niveauConfiance}, vérifié le ${e.dateVerification}).`
      + (e.fraicheur.aRevalider ? ' ⚠ Cette information doit être revérifiée avant utilisation.' : ''),
  };
}

/**
 * Vérifie que chaque source d'obligation appartient au registre officiel.
 * @returns {object[]} entrées dont l'hôte n'est pas dans data/sources.json
 */
export function verifierSourcesConnues(opts = {}) {
  const connus = hotesConnus();
  return baseConnaissances(opts)
    .filter((e) => e.origine === 'obligation')
    .filter((e) => !connus.has(hote(e.source)))
    .map((e) => ({ id: e.id, source: e.source, hote: hote(e.source) }));
}

/** Rapport de synthèse de la base (compteurs par niveau + à revérifier). */
export function rapport(opts = {}) {
  const base = baseConnaissances(opts);
  const parNiveau = {};
  for (const e of base) parNiveau[e.niveauConfiance] = (parNiveau[e.niveauConfiance] || 0) + 1;
  return {
    total: base.length,
    parNiveau,
    aRevalider: base.filter((e) => e.fraicheur.aRevalider).length,
    sansSource: base.filter((e) => !e.source).length,
  };
}

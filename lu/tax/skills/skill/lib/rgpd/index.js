/**
 * lib/rgpd — Sécurité, confidentialité & conformité (Milestone 12).
 *
 * Fournit les primitives de conformité RGPD, sans dépendance externe
 * (chiffrement via le module intégré node:crypto) :
 *   - chiffrement/déchiffrement au repos (AES-256-GCM, clé dérivée par scrypt) ;
 *   - masquage des données sensibles (revenus, IBAN, identifiants…) ;
 *   - journalisation des accès ;
 *   - consentement explicite (garde à l'entrée du store) ;
 *   - durées de conservation et purge ;
 *   - store sécurisé (isolation par propriétaire + journal + consentement).
 *
 * L'hébergement des données réelles (UE) relève de l'exploitation ; ce module
 * fournit les briques logicielles côté application.
 */

import { createCipheriv, createDecipheriv, randomBytes, scryptSync } from 'node:crypto';
import { ceJourISO } from '../diagnostic/provenance.js';

// ---------------------------------------------------------------------------
// Chiffrement au repos (AES-256-GCM)
// ---------------------------------------------------------------------------

/**
 * Chiffre une chaîne avec une phrase secrète. Renvoie un paquet autoportant
 * (sel + IV + tag + données, encodés base64) déchiffrable par `dechiffrer`.
 */
export function chiffrer(texte, motDePasse) {
  if (typeof texte !== 'string') throw new Error('chiffrer : texte (string) requis');
  if (!motDePasse) throw new Error('chiffrer : phrase secrète requise');
  const sel = randomBytes(16);
  const iv = randomBytes(12);
  const cle = scryptSync(motDePasse, sel, 32);
  const cipher = createCipheriv('aes-256-gcm', cle, iv);
  const chiffre = Buffer.concat([cipher.update(texte, 'utf8'), cipher.final()]);
  const tag = cipher.getAuthTag();
  return {
    v: 1,
    algo: 'aes-256-gcm',
    sel: sel.toString('base64'),
    iv: iv.toString('base64'),
    tag: tag.toString('base64'),
    data: chiffre.toString('base64'),
  };
}

/** Déchiffre un paquet produit par `chiffrer`. Lève une erreur si altéré. */
export function dechiffrer(paquet, motDePasse) {
  if (!paquet || !paquet.data) throw new Error('dechiffrer : paquet invalide');
  const sel = Buffer.from(paquet.sel, 'base64');
  const iv = Buffer.from(paquet.iv, 'base64');
  const tag = Buffer.from(paquet.tag, 'base64');
  const cle = scryptSync(motDePasse, sel, 32);
  const decipher = createDecipheriv('aes-256-gcm', cle, iv);
  decipher.setAuthTag(tag);
  return Buffer.concat([decipher.update(Buffer.from(paquet.data, 'base64')), decipher.final()]).toString('utf8');
}

export const chiffrerObjet = (obj, mdp) => chiffrer(JSON.stringify(obj), mdp);
export const dechiffrerObjet = (paquet, mdp) => JSON.parse(dechiffrer(paquet, mdp));

// ---------------------------------------------------------------------------
// Masquage des données sensibles
// ---------------------------------------------------------------------------

/** Champs considérés sensibles par défaut. */
export const CHAMPS_SENSIBLES = [
  'revenus', 'revenusApprox', 'iban', 'coordonneesBancaires', 'tva', 'numeroTVA',
  'matricule', 'email', 'telephone', 'dateNaissance', 'sante', 'nationalite',
];

function masquerValeur(cle, valeur) {
  if (valeur == null) return valeur;
  if (typeof valeur === 'number') return '***';
  const s = String(valeur);
  if (cle === 'email' && s.includes('@')) {
    const [u, d] = s.split('@');
    return `${u.slice(0, 1)}***@${d}`;
  }
  if (s.length <= 2) return '***';
  return `${s.slice(0, 2)}***`;
}

/**
 * Renvoie une copie de l'objet avec les champs sensibles masqués (récursif).
 * @param {object} obj
 * @param {object} [opts] { champs }
 */
export function masquer(obj, { champs = CHAMPS_SENSIBLES } = {}) {
  const set = new Set(champs);
  const parcourir = (v) => {
    if (Array.isArray(v)) return v.map(parcourir);
    if (v && typeof v === 'object') {
      const out = {};
      for (const [k, val] of Object.entries(v)) {
        out[k] = set.has(k) ? masquerValeur(k, val) : parcourir(val);
      }
      return out;
    }
    return v;
  };
  return parcourir(obj);
}

// ---------------------------------------------------------------------------
// Journalisation des accès
// ---------------------------------------------------------------------------

/**
 * Journal d'accès en mémoire (horodatage injectable pour les tests).
 */
export function creerJournal() {
  const evenements = [];
  return {
    enregistrer({ action, collection = null, id = null, acteur = 'système', details = null, horodatage } = {}) {
      const evt = { horodatage: horodatage || ceJourISO(), action, collection, id, acteur, details };
      evenements.push(evt);
      return evt;
    },
    lister() { return evenements.slice(); },
    pour(collection, id) { return evenements.filter((e) => e.collection === collection && (id ? e.id === id : true)); },
    exporter() { return JSON.parse(JSON.stringify(evenements)); },
  };
}

// ---------------------------------------------------------------------------
// Consentement explicite
// ---------------------------------------------------------------------------

export const consentementValide = (profil) => Boolean(profil && profil.consentementRGPD);

export function exigerConsentement(profil) {
  if (!consentementValide(profil)) {
    throw new Error('Consentement RGPD requis avant tout traitement de ce profil (consentementRGPD manquant).');
  }
  return true;
}

// ---------------------------------------------------------------------------
// Durées de conservation & purge
// ---------------------------------------------------------------------------

/**
 * Durées de conservation indicatives par catégorie (en années). À confirmer
 * selon la finalité et le texte applicable.
 */
export const DUREES_CONSERVATION = Object.freeze({
  fiscal: 10,          // pièces comptables/fiscales (AO / loi comptable)
  tva: 10,
  societe: 10,
  social: 5,
  document: 3,
  residence: 5,
  defaut: 3,
});

export const CONSERVATION_PROVENANCE = Object.freeze({
  source: 'https://cnpd.public.lu',
  niveauConfiance: 'derive',
  note: 'Durées indicatives ; la durée réelle dépend de la finalité et du texte applicable — à confirmer.',
});

/** Nombre d'années entre deux dates ISO. */
function anneesEntre(depuis, jusqua) {
  return (Date.parse(`${jusqua}T00:00:00Z`) - Date.parse(`${depuis}T00:00:00Z`)) / (365.25 * 86_400_000);
}

/**
 * Une entité a-t-elle dépassé sa durée de conservation ?
 * @param {object} entite       Doit porter une date de référence.
 * @param {object} [opts]       { aujourdhui, categorie, champDate, dureeAnnees }
 */
export function estExpiree(entite, { aujourdhui = ceJourISO(), categorie, champDate = 'date', dureeAnnees } = {}) {
  const ref = entite[champDate] || entite.dateCreation || entite.dateMiseAJour || null;
  if (!ref) return { expiree: false, raison: 'aucune date de référence' };
  const cat = categorie || entite.categorie || 'defaut';
  const duree = dureeAnnees ?? DUREES_CONSERVATION[cat] ?? DUREES_CONSERVATION.defaut;
  const age = anneesEntre(ref, aujourdhui);
  return { expiree: age > duree, ageAnnees: Math.round(age * 100) / 100, dureeAnnees: duree, dateReference: ref };
}

/**
 * Sépare une liste d'entités en conservées / expirées (droit à l'oubli).
 */
export function purger(entites, opts = {}) {
  const conserves = [];
  const expires = [];
  for (const e of entites) {
    (estExpiree(e, opts).expiree ? expires : conserves).push(e);
  }
  return { conserves, expires };
}

// ---------------------------------------------------------------------------
// Store sécurisé (isolation + journal + consentement)
// ---------------------------------------------------------------------------

/**
 * Enveloppe un store (lib/diagnostic/store) pour :
 *   - exiger le consentement RGPD à l'ajout d'un profil ;
 *   - journaliser chaque accès (ajout, lecture, suppression, export).
 *
 * @param {object} store    Store de base (creerStore / creerStoreMemoire).
 * @param {object} [opts]   { journal, acteur }
 */
export function creerStoreSecurise(store, { journal = creerJournal(), acteur = 'utilisateur' } = {}) {
  const log = (action, collection, id, details) => journal.enregistrer({ action, collection, id, acteur, details });
  return {
    journal,
    ajouter(collection, entite) {
      if (collection === 'profils') exigerConsentement(entite);
      const stocke = store.ajouter(collection, entite);
      log('ajouter', collection, stocke.id);
      return stocke;
    },
    obtenir(collection, id) { log('lire', collection, id); return store.obtenir(collection, id); },
    lister(collection) { log('lister', collection, null); return store.lister(collection); },
    listerPour(collection, filtre) { log('lister_pour', collection, null, filtre); return store.listerPour(collection, filtre); },
    mettreAJour(collection, id, patch) { log('modifier', collection, id); return store.mettreAJour(collection, id, patch); },
    supprimer(collection, id) { log('supprimer', collection, id); return store.supprimer(collection, id); },
    exporter() { log('exporter', null, null); return store.exporter(); },
  };
}

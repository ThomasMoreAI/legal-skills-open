/**
 * lib/faia — Générateur du Fichier d'Audit Informatisé (FAIA) pour l'AED Luxembourg.
 *
 * Format : SAF-T LU 2.01 (Standard Audit File for Tax, profil luxembourgeois).
 * Source : Administration de l'Enregistrement, des Domaines et de la TVA (AED),
 *   circulaire FAIA, schéma XSD officiel publié par l'AED.
 *
 * Le FAIA est exigible lors de tout contrôle TVA depuis le 1er janvier 2011.
 * Il doit contenir, pour la période contrôlée :
 *   - Header (entreprise, période, devise, version logiciel)
 *   - MasterFiles (comptes, clients, fournisseurs, table TVA)
 *   - GeneralLedgerEntries (écritures comptables, équilibrées D=C)
 *   - SourceDocuments (factures vente/achat, paiements)
 *
 * LIMITATIONS CONNUES :
 *   - Ne génère pas la section <Owners> (rare, à ajouter manuellement si demandée).
 *   - Pas de support multi-devises avec conversions historiques (mono-devise EUR).
 *   - Pas de validation XSD complète : utiliser un validateur XSD externe avant dépôt.
 */

import { validerFAIAInput } from './validation.js';
import {
  buildHeader,
  buildMasterFiles,
  buildGeneralLedgerEntries,
  buildSourceDocuments,
} from './xml.js';

export { validerFAIAInput, TAX_CODES_LU } from './validation.js';

/**
 * Génère un fichier FAIA XML conforme au profil SAF-T LU 2.01.
 *
 * @param {object} input
 * @param {object} input.company         { rcs, matriculeTVA, raisonSociale, siegeSocial }
 * @param {object} input.period          { start: 'YYYY-MM-DD', end: 'YYYY-MM-DD', fiscalYear?: 'YYYY' }
 * @param {Array}  input.accounts        Plan comptable utilisé sur la période
 * @param {Array=} input.customers       Comptes clients (defaults: [])
 * @param {Array=} input.suppliers       Comptes fournisseurs (defaults: [])
 * @param {Array=} input.taxTable        Table TVA (defaults: TAX_CODES_LU)
 * @param {Array}  input.entries         Écritures de grand livre (équilibrées)
 * @param {Array=} input.salesInvoices   Factures émises
 * @param {Array=} input.purchaseInvoices Factures reçues
 * @param {Array=} input.payments        Paiements
 * @param {object=} options
 * @param {string=} options.softwareName    (default: 'Paperasse Lux')
 * @param {string=} options.softwareVersion (default: lit package.json)
 * @param {boolean=} options.skipValidation (default: false ; déconseillé)
 *
 * @returns {{ xml: string, totals: object, validation: object }}
 *   - xml         : chaîne XML prête à être déposée
 *   - totals      : { debit, credit, entryCount, salesCount, purchaseCount }
 *   - validation  : { valide, erreurs[], avertissements[] }
 */
export function genererFAIA(input, options = {}) {
  const validation = validerFAIAInput(input);
  if (!validation.valide && !options.skipValidation) {
    const err = new Error(`Entrée FAIA invalide :\n  - ${validation.erreurs.join('\n  - ')}`);
    err.validation = validation;
    throw err;
  }

  const opts = {
    softwareName: options.softwareName || 'Paperasse Lux',
    softwareVersion: options.softwareVersion || PAPERASSE_LUX_VERSION,
    softwareId: options.softwareId || 'paperasse-lux',
  };

  const entries = input.entries || [];
  const salesInvoices = input.salesInvoices || [];
  const purchaseInvoices = input.purchaseInvoices || [];
  const payments = input.payments || [];

  const totals = {
    debit: round2(sum(entries.flatMap((e) => (e.lines || []).map((l) => l.debit || 0)))),
    credit: round2(sum(entries.flatMap((e) => (e.lines || []).map((l) => l.credit || 0)))),
    entryCount: entries.length,
    salesCount: salesInvoices.length,
    purchaseCount: purchaseInvoices.length,
  };

  const headerDate = new Date().toISOString().slice(0, 10);
  const xml = [
    `<?xml version="1.0" encoding="UTF-8"?>`,
    `<AuditFile xmlns="urn:OECD:StandardAuditFile-Tax:LU_2.01">`,
    buildHeader(input, opts, headerDate),
    buildMasterFiles(input),
    buildGeneralLedgerEntries(entries, totals),
    buildSourceDocuments(salesInvoices, purchaseInvoices, payments),
    `</AuditFile>`,
  ].filter(Boolean).join('\n');

  return { xml, totals, validation };
}

const PAPERASSE_LUX_VERSION = '0.8.0';

function sum(arr) { return arr.reduce((a, b) => a + Number(b || 0), 0); }
function round2(n) { return Math.round(n * 100) / 100; }

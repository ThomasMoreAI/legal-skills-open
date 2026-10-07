/**
 * lib/bank-parsers — Parseurs de relevés bancaires luxembourgeois.
 *
 * Auto-détecte le format (BCEE/POST/BIL/générique CSV ou CAMT.053 XML)
 * et retourne une liste normalisée de transactions :
 *
 *   {
 *     date: '2025-03-12',           // ISO yyyy-mm-dd
 *     date_valeur: '2025-03-13',
 *     libelle: 'Virement client X',
 *     montant: 1234.56,             // signé : positif=crédit, négatif=débit
 *     sens: 'credit' | 'debit',
 *     devise: 'EUR',
 *     solde: 5678.90,               // null si non disponible
 *     reference: 'INV-2025-001',    // null si absent
 *     banque: 'BCEE'
 *   }
 *
 * Usage :
 *   import { parseBankStatement } from './lib/bank-parsers/index.js';
 *   const result = parseBankStatement(textContent);
 *   // → { format: 'bcee', count: 42, transactions: [...] }
 */

import { parseCSV } from './csv.js';
import * as bcee from './bcee.js';
import * as post from './post.js';
import * as bil from './bil.js';
import * as generic from './generic.js';
import * as camt053 from './camt053.js';

const CSV_PROFILES = [bcee, post, bil, generic];

export function parseBankStatement(text) {
  // Détection XML/CAMT.053 d'abord
  if (camt053.isCAMT053(text)) {
    const transactions = camt053.parse(text);
    return { format: 'camt053', count: transactions.length, transactions };
  }
  // Sinon, CSV : détecte le profil avec le meilleur score
  const csv = parseCSV(text);
  if (csv.rows.length === 0) {
    return { format: 'inconnu', count: 0, transactions: [], erreur: 'Fichier vide ou non-CSV' };
  }
  let best = { profile: generic, score: -1 };
  for (const p of CSV_PROFILES) {
    const score = p.detect(csv);
    if (score > best.score) best = { profile: p, score };
  }
  const transactions = best.profile.map(csv);
  return {
    format: best.profile.id,
    count: transactions.length,
    transactions,
    confiance: best.score >= 3 ? 'haute' : best.score >= 2 ? 'moyenne' : 'faible — vérifier le mapping',
  };
}

/**
 * Agrège les transactions par sens (crédits/débits) et calcule les totaux.
 */
export function aggregate(transactions) {
  let credits = 0, debits = 0;
  for (const t of transactions) {
    if (t.montant == null) continue;
    if (t.montant >= 0) credits += t.montant;
    else debits += -t.montant;
  }
  return {
    nb_transactions: transactions.length,
    total_credits: Math.round(credits * 100) / 100,
    total_debits: Math.round(debits * 100) / 100,
    flux_net: Math.round((credits - debits) * 100) / 100,
  };
}

export { bcee, post, bil, generic, camt053 };

/**
 * post.js — Profil POST Finance Luxembourg (CCPL).
 *
 * Format CSV typique :
 *   Date;Description;Montant;Devise;Solde après opération
 *
 * Séparateur : ; (point-virgule)
 * Montants : format européen, signe négatif pour débit ("-150,00")
 *
 * NOTE : à valider sur un export réel CCPL.
 */

import { parseAmount, parseDate } from './csv.js';

export const id = 'post';
export const labels = ['POST', 'POST Finance', 'CCPL', 'CCPLLULL'];

const COLS = {
  date: ['Date', 'Date opération', 'Date d\'opération'],
  description: ['Description', 'Libellé', 'Communication'],
  montant: ['Montant', 'Amount'],
  devise: ['Devise', 'Currency'],
  solde: ['Solde', 'Solde après opération'],
};

function pick(row, header, names) {
  for (const n of names) {
    const i = header.findIndex(h => h.toLowerCase() === n.toLowerCase());
    if (i >= 0 && row[i] !== undefined) return row[i];
  }
  return null;
}

export function detect({ header, separator }) {
  if (separator !== ';') return 0;
  const lower = header.map(h => h.toLowerCase());
  let score = 0;
  // POST utilise une seule colonne montant signée (vs BCEE débit/crédit)
  if (lower.includes('montant') && !lower.includes('débit')) score += 3;
  if (lower.includes('description')) score += 1;
  if (lower.includes('solde après opération')) score += 2;
  return score;
}

export function map({ header, rows }) {
  return rows.map(row => {
    const montant = parseAmount(pick(row, header, COLS.montant));
    return {
      date: parseDate(pick(row, header, COLS.date)),
      date_valeur: null,
      libelle: (pick(row, header, COLS.description) || '').trim(),
      montant: montant != null ? Math.round(montant * 100) / 100 : null,
      sens: montant != null ? (montant >= 0 ? 'credit' : 'debit') : null,
      devise: (pick(row, header, COLS.devise) || 'EUR').trim(),
      solde: parseAmount(pick(row, header, COLS.solde)),
      reference: null,
      banque: 'POST',
    };
  });
}

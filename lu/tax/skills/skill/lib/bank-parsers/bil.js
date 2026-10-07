/**
 * bil.js — Profil BIL (Banque Internationale à Luxembourg).
 *
 * Format CSV typique (export BILnet) :
 *   Date;Date valeur;Libellé;Montant;Devise;Solde
 *
 * Séparateur : ; (point-virgule)
 * Montants : format européen, signé
 *
 * NOTE : à valider sur un export réel BILnet.
 */

import { parseAmount, parseDate } from './csv.js';

export const id = 'bil';
export const labels = ['BIL', 'BILLULL'];

const COLS = {
  date: ['Date', 'Date opération'],
  dateValeur: ['Date valeur'],
  libelle: ['Libellé', 'Description', 'Communication'],
  montant: ['Montant', 'Amount'],
  devise: ['Devise', 'Currency'],
  solde: ['Solde'],
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
  if (lower.includes('montant') && lower.includes('date valeur') && !lower.includes('description')) score += 2;
  if (lower.includes('libellé') && lower.includes('montant')) score += 2;
  return score;
}

export function map({ header, rows }) {
  return rows.map(row => {
    const montant = parseAmount(pick(row, header, COLS.montant));
    return {
      date: parseDate(pick(row, header, COLS.date)),
      date_valeur: parseDate(pick(row, header, COLS.dateValeur)),
      libelle: (pick(row, header, COLS.libelle) || '').trim(),
      montant: montant != null ? Math.round(montant * 100) / 100 : null,
      sens: montant != null ? (montant >= 0 ? 'credit' : 'debit') : null,
      devise: (pick(row, header, COLS.devise) || 'EUR').trim(),
      solde: parseAmount(pick(row, header, COLS.solde)),
      reference: null,
      banque: 'BIL',
    };
  });
}

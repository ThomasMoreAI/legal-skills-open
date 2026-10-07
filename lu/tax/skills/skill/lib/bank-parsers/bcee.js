/**
 * bcee.js — Profil BCEE / Spuerkeess (Banque et Caisse d'Épargne de l'État).
 *
 * Format CSV typique :
 *   Date;Date valeur;Libellé;Débit;Crédit;Solde;Devise;Référence
 *
 * Séparateur : ; (point-virgule)
 * Encodage : UTF-8 ou ISO-8859-1
 * Montants : format européen ("1.234,56")
 *
 * NOTE : profil basé sur la documentation publique BCEE de l'export S-Net.
 * Les noms de colonnes peuvent légèrement varier selon la version de S-Net.
 * À valider sur un export réel et à ajuster `COLS` si nécessaire.
 */

import { parseAmount, parseDate } from './csv.js';

export const id = 'bcee';
export const labels = ['BCEE', 'Spuerkeess', 'BCEELULL'];

const COLS = {
  date: ['Date', 'Date opération', 'Date d\'opération'],
  dateValeur: ['Date valeur'],
  libelle: ['Libellé', 'Communication', 'Description'],
  debit: ['Débit', 'Debit'],
  credit: ['Crédit', 'Credit'],
  solde: ['Solde'],
  devise: ['Devise', 'Currency'],
  reference: ['Référence', 'Reference', 'No. de référence'],
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
  if (lower.includes('débit') || lower.includes('debit')) score += 2;
  if (lower.includes('crédit') || lower.includes('credit')) score += 2;
  if (lower.includes('libellé')) score += 1;
  if (lower.includes('date valeur')) score += 1;
  return score;
}

export function map({ header, rows }) {
  return rows.map(row => {
    const debit = parseAmount(pick(row, header, COLS.debit));
    const credit = parseAmount(pick(row, header, COLS.credit));
    const montant = (credit || 0) - (debit || 0);
    return {
      date: parseDate(pick(row, header, COLS.date)),
      date_valeur: parseDate(pick(row, header, COLS.dateValeur)),
      libelle: (pick(row, header, COLS.libelle) || '').trim(),
      montant: Math.round(montant * 100) / 100,
      sens: montant >= 0 ? 'credit' : 'debit',
      devise: (pick(row, header, COLS.devise) || 'EUR').trim(),
      solde: parseAmount(pick(row, header, COLS.solde)),
      reference: (pick(row, header, COLS.reference) || '').trim() || null,
      banque: 'BCEE',
    };
  });
}

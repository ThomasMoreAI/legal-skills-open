/**
 * generic.js — Profil générique fallback.
 *
 * Reconnaît les colonnes par mots-clés (date, libellé, montant) en FR/EN/DE.
 * Utilisé quand aucun profil spécifique ne matche.
 */

import { parseAmount, parseDate } from './csv.js';

export const id = 'generic';
export const labels = ['Generic', 'CSV générique'];

const KEYWORDS = {
  date: ['date', 'datum', 'buchung', 'opération'],
  libelle: ['libellé', 'libelle', 'description', 'communication', 'verwendungszweck', 'narrative', 'détails'],
  debit: ['débit', 'debit', 'soll'],
  credit: ['crédit', 'credit', 'haben'],
  montant: ['montant', 'amount', 'betrag', 'value'],
  devise: ['devise', 'currency', 'währung', 'ccy'],
  solde: ['solde', 'balance', 'saldo'],
};

function findCol(header, keywords) {
  const lower = header.map(h => h.toLowerCase().trim());
  for (const kw of keywords) {
    const i = lower.findIndex(h => h.includes(kw));
    if (i >= 0) return i;
  }
  return -1;
}

export function detect() { return 0.5; } // toujours un fallback faible

export function map({ header, rows }) {
  const idx = {
    date: findCol(header, KEYWORDS.date),
    libelle: findCol(header, KEYWORDS.libelle),
    debit: findCol(header, KEYWORDS.debit),
    credit: findCol(header, KEYWORDS.credit),
    montant: findCol(header, KEYWORDS.montant),
    devise: findCol(header, KEYWORDS.devise),
    solde: findCol(header, KEYWORDS.solde),
  };
  return rows.map(row => {
    let montant = null;
    if (idx.montant >= 0) {
      montant = parseAmount(row[idx.montant]);
    } else if (idx.debit >= 0 || idx.credit >= 0) {
      const d = parseAmount(row[idx.debit]) || 0;
      const c = parseAmount(row[idx.credit]) || 0;
      montant = c - d;
    }
    return {
      date: idx.date >= 0 ? parseDate(row[idx.date]) : null,
      date_valeur: null,
      libelle: idx.libelle >= 0 ? (row[idx.libelle] || '').trim() : '',
      montant: montant != null ? Math.round(montant * 100) / 100 : null,
      sens: montant != null ? (montant >= 0 ? 'credit' : 'debit') : null,
      devise: idx.devise >= 0 ? (row[idx.devise] || 'EUR').trim() : 'EUR',
      solde: idx.solde >= 0 ? parseAmount(row[idx.solde]) : null,
      reference: null,
      banque: 'Inconnue',
    };
  });
}

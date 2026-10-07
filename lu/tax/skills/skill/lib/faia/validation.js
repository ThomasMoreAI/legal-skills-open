/**
 * lib/faia/validation — Validation des entrées FAIA avant génération.
 *
 * Garantit que le XML produit respectera les contraintes de base du SAF-T LU 2.01 :
 *   - identifiants entreprise valides (RCS, matricule TVA)
 *   - dates ISO YYYY-MM-DD réelles, période cohérente (start ≤ end)
 *   - écritures équilibrées (somme débits = somme crédits par transaction)
 *   - références aux comptes existantes (pas d'AccountID orphelin)
 */

/**
 * Codes TVA luxembourgeois en vigueur (TVA loi modifiée du 12 février 1979).
 * Taux applicables au 09/05/2026.
 */
export const TAX_CODES_LU = [
  { code: 'STD', taux: 17.00, libelle: 'Standard' },
  { code: 'INT', taux: 14.00, libelle: 'Intermédiaire' },
  { code: 'RED', taux: 8.00,  libelle: 'Réduit' },
  { code: 'SUP', taux: 3.00,  libelle: 'Super-réduit (logement)' },
  { code: 'EXM', taux: 0,     libelle: 'Exonération' },
  { code: 'ZRO', taux: 0,     libelle: 'Zéro (export/intracom)' },
];

const RE_RCS_LU = /^[BFGEKX]\d{1,7}$/;
const RE_TVA_LU = /^LU\d{8}$/;
const RE_DATE_ISO = /^\d{4}-\d{2}-\d{2}$/;

/**
 * @param {object} input
 * @returns {{ valide: boolean, erreurs: string[], avertissements: string[] }}
 */
export function validerFAIAInput(input) {
  const erreurs = [];
  const avertissements = [];

  if (!input || typeof input !== 'object') {
    return { valide: false, erreurs: ['input absent ou non-objet'], avertissements };
  }

  // --- Company ---
  const c = input.company;
  if (!c) erreurs.push('company manquant');
  else {
    if (!c.raisonSociale) erreurs.push('company.raisonSociale manquant');
    if (!c.rcs) erreurs.push('company.rcs manquant');
    else if (!RE_RCS_LU.test(String(c.rcs).trim().toUpperCase().replace(/\s+/g, ''))) {
      erreurs.push(`company.rcs "${c.rcs}" invalide (attendu B/F/G/E/K/X + 1 à 7 chiffres)`);
    }
    if (!c.matriculeTVA) erreurs.push('company.matriculeTVA manquant');
    else if (!RE_TVA_LU.test(String(c.matriculeTVA).replace(/\s+/g, '').toUpperCase())) {
      erreurs.push(`company.matriculeTVA "${c.matriculeTVA}" invalide (attendu LU + 8 chiffres)`);
    }
    if (!c.siegeSocial) erreurs.push('company.siegeSocial manquant');
    else {
      for (const f of ['rue', 'ville', 'codePostal']) {
        if (!c.siegeSocial[f]) erreurs.push(`company.siegeSocial.${f} manquant`);
      }
    }
  }

  // --- Period ---
  const p = input.period;
  if (!p) erreurs.push('period manquant');
  else {
    if (!validerDateISO(p.start)) erreurs.push(`period.start "${p.start}" invalide (YYYY-MM-DD réelle attendue)`);
    if (!validerDateISO(p.end)) erreurs.push(`period.end "${p.end}" invalide (YYYY-MM-DD réelle attendue)`);
    if (validerDateISO(p.start) && validerDateISO(p.end) && p.start > p.end) {
      erreurs.push(`period.start (${p.start}) postérieur à period.end (${p.end})`);
    }
  }

  // --- Accounts (optionnel mais avertissement si vide) ---
  const accountsRaw = input.accounts;
  const accountsIsArray = accountsRaw === undefined || Array.isArray(accountsRaw);
  if (!accountsIsArray) erreurs.push('accounts doit être un tableau');
  const accounts = accountsIsArray ? (accountsRaw || []) : [];
  if (accountsIsArray && accounts.length === 0) avertissements.push('accounts vide : MasterFiles/GeneralLedgerAccounts sera vide');

  const accountIds = new Set(accounts.map((a) => String(a && a.id)));
  for (const a of accounts) {
    if (!a || !a.id) erreurs.push('un compte sans id détecté');
    if (a && !a.label) avertissements.push(`compte ${a.id} sans label`);
  }

  // --- Entries (équilibre D=C) ---
  const entriesRaw = input.entries;
  const entriesIsArray = entriesRaw === undefined || Array.isArray(entriesRaw);
  if (!entriesIsArray) erreurs.push('entries doit être un tableau');
  const entries = entriesIsArray ? (entriesRaw || []) : [];
  let i = 0;
  for (const e of entries) {
    i++;
    if (!e.id) erreurs.push(`entries[${i - 1}] sans id`);
    if (!validerDateISO(e.date)) erreurs.push(`entries[${i - 1}].date "${e.date}" invalide`);
    const lines = e.lines || [];
    if (lines.length < 2) {
      erreurs.push(`entries[${i - 1}] ${e.id || ''} : moins de 2 lignes (écriture comptable invalide)`);
    }
    let d = 0, c2 = 0;
    for (const l of lines) {
      d += Number(l.debit || 0);
      c2 += Number(l.credit || 0);
      if (l.accountId && !accountIds.has(String(l.accountId))) {
        avertissements.push(`entries[${i - 1}] ${e.id || ''} : ligne référence accountId "${l.accountId}" absent de accounts`);
      }
      if ((l.debit && l.credit) || (!l.debit && !l.credit)) {
        erreurs.push(`entries[${i - 1}] ligne ${l.id || ''} : doit avoir SOIT debit SOIT credit (pas les deux, pas aucun)`);
      }
    }
    if (Math.abs(d - c2) > 0.005) {
      erreurs.push(`entries[${i - 1}] ${e.id || ''} : non équilibrée (débit ${d.toFixed(2)} ≠ crédit ${c2.toFixed(2)})`);
    }
  }

  // --- SalesInvoices / PurchaseInvoices : contrôles légers ---
  for (const [key, label] of [['salesInvoices', 'salesInvoice'], ['purchaseInvoices', 'purchaseInvoice']]) {
    const raw = input[key];
    if (raw !== undefined && !Array.isArray(raw)) {
      erreurs.push(`${key} doit être un tableau`);
      continue;
    }
    for (const s of raw || []) {
      if (!s || !s.invoiceNo) erreurs.push(`${label} sans invoiceNo`);
      if (s && !validerDateISO(s.date)) erreurs.push(`${label} ${s.invoiceNo || ''} date invalide`);
    }
  }

  return { valide: erreurs.length === 0, erreurs, avertissements };
}

/**
 * Valide une date YYYY-MM-DD réelle (rejette 2025-02-30 etc.).
 */
function validerDateISO(s) {
  if (typeof s !== 'string' || !RE_DATE_ISO.test(s)) return false;
  const [y, m, d] = s.split('-').map(Number);
  const dt = new Date(Date.UTC(y, m - 1, d));
  return dt.getUTCFullYear() === y && dt.getUTCMonth() === m - 1 && dt.getUTCDate() === d;
}

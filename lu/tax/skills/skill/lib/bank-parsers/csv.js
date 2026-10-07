/**
 * csv.js — Parseur CSV minimaliste sans dépendance.
 *
 * Gère :
 *   - séparateurs ; , \t (auto-détection)
 *   - guillemets doubles avec échappement ""
 *   - lignes vides ignorées
 *   - BOM UTF-8 retiré
 *
 * Limites : pas de retours-ligne dans une cellule.
 */

export function detectSeparator(firstLine) {
  const counts = { ';': 0, ',': 0, '\t': 0 };
  let inQuote = false;
  for (const c of firstLine) {
    if (c === '"') inQuote = !inQuote;
    else if (!inQuote && c in counts) counts[c]++;
  }
  return Object.entries(counts).sort((a, b) => b[1] - a[1])[0][0] || ',';
}

export function parseCSVLine(line, sep) {
  const out = [];
  let cur = '';
  let inQuote = false;
  for (let i = 0; i < line.length; i++) {
    const c = line[i];
    if (inQuote) {
      if (c === '"' && line[i + 1] === '"') { cur += '"'; i++; }
      else if (c === '"') inQuote = false;
      else cur += c;
    } else {
      if (c === '"') inQuote = true;
      else if (c === sep) { out.push(cur); cur = ''; }
      else cur += c;
    }
  }
  out.push(cur);
  return out;
}

export function parseCSV(text, { separator } = {}) {
  text = text.replace(/^\uFEFF/, ''); // strip BOM
  const lines = text.split(/\r?\n/).filter(l => l.trim().length > 0);
  if (lines.length === 0) return { header: [], rows: [], separator: ',' };
  const sep = separator || detectSeparator(lines[0]);
  const header = parseCSVLine(lines[0], sep).map(h => h.trim());
  const rows = lines.slice(1).map(l => parseCSVLine(l, sep));
  return { header, rows, separator: sep };
}

/**
 * Parse un montant FR/LU :
 *   "1.234,56"  → 1234.56
 *   "1,234.56"  → 1234.56
 *   "-1234,56"  → -1234.56
 *   "1234,56 €" → 1234.56
 */
export function parseAmount(raw) {
  if (raw == null) return null;
  let s = String(raw).trim().replace(/[€$£\s]/g, '');
  if (s === '' || s === '-') return null;
  // Format européen "1.234,56" : virgule = décimale
  const hasComma = s.includes(',');
  const hasDot = s.includes('.');
  if (hasComma && hasDot) {
    // Le dernier des deux est le séparateur décimal
    if (s.lastIndexOf(',') > s.lastIndexOf('.')) {
      s = s.replace(/\./g, '').replace(',', '.');
    } else {
      s = s.replace(/,/g, '');
    }
  } else if (hasComma) {
    s = s.replace(',', '.');
  }
  const n = Number(s);
  return Number.isFinite(n) ? n : null;
}

/**
 * Normalise une date : "12/03/2025", "12.03.2025", "2025-03-12", "12-Mar-2025"
 * → "2025-03-12" (ISO).
 */
export function parseDate(raw) {
  if (!raw) return null;
  const s = String(raw).trim();
  // ISO yyyy-mm-dd déjà
  if (/^\d{4}-\d{2}-\d{2}/.test(s)) return s.slice(0, 10);
  // dd/mm/yyyy ou dd.mm.yyyy ou dd-mm-yyyy
  const m = s.match(/^(\d{1,2})[\/.\-](\d{1,2})[\/.\-](\d{2,4})/);
  if (m) {
    const [, d, mo, y] = m;
    const yr = y.length === 2 ? '20' + y : y;
    return `${yr}-${mo.padStart(2, '0')}-${d.padStart(2, '0')}`;
  }
  return s;
}

/**
 * camt053.js — Parseur CAMT.053 (ISO 20022 Bank-to-Customer Statement).
 *
 * CAMT.053 est le format standard XML utilisé par toutes les banques européennes
 * pour les relevés de compte B2B. Le Luxembourg supporte ce format via SEPA.
 *
 * Spécification : ISO 20022 + Implementation Guidelines EBA / EPC
 *
 * Ce parseur extrait les transactions essentielles sans dépendance XML externe :
 * il fait du pattern-matching sur les balises CAMT bien définies. Suffit pour
 * 95 % des relevés bancaires luxembourgeois standard. Pour des cas exotiques
 * (multi-namespace complexe, transactions composées), envisager fast-xml-parser.
 *
 * Référence des balises ISO 20022 :
 *   <Ntry>          — Entry (transaction)
 *     <Amt Ccy="X">  — montant + devise
 *     <CdtDbtInd>    — CRDT (crédit) ou DBIT (débit)
 *     <BookgDt><Dt>  — date de comptabilisation (ISO yyyy-mm-dd)
 *     <ValDt><Dt>    — date de valeur
 *     <NtryRef>      — référence d'entrée
 *     <AddtlNtryInf> — libellé/description
 */

export const id = 'camt053';
export const labels = ['CAMT.053', 'ISO 20022', 'XML'];

function extractAll(xml, tag) {
  const re = new RegExp(`<${tag}\\b[^>]*>([\\s\\S]*?)</${tag}>`, 'g');
  const out = [];
  let m;
  while ((m = re.exec(xml)) !== null) out.push(m[1]);
  return out;
}

function extractFirst(xml, tag) {
  const re = new RegExp(`<${tag}\\b[^>]*>([\\s\\S]*?)</${tag}>`);
  const m = xml.match(re);
  return m ? m[1] : null;
}

function extractAttr(xml, tag, attr) {
  const re = new RegExp(`<${tag}\\b([^>]*)>`);
  const m = xml.match(re);
  if (!m) return null;
  const a = m[1].match(new RegExp(`${attr}="([^"]*)"`));
  return a ? a[1] : null;
}

export function isCAMT053(text) {
  return /<Document\b/.test(text) && /<BkToCstmrStmt\b/.test(text);
}

export function parse(xmlText) {
  const entries = extractAll(xmlText, 'Ntry');
  return entries.map(ntry => {
    const amtRaw = extractFirst(ntry, 'Amt');
    const devise = extractAttr(ntry, 'Amt', 'Ccy') || 'EUR';
    const sens = extractFirst(ntry, 'CdtDbtInd'); // CRDT|DBIT
    const bookgDt = extractFirst(extractFirst(ntry, 'BookgDt') || '', 'Dt');
    const valDt = extractFirst(extractFirst(ntry, 'ValDt') || '', 'Dt');
    const ref = extractFirst(ntry, 'NtryRef') || extractFirst(ntry, 'AcctSvcrRef');
    const addtl = extractFirst(ntry, 'AddtlNtryInf') || '';
    // Tenter d'extraire le libellé depuis NtryDtls > TxDtls > RmtInf > Ustrd si AddtlNtryInf est vide
    const ustrd = extractFirst(ntry, 'Ustrd');
    const libelle = (addtl || ustrd || '').replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ').trim();

    const montantBrut = amtRaw ? parseFloat(amtRaw) : null;
    const montant = montantBrut != null
      ? Math.round((sens === 'DBIT' ? -montantBrut : montantBrut) * 100) / 100
      : null;

    return {
      date: bookgDt,
      date_valeur: valDt,
      libelle,
      montant,
      sens: sens === 'DBIT' ? 'debit' : 'credit',
      devise,
      solde: null,
      reference: ref,
      banque: 'CAMT.053',
    };
  });
}

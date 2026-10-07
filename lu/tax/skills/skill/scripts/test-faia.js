#!/usr/bin/env node
/**
 * test-faia.js — Tests du module FAIA.
 */

import { genererFAIA, validerFAIAInput, TAX_CODES_LU } from '../lib/faia/index.js';

let passed = 0, failed = 0;
function test(name, fn) {
  try { fn(); console.log(`  ✓ ${name}`); passed++; }
  catch (e) { console.log(`  ✗ ${name}\n      ${e.message}`); failed++; }
}
function eq(a, b, msg) { if (a !== b) throw new Error(`${msg||''}: attendu ${JSON.stringify(b)}, reçu ${JSON.stringify(a)}`); }
function truthy(v, msg) { if (!v) throw new Error(msg || 'attendu truthy'); }
function falsy(v, msg) { if (v) throw new Error(msg || 'attendu falsy'); }
function contains(haystack, needle, msg) {
  if (!String(haystack).includes(needle)) throw new Error(`${msg||''}: "${needle}" introuvable`);
}

const baseCompany = {
  rcs: 'B12345',
  matriculeTVA: 'LU12345678',
  raisonSociale: 'ACME S.à r.l.',
  siegeSocial: { rue: '1 rue du Test', ville: 'Luxembourg', codePostal: 'L-1234' },
};

const baseInput = {
  company: baseCompany,
  period: { start: '2025-01-01', end: '2025-12-31', fiscalYear: '2025' },
  accounts: [
    { id: '601', label: 'Achats marchandises', closingDebit: 1000, closingCredit: 0 },
    { id: '707', label: 'Ventes marchandises', closingDebit: 0, closingCredit: 2000 },
  ],
  entries: [
    {
      id: 'TX001', date: '2025-03-15', journalId: 'VEN', description: 'Vente test',
      lines: [
        { id: 'L1', accountId: '411', debit: 1170, description: 'Client X' },
        { id: 'L2', accountId: '707', credit: 1000, description: 'Vente HT' },
        { id: 'L3', accountId: '4457', credit: 170, description: 'TVA 17%', taxCode: 'STD' },
      ],
    },
  ],
};

console.log('=== Tests validation ===');

test('input valide passe', () => {
  const v = validerFAIAInput(baseInput);
  truthy(v.valide, JSON.stringify(v.erreurs));
  eq(v.erreurs.length, 0);
});

test('company manquant détecté', () => {
  const v = validerFAIAInput({ ...baseInput, company: undefined });
  falsy(v.valide);
  contains(v.erreurs.join(' '), 'company manquant');
});

test('RCS invalide rejeté', () => {
  const v = validerFAIAInput({ ...baseInput, company: { ...baseCompany, rcs: 'Z9999' } });
  falsy(v.valide);
  contains(v.erreurs.join(' '), 'rcs');
});

test('matricule TVA sans LU rejeté', () => {
  const v = validerFAIAInput({ ...baseInput, company: { ...baseCompany, matriculeTVA: '12345678' } });
  falsy(v.valide);
});

test('matricule TVA LU avec espaces accepté', () => {
  const v = validerFAIAInput({ ...baseInput, company: { ...baseCompany, matriculeTVA: 'LU 12345678' } });
  truthy(v.valide, JSON.stringify(v.erreurs));
});

test('siège social incomplet rejeté', () => {
  const v = validerFAIAInput({ ...baseInput, company: { ...baseCompany, siegeSocial: { rue: 'X', ville: 'Y' } } });
  falsy(v.valide);
});

test('date invalide 2025-02-30 rejetée', () => {
  const v = validerFAIAInput({ ...baseInput, period: { start: '2025-02-30', end: '2025-12-31' } });
  falsy(v.valide);
});

test('période inversée rejetée', () => {
  const v = validerFAIAInput({ ...baseInput, period: { start: '2025-12-31', end: '2025-01-01' } });
  falsy(v.valide);
});

test('écriture déséquilibrée détectée', () => {
  const bad = {
    ...baseInput,
    entries: [{
      id: 'X', date: '2025-03-15',
      lines: [
        { id: 'L1', accountId: '411', debit: 100 },
        { id: 'L2', accountId: '707', credit: 50 },
      ],
    }],
  };
  const v = validerFAIAInput(bad);
  falsy(v.valide);
  contains(v.erreurs.join(' '), 'non équilibrée');
});

test('ligne avec debit ET credit rejetée', () => {
  const bad = {
    ...baseInput,
    entries: [{
      id: 'X', date: '2025-03-15',
      lines: [
        { id: 'L1', accountId: '411', debit: 100, credit: 100 },
        { id: 'L2', accountId: '707', credit: 100 },
      ],
    }],
  };
  const v = validerFAIAInput(bad);
  falsy(v.valide);
});

test('écriture à 1 ligne rejetée', () => {
  const bad = { ...baseInput, entries: [{ id: 'X', date: '2025-03-15', lines: [{ id: 'L1', accountId: '411', debit: 100 }] }] };
  const v = validerFAIAInput(bad);
  falsy(v.valide);
});

test('accounts non-array rejeté sans crash', () => {
  const v = validerFAIAInput({ ...baseInput, accounts: 'pas un tableau' });
  falsy(v.valide);
  contains(v.erreurs.join(' '), 'accounts');
});

test('entries non-array rejeté sans crash', () => {
  const v = validerFAIAInput({ ...baseInput, entries: { foo: 'bar' } });
  falsy(v.valide);
  contains(v.erreurs.join(' '), 'entries');
});

test('salesInvoices non-array rejeté sans crash', () => {
  const v = validerFAIAInput({ ...baseInput, salesInvoices: 42 });
  falsy(v.valide);
  contains(v.erreurs.join(' '), 'salesInvoices');
});

test('avertissement si accountId orphelin', () => {
  const odd = {
    ...baseInput,
    entries: [{
      id: 'TX', date: '2025-03-15',
      lines: [
        { id: 'L1', accountId: '999999', debit: 100 },
        { id: 'L2', accountId: '707', credit: 100 },
      ],
    }],
  };
  const v = validerFAIAInput(odd);
  truthy(v.valide);
  contains(v.avertissements.join(' '), '999999');
});

console.log('\n=== Tests génération XML ===');

test('genererFAIA produit du XML SAF-T LU 2.01', () => {
  const { xml } = genererFAIA(baseInput);
  contains(xml, '<?xml version="1.0" encoding="UTF-8"?>');
  contains(xml, 'urn:OECD:StandardAuditFile-Tax:LU_2.01');
  contains(xml, '<AuditFileVersion>2.01</AuditFileVersion>');
  contains(xml, '<AuditFileCountry>LU</AuditFileCountry>');
});

test('Header contient identifiants entreprise', () => {
  const { xml } = genererFAIA(baseInput);
  contains(xml, '<RegistrationNumber>B12345</RegistrationNumber>');
  contains(xml, '<TaxRegistrationNumber>LU12345678</TaxRegistrationNumber>');
  contains(xml, '<TaxAuthority>AED</TaxAuthority>');
  contains(xml, '<Name>ACME S.à r.l.</Name>');
});

test('FiscalYear inclus si fourni', () => {
  const { xml } = genererFAIA(baseInput);
  contains(xml, '<FiscalYear>2025</FiscalYear>');
});

test('TaxTable contient les 6 codes LU', () => {
  const { xml } = genererFAIA(baseInput);
  for (const tc of TAX_CODES_LU) contains(xml, `<TaxCode>${tc.code}</TaxCode>`);
  contains(xml, '<TaxPercentage>17.00</TaxPercentage>');
  contains(xml, '<TaxPercentage>3.00</TaxPercentage>');
});

test('GeneralLedgerEntries totaux corrects', () => {
  const { xml, totals } = genererFAIA(baseInput);
  eq(totals.debit, 1170);
  eq(totals.credit, 1170);
  eq(totals.entryCount, 1);
  contains(xml, '<NumberOfEntries>1</NumberOfEntries>');
  contains(xml, '<TotalDebit>1170.00</TotalDebit>');
  contains(xml, '<TotalCredit>1170.00</TotalCredit>');
});

test('DebitLine et CreditLine bien tagués', () => {
  const { xml } = genererFAIA(baseInput);
  contains(xml, '<DebitLine>');
  contains(xml, '<DebitAmount>1170.00</DebitAmount>');
  contains(xml, '<CreditLine>');
  contains(xml, '<CreditAmount>1000.00</CreditAmount>');
});

test('TaxCode propagé dans les lignes', () => {
  const { xml } = genererFAIA(baseInput);
  contains(xml, '<TaxCode>STD</TaxCode>');
});

test('SourceDocuments inclus si SalesInvoices fournies', () => {
  const withInvoices = {
    ...baseInput,
    salesInvoices: [
      { invoiceNo: 'F2025-001', date: '2025-03-15', customerId: 'C001', totalHT: 1000, tva: 170, totalTTC: 1170 },
    ],
  };
  const { xml, totals } = genererFAIA(withInvoices);
  eq(totals.salesCount, 1);
  contains(xml, '<SourceDocuments>');
  contains(xml, '<InvoiceNo>F2025-001</InvoiceNo>');
  contains(xml, '<GrossTotal>1170.00</GrossTotal>');
});

test('SourceDocuments omis si rien à reporter', () => {
  const { xml } = genererFAIA(baseInput);
  if (xml.includes('<SourceDocuments>')) throw new Error('SourceDocuments présent à tort');
});

test('Échappement XML des 5 entités', () => {
  const dangerous = {
    ...baseInput,
    company: {
      ...baseCompany,
      raisonSociale: `Tom & Jerry's <"Café">`,
    },
  };
  const { xml } = genererFAIA(dangerous);
  contains(xml, '&amp;');
  contains(xml, '&apos;');
  contains(xml, '&lt;');
  contains(xml, '&gt;');
  contains(xml, '&quot;');
});

test('genererFAIA throw si validation KO', () => {
  let threw = false;
  try { genererFAIA({ ...baseInput, company: undefined }); }
  catch (e) { threw = true; truthy(e.validation); }
  truthy(threw, 'devrait throw');
});

test('skipValidation permet de forcer la génération', () => {
  const { xml } = genererFAIA({ ...baseInput, company: baseCompany, period: baseInput.period, accounts: [], entries: [] }, { skipValidation: true });
  contains(xml, '<AuditFile');
});

console.log(`\n${passed} passé(s), ${failed} échec(s)`);
process.exit(failed === 0 ? 0 : 1);

/**
 * lib/faia/xml — Constructeurs XML par section pour le FAIA SAF-T LU 2.01.
 *
 * Pas de dépendance externe. L'échappement couvre les 5 entités XML
 * réservées (& < > " ').
 */

import { TAX_CODES_LU } from './validation.js';

/** Échappe les 5 entités XML. */
export function esc(s) {
  return String(s ?? '')
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&apos;');
}

const f2 = (n) => Number(n || 0).toFixed(2);

export function buildHeader(input, opts, headerDate) {
  const { company, period } = input;
  return `  <Header>
    <AuditFileVersion>2.01</AuditFileVersion>
    <AuditFileCountry>LU</AuditFileCountry>
    <AuditFileDateCreated>${headerDate}</AuditFileDateCreated>
    <SoftwareCompanyName>${esc(opts.softwareName)}</SoftwareCompanyName>
    <SoftwareID>${esc(opts.softwareId)}</SoftwareID>
    <SoftwareVersion>${esc(opts.softwareVersion)}</SoftwareVersion>
    <Company>
      <RegistrationNumber>${esc(company.rcs)}</RegistrationNumber>
      <Name>${esc(company.raisonSociale)}</Name>
      <Address>
        <StreetName>${esc(company.siegeSocial.rue)}</StreetName>
        <City>${esc(company.siegeSocial.ville)}</City>
        <PostalCode>${esc(company.siegeSocial.codePostal)}</PostalCode>
        <Country>${esc(company.siegeSocial.pays || 'LU')}</Country>
      </Address>
      <TaxRegistration>
        <TaxRegistrationNumber>${esc(company.matriculeTVA)}</TaxRegistrationNumber>
        <TaxAuthority>AED</TaxAuthority>
        <TaxType>VAT</TaxType>
      </TaxRegistration>
    </Company>
    <DefaultCurrencyCode>${esc(input.currency || 'EUR')}</DefaultCurrencyCode>
    <SelectionCriteria>
      <PeriodStart>${esc(period.start)}</PeriodStart>
      <PeriodEnd>${esc(period.end)}</PeriodEnd>
${period.fiscalYear ? `      <FiscalYear>${esc(period.fiscalYear)}</FiscalYear>\n` : ''}    </SelectionCriteria>
    <TaxAccountingBasis>${esc(input.taxAccountingBasis || 'A')}</TaxAccountingBasis>
  </Header>`;
}

export function buildMasterFiles(input) {
  const accounts = input.accounts || [];
  const customers = input.customers || [];
  const suppliers = input.suppliers || [];
  const taxTable = input.taxTable || TAX_CODES_LU;

  return `  <MasterFiles>
    <GeneralLedgerAccounts>
${accounts.map((a) => `      <Account>
        <AccountID>${esc(a.id)}</AccountID>
        <AccountDescription>${esc(a.label)}</AccountDescription>
        <OpeningDebitBalance>${f2(a.openingDebit)}</OpeningDebitBalance>
        <OpeningCreditBalance>${f2(a.openingCredit)}</OpeningCreditBalance>
        <ClosingDebitBalance>${f2(a.closingDebit)}</ClosingDebitBalance>
        <ClosingCreditBalance>${f2(a.closingCredit)}</ClosingCreditBalance>
      </Account>`).join('\n')}
    </GeneralLedgerAccounts>
    <Customers>
${customers.map((c) => `      <Customer>
        <CustomerID>${esc(c.id)}</CustomerID>
        <AccountID>${esc(c.accountId || '401')}</AccountID>
        <CustomerTaxID>${esc(c.tva || '')}</CustomerTaxID>
        <CompanyName>${esc(c.name)}</CompanyName>
${c.country ? `        <Country>${esc(c.country)}</Country>\n` : ''}      </Customer>`).join('\n')}
    </Customers>
    <Suppliers>
${suppliers.map((s) => `      <Supplier>
        <SupplierID>${esc(s.id)}</SupplierID>
        <AccountID>${esc(s.accountId || '451')}</AccountID>
        <SupplierTaxID>${esc(s.tva || '')}</SupplierTaxID>
        <CompanyName>${esc(s.name)}</CompanyName>
${s.country ? `        <Country>${esc(s.country)}</Country>\n` : ''}      </Supplier>`).join('\n')}
    </Suppliers>
    <TaxTable>
${taxTable.map((t) => `      <TaxTableEntry>
        <TaxCode>${esc(t.code)}</TaxCode>
        <TaxType>VAT</TaxType>
        <Description>${esc(t.libelle)}</Description>
        <TaxPercentage>${Number(t.taux).toFixed(2)}</TaxPercentage>
      </TaxTableEntry>`).join('\n')}
    </TaxTable>
  </MasterFiles>`;
}

export function buildGeneralLedgerEntries(entries, totals) {
  return `  <GeneralLedgerEntries>
    <NumberOfEntries>${totals.entryCount}</NumberOfEntries>
    <TotalDebit>${f2(totals.debit)}</TotalDebit>
    <TotalCredit>${f2(totals.credit)}</TotalCredit>
${entries.map((e) => `    <Journal>
      <JournalID>${esc(e.journalId || 'GEN')}</JournalID>
      <Description>${esc(e.description || '')}</Description>
      <Transaction>
        <TransactionID>${esc(e.id)}</TransactionID>
        <Period>${esc(e.period || (e.date ? e.date.slice(0, 7) : ''))}</Period>
        <TransactionDate>${esc(e.date)}</TransactionDate>
        <Lines>
${(e.lines || []).map((l) => {
  const isDebit = Number(l.debit || 0) > 0;
  const tag = isDebit ? 'DebitLine' : 'CreditLine';
  const amtTag = isDebit ? 'DebitAmount' : 'CreditAmount';
  const amt = f2(isDebit ? l.debit : l.credit);
  const taxBlock = l.taxCode
    ? `\n            <Tax><TaxCode>${esc(l.taxCode)}</TaxCode><TaxType>VAT</TaxType></Tax>`
    : '';
  return `          <${tag}>
            <RecordID>${esc(l.id)}</RecordID>
            <AccountID>${esc(l.accountId)}</AccountID>
            <Description>${esc(l.description || '')}</Description>
            <${amtTag}>${amt}</${amtTag}>${taxBlock}
          </${tag}>`;
}).join('\n')}
        </Lines>
      </Transaction>
    </Journal>`).join('\n')}
  </GeneralLedgerEntries>`;
}

export function buildSourceDocuments(salesInvoices, purchaseInvoices, payments) {
  if (!salesInvoices.length && !purchaseInvoices.length && !payments.length) return null;

  const totalSales = salesInvoices.reduce((acc, s) => acc + Number(s.totalTTC || 0), 0);
  const totalPurchases = purchaseInvoices.reduce((acc, p) => acc + Number(p.totalTTC || 0), 0);

  return `  <SourceDocuments>
${salesInvoices.length ? `    <SalesInvoices>
      <NumberOfEntries>${salesInvoices.length}</NumberOfEntries>
      <TotalDebit>${f2(totalSales)}</TotalDebit>
      <TotalCredit>0.00</TotalCredit>
${salesInvoices.map((s) => `      <Invoice>
        <InvoiceNo>${esc(s.invoiceNo)}</InvoiceNo>
        <InvoiceDate>${esc(s.date)}</InvoiceDate>
        <CustomerID>${esc(s.customerId || '')}</CustomerID>
        <DocumentTotals>
          <TaxPayable>${f2(s.tva)}</TaxPayable>
          <NetTotal>${f2(s.totalHT)}</NetTotal>
          <GrossTotal>${f2(s.totalTTC)}</GrossTotal>
        </DocumentTotals>
      </Invoice>`).join('\n')}
    </SalesInvoices>` : ''}
${purchaseInvoices.length ? `    <PurchaseInvoices>
      <NumberOfEntries>${purchaseInvoices.length}</NumberOfEntries>
      <TotalDebit>0.00</TotalDebit>
      <TotalCredit>${f2(totalPurchases)}</TotalCredit>
${purchaseInvoices.map((p) => `      <Invoice>
        <InvoiceNo>${esc(p.invoiceNo)}</InvoiceNo>
        <InvoiceDate>${esc(p.date)}</InvoiceDate>
        <SupplierID>${esc(p.supplierId || '')}</SupplierID>
        <DocumentTotals>
          <TaxPayable>${f2(p.tva)}</TaxPayable>
          <NetTotal>${f2(p.totalHT)}</NetTotal>
          <GrossTotal>${f2(p.totalTTC)}</GrossTotal>
        </DocumentTotals>
      </Invoice>`).join('\n')}
    </PurchaseInvoices>` : ''}
${payments.length ? `    <Payments>
      <NumberOfEntries>${payments.length}</NumberOfEntries>
${payments.map((pm) => `      <Payment>
        <PaymentRefNo>${esc(pm.ref)}</PaymentRefNo>
        <TransactionDate>${esc(pm.date)}</TransactionDate>
        <PaymentMethod><PaymentMechanism>${esc(pm.method || 'TRA')}</PaymentMechanism><PaymentAmount>${f2(pm.amount)}</PaymentAmount></PaymentMethod>
      </Payment>`).join('\n')}
    </Payments>` : ''}
  </SourceDocuments>`;
}

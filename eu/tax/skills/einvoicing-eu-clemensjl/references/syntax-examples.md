# Worked minimal invoice in both syntaxes

Same business fact in both permitted syntaxes: one seller in Austria, one buyer in Germany, two units at 100.00 EUR, 20 % standard-rated VAT, total 240.00 EUR. Element names and cardinalities are taken from docs.peppol.eu/poacc/billing/3.0/syntax/ubl-invoice/tree/ (UBL) and from the CEN reference example `cii/examples/CII_business_example_01.xml` in github.com/ConnectingEurope/eInvoicing-EN16931 (CII).

**Element order is part of the schema in both syntaxes.** UBL 2.1 and CII D16B are sequence-constrained; moving `cac:PaymentMeans` after `cac:TaxTotal` is a schema error, not a style question. Generate from a template or a serialiser that preserves order — never by string concatenation in arbitrary order.

Replace every `[[…]]` before use, then validate. These examples are constructed to satisfy BR-01…BR-16, BR-CO-10…BR-CO-17, BR-CO-25 and BR-CO-26; they are still not "known good" until a validator says so (`implementation.md`).

## UBL 2.1 — `ubl:Invoice`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- ENTWURF – steuerlich nicht freigegeben -->
<Invoice xmlns="urn:oasis:names:specification:ubl:schema:xsd:Invoice-2"
         xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"
         xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:CustomizationID>urn:cen.eu:en16931:2017</cbc:CustomizationID>
  <cbc:ID>2026-000417</cbc:ID>
  <cbc:IssueDate>2026-08-05</cbc:IssueDate>
  <cbc:DueDate>2026-09-04</cbc:DueDate>
  <cbc:InvoiceTypeCode>380</cbc:InvoiceTypeCode>
  <cbc:DocumentCurrencyCode>EUR</cbc:DocumentCurrencyCode>
  <cbc:BuyerReference>[[BT-10 buyer routing reference]]</cbc:BuyerReference>

  <cac:AccountingSupplierParty>
    <cac:Party>
      <cbc:EndpointID schemeID="9914">[[ATU12345678]]</cbc:EndpointID>
      <cac:PostalAddress>
        <cbc:StreetName>[[street and number]]</cbc:StreetName>
        <cbc:CityName>[[city]]</cbc:CityName>
        <cbc:PostalZone>[[postcode]]</cbc:PostalZone>
        <cac:Country><cbc:IdentificationCode>AT</cbc:IdentificationCode></cac:Country>
      </cac:PostalAddress>
      <cac:PartyTaxScheme>
        <cbc:CompanyID>[[ATU12345678]]</cbc:CompanyID>
        <cac:TaxScheme><cbc:ID>VAT</cbc:ID></cac:TaxScheme>
      </cac:PartyTaxScheme>
      <cac:PartyLegalEntity>
        <cbc:RegistrationName>[[seller legal name]]</cbc:RegistrationName>
        <cbc:CompanyID>[[FN 123456a]]</cbc:CompanyID>
      </cac:PartyLegalEntity>
    </cac:Party>
  </cac:AccountingSupplierParty>

  <cac:AccountingCustomerParty>
    <cac:Party>
      <cbc:EndpointID schemeID="9930">[[DE123456789]]</cbc:EndpointID>
      <cac:PostalAddress>
        <cbc:StreetName>[[street and number]]</cbc:StreetName>
        <cbc:CityName>[[city]]</cbc:CityName>
        <cbc:PostalZone>[[postcode]]</cbc:PostalZone>
        <cac:Country><cbc:IdentificationCode>DE</cbc:IdentificationCode></cac:Country>
      </cac:PostalAddress>
      <cac:PartyTaxScheme>
        <cbc:CompanyID>[[DE123456789]]</cbc:CompanyID>
        <cac:TaxScheme><cbc:ID>VAT</cbc:ID></cac:TaxScheme>
      </cac:PartyTaxScheme>
      <cac:PartyLegalEntity>
        <cbc:RegistrationName>[[buyer legal name]]</cbc:RegistrationName>
      </cac:PartyLegalEntity>
    </cac:Party>
  </cac:AccountingCustomerParty>

  <cac:PaymentMeans>
    <cbc:PaymentMeansCode>30</cbc:PaymentMeansCode>
    <cbc:PaymentID>2026-000417</cbc:PaymentID>
    <cac:PayeeFinancialAccount><cbc:ID>[[IBAN]]</cbc:ID></cac:PayeeFinancialAccount>
  </cac:PaymentMeans>

  <cac:PaymentTerms><cbc:Note>Net 30 days</cbc:Note></cac:PaymentTerms>

  <cac:TaxTotal>
    <cbc:TaxAmount currencyID="EUR">40.00</cbc:TaxAmount>
    <cac:TaxSubtotal>
      <cbc:TaxableAmount currencyID="EUR">200.00</cbc:TaxableAmount>
      <cbc:TaxAmount currencyID="EUR">40.00</cbc:TaxAmount>
      <cac:TaxCategory>
        <cbc:ID>S</cbc:ID>
        <cbc:Percent>20</cbc:Percent>
        <cac:TaxScheme><cbc:ID>VAT</cbc:ID></cac:TaxScheme>
      </cac:TaxCategory>
    </cac:TaxSubtotal>
  </cac:TaxTotal>

  <cac:LegalMonetaryTotal>
    <cbc:LineExtensionAmount currencyID="EUR">200.00</cbc:LineExtensionAmount>
    <cbc:TaxExclusiveAmount currencyID="EUR">200.00</cbc:TaxExclusiveAmount>
    <cbc:TaxInclusiveAmount currencyID="EUR">240.00</cbc:TaxInclusiveAmount>
    <cbc:PayableAmount currencyID="EUR">240.00</cbc:PayableAmount>
  </cac:LegalMonetaryTotal>

  <cac:InvoiceLine>
    <cbc:ID>1</cbc:ID>
    <cbc:InvoicedQuantity unitCode="C62">2</cbc:InvoicedQuantity>
    <cbc:LineExtensionAmount currencyID="EUR">200.00</cbc:LineExtensionAmount>
    <cac:Item>
      <cbc:Name>[[item name]]</cbc:Name>
      <cac:ClassifiedTaxCategory>
        <cbc:ID>S</cbc:ID>
        <cbc:Percent>20</cbc:Percent>
        <cac:TaxScheme><cbc:ID>VAT</cbc:ID></cac:TaxScheme>
      </cac:ClassifiedTaxCategory>
    </cac:Item>
    <cac:Price><cbc:PriceAmount currencyID="EUR">100.00</cbc:PriceAmount></cac:Price>
  </cac:InvoiceLine>
</Invoice>
```

For **Peppol BIS Billing 3.0**, three changes: `cbc:CustomizationID` becomes `urn:cen.eu:en16931:2017#compliant#urn:fdc:peppol.eu:2017:poacc:billing:3.0`, a `cbc:ProfileID` of `urn:fdc:peppol.eu:2017:poacc:billing:01:1.0` is inserted immediately after it, and `cbc:EndpointID` on both parties is mandatory with a valid EAS `schemeID` (`identifiers.md`).

For a **credit note**, the root element is `CreditNote` in namespace `urn:oasis:names:specification:ubl:schema:xsd:CreditNote-2`, `cbc:InvoiceTypeCode` becomes `cbc:CreditNoteTypeCode` with value `381`, and `cac:InvoiceLine` becomes `cac:CreditNoteLine` with `cbc:CreditedQuantity`.

## UN/CEFACT CII D16B — `rsm:CrossIndustryInvoice`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- ENTWURF – steuerlich nicht freigegeben -->
<rsm:CrossIndustryInvoice
    xmlns:rsm="urn:un:unece:uncefact:data:standard:CrossIndustryInvoice:100"
    xmlns:ram="urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
    xmlns:udt="urn:un:unece:uncefact:data:standard:UnqualifiedDataType:100">
  <rsm:ExchangedDocumentContext>
    <ram:GuidelineSpecifiedDocumentContextParameter>
      <ram:ID>urn:cen.eu:en16931:2017</ram:ID>
    </ram:GuidelineSpecifiedDocumentContextParameter>
  </rsm:ExchangedDocumentContext>

  <rsm:ExchangedDocument>
    <ram:ID>2026-000417</ram:ID>
    <ram:TypeCode>380</ram:TypeCode>
    <ram:IssueDateTime>
      <udt:DateTimeString format="102">20260805</udt:DateTimeString>
    </ram:IssueDateTime>
  </rsm:ExchangedDocument>

  <rsm:SupplyChainTradeTransaction>
    <ram:IncludedSupplyChainTradeLineItem>
      <ram:AssociatedDocumentLineDocument><ram:LineID>1</ram:LineID></ram:AssociatedDocumentLineDocument>
      <ram:SpecifiedTradeProduct><ram:Name>[[item name]]</ram:Name></ram:SpecifiedTradeProduct>
      <ram:SpecifiedLineTradeAgreement>
        <ram:NetPriceProductTradePrice><ram:ChargeAmount>100.00</ram:ChargeAmount></ram:NetPriceProductTradePrice>
      </ram:SpecifiedLineTradeAgreement>
      <ram:SpecifiedLineTradeDelivery>
        <ram:BilledQuantity unitCode="C62">2</ram:BilledQuantity>
      </ram:SpecifiedLineTradeDelivery>
      <ram:SpecifiedLineTradeSettlement>
        <ram:ApplicableTradeTax>
          <ram:TypeCode>VAT</ram:TypeCode>
          <ram:CategoryCode>S</ram:CategoryCode>
          <ram:RateApplicablePercent>20</ram:RateApplicablePercent>
        </ram:ApplicableTradeTax>
        <ram:SpecifiedTradeSettlementLineMonetarySummation>
          <ram:LineTotalAmount>200.00</ram:LineTotalAmount>
        </ram:SpecifiedTradeSettlementLineMonetarySummation>
      </ram:SpecifiedLineTradeSettlement>
    </ram:IncludedSupplyChainTradeLineItem>

    <ram:ApplicableHeaderTradeAgreement>
      <ram:BuyerReference>[[BT-10 buyer routing reference]]</ram:BuyerReference>
      <ram:SellerTradeParty>
        <ram:Name>[[seller legal name]]</ram:Name>
        <ram:SpecifiedLegalOrganization><ram:ID>[[FN 123456a]]</ram:ID></ram:SpecifiedLegalOrganization>
        <ram:PostalTradeAddress>
          <ram:PostcodeCode>[[postcode]]</ram:PostcodeCode>
          <ram:LineOne>[[street and number]]</ram:LineOne>
          <ram:CityName>[[city]]</ram:CityName>
          <ram:CountryID>AT</ram:CountryID>
        </ram:PostalTradeAddress>
        <ram:SpecifiedTaxRegistration>
          <ram:ID schemeID="VA">[[ATU12345678]]</ram:ID>
        </ram:SpecifiedTaxRegistration>
      </ram:SellerTradeParty>
      <ram:BuyerTradeParty>
        <ram:Name>[[buyer legal name]]</ram:Name>
        <ram:PostalTradeAddress>
          <ram:PostcodeCode>[[postcode]]</ram:PostcodeCode>
          <ram:LineOne>[[street and number]]</ram:LineOne>
          <ram:CityName>[[city]]</ram:CityName>
          <ram:CountryID>DE</ram:CountryID>
        </ram:PostalTradeAddress>
        <ram:SpecifiedTaxRegistration>
          <ram:ID schemeID="VA">[[DE123456789]]</ram:ID>
        </ram:SpecifiedTaxRegistration>
      </ram:BuyerTradeParty>
    </ram:ApplicableHeaderTradeAgreement>

    <ram:ApplicableHeaderTradeDelivery/>

    <ram:ApplicableHeaderTradeSettlement>
      <ram:InvoiceCurrencyCode>EUR</ram:InvoiceCurrencyCode>
      <ram:SpecifiedTradeSettlementPaymentMeans>
        <ram:TypeCode>30</ram:TypeCode>
        <ram:PayeePartyCreditorFinancialAccount><ram:IBANID>[[IBAN]]</ram:IBANID></ram:PayeePartyCreditorFinancialAccount>
      </ram:SpecifiedTradeSettlementPaymentMeans>
      <ram:ApplicableTradeTax>
        <ram:CalculatedAmount>40.00</ram:CalculatedAmount>
        <ram:TypeCode>VAT</ram:TypeCode>
        <ram:BasisAmount>200.00</ram:BasisAmount>
        <ram:CategoryCode>S</ram:CategoryCode>
        <ram:RateApplicablePercent>20</ram:RateApplicablePercent>
      </ram:ApplicableTradeTax>
      <ram:SpecifiedTradePaymentTerms>
        <ram:Description>Net 30 days</ram:Description>
        <ram:DueDateDateTime><udt:DateTimeString format="102">20260904</udt:DateTimeString></ram:DueDateDateTime>
      </ram:SpecifiedTradePaymentTerms>
      <ram:SpecifiedTradeSettlementHeaderMonetarySummation>
        <ram:LineTotalAmount>200.00</ram:LineTotalAmount>
        <ram:TaxBasisTotalAmount>200.00</ram:TaxBasisTotalAmount>
        <ram:TaxTotalAmount currencyID="EUR">40.00</ram:TaxTotalAmount>
        <ram:GrandTotalAmount>240.00</ram:GrandTotalAmount>
        <ram:DuePayableAmount>240.00</ram:DuePayableAmount>
      </ram:SpecifiedTradeSettlementHeaderMonetarySummation>
    </ram:ApplicableHeaderTradeSettlement>
  </rsm:SupplyChainTradeTransaction>
</rsm:CrossIndustryInvoice>
```

CII notes that catch people out:

- Dates are `udt:DateTimeString` with `format="102"` and value `YYYYMMDD` — not ISO `YYYY-MM-DD`.
- `ram:TaxTotalAmount` carries `currencyID`; the other monetary summation elements do not.
- `ram:ApplicableHeaderTradeDelivery` is mandatory as a container even when empty.
- A credit note in CII is not a different root element: it is `ram:TypeCode` = `381` inside the same `rsm:CrossIndustryInvoice`. This is the biggest structural difference from UBL.
- CII carries the VAT identifier in `ram:SpecifiedTaxRegistration/ram:ID` with `schemeID="VA"`; the company registration number goes in `ram:SpecifiedLegalOrganization/ram:ID`.

## Which syntax to pick

| Situation | Syntax |
|---|---|
| Peppol network, any country | UBL 2.1 in practice — Peppol BIS Billing 3.0 defines both, UBL dominates |
| Germany XRechnung | Either; UBL is the more common implementation, CII is fully supported |
| Factur-X / ZUGFeRD hybrid PDF | CII only — the embedded XML is CII D16B |
| France PDP flows | Factur-X (CII), UBL and CII all accepted as the *socle* formats |
| Italy SdI | Neither — FatturaPA is a national XML, not an EN 16931 syntax |
| You have no constraint | UBL. More tooling, more examples, more validators |

Do not build both unless a channel forces it. Build the semantic model once and serialise; the BT-/BG- numbers are the stable interface between your domain model and either syntax.

## Checkpoints

- [ ] Element order matches the schema sequence, verified by XSD validation
- [ ] `[[…]]` placeholders all resolved
- [ ] CustomizationID matches the target specification exactly
- [ ] CII dates use `format="102"` and `YYYYMMDD`
- [ ] `currencyID` present on every UBL amount and on CII `ram:TaxTotalAmount`
- [ ] Credit note modelled per syntax: separate root in UBL, type code 381 in CII
- [ ] Validated against EN 16931 Schematron and the target CIUS Schematron before shipping

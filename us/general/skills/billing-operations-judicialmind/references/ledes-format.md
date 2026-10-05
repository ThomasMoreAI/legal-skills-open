# LEDES Billing Format Specifications

## Overview

LEDES (Legal Electronic Data Exchange Standard) is the standardized format for electronic legal billing accepted by major corporations and insurance companies worldwide.

## LEDES 1998B Format

The most widely adopted format, using pipe-delimited flat files.

### File Structure

```
LEDES1998B[]
INVOICE_DATE|INVOICE_NUMBER|CLIENT_ID|LAW_FIRM_MATTER_ID|INVOICE_TOTAL|...[]
20240115|INV-2024-001|CLIENT001|MATTER-12345|15750.00|...[]
```

### Required Header Fields

| Field Position | Field Name | Max Length | Description |
|----------------|------------|------------|-------------|
| 1 | INVOICE_DATE | 8 | YYYYMMDD format |
| 2 | INVOICE_NUMBER | 35 | Unique invoice identifier |
| 3 | CLIENT_ID | 24 | Client's internal ID |
| 4 | LAW_FIRM_MATTER_ID | 24 | Law firm's matter number |
| 5 | INVOICE_TOTAL | 12.2 | Total invoice amount |
| 6 | BILLING_START_DATE | 8 | Period start YYYYMMDD |
| 7 | BILLING_END_DATE | 8 | Period end YYYYMMDD |
| 8 | INVOICE_DESCRIPTION | 500 | Invoice summary |

### Line Item Fields

| Field | Description | Required |
|-------|-------------|----------|
| LINE_ITEM_NUMBER | Sequential line number | Yes |
| EXP/FEE/INV_ADJ_TYPE | F=Fee, E=Expense, IF=Invoice Fee Adj | Yes |
| LINE_ITEM_DATE | Service date YYYYMMDD | Yes |
| LINE_ITEM_TASK_CODE | UTBMS task code | Conditional |
| LINE_ITEM_EXPENSE_CODE | UTBMS expense code | Conditional |
| LINE_ITEM_ACTIVITY_CODE | UTBMS activity code | Conditional |
| TIMEKEEPER_ID | Firm's timekeeper ID | Yes for fees |
| LINE_ITEM_DESCRIPTION | Narrative description | Yes |
| LINE_ITEM_UNIT_COST | Hourly rate or unit cost | Yes |
| LINE_ITEM_NUMBER_OF_UNITS | Hours or quantity | Yes |
| LINE_ITEM_TOTAL | Line total amount | Yes |

## LEDES 2000 Format (XML)

XML-based format for complex billing scenarios.

### Basic Structure

```xml
<?xml version="1.0" encoding="UTF-8"?>
<ledes:Invoice xmlns:ledes="http://www.ledes.org/ledes2000">
  <InvoiceDate>2024-01-15</InvoiceDate>
  <InvoiceNumber>INV-2024-001</InvoiceNumber>
  <Client>
    <ClientID>CLIENT001</ClientID>
    <ClientName>Acme Corporation</ClientName>
  </Client>
  <Matter>
    <MatterID>MATTER-12345</MatterID>
    <MatterName>Smith v. Jones Litigation</MatterName>
  </Matter>
  <LineItems>
    <LineItem>
      <LineItemType>FEE</LineItemType>
      <TaskCode>L110</TaskCode>
      <ActivityCode>A101</ActivityCode>
      <Description>Review complaint and exhibits</Description>
      <Hours>2.5</Hours>
      <Rate>450.00</Rate>
      <Total>1125.00</Total>
    </LineItem>
  </LineItems>
</ledes:Invoice>
```

## LEDES 2.2 (eBilling Hub Standard)

Enhanced XML format with support for:
- Alternative fee arrangements
- Budget tracking
- Accrual reporting
- Split billing

## Field Validation Rules

### Date Fields
- Format: YYYYMMDD (1998B) or YYYY-MM-DD (XML)
- Invoice date cannot be future dated
- Line item dates must fall within billing period

### Amount Fields
- Decimal precision: 2 places
- Negative amounts indicate credits
- Currency specified at invoice level

### Text Fields
- Block billing prohibited (separate entries for distinct tasks)
- Minimum description length typically 10+ characters
- No special characters: | [ ] (1998B only)

## Common Rejection Reasons

1. **Missing UTBMS Codes** - Task/activity codes required
2. **Block Billing** - Multiple tasks in single entry
3. **Vague Descriptions** - Insufficient detail
4. **Rate Violations** - Exceeds agreed-upon rates
5. **Format Errors** - Invalid characters, wrong delimiters

## E-Billing Vendor Requirements

### Serengeti/LegalTracker
- LEDES 1998B primary
- Requires timekeeper ID mapping
- 90-day submission window

### Legal Tracker (Thomson Reuters)
- LEDES 1998B and 2000
- Supports accruals
- Budget variance alerts

### CounselLink (LexisNexis)
- LEDES 1998B standard
- Matter-level validation
- Rate card enforcement

### Brightflag
- LEDES 1998B and custom JSON
- AI-powered review
- Real-time validation

## Sample LEDES 1998B File

```
LEDES1998B[]
INVOICE_DATE|INVOICE_NUMBER|CLIENT_ID|LAW_FIRM_MATTER_ID|INVOICE_TOTAL|BILLING_START_DATE|BILLING_END_DATE|INVOICE_DESCRIPTION|LAW_FIRM_ID|LINE_ITEM_NUMBER|EXP/FEE/INV_ADJ_TYPE|LINE_ITEM_NUMBER_OF_UNITS|LINE_ITEM_ADJUSTMENT_AMOUNT|LINE_ITEM_TOTAL|LINE_ITEM_DATE|LINE_ITEM_TASK_CODE|LINE_ITEM_EXPENSE_CODE|LINE_ITEM_ACTIVITY_CODE|TIMEKEEPER_ID|LINE_ITEM_DESCRIPTION|LAW_FIRM_NAME|LINE_ITEM_UNIT_COST|TIMEKEEPER_NAME|TIMEKEEPER_CLASSIFICATION|CLIENT_MATTER_ID[]
20240115|INV-2024-001|ACME001|M-2024-0001|2325.00|20240101|20240115|Legal Services - January 2024|LAWFIRM01|1|F|2.5|0.00|1125.00|20240108|L110||A101|TK001|Review and analyze complaint and supporting exhibits; identify key factual allegations|Smith & Associates|450.00|John Smith|PARTNER|ACME-LIT-001[]
20240115|INV-2024-001|ACME001|M-2024-0001|2325.00|20240101|20240115|Legal Services - January 2024|LAWFIRM01|2|F|3.0|0.00|900.00|20240110|L110||A102|TK002|Research applicable statutes of limitation; draft research memorandum|Smith & Associates|300.00|Jane Doe|ASSOCIATE|ACME-LIT-001[]
20240115|INV-2024-001|ACME001|M-2024-0001|2325.00|20240101|20240115|Legal Services - January 2024|LAWFIRM01|3|E|1|0.00|300.00|20240112||E110||TK001|Westlaw research charges for January 2024|Smith & Associates|300.00|||ACME-LIT-001[]
```

## Best Practices

1. **Validate before submission** - Use LEDES validation tools
2. **Map timekeepers early** - Register with e-billing system
3. **Review billing guidelines** - Each client has specific requirements
4. **Track rejections** - Identify patterns in rejections
5. **Archive submissions** - Retain copies with confirmation numbers

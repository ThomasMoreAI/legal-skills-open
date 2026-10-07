# Patent Drafting - Validations

## Means-Plus-Function Language Detected

### **Id**
means-plus-function
### **Severity**
warning
### **Type**
regex
### **Pattern**
  - means for \w+
  - module for \w+
  - mechanism for \w+
### **Message**
Means-plus-function language triggers 112(f) narrow interpretation.
### **Fix Action**
Replace with structural language: 'a processor configured to...'
### **Applies To**
  - **/*claim*.txt
  - **/*patent*.md

## Potential Missing Antecedent Basis

### **Id**
missing-antecedent
### **Severity**
warning
### **Type**
regex
### **Pattern**
  - the \w+(?!.*(?:a|an) \1)
  - said \w+(?!.*(?:a|an) \1)
### **Message**
Check that 'the [noun]' has a prior 'a [noun]' introduction.
### **Fix Action**
Add antecedent: 'a [noun]' before 'the [noun]'
### **Applies To**
  - **/*claim*.txt

## Closed Claim Language

### **Id**
consisting-of-closed
### **Severity**
info
### **Type**
regex
### **Pattern**
  - consisting of
### **Message**
'Consisting of' is closed transitional phrase - excludes unlisted elements.
### **Fix Action**
Consider 'comprising' for open claim unless closure is intentional
### **Applies To**
  - **/*claim*.txt

## No CRM Claim in Software Application

### **Id**
no-crm-claim
### **Severity**
info
### **Type**
regex
### **Pattern**
  - method.*comprising(?!.*non-transitory.*computer-readable)
### **Message**
Consider adding CRM claim for software inventions.
### **Fix Action**
Add: 'A non-transitory computer-readable medium storing instructions...'
### **Applies To**
  - **/*claim*.txt

## Generic Computer Implementation

### **Id**
abstract-generic-computer
### **Severity**
warning
### **Type**
regex
### **Pattern**
  - a computer.*performing
  - a processor.*executing
  - generic.*computer
### **Message**
Generic computer implementation may face 101 rejection.
### **Fix Action**
Add specific technical improvement or unconventional implementation
### **Applies To**
  - **/*claim*.txt
  - **/*patent*.md
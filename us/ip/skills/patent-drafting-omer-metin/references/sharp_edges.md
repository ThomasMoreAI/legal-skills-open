# Patent Drafting - Sharp Edges

## Means-Plus-Function Invokes 35 USC 112(f)

### **Id**
means-plus-function-trap
### **Severity**
critical
### **Summary**
Claim term 'means for' limits scope to spec embodiments only
### **Symptoms**
  - Claim scope unexpectedly narrow
  - Competitors avoid infringement with different implementations
  - Court limits claim to spec examples
### **Why**
  Using "means for [function]" language triggers 112(f) interpretation.
  The claim term is limited to the corresponding structure in the
  specification plus equivalents. If you only described one way to
  do something, that's all your claim covers.
  
### **Gotcha**
  Claim: "means for processing data"
  
  Spec only describes: "Processing module 102 uses algorithm X"
  
  Result: Claim limited to algorithm X and equivalents
          - Algorithm Y that achieves same result? Not covered!
  
### **Solution**
  Use structural language instead:
  
  BAD:  "means for processing data"
  GOOD: "a processor configured to execute instructions that cause..."
  
  BAD:  "means for storing data"
  GOOD: "a memory storing instructions that, when executed, cause..."
  
  Include multiple embodiments in spec for each functional term.
  

## Missing Antecedent Basis Causes 112(b) Rejection

### **Id**
antecedent-basis-missing
### **Severity**
high
### **Summary**
'The' references something never introduced
### **Symptoms**
  - Office action cites 35 USC 112(b)
  - Claim term lacks antecedent basis
  - Indefiniteness rejection
### **Why**
  When you write "the data" in a claim, there must be an earlier
  reference to "a data" or "data." Otherwise, the examiner doesn't
  know what "the data" refers to.
  
### **Gotcha**
  "A method comprising:
     processing the data..."  ← What data?
  
  "A system comprising:
     wherein the controller performs..."  ← What controller?
  
### **Solution**
  Every "the [noun]" must have a prior "a [noun]" or "[noun]":
  
  "A method comprising:
     receiving a data set;
     processing the data set..."  ← Proper antecedent
  
  For multiple instances:
  "a first processor... a second processor...
   wherein the first processor communicates with the second processor"
  

## New Matter Cannot Be Added After Filing

### **Id**
new-matter-added
### **Severity**
critical
### **Summary**
Amendments must be supported by original specification
### **Symptoms**
  - Examiner rejects amendment as new matter
  - Cannot claim feature not in original spec
  - Continuation doesn't help - same spec
### **Why**
  35 USC 132 prohibits adding new matter after filing. The specification
  is frozen at the filing date. If you didn't disclose a feature,
  you can't claim it - ever. This is why thorough initial disclosure
  is critical.
  
### **Gotcha**
  Original spec: "The widget processes data using algorithm A"
  
  Later amendment: "...wherein the widget uses machine learning"
  
  Result: REJECTED - ML never disclosed in original application
  
### **Solution**
  At drafting time, include:
  - All known embodiments
  - Alternative implementations
  - Future variations you might want to claim
  - "In some embodiments" language for flexibility
  
  Example: "In some embodiments, the processing includes
            machine learning, neural networks, or statistical methods"
  

## Software Claims Rejected as Abstract Ideas

### **Id**
abstract-idea-101
### **Severity**
high
### **Summary**
Alice/Mayo creates 101 rejection for software patents
### **Symptoms**
  - Examiner cites Alice Corp. v. CLS Bank
  - Claims characterized as 'abstract idea'
  - Told to 'integrate into practical application'
### **Why**
  Post-Alice, many software claims are rejected as abstract ideas.
  The two-step test asks: (1) Is it directed to an abstract idea?
  (2) If so, does it add "significantly more"? Generic computer
  implementation doesn't satisfy step 2.
  
### **Gotcha**
  "A method comprising:
     receiving user input;
     calculating a result based on the input;
     displaying the result"
  
  Examiner: "This is the abstract idea of performing calculations"
  
### **Solution**
  Integrate practical application:
  
  1. Claim specific technical improvement:
     "...thereby reducing memory usage by 40%"
  
  2. Claim unconventional technical steps:
     "...using a convolutional neural network with architecture X"
  
  3. Claim specific hardware integration:
     "...wherein the sensor captures real-time data at 1000Hz"
  
  4. Focus on HOW, not WHAT:
     Don't just claim the goal; claim the novel technical means
  

## Single Embodiment Limits Claim Scope

### **Id**
single-embodiment-spec
### **Severity**
medium
### **Summary**
Specification only describes one way - claims limited
### **Symptoms**
  - Examiner narrows claim to match spec
  - No support for broader claim language
  - Can't claim alternatives not disclosed
### **Why**
  Claims are limited by the specification. If you only describe
  one embodiment, your broad claim language may be construed
  narrowly. Competitors can use alternative implementations
  you never disclosed.
  
### **Gotcha**
  Claim: "A method for processing images..."
  Spec: Only describes processing with algorithm X
  
  Court/examiner: "Processing" means algorithm X
                   because that's all the spec discloses
  
### **Solution**
  Describe multiple embodiments:
  
  "In one embodiment, image processing uses algorithm X.
   In another embodiment, algorithm Y may be used.
   In yet another embodiment, machine learning models
   such as CNNs, transformers, or ensemble methods may be employed."
  
  Use open-ended language:
  "Processing may include, but is not limited to..."
  
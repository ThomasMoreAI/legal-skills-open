# 📖 General Definitions for Extraction

To maintain strict objectivity during Step 1 (Granular Review), the agent must separate extracted information based on the following definitions:

* **Facts:** Objective, empirically verifiable realities, undisputed events, physical measurements, dates, and exact quotes. A Fact from one file may be a disputed event when contributed by another file.
  * *Formatting Rule:* Must ALWAYS be wrapped in `<fact> [Fact] </fact>` tags to anchor the model and prevent hallucination. 
  * *Example:* `<fact>The invoice is dated March 14, 2026.</fact>`
* **Opinions / Claims:** Subjective allegations, demands, disputed statements, or unproven conclusions made by a party. 
  * *Example:* "The office is completely uninhabitable due to the construction noise."
* **Legal Views:** Statutory references, citations of case law, and specific legal interpretations advanced by the authors. 
  * *Example:* "The office was terminated in accordance with the agreement and statutory law."

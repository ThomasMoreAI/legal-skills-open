# 📝 Output Formats (Disk Writes)

Depending on the active step in `PRD.md` and the configuration in configuration.md, the agent must write its output to the disk using the following strict XML formats.

### Step 1: Individual File Summaries
*Write to `summary_[filename].xml`*

```xml
<document_summary source="[Insert File Name]">
  <metadata>
    <date_processed>[Current Date]</date_processed>
    <document_type>[e.g., evidence, motion, decision]</document_type>
    <tags>[comma separated tags]</tags>
  </metadata>
  <facts>
    [Bullet points of objective, verifiable facts. Use <fact> tags with quotes from the source if configured.]
  </facts>
  <opinions_and_claims>
    [Bullet points of subjective allegations or demands with quotes from the source if configured.]
  </opinions_and_claims>
  <legal_views>
    [Bullet points of the legal arguments or statutes with quotes from the source if configured.]
  </legal_views>
</document_summary>
```

### Step 2: Synthesis
*Write to `final_synthesis.xml`*

```xml
<qc_and_synthesis_certificate>
  <review_metadata>
    <perspective_applied>[State the perspective used in Step 2]</perspective_applied>
    <files_reviewed>[List of all files synthesized]</files_reviewed>
    <status>[PASS / FAIL / REVIEW REQUIRED]</status>
  </review_metadata>

  <timeline_overview>
    [A synthesized, chronological timeline of the key <fact> events across all processed XML summaries.]
  </timeline_overview>
  
  <contradictions_and_discrepancies>
    [Identify where opinions/claims in one document clash with facts or claims in another document.]
  </contradictions_and_discrepancies>
  
  <holistic_assessment>
    [A comprehensive summary of the entire case. What is the core conflict and factual discrepancies? What are the primary strengths and weaknesses of the overarching positions? What is uncertain and why?]
  </holistic_assessment>
</qc_and_synthesis_certificate>
```

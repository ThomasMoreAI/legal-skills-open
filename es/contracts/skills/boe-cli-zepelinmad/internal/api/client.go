package api

import (
	"encoding/json"
	"encoding/xml"
	"fmt"
	"io"
	"net/http"
	"net/url"
	"strings"
	"time"
)

const baseURL = "https://www.boe.es/datosabiertos/api"

// Client is the BOE API client
type Client struct {
	http *http.Client
}

// NewClient creates a new BOE API client
func NewClient() *Client {
	return &Client{
		http: &http.Client{
			Timeout: 30 * time.Second,
		},
	}
}

// XMLResponse is the generic BOE API XML response wrapper
type XMLResponse struct {
	XMLName xml.Name `xml:"response"`
	Status  struct {
		Code string `xml:"code"`
		Text string `xml:"text"`
	} `xml:"status"`
	Data string `xml:",innerxml"`
}

// doRequest performs an HTTP request to the BOE API
func (c *Client) doRequest(path string, acceptJSON bool) ([]byte, error) {
	reqURL := baseURL + path

	req, err := http.NewRequest("GET", reqURL, nil)
	if err != nil {
		return nil, fmt.Errorf("creating request: %w", err)
	}

	if acceptJSON {
		req.Header.Set("Accept", "application/json")
	} else {
		req.Header.Set("Accept", "application/xml")
	}

	resp, err := c.http.Do(req)
	if err != nil {
		return nil, fmt.Errorf("request failed: %w", err)
	}
	defer resp.Body.Close()

	body, err := io.ReadAll(resp.Body)
	if err != nil {
		return nil, fmt.Errorf("reading response: %w", err)
	}

	return body, nil
}

// GetJSON fetches a BOE API endpoint and returns parsed JSON
func (c *Client) GetJSON(path string) (json.RawMessage, error) {
	body, err := c.doRequest(path, true)
	if err != nil {
		return nil, err
	}

	var result json.RawMessage
	if err := json.Unmarshal(body, &result); err != nil {
		return nil, fmt.Errorf("API returned non-JSON response: %s", truncate(string(body), 200))
	}

	var apiResp struct {
		Status struct {
			Code string `json:"code"`
			Text string `json:"text"`
		} `json:"status"`
	}
	if err := json.Unmarshal(body, &apiResp); err == nil {
		if apiResp.Status.Code != "" && apiResp.Status.Code != "200" {
			return nil, fmt.Errorf("API error %s: %s", apiResp.Status.Code, apiResp.Status.Text)
		}
	}

	return result, nil
}

// GetXML fetches a BOE API endpoint and returns raw XML
func (c *Client) GetXML(path string) ([]byte, error) {
	return c.doRequest(path, false)
}

// NormalizeQuery takes a user query and normalizes it for the BOE API.
// If no field prefixes are used, searches in texto: by default.
// Multi-word searches are connected with AND.
func NormalizeQuery(input string) string {
	input = strings.TrimSpace(input)
	if input == "" {
		return ""
	}

	// If it already contains field:value syntax, use as-is
	if strings.Contains(input, ":") {
		// But fix multi-word field queries: "texto:compraventa participaciones"
		// → "texto:compraventa and texto:participaciones"
		return expandMultiWordFields(input)
	}

	// Plain text: wrap each word with texto:
	words := strings.Fields(input)
	parts := make([]string, len(words))
	for i, w := range words {
		lower := strings.ToLower(w)
		if lower == "and" || lower == "or" || lower == "not" || lower == "(" || lower == ")" {
			parts[i] = w
		} else {
			parts[i] = "texto:" + w
		}
	}
	return strings.Join(parts, " and ")
}

// expandMultiWordFields fixes queries like "texto:compraventa participaciones"
// to "texto:compraventa and texto:participaciones"
func expandMultiWordFields(input string) string {
	tokens := strings.Fields(input)
	var result []string
	currentField := ""

	for _, token := range tokens {
		lower := strings.ToLower(token)

		// Check if it's a logical operator
		if lower == "and" || lower == "or" || lower == "not" || lower == "(" || lower == ")" {
			result = append(result, token)
			continue
		}

		// Check if it has a field prefix
		if idx := strings.Index(token, ":"); idx > 0 {
			field := token[:idx]
			// Known fields
			knownFields := []string{"titulo", "texto", "ambito@codigo", "departamento@codigo",
				"rango@codigo", "materia@codigo", "estado_consolidacion@codigo",
				"fecha_disposicion", "numero_oficial", "fecha_publicacion",
				"diario_numero", "vigencia_agotada"}
			isField := false
			for _, f := range knownFields {
				if field == f {
					isField = true
					break
				}
			}
			if isField {
				currentField = field
				result = append(result, token)
				continue
			}
		}

		// No field prefix — use current field or default to texto
		if currentField != "" {
			if len(result) > 0 {
				result = append(result, "and")
			}
			result = append(result, currentField+":"+token)
		} else {
			if len(result) > 0 {
				result = append(result, "and")
			}
			result = append(result, "texto:"+token)
		}
	}

	return strings.Join(result, " ")
}

// SearchLegislation searches consolidated legislation using the advanced query API
func (c *Client) SearchLegislation(queryStr string, limit int, offset int, from string, to string) (json.RawMessage, error) {
	params := url.Values{}

	if queryStr != "" {
		normalized := NormalizeQuery(queryStr)
		queryJSON := fmt.Sprintf(`{"query":{"query_string":{"query":"%s"}},"sort":[]}`, normalized)
		params.Set("query", queryJSON)
	}

	if limit > 0 {
		params.Set("limit", fmt.Sprintf("%d", limit))
	}
	if offset > 0 {
		params.Set("offset", fmt.Sprintf("%d", offset))
	}
	if from != "" {
		params.Set("from", from)
	}
	if to != "" {
		params.Set("to", to)
	}

	path := "/legislacion-consolidada"
	if len(params) > 0 {
		path += "?" + params.Encode()
	}

	return c.GetJSON(path)
}

// SearchRaw sends a raw JSON query to the search endpoint
func (c *Client) SearchRaw(rawQuery string, limit int, offset int) (json.RawMessage, error) {
	params := url.Values{}
	params.Set("query", rawQuery)
	if limit > 0 {
		params.Set("limit", fmt.Sprintf("%d", limit))
	}
	if offset > 0 {
		params.Set("offset", fmt.Sprintf("%d", offset))
	}

	path := "/legislacion-consolidada?" + params.Encode()
	return c.GetJSON(path)
}

// ListRecentLegislation lists recently updated consolidated legislation
func (c *Client) ListRecentLegislation(limit int, offset int) (json.RawMessage, error) {
	params := url.Values{}
	if limit > 0 {
		params.Set("limit", fmt.Sprintf("%d", limit))
	}
	if offset > 0 {
		params.Set("offset", fmt.Sprintf("%d", offset))
	}

	path := "/legislacion-consolidada"
	if len(params) > 0 {
		path += "?" + params.Encode()
	}

	return c.GetJSON(path)
}

// GetLawIndex gets the structural index (blocks) of a law
func (c *Client) GetLawIndex(id string) (json.RawMessage, error) {
	return c.GetJSON(fmt.Sprintf("/legislacion-consolidada/id/%s/texto/indice", id))
}

// GetLawBlock gets a specific block (article, chapter, etc.) of a law
func (c *Client) GetLawBlock(id string, blockID string) ([]byte, error) {
	return c.GetXML(fmt.Sprintf("/legislacion-consolidada/id/%s/texto/bloque/%s", id, blockID))
}

// GetLawMetadata gets metadata for a law
func (c *Client) GetLawMetadata(id string) (json.RawMessage, error) {
	return c.GetJSON(fmt.Sprintf("/legislacion-consolidada/id/%s/metadatos", id))
}

// GetLawAnalysis gets the analysis (modifications, references) for a law
func (c *Client) GetLawAnalysis(id string) (json.RawMessage, error) {
	return c.GetJSON(fmt.Sprintf("/legislacion-consolidada/id/%s/analisis", id))
}

// GetDailySummary gets the BOE summary for a specific date (YYYYMMDD)
func (c *Client) GetDailySummary(date string) (json.RawMessage, error) {
	if date == "" {
		date = time.Now().Format("20060102")
	}
	return c.GetJSON(fmt.Sprintf("/boe/sumario/%s", date))
}

// GetBORMESummary gets the BORME summary for a specific date (YYYYMMDD)
func (c *Client) GetBORMESummary(date string) (json.RawMessage, error) {
	if date == "" {
		date = time.Now().Format("20060102")
	}
	return c.GetJSON(fmt.Sprintf("/borme/sumario/%s", date))
}

func truncate(s string, max int) string {
	if len(s) > max {
		return s[:max] + "..."
	}
	return s
}

// SearchResultItem is a parsed search result
type SearchResultItem struct {
	ID      string `json:"identificador"`
	Title   string `json:"titulo"`
	URL     string `json:"url"`
	Rango   struct {
		Text string `json:"texto"`
	} `json:"rango"`
	Date    string `json:"fecha_publicacion"`
	Vigente string `json:"vigencia_agotada"`
	Score   int    `json:"-"` // internal ranking score
	Source  string `json:"-"` // "alias", "title", "texto"
}

// BoeURL returns the consolidated text URL for a BOE identifier
func BoeURL(id string) string {
	return "https://www.boe.es/buscar/act.php?id=" + id
}

// SmartSearch performs an intelligent search with alias lookup, title-first, and reranking
func (c *Client) SmartSearch(query string, limit int) ([]SearchResultItem, string, error) {
	// Step 1: Check aliases (exact match)
	if id, ok := LookupAlias(query); ok {
		items, err := c.fetchLawAsResult(id)
		if err == nil && len(items) > 0 {
			return items, "alias", nil
		}
	}

	// Step 2: Check synonyms — expand colloquial terms to legal terms
	// then try alias again with expanded term
	expandedQuery := query
	if expanded, ok := ExpandSynonyms(query); ok {
		expandedQuery = expanded
		if id, ok := LookupAlias(expanded); ok {
			items, err := c.fetchLawAsResult(id)
			if err == nil && len(items) > 0 {
				return items, "alias", nil
			}
		}
	}

	// Step 3: Fuzzy match — catch typos and near-misses
	if id, matched, dist := FuzzyMatch(query, 3); id != "" {
		items, err := c.fetchLawAsResult(id)
		if err == nil && len(items) > 0 {
			items[0].Source = fmt.Sprintf("fuzzy:%s(d=%d)", matched, dist)
			return items, "fuzzy", nil
		}
	}

	// Step 4: Word-level fuzzy match — "tributria" matches "tributaria" in "general tributaria"
	if id, matched := FuzzyWordMatch(query, 2); id != "" {
		items, err := c.fetchLawAsResult(id)
		if err == nil && len(items) > 0 {
			items[0].Source = "fuzzyword:" + matched
			return items, "fuzzy", nil
		}
	}

	// Step 5: Partial word match in aliases — "sociedades" matches "sociedades de capital"
	if id, matched := ContainsWordMatch(query); id != "" {
		items, err := c.fetchLawAsResult(id)
		if err == nil && len(items) > 0 {
			items[0].Source = "partial:" + matched
			return items, "partial", nil
		}
	}

	// Step 5: Check if user used explicit field syntax — pass through
	if strings.Contains(query, ":") && !strings.HasPrefix(strings.ToLower(query), "search") {
		items, err := c.searchAndParse(NormalizeQuery(query), limit)
		return items, "direct", err
	}

	// Step 6: Smart search — multi-strategy title search, then texto
	cleanQuery := RemoveStopWords(query)
	if cleanQuery == "" {
		cleanQuery = query
	}
	cleanExpanded := RemoveStopWords(expandedQuery)
	if cleanExpanded == "" {
		cleanExpanded = expandedQuery
	}

	var allTitleResults []SearchResultItem

	// Strategy A: Title search with original query (quoted phrase)
	titleQuery := buildTitleQuery(cleanQuery)
	if titleQuery != "" {
		results, _ := c.searchAndParse(titleQuery, limit)
		allTitleResults = append(allTitleResults, results...)
	}

	// Strategy B: If synonym expanded, also search with expanded terms
	if cleanExpanded != cleanQuery {
		expandedTitleQuery := buildTitleQuery(cleanExpanded)
		if expandedTitleQuery != "" {
			results, _ := c.searchAndParse(expandedTitleQuery, limit)
			allTitleResults = append(allTitleResults, results...)
		}
	}

	// Strategy C: Title search with individual words (AND, not phrase) if few results
	if len(allTitleResults) < 3 {
		wordQuery := buildTitleWordsQuery(cleanQuery)
		if wordQuery != "" && wordQuery != titleQuery {
			results, _ := c.searchAndParse(wordQuery, limit)
			allTitleResults = append(allTitleResults, results...)
		}
	}

	// Strategy D: Texto search for additional results
	var textoResults []SearchResultItem
	if len(allTitleResults) < limit {
		textoQuery := buildTextoQuery(cleanQuery)
		textoResults, _ = c.searchAndParse(textoQuery, limit)
	}

	// Merge and rerank
	merged := mergeAndRerank(allTitleResults, textoResults, query, limit)

	source := "smart"
	if len(allTitleResults) > 0 {
		source = "title"
	}
	return merged, source, nil
}

// fetchLawAsResult gets a single law's metadata and returns it as a search result
func (c *Client) fetchLawAsResult(id string) ([]SearchResultItem, error) {
	meta, err := c.GetLawMetadata(id)
	if err != nil {
		return nil, err
	}

	// BOE metadata API returns data as a list of objects
	var metaResp struct {
		Data []struct {
			ID     string `json:"identificador"`
			Title  string `json:"titulo"`
			Rango  struct {
				Text string `json:"texto"`
			} `json:"rango"`
			Date    string `json:"fecha_publicacion"`
			Vigente string `json:"vigencia_agotada"`
		} `json:"data"`
	}

	if err := json.Unmarshal(meta, &metaResp); err != nil {
		return nil, fmt.Errorf("parsing metadata: %w", err)
	}

	if len(metaResp.Data) == 0 {
		return nil, fmt.Errorf("no metadata found for %s", id)
	}

	m := metaResp.Data[0]
	item := SearchResultItem{
		ID:      m.ID,
		Title:   m.Title,
		URL:     BoeURL(m.ID),
		Date:    m.Date,
		Vigente: m.Vigente,
		Score:   1000,
		Source:  "alias",
	}
	item.Rango.Text = m.Rango.Text
	return []SearchResultItem{item}, nil
}

// searchAndParse runs a raw query and returns parsed items
func (c *Client) searchAndParse(queryStr string, limit int) ([]SearchResultItem, error) {
	params := url.Values{}
	// Escape inner double quotes for valid JSON
	escaped := strings.ReplaceAll(queryStr, `"`, `\"`)
	queryJSON := fmt.Sprintf(`{"query":{"query_string":{"query":"%s"}},"sort":[]}`, escaped)
	params.Set("query", queryJSON)
	if limit > 0 {
		params.Set("limit", fmt.Sprintf("%d", limit))
	}

	path := "/legislacion-consolidada?" + params.Encode()
	data, err := c.GetJSON(path)
	if err != nil {
		return nil, err
	}

	var resp struct {
		Data []SearchResultItem `json:"data"`
	}
	if err := json.Unmarshal(data, &resp); err != nil {
		return nil, err
	}

	// Populate URL from ID
	for i := range resp.Data {
		if resp.Data[i].ID != "" {
			resp.Data[i].URL = BoeURL(resp.Data[i].ID)
		}
	}

	return resp.Data, nil
}

// buildTitleQuery creates an optimized title search query
func buildTitleQuery(cleanedInput string) string {
	words := strings.Fields(cleanedInput)
	if len(words) == 0 {
		return ""
	}

	// Use quoted phrase for 2+ words
	if len(words) >= 2 {
		phrase := strings.Join(words, " ")
		return fmt.Sprintf(`titulo:"%s"`, phrase)
	}
	return "titulo:" + words[0]
}

// buildTitleWordsQuery creates a title search with individual words ANDed (not phrase)
func buildTitleWordsQuery(cleanedInput string) string {
	words := strings.Fields(cleanedInput)
	if len(words) <= 1 {
		return ""
	}
	parts := make([]string, len(words))
	for i, w := range words {
		parts[i] = "titulo:" + w
	}
	return strings.Join(parts, " and ")
}

// buildTextoQuery creates a texto search query
func buildTextoQuery(cleanedInput string) string {
	words := strings.Fields(cleanedInput)
	if len(words) == 0 {
		return ""
	}

	parts := make([]string, len(words))
	for i, w := range words {
		parts[i] = "texto:" + w
	}
	return strings.Join(parts, " and ")
}

// mergeAndRerank combines title and texto results, deduplicates, and sorts by relevance
func mergeAndRerank(titleResults, textoResults []SearchResultItem, originalQuery string, limit int) []SearchResultItem {
	seen := make(map[string]bool)
	var all []SearchResultItem

	// Title results get base score 100
	for _, r := range titleResults {
		r.Source = "title"
		r.Score = 100 + scoreResult(r, originalQuery)
		if !seen[r.ID] {
			seen[r.ID] = true
			all = append(all, r)
		}
	}

	// Texto results get base score 0
	for _, r := range textoResults {
		if !seen[r.ID] {
			r.Source = "texto"
			r.Score = scoreResult(r, originalQuery)
			seen[r.ID] = true
			all = append(all, r)
		}
	}

	// Sort by score descending
	for i := 0; i < len(all); i++ {
		for j := i + 1; j < len(all); j++ {
			if all[j].Score > all[i].Score {
				all[i], all[j] = all[j], all[i]
			}
		}
	}

	if len(all) > limit {
		all = all[:limit]
	}
	return all
}

// scoreResult assigns a relevance score to a search result
func scoreResult(r SearchResultItem, query string) int {
	score := 0
	lowerTitle := strings.ToLower(r.Title)
	lowerQuery := strings.ToLower(query)
	queryWords := strings.Fields(RemoveStopWords(lowerQuery))

	// Base law indicators (huge boost)
	if strings.Contains(lowerTitle, "texto refundido") && strings.Contains(lowerTitle, "aprueba") {
		score += 80
	} else if strings.Contains(lowerTitle, "texto refundido") {
		score += 60
	} else if strings.Contains(lowerTitle, "aprueba") {
		score += 40
	}

	// Amendment/modification penalty
	if strings.Contains(lowerTitle, "modifica") || strings.Contains(lowerTitle, "modificación") {
		score -= 30
	}
	if strings.Contains(lowerTitle, "deroga") {
		score -= 20
	}

	// No longer in force penalty
	if r.Vigente == "S" {
		score -= 40
	}

	// Query words in title bonus
	matchCount := 0
	for _, w := range queryWords {
		if strings.Contains(lowerTitle, w) {
			matchCount++
		}
	}
	if len(queryWords) > 0 {
		score += (matchCount * 20) / len(queryWords)
	}

	// Exact substring match (normalized) — huge bonus
	cleanQuery := strings.Join(queryWords, " ")
	if cleanQuery != "" && strings.Contains(normalizeForAlias(lowerTitle), normalizeForAlias(cleanQuery)) {
		score += 50
	}

	// Rank type bonus (prefer Ley, Ley Orgánica, Real Decreto Legislativo)
	rangoLower := strings.ToLower(r.Rango.Text)
	switch {
	case strings.Contains(rangoLower, "ley orgánica") || strings.Contains(rangoLower, "ley organica"):
		score += 15
	case rangoLower == "ley":
		score += 12
	case strings.Contains(rangoLower, "decreto legislativo"):
		score += 10
	case strings.Contains(rangoLower, "real decreto-ley"):
		score += 5
	}

	return score
}

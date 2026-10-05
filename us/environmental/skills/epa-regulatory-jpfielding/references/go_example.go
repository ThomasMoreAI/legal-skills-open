// Package epareg shows stdlib-only Go clients for the four EPA regulatory
// data subsystems: Envirofacts, ECHO, GHGRP, and Subpart W (a GHGRP subset).
//
// No external dependencies. No API key required today; if EPA adds one, see
// resolveAPIKey() for the credential chain.
package epareg

import (
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"net/url"
	"os"
	"path/filepath"
	"sort"
	"strings"
	"time"
)

// --------------------------------------------------------------------------
// Credential chain (contingency — EPA does not require a key today)
// --------------------------------------------------------------------------

func resolveAPIKey() (string, error) {
	if home, err := os.UserHomeDir(); err == nil {
		creds := filepath.Join(home, ".config", "epa", "credentials")
		if data, err := os.ReadFile(creds); err == nil {
			for _, line := range strings.Split(string(data), "\n") {
				if strings.HasPrefix(line, "api_key=") {
					return strings.TrimPrefix(line, "api_key="), nil
				}
			}
		}
	}
	if k := os.Getenv("EPA_API_KEY"); k != "" {
		return k, nil
	}
	return "", nil // no key required today; return empty string, not error
}

// --------------------------------------------------------------------------
// Shared HTTP client
// --------------------------------------------------------------------------

var httpClient = &http.Client{Timeout: 60 * time.Second}

func httpGetJSON(rawURL string, out any) error {
	req, err := http.NewRequest("GET", rawURL, nil)
	if err != nil {
		return err
	}
	req.Header.Set("Accept", "application/json")
	resp, err := httpClient.Do(req)
	if err != nil {
		return err
	}
	defer resp.Body.Close()
	body, err := io.ReadAll(resp.Body)
	if err != nil {
		return err
	}
	if resp.StatusCode != 200 {
		return fmt.Errorf("HTTP %d: %s", resp.StatusCode, string(body))
	}
	return json.Unmarshal(body, out)
}

// --------------------------------------------------------------------------
// Envirofacts client (Mode 1)
// --------------------------------------------------------------------------

const envirofactsBase = "https://data.epa.gov/efservice"

type EnvirofactsQuery struct {
	Table   string            // e.g., "TRI_FACILITY"
	Filters map[string]string // column → value (exact match)
	Start   int               // row range start (0-based)
	End     int               // row range end (inclusive)
	Format  string            // JSON, XML, CSV — defaults to JSON
}

// URL builds the path-based Envirofacts URL. Filters apply in insertion order
// via map iteration — if order matters, pre-sort your filter keys.
func (q EnvirofactsQuery) URL() string {
	parts := []string{envirofactsBase, q.Table}
	for col, val := range q.Filters {
		parts = append(parts, col, val)
	}
	if q.End > 0 || q.Start > 0 {
		parts = append(parts, "rows", fmt.Sprintf("%d:%d", q.Start, q.End))
	}
	fmtOut := q.Format
	if fmtOut == "" {
		fmtOut = "JSON"
	}
	parts = append(parts, fmtOut)
	return strings.Join(parts, "/")
}

// FetchRaw returns the raw JSON array as []map[string]any. Envirofacts replies
// are flat arrays at the root.
func (q EnvirofactsQuery) FetchRaw() ([]map[string]any, error) {
	var rows []map[string]any
	if err := httpGetJSON(q.URL(), &rows); err != nil {
		// Envirofacts returns {"error": "...table is not available."} on 404
		// but that parses as a map, not an array. Retry as a single object.
		var errObj map[string]any
		if err2 := httpGetJSON(q.URL(), &errObj); err2 == nil {
			if msg, ok := errObj["error"].(string); ok {
				return nil, fmt.Errorf("envirofacts: %s", msg)
			}
		}
		return nil, err
	}
	return rows, nil
}

// FetchAll paginates through all rows in pages of `pageSize`.
func (q EnvirofactsQuery) FetchAll(pageSize int) ([]map[string]any, error) {
	var out []map[string]any
	start := 0
	for {
		q.Start = start
		q.End = start + pageSize - 1
		page, err := q.FetchRaw()
		if err != nil {
			return nil, err
		}
		out = append(out, page...)
		if len(page) < pageSize {
			break
		}
		start += pageSize
	}
	return out, nil
}

// --------------------------------------------------------------------------
// ECHO client (Mode 2) — two-step search/retrieve
// --------------------------------------------------------------------------

const echoBase = "https://echodata.epa.gov/echo"

type EchoProgram string

const (
	EchoCWA  EchoProgram = "cwa"
	EchoRCRA EchoProgram = "rcra"
	EchoSDW  EchoProgram = "sdw"
	EchoCAA  EchoProgram = "air"
)

func (p EchoProgram) searchEndpoint() string {
	switch p {
	case EchoSDW:
		return "sdw_rest_services.get_systems"
	default:
		return fmt.Sprintf("%s_rest_services.get_facilities", p)
	}
}

func (p EchoProgram) retrieveEndpoint() string {
	return fmt.Sprintf("%s_rest_services.get_qid", p)
}

type EchoSearchResult struct {
	Results struct {
		Message   string `json:"Message"`
		QueryID   string `json:"QueryID"`
		QueryRows string `json:"QueryRows"`
		Error     *struct {
			ErrorMessage string `json:"ErrorMessage"`
		} `json:"Error"`
	} `json:"Results"`
}

// EchoSearch issues the step-1 search and returns the QueryID + total count.
func EchoSearch(prog EchoProgram, params map[string]string) (qid string, total string, err error) {
	v := url.Values{}
	v.Set("output", "JSON")
	for k, val := range params {
		v.Set(k, val)
	}
	u := fmt.Sprintf("%s/%s?%s", echoBase, prog.searchEndpoint(), v.Encode())
	var res EchoSearchResult
	if err := httpGetJSON(u, &res); err != nil {
		return "", "", err
	}
	if res.Results.Error != nil {
		return "", "", fmt.Errorf("echo error: %s", res.Results.Error.ErrorMessage)
	}
	return res.Results.QueryID, res.Results.QueryRows, nil
}

// EchoRetrieve fetches a single page of records for a given QueryID.
func EchoRetrieve(prog EchoProgram, qid string, pageNo, pageSize int) (map[string]any, error) {
	v := url.Values{}
	v.Set("output", "JSON")
	v.Set("qid", qid)
	v.Set("pageno", fmt.Sprintf("%d", pageNo))
	v.Set("pagesize", fmt.Sprintf("%d", pageSize))
	u := fmt.Sprintf("%s/%s?%s", echoBase, prog.retrieveEndpoint(), v.Encode())
	var out map[string]any
	if err := httpGetJSON(u, &out); err != nil {
		return nil, err
	}
	return out, nil
}

// --------------------------------------------------------------------------
// GHGRP / Subpart W helpers (Mode 3 + Mode 4)
// --------------------------------------------------------------------------

// GHGRPQuery is a typed wrapper around EnvirofactsQuery for V_GHG_EMITTER_SUBPART.
type GHGRPQuery struct {
	Subpart  string // e.g., "W", "C", "Y", "UU", "RR"
	State    string // e.g., "WV"
	Year     int    // e.g., 2022
	GasCode  string // e.g., "CH4" (optional)
	Facility string // CONTAINING substring (optional)
	Start    int
	End      int
}

func (g GHGRPQuery) toEnvirofacts() EnvirofactsQuery {
	filters := map[string]string{}
	if g.Subpart != "" {
		filters["SUBPART_NAME"] = g.Subpart
	}
	if g.State != "" {
		filters["STATE"] = g.State
	}
	if g.Year > 0 {
		filters["YEAR"] = fmt.Sprintf("%d", g.Year)
	}
	if g.GasCode != "" {
		filters["GAS_CODE"] = g.GasCode
	}
	// Facility substring uses CONTAINING operator; Envirofacts accepts
	// it inline after the column. This simple client does not encode
	// operators — callers needing CONTAINING should build a URL directly.
	return EnvirofactsQuery{
		Table:   "V_GHG_EMITTER_SUBPART",
		Filters: filters,
		Start:   g.Start,
		End:     g.End,
	}
}

// FetchRows returns raw GHGRP rows (one row per gas per subpart per facility).
func (g GHGRPQuery) FetchRows() ([]map[string]any, error) {
	if g.End == 0 && g.Start == 0 {
		g.End = 499
	}
	return g.toEnvirofacts().FetchRaw()
}

// FacilityTotal is an aggregated view per facility.
type FacilityTotal struct {
	FacilityID   int64
	FacilityName string
	County       string
	State        string
	TotalCO2e    float64
	MethaneCO2e  float64
}

// AggregateByFacility rolls up raw rows to per-facility totals and per-gas
// CH4 totals. Returns results sorted by total CO2e descending.
func AggregateByFacility(rows []map[string]any) []FacilityTotal {
	byID := make(map[int64]*FacilityTotal)
	for _, r := range rows {
		fid := toInt64(r["facility_id"])
		if _, ok := byID[fid]; !ok {
			byID[fid] = &FacilityTotal{
				FacilityID:   fid,
				FacilityName: toStr(r["facility_name"]),
				County:       toStr(r["county"]),
				State:        toStr(r["state"]),
			}
		}
		ft := byID[fid]
		co2e := toFloat(r["co2e_emission"])
		ft.TotalCO2e += co2e
		if strings.EqualFold(toStr(r["gas_code"]), "CH4") {
			ft.MethaneCO2e += co2e
		}
	}
	out := make([]FacilityTotal, 0, len(byID))
	for _, ft := range byID {
		out = append(out, *ft)
	}
	sort.Slice(out, func(i, j int) bool { return out[i].TotalCO2e > out[j].TotalCO2e })
	return out
}

// MethaneMass converts CH4 CO2e (MT) to physical methane mass (tonnes).
// Uses EPA regulatory GWP basis (AR4, CH4=25). Pass a different gwp to compare.
func MethaneMass(co2eTonnes, gwp float64) float64 {
	if gwp <= 0 {
		gwp = 25 // AR4 default
	}
	return co2eTonnes / gwp
}

// --------------------------------------------------------------------------
// Small type helpers — Envirofacts returns numeric fields as interface{}
// --------------------------------------------------------------------------

func toStr(v any) string {
	if v == nil {
		return ""
	}
	if s, ok := v.(string); ok {
		return s
	}
	return fmt.Sprintf("%v", v)
}

func toInt64(v any) int64 {
	switch x := v.(type) {
	case float64:
		return int64(x)
	case int64:
		return x
	case int:
		return int64(x)
	case string:
		var n int64
		fmt.Sscanf(x, "%d", &n)
		return n
	}
	return 0
}

func toFloat(v any) float64 {
	switch x := v.(type) {
	case float64:
		return x
	case int64:
		return float64(x)
	case int:
		return float64(x)
	case string:
		var f float64
		fmt.Sscanf(x, "%f", &f)
		return f
	}
	return 0
}

// --------------------------------------------------------------------------
// Example usage (compile-time only, not run)
// --------------------------------------------------------------------------

func exampleTRIWestVirginia() {
	q := EnvirofactsQuery{
		Table:   "TRI_FACILITY",
		Filters: map[string]string{"STATE_ABBR": "WV", "COUNTY_NAME": "MONONGALIA"},
		Start:   0, End: 49,
	}
	rows, err := q.FetchRaw()
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Printf("%d TRI facilities in Monongalia County, WV\n", len(rows))
}

func exampleEchoCWA() {
	qid, total, err := EchoSearch(EchoCWA, map[string]string{
		"p_st": "WV",
		"p_co": "MONONGALIA",
	})
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Printf("QueryID=%s total=%s\n", qid, total)
	page, _ := EchoRetrieve(EchoCWA, qid, 1, 20)
	fmt.Printf("page 1: %d keys\n", len(page))
}

func exampleSubpartW_WV_2022() {
	q := GHGRPQuery{Subpart: "W", State: "WV", Year: 2022, Start: 0, End: 499}
	rows, err := q.FetchRows()
	if err != nil {
		fmt.Println(err)
		return
	}
	totals := AggregateByFacility(rows)
	for i := 0; i < 10 && i < len(totals); i++ {
		t := totals[i]
		fmt.Printf("%d. %s (%s) — %.0f MT CO2e total, %.0f MT CH4 CO2e (%.1f t CH4)\n",
			i+1, t.FacilityName, t.County, t.TotalCO2e, t.MethaneCO2e,
			MethaneMass(t.MethaneCO2e, 25))
	}
}

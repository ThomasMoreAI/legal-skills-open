package cmd

import (
	"encoding/json"
	"fmt"
	"strconv"
	"strings"

	"github.com/peterh/liner"
	"github.com/spf13/cobra"
	"github.com/zepelinmad/boe-cli/internal/api"
	"github.com/zepelinmad/boe-cli/internal/semantic"
	"github.com/zepelinmad/boe-cli/internal/ui"
)

// REPLState holds the interactive session state
type REPLState struct {
	client        *api.Client
	currentLaw    string
	lawTitle      string
	index         []indexEntry
	lastSearch    []searchResult
	semanticIndex *semantic.Index
	embedClient   *semantic.EmbedClient
}

type indexEntry struct {
	ID    string
	Title string
}

type searchResult struct {
	ID    string
	Title string
}

// StartREPL launches the interactive shell
func StartREPL() {
	state := &REPLState{
		client: api.NewClient(),
	}

	// Try to load semantic index
	idxPath := semantic.DefaultIndexPath()
	if semIdx, err := semantic.LoadIndex(idxPath); err == nil {
		state.semanticIndex = semIdx
		state.embedClient = semantic.NewEmbedClient()
	}

	line := liner.NewLiner()
	defer line.Close()
	line.SetCtrlCAborts(true)

	commands := []string{
		"search", "law", "article", "art", "index", "metadata", "analysis",
		"today", "borme", "help", "exit", "quit", "clear", "back",
	}
	line.SetCompleter(func(l string) (c []string) {
		for _, cmd := range commands {
			if strings.HasPrefix(cmd, strings.ToLower(l)) {
				c = append(c, cmd)
			}
		}
		if state.index != nil {
			parts := strings.Fields(l)
			if len(parts) >= 1 && (parts[0] == "article" || parts[0] == "art" || parts[0] == "a") {
				prefix := ""
				if len(parts) > 1 {
					prefix = parts[1]
				}
				for _, entry := range state.index {
					if strings.HasPrefix(entry.ID, prefix) {
						c = append(c, parts[0]+" "+entry.ID)
					}
				}
			}
		}
		return
	})

	ui.Banner(Version)

	for {
		// Print colored prompt manually since liner doesn't support ANSI codes
		lawName := ""
		if state.currentLaw != "" {
			lawName = shortLawName(state.lawTitle, state.currentLaw)
		}
		fmt.Print(ui.LawPrompt(lawName))

		input, err := line.Prompt("")
		if err != nil {
			fmt.Printf("\n  %s👋 Hasta luego%s\n\n", ui.Sand, ui.Reset)
			return
		}

		input = strings.TrimSpace(input)
		if input == "" {
			continue
		}
		line.AppendHistory(input)

		parts := strings.Fields(input)
		cmd := strings.ToLower(parts[0])
		args := parts[1:]

		switch cmd {
		case "exit", "quit", "q":
			fmt.Printf("\n  %s👋 Hasta luego%s\n\n", ui.Sand, ui.Reset)
			return
		case "help", "h", "?":
			printHelp(state)
		case "clear":
			fmt.Print("\033[H\033[2J")
			ui.Banner(Version)
		case "search", "s":
			handleSearch(state, args)
		case "law", "l":
			handleLaw(state, args)
		case "article", "art", "a":
			handleArticle(state, args)
		case "index", "i":
			handleIndex(state, args)
		case "metadata", "meta", "m":
			handleMetadata(state, args)
		case "analysis":
			handleAnalysis(state, args)
		case "today", "t":
			handleToday(state, args)
		case "borme":
			handleBorme(state, args)
		case "back", "b":
			state.currentLaw = ""
			state.lawTitle = ""
			state.index = nil
			fmt.Printf("  %s← Vuelto al nivel raíz%s\n", ui.Sand, ui.Reset)
		default:
			if state.currentLaw != "" {
				handleArticle(state, parts)
			} else {
				ui.Error(fmt.Sprintf("Comando desconocido: %s (escribe 'help')", cmd))
			}
		}
		fmt.Println()
	}
}

func printHelp(state *REPLState) {
	fmt.Println()
	ui.Divider()
	fmt.Printf("  %s%sCOMANDOS%s\n\n", ui.Bold, ui.Orange, ui.Reset)

	fmt.Printf("  %ssearch%s %s<query>%s         Buscar legislación\n", ui.Bold, ui.Reset, ui.Sand, ui.Reset)
	fmt.Printf("  %s%s                       Ej: search compraventa participaciones%s\n", ui.Dim, ui.Sand, ui.Reset)
	fmt.Printf("  %s%s                       Ej: search titulo:sociedades capital%s\n\n", ui.Dim, ui.Sand, ui.Reset)

	fmt.Printf("  %slaw%s %s<ID|número>%s        Seleccionar una ley\n", ui.Bold, ui.Reset, ui.Sand, ui.Reset)
	fmt.Printf("  %s%s                       Ej: law BOE-A-2010-10544  o  law 3%s\n\n", ui.Dim, ui.Sand, ui.Reset)

	fmt.Printf("  %sarticle%s %s<id>%s           Leer artículo de la ley actual\n", ui.Bold, ui.Reset, ui.Sand, ui.Reset)
	fmt.Printf("  %s%s                       Ej: article a107  o  art 236%s\n\n", ui.Dim, ui.Sand, ui.Reset)

	fmt.Printf("  %sindex%s %s[filtro]%s         Estructura de la ley actual\n", ui.Bold, ui.Reset, ui.Sand, ui.Reset)
	fmt.Printf("  %smetadata%s               Metadatos de la ley\n", ui.Bold, ui.Reset)
	fmt.Printf("  %sanalysis%s               Modificaciones y referencias\n\n", ui.Bold, ui.Reset)

	fmt.Printf("  %stoday%s %s[YYYYMMDD]%s      Sumario del BOE\n", ui.Bold, ui.Reset, ui.Sand, ui.Reset)
	fmt.Printf("  %sborme%s %s[YYYYMMDD]%s      Sumario del BORME\n\n", ui.Bold, ui.Reset, ui.Sand, ui.Reset)

	fmt.Printf("  %sback%s                   Deseleccionar ley\n", ui.Bold, ui.Reset)
	fmt.Printf("  %sclear%s                  Limpiar pantalla\n", ui.Bold, ui.Reset)
	fmt.Printf("  %sexit%s                   Salir\n", ui.Bold, ui.Reset)
	ui.Divider()

	if state.currentLaw != "" {
		fmt.Printf("\n  %s📋 Ley actual: %s%s%s — %s%s\n",
			ui.Sand, ui.Amber, state.currentLaw, ui.Sand, state.lawTitle, ui.Reset)
	}
}

func handleSearch(state *REPLState, args []string) {
	if len(args) == 0 {
		ui.Info("Uso: search <query>")
		fmt.Printf("  %sEjemplos: search ley de sociedades de capital%s\n", ui.Dim, ui.Reset)
		fmt.Printf("  %s          search lsc%s\n", ui.Dim, ui.Reset)
		fmt.Printf("  %s          search compraventa participaciones%s\n", ui.Dim, ui.Reset)
		return
	}

	query := strings.Join(args, " ")
	fmt.Printf("\n  %s🔍 Buscando: %s%s%s\n\n", ui.Sand, ui.Cream, query, ui.Reset)

	items, source, err := state.client.SmartSearch(query, 10)
	if err != nil {
		ui.Error(fmt.Sprintf("%v", err))
		return
	}

	// If SmartSearch returned few/no results and we have semantic index, try semantic search
	if len(items) < 3 && state.semanticIndex != nil && state.embedClient != nil && state.embedClient.IsAvailable() {
		if source != "alias" && source != "fuzzy" && source != "partial" {
			queryVec, embedErr := state.embedClient.EmbedQuery(query)
			if embedErr == nil {
				semResults := state.semanticIndex.Search(queryVec, 10)
				if len(semResults) > 0 {
					// Merge semantic results with existing
					seen := make(map[string]bool)
					for _, item := range items {
						seen[item.ID] = true
					}
					for _, sr := range semResults {
						if seen[sr.ID] || sr.Score < 0.35 { // threshold (raised from 0.3)
							continue
						}
						seen[sr.ID] = true
						items = append(items, api.SearchResultItem{
							ID:     sr.ID,
							Title:  sr.Title,
							Score:  int(sr.Score * 100),
							Source: "semantic",
						})
					}
					if source == "smart" || source == "" {
						source = "semantic"
					}
				}
			}
		}
	}

	if len(items) == 0 {
		fmt.Printf("  %sNo se encontraron resultados%s\n", ui.Sand, ui.Reset)
		ui.Hint("Prueba con menos palabras o usa titulo: o texto: como prefijo")
		return
	}

	switch source {
	case "alias":
		fmt.Printf("  %s⚡ Coincidencia directa%s\n\n", ui.Gold, ui.Reset)
	case "fuzzy":
		if len(items) > 0 && items[0].Source != "" {
			fmt.Printf("  %s🔮 Quizás quisiste decir: %s%s%s\n\n", ui.Sand, ui.Cream, items[0].Title, ui.Reset)
		}
	case "partial":
		fmt.Printf("  %s🎯 Mejor coincidencia%s\n\n", ui.Gold, ui.Reset)
	case "semantic":
		fmt.Printf("  %s🧠 Búsqueda semántica%s\n\n", ui.Sand, ui.Reset)
	}

	state.lastSearch = nil
	for i, item := range items {
		fmt.Print(ui.ResultHeader(i+1, item.ID, item.Vigente))
		fmt.Printf(" %s%s%s\n", ui.Cream, truncateStr(item.Title, 120), ui.Reset)
		if item.Rango.Text != "" || item.Date != "" {
			date := formatDisplayDate(item.Date)
			fmt.Printf("        %s%s — %s%s\n", ui.Dim, item.Rango.Text, date, ui.Reset)
		}
		state.lastSearch = append(state.lastSearch, searchResult{ID: item.ID, Title: item.Title})
	}

	ui.Hint("Usa 'law <número>' para seleccionar una ley")
}

func handleLaw(state *REPLState, args []string) {
	if len(args) == 0 {
		if state.currentLaw != "" {
			fmt.Printf("  %s📋 %s%s%s — %s%s\n", ui.Sand, ui.Amber, state.currentLaw, ui.Sand, state.lawTitle, ui.Reset)
			return
		}
		ui.Info("Uso: law <BOE-ID> o law <número de búsqueda>")
		return
	}

	id := args[0]

	if num, err := strconv.Atoi(id); err == nil {
		if state.lastSearch != nil && num >= 1 && num <= len(state.lastSearch) {
			id = state.lastSearch[num-1].ID
		} else {
			ui.Warning("No hay búsqueda previa o número fuera de rango")
			return
		}
	}

	fmt.Printf("  %s📋 Cargando %s%s%s...%s\n", ui.Sand, ui.Amber, id, ui.Sand, ui.Reset)

	meta, err := state.client.GetLawMetadata(id)
	if err != nil {
		idx, err2 := state.client.GetLawIndex(id)
		if err2 != nil {
			ui.Error(fmt.Sprintf("%v", err))
			return
		}
		state.currentLaw = id
		state.lawTitle = id
		parseAndStoreIndex(state, idx)
		ui.Success(fmt.Sprintf("%s (%d bloques)", id, len(state.index)))
		return
	}

	var metaResp struct {
		Data struct {
			Metadatos struct {
				Title string `json:"titulo"`
			} `json:"metadatos"`
		} `json:"data"`
	}
	title := id
	if err := json.Unmarshal(meta, &metaResp); err == nil && metaResp.Data.Metadatos.Title != "" {
		title = metaResp.Data.Metadatos.Title
	}

	idx, err := state.client.GetLawIndex(id)
	if err == nil {
		parseAndStoreIndex(state, idx)
	}

	state.currentLaw = id
	state.lawTitle = title

	ui.Success(truncateStr(title, 80))
	if state.index != nil {
		artCount := 0
		for _, e := range state.index {
			if strings.HasPrefix(strings.ToLower(e.Title), "art") {
				artCount++
			}
		}
		fmt.Printf("     %s%d bloques, ~%d artículos%s\n", ui.Sand, len(state.index), artCount, ui.Reset)
	}
	ui.Hint("'index' para ver estructura, 'article <id>' para leer, 'art <número>'")
}

func handleArticle(state *REPLState, args []string) {
	if state.currentLaw == "" {
		ui.Warning("Primero selecciona una ley con 'law <ID>'")
		return
	}
	if len(args) == 0 {
		ui.Info("Uso: article <block_id> o art <número>")
		return
	}

	blockID := args[0]

	// Smart article lookup by number
	if num, err := strconv.Atoi(blockID); err == nil && state.index != nil {
		targets := []string{
			fmt.Sprintf("art%d", num),
			fmt.Sprintf("a%d", num),
			fmt.Sprintf("Art%d", num),
		}
		found := false
		for _, e := range state.index {
			for _, t := range targets {
				if strings.EqualFold(e.ID, t) {
					blockID = e.ID
					found = true
					break
				}
			}
			if found {
				break
			}
		}
	}

	xmlData, err := state.client.GetLawBlock(state.currentLaw, blockID)
	if err != nil {
		ui.Error(fmt.Sprintf("%v", err))
		return
	}

	text, err := api.BlockToText(xmlData)
	if err != nil || text == "" {
		if strings.Contains(string(xmlData), "404") {
			ui.Error(fmt.Sprintf("Bloque '%s' no encontrado. Usa 'index' para ver IDs.", blockID))
			return
		}
		ui.Error(fmt.Sprintf("Error extrayendo texto: %v", err))
		return
	}

	fmt.Println()
	for _, l := range strings.Split(text, "\n") {
		switch {
		case strings.HasPrefix(l, "## "):
			ui.ArticleTitle(strings.TrimPrefix(l, "## "))
		case strings.HasPrefix(l, "### "):
			ui.ArticleHeading(strings.TrimPrefix(l, "### "))
		case strings.HasPrefix(l, "[Vigente"):
			ui.ArticleMeta(l)
		case strings.HasPrefix(l, "Se modifica"):
			ui.ArticleMeta(l)
		case l != "":
			ui.ArticleText(l)
		}
	}
}

func handleIndex(state *REPLState, args []string) {
	if state.currentLaw == "" {
		ui.Warning("Primero selecciona una ley con 'law <ID>'")
		return
	}
	if state.index == nil {
		ui.Warning("No hay índice cargado")
		return
	}

	filter := ""
	if len(args) > 0 {
		filter = strings.ToLower(strings.Join(args, " "))
	}

	fmt.Println()
	count := 0
	for _, entry := range state.index {
		if entry.Title == "" {
			continue
		}
		if filter != "" && !strings.Contains(strings.ToLower(entry.Title), filter) && !strings.Contains(strings.ToLower(entry.ID), filter) {
			continue
		}

		lower := strings.ToLower(entry.Title)
		switch {
		case strings.HasPrefix(lower, "libro") || strings.HasPrefix(lower, "título") || strings.HasPrefix(lower, "title"):
			ui.IndexBook(entry.ID, entry.Title)
		case strings.HasPrefix(lower, "capítulo") || strings.HasPrefix(lower, "sección"):
			ui.IndexChapter(entry.ID, entry.Title)
		case strings.HasPrefix(lower, "art"):
			ui.IndexArticle(entry.ID, entry.Title)
		default:
			fmt.Printf("  %s%-17s %s%s\n", ui.Sand, entry.ID, entry.Title, ui.Reset)
		}
		count++

		if count >= 80 && filter == "" {
			ui.Hint(fmt.Sprintf("... y %d bloques más. Usa 'index <filtro>' para filtrar.", len(state.index)-count))
			break
		}
	}

	if count == 0 {
		fmt.Printf("  %sNo se encontraron bloques con ese filtro%s\n", ui.Sand, ui.Reset)
	}
}

func handleMetadata(state *REPLState, args []string) {
	id := state.currentLaw
	if len(args) > 0 {
		id = args[0]
	}
	if id == "" {
		ui.Warning("Primero selecciona una ley o pasa un ID")
		return
	}

	result, err := state.client.GetLawMetadata(id)
	if err != nil {
		ui.Error(fmt.Sprintf("%v", err))
		return
	}

	var pretty interface{}
	if err := json.Unmarshal(result, &pretty); err == nil {
		out, _ := json.MarshalIndent(pretty, "  ", "  ")
		fmt.Printf("  %s%s%s\n", ui.Cream, string(out), ui.Reset)
	}
}

func handleAnalysis(state *REPLState, args []string) {
	id := state.currentLaw
	if len(args) > 0 {
		id = args[0]
	}
	if id == "" {
		ui.Warning("Primero selecciona una ley o pasa un ID")
		return
	}

	result, err := state.client.GetLawAnalysis(id)
	if err != nil {
		ui.Error(fmt.Sprintf("%v", err))
		return
	}

	var pretty interface{}
	if err := json.Unmarshal(result, &pretty); err == nil {
		out, _ := json.MarshalIndent(pretty, "  ", "  ")
		fmt.Printf("  %s%s%s\n", ui.Cream, string(out), ui.Reset)
	}
}

func handleToday(state *REPLState, args []string) {
	date := ""
	if len(args) > 0 {
		date = args[0]
	}

	result, err := state.client.GetDailySummary(date)
	if err != nil {
		ui.Error(fmt.Sprintf("%v", err))
		return
	}

	printDailySummary(result)
}

func handleBorme(state *REPLState, args []string) {
	date := ""
	if len(args) > 0 {
		date = args[0]
	}

	result, err := state.client.GetBORMESummary(date)
	if err != nil {
		ui.Error(fmt.Sprintf("%v", err))
		return
	}

	printDailySummary(result)
}

func printDailySummary(data json.RawMessage) {
	var resp struct {
		Data struct {
			Sumario struct {
				Metadatos struct {
					Date string `json:"fecha_publicacion"`
				} `json:"metadatos"`
				Diario []struct {
					Numero  string `json:"numero"`
					Seccion []struct {
						Nombre       string `json:"nombre"`
						Departamento []struct {
							Nombre   string `json:"nombre"`
							Epigrafe []struct {
								Nombre string      `json:"nombre"`
								Item   interface{} `json:"item"`
							} `json:"epigrafe"`
						} `json:"departamento"`
					} `json:"seccion"`
				} `json:"diario"`
			} `json:"sumario"`
		} `json:"data"`
	}

	if err := json.Unmarshal(data, &resp); err != nil {
		var pretty interface{}
		if err := json.Unmarshal(data, &pretty); err == nil {
			out, _ := json.MarshalIndent(pretty, "  ", "  ")
			fmt.Printf("  %s%s%s\n", ui.Cream, string(out), ui.Reset)
		}
		return
	}

	date := formatDisplayDate(resp.Data.Sumario.Metadatos.Date)
	ui.SummaryDate(date)

	for _, diario := range resp.Data.Sumario.Diario {
		for _, seccion := range diario.Seccion {
			ui.SummarySection(seccion.Nombre)
			for _, dept := range seccion.Departamento {
				ui.SummaryDept(dept.Nombre)
				for _, epi := range dept.Epigrafe {
					if epi.Nombre != "" {
						fmt.Printf("      %s📌 %s%s\n", ui.Gold, epi.Nombre, ui.Reset)
					}
					items := extractItems(epi.Item)
					for _, item := range items {
						ui.SummaryItem(truncateStr(item.Title, 70), item.ID)
					}
				}
			}
			fmt.Println()
		}
	}
}

type summaryItem struct {
	ID    string
	Title string
}

func extractItems(raw interface{}) []summaryItem {
	var items []summaryItem
	switch v := raw.(type) {
	case map[string]interface{}:
		items = append(items, parseSummaryItem(v))
	case []interface{}:
		for _, item := range v {
			if m, ok := item.(map[string]interface{}); ok {
				items = append(items, parseSummaryItem(m))
			}
		}
	}
	return items
}

func parseSummaryItem(m map[string]interface{}) summaryItem {
	id, _ := m["identificador"].(string)
	title, _ := m["titulo"].(string)
	return summaryItem{ID: id, Title: title}
}

func parseAndStoreIndex(state *REPLState, data json.RawMessage) {
	var resp struct {
		Data []struct {
			Bloque []struct {
				ID    string `json:"id"`
				Title string `json:"titulo"`
			} `json:"bloque"`
		} `json:"data"`
	}

	if err := json.Unmarshal(data, &resp); err != nil {
		return
	}

	state.index = nil
	for _, d := range resp.Data {
		for _, b := range d.Bloque {
			state.index = append(state.index, indexEntry{ID: b.ID, Title: b.Title})
		}
	}
}

func shortLawName(title, id string) string {
	lower := strings.ToLower(title)
	switch {
	case strings.Contains(lower, "código civil"):
		return "CC"
	case strings.Contains(lower, "sociedades de capital"):
		return "LSC"
	case strings.Contains(lower, "general tributaria"):
		return "LGT"
	case strings.Contains(lower, "estatuto de los trabajadores"):
		return "ET"
	case strings.Contains(lower, "código de comercio"):
		return "CCom"
	case strings.Contains(lower, "enjuiciamiento civil"):
		return "LEC"
	case strings.Contains(lower, "modificaciones estructurales"):
		return "LME"
	case strings.Contains(lower, "defensa de la competencia"):
		return "LDC"
	case strings.Contains(lower, "impuesto sobre sociedades"):
		return "LIS"
	default:
		if len(id) > 20 {
			return id[:20]
		}
		return id
	}
}

func formatDisplayDate(yyyymmdd string) string {
	if len(yyyymmdd) != 8 {
		return yyyymmdd
	}
	return yyyymmdd[6:8] + "/" + yyyymmdd[4:6] + "/" + yyyymmdd[0:4]
}

func truncateStr(s string, max int) string {
	if len(s) > max {
		return s[:max] + "..."
	}
	return s
}

func init() {
	shellCmd := &cobra.Command{
		Use:   "shell",
		Short: "Start interactive shell (REPL)",
		Run: func(cmd *cobra.Command, args []string) {
			StartREPL()
		},
	}
	rootCmd.AddCommand(shellCmd)
}

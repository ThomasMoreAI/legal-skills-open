package cmd

import (
	"fmt"
	"strings"

	"github.com/spf13/cobra"
	"github.com/zepelinmad/boe-cli/internal/api"
	"github.com/zepelinmad/boe-cli/internal/output"
)

var searchCmd = &cobra.Command{
	Use:   "search [query]",
	Short: "Search consolidated legislation",
	Long: `Search the BOE consolidated legislation database.

The query uses BOE's advanced search syntax. Available fields:
  titulo:TEXT              Search in law title
  texto:TEXT               Full-text search in law content
  ambito@codigo:N          Scope (1=State, 2=Autonomous)
  departamento@codigo:N    Department code
  rango@codigo:N           Legal rank code
  materia@codigo:N         Subject matter code
  estado_consolidacion@codigo:N  Status code

Combine with: and, or, not, parentheses

Examples:
  boe search "titulo:sociedades capital"
  boe search "titulo:arrendamientos and ambito@codigo:1"
  boe search "texto:compraventa participaciones"
  boe search "titulo:tributaria and rango@codigo:1010"   # 1010 = Ley
  boe search --recent --limit 5                          # Recently updated laws
  boe search --raw '{"query":{"query_string":{"query":"titulo:civil"}}}'
  boe search --raw -                                     # Read raw JSON query from stdin`,
	RunE: func(cmd *cobra.Command, args []string) error {
		client := api.NewClient()
		limit, _ := cmd.Flags().GetInt("limit")
		offset, _ := cmd.Flags().GetInt("offset")
		from, _ := cmd.Flags().GetString("from")
		to, _ := cmd.Flags().GetString("to")
		rawQuery, _ := cmd.Flags().GetString("raw")
		recent, _ := cmd.Flags().GetBool("recent")
		legacy, _ := cmd.Flags().GetBool("legacy")

		// Raw query mode — support "-" to read from stdin
		if rawQuery == "-" {
			stdinData, ok := output.ReadStdinAll()
			if !ok {
				return fmt.Errorf("--raw -: no data on stdin\n  Usage: cat query.json | boe search --raw -")
			}
			rawQuery = stdinData
		}
		if rawQuery != "" {
			result, err := client.SearchRaw(rawQuery, limit, offset)
			if err != nil {
				return wrapSearchError(err)
			}
			return output.PrintRawJSON(cmd, result)
		}

		// Recent mode (no query, just list recent updates)
		if recent || len(args) == 0 {
			result, err := client.ListRecentLegislation(limit, offset)
			if err != nil {
				return wrapSearchError(err)
			}
			return output.PrintRawJSON(cmd, result)
		}

		// Legacy mode — use old search behavior
		if legacy || from != "" || to != "" || offset > 0 {
			result, err := client.SearchLegislation(args[0], limit, offset, from, to)
			if err != nil {
				return wrapSearchError(err)
			}
			return output.PrintRawJSON(cmd, result)
		}

		// Smart search (default)
		items, _, err := client.SmartSearch(args[0], limit)
		if err != nil {
			return wrapSearchError(err)
		}
		return output.PrintJSON(cmd, items)
	},
}

func wrapSearchError(err error) error {
	msg := err.Error()
	if strings.Contains(msg, "request failed") {
		return fmt.Errorf("%w\n  Check connectivity. BOE API: https://www.boe.es/datosabiertos/api", err)
	}
	return err
}

func init() {
	searchCmd.Flags().IntP("limit", "l", 10, "Maximum number of results")
	searchCmd.Flags().IntP("offset", "o", 0, "Offset for pagination")
	searchCmd.Flags().String("from", "", "Filter by update date from (YYYYMMDD)")
	searchCmd.Flags().String("to", "", "Filter by update date to (YYYYMMDD)")
	searchCmd.Flags().String("raw", "", "Raw JSON query (advanced, use \"-\" to read from stdin)")
	searchCmd.Flags().Bool("recent", false, "List recently updated laws (no query needed)")
	searchCmd.Flags().Bool("legacy", false, "Use legacy search (raw BOE API, no smart features)")
	rootCmd.AddCommand(searchCmd)
}

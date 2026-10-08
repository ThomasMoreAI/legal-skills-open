package cmd

import (
	"encoding/json"
	"fmt"
	"strings"

	"github.com/spf13/cobra"
	"github.com/zepelinmad/boe-cli/internal/api"
	"github.com/zepelinmad/boe-cli/internal/output"
)

var lawCmd = &cobra.Command{
	Use:   "law [id]",
	Short: "Access a specific law by its BOE identifier",
	Long: `Access consolidated legislation by BOE identifier.

Common law identifiers:
  BOE-A-1889-4763    Código Civil
  BOE-A-2010-10544   Ley de Sociedades de Capital
  BOE-A-2003-23186   Ley General Tributaria
  BOE-A-2015-11430   Ley de Enjuiciamiento Civil (reforma)
  BOE-A-1885-6627    Código de Comercio

The law ID can also be piped via stdin:
  echo "BOE-A-1889-4763" | boe law --index

Examples:
  boe law BOE-A-1889-4763 --index              # Structure of Código Civil
  boe law BOE-A-1889-4763 --article a1255      # Article 1255
  boe law BOE-A-1889-4763 --article a1255 --text  # Human-readable text
  boe law BOE-A-1889-4763 --block tpreliminar  # Título Preliminar
  boe law BOE-A-1889-4763 --metadata           # Law metadata
  boe law BOE-A-1889-4763 --analysis           # Modifications & references`,
	Args: cobra.MaximumNArgs(1),
	RunE: func(cmd *cobra.Command, args []string) error {
		client := api.NewClient()

		// Resolve law ID from args or stdin
		var id string
		if len(args) == 1 {
			id = args[0]
		} else {
			stdinID, ok := output.ReadStdinLine()
			if !ok {
				return fmt.Errorf("law ID required\n  Usage: boe law <id> [flags]\n  Example: boe law BOE-A-1889-4763 --index\n  Find IDs: boe search \"<query>\"")
			}
			id = stdinID
		}

		showIndex, _ := cmd.Flags().GetBool("index")
		article, _ := cmd.Flags().GetString("article")
		block, _ := cmd.Flags().GetString("block")
		metadata, _ := cmd.Flags().GetBool("metadata")
		analysis, _ := cmd.Flags().GetBool("analysis")
		textMode, _ := cmd.Flags().GetBool("text")

		// Determine what to fetch
		switch {
		case showIndex:
			result, err := client.GetLawIndex(id)
			if err != nil {
				return wrapLawError(err, id)
			}
			return output.PrintRawJSON(cmd, result)

		case article != "":
			return fetchBlock(cmd, client, id, article, textMode)

		case block != "":
			return fetchBlock(cmd, client, id, block, textMode)

		case metadata:
			result, err := client.GetLawMetadata(id)
			if err != nil {
				return wrapLawError(err, id)
			}
			return output.PrintRawJSON(cmd, result)

		case analysis:
			result, err := client.GetLawAnalysis(id)
			if err != nil {
				return wrapLawError(err, id)
			}
			return output.PrintRawJSON(cmd, result)

		default:
			// Default: show index
			result, err := client.GetLawIndex(id)
			if err != nil {
				return wrapLawError(err, id)
			}
			return output.PrintRawJSON(cmd, result)
		}
	},
}

func wrapLawError(err error, id string) error {
	msg := err.Error()
	if strings.Contains(msg, "404") || strings.Contains(msg, "400") || strings.Contains(msg, "non-JSON response") {
		return fmt.Errorf("%w\n  Invalid or unknown law ID: %s\n  Find valid IDs: boe search \"<query>\"", err, id)
	}
	if strings.Contains(msg, "request failed") {
		return fmt.Errorf("%w\n  Check connectivity. BOE API: https://www.boe.es/datosabiertos/api", err)
	}
	return err
}

func fetchBlock(cmd *cobra.Command, client *api.Client, id, blockID string, textMode bool) error {
	xmlData, err := client.GetLawBlock(id, blockID)
	if err != nil {
		return wrapLawError(err, id)
	}

	// Extract human-readable text
	text, textErr := api.BlockToText(xmlData)

	if textMode {
		if textErr != nil {
			return fmt.Errorf("extracting text: %w", textErr)
		}
		output.PrintText(text)
		return nil
	}

	// JSON output with structured data
	result := map[string]interface{}{
		"id":       id,
		"block_id": blockID,
	}
	if textErr == nil && text != "" {
		result["text"] = text
	}
	jsonData, err := json.Marshal(result)
	if err != nil {
		return err
	}
	return output.PrintRawJSON(cmd, json.RawMessage(jsonData))
}

func init() {
	lawCmd.Flags().Bool("index", false, "Show structural index (titles, chapters, articles)")
	lawCmd.Flags().StringP("article", "a", "", "Get a specific article by block ID (e.g., a1255, art42)")
	lawCmd.Flags().StringP("block", "b", "", "Get a specific block (e.g., tpreliminar, ci)")
	lawCmd.Flags().Bool("metadata", false, "Show law metadata")
	lawCmd.Flags().Bool("analysis", false, "Show modifications and references analysis")
	lawCmd.Flags().BoolP("text", "t", false, "Output human-readable text instead of JSON")
	rootCmd.AddCommand(lawCmd)
}

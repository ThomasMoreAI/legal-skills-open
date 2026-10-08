package cmd

import (
	"os"

	"github.com/spf13/cobra"
	"github.com/zepelinmad/boe-cli/internal/ui"
)

var rootCmd = &cobra.Command{
	Use:           "boe",
	Short:         "CLI for Spain's Boletín Oficial del Estado (BOE)",
	SilenceUsage:  true,
	SilenceErrors: true,
	Long: `boe-cli — Navigate Spanish legislation from the command line.

Access consolidated legislation, daily publications, and legal analysis
from the BOE (Boletín Oficial del Estado) open data API.

Built for AI agents and legal professionals.
Use "boe shell" to start the interactive REPL.`,
}

func Execute() error {
	return rootCmd.Execute()
}

func init() {
	rootCmd.PersistentFlags().BoolP("pretty", "p", false, "Pretty-print JSON output")
	rootCmd.PersistentFlags().Bool("no-color", false, "Disable colored output (also: NO_COLOR env var)")
	rootCmd.PersistentPreRunE = func(cmd *cobra.Command, args []string) error {
		noColor, _ := rootCmd.PersistentFlags().GetBool("no-color")
		if noColor || os.Getenv("NO_COLOR") != "" {
			ui.DisableColors()
		}
		return nil
	}
}

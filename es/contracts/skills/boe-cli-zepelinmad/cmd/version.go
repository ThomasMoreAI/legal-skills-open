package cmd

import (
	"encoding/json"
	"fmt"
	"os"

	"github.com/spf13/cobra"
)

var Version = "0.7.0"

var versionCmd = &cobra.Command{
	Use:   "version",
	Short: "Print the version",
	Long: `Print the version of boe-cli.

Examples:
  boe version          # Human-readable: boe-cli v0.6.0
  boe version --json   # Machine-readable: {"version":"0.6.0"}`,
	Run: func(cmd *cobra.Command, args []string) {
		jsonOut, _ := cmd.Flags().GetBool("json")
		if jsonOut {
			out, _ := json.Marshal(map[string]string{"version": Version})
			fmt.Fprintln(os.Stdout, string(out))
			return
		}
		fmt.Printf("boe-cli v%s\n", Version)
	},
}

func init() {
	versionCmd.Flags().Bool("json", false, "Output version as JSON")
	rootCmd.AddCommand(versionCmd)
}

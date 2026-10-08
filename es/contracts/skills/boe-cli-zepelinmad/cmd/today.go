package cmd

import (
	"fmt"
	"strings"
	"time"

	"github.com/spf13/cobra"
	"github.com/zepelinmad/boe-cli/internal/api"
	"github.com/zepelinmad/boe-cli/internal/output"
)

var todayCmd = &cobra.Command{
	Use:   "today",
	Short: "Get today's BOE summary (or a specific date)",
	Long: `Fetch the BOE daily summary.

Examples:
  boe today                    # Today's BOE
  boe today --date 20260321    # Specific date
  boe today --borme            # Today's BORME (mercantile)
  boe today -p                 # Pretty-printed`,
	RunE: func(cmd *cobra.Command, args []string) error {
		client := api.NewClient()
		date, _ := cmd.Flags().GetString("date")
		borme, _ := cmd.Flags().GetBool("borme")

		if date == "" {
			date = time.Now().Format("20060102")
		}

		var result []byte
		var err error

		if borme {
			result, err = client.GetBORMESummary(date)
		} else {
			result, err = client.GetDailySummary(date)
		}

		if err != nil {
			return wrapTodayError(err, date)
		}

		return output.PrintRawJSON(cmd, result)
	},
}

func wrapTodayError(err error, date string) error {
	msg := err.Error()
	if strings.Contains(msg, "400") || strings.Contains(msg, "non-JSON response") {
		return fmt.Errorf("%w\n  Invalid date: %s — use YYYYMMDD format: boe today --date %s", err, date, time.Now().Format("20060102"))
	}
	if strings.Contains(msg, "404") {
		return fmt.Errorf("%w\n  No BOE published for date: %s\n  Use YYYYMMDD format: boe today --date %s", err, date, time.Now().Format("20060102"))
	}
	if strings.Contains(msg, "request failed") {
		return fmt.Errorf("%w\n  Check connectivity. BOE API: https://www.boe.es/datosabiertos/api", err)
	}
	return err
}

func init() {
	todayCmd.Flags().StringP("date", "d", "", "Date in YYYYMMDD format (default: today)")
	todayCmd.Flags().Bool("borme", false, "Fetch BORME (mercantile) instead of BOE")
	rootCmd.AddCommand(todayCmd)
}

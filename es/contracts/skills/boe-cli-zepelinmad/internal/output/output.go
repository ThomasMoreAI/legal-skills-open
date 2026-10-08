package output

import (
	"encoding/json"
	"fmt"
	"os"

	"github.com/spf13/cobra"
)

// PrintJSON outputs JSON to stdout, optionally pretty-printed
func PrintJSON(cmd *cobra.Command, data interface{}) error {
	pretty, _ := cmd.Flags().GetBool("pretty")

	var out []byte
	var err error

	if pretty {
		out, err = json.MarshalIndent(data, "", "  ")
	} else {
		out, err = json.Marshal(data)
	}

	if err != nil {
		return fmt.Errorf("encoding JSON: %w", err)
	}

	fmt.Fprintln(os.Stdout, string(out))
	return nil
}

// PrintRawJSON outputs raw JSON bytes to stdout, optionally pretty-printed
func PrintRawJSON(cmd *cobra.Command, data json.RawMessage) error {
	pretty, _ := cmd.Flags().GetBool("pretty")

	if pretty {
		var parsed interface{}
		if err := json.Unmarshal(data, &parsed); err != nil {
			// Just print raw if we can't parse
			fmt.Fprintln(os.Stdout, string(data))
			return nil
		}
		out, err := json.MarshalIndent(parsed, "", "  ")
		if err != nil {
			fmt.Fprintln(os.Stdout, string(data))
			return nil
		}
		fmt.Fprintln(os.Stdout, string(out))
		return nil
	}

	fmt.Fprintln(os.Stdout, string(data))
	return nil
}

// PrintText outputs plain text to stdout
func PrintText(text string) {
	fmt.Fprintln(os.Stdout, text)
}

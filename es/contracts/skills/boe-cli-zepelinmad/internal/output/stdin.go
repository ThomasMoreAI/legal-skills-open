package output

import (
	"bufio"
	"os"
	"strings"
)

// ReadStdinLine reads a single trimmed line from stdin.
// Returns the line and true if stdin is a pipe with content.
// Returns empty string and false if stdin is a terminal or empty.
func ReadStdinLine() (string, bool) {
	if isTerminalStdin() {
		return "", false
	}
	scanner := bufio.NewScanner(os.Stdin)
	if scanner.Scan() {
		line := strings.TrimSpace(scanner.Text())
		if line != "" {
			return line, true
		}
	}
	return "", false
}

// ReadStdinAll reads all of stdin as a single trimmed string.
// Returns the content and true if stdin is a pipe with content.
// Returns empty string and false if stdin is a terminal or empty.
func ReadStdinAll() (string, bool) {
	if isTerminalStdin() {
		return "", false
	}
	var sb strings.Builder
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		sb.WriteString(scanner.Text())
		sb.WriteString("\n")
	}
	result := strings.TrimSpace(sb.String())
	if result == "" {
		return "", false
	}
	return result, true
}

func isTerminalStdin() bool {
	fi, err := os.Stdin.Stat()
	if err != nil {
		return true
	}
	return (fi.Mode() & os.ModeCharDevice) != 0
}

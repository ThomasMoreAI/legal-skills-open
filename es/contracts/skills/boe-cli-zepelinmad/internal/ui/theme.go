package ui

import "fmt"

// Warm palette ANSI colors (vars so DisableColors can clear them)
var (
	Reset     = "\033[0m"
	Bold      = "\033[1m"
	Dim       = "\033[2m"
	Italic    = "\033[3m"

	// Warm palette
	Amber     = "\033[38;5;214m" // Primary accent
	Orange    = "\033[38;5;208m" // Headers
	Gold      = "\033[38;5;220m" // Highlights
	Terracota = "\033[38;5;167m" // Errors, warnings
	Cream     = "\033[38;5;223m" // Body text
	Sage      = "\033[38;5;108m" // Success, secondary
	Sand      = "\033[38;5;180m" // Muted text
	BgDark    = "\033[48;5;235m" // Background accent
)

// DisableColors clears all ANSI escape codes. Call when --no-color or NO_COLOR is set.
func DisableColors() {
	Reset = ""
	Bold = ""
	Dim = ""
	Italic = ""
	Amber = ""
	Orange = ""
	Gold = ""
	Terracota = ""
	Cream = ""
	Sage = ""
	Sand = ""
	BgDark = ""
}

// Banner prints the ASCII art banner
func Banner(version string) {
	fmt.Println()
	fmt.Print(Orange)
	fmt.Println(`    ____  ____  ______`)
	fmt.Println(`   / __ )/ __ \/ ____/`)
	fmt.Println(`  / __  / / / / __/   `)
	fmt.Println(` / /_/ / /_/ / /___   `)
	fmt.Print(Amber)
	fmt.Println(`/_____/\____/_____/   `)
	fmt.Println()
	fmt.Printf("%s%s  Boletín Oficial del Estado%s\n", Bold, Cream, Reset)
	fmt.Printf("%s  Legislación española consolidada — v%s%s\n", Sand, version, Reset)
	fmt.Println()
	fmt.Printf("%s  Escribe %shelp%s%s para ver comandos, %sexit%s%s para salir%s\n",
		Dim, Bold, Reset, Dim, Bold, Reset, Dim, Reset)
	fmt.Println()
}

// Section prints a section header
func Section(icon, text string) {
	fmt.Printf("  %s%s %s%s\n", Orange, icon, text, Reset)
}

// Success prints a success message
func Success(text string) {
	fmt.Printf("  %s✅ %s%s\n", Sage, text, Reset)
}

// Error prints an error message
func Error(text string) {
	fmt.Printf("  %s❌ %s%s\n", Terracota, text, Reset)
}

// Warning prints a warning message
func Warning(text string) {
	fmt.Printf("  %s⚠️  %s%s\n", Gold, text, Reset)
}

// Info prints an info message
func Info(text string) {
	fmt.Printf("  %sℹ️  %s%s\n", Sand, text, Reset)
}

// Hint prints a hint/tip
func Hint(text string) {
	fmt.Printf("\n  %s💡 %s%s\n", Dim, text, Reset)
}

// ResultHeader prints a search result header
func ResultHeader(num int, id, vigente string) string {
	icon := Sage + "✅" + Reset
	if vigente == "S" {
		icon = Terracota + "⛔" + Reset
	}
	return fmt.Sprintf("  %s %s%2d.%s %s%-22s%s", icon, Bold, num, Reset, Amber, id, Reset)
}

// ArticleTitle formats an article title
func ArticleTitle(text string) {
	fmt.Printf("\n  %s%s📖 %s%s\n", Bold, Orange, text, Reset)
}

// ArticleHeading formats an article heading
func ArticleHeading(text string) {
	fmt.Printf("  %s%s%s%s\n", Bold, Cream, text, Reset)
}

// ArticleMeta formats metadata like vigency dates
func ArticleMeta(text string) {
	fmt.Printf("  %s%s%s\n", Sand, text, Reset)
}

// ArticleText formats regular article text
func ArticleText(text string) {
	fmt.Printf("  %s%s%s\n", Cream, text, Reset)
}

// LawPrompt returns the formatted prompt string
func LawPrompt(lawName string) string {
	if lawName == "" {
		return fmt.Sprintf("%s%sboe%s%s>%s ", Bold, Amber, Reset, Sand, Reset)
	}
	return fmt.Sprintf("%s%sboe%s %s[%s]%s%s>%s ", Bold, Amber, Reset, Gold, lawName, Reset, Sand, Reset)
}

// IndexBook formats a book/title in the index
func IndexBook(id, title string) {
	fmt.Printf("  %s📚 %-15s %s%s%s\n", Orange, id, Bold, title, Reset)
}

// IndexChapter formats a chapter/section in the index
func IndexChapter(id, title string) {
	fmt.Printf("    %s📂 %-13s %s%s\n", Sand, id, title, Reset)
}

// IndexArticle formats an article in the index
func IndexArticle(id, title string) {
	fmt.Printf("      %s📄 %-11s %s%s\n", Cream, id, title, Reset)
}

// SummaryDate formats the daily summary date
func SummaryDate(date string) {
	fmt.Printf("  %s%s📰 BOE — %s%s\n\n", Bold, Orange, date, Reset)
}

// SummarySection formats a section name
func SummarySection(name string) {
	fmt.Printf("  %s%s📋 %s%s\n", Bold, Amber, name, Reset)
}

// SummaryDept formats a department name
func SummaryDept(name string) {
	fmt.Printf("    %s🏛️  %s%s\n", Sand, name, Reset)
}

// SummaryItem formats a summary item
func SummaryItem(title, id string) {
	fmt.Printf("        %s• %s%s\n", Cream, title, Reset)
	fmt.Printf("          %s%s%s\n", Dim, id, Reset)
}

// Divider prints a subtle divider
func Divider() {
	fmt.Printf("  %s%s%s\n", Dim, "─────────────────────────────────────────", Reset)
}

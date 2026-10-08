package api

import (
	"sort"
	"strings"
)

// FuzzyMatch finds the closest alias match using Levenshtein distance
// Returns the BOE ID and the matched alias name, or empty if no close match found
func FuzzyMatch(query string, maxDistance int) (id string, matchedAlias string, distance int) {
	normalized := normalizeForAlias(query)
	if normalized == "" {
		return "", "", -1
	}

	type candidate struct {
		alias    string
		id       string
		distance int
	}

	var candidates []candidate

	for alias, boeID := range KnownLaws {
		d := levenshtein(normalized, alias)
		// Dynamic threshold: for short strings, allow less distance
		maxAllowed := maxDistance
		minLen := len(normalized)
		if len(alias) < minLen {
			minLen = len(alias)
		}
		// For very short aliases (2-3 chars like "cc", "et"), require exact match
		if len(alias) <= 3 && d > 0 {
			continue
		}
		// Scale threshold: max 1 edit per 4 chars, capped at maxDistance
		scaledMax := (minLen / 4) + 1
		if scaledMax > maxAllowed {
			scaledMax = maxAllowed
		}
		if d <= scaledMax && d > 0 { // d > 0 because exact matches are handled by LookupAlias
			candidates = append(candidates, candidate{alias, boeID, d})
		}
	}

	// Also check synonyms
	for synonym, expanded := range Synonyms {
		d := levenshtein(normalized, synonym)
		if len(synonym) <= 3 && d > 0 {
			continue
		}
		scaledMax := (len(synonym) / 4) + 1
		if scaledMax > maxDistance {
			scaledMax = maxDistance
		}
		if d <= scaledMax && d > 0 {
			// Resolve synonym to BOE ID
			if boeID, ok := KnownLaws[expanded]; ok {
				candidates = append(candidates, candidate{synonym + " → " + expanded, boeID, d})
			}
		}
	}

	if len(candidates) == 0 {
		return "", "", -1
	}

	// Sort by distance, then by alias length (prefer shorter/more specific)
	sort.Slice(candidates, func(i, j int) bool {
		if candidates[i].distance != candidates[j].distance {
			return candidates[i].distance < candidates[j].distance
		}
		return len(candidates[i].alias) < len(candidates[j].alias)
	})

	best := candidates[0]
	return best.id, best.alias, best.distance
}

// levenshtein computes the Levenshtein edit distance between two strings
func levenshtein(a, b string) int {
	la := len([]rune(a))
	lb := len([]rune(b))

	if la == 0 {
		return lb
	}
	if lb == 0 {
		return la
	}

	ra := []rune(a)
	rb := []rune(b)

	// Use two rows instead of full matrix for O(min(m,n)) space
	prev := make([]int, lb+1)
	curr := make([]int, lb+1)

	for j := 0; j <= lb; j++ {
		prev[j] = j
	}

	for i := 1; i <= la; i++ {
		curr[0] = i
		for j := 1; j <= lb; j++ {
			cost := 1
			if ra[i-1] == rb[j-1] {
				cost = 0
			}
			curr[j] = min3(
				prev[j]+1,      // deletion
				curr[j-1]+1,    // insertion
				prev[j-1]+cost, // substitution
			)
		}
		prev, curr = curr, prev
	}

	return prev[lb]
}

func min3(a, b, c int) int {
	if a < b {
		if a < c {
			return a
		}
		return c
	}
	if b < c {
		return b
	}
	return c
}

// FuzzyWordMatch performs word-level fuzzy matching against alias words
// Useful for queries like "tributria" matching "tributaria" inside "general tributaria"
func FuzzyWordMatch(query string, maxWordDist int) (id string, matchedAlias string) {
	normalized := normalizeForAlias(query)
	words := strings.Fields(normalized)
	if len(words) == 0 {
		return "", ""
	}

	// Remove stop words from query for matching
	var queryWords []string
	for _, w := range words {
		if !StopWords[w] && len(w) > 2 {
			queryWords = append(queryWords, w)
		}
	}
	if len(queryWords) == 0 {
		queryWords = words
	}

	type candidate struct {
		alias      string
		id         string
		matchScore int // how many query words fuzzy-matched
		totalDist  int // total edit distance
	}

	var candidates []candidate

	for alias, boeID := range KnownLaws {
		aliasWords := strings.Fields(alias)
		matchCount := 0
		totalDist := 0

		for _, qw := range queryWords {
			bestDist := len(qw) // worst case
			for _, aw := range aliasWords {
				if len(aw) <= 2 {
					continue
				}
				d := levenshtein(qw, aw)
				// Allow 1 edit per 5 chars of the word, min 1
				maxAllowed := maxWordDist
				scaledMax := (len(aw) / 5) + 1
				if scaledMax < maxAllowed {
					maxAllowed = scaledMax
				}
				if d <= maxAllowed && d < bestDist {
					bestDist = d
				}
			}
			if bestDist <= maxWordDist {
				matchCount++
				totalDist += bestDist
			}
		}

		if matchCount == len(queryWords) && totalDist > 0 {
			candidates = append(candidates, candidate{alias, boeID, matchCount, totalDist})
		}
	}

	if len(candidates) == 0 {
		return "", ""
	}

	// Sort by: most words matched, then least total distance, then shortest alias
	sort.Slice(candidates, func(i, j int) bool {
		if candidates[i].matchScore != candidates[j].matchScore {
			return candidates[i].matchScore > candidates[j].matchScore
		}
		if candidates[i].totalDist != candidates[j].totalDist {
			return candidates[i].totalDist < candidates[j].totalDist
		}
		return len(candidates[i].alias) < len(candidates[j].alias)
	})

	return candidates[0].id, candidates[0].alias
}

// ContainsWordMatch checks if query words appear as substrings in any alias
// Useful for partial/abbreviated searches like "sociedades" matching "sociedades de capital"
func ContainsWordMatch(query string) (id string, matchedAlias string) {
	normalized := normalizeForAlias(query)
	words := strings.Fields(normalized)
	if len(words) == 0 {
		return "", ""
	}

	type candidate struct {
		alias string
		id    string
		score int // number of query words found in alias
	}

	var candidates []candidate

	for alias, boeID := range KnownLaws {
		// Skip very short aliases (abbreviations)
		if len(alias) <= 4 {
			continue
		}

		matchCount := 0
		for _, w := range words {
			if strings.Contains(alias, w) {
				matchCount++
			}
		}

		if matchCount > 0 && matchCount == len(words) {
			candidates = append(candidates, candidate{alias, boeID, matchCount})
		}
	}

	if len(candidates) == 0 {
		return "", ""
	}

	// Sort by: all words matched first, then shorter alias (more specific)
	sort.Slice(candidates, func(i, j int) bool {
		if candidates[i].score != candidates[j].score {
			return candidates[i].score > candidates[j].score
		}
		return len(candidates[i].alias) < len(candidates[j].alias)
	})

	return candidates[0].id, candidates[0].alias
}

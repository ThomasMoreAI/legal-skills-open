package semantic

import (
	"encoding/binary"
	"fmt"
	"io"
	"math"
	"os"
	"path/filepath"
	"sort"
)

// IndexEntry represents a single law in the semantic index
type IndexEntry struct {
	ID     string
	Title  string
	Vector []float32
}

// Index is the semantic search index
type Index struct {
	Dimensions int
	Entries    []IndexEntry
}

// SearchResult is a semantic search result
type SearchResult struct {
	ID    string  `json:"identificador"`
	Title string  `json:"titulo"`
	URL   string  `json:"url"`
	Score float32 `json:"score"` // cosine similarity
}

// DefaultIndexPath returns the default index file path
func DefaultIndexPath() string {
	home, _ := os.UserHomeDir()
	return filepath.Join(home, ".boe", "index-v1.bin")
}

// LoadIndex reads the binary index from disk
func LoadIndex(path string) (*Index, error) {
	f, err := os.Open(path)
	if err != nil {
		return nil, err
	}
	defer f.Close()

	// Read header: magic(4) + version(4) + dimensions(4) + count(4)
	magic := make([]byte, 4)
	if _, err := io.ReadFull(f, magic); err != nil {
		return nil, fmt.Errorf("reading magic: %w", err)
	}
	if string(magic) != "BOEI" {
		return nil, fmt.Errorf("invalid index file (bad magic: %s)", string(magic))
	}

	var version, dims, count uint32
	binary.Read(f, binary.LittleEndian, &version)
	binary.Read(f, binary.LittleEndian, &dims)
	binary.Read(f, binary.LittleEndian, &count)

	if version != 1 {
		return nil, fmt.Errorf("unsupported index version: %d", version)
	}

	idx := &Index{
		Dimensions: int(dims),
		Entries:    make([]IndexEntry, 0, count),
	}

	for i := uint32(0); i < count; i++ {
		// Read ID
		var idLen uint32
		binary.Read(f, binary.LittleEndian, &idLen)
		idBytes := make([]byte, idLen)
		io.ReadFull(f, idBytes)

		// Read Title
		var titleLen uint32
		binary.Read(f, binary.LittleEndian, &titleLen)
		titleBytes := make([]byte, titleLen)
		io.ReadFull(f, titleBytes)

		// Read Vector
		vec := make([]float32, dims)
		binary.Read(f, binary.LittleEndian, &vec)

		idx.Entries = append(idx.Entries, IndexEntry{
			ID:     string(idBytes),
			Title:  string(titleBytes),
			Vector: vec,
		})
	}

	return idx, nil
}

// Search finds the top-K most similar entries to the query vector
func (idx *Index) Search(queryVec []float32, k int) []SearchResult {
	if len(queryVec) != idx.Dimensions {
		return nil
	}

	type scored struct {
		idx   int
		score float32
	}

	scores := make([]scored, len(idx.Entries))
	for i, entry := range idx.Entries {
		scores[i] = scored{i, cosineSimilarity(queryVec, entry.Vector)}
	}

	sort.Slice(scores, func(i, j int) bool {
		return scores[i].score > scores[j].score
	})

	if k > len(scores) {
		k = len(scores)
	}

	results := make([]SearchResult, k)
	for i := 0; i < k; i++ {
		entry := idx.Entries[scores[i].idx]
		results[i] = SearchResult{
			ID:    entry.ID,
			Title: entry.Title,
			URL:   "https://www.boe.es/buscar/act.php?id=" + entry.ID,
			Score: scores[i].score,
		}
	}

	return results
}

// cosineSimilarity computes cosine similarity between two vectors
func cosineSimilarity(a, b []float32) float32 {
	if len(a) != len(b) {
		return 0
	}

	var dot, normA, normB float64
	for i := range a {
		dot += float64(a[i]) * float64(b[i])
		normA += float64(a[i]) * float64(a[i])
		normB += float64(b[i]) * float64(b[i])
	}

	denom := math.Sqrt(normA) * math.Sqrt(normB)
	if denom == 0 {
		return 0
	}

	return float32(dot / denom)
}

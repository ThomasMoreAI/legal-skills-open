package api

import (
	"encoding/json"
	"encoding/xml"
	"fmt"
	"strings"
)

// xmlNode represents a generic XML node for conversion
type xmlNode struct {
	XMLName  xml.Name
	Attrs    []xml.Attr `xml:",any,attr"`
	Content  string     `xml:",chardata"`
	Children []xmlNode  `xml:",any"`
}

// xmlToJSON converts XML response bytes to JSON
func xmlToJSON(data []byte) (json.RawMessage, error) {
	var node xmlNode
	if err := xml.Unmarshal(data, &node); err != nil {
		return nil, fmt.Errorf("parsing XML: %w", err)
	}

	result := nodeToMap(node)
	jsonBytes, err := json.Marshal(result)
	if err != nil {
		return nil, fmt.Errorf("marshalling JSON: %w", err)
	}

	return json.RawMessage(jsonBytes), nil
}

func nodeToMap(node xmlNode) interface{} {
	// If it's a leaf node with just text
	content := strings.TrimSpace(node.Content)
	if len(node.Children) == 0 && len(node.Attrs) == 0 {
		return content
	}

	result := make(map[string]interface{})

	// Add attributes
	for _, attr := range node.Attrs {
		result["@"+attr.Name.Local] = attr.Value
	}

	// Add text content if present
	if content != "" {
		result["#text"] = content
	}

	// Group children by name for arrays
	childGroups := make(map[string][]interface{})
	childOrder := []string{}

	for _, child := range node.Children {
		name := child.XMLName.Local
		if _, exists := childGroups[name]; !exists {
			childOrder = append(childOrder, name)
		}
		childGroups[name] = append(childGroups[name], nodeToMap(child))
	}

	for _, name := range childOrder {
		children := childGroups[name]
		if len(children) == 1 {
			result[name] = children[0]
		} else {
			result[name] = children
		}
	}

	return result
}

// BlockToText extracts readable text from a law block XML response
func BlockToText(xmlData []byte) (string, error) {
	var node xmlNode
	if err := xml.Unmarshal(xmlData, &node); err != nil {
		return "", fmt.Errorf("parsing XML: %w", err)
	}

	var sb strings.Builder
	extractText(&sb, node, 0)
	return strings.TrimSpace(sb.String()), nil
}

func extractText(sb *strings.Builder, node xmlNode, depth int) {
	name := node.XMLName.Local

	// Handle specific BOE XML elements
	switch name {
	case "bloque":
		// Get title from attributes
		for _, attr := range node.Attrs {
			if attr.Name.Local == "titulo" && attr.Value != "" {
				sb.WriteString(fmt.Sprintf("## %s\n\n", attr.Value))
			}
		}
	case "version":
		// Show which version this is
		var fecha string
		for _, attr := range node.Attrs {
			if attr.Name.Local == "fecha_vigencia" {
				fecha = attr.Value
			}
		}
		if fecha != "" {
			sb.WriteString(fmt.Sprintf("[Vigente desde: %s]\n", formatDate(fecha)))
		}
	case "p":
		content := strings.TrimSpace(node.Content)
		if content != "" {
			// Check class for formatting
			class := ""
			for _, attr := range node.Attrs {
				if attr.Name.Local == "class" {
					class = attr.Value
				}
			}
			switch class {
			case "articulo":
				sb.WriteString(fmt.Sprintf("### %s\n\n", content))
			default:
				sb.WriteString(content + "\n\n")
			}
		}
	}

	// Recurse into children
	for _, child := range node.Children {
		extractText(sb, child, depth+1)
	}
}

func formatDate(yyyymmdd string) string {
	if len(yyyymmdd) != 8 {
		return yyyymmdd
	}
	return yyyymmdd[6:8] + "/" + yyyymmdd[4:6] + "/" + yyyymmdd[0:4]
}

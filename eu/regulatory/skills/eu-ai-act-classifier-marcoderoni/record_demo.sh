#!/bin/bash
# ─────────────────────────────────────────────────────────────────
# EU AI Act Classifier — Demo GIF Recording Script
# 
# Prerequisites:
#   brew install asciinema          (macOS)
#   pip install agg                 (asciinema to GIF converter)
#   npm install -g svg-term-cli     (alternative: svg-term)
#
# Usage:
#   chmod +x record_demo.sh
#   ./record_demo.sh
#
# Output: assets/demo.gif
# ─────────────────────────────────────────────────────────────────

set -e

mkdir -p assets

echo "Recording demo for EU AI Act Risk Classifier..."
echo "This will record a terminal session — press Ctrl+D to stop early."
echo ""

# Record with asciinema
asciinema rec /tmp/eu-ai-act-demo.cast \
  --title "EU AI Act Risk Classifier" \
  --command "bash demo_script.sh" \
  --overwrite

echo ""
echo "Converting to GIF..."

# Convert to GIF using agg (https://github.com/asciinema/agg)
agg /tmp/eu-ai-act-demo.cast assets/demo.gif \
  --font-size 14 \
  --cols 80 \
  --rows 36 \
  --speed 1.5

echo "✓ Demo GIF saved to assets/demo.gif"
echo ""
echo "To preview: open assets/demo.gif"

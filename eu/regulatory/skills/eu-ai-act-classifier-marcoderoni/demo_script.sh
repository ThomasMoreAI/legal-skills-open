#!/bin/bash
# Demo script — executed during asciinema recording
# Simulates realistic classifier usage for the GIF

sleep 1

echo ""
echo "# EU AI Act Risk Classifier — Demo"
echo "# github.com/marcoderoni/eu-ai-act-classifier"
echo ""
sleep 1.5

echo "# Example 1: HR screening tool"
sleep 0.8
echo '$ python classifier.py -d "HR tool that ranks job applicants using CV data and predicted performance scores"'
sleep 0.5
python classifier.py -d "HR tool that ranks job applicants using CV data and predicted performance scores"
sleep 2

echo ""
echo "# Example 2: Customer support chatbot"
sleep 0.8
echo '$ python classifier.py -d "Chatbot on a bank website that answers customer questions about products"'
sleep 0.5
python classifier.py -d "Chatbot on a bank website that answers customer questions about products"
sleep 2

echo ""
echo "# Example 3: Batch mode — 10 systems at once"
sleep 0.8
echo "$ python batch_classifier.py -i examples/sample_systems.csv --csv summary.csv"
sleep 0.5
python batch_classifier.py -i examples/sample_systems.csv --csv /tmp/summary.csv
sleep 2

echo ""
echo "# Done. Reports saved."
sleep 1

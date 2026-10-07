#!/bin/bash

# Get the description of the AI system from the first argument
SYSTEM_DESCRIPTION=$1

if [ -z "$SYSTEM_DESCRIPTION" ]; then
  echo "Error: Please provide a description of the AI system to check."
  exit 1
fi

# Define the high-risk categories based on EU AI Act Annex III
PROMPT=\\"
You are an expert in the EU AI Act. Your task is to classify an AI system description as either 'HIGH-RISK' or 'LOW-RISK' based ONLY on Annex III (Article 6).

Annex III High-Risk Categories include AI used for:
1. Biometric identification (remote/real-time)
2. Critical infrastructure (management/operation)
3. Education/Vocational training (access/evaluation)
4. Employment, worker management, and self-employment access (e.g., recruitment, promotion)
5. Essential private/public services (e.g., credit scoring, emergency dispatch)
6. Law enforcement (e.g., risk assessment, evidence evaluation)
7. Migration, asylum, and border control (e.g., lie detection, risk assessment)
8. Administration of justice and democratic processes.

AI System Description: \\"$SYSTEM_DESCRIPTION\\"

INSTRUCTIONS:
1. Analyze the description against the categories above.
2. If it fits ANY category, output: 'HIGH-RISK: [Category Number(s)]'.
3. If it does NOT fit, output: 'LOW-RISK: General Purpose AI or Not Listed'.

Output ONLY the classification line. Do not add any explanation or preamble.
\\"

# Use the 'gemini' CLI for the classification inference
# The response is saved to a variable
RESULT=$(gemini -p \\"$PROMPT\\")

echo "---"
echo "AI System: $SYSTEM_DESCRIPTION"
echo "---"
echo "PRELIMINARY AI ACT RISK CLASSIFICATION:"
echo "$RESULT"
echo "---"
echo "Disclaimer: This is an automated, preliminary check and does not constitute legal advice."

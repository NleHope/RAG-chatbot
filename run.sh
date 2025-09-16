#!/bin/bash
set -e

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
 
echo "Step 1: Preprocess data..."
python3 scripts/preprocessed.py

echo "Step 2: Build embeddings..."
python3 scripts/embed.py

echo "Step 3: Run query..."
python3 scripts/query.py

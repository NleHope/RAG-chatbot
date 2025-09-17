#!/bin/bash

echo "Step 1: Preprocess data..."
python3 scripts/preprocessed.py

echo "Step 2: Build embeddings..."
python3 scripts/embed.py

echo "Step 3: Run query..."
# Use environment variable QUESTION or default question
QUESTION=${QUESTION:-"What is the main topic of this document?"}
python3 scripts/query.py --question "$QUESTION"

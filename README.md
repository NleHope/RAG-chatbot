

# Simple RAG System with Small Language Model

A lightweight Retrieval-Augmented Generation (RAG) system that runs locally with FAISS and a small language model.

---

## How to Run

1. Clone the repo
   ```bash
   git clone https://github.com/NleHope/RAG-chatbot.git

1. Open your terminal and navigate to the project root:
   ```bash
   cd RAG-chatbot
3. Open Docker Desktop and run this command in terminal
   ```bash
   docker build -t <your-designated-name> .
4. Run the container and enjoy
   ```bash
   docker run <your-designated-name>



Add your own .txt files to the data/ folder for better context in retrieval.

## Project Structure
      
      rag_system/
      │
      ├── data/ # raw documents
      ├── processed/ # cleaned documents
      ├── embeddings/ # FAISS index + doc IDs
      ├── scripts/
      │ ├── preprocess.py # text preprocessing
      │ ├── embed.py # build embeddings
      │ ├── query.py # RAG query pipeline
      │ └── run.sh # orchestration script
      └── requirements.txt


## Data Pipeline

      data/ (raw input)
         │
         ▼
      [Preprocess: clean text]
         │
         ▼
      processed/ (normalized text)
         │
         ▼
      [Embed: generate embeddings]
         │
         ▼
      embeddings/ (FAISS index + doc IDs)
         │
         ▼
      [Query: retrieve + generate answer]
         │
         ▼
      User output (answer with context)

Features

Simple terminal-based chat with a local language model

Data stored as embeddings in a FAISS vector database

Easy to extend with more document types or larger models



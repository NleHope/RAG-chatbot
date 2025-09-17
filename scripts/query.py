import faiss, pickle
from pathlib import Path
from sentence_transformers import SentenceTransformer
from transformers import pipeline
import torch
import sys
import os

# Get the project root directory (parent of scripts directory)
script_dir = Path(__file__).parent
project_root = script_dir.parent

# Change to project root directory for consistent paths
os.chdir(project_root)

# load
index = faiss.read_index("embeddings/index.faiss")
ids = pickle.load(open("embeddings/ids.pkl", "rb"))
docs = [Path("processed")/i for i in ids]


model = SentenceTransformer("all-MiniLM-L6-v2")
qa = pipeline("text-generation", model="gpt2", max_new_tokens = 256)  # replace with LLM

model = SentenceTransformer("all-MiniLM-L6-v2")
qa = pipeline("text-generation", model="gpt2", max_new_tokens = 256)  # replace with LLM

# Check for command line arguments
if len(sys.argv) > 1 and sys.argv[1] == "--question" and len(sys.argv) > 2:
    # Single question from command line
    questions = [sys.argv[2]]
    print(f"Running RAG query for: {sys.argv[2]}")
else:
    # Sample questions for demo
    questions = [
        "What is the main topic discussed?",
        "Can you summarize the key points?",
        "What are the important details mentioned?"
    ]
    print("Running RAG queries on sample questions...")

print("=" * 50)

for i, question in enumerate(questions, 1):
    print(f"\nQuestion {i}: {question}")
    q_emb = model.encode([question], truncate=True)
    
    D, I = index.search(q_emb, k=2)
    context = " ".join([docs[i].read_text() for i in I[0]])
    
    answer = qa(f"Question: {question}\nAnswer:", max_length = 100)[0]["generated_text"]
    
    print(f"Answer: {answer}")
    print("-" * 30)

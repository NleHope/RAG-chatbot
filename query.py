import faiss, pickle
from pathlib import Path
from sentence_transformers import SentenceTransformer
from transformers import pipeline
import torch


# load
index = faiss.read_index("embeddings/index.faiss")
ids = pickle.load(open("embeddings/ids.pkl", "rb"))
docs = [Path("processed")/i for i in ids]


model = SentenceTransformer("all-MiniLM-L6-v2")
qa = pipeline("text-generation", model="gpt2", max_new_tokens = 256)  # replace with LLM


question = input("Enter your question: ")
q_emb = model.encode([question], truncate=True)

D, I = index.search(q_emb, k=2)
context = " ".join([docs[i].read_text() for i in I[0]])

answer = qa(f"Question: {question}\nAnswer:", max_length = 100)[0]["generated_text"]

print("Answer:", answer)

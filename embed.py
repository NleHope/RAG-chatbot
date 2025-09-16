import faiss, pickle
from pathlib import Path
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
docs, ids = [], []

for file in Path("processed").glob("*.txt"):
    text = file.read_text(encoding="utf-8")
    docs.append(text)
    ids.append(file.name)

embeddings = model.encode(docs)
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

faiss.write_index(index, "embeddings/index.faiss")
with open("embeddings/ids.pkl", "wb") as f:
    pickle.dump(ids, f)

print("✅ Embeddings built.")

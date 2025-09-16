import os
from pathlib import Path

input_dir = Path("data")
output_dir = Path("processed")
output_dir.mkdir(exist_ok=True)

for file in input_dir.glob("*.txt"):
    text = file.read_text(encoding="utf-8")
    cleaned = text.strip().replace("\n", " ")  # trivial cleaning
    (output_dir / file.name).write_text(cleaned, encoding="utf-8")

print("✅ Preprocessing done.")

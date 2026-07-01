from app.services.chunking import chunk_text
from app.services.extraction.extractor import extract_document

text = extract_document("uploads/825ade6b-d4d6-441c-9931-03bb5431c539.pdf")

chunks = chunk_text(text)

print(f"Total Chunks: {len(chunks)}")

for i, chunk in enumerate(chunks, start=1):
    print(f"\n----- Chunk {i} -----")
    print(chunk[:300])
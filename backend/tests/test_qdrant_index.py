from app.services.chunking import chunk_text
from app.services.qdrant_client.indexer import index_chunks


text = """
ShadowBoard AI is an enterprise multi-agent decision intelligence platform.

It combines Google ADK,
Gemini,
Qdrant,
Lyzr,
A2A,
and MCP
to help executive teams make decisions.
"""


chunks = chunk_text(text)

count = index_chunks(
    chunks,
    metadata={
        "document": "shadowboard_intro"
    },
)

print(f"Indexed {count} chunks.")
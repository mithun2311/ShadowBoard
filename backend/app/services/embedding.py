from google import genai

from app.core.config import settings

client = genai.Client(
    api_key=settings.GEMINI_API_KEY,
)

EMBEDDING_MODEL = "gemini-embedding-001"
def embedding_dimension() -> int:
    return len(generate_embedding("ShadowBoard"))

def generate_embedding(text: str) -> list[float]:
    """
    Generate an embedding vector for the given text.
    """

    response = client.models.embed_content(
        model=EMBEDDING_MODEL,
        contents=text,
    )

    return response.embeddings[0].values
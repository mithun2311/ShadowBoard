from app.core.config import settings
from app.services.embedding import generate_embedding
from app.services.qdrant_client.client import client


def retrieve_context(
    query: str,
    limit: int = 5,
) -> str:

    vector = generate_embedding(query)

    results = client.query_points(
        collection_name=settings.QDRANT_COLLECTION,
        query=vector,
        limit=limit,
    )

    contexts = []

    for point in results.points:

        payload = point.payload or {}

        text = payload.get("text")

        if text:
            contexts.append(text)

    return "\n\n".join(contexts)
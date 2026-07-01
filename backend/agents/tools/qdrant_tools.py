from app.core.config import settings
from qdrant_client import QdrantClient

client = QdrantClient(
    url=settings.QDRANT_URL,
    api_key=settings.QDRANT_API_KEY,
)


def list_collections():
    """
    Returns all Qdrant collections.
    """
    collections = client.get_collections()

    return [
        collection.name
        for collection in collections.collections
    ]

from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams
from app.services.embedding import embedding_dimension
from app.core.config import settings


client = QdrantClient(
    url=settings.QDRANT_URL,
    api_key=settings.QDRANT_API_KEY or None,
)


def ensure_collection():

    collections = client.get_collections().collections

    names = [c.name for c in collections]

    if settings.QDRANT_COLLECTION not in names:

        client.create_collection(
            collection_name=settings.QDRANT_COLLECTION,

            vectors_config=VectorParams(
                size=embedding_dimension(),
                distance=Distance.COSINE,
            ),
        )

    return settings.QDRANT_COLLECTION
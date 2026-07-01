from uuid import uuid4

from qdrant_client.http.models import PointStruct

from app.core.config import settings
from app.services.embedding import generate_embedding
from app.services.qdrant_client.client import (
    client,
    ensure_collection,
)


def index_chunks(
    chunks: list[str],
    metadata: dict | None = None,
):

    ensure_collection()

    points = []

    metadata = metadata or {}

    for chunk in chunks:

        vector = generate_embedding(chunk)

        points.append(
            PointStruct(
                id=str(uuid4()),
                vector=vector,
                payload={
                    "text": chunk,
                    **metadata,
                },
            )
        )

    client.upsert(
        collection_name=settings.QDRANT_COLLECTION,
        points=points,
    )

    return len(points)
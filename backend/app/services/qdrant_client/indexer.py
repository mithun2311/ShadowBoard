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

    if not chunks:
        print("No chunks found.")
        return 0

    ensure_collection()

    points = []

    metadata = metadata or {}

    for chunk in chunks:

        if not chunk.strip():
            continue

        vector = generate_embedding(chunk)

        if not vector:
            print("Embedding generation failed.")
            continue

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

    print("Points created:", len(points))

    if not points:
        print("No points generated. Skipping upsert.")
        return 0

    client.upsert(
        collection_name=settings.QDRANT_COLLECTION,
        points=points,
    )

    return len(points)        )

    client.upsert(
        collection_name=settings.QDRANT_COLLECTION,
        points=points,
    )

    return len(points)

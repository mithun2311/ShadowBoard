from qdrant_client import QdrantClient

client = QdrantClient(
    host="localhost",
    port=6333,
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
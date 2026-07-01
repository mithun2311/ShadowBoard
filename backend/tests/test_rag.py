from app.services.qdrant_client.retrieval import retrieve_context


query = "What is ShadowBoard?"

context = retrieve_context(query)

print("=" * 60)
print(context)
print("=" * 60)
from app.services.embedding import generate_embedding

vector = generate_embedding(
    "ShadowBoard AI is an enterprise multi-agent platform."
)

print("Vector length:", len(vector))

print(vector[:10])
from app.services.mcp import mcp_server

print(mcp_server.health())

print()

print(
    mcp_server.search_documents(
        "What is ShadowBoard?"
    )
)
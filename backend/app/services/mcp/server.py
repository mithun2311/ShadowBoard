from app.services.qdrant_client.retrieval import retrieve_context


class ShadowBoardMCPServer:
    """
    MCP service wrapper exposing ShadowBoard capabilities.
    """

    def search_documents(
        self,
        query: str,
        limit: int = 5,
    ) -> str:
        return retrieve_context(
            query=query,
            limit=limit,
        )

    def health(self):
        return {
            "service": "ShadowBoard MCP",
            "status": "healthy",
            "version": "1.0.0",
        }


mcp_server = ShadowBoardMCPServer()
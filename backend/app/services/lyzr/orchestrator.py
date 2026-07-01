from app.services.qdrant_client.retrieval import retrieve_context


class ShadowBoardOrchestrator:
    """
    Prepares business context that can later be consumed
    by a Lyzr SuperFlow.
    """

    def prepare_workflow_context(
        self,
        query: str,
    ) -> dict:

        context = retrieve_context(query)

        return {
            "query": query,
            "retrieved_context": context,
            "workflow": "ShadowBoard Executive Review",
            "source": "Google ADK + Qdrant",
        }


orchestrator = ShadowBoardOrchestrator()
from app.services.qdrant_client.retrieval import retrieve_context


class ShadowBoardWorkflow:

    def prepare_context(
        self,
        query: str,
    ) -> str:
        return retrieve_context(query)


workflow = ShadowBoardWorkflow()
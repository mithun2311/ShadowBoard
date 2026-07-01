import httpx

from app.core.config import settings


class LyzrClient:

    def __init__(self):
        self.base_url = settings.LYZR_BASE_URL
        self.api_key = settings.LYZR_API_KEY

    async def health(self):
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{self.base_url}/health",
                headers={
                    "x-api-key": self.api_key,
                },
                timeout=20,
            )
            return response.json()


lyzr_client = LyzrClient()
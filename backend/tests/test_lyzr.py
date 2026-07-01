import asyncio

from app.services.lyzr.client import lyzr_client


async def main():
    try:
        result = await lyzr_client.health()
        print(result)
    except Exception as e:
        print("Lyzr connection failed:")
        print(e)


if __name__ == "__main__":
    asyncio.run(main())
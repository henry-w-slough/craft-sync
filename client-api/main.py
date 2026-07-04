#the api is truly just a test. This is not the real api, which will most likely be made in Java
#after the backend is complete.

import config
import asyncio
import httpx


async def main():
    print(httpx.post(
        f"http://localhost:8020/world",
        json={"name": "world", "description": "my first world"}
        ))


if __name__ == "__main__":
    asyncio.run(main())





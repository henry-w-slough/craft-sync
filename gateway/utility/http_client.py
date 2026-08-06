import httpx


async def send_request(connection: httpx.AsyncClient, method: str, url: str, *args, **kwargs) -> httpx.Response:

    async with connection as client:

        response = await client.request(method, url, *args, **kwargs)
        response.raise_for_status()

        
        return response

        
        

import httpx
from typing import Callable


async def send_request(request_method: Callable, url: str, *args, **kwargs) -> None:

    async with httpx.AsyncClient() as client:
        
        

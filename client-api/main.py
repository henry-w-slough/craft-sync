#the api is truly just a test. This is not the real api, which will most likely be made in Java
#after the backend is complete.

import asyncio
import aiofiles
import uuid
import os

import httpx
from typing import Callable, AsyncGenerator


backend_address = "http://localhost:8040"


async def send_request(request: Callable, url: str, *args, **kwargs) -> httpx.Response:

    response: httpx.Response = await request(url, *args, **kwargs)
    response.raise_for_status()

    return response


async def file_to_chunks(path, chunk_size=8 * 1024 * 1024) -> AsyncGenerator[bytes, None]:
    async with aiofiles.open(path, "rb") as f:
        while chunk := await f.read(chunk_size):
            yield chunk


async def connect_to_cloud(url: str):

    async with httpx.AsyncClient() as client:
        
            await send_request(
                client.put,
                url,
                content=file_to_chunks("movie.mp4"),
                headers={"Content-Length": str(os.path.getsize("movie.mp4"))}
            )


async def main():

    async with httpx.AsyncClient() as client:

        while True:

            action = input("> ").strip().lower()


            if action == "add":
                response = await send_request(
                    client.post,
                    f"{backend_address}/worlds",
                    json={"id": str(uuid.uuid4())},
                )
                print(response.json())
                print(await connect_to_cloud(response.json()["presigned_url"]))


            elif action == "delete":
                world_id = input("Id: ")
                response = await send_request(client.delete, f"{backend_address}/worlds/{world_id}")
                print(response)


            elif action == "update":
                
                world_id = input("Id: ")
                updates = {}

                name = input("Name (blank for current): ")
                description = input("Description (blank for current): ")

                if name:
                    updates["name"] = name
                if description:
                    updates["description"] = description

                response = await send_request(
                    client.patch,
                    f"{backend_address}/worlds/{world_id}",
                    json=updates,
                )
                print(response)



if __name__ == "__main__":
    asyncio.run(main())





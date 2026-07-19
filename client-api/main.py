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


async def send_to_cloud(url: str, src_to_send: str):

    async with httpx.AsyncClient() as client:
        
            await send_request(
                client.put,
                url,
                content=file_to_chunks(src_to_send),
                headers={"Content-Length": str(os.path.getsize(src_to_send))}
            )


async def main():

    async with httpx.AsyncClient() as client:

        while True:

            action = input("> ").strip().lower()


            if action == "add":

                response = await send_request(
                    client.post,
                    f"{backend_address}/worlds/{str(uuid.uuid4())}",
                    json={} #since create request is empty but in use
                )

                print("---------------- Added World Metadata ----------------")
                for item in response.json():
                    print(f"{item} -> {response.json()[item]}")
                    print(" ------------------------------------------------------")

                await send_to_cloud(response.json()["presigned_url"], input("File to send: "))


            elif action == "delete":
                world_id = input("Id: ")
                response = await send_request(client.delete, f"{backend_address}/worlds/{world_id}")
                print(response)


            elif action == "update":

                response = await send_request(
                    client.put,
                    f"{backend_address}/worlds/{input("Id of world: ")}",
                    json={}
                )

                print("---------------- Added World Metadata ----------------")
                for item in response.json():
                    print(f"{item} -> {response.json()[item]}")
                    print(" ------------------------------------------------------")

                await send_to_cloud(response.json()["presigned_url"], input("File to send: "))

                


                



if __name__ == "__main__":
    asyncio.run(main())





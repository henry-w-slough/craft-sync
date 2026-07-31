#the api is truly just a test. This is not the real api, which will most likely be made in Java
#after the backend is complete.

import asyncio
import aiofiles
import uuid
import os
from pathlib import Path

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


async def main():

    async with httpx.AsyncClient() as client:

        while True:

            action = input("> ").strip().lower()


            if action == "add":

                world_root_dir = input("world to send: ")
                root = Path(world_root_dir)
                paths = [
                    path.relative_to(root).as_posix()
                    for path in root.rglob("*")
                    if path.is_file()
                ]
            
                response = await send_request(
                    client.post,
                    f"{backend_address}/worlds/{str(uuid.uuid4())}",
                    json={"relative_paths": paths} #since create request is empty but in use
                )

                presigned_urls = response.json()["path_presigned_urls"]

                for path in presigned_urls:
                    path_directory = os.path.join(world_root_dir, path)
                    await send_request(
                        client.put,
                        presigned_urls[path],
                        content = file_to_chunks(path_directory),
                        headers = {"Content-Length": str(os.path.getsize(path_directory))}
                    )


            if action == "update":

                world_id = input("id of world to update: ")

                world_root_dir = input("world folder to send: ")
                root = Path(world_root_dir)
                paths = [
                    path.relative_to(root).as_posix()
                    for path in root.rglob("*")
                    if path.is_file()
                ]
            
                response = await send_request(
                    client.put,
                    f"{backend_address}/worlds/{world_id}",
                    json={"relative_paths": paths}
                )

                presigned_urls = response.json()["path_presigned_urls"]

                for path in presigned_urls:
                    path_directory = os.path.join(world_root_dir, path)
                    await send_request(
                        client.put,
                        presigned_urls[path],
                        content = file_to_chunks(path_directory),
                        headers = {"Content-Length": str(os.path.getsize(path_directory))}
                    )


            if action == "download":

                response = await send_request(
                    client.get,
                    f"{backend_address}/worlds/{input("Id of world to download: ")}"
                )

                presigned_url_paths = response.json()["path_presigned_urls"]

                download_root = input(f"Directory to download to: ")
                os.makedirs(download_root, exist_ok=True)

                for path in presigned_url_paths:

                    os.makedirs(os.path.join(download_root, os.path.dirname(path)), exist_ok=True)
                    cloud_response = await send_request(
                        client.get,
                        presigned_url_paths[path]
                    )

                    with open(path, "wb") as file:
                        file.write(cloud_response.content)
                        

            if action == "delete":

                response = await send_request(
                    client.delete,
                    f"{backend_address}/worlds/{input("Id of world to delete: ")}"
                )

                print(response)

                   


        


                

if __name__ == "__main__":
    asyncio.run(main())





#the api is truly just a test. This is not the real api, which will most likely be made in Java
#after the backend is complete.

import config
import asyncio
import httpx
from typing import Callable


async def send_request(request: Callable, url: str, *args, **kwargs) -> httpx.Response:

    response: httpx.Response = await request(url, *args, **kwargs)
    response.raise_for_status()

    return response



async def main():

    async with httpx.AsyncClient() as client:

        while True:

            action = input("> ")
            
            if action == "list":
                response = await send_request(client.get, "http://localhost:8020/worlds")
                for world in response.json():
                    print("-------------------")
                    print(f"Name: {world["name"]}")
                    print(f"Description: {world["description"]}")
                    print(f"Date Added: {world["date_added"]}")
                    print(f"Id: {world["id"]}")

            if action == "add":
                response = await send_request(client.post, "http://localhost:8020/worlds", json={"name": input("Name: "), "description": input("Description: ")})
                print(response)

            if action == "delete":
                response = await send_request(client.delete, f"http://localhost:8020/worlds/{input("Id: ")}")
                print(response)

if __name__ == "__main__":
    asyncio.run(main())





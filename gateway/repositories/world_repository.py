import httpx

from ..utility import http_client
import config


class WorldRepository:


    def __init__(self) -> None:

        self.client_connection = httpx.AsyncClient()


    async def add_world(self) -> None:

        metadata_request = await http_client.send_request(
            self.client_connection,
            self.client_connection.get,
            f"{config.METADATA_ADDRESS}/worlds"
        )

        


    async def download_world_by_id(self) -> None:
        pass


    async def update_world_by_id(self) -> None:
        pass


    async def delete_world_by_id(self) -> None:
        pass


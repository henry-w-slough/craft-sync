from models.world_response import WorldResponse
from models.world_create_request import WorldCreateRequest

from exceptions.world_not_found_exception import WorldNotFoundException

import uuid
import os
import shutil
import config
import asyncio


class WorldStorageRepository:


    def __init__(self) -> None:
        pass


    async def add_world(self, world_create_request: WorldCreateRequest) -> WorldResponse:
        
        os.makedirs(f"{config.STORAGE_DIR}/{world_create_request.id}")
        
        return WorldResponse(
            id = world_create_request.id
        )


    async def delete_world_by_id(self, id: uuid.UUID) -> None:

        try:
            await asyncio.to_thread(shutil.rmtree, f"{config.STORAGE_DIR}/{id}", False, None)
        except FileNotFoundError:
            raise WorldNotFoundException()
    



    
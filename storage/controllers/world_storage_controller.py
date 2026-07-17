from services.world_storage_service import WorldStorageService
from models.world_response import WorldResponse
from models.world_create_request import WorldCreateRequest

import fastapi
import uuid

class WorldStorageController:

    
    def __init__(self, app:fastapi.FastAPI, world_storage_service: WorldStorageService) -> None:
        
        self.world_storage_service = world_storage_service

        app.post("/worlds", status_code=201)(self.add_world)
        app.delete("/worlds/{id}", status_code=204)(self.delete_world_by_id)


    async def add_world(self, request: WorldCreateRequest) -> WorldResponse:

        return await self.world_storage_service.add_world(request)
    

    async def delete_world_by_id(self, id: uuid.UUID) -> None:
        await self.world_storage_service.delete_world_by_id(id)
        


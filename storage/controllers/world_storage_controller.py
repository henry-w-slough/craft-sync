from services.world_storage_service import WorldStorageService

from models.responses.world_update_response import WorldUpdateResponse
from models.requests.world_create_request import WorldCreateRequest
from models.requests.world_update_request import WorldUpdateRequest
from models.responses.world_create_response import WorldCreateResponse


import fastapi
import uuid


class WorldStorageController:

    
    def __init__(self, app:fastapi.FastAPI, world_storage_service: WorldStorageService) -> None:
        
        self.world_storage_service = world_storage_service

        app.post("/worlds/{id}", status_code=201)(self.add_world)
        app.delete("/worlds/{id}", status_code=204)(self.delete_world_by_id)
        app.put("/worlds/{id}", status_code=200)(self.update_world_by_id)


    async def add_world(self, id: uuid.UUID, request: WorldCreateRequest) -> WorldCreateResponse:
        return await self.world_storage_service.add_world(id, request)
    

    async def delete_world_by_id(self, id: uuid.UUID) -> None:
        await self.world_storage_service.delete_world_by_id(id)


    async def update_world_by_id(self, id:uuid.UUID, request: WorldUpdateRequest) -> WorldUpdateResponse:
        return await self.world_storage_service.update_world_by_id(id, request)
        


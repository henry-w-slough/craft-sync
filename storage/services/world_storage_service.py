from repositories.world_storage_repository import WorldStorageRepository
from models.world_response import WorldResponse
from models.world_create_request import WorldCreateRequest
from models.world_create_response import WorldCreateResponse

from models.world_update_request import WorldUpdateRequest

import uuid


class WorldStorageService:


    def __init__(self, world_storage_repository: WorldStorageRepository) -> None:
        
        self.world_storage_repository = world_storage_repository


    async def add_world(self, id: uuid.UUID, world_create_request: WorldCreateRequest) -> WorldCreateResponse:
        return await self.world_storage_repository.add_world(id, world_create_request)
    

    async def delete_world_by_id(self, id: uuid.UUID) -> None:
        await self.world_storage_repository.delete_world_by_id(id)


    async def update_world_by_id(self, id: uuid.UUID, world_update_request: WorldUpdateRequest) -> WorldResponse:
        return await self.world_storage_repository.update_world_by_id(id, world_update_request)
        
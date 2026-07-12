import uuid

from models.world import World
from models.world_create_request import WorldCreateRequest
from models.world_update_request import WorldUpdateRequest

from metadata.repositories.world_metadata_repository import WorldMetadataRepository


class WorldMetadataService:


    def __init__(self, world_repository: WorldMetadataRepository):
        
        self.world_repository = world_repository


    async def get_all_worlds(self) -> list[World]:
        
        return await self.world_repository.get_all_worlds()


    async def add_world(self, world_create_request: WorldCreateRequest) -> World:

        return await self.world_repository.add_world(
            #constructing world based on Request
            World(
                world_create_request.name,
                world_create_request.description
            )
        )
    

    async def update_world(self, world_update_request: WorldUpdateRequest, id: uuid.UUID) -> World:

        return await self.world_repository.update_world(world_update_request, id)
    

    async def delete_world_by_id(self, id: uuid.UUID) -> None:
        await self.world_repository.delete_world_by_id(id)

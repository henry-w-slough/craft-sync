from models.world import World
from models.world_create_request import WorldCreateRequest
from repositories.world_repository import WorldRepository


class WorldService:


    def __init__(self, world_repository: WorldRepository):
        
        self.world_repository = world_repository


    async def add_world(self, world_create_request: WorldCreateRequest) -> World:

        #NOTE: creating the World here seperates the function of the Controller properly
        return await self.world_repository.add_world(
            World(
                world_create_request.name,
                world_create_request.description
            )
        )

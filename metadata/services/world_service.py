from models.world import World
from repositories.world_repository import WorldRepository


class WorldService:


    def __int__(self):
        

        self.world_repository = WorldRepository()


    def add_world(self, world: World) -> World:
        return self.world_repository.add_world(world)

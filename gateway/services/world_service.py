from ..repositories.world_repository import WorldRepository


class WorldService:


    def __init__(self, world_repository: WorldRepository) -> None:

        self.world_repository = world_repository
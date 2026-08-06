from ..repositories.world_repository import WorldRepository


class WorldService:


    def __init__(self, world_repository: WorldRepository) -> None:

        self.world_repository = world_repository


    async def add_world(self) -> None:
        return await self.world_repository.add_world()


    async def download_world_by_id(self) -> None:
        return await self.world_repository.download_world_by_id()


    async def update_world_by_id(self) -> None:
        return await self.world_repository.update_world_by_id()


    async def delete_world_by_id(self) -> None:
        return await self.world_repository.delete_world_by_id()

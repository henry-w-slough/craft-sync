import fastapi

from ..services.world_service import WorldService


class WorldController:


    def __init__(self, app: fastapi.FastAPI, world_service: WorldService) -> None:

        self.world_service = world_service

        app.post("/worlds/{id}", status_code=201)(self.add_world)
        app.delete("/worlds/{id}", status_code=204)(self.delete_world_by_id)
        app.put("/worlds/{id}", status_code=200)(self.update_world_by_id)
        app.get("/worlds/{id}", status_code=200)(self.download_world_by_id)


    async def add_world(self) -> None:
        return await self.world_service.add_world()


    async def download_world_by_id(self) -> None:
        return await self.world_service.download_world_by_id()


    async def update_world_by_id(self) -> None:
        return await self.world_service.update_world_by_id()


    async def delete_world_by_id(self) -> None:
        return await self.world_service.delete_world_by_id()





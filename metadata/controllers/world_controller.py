import fastapi

from responses.world_response import WorldResponse
from services.world_service import WorldService
from models.world import World


class WorldController:


    def __init__(self, app: fastapi.FastAPI) -> None:
        
        self.world_service = WorldService()
        
        app.post("/", status_code=201)(self.add_world)


    async def add_world(self, world: World) -> WorldResponse:

        return await self.world_service.add_world()
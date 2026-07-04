import fastapi
from services.world_service import WorldService

from models.world_response import WorldResponse
from models.world_create_request import WorldCreateRequest


class WorldController:


    def __init__(self, app: fastapi.FastAPI, world_service: WorldService) -> None:
        
        self.world_service = world_service
        
        app.post("/world", status_code=201)(self.add_world)


    async def add_world(self, request: WorldCreateRequest) -> WorldResponse:
        
        created_world = await self.world_service.add_world(request)

        return WorldResponse(
            name = created_world.name,
            description = created_world.description,
            date_added = created_world.date_added
        )
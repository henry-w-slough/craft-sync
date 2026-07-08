import fastapi
import uuid

from services.world_service import WorldService

from models.world_response import WorldResponse
from models.world_create_request import WorldCreateRequest


class WorldController():


    def __init__(self, app: fastapi.FastAPI, world_service: WorldService) -> None:
        
        self.world_service = world_service
        
        app.post("/worlds", status_code=201)(self.add_world)
        app.delete("/worlds/{id}", status_code=204)(self.delete_world_by_id)


    async def add_world(self, request: WorldCreateRequest) -> WorldResponse:
        
        added_world = await self.world_service.add_world(request)

        return WorldResponse(
            name = added_world.name,
            description = added_world.description,
            date_added = added_world.date_added,
            id = added_world.id
        )
    

    async def delete_world_by_id(self, id: uuid.UUID) -> None:
        await self.world_service.delete_world_by_id(id)
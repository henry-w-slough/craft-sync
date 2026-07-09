import fastapi
import uuid

from services.world_service import WorldService

from models.world_response import WorldResponse
from models.world_create_request import WorldCreateRequest
from models.world_update_request import WorldUpdateRequest


class WorldController():


    def __init__(self, app: fastapi.FastAPI, world_service: WorldService) -> None:
        
        self.world_service = world_service
        
        app.get("/worlds", status_code=200)(self.get_all_worlds)
        app.post("/worlds", status_code=201)(self.add_world)
        app.delete("/worlds/{id}", status_code=204)(self.delete_world_by_id)
        app.patch("/worlds/{id}", status_code=200)(self.update_world)


    async def get_all_worlds(self) -> list[WorldResponse]:

        all_worlds = await self.world_service.get_all_worlds()

        world_responses = []
        for world in all_worlds:
            world_responses.append(
                WorldResponse(
                    name=world.name,
                    description=world.description,
                    id=world.id,
                    date_added=world.date_added
                )
            )
        return world_responses


    async def add_world(self, request: WorldCreateRequest) -> WorldResponse:
        
        added_world = await self.world_service.add_world(request)

        return WorldResponse(
            name = added_world.name,
            description = added_world.description,
            date_added = added_world.date_added,
            id = added_world.id
        )
    

    async def update_world(self, request: WorldUpdateRequest, world_id: uuid.UUID) -> WorldResponse:

        updated_world = await self.world_service.update_world(request, world_id)

        return WorldResponse(
            name = updated_world.name,
            description = updated_world.description,
            date_added = updated_world.date_added,
            id = updated_world.id
        )
    

    async def delete_world_by_id(self, id: uuid.UUID) -> None:
        await self.world_service.delete_world_by_id(id)
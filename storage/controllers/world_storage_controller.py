from services.world_storage_service import WorldStorageService
from models.world_response import WorldResponse
from models.world_create_request import WorldCreateRequest

import fastapi


class WorldStorageController:

    
    def __init__(self, app:fastapi.FastAPI, world_storage_service: WorldStorageService) -> None:
        
        self.world_storage_service = world_storage_service

        app.post("/worlds")(self.add_world)


    def add_world(self, request: WorldCreateRequest) -> WorldResponse:

        return self.world_storage_service.add_world(request.id)
        


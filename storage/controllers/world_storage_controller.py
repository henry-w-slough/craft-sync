from services.world_storage_service import WorldStorageService

import fastapi


class WorldStorageController:

    
    def __init__(self, app:fastapi.FastAPI, world_storage_service: WorldStorageService) -> None:
        
        self.world_storage_service = world_storage_service


    def add_world(self) -> None:
        return self.world_storage_service.add_world()
        


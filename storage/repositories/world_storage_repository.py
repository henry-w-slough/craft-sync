from models.world_response import WorldResponse

import uuid
import os


class WorldStorageRepository:


    def __init__(self) -> None:
        pass


    def add_world(self, world_id: uuid.UUID) -> WorldResponse:
        
        os.makedirs(f"worlds/{world_id}")
        
        return WorldResponse(
            id = world_id
        )
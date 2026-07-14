from repositories.world_storage_repository import WorldStorageRepository
from models.world_response import WorldResponse

import uuid


class WorldStorageService:


    def __init__(self, world_storage_repository: WorldStorageRepository) -> None:
        
        self.world_storage_repository = world_storage_repository


    def add_world(self, world_id: uuid.UUID) -> WorldResponse:

        return self.world_storage_repository.add_world(world_id)
        
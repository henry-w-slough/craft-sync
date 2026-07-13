from repositories.world_storage_repository import WorldStorageRepository


class WorldStorageService:


    def __init__(self, world_storage_repository: WorldStorageRepository) -> None:
        
        self.world_storage_repository = world_storage_repository
        
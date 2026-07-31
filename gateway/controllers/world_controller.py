import fastapi

from ..services.world_service import WorldService


class WorldController:


    def __init__(self, app: fastapi.FastAPI, world_service: WorldService) -> None:

        self.world_service = world_service

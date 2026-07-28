import fastapi
import uvicorn

import config

from repositories.world_storage_repository import WorldStorageRepository
from services.world_storage_service import WorldStorageService
from controllers.world_storage_controller import WorldStorageController

from exceptions.global_exception_handler import register_exception_handlers


app = fastapi.FastAPI()


register_exception_handlers(app)


world_storage_repository = WorldStorageRepository()
world_storage_service = WorldStorageService(world_storage_repository)
world_storage_controller = WorldStorageController(app, world_storage_service)


if __name__ == "__main__":
    uvicorn.run(app, host=config.HOST, port=config.PORT)
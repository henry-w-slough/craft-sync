import fastapi
import uvicorn

import config

from exceptions import global_exception_handler

from metadata.controllers.world_metadata_controller import WorldMetadataController
from metadata.services.world_metadata_service import WorldMetadataService
from metadata.repositories.world_metadata_repository import WorldMetadataRepository

from lifespan import create_lifespan


world_repository = WorldMetadataRepository()


app = fastapi.FastAPI(lifespan=create_lifespan([world_repository]))


global_exception_handler.register_exception_handlers(app)


world_service = WorldMetadataService(world_repository)
world_controller = WorldMetadataController(app, world_service)


if __name__ == "__main__":
    uvicorn.run(app, host=config.HOST, port=config.PORT)



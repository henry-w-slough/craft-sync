import fastapi
import uvicorn

import config
from exceptions import global_exception_handler

from controllers.world_controller import WorldController
from services.world_service import WorldService
from repositories.world_repository import WorldRepository

from lifespan import create_lifespan


world_repository = WorldRepository()


app = fastapi.FastAPI(lifespan=create_lifespan([world_repository]))


global_exception_handler.register_exception_handlers(app)


world_service = WorldService(world_repository)
world_controller = WorldController(app, world_service)


if __name__ == "__main__":
    uvicorn.run(app, host=config.HOST, port=config.PORT)



import fastapi
import uvicorn
from contextlib import asynccontextmanager

import config
from exceptions import global_exception_handler

from controllers.world_controller import WorldController
from services.world_service import WorldService
from repositories.world_repository import WorldRepository


world_repository = WorldRepository()


@asynccontextmanager
async def lifespan(app: fastapi.FastAPI):
    for repository in [world_repository]:
        await repository.initialize_database()
    yield


app = fastapi.FastAPI(lifespan=lifespan)


global_exception_handler.register_exception_handlers(app)


world_service = WorldService(world_repository)
world_controller = WorldController(app, world_service)


if __name__ == "__main__":
    uvicorn.run(app, host=config.HOST, port=config.PORT)



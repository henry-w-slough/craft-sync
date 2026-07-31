import fastapi
import uvicorn

import config

from controllers.world_controller import WorldController
from services.world_service import WorldService
from repositories.world_repository import WorldRepository


app = fastapi.FastAPI()
 

world_repository = WorldRepository()

world_service = WorldService(world_repository)

world_controller = WorldController(app, world_service)


if __name__ == "__main__":
    uvicorn.run(app, port=config.PORT, host=config.HOST)
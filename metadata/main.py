import fastapi
import uvicorn

import config
from exceptions import global_exception_handler
from controllers.world_controller import WorldController


app = fastapi.FastAPI()


global_exception_handler.register_exception_handlers(app)


world_controller = WorldController(app)


if __name__ == "__main__":
    uvicorn.run(app, host=config.HOST, port=config.PORT)



import fastapi
import uvicorn

import config
from exceptions import global_exception_handler


app = fastapi.FastAPI()


global_exception_handler.register_exception_handlers(app)


if __name__ == "__main__":
    uvicorn.run(app, host=config.HOST, port=config.PORT)



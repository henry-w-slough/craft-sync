import fastapi
import uvicorn

import config


app = fastapi.FastAPI()


if __name__ == "__name__":
    uvicorn.run(app, host=config.HOST, port=config.PORT)
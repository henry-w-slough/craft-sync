import fastapi
import uvicorn

import config

#the api is truly just a test. This is not the real api, which will most likely be made in Java
#after the backend is complete.

app = fastapi.FastAPI()





if __name__ == "__main__":
    uvicorn.run(app, host=config.HOST, port=config.PORT)
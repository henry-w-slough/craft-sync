from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError


def register_exception_handlers(app: FastAPI):
    

    @app.exception_handler(RequestValidationError)
    async def validation_exception(request: Request, exc: RequestValidationError):
        return JSONResponse(status_code=422, content={"error": "The HTTP request given is formatted incorrectly or provides incorrect data and could not be read."})


    @app.exception_handler(Exception)
    async def general_error(request: Request, exc: Exception):
        return JSONResponse(status_code=500, content={"error": "Unhandled exception occurred."})
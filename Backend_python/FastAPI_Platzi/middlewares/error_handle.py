from starlette.middleware.base import BaseHTTPMiddleware, DispatchFunction, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response
from starlette.types import ASGIApp
from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse

class ErrorHandler(BaseHTTPMiddleware):
    def __init__(self, app: FastAPI) -> None:  #constructor
        super().__init__(app)

    async def dispatch(self, request: Request, call_next) -> Response | JSONResponse:
        try:
            return await call_next(request)  #si no ocurre ningún error va a retornar a la siguiente llamada
        except Exception as e:  #Atrapamos el error
            return JSONResponse(status_code=500, content= {'error':str(e)})

from fastapi import APIRouter, FastAPI, Body, Path, Query, HTTPException, status, Request
from schemas.user import User
from fastapi.security import HTTPBearer
from jwt import encode, decode
from utils.jwt_manager import validate_token


class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        print(auth.credentials)
        data = validate_token(auth.credentials)
        print(data)
        if data['email'] != "admin@gmail.com":
            raise HTTPException(status_code=403, detail=("credenciales inválidas"))
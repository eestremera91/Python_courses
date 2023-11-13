
from fastapi import APIRouter, Body, Path, Query, HTTPException, status, Request
from schemas.user import User
from utils.jwt_manager import create_token


router = APIRouter(prefix="/login",
                   tags=["jwt"],
                   responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})

@router.post('/')
async def login(user:User):
    if user.email == "admin@gmail.com" and user.password == "admin":
        token: str = create_token(user.dict())
        return token
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Credenciales de autenticación inválidas")
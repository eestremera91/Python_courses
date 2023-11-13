from typing import Any, Coroutine, Optional
from fastapi import APIRouter, FastAPI, Body, Path, Query, HTTPException, status, Request
from schemas.user import User
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jwt import encode, decode
from dotenv import load_dotenv
import os
#usar un token definido, menor seguridad

#def create_token(data: dict):
#    token: str = encode(payload=data, key="my_key_from_babilonia", algorithm="HS256")
#    return token

#generar un token aleatorio, mayor seguridad


load_dotenv()

def create_token(data: dict) -> str:
    name=os.getenv('API_KEY')
    token: str = encode(payload=data,  #La información contenida en el payload es facilmente detectable, por lo que es importante que no vaya información sencible o podra ser hackeada
                        key = os.getenv('API_KEY'),
                        algorithm="HS256"
                        )
    return token

def validate_token(token: dict) -> str:
    token: str = decode(token,  
                        key = os.getenv('API_KEY'),
                        algorithms=['HS256']
                        )
    return token




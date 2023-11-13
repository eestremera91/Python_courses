# Clase en vídeo: https://youtu.be/_y9qQZXE24A?t=14094

### Users API con autorización OAuth2 básica ###

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordRequestForm #para gestionar contreseñas:se encarga de gestionar la autenticación (usuario y contraseña)
from fastapi.security import OAuth2PasswordBearer      #para la forma en la que se va a enviar a nuestra API los criterios de autentificación

router = APIRouter(prefix="/basicauth",
                   tags=["basicauth"],
                   responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})

oauth2 = OAuth2PasswordBearer(tokenUrl="login")


class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool


class UserDB(User):
    password: str


users_db = {                                      #cree una base de datos (esto es de prueba para el proyecto)
    "eestremera91"  :{    
        "username"  : "eestremera91",
        "full_name" : "Ernesto Estremera",
        "email"     : "ernesto@gmail.com",
        "disabled"  : False,
        "password"  : "1234"
    },
    "eestremera912" :{    
        "username"  : "eestremera912",
        "full_name" : "Ernesto Estremera2",
        "email"     : "ernesto2@gmail.com",
        "disabled"  : True,
        "password"  : "5678"
    }
}

def search_user_db(username: str):                      #busco si el usuario está en la base de datos
    if username in users_db :
        return UserDB(**users_db[username])  #estos asterizcos es porque no le especifica la cantidad de parámetros que le pueden entrar
    
def search_user(username: str):                      #busco si el usuario está en la base de datos
    if username in users_db:
        return User(**users_db[username])  #estos asterizcos es porque no le especifica l cantidad de parámetros que le pueden entrar
    



async def current_user(token: str = Depends(oauth2)):
    user = search_user(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales de autenticación inválidas",
            headers={"WWW-Authenticate": "Bearer"})

    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuario inactivo")

    return user


@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no es correcto")

    user = search_user_db(form.username)
    if not form.password == user.password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="La contraseña no es correcta")

    return {"access_token": user.username, "token_type": "bearer"}


@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user

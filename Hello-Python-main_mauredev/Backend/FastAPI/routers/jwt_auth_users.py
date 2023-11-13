# Clase en vídeo: https://youtu.be/_y9qQZXE24A?t=17664

### Users API con autorización OAuth2 JWT ###

#Autentificación con encriptación, mucho más seguro: JWT: Jason Web token
#paquetes necesarios: pip install "passlib[bcrypt]"
#                     pip install "python-jose[cryptography]"        

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordRequestForm # para gestionar contraseñas:se encarga de gestionar la autenticación (usuario y contraseña)
from fastapi.security import OAuth2PasswordBearer      # para la forma en la que se va a enviar a nuestra API los criterios de autentificación
from jose import jwt, JWTError                         # para hacer la encriptación.el segundo gestiona los errores
from passlib.context import CryptContext               # para contexto de encriptación
from datetime import datetime, timedelta               # para tener acceso a la fecha y hora para calcular cuanto riempo está conectado

ALGORITHM = "HS256"                                  # algoritmo de encriptación que utilizaremos (hay otros que se pueden ver en la docuemntación)
ACCESS_TOKEN_DURATION = 10                           # PARA ESPECIFICAR CUANTO TIEMPO SERÁ VÁLIDO EL TOKEN en  minutos
crypt     =  CryptContext(schemes= ["bcrypt"])       # definir contexto de encriptación
SECRET_KEY =  "f0426b02839f903d2730bfdd94043c433eedb0efb747eab738de637398ad5ffd"  # definir la semilla de nuestra encriptación para nuestra aploicación. Podemos escribir 
                                                                                  # cualquier cosa o desde la ventana de comando con : openssl rand -hex 32
ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION = 1
SECRET = "201d573bd7d1344d3a3bfce1550b69102fd11be3db6d379508b6cccc58ea230b"

router = APIRouter(prefix="/jwtauth",
                   tags=["jwtauth"],
                   responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

crypt = CryptContext(schemes=["bcrypt"])


class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool


class UserDB(User):
    password: str


users_db = {                                      # cree una base de datos (esto es de prueba para el proyecto)
    "eestremera91":{    
        "username": "eestremera91",
        "full_name": "Ernesto Estremera",
        "email" : "ernesto@gmail.com",
        "disabled": False,
        "password": "$2a$12$MnR8B99MpDlwrx59vki.VO5/mu4IRn.bY.Oy8JoIt0BWNra8I3wVe" # guardo la contraseña encriptada con el contexto de encriptación que se
    },                                                                             # va a usar (en este caso "bcrypt"(lo escribo en el buscador y busco un coversor)). 
    "eestremera912":{    
        "username": "eestremera912",
        "full_name": "Ernesto Estremera2",
        "email" : "ernesto2@gmail.com",
        "disabled": False,
        "password": "$2a$12$zERtO0XuMbOYsMa9cc2JWuQexHUG62np2AJcXEa3Rg73HQdw3jiMG"
    }
}


def search_user_db(username: str):                      # busco si el usuario está en la base de datos
    if username in users_db :
        return UserDB(**users_db[username])  # estos asterizcos es porque no le especifica l cantidad de parámetros que le pueden entrar
    
def search_user(username: str):                      # busco si el usuario está en la base de datos
    if username in users_db :
        return User(**users_db[username])  # estos asterizcos es porque no le especifica l cantidad de parámetros que le pueden entrar


async def auth_user(token: str = Depends(oauth2)):       # función que se encargará de buscar el usuario

    exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Credenciales de autenticación inválidas",
        headers={"WWW-Authenticate": "Bearer"})

    try:  # manejo las exepciones que puede lanzar un error por no enconrtrar nada
        username = jwt.decode(token, SECRET, algorithms=[ALGORITHM]).get("sub")  # decodifica el hash y devuelve el Json que se encriptó antes y  
                                                                                 # tomo el nombre de usuario que se guardó en la clave "sub"
        if username is None:
            raise exception

    except JWTError:
        raise exception

    return search_user(username)


async def current_user(user: User = Depends(auth_user)):
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

# crypt.verify(form.password,user.password)     # verificar las contraseñas original vs la incertada. Nos devuelve T/F si las contraseñas son iguales
    if not crypt.verify(form.password, user.password):    
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="La contraseña no es correcta")
#  expire_date =   datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_DURATION)  # determina hasta cuando va a durar el token
    access_token = {"sub": user.username,
                    "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_DURATION)}

    return {"access_token": jwt.encode(access_token, SECRET, algorithm=ALGORITHM), "token_type": "bearer"} # Encripta el access token ahora vamos a generar un acces
                                                                                                           # token de forma segura, encriptada también


@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user

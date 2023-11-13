# Clase en vídeo: https://youtu.be/_y9qQZXE24A?t=5382

### Users API ###

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

# Inicia el server: uvicorn users:app --reload

router = APIRouter(prefix = "/users", # esto incluye el prefix en la URL   users
                   tags=["users"],)


class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int


users_list = [User(id=1 ,name= "Ernesto", surname= "moure" , url="https://moure.dev"   , age=35),
              User(id=2 ,name= "pepe"   , surname= "pepin" , url="https://mouredev.com",age=30),
              User(id=3 ,name= "carlos" , surname= "carlin", url="https://mourepy.dev" ,age=25)]


@router.get("/usersjson")  #esta operación está en '/', esto significa que es la raíz de donde se ejecuta mi API (llama a localHost). 
               #Lógicamente no poidremos crear más de una operación get en la raíz. Se craemos varias se ejecuta la primera
async def usersjson(): 
    return [{"name": "Ernesto", "surname": "moure" , "url":"https://moure.dev"   , "age":35},
            {"name": "pepe"   , "surname": "pepin" , "url":"https://mouredev.com", "age":30},
            {"name": "carlos" , "surname": "carlin", "url":"https://mourepy.dev" , "age":25}]


@router.get("/users") #esta operación está en '/', esto significa que es la raíz de donde se ejecuta mi API (llama a localHost). 
               #Lógicamente no poidremos crear más de una operación get en la raíz. Se craemos varias se ejecuta la primera
async def users():
    return users_list

# Path 
@router.get("/user/{id}")   #tomaremos un usuario por uno de los campos de los objetos (en este caso el ID)
async def user(id: int):
    return search_user(id)

# Query
@router.get("/user/")  #tomaremos un usuario pasándole el parámetro por query:se llamaría: http://127.0.0.1:8000/user/?id=1
async def user(id: int):
#async def user(id: int, name:str): #tomaremos un usuario pasándole el ID el el name por query:se llamaría: http://127.0.0.1:8000/user/?id=1&name=Ernesto
    return search_user(id)


# Clase en vídeo: https://youtu.be/_y9qQZXE24A?t=8529


@router.post("/user/", response_model=User, status_code=201)    #incertar un usuario
async def user(user: User):
    if type(search_user(user.id)) == User:        #compruebo si el usuario ya existe
        raise HTTPException(status_code=404, detail="El usuario ya existe")

    users_list.append(user)                          #añado al usuario
    return user


#operaciones put    #actualizar el usuario
@router.put("/user/")
async def user(user: User):

    found = False

    for index, saved_user in enumerate(users_list):    #busco el usuario en la lista
        if saved_user.id == user.id:
            users_list[index] = user
            found = True

    if not found:
        return {"error": "No se ha actualizado el usuario"}

    return user


@router.delete("/user/{id}")
async def user(id: int):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True

    if not found:
        return {"error": "No se ha eliminado el usuario"}


def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)        #función filter de orden superior ya definida en python
    try:                                                          #esto es para manejar las exepciones (en este caso que no haya usuarios con ese ID y que no pete el servidor)
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}

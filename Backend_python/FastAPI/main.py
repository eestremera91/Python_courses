# Clase en vídeo: https://youtu.be/_y9qQZXE24A

### Hola Mundo ###

# Documentación oficial: https://fastapi.tiangolo.com/es/

# Instala FastAPI: pip install "fastapi[all]"

from fastapi import FastAPI
from routers import products, users, basic_auth_users, jwt_auth_users, users_db
from fastapi.staticfiles import StaticFiles

app = FastAPI()  #instanciamos FastApi

#routers: esto es para enlazar otras APIs a estas como API principal
# Clase en vídeo: https://youtu.be/_y9qQZXE24A?t=12475
app.include_router(products.router)
app.include_router(users.router)

# Clase en vídeo: https://youtu.be/_y9qQZXE24A?t=14094
app.include_router(basic_auth_users.router)

# Clase en vídeo: https://youtu.be/_y9qQZXE24A?t=17664
app.include_router(jwt_auth_users.router)

# Clase en vídeo: https://youtu.be/_y9qQZXE24A?t=20480
app.include_router(users_db.router)

# Clase en vídeo: https://youtu.be/_y9qQZXE24A?t=13618
app.mount("/static", StaticFiles(directory="static"), name="static") #para exponer algún recurso estático(imagenes, documentos, etc) 
                                    #http://127.0.0.1:8000/static/image/imagen.png
                                    #http://127.0.0.1:8000/static/Documents/137177%20Ernesto%20Estremera-R.pdf


# Url local: http://127.0.0.1:8000


@app.get("/")     #esta operación está en '/', esto significa que es la raíz de donde se ejecuta mi API (llama a localHost). 
                  #Lógicamente no podremos crear más de una operación get en la raíz. Si creamos varias se ejecuta la primera
async def root():
    return "Hola FastAPI!"

# Url local: http://127.0.0.1:8000/url


@app.get("/url")
async def url(): 
    return {"url": "https://mouredev.com/python"}

# Inicia el server: uvicorn main:app --reload
# Detener el server: CTRL+C  

# Documentación con Swagger: http://127.0.0.1:8000/docs
# Documentación con Redocly: http://127.0.0.1:8000/redoc

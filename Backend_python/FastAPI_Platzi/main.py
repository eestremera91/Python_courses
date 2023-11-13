from fastapi import FastAPI
from routers import movies, user
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.security import HTTPBearer
from middlewares.error_handle import ErrorHandler


app = FastAPI()  #instanciamos FastApi
app.title = "aplicación con FastAPI"
app.version = "1.0"
app.add_middleware(ErrorHandler)

#routers: esto es para enlazar otras APIs a estas como API principal
@app.get('/', tags=['home'])
async def message():
    return HTMLResponse('<h1> Hello World</h1')

app.include_router(user.router)
app.include_router(movies.router)

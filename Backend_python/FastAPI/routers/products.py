# Clase en vídeo: https://youtu.be/_y9qQZXE24A?t=12475

### Products API ###

from fastapi import APIRouter

router = APIRouter(prefix="/products",
                   tags=["products"],
                   responses={404: {"message": "No encontrado"}})

products_list = ["Producto 1", "Producto 2",
                 "Producto 3", "Producto 4", "Producto 5"]


@router.get("/")  #esta operación está en '/', esto significa que es la raíz de donde se ejecuta mi API (llama a localHost). 
async def products():
    return products_list


@router.get("/{id}")   #esta operación está en '/', esto significa que es la raíz de donde se ejecuta mi API (llama a localHost). 
async def products(id: int):
    return products_list[id]

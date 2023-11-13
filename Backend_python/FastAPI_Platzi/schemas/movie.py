from pydantic import BaseModel, Field
from typing import Optional

# Se crea clase Movie, que hereda de BaseModel

class Movie(BaseModel):
#    id: int | None = None     # de esta manera se le dice que puede ser opcional el parámetro
    id: Optional[int] = None    # de esta manera se le dice que puede ser opcional el parámetro
    title: str = Field(default= "No nombre", min_length=1,max_length=50)  #validación de los campos
    overview:str
    rating: float 
    year: str 
    category: str 

#Poner una configuración inicial del esquema
    class Config:
        schema_extra = {
                "example": 
                    {
                        "id": 1,"title": "Nombre Pelicula","overview": "This movie is about...", "rating": 7.8, "year": "2009", "category": "Acción"
                    }
            }
        
      
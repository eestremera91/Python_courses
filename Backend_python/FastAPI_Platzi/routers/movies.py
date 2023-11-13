from fastapi import APIRouter, FastAPI, Body, Path, Query, HTTPException, status, Depends
from pydantic import BaseModel, Field  
from schemas.movie import Movie
from data.movies import movies
from data.users import users
from fastapi.responses import HTMLResponse, JSONResponse #para que devuelva un HTML Y jSON response
from typing import Optional, List   #para usar otra manera de decir que será opcional el parámetro
from middlewares.jwt_bearer import JWTBearer
from config.database import session, engine, base  #importo esto desde config
from models.movie import Movie as Movie_model  #como ya tengo un esquema que se llama Movie lo redefino para que no se confunda al llamarlo
from fastapi.encoders import jsonable_encoder #sirve para llevarlo a formato json
from services.movie import MovieService


router = APIRouter(prefix="/movies",
                   tags=["movies"],
                   responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})

base.metadata.create_all(bind=engine)


@router.get('', status_code=status.HTTP_200_OK)
def get_movies():  # -> List[Movie] sirve para decirnos el tipo de respuesta que vamos a obtener 
    db     = session()     #crear una sesión para conectarme a la BD
    # esto es para hacerlo sin services
    #  result =  MovieService(db).get_movies()  #especifico la tabla que quiero consultar y la leo y filtro para hacer búsqueda y tomo el primer resultado
    #esto es utilizando los services
    result = MovieService(db).get_movies()
    #para devolver el listado de movies de la base de datos
    return jsonable_encoder(result)
    # para devolver el listado de movies de from data.movies import movies que es un listado en diccionario de las películas
    return movies
    #return JSONResponse(content=movies)  #para devolverme el estado de películas en un json (Por defecto FastAPI convierte los valores retornados a JSON, 
                                         #transformando y usando por detras JSONResponse. No sería del todo necesario usar JSONResponse si es que no es 
                                         #para un caso especifico. https://fastapi.tiangolo.com/advanced/response-directly/)


# Path
@router.get('/{id}')    #buscar por un parámetro (en este caso el ID)
def get_movie(id: int) :  # el Path sirve para validar los parámetros de ruta, en este caso estará entre 1 y 5000
    db     = session()     #crear una sesión para conectarme a la BD
    # esto es para hacerlo sin services
    #  result = db.query(Movie_model).filter(Movie_model.id == id).first()  #especifico la tabla que quiero consultar y la leo y filtro para hacer búsqueda y tomo el primer resultado
    #esto es utilizando los services
    result = MovieService(db).get_movie(id)
    
    if not result:
        raise HTTPException(status_code=404, detail="La entrada no existe")   
    #para devolver el listado de movies de la base de datos
    return jsonable_encoder(result)
    # para buscar y devolver el listado de movies de from data.movies import movies que es un listado en diccionario de las película
    for item in movies:
        if item["id"] == id:
            return item
            #return JSONResponse(content=item) 
    return {"error": "Película no encontrada"}

# Query
@router.get('/')    #buscar por un parámetro (en este caso el ID)
def get_movie_by_category(category:str = Query(min_length=1,max_length=25)):  # dentro del paréntesis van los datos que requiero por Query (para un parámetro 
                                                                               # requerido). el Query sirve para validar los parámetros de Query    
    db     = session()     #crear una sesión para conectarme a la BD
    
    # esto es para hacerlo sin services
    # result = db.query(Movie_model).filter(Movie_model.category == category).all()  #especifico la tabla que quiero consultar y la leo y filtro para hacer búsqueda y tomo el primer resultado
    #esto es utilizando los services
    result = MovieService(db).get_movie_category(category)
    if not result:
        raise HTTPException(status_code=404, detail="No se encontraron peliculas de esa categoría")    
    #para devolver el listado de movies de la base de datos
    return jsonable_encoder(result)  

    # para buscar y devolver el listado de movies de from data.movies import movies que es un listado en diccionario de las película                                                                
    for item in movies:                 # Lo mismo en una línea: return [item for item in movies if item["category"] == category]
        if item["category"] == category:
            return item
    return {"error": "Categoría no encontrada"}


@router.post('/')
def create_movie(movie: Movie):
    db        = session()     #crear una sesión para conectarme a la BD

    # esto es para hacerlo sin services
    # new_movie = Movie_model(**movie.dict())  #lo convierto a diccionario y los asteriscos extraen los atributos y los pasa como parámetros
    # db.add(new_movie)
    # actualizo la bd 
    # db.commit()

    #esto es utilizando los services
    new_movie = MovieService(db).add_movie(movie)

    # para buscar y devolver el listado de movies de from data.movies import movies que es un listado en diccionario de las película
    # movies.append(movie.dict())
    return {"msg": "Película añadida"}


@router.put('/{id}')
def modify_movie(id: int, movie: Movie):
    db     = session()     #crear una sesión para conectarme a la BD
    # esto es para hacerlo sin services
    #    result = db.query(Movie_model).filter(Movie_model.id == id).first() #verifico si la película existe
    #    if not result:
    #       raise HTTPException(status_code=404, detail="La entrada no existe")  
    #    result.title =movie.title
    #    result.overview = movie.overview
    #    result.rating = movie.rating
    #    result.year  = movie.year
    #    result.category = movie.category
    #    db.commit()
    #    result = db.query(Movie_model).filter(Movie_model.id == id).first()

    #esto es utilizando los services
    new_movie = MovieService(db).modify_movie(movie, id)
    return jsonable_encoder(new_movie)

    # para buscar y modificar el listado de movies de from data.movies import movies que es un listado en diccionario de las película
    for item in movies:       
        if item["id"] == id:
            item["title"] = movie.title
            item["rating"] = movie.rating
            item["year"] = movie.year
            item["category"] = movie.category
            return {"msg": "Película modificada"}
    return {"error": "Película no encontrada"}

@router.delete('/{id}')
def delete_movie(id: int):
    db     = session()     #crear una sesión para conectarme a la BD
    result = MovieService(db).delete_movie(id)
    return result
     # para buscar y modificar el listado de movies de from data.movies import movies que es un listado en diccionario de las película
    # for item in movies:       
    #        if item["id"] == id:
    #            movies.remove(item)
    #            return {"msg": "Película eliminada"}
    #    return {"error": "Película no encontrada"}

from models.movie import Movie as Movie_model 
from schemas.movie import Movie
from fastapi import HTTPException

class MovieService():
    def __init__(self, db) -> None:
        self.db = db

    def get_movies(self):
        result = self.db.query(Movie_model).all()
        return result
    
    def get_movie(self, id):
        result = self.db.query(Movie_model).filter(Movie_model.id == id).first()
        return result
    
    def get_movie_category(self, category):
        result = self.db.query(Movie_model).filter(Movie_model.category == category).all()
        return result
    
    def add_movie(self, movie = Movie):
        new_movie = Movie_model(**movie.dict())
        self.db.add(new_movie)
        self.db.commit()
        return new_movie
    
    def modify_movie(self, movie: Movie, id:int):
        result = self.db.query(Movie_model).filter(Movie_model.id == id).first() #verifico si la película existe
        if not result:
           raise HTTPException(status_code=404, detail="La entrada no existe")  
        result.title =movie.title
        result.overview = movie.overview
        result.rating = movie.rating
        result.year  = movie.year
        result.category = movie.category
        self.db.commit()
        new_movie = self.db.query(Movie_model).filter(Movie_model.id == id).first()
        return new_movie
    
    def delete_movie(self, id):
        result = self.db.query(Movie_model).filter(Movie_model.id == id).first()
        if not result:
           raise HTTPException(status_code=404, detail="La entrada no existe")
        self.db.delete(result)
        self.db.commit()      
        return {"msg": "Película eliminada"}

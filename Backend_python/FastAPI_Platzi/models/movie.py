from config.database import base
from sqlalchemy import Column, Integer, String, Float  

#https://fastapi.tiangolo.com/es/tutorial/sql-databases/#install-sqlalchemy
class Movie(base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key = True)
    title = Column(String)
    overview = Column(String)
    rating = Column(Float) 
    year = Column(String) 
    category = Column(String) 
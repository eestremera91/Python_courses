import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base #sirve para manipular todas las tablas de las bases de datos

sqlite_file_name = "../db/Database.sqlite"  #Nombre de la BD
base_dir = os.path.dirname(os.path.realpath(__file__))  # Esto me lee el directorio de este archivo

database_url = f"sqlite:///{os.path.join(base_dir, sqlite_file_name)}"  #crea el url de la base de datos
engine = create_engine(database_url, echo=True) #motor de la base de datos
session = sessionmaker(bind=engine) #sesión para conectarme a la BD
base = declarative_base()  #para el manejo de la BD
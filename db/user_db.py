from typing import List
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from db.db_connection import Base, engine

    
class UserInDB(Base):
    __tablename__ = "Usuario"
    
    id_user = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)
    apellido = Column(String)
    correo = Column(String)
    password = Column(String)
    
Base.metadata.create_all(bind=engine)
    
    
'''def update_user(user_in_db: UserInDB):
    database_users[user_in_db.id_habitacion] = user_in_db
    return user_in_db'''
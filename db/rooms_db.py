from typing import Dict
from pydantic import BaseModel
from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, String
from db.db_connection import Base, engine

    
class RoomsInDB(Base):
    __tablename__ = "rooms"
    id_room = Column(Integer, primary_key=True, autoincrement=True)
    numero = Column(Integer)
    piso = Column(Integer)
    descripcion = Column(String)
    caracteristicas = Column(String)
    
Base.metadata.create_all(bind=engine)


'''def get_room(id_habitacion: int):
    if id_habitacion in database_rooms.keys():
        return database_rooms[id_habitacion]
    else:
        return None'''
    
def update_room(room_in_db: RoomsInDB):
    database_rooms[room_in_db.id_habitacion] = room_in_db
    return room_in_db
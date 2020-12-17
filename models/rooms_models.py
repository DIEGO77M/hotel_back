from pydantic import BaseModel

class RoomIn(BaseModel):
    id_room: int
    
    
class RoomOut(BaseModel):
    id_room: int
    numero: int
    piso: int
    descripcion: str
    caracteristicas: str
    precio_diario: int
    tipo: str
    
    class Config:
        orm_mode = True
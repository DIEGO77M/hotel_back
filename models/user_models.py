from pydantic import BaseModel


class UserIn(BaseModel):
    nombre: str
    apellido: str
    correo: str
    password: str
    
    
class UserOut(BaseModel):
    id_user: int
    nombre: str
    apellido: str
    
    class Config:
        orm_mode = True
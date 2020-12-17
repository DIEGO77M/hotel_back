from typing import List
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from db.db_connection import get_db
from db.user_db import UserInDB
from db.rooms_db import RoomsInDB
from models.user_models import UserIn, UserOut
from models.rooms_models import RoomIn, RoomOut

router = APIRouter()

@router.get("/user/{id_user}", response_model=UserOut)
async def get_user(id_user: int, db: Session = Depends(get_db)):
    
    user_in_db = db.query(UserInDB).get(id_user)
    
    if user_in_db == None:
        raise HTTPException(status_code=404,
                            detail="El usuario no existe")
    return user_in_db


@router.get("/users/", response_model=UserOut)
async def find_all_users():
    query = find_all_users.select()
    return await UserInDB.fetch_all(query)


@router.post("/user/", response_model=UserIn)
async def create_user(user: UserIn, db: Session = Depends(get_db)): 
    user_in_db = UserInDB(nombre=user.nombre, apellido=user.apellido, correo=user.correo, password=user.password) 
    db.add(user_in_db)
    db.commit()
    db.refresh(user_in_db)
    return user_in_db



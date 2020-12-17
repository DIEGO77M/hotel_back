from typing import List
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from db.db_connection import get_db
from db.user_db import UserInDB
from db.rooms_db import RoomsInDB
from models.user_models import UserIn, UserOut
from models.rooms_models import RoomIn, RoomOut

router = APIRouter()

@router.get("/rooms/{id_room}", response_model=RoomOut)
async def get_room(id_room: int, db: Session = Depends(get_db)):
    
    room_in_db = db.query(UserInDB).get(id_room)
    if room_in_db == None:
        raise HTTPException(status_code=404,
                            detail="La habitación no existe")
        
    return room_in_db
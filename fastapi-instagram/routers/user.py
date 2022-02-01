from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from DB.database import get_db
from DB import db_user
from schemas import (
    UserBase, UserDisplay
)

router = APIRouter(
    prefix='/user',
    tags=['user']
)


@router.post('', response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)

from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from hashing import Hash
from DB.models import (
    DbUser
)
from schemas import (
    UserBase, UserDisplay
)


def search_user(db: Session, username: str):
    if db.query(DbUser).filter(DbUser.username == username).first():
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail='Someone use same username.\nPlease change username'
        )


def create_user(db: Session, request: UserBase):
    search_user(db, request.username)
    new_data = DbUser(
        username=request.username,
        email=request.email,
        password=Hash.bcrypt(request.password)
    )
    db.add(new_data)
    db.commit()
    db.refresh(new_data)
    return new_data


def get_user_by_username(db: Session, username: str):
    user = db.query(DbUser).filter(DbUser.username == username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'{username} is not exist')
    return user

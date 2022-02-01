from fastapi import APIRouter, UploadFile, File, Depends
from typing import List
from sqlalchemy.orm import Session
from oauth2 import get_current_user
from schemas import PostBase, PostDisplay, UserAuth
from DB.database import get_db
from DB import db_post

router = APIRouter(
    prefix='/post',
    tags=['post']
)


@router.post('', response_model=PostDisplay)
def create_post(request: PostBase, db: Session = Depends(get_db), current_user: UserAuth = Depends(get_current_user)):
    return db_post.create_post(db, request)


@router.get('/all', response_model=List[PostDisplay])
def get_all_post(db: Session = Depends(get_db)):
    return db_post.get_all_post(db)


@router.post('/image')
def upload_image(db: Session = Depends(get_db), request: UploadFile = File(...), current_user: UserAuth = Depends(get_current_user)):
    return db_post.upload_image(request)

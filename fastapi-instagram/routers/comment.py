from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from DB.database import get_db
from DB import db_comment
from schemas import Comment
from DB import db_comment

router = APIRouter(
    prefix='/comment',
    tags=['comment']
)


@router.post('')
def create_comment(request: Comment, db: Session = Depends(get_db)):
    return db_comment.create_comment(request, db)

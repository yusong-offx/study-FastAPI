from sqlalchemy.orm import Session
from schemas import Comment
from DB.models import DbComment
from schemas import Comment
import datetime


def create_comment(request: Comment, db: Session):
    new_comment = DbComment(user_id=request.username, timestamp=datetime.datetime.now(),
                            post_id=request.post_id, comment=request.comment)
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment

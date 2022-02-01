from fastapi import HTTPException, UploadFile, status, File
from sqlalchemy.orm import Session
from DB.models import DbPost
from schemas import PostBase, PostDisplay
from datetime import datetime
from string import ascii_letters
from random import choices
from shutil import copyfileobj
image_url_type = ['absolute', 'relative']


def create_post(db: Session, request: PostBase):
    if request.image_url_type not in image_url_type:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail='This option is not supported (absolute/relative)'
        )
    new_data = DbPost(
        image_url=request.image_url,
        image_url_type=request.image_url_type,
        caption=request.caption,
        timestamp=datetime.now(),
        user_id=request.creator_id,
    )
    db.add(new_data)
    db.commit()
    db.refresh(new_data)
    return new_data


def get_all_post(db: Session):
    return db.query(DbPost).all()


def upload_image(image: UploadFile):
    random_ascii = ''.join(choices(ascii_letters, k=10)) + '.'
    filename = image.filename.rsplit('.', 1)
    path = 'public/images/' + random_ascii.join(filename)
    with open(path, 'xb') as buf:
        copyfileobj(image.file, buf)
    return {'filename': path}

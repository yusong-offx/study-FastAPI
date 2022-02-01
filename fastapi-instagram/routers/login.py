from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from DB.database import get_db
from DB.models import DbUser
from oauth2 import create_access_token
from hashing import Hash

router = APIRouter(
    tags=['Authentication']
)


@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(DbUser).filter(DbUser.username == request.username).first()
    if not user or not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='No user or Incorrect password')
    access_token = create_access_token(data={'username': request.username})
    return {
        'access_token': access_token,
        'token_type': 'bearer',
        'username': user.username
    }

from schemas import Test
from typing import List
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, Header
from DB.database import engine
from DB import models
from routers import (
    user, post, login, comment
)

from fastapi import Request, Depends
from DB.database import get_db
from sqlalchemy.orm import Session
from DB.models import DbUser, DbComment

models.Base.metadata.create_all(engine)

app = FastAPI()
app.include_router(login.router)
app.include_router(user.router)
app.include_router(post.router)
app.include_router(comment.router)

app.mount("/public/images", StaticFiles(directory='public/images'), name="images")


@app.get('/abc', response_model=List[Test])
def index(db: Session = Depends(get_db)):
    a = db.query(DbUser).all()
    print(f'index : {a}')
    return a

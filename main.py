from fastapi import FastAPI, status, Response
from db import models
from db.database import engine

from router import blog

import pydantic

models.Base.metadata.create_all(engine)

app = FastAPI()

app.include_router(blog.router)


@app.get('/', tags=['main'])
def index():
    return 'Welcome'

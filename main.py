from fastapi import FastAPI
from database import engine
from router.sell import models, schema

models.Base.metadata.create_all(engine)
app = FastAPI()

@app.get('/')
def index():
	return {'detail' : 'init project'}

@app.post('/')
def create(request: schema.test):
	return request

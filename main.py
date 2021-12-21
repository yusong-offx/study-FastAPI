# https://youtu.be/7t2alSnE2-I?t=2762

from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
	return {'First' : 'index'}

@app.get('/{id}')
def id(id: str):
	return {'id' : id}
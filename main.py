from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import engine, SessionLocal
from router.sell import schema

import models

models.Base.metadata.create_all(engine)
def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()

app = FastAPI()

@app.get('/')
def index():
	return {'detail' : 'init project'}

@app.get('/all')
def get_all(db: Session = Depends(get_db)):
	return db.query(models.Sell).all()

@app.post('/test')
def create(request:schema.test, db: Session = Depends(get_db)):
	new_data = models.Sell(name=request.name)
	db.add(new_data)
	db.commit()
	#db.refresh(new_data)
	return 'success'

@app.get('/test/{id}')
def get_name(id: int, db: Session = Depends(get_db)):
	return db.query(models.Sell).filter(models.Sell.id == id).all()

@app.delete('/test/{id}')
def delet_name(id: int, db: Session = Depends(get_db)):
	for i in range(1, id+1):
		db.query(models.Sell).filter(models.Sell.id == i).delete(synchronize_session=False)
	db.commit()

import schemas
from typing import List
from sqlalchemy.orm import Session
from db.database import get_db
from db import models
from fastapi import FastAPI, APIRouter, Response, status, Query, Depends
from pydantic import BaseModel
from typing import Optional


router = APIRouter(
    prefix='/blog',
    tags=['blog']
)


@router.post('/')
def create_parent(request: schemas.ParentsBase, db: Session = Depends(get_db)):
    new_parents = models.Parents(name=request.name)
    db.add(new_parents)
    db.commit()
    db.refresh(new_parents)
    return 'ok'


@router.get('/all')
def a(db: Session = Depends(get_db)):
    return db.query(models.Parents).all()


@router.get('/all/{id}')
def a(id: int, db: Session = Depends(get_db)):
    r = db.query(models.Parents).filter(models.Parents.id == id).first()
    print(r.children)
    return r


@router.post('/children/')
def create_parent(request: schemas.ChildrenBase, db: Session = Depends(get_db)):
    new_Children = models.Children(name=request.name, parent_id=request.p_id)
    db.add(new_Children)
    db.commit()
    db.refresh(new_Children)
    return 'ok'


@router.get('/children/all')
def a(db: Session = Depends(get_db)):
    return db.query(models.Children).all()


@router.get('/children/all/{id}')
def a(id: int, db: Session = Depends(get_db)):
    r = db.query(models.Children).filter(models.Children.id == id).first()
    return r

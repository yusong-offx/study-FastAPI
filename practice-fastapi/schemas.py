from pydantic import BaseModel
from fastapi import Body


class ParentsBase(BaseModel):
    name: str = Body(None, max_length=10)


class CD(BaseModel):
    id: int
    name: str

    class Config():
        orm_mode = True


class ParentsDisplay(BaseModel):
    name: str
    children: CD

    class Config():
        orm_mode = True


class ChildrenBase(BaseModel):
    name: str
    p_id: int


class ChildrenDisplay(BaseModel):
    name: str
    p_id: int

    class Config():
        orm_mode = True

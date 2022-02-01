from typing import List
from datetime import datetime
from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str
    password: str


class UserDisplay(BaseModel):
    username: str
    email: str

    class Config():
        orm_mode = True


class PostBase(BaseModel):
    image_url: str
    image_url_type: str
    caption: str
    creator_id: str


class User(BaseModel):
    username: str

    class Config():
        orm_mode = True


class Comment(BaseModel):
    username: str
    post_id: int
    comment: str


class CommentTest(BaseModel):
    user_id: str
    comment: str

    class Config:
        orm_mode = True


class PostDisplay(BaseModel):
    image_url: str
    image_url_type: str
    caption: str
    timestamp: datetime
    user: User
    comment: List[CommentTest]

    class Config():
        orm_mode = True


class UserAuth(BaseModel):
    username: str
    email: str


class Test(BaseModel):
    username: str
    email: str
    items: list
    comment: list

    class Config:
        orm_mode = True

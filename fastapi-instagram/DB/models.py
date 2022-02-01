from operator import index
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from DB.database import Base
from sqlalchemy.orm import relationship


class DbUser(Base):
    __tablename__ = 'user'
    username = Column(String, primary_key=True)
    email = Column(String)
    password = Column(String)
    items = relationship('DbPost', back_populates='user')
    comment = relationship('DbComment')


class DbPost(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True, index=True)
    image_url = Column(String)
    image_url_type = Column(String)
    caption = Column(String)
    timestamp = Column(DateTime)
    user_id = Column(String, ForeignKey('user.username'))
    user = relationship('DbUser', back_populates='items')
    comment = relationship('DbComment')


class DbComment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, ForeignKey('user.username'))
    post_id = Column(Integer, ForeignKey('post.id'))
    timestamp = Column(DateTime)
    comment = Column(String)

import sqlalchemy
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Column
from db.database import Base


class Parents(Base):
    __tablename__ = 'parents'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    children = relationship('Children')


class Children(Base):
    __tablename__ = 'children'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    parent_id = Column(Integer, ForeignKey('parents.id'))

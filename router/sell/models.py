from sqlalchemy.sql.expression import true
from sqlalchemy import Column, Integer, String
from database import Base

class Sell(Base):
	__tablename__ = 'sell_table'
	id = Column(Integer, primary_key=True, index=True)
	name = Column(String)

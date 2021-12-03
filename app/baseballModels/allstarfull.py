from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()


class AllstarFull(Base):
	__tablename__ = "allstarfull" # required

	ID = Column(Integer, primary_key=True)  # required
	playerID = Column(String(9))
	yearID = Column(Integer)
	gameNum = Column(String(12))
	teamID = Column(String(3))
	GP = Column(Integer)
	startingPos = Column(Integer)

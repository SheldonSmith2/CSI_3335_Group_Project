from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class AwardsManagers(Base): # Awards(Base)
	__tablename__ = "awardsmanagers" # required # "awards"

	ID = Column(Integer, primary_key=True)  # required
	playerID = Column(String(10))
	awardID = Column(String(75))
	yearID = Column(Integer)
	lgID = Column(String(2))
	tie = Column(String(1))
	notes = Column(String(100))

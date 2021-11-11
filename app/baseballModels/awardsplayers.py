from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()


class AwardsPlayers(Base):
	__tablename__ = "awardsplayers" # required

	ID = Column(Integer, primary_key=True)  # required
	playerid = Column(String(9))
	awardID = Column(String(255))
	yearID = Column(Integer)
	lgID = Column(String(2))
	tie = Column(String(1))
	notes = Column(String(100))

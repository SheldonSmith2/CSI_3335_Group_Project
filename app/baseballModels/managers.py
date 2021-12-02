from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()


class Managers(Base):
	__tablename__ = "managers" # required # Change to "manager"

	ID = Column(Integer, primary_key=True)  # required
	playerid = Column(String(9))  # playerID = Column(String(9))
	yearID = Column(Integer)
	teamID = Column(String(3))
	lgID = Column(String(2)) # Remove
	inseason = Column(Integer) # inSeason = Column(Integer)
	G = Column(Integer)  # manager_G = Column(Integer)
	W = Column(Integer)  # manager_W = Column(Integer)
	L = Column(Integer)  # manager_L = Column(Integer)
	teamRank = Column(Integer)
	plyrMgr = Column(String(1))

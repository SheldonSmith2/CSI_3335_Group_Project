from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()


class Fielding(Base):
	__tablename__ = "fielding" # required

	ID = Column(Integer, primary_key=True)  # required
	playerid = Column(String(9))
	yearID = Column(Integer)
	stint = Column(Integer)
	teamID = Column(String(3))
	lgID = Column(String(2))
	POS = Column(String(2))
	G = Column(Integer)
	GS = Column(Integer)
	InnOuts = Column(Integer)
	PO = Column(Integer)
	A = Column(Integer)
	E = Column(Integer)
	DP = Column(Integer)
	PB = Column(Integer)
	WP = Column(Integer)
	SB = Column(Integer)
	CS = Column(Integer)
	ZR = Column(Float)

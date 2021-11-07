from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()


class Pitching(Base):
	__tablename__ = "pitching" # required

	ID = Column(Integer, primary_key=True)  # required
	playerid = Column(String(9))
	yearID = Column(Integer)
	stint = Column(Integer)
	teamID = Column(String(3))
	lgID = Column(String(2))
	W = Column(Integer)
	L = Column(Integer)
	G = Column(Integer)
	GS = Column(Integer)
	CG = Column(Integer)
	SHO = Column(Integer)
	SV = Column(Integer)
	IPouts = Column(Integer)
	H = Column(Integer)
	ER = Column(Integer)
	HR = Column(Integer)
	BB = Column(Integer)
	SO = Column(Integer)
	BAOpp = Column(Float)
	ERA = Column(Float)
	IBB = Column(Integer)
	WP = Column(Integer)
	HBP = Column(Integer)
	BK = Column(Integer)
	BFP = Column(Integer)
	GF = Column(Integer)
	R = Column(Integer)
	SH = Column(Integer)
	SF = Column(Integer)
	GIDP = Column(Integer)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()


class Teams(Base):
	__tablename__ = "teams" # required

	ID = Column(Integer, primary_key=True)  # required
	yearID = Column(Integer, nullable=False)
	lgID = Column(String(2))
	teamID = Column(String(3), nullable=False)
	franchID = Column(String(3))
	divID = Column(String(1))
	teamRank = Column(Integer)
	G = Column(Integer)
	Ghome = Column(Integer)
	W = Column(Integer)
	L = Column(Integer)
	DivWin = Column(Integer)
	WCWin = Column(Integer)
	LgWin = Column(Integer)
	WSWin = Column(Integer)
	R = Column(Integer)
	AB = Column(Integer)
	H = Column(Float)
	# Add 2B, 3B
	HR = Column(Float)
	BB = Column(Integer)
	SO = Column(Integer)
	SB = Column(Integer)
	CS = Column(Integer)
	HBP = Column(Integer)
	SF = Column(Integer)
	RA = Column(Integer)
	ER = Column(Integer)
	ERA = Column(Float)
	CG = Column(Integer)
	SHO = Column(Integer)
	SV = Column(Integer)
	IPouts = Column(Integer)
	HA = Column(Integer)
	HRA = Column(Integer)
	BBA = Column(Integer)
	SOA = Column(Integer)
	E = Column(Integer)
	DP = Column(Integer)
	FP = Column(Integer)
	name = Column(String(50))
	park = Column(String(255))
	attendance = Column(Integer)

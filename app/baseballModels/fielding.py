from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()


class Fielding(Base):
	__tablename__ = "fielding" # required

	ID = Column(Integer, primary_key=True)  # required
	playerid = Column(String(9))  # playerID = Column(String(9))
	yearID = Column(Integer)
	stint = Column(Integer)
	teamID = Column(String(3))
	lgID = Column(String(2)) # Remove
	POS = Column(String(2)) # position = Column(String(2))
	G = Column(Integer)  # f_G = Column(Integer)
	GS = Column(Integer)  # f_GS = Column(Integer)
	InnOuts = Column(Integer)  # f_InnOuts = Column(Integer)
	PO = Column(Integer)  # f_PO = Column(Integer)
	A = Column(Integer)  # f_A = Column(Integer)
	E = Column(Integer)  # f_E = Column(Integer)
	DP = Column(Integer)  # f_DP = Column(Integer)
	PB = Column(Integer)  # f_PB = Column(Integer)
	WP = Column(Integer)  # f_WP = Column(Integer)
	SB = Column(Integer)  # f_SB = Column(Integer)
	CS = Column(Integer)  # f_CS = Column(Integer)
	ZR = Column(Float)  # f_ZR = Column(Integer)

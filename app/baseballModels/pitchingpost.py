from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()


class PitchingPost(Base):
	__tablename__ = "pitchingpost" # required

	ID = Column(Integer, primary_key=True)  # required
	playerid = Column(String(9))  # playerID = Column(String(9))
	yearID = Column(Integer)
	round = Column(String(10))
	teamID = Column(String(3))
	lgID = Column(String(2)) # remove
	W = Column(Integer)  # p_W = Column(Integer)
	L = Column(Integer)  # p_L = Column(Integer)
	G = Column(Integer)  # p_G = Column(Integer)
	GS = Column(Integer)  # p_GS = Column(Integer)
	CG = Column(Integer)  # p_CG = Column(Integer)
	SHO = Column(Integer)  # p_SHO = Column(Integer)
	SV = Column(Integer)  # p_SV = Column(Integer)
	IPouts = Column(Integer)  # p_IPouts = Column(Integer)
	H = Column(Integer)  # p_H = Column(Integer)
	ER = Column(Integer)  # p_ER = Column(Integer)
	HR = Column(Integer)  # p_HR = Column(Integer)
	BB = Column(Integer)  # p_BB = Column(Integer)
	SO = Column(Integer)  # p_SO = Column(Integer)
	BAOpp = Column(Float)  # p_BAOpp = Column(Integer)
	ERA = Column(Float)  # p_ERA = Column(Integer)
	IBB = Column(Integer)  # p_IBB = Column(Integer)
	WP = Column(Integer)  # p_WP = Column(Integer)
	HBP = Column(Integer)  # p_HBP = Column(Integer)
	BK = Column(Integer)  # p_BK = Column(Integer)
	BFP = Column(Integer)  # p_BFP = Column(Integer)
	GF = Column(Integer)  # p_GF = Column(Integer)
	R = Column(Integer)  # p_R = Column(Integer)
	SH = Column(Integer)  # p_SH = Column(Integer)
	SF = Column(Integer)  # p_SF = Column(Integer)
	GIDP = Column(Integer)  # p_GIDP = Column(Integer)

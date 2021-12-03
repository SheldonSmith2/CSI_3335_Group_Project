from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()


class PitchingPost(Base):
	__tablename__ = "pitchingpost" # required

	ID = Column(Integer, primary_key=True)  # required
	playerID = Column(String(9))  # playerID = Column(String(9))
	yearID = Column(Integer)
	round = Column(String(10))
	teamID = Column(String(3))
	#lgID = Column(String(2)) # remove
	p_W = Column(Integer)  # p_W = Column(Integer)
	p_L = Column(Integer)  # p_L = Column(Integer)
	p_G = Column(Integer)  # p_G = Column(Integer)
	p_GS = Column(Integer)  # p_GS = Column(Integer)
	p_CG = Column(Integer)  # p_CG = Column(Integer)
	p_SHO = Column(Integer)  # p_SHO = Column(Integer)
	p_SV = Column(Integer)  # p_SV = Column(Integer)
	p_IPouts = Column(Integer)  # p_IPouts = Column(Integer)
	p_H = Column(Integer)  # p_H = Column(Integer)
	p_ER = Column(Integer)  # p_ER = Column(Integer)
	p_HR = Column(Integer)  # p_HR = Column(Integer)
	p_BB = Column(Integer)  # p_BB = Column(Integer)
	p_SO = Column(Integer)  # p_SO = Column(Integer)
	p_BAOpp = Column(Float)  # p_BAOpp = Column(Integer)
	p_ERA = Column(Float)  # p_ERA = Column(Integer)
	p_IBB = Column(Integer)  # p_IBB = Column(Integer)
	p_WP = Column(Integer)  # p_WP = Column(Integer)
	p_HBP = Column(Integer)  # p_HBP = Column(Integer)
	p_BK = Column(Integer)  # p_BK = Column(Integer)
	p_BFP = Column(Integer)  # p_BFP = Column(Integer)
	p_GF = Column(Integer)  # p_GF = Column(Integer)
	p_R = Column(Integer)  # p_R = Column(Integer)
	p_SH = Column(Integer)  # p_SH = Column(Integer)
	p_SF = Column(Integer)  # p_SF = Column(Integer)
	p_GIDP = Column(Integer)  # p_GIDP = Column(Integer)

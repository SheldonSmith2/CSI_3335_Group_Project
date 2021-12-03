from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()


class Teams(Base):
	__tablename__ = "team" # required

	ID = Column(Integer, primary_key=True)  # required
	yearID = Column(Integer, nullable=False)
	lgID = Column(String(2))
	teamID = Column(String(3), nullable=False)
	franchID = Column(String(3))
	divID = Column(String(1))
	teamRank = Column(Integer)
	team_G = Column(Integer)
	team_G_home = Column(Integer)
	team_W = Column(Integer)
	team_L = Column(Integer)
	DivWin = Column(Integer)
	WCWin = Column(Integer)
	LgWin = Column(Integer)
	WSWin = Column(Integer)
	team_R = Column(Integer)
	team_AB = Column(Integer)
	team_H = Column(Float)
	# Add 2B, 3B
	team_2B = Column(Integer)
	team_3B = Column(Integer)
	team_HR = Column(Float)
	team_BB = Column(Integer)
	team_SO = Column(Integer)
	team_SB = Column(Integer)
	team_CS = Column(Integer)
	team_HBP = Column(Integer)
	team_SF = Column(Integer)
	team_RA = Column(Integer)
	team_ER = Column(Integer)
	team_ERA = Column(Float)
	team_CG = Column(Integer)
	team_SHO = Column(Integer)
	team_SV = Column(Integer)
	team_IPouts = Column(Integer)
	team_HA = Column(Integer)
	team_HRA = Column(Integer)
	team_BBA = Column(Integer)
	team_SOA = Column(Integer)
	name = Column(String(50))

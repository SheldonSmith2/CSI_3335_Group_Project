from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class BattingPost(Base):
	__tablename__ = "battingpost" # required

	ID = Column(Integer, primary_key=True)  # required
	playerid = Column(String(9))
	yearID = Column(Integer)
	round = Column(String(10))
	teamID = Column(String(3))
	lgID = Column(String(2))
	G = Column(Integer)
	AB = Column(Integer)
	R = Column(Integer)
	H = Column(Integer)
	HR = Column(Integer)
	RBI = Column(Integer)
	SB = Column(Integer)
	# Add 2B, 3B
	CS = Column(Integer)
	BB = Column(Integer)
	SO = Column(Integer)
	IBB = Column(Integer)
	HBP = Column(Integer)
	SH = Column(Integer)
	SF = Column(Integer)
	GIDP = Column(Integer)

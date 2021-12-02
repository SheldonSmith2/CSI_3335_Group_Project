from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class BattingPost(Base):
	__tablename__ = "battingpost" # required

	ID = Column(Integer, primary_key=True)  # required
	playerid = Column(String(9))  # playerID = Column(String(9))
	yearID = Column(Integer)  # yearId = Column(Integer)
	round = Column(String(10))
	teamID = Column(String(3))
	lgID = Column(String(2))  # Remove
	G = Column(Integer)  # b_G = Column(Integer)
	AB = Column(Integer)  # b_AB = Column(Integer)
	R = Column(Integer)  # b_R = Column(Integer)
	H = Column(Integer)  # b_H = Column(Integer)
	HR = Column(Integer)  # b_HR = Column(Integer)
	RBI = Column(Integer)  # b_RBI = Column(Integer)
	SB = Column(Integer)  # b_SB = Column(Integer)
	# b_2B = Column(Integer)
	# b_3B = Column(Integer)
	CS = Column(Integer)  # b_CS = Column(Integer)
	BB = Column(Integer)  # b_BB = Column(Integer)
	SO = Column(Integer)  # b_SO = Column(Integer)
	IBB = Column(Integer)  # b_IBB = Column(Integer)
	HBP = Column(Integer)  # b_HBP = Column(Integer)
	SH = Column(Integer)  # b_SH = Column(Integer)
	SF = Column(Integer)  # b_SF = Column(Integer)
	GIDP = Column(Integer)  # b_GIDP = Column(Integer)

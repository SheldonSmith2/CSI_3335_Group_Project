from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()


class SeriesPost(Base):
	__tablename__ = "seriespost" # required

	ID = Column(Integer, primary_key=True)  # required
	yearID = Column(Integer)
	round = Column(String(5))
	teamIDwinner = Column(String(3))
	#lgIDwinner = Column(String(2)) # Remove
	teamIDloser = Column(String(3))
	#lgIDloser = Column(String(2)) # Remove
	wins = Column(Integer)
	loses = Column(Integer)  # loses = Column(Integer)
	ties = Column(Integer)

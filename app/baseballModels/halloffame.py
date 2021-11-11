from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()


class HallofFame(Base):
	__tablename__ = "halloffame" # required

	ID = Column(Integer, primary_key=True)  # required
	playerid = Column(String(9))
	yearid = Column(Integer)
	votedBy = Column(String(64))
	ballots = Column(Integer)
	needed = Column(Integer)
	votes = Column(Integer)
	inducted = Column(String(1))
	category = Column(String(20))
	needed_note = Column(String(25))

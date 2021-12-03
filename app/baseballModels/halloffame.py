from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class HallofFame(Base):
	__tablename__ = "halloffame" # required

	ID = Column(Integer, primary_key=True)  # required
	playerID = Column(String(9))  # playerID = Column(String(9))
	yearID = Column(Integer)  # yearID = Column(Integer)
	votedBy = Column(String(64))
	ballots = Column(Integer)
	needed = Column(Integer)
	votes = Column(Integer)
	inducted = Column(String(1))
	category = Column(String(20))
	note = Column(String(25))  # note = Column(String(25))

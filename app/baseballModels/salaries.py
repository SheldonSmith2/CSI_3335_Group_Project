from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()


class Salaries(Base):
	__tablename__ = "salaries" # required # "Salary"

	ID = Column(Integer, primary_key=True)  # required
	playerid = Column(String(9))  # playerID = Column(String(9))
	yearID = Column(Integer)  # yearId = Column(Integer)
	teamID = Column(String(3))
	lgID = Column(String(2))  # lgId = Column(String(2))
	salary = Column(Float)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()


class Salaries(Base):
	__tablename__ = "salary" # required # "Salary"

	ID = Column(Integer, primary_key=True)  # required
	playerID = Column(String(9))  # playerID = Column(String(9))
	yearId = Column(Integer)  # yearId = Column(Integer)
	teamID = Column(String(3))
	lgId = Column(String(2))  # lgId = Column(String(2))
	salary = Column(Float)

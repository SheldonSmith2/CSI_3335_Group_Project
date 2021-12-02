from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class People(Base):
	__tablename__ = "people" # required

	playerid = Column(String(9),primary_key=True)  # playerID = Column(String(9),primary_key=True)
	birthYear = Column(Integer)
	birthMonth = Column(Integer)
	birthDay = Column(Integer)
	birthCountry = Column(String(255))
	birthState = Column(String(255))
	birthCity = Column(String(255))
	deathYear = Column(Integer)
	deathMonth = Column(Integer)
	deathDay = Column(Integer)
	deathCountry = Column(String(255))
	deathState = Column(String(255))
	deathCity = Column(String(255))
	nameFirst = Column(String(255))
	nameLast = Column(String(255))
	nameGiven = Column(String(255))
	weight = Column(Integer)
	height = Column(Integer)
	bats = Column(String(255))
	throws = Column(String(255))
	debut = Column(String(255)) # Remove

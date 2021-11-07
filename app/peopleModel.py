from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Numeric, create_engine
from battingModel import Batting
import dbconfig as cfg

Base = declarative_base()

import sys

class People(Base):
	__tablename__ = "people" # required

	playerid = Column(String(9),primary_key=True)
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
	debut = Column(String(255))

enginestr = "mysql+pymysql://" +cfg.mysql['user']+":" +cfg.mysql['password']+"@" +cfg.mysql['host']+":3306/" +cfg.mysql['db']

engine = create_engine(enginestr)

Session = sessionmaker(bind=engine)
session = Session()

for p, b in session.query(People, Batting).filter(People.playerid == Batting.playerid, Batting.teamID == sys.argv[1], Batting.yearID == sys.argv[2]).all():
	print(p.nameFirst, p.nameLast, b.R, b.AB)
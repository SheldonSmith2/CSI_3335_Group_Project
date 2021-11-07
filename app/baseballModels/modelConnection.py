from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import app.baseballModels.dbconfig as cfg
from app.baseballModels.people import People
from app.baseballModels.batting import Batting


def createConnection():
	enginestr = "mysql+pymysql://" +cfg.mysql['user']+":" +cfg.mysql['password']+"@" +cfg.mysql['host']+":3306/" +cfg.mysql['db']

	engine = create_engine(enginestr)

	Session = sessionmaker(bind=engine)
	session = Session()
	return session


def getRoster(team, year):
	session = createConnection()
	players = session.query(People, Batting).filter(People.playerid == Batting.playerid, Batting.teamID == team, Batting.yearID == year).all()
	return players
